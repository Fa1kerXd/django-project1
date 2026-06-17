from django.urls import reverse, resolve
from recipes import views
from .test_recipe_base import RecipeTestBase


class RecipeViewsTest(RecipeTestBase):

    def test_recipes_view_home_is_ok(self):
        view = resolve(reverse('recipes:index'))
        self.assertIs(view.func, views.home)

    def test_recipe_view_home_returns_statuscode_is_200_ok(self):
        response = self.client.get(reverse('recipes:index'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_view_home_loads_correct_template(self):
        response = self.client.get(reverse('recipes:index'))
        self.assertTemplateUsed(response, 'recipes/partials/head.html')

    def test_recipe_template_home_shows_no_recipe_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes:index'))
        print(response.context.get("message"))
        self.assertIn(
            response.context.get("message"),
            response.content.decode("utf-8")
        )

    def test_recipe_home_templates_load_recipes(self):
        self.make_recipe()
        response = self.client.get(reverse('recipes:index'))
        response_content = response.content.decode('utf-8')
        self.assertIn('Recipe Title', response_content)

    def test_recipe_category_templates_load_recipes(self):
        needed_title = 'Category name'
        self.make_recipe(title=needed_title)
        response = self.client.get(reverse('recipes:category',args=(1, )) )
        response_content = response.content.decode('utf-8')
        self.assertIn(needed_title, response_content)

    def test_recipes_view_category_is_ok(self):
        view = resolve(
            reverse("recipes:category", args=[1])
        )
        self.assertIs(view.func, views.category)

    def test_recipes_category_function_returns_404_if_no_category_found(self):
        response = self.client.get(reverse('recipes:category', args=[200]))
        self.assertEqual(response.status_code, 404)

    def test_recipes_view_recipe_is_ok(self):
        view = resolve(
            reverse('recipes:recipe', args=[3])
        )
        self.assertIs(view.func, views.recipe)

    def test_recipes_recipe_function_returns_404_if_no_recipe_found(self):
        response = self.client.get(reverse('recipes:recipe', args=[3]))
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_templates_load_correct_recipe(self):
        needed_title = 'Is a detail page'
        self.make_recipe(title=needed_title)
        response = self.client.get(reverse('recipes:recipe', kwargs={"id": 1}))
        response_content = response.content.decode('utf-8')
        self.assertIn(needed_title, response_content)

    def test_home_template_dont_show_if_not_published(self):
        self.make_recipe(is_published=False)
        response = self.client.get(reverse('recipes:index'))
        print(response.context.get("message"))
        self.assertIn(
            response.context.get("message"),
            response.content.decode("utf-8")
        )

    def test_recipe_category_template_dont_loads_recipes_not_published(self):
        recipe = self.make_recipe(is_published=False)
        response = self.client.get(reverse("recipes:recipe", kwargs={"id": recipe.category.id}))
        self.assertEqual(response.status_code, 404)
    
    def test_recipe_detail_template_dont_loads_recipes_not_published(self):
        recipe = self.make_recipe(is_published=False)
        response = self.client.get(reverse("recipes:recipe", kwargs={"id": recipe.id}))
        self.assertEqual(response.status_code, 404)
    
    def test_recipe_search_view_uses_correct_function(self):
        resolved = resolve(reverse('recipes:search'))
        self.assertIs(resolved.func, views.search)

    def test_recipe_search_loads_correct_template(self):
        response = self.client.get(reverse("recipes:search")+'?q=teste')
        self.assertTemplateUsed(response, 'recipes/pages/search-page.html')

    def test_recipe_search_view_return_http_response_status_code_404(self):
        response = self.client.get(reverse('recipes:search'))
        self.assertEqual(response.status_code, 404)
    
    def test_recipe_search_term_is_on_page_title_and_escaped(self):
        response = self.client.get(reverse('recipes:search')+'?q="Teste"')
        self.assertIn('&quot;Teste&quot;', response.content.decode('utf-8'))

    def test_search_can_find_recipe_by_title(self):
        title_one = 'Title one'
        title_two = 'Title two'

        recipe_one = self.make_recipe(
            slug='one', title=title_one, author_data={'username': 'one'}
        )

        recipe_two = self.make_recipe(
            slug='two', title=title_two, author_data={'username': 'two'}
        )
        search_link = reverse('recipes:search')
        response1 = self.client.get(f'{search_link}?q={title_one}')
        response2 = self.client.get(f'{search_link}?q={title_two}')
        response_both = self.client.get(f'{search_link}?q=Title')
        
        self.assertIn(recipe_one, response1.context['recipes'])
        self.assertNotIn(recipe_one, response2.context['recipes'])
        self.assertIn(recipe_two, response2.context['recipes'])
        self.assertNotIn(recipe_two, response1.context['recipes'])
        self.assertIn(recipe_one, response_both.context['recipes'])
        self.assertIn(recipe_two, response_both.context['recipes'])

        