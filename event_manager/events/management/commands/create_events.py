import random
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from events.models import Category, Event
from events.factories import CategoryFactory, EventFactory

NUM_CATEGORIES = 5
NUM_EVENTS = 20

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        print("Deleting events data ...")

        users = get_user_model().objects.all()
        if not users:
            print("there have to be users in the system")
            raise SystemExit(1)

        for model in [Category, Event]:
            model.objects.all().delete()

        print("Objects successfully deleted ...")
        print("Creating event data ...")
        #for _ in range(5):
        #    cat = CategoryFactory()
        categories = CategoryFactory.create_batch(NUM_CATEGORIES)

        for _ in range(NUM_EVENTS):
            EventFactory(author=random.choice(users), 
                        category=random.choice(categories))

        