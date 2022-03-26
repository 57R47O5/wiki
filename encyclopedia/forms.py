from django import forms

# En este archivo definimos todos los formularios a ser utilizados en views.py

# Definimos un form de donde recibiremos la cadena que busca el usuario
class BuscarForm(forms.Form):
    busqueda = forms.CharField(label="Buscar")

# Esta form sirve para ingresar una nueva entrada
class AgregarEntradaForm(forms.Form):  
    titulo = forms.CharField(label="Título")  
    contenido = forms.CharField(label="Contenido", widget=forms.Textarea)