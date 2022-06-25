from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/caixa-leads/', views.caixa_leads, name='caixa-leads'),
    path('leads/<int:pk>/', views.leads, name='leads'),
    path('status/<int:pk>/', views.status, name='status'),
    path('area-adm/', views.area_adm, name='area-adm'),
    path('cadastro-clientes/', views.cadastro_clientes, name='cadastro-clientes'),
    path('cliente/<int:pk>/', views.cliente_info, name='cliente'),
    path('lista-clientes/', views.lista_clientes, name='lista-cliente'),
    path('editar-cliente/<int:pk>/', views.editar_cliente, name='editar-cliente'),
    path('deletar-cliente/<int:pk>/', views.deletar_cliente, name='deletar-cliente'),
    path('cliente-deletado/', views.cliente_deletado, name='cliente-deletado'),
    path('cadastro-produtos/', views.cadastro_produtos, name='cadastro-produto'),
    path('lista-produtos/', views.lista_produtos, name='lista-produtos'),
    path('editar-listagem-produtos/<int:pk>/', views.editar_lista_produtos, name='editar-listagem-produtos'),
    path('deletar-produtos/<int:pk>/', views.deletar_produtos, name='deletar-produtos')
]
