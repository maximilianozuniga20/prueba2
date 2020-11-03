from django import forms
from .models import Juegos
from django.forms import ModelForm

class FormularioJuegos(forms.ModelForm):

    class Meta:
        model = Juegos
        fields = ('__all__')
