from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib. auth import authenticate, login as django_login
from usuarios.forms import CreacionDeUsuarios, EditarPerfil, EditarContraseña
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from usuarios.models import DatosExtras


def login(request):
    formulario = AuthenticationForm()
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            contrasenia = formulario.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contrasenia)
            django_login(request, user)
            return redirect('inicio')
    return render(request, 'usuarios/login.html', {'formulario': formulario})

def registro(request):
    formulario = CreacionDeUsuarios()
    if request.method == 'POST':
        formulario = CreacionDeUsuarios(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('login')
    return render(request, 'usuarios/registro.html', {'formulario': formulario})

def perfil(request):
    return render(request, 'usuarios/perfil.html')

def editar_perfil(request):
    user = request.user
    datos_extra, _ = DatosExtras.objects.get_or_create(user=user)
    if request.method == 'POST':
        formulario = EditarPerfil(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            descripcion = formulario.cleaned_data.get('descripcion')
            link = formulario.cleaned_data.get('link')
            avatar = formulario.cleaned_data.get('avatar')
            if avatar:
                datos_extra.avatar = avatar
            if descripcion:
                datos_extra.descripcion = descripcion
            if link:
                datos_extra.link = link  
            datos_extra.save()
            formulario.save()
            return redirect('perfil')
    else:
        formulario = EditarPerfil(instance=request.user)       
    return render(request, 'usuarios/editar_perfil.html', {'formulario': formulario})

class EditarContraseña(PasswordChangeView):
    template_name = 'usuarios/editar_contraseña.html'
    success_url = reverse_lazy('perfil')
    form_class = EditarContraseña