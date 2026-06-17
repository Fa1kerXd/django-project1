from .test_recipe_base import RecipeTestBase
from django.core.exceptions import ValidationError
from parameterized import parameterized
from recipes.models import Recipe


class RecipeModelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()

    def make_recipe_no_defaults(self):
        recipe = Recipe(
            category=self.make_category(name='Category'),
            author=self.make_author(username='newuser'),
            title='Recipe Title',
            description="Recipe Description",
            slug='recipe-slug',
            preparation_time=15,
            preparation_time_unit='Minutes',
            servings=2,
            servings_unit='Porção',
            preparation_steps='Recipe Preparation Steps',
        )
        self.recipe.full_clean()
        self.recipe.save()
        return recipe
    
    @parameterized.expand([
            ('title', 65),
            ('description', 165),
            ('preparation_time_unit', 65),
            ('servings_unit', 65),]    
    )
    def test_recipe_fields_max_length(self, field, max_length):
        setattr(self.recipe, field, 'A' * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()
    
    def test_recipe_preparation_steps_is_html_not_false_by_default(self):
        recipe = self.make_recipe_no_defaults()
        self.assertFalse(recipe.preparation_steps_is_html)
    
    def test_recipe_is_published_not_false_by_default(self):
        recipe = self.make_recipe_no_defaults()
        self.assertFalse(recipe.is_published)
    
    def test_recipe_title_representation(self):
        self.recipe.title = 'Test Representation'
        self.recipe.full_clean()
        self.recipe.save()
        self.assertEqual(self.recipe.title, 'Test Representation')

    