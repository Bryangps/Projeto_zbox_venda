from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class Homepage(TemplateView):
    template_name = 'homepage.html'



class Login(TemplateView):
    template_name = 'login.html'