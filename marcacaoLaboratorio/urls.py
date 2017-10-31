from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.do_index, name='indexMarcacao'),
    url(r'^cadastrar$', views.cadastrarMarcacao, name='novoMarcacao'),
    url(r'^editar/(?P<id>\d+)/$', views.editarMarcacao, name='editarMarcacao'),
    url(r'^excluir/(?P<id>\d+)/$', views.excluirMarcacao, name='excluirMarcacao'),
]