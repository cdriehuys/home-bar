from django.db import models
from django.utils.text import slugify


class Drink(models.Model):
    description = models.TextField(blank=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, primary_key=True)

    class Meta:
        ordering = ("name",)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs) -> None:
        # Only generate a new slug if one has not been saved. This avoids
        # breaking existing links.
        if not self.slug:
            self.slug = slugify(self.name)[:50]

        super().save(*args, **kwargs)


class DrinkRecipe(models.Model):
    drink = models.ForeignKey(
        "drinks.Drink",
        on_delete=models.CASCADE,
        related_name="recipes",
        related_query_name="recipe"
    )
    ingredients = models.ManyToManyField(
        "drinks.Ingredient",
        blank=True,
        related_name="recipes",
        related_query_name="recipe",
    )
    notes = models.TextField(blank=True)
    variation = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.drink} - {self.variation}"


class Ingredient(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    in_stock = models.BooleanField(default=True)

    class Meta:
        ordering = ("name",)

    def __str__(self) -> str:
        return self.name
