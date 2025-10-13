from django.shortcuts import render


#criando a view para puxar pra urls depois 
def home(request):
    return render(request, 'login/validacao.html')
