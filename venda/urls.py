from django.urls import path
from .views import Homepage, Login


urlpatterns = [
    path('', Homepage.as_view()),
    path('login/', Login.as_view())
]
