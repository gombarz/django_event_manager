from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    """a Category Model class, e.g. sport, book, hiking"""

    name = models.CharField(max_length=100, unique=True)  # VARCHAR 100

    # blank=True => Formfield can be blank
    # null=True => Database Field is nullable
    sub_title = models.CharField(
        max_length=100, null=True, blank=True)  # optional

    description = models.TextField(null=True, blank=True)  # TEXT

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name

    def number_of_events(self) -> int:
        """returns number of events of this category."""
        return self.events.count()


class Event(models.Model):
    """describes an event in the future."""

    class Group(models.IntegerChoices):
        SMALL = 2, "small group"
        MEDIUM = 5, "medium group"
        BIG = 10, "big group"
        LARGE = 20, "large group"
        UNLIMITED = 0, "no limit"

    name = models.CharField(max_length=100)
    sub_title = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text="this is a short summary of the event.")

    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField()
    is_active = models.BooleanField(default=True)  # checkbox
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="events"
    )
    # 1, 5, 10, 20, 50
    min_group = models.IntegerField(choices=Group.choices)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="events"
    )

    def __str__(self) -> str:
        return self.name
