import random
from datetime import timedelta
import factory
from django.utils import timezone 

from . import models

categories = [
    "Cooking",
    "Books",
    "Sports",
    "Fun",
    "Flying",
]

class CategoryFactory(factory.django.DjangoModelFactory):
    """Create a Category object out of specified names."""
    class Meta:
        model = models.Category
    
    name = factory.Iterator(categories)
    sub_title = factory.Faker("sentence")
    description = factory.Faker("paragraph", nb_sentences=6)

class EventFactory(factory.django.DjangoModelFactory):
    """Create an random Event object"""
    class Meta:
        model = models.Event

    name = factory.Faker("sentence")
    sub_title = factory.Faker("sentence")
    description = factory.Faker("paragraph", nb_sentences=6)
    min_group = factory.LazyAttribute(lambda _: random.choice(
        list(models.Event.Group)
    ))
    date = factory.Faker(
        "date_time_between",
        start_date=timezone.now() + timedelta(days=1),
        end_date=timezone.now() + timedelta(days=60),
        tzinfo=timezone.get_current_timezone()                
    )
