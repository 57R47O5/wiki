from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),

    # Al escribir algo en la dirección url, se envía lo escrito a views con el nombre "name"  
      
    path("wiki/<str:name>", views.buscar, name="buscar"),

    # De que forma enviar a views.recibir? Siempre va a views.buscar, porque es muy generico
    path("recibir", views.recibir, name="recibir"),

    # Vamos a crear un path para una aplicacion de prueba

    path("prueba", views.prueba, name="prueba"),

    path("formulario", views.formulario, name="formulario")
]
