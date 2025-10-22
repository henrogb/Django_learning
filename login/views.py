from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


#criando a view para puxar pra urls depois 

def home(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("entrou")
        else: 
            return render(request, "login/validacao.html", {"erro": "Usuário ou senha incorretos"})
    return render(request, "login/validacao.html")
   
    
@login_required
def entrou(request):
    print("Usuário autenticado?", request.user.is_authenticated)
    return render(request, 'login/entrou.html')