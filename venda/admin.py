from django.contrib import admin
from .models import Estoque, Venda, Cliente
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(Estoque)
admin.site.register(Venda)
admin.site.register(Cliente)

