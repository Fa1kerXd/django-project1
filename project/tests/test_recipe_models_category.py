from .test_recipe_base import RecipeTestBase
from django.core.exceptions import ValidationError


class RecipeModelCategoryTest(RecipeTestBase):
    def setUp(self) -> None:
        self.category = self.make_category(name='Category')
        return super().setUp()

    def test_recipe_model_category_representation(self):
        self.assertEqual(str(self.category), 'Category')
    
    def test_recipe_model_category_name_field_max_length_is_65(self):
        self.category.name = 'A' * 70
        with self.assertRaises(ValidationError):
            self.category.full_clean()