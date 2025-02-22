from django.urls import path
from . import views

urlpatterns = [
    path('perros/', views.lista_perros, name='lista_perros'),
    path('perros/agregar/', views.agregar_perro, name='agregar_perro'),
    path('perros/editar/<int:id>/', views.editar_perro, name='editar_perro'),
    path('perros/eliminar/<int:id>/', views.eliminar_perro, name='eliminar_perro'),
]
