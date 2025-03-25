from django import forms
from .models import Perro

RAZAS_PERROS = [
    "Affenpinscher", "Akita", "Alaskan Malamute", "American Bulldog", "American Pit Bull Terrier",
    "Basset Hound", "Beagle", "Bichón Frisé", "Bloodhound", "Border Collie", "Boston Terrier", "Boxer",
    "Bulldog Francés", "Bulldog Inglés",
    "Chihuahua", "Chow Chow", "Cocker Spaniel", "Collie",
    "Dachshund", "Dálmata", "Doberman",
]

class PerroForm(forms.ModelForm):
    raza = forms.CharField(
        widget=forms.TextInput(attrs={'list': 'razas', 'autocomplete': 'off'})
    )
    
    fecha_perdido = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    
    class Meta:
        model = Perro
        fields = ['nombre', 'raza', 'tamano', 'sexo', 'color', 'tipo_pelo', 'collar', 'color_collar', 'foto', 'descripcion', 'fecha_perdido', 'ultima_calle', 'ultima_colonia', 'ultima_alcaldia', 'ultima_latitud', 'ultima_longitud', 'ruac', 'ruac_clave', 'puppy', 'rabia', 'parvovirus_vacuna', 'giardia', 'cuadruple', 'quintuple', 'sextuple', 'bordetella', 'pulgas', 'displasia_cadera', 'nematodos', 'cestodos', 'giardas_coccidios', 'parvovirus_enfermo']
        #, 'microchip', 'microchip_num']
        #""", 'identificador', 'tatuaje', 'estado', 'nombreAlbergue', 'contactoAlbergue', 'ubicacionAlbergue']"""

        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['color_collar'].required = False
        
    def clean(self):
        cleaned_data = super().clean()
        collar = cleaned_data.get('collar')
        color_collar = cleaned_data.get('color_collar')
        
        if collar == 'si' and not color_collar:
            self.add_error('color_collar', 'Por favor indique el color del collar')
        
        return cleaned_data
