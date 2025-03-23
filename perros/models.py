from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import uuid

def validarMicrochipNum(value):
    if len(str(value)) < 10:
       print(str(value))
       raise ValidationError(
            _("%(value)s No es de 10 dígitos ni de 15 dígitos"),
            params={"value": value},
        )
    if len(str(value)) >= 10:
        if len(str(value)) == 10:
            pass
        elif len(str(value)) == 15:
            pass
        elif len(str(value)) != 10 or len(str(value)) != 15:
           raise ValidationError(
            _("%(value)s Te pasaste de 10 dígitos o son menos o mas de 15 dígitos" + str(len(str(value)))),
            params={"value": value},
           )

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
    
    COLORES_CHOICES = [
    	('rojizo', 'Rojizo'),
    	('blanco', 'Blanco'),
    	('negro', 'Negro'),
    	('azul oscuro', 'Azul oscuro'),
    	('marron', 'Marron'),
    	('durazno', 'Durazno'),
    	('beige', 'Beige'),
    	('cafe', 'Cafe'),
    	('gris', 'Gris'),
    	('gris oscuro', 'Gris oscuro'),
    	('gris claro', 'Gris claro'),
    	('amarillo dorado', 'Amarillo dorado'),
    	('bicolor', 'Bicolor'),
    	('tricolor', 'Tricolor'),
    	('atigrado', 'Atrigrado'),
    	('arlequin', 'Arlequin'),
    ]
    
    PELAJES_CHOICES = [
    	('corto', 'Corto'),
    	('rizado', 'Rizado'),
    	('duro', 'Duro'),
    	('lanoso_lanudo', 'lanoso/lanudo'),
    	('profundo', 'Profundo'),
    	('protector', 'Protector'),
    	('medio', 'Medio'),
    	('aspero', 'Aspero'),
    	('sedoso', 'Sedoso'),
    ]
    
    COLOR_COLLAR_CHOICES = [
        ('rojo', 'Rojo'),
        ('blanco', 'Blanco'),
        ('azul', 'Azul'),
        ('naranja', 'Naranja'),
        ('negro', 'Negro'),
        ('cielo', 'Azul Cielo'),
        ('gris', 'Gris'),
        ('rosa', 'Rosa'),
        ('morado', 'Morado'),
    ]
    
    ALCALDIA_CHOICES = [
    	('azcapotzalco', 'Azcapotzalco'),
    	('coyoacan', 'Coyoacan'),
    	('cuajimalpa', 'Cuajimalpa de Morelos'),
    	('gam', 'Gustavo A. Madero'),
    	('iztacalco', 'Iztacalco'),
    	('iztapalapa', 'Iztapalapa'),
    	('magdalena contreras', 'La Magdalena Contreras'),
    	('milpa alta', 'Milpa Alta'),
    	('alvaro obregon', 'Alvaro Obregon'),
    	('tlahuac', 'Tlahuac'),
    	('tlalpan', 'Tlalpan'),
    	('xochimilco', 'Xochimilco'),
    	('benito juarez', 'Benito Juarez'),
    	('cuauhtemoc', 'Cuauhtemoc'),
    	('miguel hidalgo', 'Miguel Hidalgo'),
    	('venustiano carranza', 'Venustiano Carranza'),
    ]
    
    IDENTIFICADOR_CHOICES = [
    	('ruac', 'RUAC'),
    	('microchip', 'Microchip'),
    	('tatuaje', 'Tatuaje'),
    	('no', 'Ninguno'),
    ]
    
    ESTADO_CHOICES = [
        ('saludable', 'Saludable'),
        ('desnutrido', 'Desnutrido'),
        ('herido', 'Herido'),
        ('sucio', 'Sucio')
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    tamano = models.CharField(max_length=10, choices=TAMANO_CHOICES)
    sexo = models.CharField(max_length=10, choices=SEXO_CHOICES)
    collar = models.CharField(max_length=2, choices=COLLAR_CHOICES)
    color_collar = models.CharField(max_length=25, null=True, blank=True, choices = COLOR_COLLAR_CHOICES)
    color = models.CharField(max_length=20, choices = COLORES_CHOICES)
    tipo_pelo = models.CharField(max_length = 14, choices = PELAJES_CHOICES, null = True, blank = True)
    foto = models.ImageField(upload_to='perros_fotos/', null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    fecha_perdido = models.DateField()
    ultima_calle = models.CharField(max_length = 31, null = True, blank = True)
    ultima_colonia = models.CharField(max_length = 49)
    ultima_alcaldia = models.CharField(max_length = 29, choices = ALCALDIA_CHOICES)
    #ultima_latitud = models.DecimalField(max_digits = 8, decimal_places = 4, validators = [MinValueValidator(0), MaxValueValidator(90)])
    #ultima_longitud = models.DecimalField(max_digits = 7, decimal_places = 3, validators = [MinValueValidator(0), MaxValueValidator(180)])
    ultima_latitud = models.DecimalField(max_digits = 8, decimal_places = 4)
    ultima_longitud = models.DecimalField(max_digits = 7, decimal_places = 3)
    microchip = models.CharField(max_length = 2, choices = COLLAR_CHOICES)
    #microchip_num = models.PositiveIntegerField(validators = [validarMicrochipNum])
    microchip_num = models.PositiveIntegerField()
    ruac = models.CharField(max_length = 2, choices = COLLAR_CHOICES)
    ruac_clave = models.CharField(max_length = 8, null = True, blank = True)
    puppy = models.BooleanField()
    rabia = models.BooleanField()
    parvovirus_vacuna = models.BooleanField()
    giardia = models.BooleanField()
    cuadruple = models.BooleanField()
    quintuple = models.BooleanField()
    sextuple = models.BooleanField()
    bordetella = models.BooleanField()
    pulgas = models.BooleanField()
    displasia_cadera = models.BooleanField()
    nematodos = models.BooleanField()
    cestodos = models.BooleanField()
    giardas_coccidios = models.BooleanField()
    parvovirus_enfermo = models.BooleanField()
    identificador = models.CharField(max_length = 10, choices = IDENTIFICADOR_CHOICES)
    tatuaje = models.CharField(max_length = 60, null = True, blank = True)
    estado = models.CharField(max_length = 10, choices = ESTADO_CHOICES) 
    nombreAlbergue = models.CharField(max_length = 60, null = True, blank = True)
    contactoAlbergue = models.PositiveIntegerField()
    ubicacionAlbergue = models.CharField(max_length = 120, null = True, blank = True)
    
    def __str__(self):
        return self.nombre
