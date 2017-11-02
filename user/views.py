# importando o render (renderizar pagina) e redirect (redirecionar pagina)
from django.shortcuts import render, redirect
#importando o formulario LaboratorioForm
from user.forms import UserModelForm
"""importando authenticate (autenticar usuarios),
    login (fazer login no sistema),
    logout( fazer logout do sistema)
"""
from django.contrib.auth import authenticate, login ,logout

def cadastro(request):

    form = UserModelForm(request.POST or None)

    # transformao formulario em um JSON para mandar para o HTML
    context = {
        'form':form
    }

    # verifica se o metodo é do tipo POST
    if request.method == 'POST':

        # verifica se o formulario esta valido de acordo com o arquivo forms.py
        if form.is_valid():
            # salva os dados do formulario no banco de dados
            form.save()
            # redireciona para a rota '/' (RAIZ)
            return redirect('/')

    # renderiza o html com o mandando o JSON como parametro
    return render(request, 'user/cadastro.html', context)

def do_login(request):

    # verifica se o metodo é do tipo POST
    if request.method == 'POST':

        #autenticando usuario
        user = authenticate(username=request.POST['username'], password=request.POST['password'])

        #verifica se existe esta existe
        if user is not None:
            #fazendo login e salvando informações do usuario na sessao
            login(request, user)
            # redireciona para a rota '/marcacaoLaboratorio'
            return redirect('/marcacaoLaboratorio')

    # renderiza o html
    return render(request, 'user/login.html')

def do_logout(request):
    #pega tudo que tem na request ( request possui o user da sessao)
    logout(request)
    #redireciona para a raiz
    return redirect('/')