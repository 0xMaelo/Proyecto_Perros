from django.shortcuts import render, redirect, get_object_or_404
from .models import Perro
from .forms import PerroForm, RAZAS_PERROS, UsarioRForm, AlbergueForm
from django.db import transaction


def home(request):
    return render(request, 'perros/home.html')

def lista_perros(request):
    perros = Perro.objects.all()
    return render(request, 'perros/lista_perros.html', {'perros': perros})

def agregar_perro(request):
    print(request.method)
    if request.method == 'POST':
        print("aqui ando")
        form = PerroForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            try:
                with transaction.atomic():
                    perro = form.save(commit=False)
                    if perro.collar == 'no':
                        perro.color_collar = None
                    #if perro.microchip == 'no':
                    #    perro.microchip_num = None
                    if perro.ruac == 'no':
                        perro.ruac_clave = None
      			                  
                    perro.save()
                return redirect('perros:lista_perros')
            except Exception as e:
                print(f"Error al guardar: {e}")
    else:
        form = PerroForm()
        print("asu")
    
    context = {
        'form': form,
        'razas': RAZAS_PERROS,
    }
    return render(request, 'perros/agregar_perro.html', context)

def editar_perro(request, pk):
    perro = get_object_or_404(Perro, pk=pk)
    if request.method == 'POST':
        form = PerroForm(request.POST, request.FILES, instance=perro)
        if form.is_valid():
            perro = form.save(commit=False)
            if perro.collar == 'no':
                perro.color_collar = None
            #if perro.microchip == 'no':
            #	perro.microchip_num = None
            if perro.ruac == 'no':
            	perro.ruac_clave = None
            	
            perro.save()
            return redirect('perros:lista_perros')
    else:
        form = PerroForm(instance=perro)
    
    context = {
        'form': form,
        'razas': RAZAS_PERROS,
        'perro': perro
    }
    return render(request, 'perros/editar_perro.html', context)

def eliminar_perro(request, pk):
    perro = get_object_or_404(Perro, pk=pk)
    if request.method == 'POST':
        perro.delete()
        return redirect('perros:lista_perros')
    return render(request, 'perros/eliminar_perro.html', {'perro': perro})

def buscar_perro(request):
    # por implementar...
    return render(request, 'perros/buscar_perro.html')

def prueba(request):
    return render(request, 'perros/prueba.html')

def agregar_perro_albergue(request):
    if request.method == 'POST':
    	form = AlbergueForm(request.POST, request.FILES, request.FILES.getlist('fotos'))
    	print("el formulario es valido? : {:}".format(form.is_valid()))
    	if form.is_valid():
    	    try:
    	        with transaction.atomic():
    	            perro = form.save(commit=False)
    	            #if perro.collar == 'no':
    	            #	perro.color_collar = None
    	            #if perro.microchip == 'no':
    	            #	perro.microchip_num = None
    	            if perro.ruac == 'no':
    	            	perro.ruac_clave = None
    	        
    	        perro.save()
    	        return redirect('perros:lista_perros')
    	    except Exception as e:
    	    	print(f"Error al guardar: {e}")
    else:
    	form = AlbergueForm()
    
    context = {
        'form': form,
        'razas': RAZAS_PERROS,
    }
    return render(request, 'perros/agregar_perro_albergue.html', context)

def agregar_perro_UsuarioR(request):
    if request.method == 'POST':
    	form = UsarioRForm(request.POST, request.FILES, request.FILES.getlist('foto'))
    	print(form.is_valid())
    	if form.is_valid():
    	    try:
    	        with transaction.atomic():
    	            perro = form.save(commit=False)
    	            #if perro.collar == 'no':
    	            #	perro.color_collar = None
    	            #if perro.microchip == 'no':
    	            #	perro.microchip_num = None
    	            if perro.ruac == 'no':
    	            	perro.ruac_clave = None
    	        
    	        perro.save()
    	        return redirect('perros:lista_perros')
    	    except Exception as e:
    	    	print(f"Error al guardar: {e}")
    else:
    	form = UsarioRForm()
    
    context = {
        'form': form,
        'razas': RAZAS_PERROS,
    }
    return render(request, 'perros/agregar_perro_UsuarioR.html', context)
