from django.urls import path
from viajes import views

urlpatterns = [
    path('cronicas/', views.Cronica.as_view(), name='cronicas'),
    path('cronicas/nuevo/', views.CrearCronica.as_view(), name='crear_cronica'),
    path('cronicas/<int:pk>/', views.DetalleCronica.as_view(), name='detalle_cronica'),
    path('cronicas/<int:pk>/editar/', views.EditarCronica.as_view(), name='editar_cronica'),
    path('cronicas/<int:pk>/eliminar/', views.EliminarCronica.as_view(), name='eliminar_cronica')
]
