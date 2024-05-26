from django.urls import path
from . import views
from Helio.middleware import TokenMiddleware

urlpatterns = [
    path('criar/', views.criar_conta, name='criar_conta'),
    path('listar/', views.listar_contas, name='listar_contas')
]