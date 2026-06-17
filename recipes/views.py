from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http.response import Http404
# from utils.recipes.factory import make_recipe
from .models import Recipe
from django.db.models import Q
from django.core.paginator import Paginator
from utils.pagination import make_pagination_range


def home(request):
    recipe = Recipe.objects.filter(
        is_published=True).order_by('-id')
    try:
        current_page = int(request.GET.get('page', 1))
    except ValueError:
        current_page = 1
    paginator = Paginator(recipe, 9)
    page_obj = paginator.get_page(current_page)

    pagination_range = make_pagination_range(
        page_range=paginator.page_range,
        qty_page=20,
        current_page=current_page,
    )
    return render(
        request,
        "recipes/pages/home.html",
        context={
            "title": "Home",
            "recipes": page_obj,
            "message": "Não tem nenhuma receita ativa",
            'pagination_range': pagination_range,
        }
        )


def category(request, category_id):
    categorys = get_list_or_404(
        Recipe.objects.filter(
            is_published=True, category__id=category_id).order_by('-id')
    )
    return render(
        request,
        "recipes/pages/categories.html",
        context={
            "title": f"{categorys[0].category.name} - Category",  # type: ignore # noqa: E501
            "recipes": categorys,
        }
        )


def recipe(request, id):
    recipe = get_object_or_404(Recipe.objects.filter(id=id, is_published=True))
    return render(
        request,
        "recipes/pages/recipe-view.html",
        context={
            "title": "Recipe",
            "recipe": recipe,
            "is_detail_page": True,
        }
    )


def search(request):
    search_input = request.GET.get("q", "").strip()
    if not search_input:
        raise Http404()
    recipes = Recipe.objects.filter(
        Q(
            Q(title__icontains=search_input) |
            Q(description__icontains=search_input) |
            Q(author__username__icontains=search_input) |
            Q(category__name__icontains=search_input) |
            Q(preparation_steps__icontains=search_input)
        ), is_published=True
    ).order_by('-id')
    context = {
        'recipes': recipes,
        'search_show': search_input,
        'title': search_input,
        'message': 'Não foi encontrado nada na busca.'

    }
    return render(
        request,
        "recipes/pages/search-page.html",
        context
    )
