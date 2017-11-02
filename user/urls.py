# importa url do DJANGO
from django.conf.urls import url
# importa todas as views
from . import views

urlpatterns = [
    # manda para a indexLaboratorio no arquivo views.py
    url(r'cadastro/$', views.cadastro, name='cadastro'),

    # manda para a indexLaboratorio no arquivo views.py
    url(r'^$', views.do_login, name='login'),

    # manda para a indexLaboratorio no arquivo views.py
    url(r'logout$', views.do_logout, name='logout'),
]