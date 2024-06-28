from django.contrib import admin
from .models import Product, Category, Client, Stock, Shopping
from django.contrib.auth.admin import UserAdmin
# Register your models here.


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Client)
admin.site.register(Stock)
admin.site.register(Shopping)
