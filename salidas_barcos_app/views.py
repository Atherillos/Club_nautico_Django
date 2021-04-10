from django.shortcuts import render, redirect
from django.http import request

from .models import SalidasBarcos
from .forms import SalidaBarcoForm

# Create your views here.

def lista_salidas_barcos(request):
    traer_salidas_barcos = SalidasBarcos.objects.all()
    contexto = {'Salidas_barcos':traer_salidas_barcos}
    return render(request, 'lista_salidas_barcos.html', contexto)

def crear_salidas_barcos(request):
    if request.method == 'GET':
        form = SalidaBarcoForm()
        contexto = {'form':form}

    elif request.method == 'POST':
        form = SalidaBarcoForm(request.POST)
        contexto = {'form':form}
        if form.is_valid():
            form.save()
            return redirect('crear_salidas_barcos1')
    return render(request, 'crear_salidas_barcos.html', contexto)

def editar_salidas_barcos(request, id):
    salidas_barco_edit = SalidasBarcos.objects.get(id = id)
    if request.method == 'GET':
        form = SalidaBarcoForm(instance=salidas_barco_edit)
        contexto = {'form':form}
    elif request.method == 'POST':
        form = SalidaBarcoForm(request.POST, instance=salidas_barco_edit)
        contexto = {'form':form}
        if form.is_valid():
            form.save()
            return redirect('lista_salidas_barcos')
    return render(request, "crear_salidas_barcos.html", contexto)


def eliminar_salidas_barcos(request, id):
    salidas_barco_elim = SalidasBarcos.objects.get(id = id)
    salidas_barco_elim.delete()
    return redirect('lista_salidas_barcos')