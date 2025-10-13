from django.contrib import admin
from django.urls import path, include

#associa e organiza os caminnhos do site
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', include('login.urls)') )
]
