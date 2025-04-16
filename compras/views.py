#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import SolicitacaoCompraForm
from .models import SolicitacaoCompra
from django.contrib.auth.decorators import login_required

@login_required
def solicitar_compra(request):
    if request.method == 'POST':
        form = SolicitacaoCompraForm(request.POST)
        if form.is_valid():
            solicitacao = form.save(commit=False)
            solicitacao.usuario = request.user  # pega o usuário logado
            solicitacao.save()
            return redirect('minhas_solicitacoes')
    else:
        form = SolicitacaoCompraForm()

    return render(request, 'compras/solicitar_compra.html', {'form': form})

@login_required
def minhas_solicitacoes(request):
    solicitacoes = SolicitacaoCompra.objects.filter(usuario=request.user)
    return render(request, 'compras/minhas_solicitacoes.html', {'solicitacoes': solicitacoes})
