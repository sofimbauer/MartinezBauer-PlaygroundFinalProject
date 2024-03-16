from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Cronicas(models.Model):
    destino = models.CharField(max_length=20)
    fecha_viaje = models.DateField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    actividades_realizadas = models.CharField(max_length=300)
    descripcion = RichTextField(null=True)
    postal = models.ImageField(upload_to='postales', null=True, blank=True)

    def __str__(self):
        return f'Mi viaje a {self.destino}'
