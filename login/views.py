from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm 


#criando a view para puxar pra urls depois 

def home(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('entrou')
        else: 
            return render(request, "login/validacao.html", {"erro": "Usuário ou senha incorretos"})
    return render(request, "login/validacao.html")


def registro(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})
   
    
@login_required
def entrou(request):
    return render(request, 'login/entrou.html')


def logout_user(reuquest):
    logout(reuquest)
    return redirect('home')