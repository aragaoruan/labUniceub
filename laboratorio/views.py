from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from laboratorio.models import Laboratorio
from laboratorio.forms import LaboratorioForm

@login_required
def indexLaboratorio(request):
    lista_laboratorio = Laboratorio.objects.all().order_by('-id')
    context = {
        'lista_laboratorio': lista_laboratorio
    }
    return render(request, 'laboratorio/index.html', context)

@login_required
def cadastrarLaboratorio(request):
    formulario = LaboratorioForm(request.POST or None)

    context = {
        'form': formulario
    }
    if request.method == 'POST':
        if formulario.is_valid():
            formulario.save()
            return redirect('/laboratorio')

    return render(request, 'laboratorio/novo.html', context)

def editarLaboratorio(request, id):
    laboratorio = Laboratorio.objects.get(id=id)
    formulario = LaboratorioForm(request.POST or None, instance=laboratorio)

    context = {
        'form': formulario
    }

    if request.method == 'POST':
        if formulario.is_valid():
            formulario.save()
            return redirect('/laboratorio')

    return render(request, 'laboratorio/novo.html', context)

def excluirLaboratorio(request, id):
    laboratotio = Laboratorio.objects.get(id=id)
    laboratotio.delete()
    return redirect('/laboratorio')


