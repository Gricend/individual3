from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=100, null=False, blank=False)
    correo = models.EmailField(max_length=100, null=False, blank=False)
    

    def __str__(self):
        return self.nombre