from django import forms
from django.forms import fields, widgets, TextInput, NumberInput
from .models import Socios

class SocioForm(forms.ModelForm):
    class Meta:
        model = Socios
        fields = '__all__'
        labels = {'dni': 'DNI'}
        widgets = {
            'nombre': TextInput(
                attrs = {
                    'class':'form-control',
                    'autocomplete':'off'
                }
            ),
            'apellido': TextInput(
                attrs = {
                    'class':'form-control',
                    'autocomplete':'off'
                }
            ),
            'dni': TextInput(
                attrs = {
                    'class':'form-control',
                    'autocomplete':'off'
                }
            ),
            'telefono': NumberInput(
                attrs = {
                    'class':'form-control',
                    'autocomplete':'off'
                }
            ),
            'direccion': TextInput(
                attrs = {
                    'class':'form-control',
                    'autocomplete':'off'
                }
            ),
        }