from django import forms
from .models import Perro

class PerroForm(forms.ModelForm):
    fecha_perdido = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = Perro
        fields = ['nombre', 'color', 'fecha_perdido', 'descripcion']