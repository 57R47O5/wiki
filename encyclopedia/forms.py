from multiprocessing.sharedctypes import Value
from django import forms

# En este archivo definimos todos los formularios a ser utilizados en views.py

# Definimos un form de donde recibiremos la cadena que busca el usuario
class BuscarForm(forms.Form):
    busqueda = forms.CharField(label="Buscar")

# Esta form sirve para ingresar una nueva entrada o editar una existente
class AgregarEntradaForm(forms.Form):  
    titulo = forms.CharField(label="Título")  
    contenido = forms.CharField(label="Contenido", widget=forms.Textarea)
    tipo = forms.CharField(label='Tipo', widget=forms.HiddenInput, initial="Agregar")

# Esta form sirve para editar una entrada existente
class Editar(forms.Form):
    contenido = forms.CharField(widget=forms.Textarea)