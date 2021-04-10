"""club_nautico URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from index_app.views import index
from socios_app.views import lista_socios, crear_socio, editar_socio, eliminar_socio
from barcos_app.views import editar_barco, eliminar_barco, lista_barcos, crear_barco
from salidas_barcos_app.views import crear_salidas_barcos, editar_salidas_barcos, eliminar_salidas_barcos, lista_salidas_barcos

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index, name="index"),

    path('lista_socios/', lista_socios, name="lista_socios"),
    path('crear_socio/', crear_socio, name="crear_socio"),
    path('crear_socio1/', crear_socio, name="crear_socio1"),
    path('editar_socio/<int:id>/', editar_socio, name='editar_socio'),
    path('eliminar_socio/<int:id>/', eliminar_socio, name='eliminar_socio'),

    path('lista_barcos/', lista_barcos, name="lista_barcos"),
    path('crear_barco/', crear_barco, name="crear_barco"),
    path('crear_barco1/', crear_barco, name="crear_barco1"),
    path('editar_barco/<int:id>/', editar_barco, name="editar_barco"),
    path('elimimar_barco/<int:id>/', eliminar_barco, name="eliminar_barco"),

    path('lista_salidas_barcos/', lista_salidas_barcos , name="lista_salidas_barcos"),
    path('crear_salidas_barcos/', crear_salidas_barcos, name="crear_salidas_barcos"),
    path('crear_salidas_barcos1/', crear_salidas_barcos, name="crear_salidas_barcos1"),
    path('editar_salidas_barcos/<int:id>/', editar_salidas_barcos, name="editar_salidas_barcos" ),
    path('eliminar_salidas_barcos/<int:id>/', eliminar_salidas_barcos, name="eliminar_salidas_barcos"),
]
