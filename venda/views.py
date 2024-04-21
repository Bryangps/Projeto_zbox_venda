from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Estoque

# Create your views here.


def home(request):
    return render(request, 'homepage.html')


def cadastro_bebida(request):
    if request.method == 'POST':
        nome = request.POST.get('nome-bebida')
        tipo = request.POST.get('tipo-bebida')
        qtd = int(request.POST.get('unidade-caixa')) * int(request.POST.get('unidade'))
        preco = request.POST.get('gasto-caixa')
        if preco in 'R$':
            preco = preco.replace('R$', ' ')
            print(preco)
            preco = float(preco)
        total_gasto = request.POST.get('venda-unidade')
        if total_gasto in 'R$':
            total_gasto = total_gasto.replace('R$', ' ')
            total_gasto = float(total_gasto)
        print(nome, tipo, qtd, preco, total_gasto)
        estoque = Estoque(nome=nome, tipo_produto=tipo, qtd=qtd, preco_vendas=preco, total_gasto=total_gasto)
        estoque.save()
        return render(request, 'homepage.html')
    else:
        return HttpResponseRedirect(reverse('meu-form'))




# class Homepage(FormView):
#     template_name = 'homepage.html'
#     form_class = CadastroBebidaForm




# class Login(TemplateView):
#     template_name = 'login.html'