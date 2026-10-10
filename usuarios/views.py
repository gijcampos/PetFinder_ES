from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .forms import CadastroForm

# ===== Arquivo que lida com as criações e validações dos formularios =====

def cadastro(request):
    # Verifique se o usuario apertou Enter
    if request.method == 'POST': 
        form = CadastroForm(request.POST)
        # Executa automaticamente as validações pelo próprio Django
        if form.is_valid():
            usuario = form.save(commit = False)
            #Pega a senha e a transforma em hash
            usuario.senha = make_password(form.cleaned_data['senha'])
            usuario.save()

            #Redireciona o Cadastro para o Login
            return redirect('login')

    else:
        form = CadastroForm()

    return render(request, 'usuarios/<tela_do_cadastro.html>', {'form': form})