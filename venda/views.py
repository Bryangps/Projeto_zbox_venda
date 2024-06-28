from django.shortcuts import render, redirect
from django.urls import reverse
from venda.models import Product, Stock, User, Category


def home(request):
    if request.method == 'POST':
        name = request.POST.get('nome-produto')
        categoria = request.POST.get('categoria')
        quantidade = request.POST.get('quantidade')
        total_gasto = request.POST.get('total-gasto')
        preco_venda = request.POST.get('preco-venda')

        category = Category.objects.create(name=categoria)
        product = Product.objects.create(id_user=request.user, name=name, category_id=category,
                                         purchase_price=total_gasto, sale_price=preco_venda)
        stock = Stock.objects.create(id_user=request.user, product_id=product, stock_quantity=quantidade)
        cate = Category.objects.all()

    return render(request, 'venda/pages/home.html', context={'category': cate})






