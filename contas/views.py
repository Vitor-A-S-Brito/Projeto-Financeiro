from django.shortcuts import render, redirect
from .forms import ContaBancariaForm
from .models import ContaBancaria

def criar_conta(request):
    if request.method == 'POST':
        form = ContaBancariaForm(request.POST)
        if form.is_valid():
            conta = form.save(commit=False)
            conta.user = request.user
            form.save()
            return redirect('listar_contas')
    else:
        form = ContaBancariaForm()
    return render(request, 'conta/criar_conta.html', {'form': form})

def listar_contas(request):
    contas = ContaBancaria.objects.filter(user=request.user)
    return render(request, 'conta/listar_contas.html', {'contas':contas})