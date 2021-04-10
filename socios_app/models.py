from django.db import models

# Create your models here.
class Socios(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    dni = models.CharField(max_length=8, unique = True)
    telefono = models.IntegerField(unique = True)
    direccion = models.CharField(max_length=40, unique = True)

    def __str__(self):
        return f"ID Socio: {self.id} | {self.nombre}, {self.apellido}"
