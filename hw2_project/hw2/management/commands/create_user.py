from django.core.management.base import BaseCommand
from hw2.models import User


class Command(BaseCommand):
    help = "Create user."
    def handle(self, *args, **kwargs):
        user = User(name='John', email='john@example.com', phone_number = 79525678798, password='secret', age=25)
        # user = User(name='Neo', email='neo@example.com',phone_number = 79213456798, password='secret', age=58)
        # user = User(name='Maks', email='captain@example.com', phone_number = 79348765698, password='secret', age=35)
        user.save()
        self.stdout.write(f'{user}')