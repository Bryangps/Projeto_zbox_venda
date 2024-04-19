from django.urls import path
from .views import home, cadastro_bebida


urlpatterns = [
    path('', home, name='home'),
    # path('login/', Login.as_view())
    path('form/', cadastro_bebida, name='form'),

]
