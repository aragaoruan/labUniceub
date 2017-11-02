# importando o render (renderizar pagina) e redirect (redirecionar pagina)
from django.shortcuts import render, redirect
# importando login_required (para verificar se o usuario esta logado)
from django.contrib.auth.decorators import login_required
# importando a model Laboratorio
from laboratorio.models import Laboratorio
#importando o formulario LaboratorioForm
from laboratorio.forms import LaboratorioForm

"""
@login_required verifica se o usuario esta logado 
caso sim entra na funcao se não estiver logado 
ele manda para a raiz do projeto
(FOI DEFINIDO QUE IRA MANDAR PARA A RAIZ DO PROJETO 
    NO ARQUIVO settings.py linha 139 - LOGIN_URL = '/' )
"""
@login_required
def indexLaboratorio(request):
    # lista todos os laboratorio com ordem do id
    lista_laboratorio = Laboratorio.objects.all().order_by('-id')

    # transforma a busca em um JSON para mandar para o HTML
    context = {
        'lista_laboratorio': lista_laboratorio
    }

    # renderiza o html com o mandando o JSON como parametro
    return render(request, 'laboratorio/index.html', context)

@login_required
def cadastrarLaboratorio(request):
    # cria um formulario definodo no arquivo forms.py
    formulario = LaboratorioForm(request.POST or None)

    # transforma o form em um JSON para mandar para o HTML
    context = {
        'form': formulario
    }

    # verifica se o metodo é do tipo POST
    if request.method == 'POST':
        # verifica se o formulario esta valido de acordo com o arquivo forms.py
        if formulario.is_valid():
            # salva os dados do formulario no banco de dados
            formulario.save()
            # redireciona para a rota '/laboratorio'
            return redirect('/laboratorio')

    # renderiza o HTML com o JSON do formulario
    return render(request, 'laboratorio/novo.html', context)

@login_required
def editarLaboratorio(request, id):
    # busca no banco de dados um determinado Laboratorio pelo id
    laboratorio = Laboratorio.objects.get(id=id)

    # adciona os dados do banco de dados no formulario definido con forms.py
    formulario = LaboratorioForm(request.POST or None, instance=laboratorio)

    # transforma o formulario carregado com os dados em um JSON
    context = {
        'form': formulario
    }

    # verifica se o metodo é um POST
    if request.method == 'POST':
        #verifica se o formulario esta valido
        if formulario.is_valid():
            # salva os dados do formulario no banco de dados
            formulario.save()
            # redireciona para a rota '/laboratorio'
            return redirect('/laboratorio')
    # renderiza o HTML com o JSON do formulario
    return render(request, 'laboratorio/novo.html', context)

@login_required
def excluirLaboratorio(request, id):
    # busca no banco de dados um determinado Laboratorio pelo id
    laboratotio = Laboratorio.objects.get(id=id)
    # deleta o dado que veio na busca
    laboratotio.delete()
    # redireciona para a rota '/laboratorio'
    return redirect('/laboratorio')


