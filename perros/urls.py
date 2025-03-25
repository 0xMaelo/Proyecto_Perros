from django.urls import path
from . import views

app_name = 'perros' 
urlpatterns = [
    path('', views.home, name='home'), 
    path('lista/', views.lista_perros, name='lista_perros'),
    path('agregar/', views.agregar_perro, name='agregar_perro'),
    path('editar/<uuid:pk>/', views.editar_perro, name='editar_perro'),
    path('eliminar/<uuid:pk>/', views.eliminar_perro, name='eliminar_perro'),
    path('buscar/', views.buscar_perro, name='buscar_perro'),
    path('prueba/', views.prueba, name='prueba'),
    path('agregar_perro_albergue/', views.agregar_perro_albergue, name = 'agregar_perro_albergue'),
    path('agregar_perro_UsuarioR/', views.agregar_perro_UsuarioR, name = 'agregar_perro_UsuarioR'),
]
