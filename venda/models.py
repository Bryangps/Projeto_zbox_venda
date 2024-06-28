from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    id_user = models.ForeignKey(User, related_name='product_user', on_delete=models.CASCADE, null=True, blank=True)
    category_id = models.ForeignKey(Category, related_name='product_cate', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)
    purchase_price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    data_criacao = models.DateField(default=datetime.today)

    def __str__(self):
        return self.name


class Stock(models.Model):
    id_user = models.ForeignKey(User, related_name='stock_user', on_delete=models.CASCADE, null=True)
    product_id = models.OneToOneField(Product, related_name='stock_product', on_delete=models.CASCADE, null=True)
    stock_quantity = models.IntegerField(default=0)
    data_cadastro = models.DateField(default=datetime.today)

    def __str__(self):
        return f'{str(self.stock_quantity)} - {self.product_id}'


class Client(models.Model):
    user_id = models.ForeignKey(User, related_name='client', on_delete=models.CASCADE, null=True)
    client_name = models.CharField(max_length=50)

    def __str__(self):
        return self.client_name


class Shopping(models.Model):
    client_id = models.ForeignKey(Client, related_name='shopping_client', on_delete=models.CASCADE, null=True)
    product_id = models.OneToOneField(Product, related_name='shopping_product', on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=0)
    unit_price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    total_price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=25)
    purchase_status = models.BooleanField(default=False)
    purchase_date = models.DateField(default=datetime.today)

    def __str__(self):
        return f'{self.client_id} comprou  {self.product_id} '
