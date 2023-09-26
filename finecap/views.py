from django.shortcuts import get_object_or_404, redirect, render

from .forms import ReservaForm
from .models import Reserva


def lista_reservas(request):
    reservas = Reserva.objects.all()
    context = {"reservas": reservas}
    return render(request, "lista_reservas.html", context)


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
