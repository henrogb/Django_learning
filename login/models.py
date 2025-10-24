from django.db import models

#modelo de tabela a ser criada
class RegistroUsuario(models.Model):
    login = models.CharField(max_length=255)
    senha = models.CharField(max_length=200)
    
