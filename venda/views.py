from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from .forms import CadastroBebidaForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def home(request):
    return render(request, 'homepage.html')


def cadastro_bebida(request):
    if request.method == 'POST':
        nome = request.POST.get('nome-bebida')
        tipo = request.POST.get('tipo-bebida')
        qtd = int(request.POST.get('unidade-caixa')) * int(request.POST.get('unidade'))
        preco = request.POST.get('gasto-caixa')
        total_gasto = request.POST.get('venda-unidade')
        print(nome, tipo, qtd, preco, total_gasto)

        return render(request, 'homepage.html')
    else:
        return HttpResponseRedirect(reverse('meu-form'))




# class Homepage(FormView):
#     template_name = 'homepage.html'
#     form_class = CadastroBebidaForm




# class Login(TemplateView):
#     template_name = 'login.html'