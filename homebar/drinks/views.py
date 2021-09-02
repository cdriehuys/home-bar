from django.shortcuts import render
from django.views.generic.list import ListView

from drinks import models


class DrinksListView(ListView):
    model = models.Drink
