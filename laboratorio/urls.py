from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.indexLaboratorio, name='indexLaboratorio'),
    url(r'^cadastrarLaboratorio$', views.cadastrarLaboratorio, name='novoLaboratorio'),
    url(r'^editarLaboratorio/(?P<id>\d+)/$', views.editarLaboratorio, name='editarLaboratorio'),
    url(r'^exluirLaboratorio/(?P<id>\d+)/$', views.excluirLaboratorio, name='excluirLaboratorio'),
]