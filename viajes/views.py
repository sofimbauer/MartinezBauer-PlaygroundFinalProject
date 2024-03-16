from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from viajes.models import Cronicas
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class Cronica(ListView):
    model = Cronicas
    context_object_name = 'cronicas'
    template_name = 'viajes/cronicas.html'
    
class CrearCronica(LoginRequiredMixin, CreateView):
    model = Cronicas
    template_name = 'viajes/crear_cronica.html'
    fields = ['destino', 'fecha_viaje', 'autor', 'actividades_realizadas','descripcion', 'postal']
    success_url = reverse_lazy('cronicas')

class EditarCronica(LoginRequiredMixin, UpdateView):
    model = Cronicas
    template_name = 'viajes/editar_cronica.html'
    fields = ['destino', 'fecha_viaje', 'autor', 'actividades_realizadas','descripcion', 'postal']
    success_url = reverse_lazy('cronicas')

class EliminarCronica(LoginRequiredMixin, DeleteView):
    model = Cronicas
    template_name = 'viajes/eliminar_cronica.html'
    success_url = reverse_lazy('cronicas')
    
class DetalleCronica(DetailView):
    model = Cronicas
    template_name = 'viajes/detalle_cronica.html'
