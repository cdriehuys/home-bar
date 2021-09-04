from django.db.models.expressions import F
from django.db.models.query import QuerySet
from django.db.models.query_utils import Q
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.db.models import Count

from drinks import models


class DrinkDetailView(DetailView):
    model = models.Drink


class DrinksListView(ListView):
    model = models.Drink

    def get_queryset(self) -> QuerySet[models.Drink]:
        queryset = super().get_queryset()

        # Exclude recipes that are missing an ingredient.
        creatable_recipes = models.DrinkRecipe.objects.exclude(
            ingredients__in_stock=False
        )

        # Only show drinks that have a creatable recipe.
        queryset = queryset.filter(recipe__in=creatable_recipes).distinct()

        return queryset
