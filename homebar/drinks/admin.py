from typing import TYPE_CHECKING

from django.contrib import admin
from django.contrib.admin.decorators import register
from django.db.models import Count
from django.db.models.query import QuerySet
from django.http.request import HttpRequest

from drinks import models


@register(models.Drink)
class DrinkAdmin(admin.ModelAdmin):
    fields = ("name", "slug", "description")
    list_display = ("name", "recipe_count")
    readonly_fields = ("slug",)
    search_fields = ("name",)

    def get_queryset(self, request: HttpRequest) -> QuerySet:
        queryset = super().get_queryset(request)

        return queryset.annotate(recipe_count=Count("recipe"))

    def recipe_count(self, obj) -> int:
        return obj.recipe_count


@register(models.DrinkRecipe)
class DrinkRecipeAdmin(admin.ModelAdmin):
    fields = ("drink", "variation", "notes", "ingredients")
    list_display = ("drink", "variation")
    search_fields = ("drink__name", "variation")


@register(models.Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    fields = ("name", "in_stock")
    list_display = ("name", "in_stock")
    search_fields = ("name",)
