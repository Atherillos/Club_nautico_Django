from django.db import models
from django.db.models.deletion import CASCADE

from datetime import datetime, time


# Create your models here.

class SalidasBarcos(models.Model):
    id_barco = models.ForeignKey("barcos_app.Barcos", on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True, blank=True)
    hora = models.TimeField(auto_now_add=True, blank=True)
    #fecha = models.DateField()
    #hora = models.CharField(max_length=50)
    destino = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.id_barco} | {self.destino}"
