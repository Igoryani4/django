from urllib import response
from django.core.management.base import BaseCommand
from django.shortcuts import redirect
from hw2.models import Order, User, Product


# class Command(BaseCommand):
#     help = "Create order."
#     def handle(self, *args, **kwargs):
#         order = Order.objects.create(customer = 1, products = 1)
#         order.save()
#         self.stdout.write(f'{order}')

""" customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2) """
        

class Command(BaseCommand):
    help = "Create order."
    def handle(self, *args, **kwargs):
        
        # Get customer data from form
        customer_id = 2
        products_id = 3
        products_id1 = 1
        price = Product.objects.filter(pk=products_id).first()
        total_price = price.price
        """ def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        user = User.objects.filter(pk=pk).first()
        user.name = name
        user.save()
        self.stdout.write(f'{user}') """

        # Create new customer instance
        # user = User.objects.create(id=id)

        # Create new order instance and assign customer instance to foreign key field
        order = Order.objects.create(customer_id=customer_id, 
                                     products_id = products_id, total_price = total_price)
        order = Order.objects.create(customer_id=customer_id, 
                                     products_id = products_id1, total_price = total_price)
        order.save()
        self.stdout.write(f'{order}')
    # Redirect to order detail page
    # return redirect('order_detail', order_id=order.id)