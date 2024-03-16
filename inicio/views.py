from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def inicio(request):
    return render(request, 'inicio/inicio.html')

@login_required
def acerca_de_mi(request):
    return render(request, 'inicio/acerca_de_mi.html')

