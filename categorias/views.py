from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Categoria, Subcategoria
from .forms import CategoriaForm, SubcategoriaForm


# Create your views here.

def criar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')  # Redireciona para a lista de categorias
    else:
        form = CategoriaForm(user=request.user)
    return render(request, 'categorias/criar_categorias.html', {'form': form})

def criar_subcategoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    if request.method == 'POST':
        form = SubcategoriaForm(request.POST)
        if form.is_valid():
            subcategoria = form.save(commit=False)
            subcategoria.categoria = categoria  # Associa a categoria diretamente aqui
            subcategoria.save()
            return redirect('listar_subcategorias', categoria_id=categoria_id)
    else:
        form = SubcategoriaForm()
    return render(request, 'subcategorias/criar_subcategorias.html', {'form': form, 'categoria': categoria, 'nome_categoria': categoria.nome})

def listar_categorias(request):
    categorias = Categoria.objects.filter(usuario=request.user)
    return render(request, 'categorias/listar_categorias.html', {'categorias': categorias})

def listar_subcategorias(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    subcategorias = Subcategoria.objects.filter(categoria=categoria)
    return render(request, 'subcategorias/listar_subcategorias.html', {'categoria': categoria, 'subcategorias': subcategorias})
