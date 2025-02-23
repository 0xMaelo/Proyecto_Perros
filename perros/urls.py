from django.urls import path
from . import views

app_name = 'perros' 

urlpatterns = [
    path('', views.lista_perros, name='lista_perros'),
    path('agregar/', views.agregar_perro, name='agregar_perro'),
    path('editar/<int:pk>/', views.editar_perro, name='editar_perro'),
    path('eliminar/<int:pk>/', views.eliminar_perro, name='eliminar_perro'),
]