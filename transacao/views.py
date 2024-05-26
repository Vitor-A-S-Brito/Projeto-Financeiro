from django.shortcuts import render, redirect, get_object_or_404
from .forms import TransacaoForm
from .models import Transacao
from contas.models import ContaBancaria
from datetime import date, datetime
from django.db.models import F

# Create your views here.

def criar_transacao(request):
    if request.method == 'POST':
        form = TransacaoForm(request.POST)

        if form.is_valid():
            transacao = form.save(commit=False)

            # Verifica se a transação é programada
            if form.cleaned_data['programada']:
                transacao.data_hora = form.cleaned_data['programada']
                transacao.consolidada = False
            else:
                # Se não for programada, verifica se a data de hoje é depois da programada
                if transacao.programada and transacao.programada < date.today():
                    transacao.atrasado = True
                transacao.consolidada = True

            # Verifica se a transação foi paga para alterar o saldo da conta
            if transacao.pago:
                if transacao.tipo == 'entrada':
                    transacao.conta.saldo += transacao.valor
                elif transacao.tipo == 'saida':
                    transacao.conta.saldo -= transacao.valor
                transacao.conta.save()

            transacao.save()
            return redirect('listar_transacoes')
    else:
        form = TransacaoForm()
    return render(request, 'transacao/criar_transacao.html', {'form': form})

def listar_trasacoes(request):
    mes = request.GET.get('mes')
    if mes:
        transacoes = Transacao.objects.filter(data_hora__mouth=mes)
    else: 
        transacoes = Transacao.objects.all()
    
    for transacao in transacoes:
        if transacao.programada and transacao.data_hora <= datetime.now().date():
            transacao.consolidada = True
        transacao.save()
    return render(request, 'transacao/listar_transacoes.html',{'transacoes': transacoes})

def marcar_feito(request, transacao_id):
    print("ID python", transacao_id)
    transacao = get_object_or_404(Transacao, pk=transacao_id)
    transacao.pago = True
    transacao.save()
    if transacao.tipo == 'entrada':
        ContaBancaria.objects.filter(pk=transacao.conta.pk).update(saldo=F('saldo') + transacao.valor)
    elif transacao.tipo == 'saida':
        ContaBancaria.objects.filter(pk=transacao.conta.pk).update(saldo=F('saldo') - transacao.valor)

        print(f"Transação {transacao_id} marcada como paga. Saldo da conta atualizado.")
    else:
        print(f"Transação {transacao_id} já está marcada como paga.")
    return redirect('listar_transacoes')
