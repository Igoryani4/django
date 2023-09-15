from django.shortcuts import get_object_or_404, render
from .models import Order, Product, User

def customer_orders(request, customer_id):
    customer = get_object_or_404(User, pk=customer_id)
    print(customer)
    orders = Order.objects.filter(customer = customer).order_by('-id')[:5]
    print (orders.filter(pk = id))
    return render(request, 'hw2/customers_orders.html', {'customer': customer, 'order': orders})


def product_by_order(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'hw2/product.html', {'product': product})

def index (request):
    return render(request, 'hw2/index.html')
