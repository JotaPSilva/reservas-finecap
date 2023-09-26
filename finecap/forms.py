from django import forms

from .models import Reserva


class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ["cnpj", "quitado", "nome", "categoria", "stand"]
        widgets = {
            "cnpj": forms.TextInput(attrs={"class": "form-control"}),
            "quitado": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "categoria": forms.TextInput(attrs={"class": "form-control"}),
            "stand": forms.Select(attrs={"class": "form-select"}),
        }
