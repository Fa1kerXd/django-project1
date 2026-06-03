from django.shortcuts import render, get_list_or_404, get_object_or_404
# from utils.recipes.factory import make_recipe
from .models import Recipe


def home(request):
    recipe = Recipe.objects.filter(
        is_published=True).order_by('-id')

    return render(
        request,
        "recipes/pages/home.html",
        context={
            "title": "Home",
            "recipes": recipe,
            "message": "Não tem nenhuma receita ativa"
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
            "title": f"{categorys[0].category.name} - Category",
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
