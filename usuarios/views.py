from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForm

def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/lista_usuarios.html', {'usuarios': usuarios})

def cadastrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
          
            usuario.save()
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'usuarios/cadastrar_usuario.html', {'form': form})
