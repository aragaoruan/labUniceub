from django.shortcuts import render, redirect
from user.forms import UserModelForm
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'user/index.html')

def cadastro(request):
    form = UserModelForm(request.POST or None)
    context = {'form':form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(do_login)

    return render(request, 'user/cadastro.html', context)

def do_login(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])

        if user is not None:
            login(request, user)
            return redirect('/')
    return render(request, 'user/login.html')

def do_logout(request):
    logout(request)
    return redirect('/login')