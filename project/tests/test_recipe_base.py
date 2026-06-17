from django.test import TestCase
from recipes.models import Category, Recipe, User


class RecipeTestBase(TestCase):

    def make_category(self, name='Category'):
        return Category.objects.create(name=name)

    def make_author(
            self,
            first_name='Augusto',
            last_name='Cesar',
            username='augustoCesar',
            email='augustocesar@gmail.com',
            password='Senha202051!'
            ):
        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password
        )
    
    def make_recipe(
            self,
            category_data=None,
            author_data=None,
            title='Recipe Title',
            description="Recipe Description",
            slug='recipe-slug',
            preparation_time=15,
            preparation_time_unit='Minutes',
            servings=2,
            servings_unit='Porção',
            preparation_steps='Recipe Preparation Steps',
            preparation_steps_is_html=False,
            created_at='',
            updated_at='',
            is_published=True,
            ):
        if category_data is None:
            category_data = {}
        if author_data is None:
            author_data = {}
        return Recipe.objects.create(
            category=self.make_category(**category_data),
            author=self.make_author(**author_data),
            title=title,
            description=description,
            slug=slug,
            preparation_time=preparation_time,
            preparation_time_unit=preparation_time_unit,
            servings=servings,
            servings_unit=servings_unit,
            preparation_steps=preparation_steps,
            preparation_steps_is_html=preparation_steps_is_html,
            created_at=created_at,
            updated_at=updated_at,
            is_published=is_published,
        )