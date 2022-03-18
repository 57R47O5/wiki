from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # Al escribir algo en la dirección url, se envía lo escrito a views con el nombre "name"     
    path("<str:name>", views.buscar, name="buscar"),
]
