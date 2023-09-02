from django.core.management.base import BaseCommand
from hw2.models import Product


class Command(BaseCommand):
    help = "Create products."
    def handle(self, *args, **kwargs):
        product = Product(name='laptop', price= 123456.78, description = 'it is so high power laptoh bla bla bla')
        # product = Product(name='phone', price= 345.67, description = 'it is so high power phone')
        # product = Product(name='tv', price= 4567.89, description = 'it is so beautiful color tv')
        product.save()
        self.stdout.write(f'{product}')