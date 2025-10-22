from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

#cria o caminho dentro do app
urlpatterns = [
    path('', views.home, name='home'),
    path('entrou/', views.entrou, name='entrou'),
]