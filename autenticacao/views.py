from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib import messages

from autenticacao.forms import NovoUsuarioForm

# Create your views here.
def logar(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            senha = form.cleaned_data.get('password')
            user = authenticate(username = usuario, password = senha)
            if user is not None:
                login(request, user)
                messages.info (request, f"Seja bem vindo, {user.username}" )
                return redirect ("index")
            else:
                messages.error(request,"Usuário ou senha inválido. ")
        else:
             messages.error(request,"Usuário ou senha inválido. ")
    form = AuthenticationForm()    
    return render(request, 'login.html', {'login_form': form})

def sair(request):
    logout(request)
    return redirect('index')


def registro(request):
    if request.method == "POST":
        form = NovoUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, F"Usuário {user.username} criado com sucesso.")
            return redirect("index")

        if len(request.POST['username'])>150:
            messages.error(request, "Campo com caracteres acima do permitido")
        
        if len(request.POST['password1'])<8:
            messages.error(request, "Senha muito curta, informe ao menos 8 caracteres")
        
        if request.POST['password1'].isnumeric():
            messages.error(request, "Não informe uma senha somente com nùmeros")
        
        if request.POST['password1'] != request.POST['password2']:
            messages.error(request, "As senhas estão diferentes.")

        #messages.error(request, "Erro ao cadastrar")
    form = NovoUsuarioForm()
    return render(request, 'registro.html', {'usuario_form': form})

