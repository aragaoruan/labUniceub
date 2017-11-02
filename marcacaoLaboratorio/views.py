# importando o render (renderizar pagina) e redirect (redirecionar pagina)
from django.shortcuts import render, redirect
# importando login_required (para verificar se o usuario esta logado)
from django.contrib.auth.decorators import login_required
# importando a model Marcacao
from marcacaoLaboratorio.models import Marcacao
#importando o formulario LaboratorioForm
from marcacaoLaboratorio.forms import MarcacaoForm

"""
@login_required verifica se o usuario esta logado 
caso sim entra na funcao se não estiver logado 
ele manda para a raiz do projeto
(FOI DEFINIDO QUE IRA MANDAR PARA A RAIZ DO PROJETO 
    NO ARQUIVO settings.py linha 139 - LOGIN_URL = '/' )
"""
@login_required
def do_index(request):
    # lista todos os Marcacao com ordem do id
    lista = Marcacao.objects.all().order_by('-id')

    # transforma a busca em um JSON para mandar para o HTML
    context = {
        'lista_marcacao': lista
    }

    return render(request, 'marcacao/index.html', context)

@login_required
def cadastrarMarcacao(request):

    formulario = MarcacaoForm(request.POST or None)

    # transformao formulario em um JSON para mandar para o HTML
    context = {
        'form': formulario
    }

    # verifica se o metodo é do tipo POST
    if request.method == 'POST':
        formulario.cod_user = request.user

        # verifica se o formulario esta valido de acordo com o arquivo forms.py
        if formulario.is_valid():
            formulario.cod_user = request.user

            # salva os dados do formulario no banco de dados
            formulario.save()

            # redireciona para a rota '/marcacaoLaboratorio'
            return redirect('/marcacaoLaboratorio')
    # renderiza o html com o mandando o JSON como parametro
    return render(request, 'marcacao/novo.html', context)

@login_required
def editarMarcacao(request, id):
    # lista todos os Marcacao com ordem do id
    marcacao = Marcacao.objects.get(id=id)

    # adciona os dados do banco de dados no formulario definido con forms.py
    formulario = MarcacaoForm(request.POST or None, instance=marcacao)
    # transforma o formulario em um JSON para mandar para o HTML

    context = {
        'form': formulario
    }

    # verifica se o metodo é do tipo POST
    if request.method == 'POST':
        # verifica se o formulario esta valido de acordo com o arquivo forms.py

        if formulario.is_valid():
            v = formulario.save(commit=False)
            v.cod_user = request.user

            # salva os dados do formulario no banco de dados
            formulario.save()

            # redireciona para a rota '/marcacaoLaboratorio'
            return redirect('/marcacaoLaboratorio')

    # renderiza o html com o mandando o JSON como parametro
    return render(request, 'marcacao/novo.html', context)

@login_required
def excluirMarcacao(request, id):
    # lista todos os Marcacao com ordem do id
    marcacao = Marcacao.objects.get(id=id)

    # deleta o dado que veio na busca
    marcacao.delete()
    # redireciona para a rota '/marcacaoLaboratorio'
    return redirect('/marcacaoLaboratorio')