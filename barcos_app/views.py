from django.shortcuts import render, redirect

from .models import Barcos
from .forms import BarcoForm

# Create your views here.

def lista_barcos(request):
    lista_barcos = Barcos.objects.all()
    contexto = {'barcos': lista_barcos}
    return render(request, 'lista_barcos.html', contexto)

def crear_barco(request):
    if request.method == 'GET':
        form = BarcoForm()
        contexto = {"form":form}

    elif request.method == 'POST':
        form =BarcoForm(request.POST)
        contexto = {'form':form}
        if form.is_valid():
            form.save()
            return redirect('crear_barco1')
    return render(request, "crear_barco.html", contexto)

def editar_barco(request, id):
    barco_edit = Barcos.objects.get(id = id)
    if request.method == 'GET':
        form = BarcoForm(instance=barco_edit)
        contexto = {'form':form}
    elif request.method == 'POST':
        form = BarcoForm(request.POST, instance=barco_edit)
        contexto = {'form':form}
        if form.is_valid():
            form.save()
            return redirect('lista_barcos')
    return render(request, "crear_barco.html", contexto)

def eliminar_barco(request, id):
    barco_elim = Barcos.objects.get(id = id)
    barco_elim.delete()
    return redirect("lista_barcos")