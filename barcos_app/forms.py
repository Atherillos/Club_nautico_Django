from django import forms
# from django.forms import Select
from django.forms.widgets import NumberInput, TextInput, Select
from .models import Barcos

class BarcoForm(forms.ModelForm):
    class Meta:
        model = Barcos
        fields = '__all__'
        labels = {'id_socio': 'Datos del socio', 'nom_barco': 'Nom. del barco', 'num_amarre':'Num. de amarre', 'num_cuota': 'Num. de cuota'}
        widgets = {
            'id_socio': Select(
                attrs = {
                    'class':'form-control',
                    'autocomplete':'off'
                }
            ),
            'nom_barco': TextInput(
                attrs = {
                    'class':'form-control',
                    'autocomplete':'off'
                }
            ),
            'num_amarre': NumberInput(
                attrs = {
                    'class':'form-control',
                    'autocomplete':'off'
                }
            ),
            'num_cuota': NumberInput(
                attrs = {
                    'class':'form-control',
                    'autocomplete':'off'
                }
            ),
        }