from django.shortcuts import render, redirect
from user.forms import UserModelForm
from django.contrib.auth import authenticate, login ,logout

def cadastro(request):
    form = UserModelForm(request.POST or None)
    context = {'form':form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('user/login.html')

    return render(request, 'user/cadastro.html', context)

def do_login(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])

        if user is not None:
            login(request, user)
            return redirect('/marcacaoLaboratorio')
    return render(request, 'user/login.html')

def do_logout(request):
    logout(request)
    return redirect('/')