from django.urls import path
from .views import product_by_order, customer_orders


urlpatterns = [
    path('customer/<int:customer_id>/', customer_orders, name='customer_orders'),
    path('product/<int:product_id>/', product_by_order, name='product_by_orders'),
    ]