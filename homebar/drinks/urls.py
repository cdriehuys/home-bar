from django.urls import path

from drinks import views


urlpatterns = [
    path("", views.DrinksListView.as_view(), name="drinks-list"),
]
