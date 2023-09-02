""" Поля модели «Клиент»:
— имя клиента
— электронная почта клиента
— номер телефона клиента
— адрес клиента
— дата регистрации клиента """

from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField(max_length=11)
    password = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return f'Username: {self.name},phone number: {self.phone_number},\
                email: {self.email}, age:{self.age}'
    
    """ Поля модели «Товар»:
— название товара
— описание товара
— цена товара
— количество товара
— дата добавления товара """

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    date_add_product = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'name: {self.name}, price: {self.price}, descriptoin: {self.description}'


""" оля модели «Заказ»:
— связь с моделью «Клиент», указывает на клиента, сделавшего заказ
— связь с моделью «Товар», указывает на товары, входящие в заказ
— общая сумма заказа
— дата оформления заказа """


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'customer: {self.customer}, product: {self.products}, total price: {self.total_price}'