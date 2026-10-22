from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Enderecos
from .forms import EnderecosForm

def cadastrar_enderecos(request):
    if request.method == 'POST':
        form = EnderecosForm(request.POST)

        if form.is_valid():
            endereco = form.save(commit=False)
            endereco.tutor = request.user.tutor
            endereco.save()
            messages.success(request, 'Endereço cadastrado com sucesso!')
        
            return redirect('=== Mude para a rota para onde o usuário deve ir após salvar ===')
        
        else:
            messages.error(request, 'Erro ao cadastrar endereço. Verifique os campos.')

    else:
        form = EnderecosForm()

    return render(request, 'enderecos/<cadastrar_endereco.html>', {'form': form})

# =====   EDIÇÃO DE ENDEREÇO =====

def editar_endereco(request, id):
    endereco = get_object_or_404(Enderecos, int=id)

    if request.method == 'POST':
        form = EnderecosForm(request.POST, instance=endereco)

        if form.is_valid():
            form.save()
            messages.success(request, 'Endereço atualizado com sucesso!')

            return redirect('lista_enderecos')

    else:
        form = EnderecosForm(instance=endereco)

    return render(request, 'enderecos/<cadastrar_endereco.html>', {'form': form})

# =====   EXCLUSAO DE ENDERECO    =====

def excluir_endereco(request, id):
    endereco = get_object_or_404(Enderecos, int=id)

    if request.method == 'POST':
        endereco.delete()
        messages.success(request, 'Endereço excluído com sucesso!')

        return redirect('lista_enderecos')

    return render(request, 'enderecos/<confirmar_exclusao.html>', {'endereco': endereco})