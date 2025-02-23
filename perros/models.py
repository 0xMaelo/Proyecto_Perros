from django.db import models

class Perro(models.Model):
    nombre = models.CharField(max_length=100)
    color = models.CharField(max_length=50)  # Agregar si falta
    fecha_perdido = models.DateField(null=True, blank=True)  # Agregar si falta
    descripcion = models.TextField(null=True, blank=True)  # Agregar si falta

    def __str__(self):
        return self.nombre
