from django.test import TestCase
from django.urls import reverse


class RecipesURLsTest(TestCase):
    def test_recipe_index_url_is_ok(self):
        home_url = reverse('recipes:index')
        self.assertEqual(home_url, '/')

    def test_recipe_category_doces_caseiros_is_ok(self):
        category_url = reverse('recipes:category', args=[2])
        self.assertEqual(category_url, '/recipes/category/2/', msg='Categoria: Doces Caseiros')  # noqa: E501

    def test_recipe_category_cafe_da_manha_is_ok(self):
        category_url = reverse("recipes:category", args=[1])
        self.assertEqual(category_url, '/recipes/category/1/', msg='Categoria: Cafe da Manha')  # noqa: E501

    def test_recipe_recipes_is_ok(self):
        recipe_url = reverse('recipes:recipe', args=[3])
        self.assertEqual(recipe_url, '/recipes/3/', msg='Recipe: Dentro da receita 3')  # noqa: E501

    def test_recipe_url_search_is_ok(self):
        url = reverse('recipes:search')
        self.assertEqual(url, '/recipes/search/')

