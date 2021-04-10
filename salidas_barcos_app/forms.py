from django import forms
from django.forms import fields, widgets
from django.forms.widgets import Select, TextInput
from .models import SalidasBarcos

class SalidaBarcoForm(forms.ModelForm):
    class Meta:
        model = SalidasBarcos
        fields = '__all__'
        labels = {'id_barco': 'Datos'}
        widgets = {
            'id_barco': Select(
                attrs={
                    'class':'form-control',
                    'autocomplete':'off'
                }
            ),
            'destino': TextInput(
                attrs={
                    'class':'form-control',
                    'autocomplete':'off'
                }
            ),
        }