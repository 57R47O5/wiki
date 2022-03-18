from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
# Aqui definimos la función "buscar". Por ahora nos envía a una página de prueba
# Ahora le vamos a pasar un argumento
def buscar(request, name):
    return render(request, "encyclopedia/prueba.html", {"name":name})

