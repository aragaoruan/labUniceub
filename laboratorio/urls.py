# importa url do DJANGO
from django.conf.urls import url
# importa todas as views
from . import views

urlpatterns = [
    # manda para a indexLaboratorio no arquivo views.py
    url(r'^$', views.indexLaboratorio, name='indexLaboratorio'),

    # manda para a cadastrarLaboratorio no arquivo views.py
    url(r'^cadastrarLaboratorio$', views.cadastrarLaboratorio, name='novoLaboratorio'),

    # manda para a editarLaboratorio no arquivo views.py
    url(r'^editarLaboratorio/(?P<id>\d+)/$', views.editarLaboratorio, name='editarLaboratorio'),

    # manda para a excluirLaboratorio no arquivo views.py
    url(r'^exluirLaboratorio/(?P<id>\d+)/$', views.excluirLaboratorio, name='excluirLaboratorio'),
]