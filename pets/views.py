from django.shortcuts import render, redirect, get_object_or_404
from .models import Pets
from .forms import PetsForm

def listar_pets(request):
    pets = Pets.objects.all()
    return render(request, 'pets/<listar_pets.html>', {'pets': pets})

def cadastrar_pets(request):
    if request.method == 'POST':
        form = PetsForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("listar_pets")

    else:
        form = PetsForm()
    return render(request, 'pets/cadastrar_pets.html', {'form': form})