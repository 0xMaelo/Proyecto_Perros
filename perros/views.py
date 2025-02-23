# from django.shortcuts import render
# from .models import Perro
# from django.shortcuts import redirect
# from django.shortcuts import render, redirect, get_object_or_404
# from .models import Perro
# from .forms import PerroForm

# def home(request):
#     return redirect('perros:lista_perros')
#   # Redirige a la lista de perros
#     perro = get_object_or_404(Perro, id=id)
#     if request.method == 'POST':
#         perro.delete()
#         return redirect('perros:lista_perros')
#     return render(request, 'perros/eliminar_perro.html', {'perro': perro})

# def lista_perros(request):
#     return render(request, 'lista_perros.html')


# def agregar_perro(request):
#     # Aquí iría la lógica para agregar un perro
#     pass

# def editar_perro(request, pk):  # Cambiar id por pk
#     perro = get_object_or_404(Perro, pk=pk)  # Cambia id= por pk=
#     # Aquí iría la lógica para editar el perro
#     pass

# def eliminar_perro(request, pk):  # Cambiar id por pk
#     perro = get_object_or_404(Perro, pk=pk)  # Cambia id= por pk=
#     perro.delete()
#     return redirect('perros:lista_perros')

from django.shortcuts import render, redirect, get_object_or_404
from .models import Perro
from .forms import PerroForm

def home(request):
    return redirect('perros:lista_perros')

def lista_perros(request):
    perros = Perro.objects.all()
    return render(request, 'perros/lista_perros.html', {'perros': perros})

def agregar_perro(request):
    if request.method == 'POST':
        form = PerroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('perros:lista_perros')
    else:
        form = PerroForm()
    return render(request, 'perros/agregar_perro.html', {'form': form})

def editar_perro(request, pk):
    perro = get_object_or_404(Perro, pk=pk)
    if request.method == 'POST':
        form = PerroForm(request.POST, instance=perro)
        if form.is_valid():
            form.save()
            return redirect('perros:lista_perros')
    else:
        form = PerroForm(instance=perro)
    return render(request, 'perros/editar_perro.html', {'form': form})

def eliminar_perro(request, pk):
    perro = get_object_or_404(Perro, pk=pk)
    if request.method == 'POST':
        perro.delete()
        return redirect('perros:lista_perros')
    return render(request, 'perros/eliminar_perro.html', {'perro': perro})