from django.db import models
from django.utils.text import slugify


class Drink(models.Model):
    description = models.TextField(blank=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, primary_key=True)

    def save(self, *args, **kwargs) -> None:
        # Only generate a new slug if one has not been saved. This avoids
        # breaking existing links.
        if not self.slug:
            self.slug = slugify(self.name)[:50]

        super().save(*args, **kwargs)
