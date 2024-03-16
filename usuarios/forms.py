from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User

class CreacionDeUsuarios(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {llave: '' for llave in fields}

class EditarPerfil(UserChangeForm):
    password = None 
    email = forms.EmailField(label='Editar email')
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    descripcion = forms.CharField(widget=forms.TextInput)
    avatar = forms.ImageField(required=False)
    link = forms.URLField(required=False, label='Link')
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'avatar', 'link']

class EditarContraseña(PasswordChangeForm):
    old_password= None
    new_password1 = forms.CharField(label='Contraseña nueva', widget=forms.PasswordInput)
    new_password2 = forms.CharField(label='Repetir contraseña nueva', widget=forms.PasswordInput)
    class Meta:
        model= User
        fields = ['new_password1', 'new_password2']