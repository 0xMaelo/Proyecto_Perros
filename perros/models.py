from django.db import models
import uuid

class Perro(models.Model):
    TAMANO_CHOICES = [
        ('pequeno', 'Pequeño'),
        ('mediano', 'Mediano'),
        ('grande', 'Grande'),
    ]
    
    SEXO_CHOICES = [
        ('macho', 'Macho'),
        ('hembra', 'Hembra'),
    ]
    
    COLLAR_CHOICES = [
        ('si', 'Sí'),
        ('no', 'No'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    tamano = models.CharField(max_length=10, choices=TAMANO_CHOICES)
    sexo = models.CharField(max_length=10, choices=SEXO_CHOICES)
    collar = models.CharField(max_length=2, choices=COLLAR_CHOICES)
    color_collar = models.CharField(max_length=50, null=True, blank=True)
    color = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='perros_fotos/', null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    fecha_perdido = models.DateField()

    def __str__(self):
        return self.nombre