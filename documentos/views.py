#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Documento
from .forms import DocumentoForm
from django.contrib.auth.decorators import login_required

@login_required
def enviar_documento(request):
    if request.method == 'POST':
        form = DocumentoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_documentos')
    else:
        form = DocumentoForm()
    return render(request, 'documentos/enviar_documento.html', {'form': form})

@login_required
def listar_documentos(request):
    documentos = Documento.objects.all()
    return render(request, 'documentos/listar_documentos.html', {'documentos': documentos})
