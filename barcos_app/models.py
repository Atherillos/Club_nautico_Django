from django.db import models

from socios_app.models import Socios
# Create your models here.

class Barcos(models.Model):
    id_socio = models.ForeignKey("socios_app.Socios", on_delete=models.CASCADE)
    nom_barco = models.CharField(max_length=50, unique=True)
    num_amarre = models.IntegerField(unique=True)
    num_cuota = models.IntegerField()

    def __str__(self):
        return f'Nombre del barco: "{self.nom_barco}" | {self.id_socio}'
