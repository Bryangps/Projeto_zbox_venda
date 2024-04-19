from django.contrib import admin
from .models import Estoque, Vendas, Cliente
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(Estoque)
admin.site.register(Vendas)
admin.site.register(Cliente)

