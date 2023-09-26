from django.shortcuts import get_object_or_404, redirect, render

from .forms import ReservaForm
from .models import Reserva
from datetime import datetime


def lista_reservas(empresa):
    nome_da_empresa = empresa.GET.get("nome_da_empresa", "")
    quitado = empresa.GET.get("quitado", "")
    stand_valor = empresa.GET.get("stand_valor", "")
    data_reserva = empresa.GET.get("data_reserva", "")

    reservas = Reserva.objects.all()

    if nome_da_empresa:
        reservas = reservas.filter(nome__icontains=nome_da_empresa)

    if quitado:
        reservas = reservas.filter(quitado=quitado)

    if stand_valor:
        reservas = reservas.filter(stand__valor=stand_valor)

    if data_reserva:
        try:
            # Converte uma string para um objeto datetime
            date_obj = datetime.strptime(data_reserva, "%Y-%m-%d")
            reservas = reservas.filter(data=date_obj)
        except ValueError:
            pass

    context = {"reservas": reservas}
    return render(empresa, "lista_reservas.html", context)


def criar_reserva(request):
    if request.method == "POST":
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_reservas")
    else:
        form = ReservaForm()

    context = {"form": form}
    return render(request, "criar_reserva.html", context)


def atualizar_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    if request.method == "POST":
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect("lista_reservas")
    else:
        form = ReservaForm(instance=reserva)

    context = {"form": form}
    return render(request, "atualizar_reserva.html", context)


def excluir_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    if request.method == "POST":
        reserva.delete()
        return redirect("lista_reservas")
    context = {"reserva": reserva}
    return render(request, "excluir_reserva.html", context)
