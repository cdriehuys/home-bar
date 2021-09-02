from django.contrib import admin
from django.contrib.admin.decorators import register
from drinks import models


@register(models.Drink)
class DrinkAdmin(admin.ModelAdmin):
    fields = ("name", "slug", "description")
    list_display = ("name",)
    readonly_fields = ("slug",)
    search_fields = ("name",)
