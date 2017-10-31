from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from marcacaoLaboratorio.models import Marcacao, Laboratorio
from marcacaoLaboratorio.forms import MarcacaoForm

@login_required
def do_index(request):
    lista = Marcacao.objects.all().order_by('-id')
    context = {'lista_marcacao': lista}

    return render(request, 'marcacao/index.html', context)

def cadastrarMarcacao(request):

    formulario = MarcacaoForm(request.POST or None)

    context = {
        'form': formulario
    }

    if request.method == 'POST':
        formulario.cod_user = request.user
        if formulario.is_valid():
            formulario.cod_user = request.user
            formulario.save()
            return redirect('/marcacaoLaboratorio')

    return render(request, 'marcacao/novo.html', context)

def editarMarcacao(request, id):
    marcacao = Marcacao.objects.get(id=id)
    formulario = MarcacaoForm(request.POST or None, instance=marcacao)
    context = {
        'form': formulario
    }
    if request.method == 'POST':
        if formulario.is_valid():
            v = formulario.save(commit=False)
            v.cod_user = request.user
            formulario.save()
            return redirect('/marcacaoLaboratorio')

    return render(request, 'marcacao/novo.html', context)

def excluirMarcacao(request, id):
        marcacao = Marcacao.objects.get(id=id)
        marcacao.delete()
        return redirect('/marcacaoLaboratorio')