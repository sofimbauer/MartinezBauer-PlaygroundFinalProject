from django.urls import path
from inicio.views import inicio, acerca_de_mi

urlpatterns = [
    path('', inicio, name='inicio'),
    path('about/', acerca_de_mi, name='acerca_de_mi')
]
