from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Form para dar de alta un Post

class NewPost(forms.Form):
    #campos del formulario
    name = forms.CharField(label='Autor')
    title = forms.CharField(label='Titulo')
    place = forms.CharField(label='Nombre del Lugar')
    description = forms.CharField(label='Contanos como estuvo tu viaje')
    img = forms.FileField(label= 'Imagenes', required=False)