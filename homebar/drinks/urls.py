from django.urls import path

from drinks import views


urlpatterns = [
    path("drinks/<slug>/", views.DrinkDetailView.as_view(), name="drink-detail"),
    path("", views.DrinksListView.as_view(), name="drink-list"),
]
