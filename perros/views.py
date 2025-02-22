from django.shortcuts import render
from .models import Perro
from django.shortcuts import redirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Perro
from .forms import PerroForm


def home(request):
    return redirect('lista_perros')  # Redirige a la lista de perros

# Vista para mostrar todos los perros perdidos
def lista_perros(request):
    perros = Perro.objects.all()  # Obtiene todos los perros
    return render(request, 'perros/lista_perros.html', {'perros': perros})

# Vista para agregar un perro perdido
def agregar_perro(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        raza = request.POST['raza']
        edad = request.POST['edad']
        color = request.POST['color']
        fecha_perdido = request.POST['fecha_perdido']
        descripcion = request.POST['descripcion']
        Perro.objects.create(
            nombre=nombre, raza=raza, edad=edad, color=color, fecha_perdido=fecha_perdido, descripcion=descripcion)
    return render(request, 'perros/agregar_perro.html')

# Vista para editar un perro perdido
def editar_perro(request, id):
    perro = Perro.objects.get(id=id)
    if request.method == 'POST':
        perro.nombre = request.POST['nombre']
        perro.raza = request.POST['raza']
        perro.edad = request.POST['edad']
        perro.color = request.POST['color']
        perro.fecha_perdido = request.POST['fecha_perdido']
        perro.descripcion = request.POST['descripcion']
        perro.save()
    return render(request, 'perros/editar_perro.html', {'perro': perro})

# Vista para eliminar un perro perdido
def eliminar_perro(request, id):
    perro = Perro.objects.get(id=id)
    perro.delete()
    return redirect('lista_perros')  # Redirige a la lista de perros
