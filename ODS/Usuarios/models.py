from django.db import models
from django.db.models.fields import CharField

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField('Nombre de usuario', max_length=100, blank=False)
    contraseña = models.CharField('Contraseña',max_length=100, blank=False)
    rol = models.CharField('Rol de usuario', max_length=100, blank=False)
    fecha_de_creacion = models.DateField('Fecha creacion', auto_now=False, auto_now_add=True)
    
    def __str__(self):
        return self.nombre_usuario
        






