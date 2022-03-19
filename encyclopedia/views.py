from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
# Aqui definimos la función "buscar". Por ahora nos envía a una página de prueba
# Ahora le vamos a pasar un argumento
def buscar(request, name):
    entrada = util.get_entry(name)
    if entrada != None:
        return render(request, "encyclopedia/layout.html", {"entrada":entrada}) #Funciona Correctamente
    else:
        return render(request, "encyclopedia/error.html") # Funciona correctamente
    
# Aquí vamos a definir una función nueva, para buscar entradas
