from django.db import models


class Category(models.Model):
    """a Category Model class, e.g. sport, book, hiking"""

    name = models.CharField(max_length=100, unique=True)  # VARCHAR 100

    # blank=True => Formfield can be blank
    # null=True => Database Field is nullable
    sub_title = models.CharField(
        max_length=100, null=True, blank=True)  # optional

    description = models.TextField(null=True, blank=True)  # TEXT
