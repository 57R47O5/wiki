from django.shortcuts import render
from django import forms

from . import util

# Definimos un form de donde recibiremos la cadena que busca el usuario

class BuscarForm(forms.Form):
    busqueda = forms.CharField(label="Buscar")

# Definimos las funciones a usar

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


# Aqui definimos la función "buscar". 
def buscar(request, name):
    entrada = util.get_entry(name)
    if entrada != None:
        return render(request, "encyclopedia/layout.html", {"entrada":entrada}) 
    else:
        return render(request, "encyclopedia/error.html"
)
    
# Aquí vamos a definir una función nueva, para buscar entradas

def recibir(request):    
    if request.method == 'GET':
        datos = request.GET.get('q')              #Recibimos los datos de la form y guardamos aquí        
        entrada = util.get_entry(datos)
        if entrada != None:
            return render(request, "encyclopedia/layout.html", {"entrada":entrada})
        else:
            return render(request, "encyclopedia/error.html")
    else:
        return render(request, "encyclopedia/error.html")   

def prueba(request):  
    if request.method == 'GET':     # Los datos se reciben. Ahora es necesario almacenarlos en una variable
        datos = request.GET.get('q')
        return render(request, "encyclopedia/prueba.html" )
    else:
        return render(request, "encyclopedia/error2.html")

def formulario(request):     
    return render(request, "encyclopedia/formulario.html" )
        



