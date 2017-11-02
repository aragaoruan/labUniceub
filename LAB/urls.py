"""LAB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

# include PARA INCLUIR OS OUTROS ARQUIVOS urls.py PARA ESSE ARQUIVO
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    # ENTRAR NO MODO ADMINSTRATIVO DO SISTEMA
    url(r'^admin/', admin.site.urls),

    # ROTAS PARA O APP USER (login, logout, cadastro de novo user)
    url(r'^', include('user.urls', namespace='usuario', app_name='user')),

    # ROTAS PARA O APP marcacaoLaboratorio (cadastro, editar, excluir e ver todas marcacao)
    url(r'^marcacaoLaboratorio', include('marcacaoLaboratorio.urls', namespace='marcacaoLaboratorio', app_name='marcacaoLaboratorio')),

    # ROTAS PARA O APP laboratorio (cadastro, editar, excluir e ver todas marcacao)
    url(r'^laboratorio', include('laboratorio.urls', namespace='laboratorio', app_name='laboratorio')),
]
