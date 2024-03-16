from django.db import models
from django.contrib.auth.models import User

class DatosExtras(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares', default='default_avatar.jpg', null=True, blank=True)
    link = models.URLField(max_length=300, null=True)
    descripcion = models.TextField(max_length=500, null=True)
    
    def __str__(self):
        return f'Datos extras del usuario {self.user}'

