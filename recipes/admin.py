from django.contrib import admin
from .models import Category, Recipe
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'
    list_display = 'id', 'name',
    ordering = '-pk',
    list_display_links = 'name',


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'
    list_display_links = 'title',
    list_display = 'id', 'title', 'is_published',
    ordering = '-pk',
