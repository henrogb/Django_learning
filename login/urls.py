from django.urls import path
from . import views

#cria o caminho dentro do app
urlpatterns = [
    path('', views.home, name='home')
]