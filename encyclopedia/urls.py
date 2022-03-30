from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),

    # Al escribir algo en la dirección url, se envía lo escrito a views con el nombre "name"  
      
    path("wiki/<str:name>", views.buscar, name="buscar"),

    # Recibe los datos escritos en la form "buscar"
    path("recibir", views.recibir, name="recibir"),

    # Crear nueva página
    path("crear", views.crear, name="crear"),

    # Editar página existente
    path("editar", views.editar, name="editar"),

    # Ir a página aleatoria
    path("aleatoria", views.aleatoria, name="aleatoria"),

    # Vamos a crear un path para una aplicacion de prueba
    path("prueba", views.prueba, name="prueba"),

    path("formulario", views.formulario, name="formulario")    
]
