from multiprocessing import context
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from . import util, forms

# Definimos las funciones a usar

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


# Aqui definimos la función "buscar". 
def buscar(request, name):
    entrada = util.get_entry(name)
    contexto = {"name":name, "entrada":entrada}
    if entrada != None:
        return render(request, "encyclopedia/layout.html", contexto) 
    else:
        return render(request, "encyclopedia/error.html", contexto)        #Estamos entrando acá    

    
# Aquí vamos a definir una función nueva, para buscar entradas
# Acá hay que solucionar. Los datos deben ir ya validados a Buscar

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
                return index(request)
            else:
                return render(request, "encyclopedia/yaexiste.html", context)                            
            #return HttpResponseRedirect('/Gracias/')
        else:
            return render(request, "encyclopedia/error.html")            
        return render(request, "encyclopedia/crear.html", context)
    else:
        return render(request, "encyclopedia/crear.html", context)  # Estamos aquí


def prueba(request):  
    if request.method == 'GET':     # Los datos se reciben. Ahora es necesario almacenarlos en una variable
        datos = request.GET.get('q')
        return render(request, "encyclopedia/prueba.html" )
    else:
        return render(request, "encyclopedia/error2.html")

def formulario(request):     
    return render(request, "encyclopedia/formulario.html" )
        



