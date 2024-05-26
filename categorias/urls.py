from django.urls import path
from . import views
from Helio.middleware import TokenMiddleware

urlpatterns=[
    path('categorias/listar/', views.listar_categorias, name='listar_categorias'),
    path('subcategorias/<int:categoria_id>/', views.listar_subcategorias, name='listar_subcategorias'),
    path('categorias/criar/', views.criar_categoria, name='criar_categorias'),
    path('subcategorias/criar/<int:categoria_id>/', views.criar_subcategoria, name='criar_subcategorias'),
]