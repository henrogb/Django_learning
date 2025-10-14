from django.contrib import admin
from django.urls import path, include
from . import views

#associa e organiza os caminnhos do site
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', include('login.urls') )
]
