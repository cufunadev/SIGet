from django.shortcuts import render, redirect, get_object_or_404
from .models import Terreno
from .forms import TerrenoForm

# Listar todos os terrenos
def lista_terrenos(request):
    terrenos = Terreno.objects.all()
    return render(request, 'terrenos/lista_terrenos.html', {'terrenos': terrenos})

# Cadastrar um novo terreno
def cadastrar_terreno(request):
    if request.method == 'POST':
        form = TerrenoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_terrenos')
    else:
        form = TerrenoForm()
    return render(request, 'terrenos/cadastrar_terreno.html', {'form': form})

# Editar um terreno existente
def editar_terreno(request, pk):
    terreno = get_object_or_404(Terreno, pk=pk)
    if request.method == 'POST':
        form = TerrenoForm(request.POST, instance=terreno)
        if form.is_valid():
            form.save()
            return redirect('lista_terrenos')
    else:
        form = TerrenoForm(instance=terreno)
    return render(request, 'terrenos/editar_terreno.html', {'form': form})

# Excluir um terreno
def excluir_terreno(request, pk):
    terreno = get_object_or_404(Terreno, pk=pk)
    if request.method == 'POST':
        terreno.delete()
        return redirect('lista_terrenos')
    return render(request, 'terrenos/excluir_terreno.html', {'terreno': terreno})
