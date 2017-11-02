# importa url do DJANGO
from django.conf.urls import url
# importa todas as views
from . import views

urlpatterns = [
    # manda para a indexLaboratorio no arquivo views.py
    url(r'^$', views.do_index, name='indexMarcacao'),

    # manda para a indexLaboratorio no arquivo views.py
    url(r'^cadastrar$', views.cadastrarMarcacao, name='novoMarcacao'),

    # manda para a indexLaboratorio no arquivo views.py
    url(r'^editar/(?P<id>\d+)/$', views.editarMarcacao, name='editarMarcacao'),

    # manda para a indexLaboratorio no arquivo views.py
    url(r'^excluir/(?P<id>\d+)/$', views.excluirMarcacao, name='excluirMarcacao'),
]