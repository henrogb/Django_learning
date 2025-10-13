from django.db import models

#modelo de tabela a ser criada
class Login(models.Model):
    login = models.CharField(max_length=255)
    email = models.CharField(max_length=200)
    
