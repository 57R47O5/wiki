from multiprocessing import context
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

import random

from . import markdown2
from . import util, forms 

# Definimos las funciones a usar

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


# Esta función recibe el nombre de una entrada y devuelve una página con la entrada (Si existe)
def buscar(request, name):    
    entrada = markdown2.markdown(util.get_entry(name))
    #entrada = util.get_entry(name)
    edit = 1                                                        # Esta bandera habilita el botón de edición
    contexto = {"name":name, "entrada":entrada, "edit":edit}
    if entrada != None:
        return render(request, "encyclopedia/layout.html", contexto) 
    else:
        return render(request, "encyclopedia/error.html", contexto)          

    

# Esta función recibe el nombre de una entrada en la barra de búsqueda y devuelve la página con la entrada

def recibir(request):    
    if request.method == 'GET':
        datos = request.GET.get('q')              #Recibimos los datos de la form y guardamos aquí        
        entrada = util.get_entry(datos)
        coincidencias = []                        # Creamos una lista vacía. Llenaremos con coincidencias
        context = {'entries': coincidencias,'datos': datos, }  #Diccionario para que entienda nuestro template
        if entrada != None:            
            return buscar(request, datos)           # Gracias, Django, por permitirme hacer esto            
        else:
            lista = util.list_entries()                             # Guardamos las entradas en una lista            
            i = 0
            while i < len(lista):
                x = -1
                x = lista[i].find(datos)
                if x == -1:
                    coincidencias = coincidencias
                else:
                    coincidencias.append(lista[i])                    
                i += 1
            return render(request, "encyclopedia/talvezquiso.html", context)
    else:
        return render(request, "encyclopedia/error2.html")   

# Función que crea nuevas entradas
def crear(request):
    entrada = forms.AgregarEntradaForm                      # Creamos el form    
    context = {'form':entrada,}                             # Creamos el contexto     
    if request.method == 'POST':                            # Si el método es un POST
        entrada = forms.AgregarEntradaForm(request.POST)    # Llenamos los datos en el form   
        if entrada.is_valid():                              # Validamos los datos
            datosentrada = entrada.cleaned_data
            context.update(datosentrada)
            if util.get_entry(datosentrada["titulo"]) == None:
                util.save_entry(datosentrada["titulo"],datosentrada["contenido"])
                #return render(request, "encyclopedia/layout.html", context)
                return buscar(request, datosentrada["titulo"])
            elif datosentrada["tipo"]=="Editar":
                util.save_entry(datosentrada["titulo"],datosentrada["contenido"])                
                return buscar(request, datosentrada["titulo"])
            else:
                return render(request, "encyclopedia/yaexiste.html", context)                                        
        else:            
            return render(request, "encyclopedia/error.html")            
        return render(request, "encyclopedia/crear.html", context)
    else:
        return render(request, "encyclopedia/crear.html", context)  


# Aplicación para editar entradas
def editar(request):    
    datos = "Vacío"
    entrada = "Todavía no hay nada"
    if request.method == 'GET':                                   
        datos = request.GET.get('entrada')                        # Recibimos los datos del get
        entrada = util.get_entry(datos)                           # Guardamos en entrada
    editarform = forms.AgregarEntradaForm(initial={'titulo':datos, 'contenido':entrada, "tipo":"Editar"})    
    context = {'datos':datos, 'entrada':entrada, 'form':editarform}
    return render(request, "encyclopedia/editar.html", context)

def aleatoria(request):
    lista = util.list_entries()                               # Creamos una lista con los nombres de las entradas
    datos = random.choice(lista)                             # Elegimos un elemento aleatorio
    return buscar(request, datos)                             # Ya listo      

def prueba(request):  
    if request.method == 'GET':     # Los datos se reciben. Ahora es necesario almacenarlos en una variable
        datos = request.GET.get('q')
        return render(request, "encyclopedia/prueba.html" )
    else:
        return render(request, "encyclopedia/error2.html")

def formulario(request):     
    return render(request, "encyclopedia/formulario.html" )
        



