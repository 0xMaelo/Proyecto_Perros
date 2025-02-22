from django.db import models

class Perro(models.Model):
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    edad = models.IntegerField()
    color = models.CharField(max_length=50)
    fecha_perdido = models.DateField()
    descripcion = models.TextField()
    perdido = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre
