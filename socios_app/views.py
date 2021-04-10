from django.http import request
from django.shortcuts import redirect, render

from .models import Socios
from .forms import SocioForm

# Create your views here.

def lista_socios(request):
    traer_socios = Socios.objects.all()
    contexto = {"Socios": traer_socios}
    return render(request, 'lista_socios.html', contexto)

def crear_socio(request):
    if request.method == 'GET':
        form = SocioForm()
        contexto = {"form":form}

    elif request.method == 'POST':
        form = SocioForm(request.POST)
        contexto = {"form":form}
        if form.is_valid():
            form.save()
            return redirect('crear_socio1')
            # return render(request,'crear_socio.html', {'mensaje':True}, redirect('lista_socios'))
    return render(request, 'crear_socio.html', contexto)

def editar_socio(request, id):
    socio_edit = Socios.objects.get(id = id)
    if request.method == 'GET':
        form = SocioForm(instance=socio_edit)
        contexto = {'form':form}
    else:
        form = SocioForm(request.POST, instance=socio_edit)
        contexto = {'form':form}
        if form.is_valid():
            form.save()
            return redirect('lista_socios')
    return render(request, 'crear_socio.html', contexto)


def eliminar_socio(request, id):
    socio_eliminar = Socios.objects.get(id = id)
    socio_eliminar.delete()
    return redirect('lista_socios')
