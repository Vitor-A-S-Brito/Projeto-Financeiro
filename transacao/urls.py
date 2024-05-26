from django.urls import path
from . import views

urlpatterns = [
    path('criar/', views.criar_transacao, name='criar_transacao'),
    path('listar/', views.listar_trasacoes, name='listar_transacoes'),
    path('marcar_feito/<int:transacao_id>/', views.marcar_feito, name='marcar_feito')
    
]