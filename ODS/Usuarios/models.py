from django.db import models
from django.db.models.fields import *
from .choices import roles, nombres_categorias

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=30, help_text="Maximo de caracteres permitidos (13)")
    correo = models.CharField(max_length=150, default="EMAIL")
    contraseña = models.CharField(max_length=150)
    rol = models.CharField(max_length=1, choices=roles, blank=True, null=True)
    on_delete = models.PROTECT
    
    def __str__(self):
        return self.nombre_usuario

    class Meta:
        verbose_name='Usuario'
        verbose_name_plural='Usuarios'
        db_table='Usuario'

class Post(models.Model):
    id_post = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo_post = models.CharField(max_length=20, help_text="Maximo 20 caracteres por titulo de Post")
    fecha_hora = models.DateTimeField(verbose_name="FECHA,HORA", auto_now_add=True)

    def __str__(self):
        return self.titulo_post
    
    class Meta:
        verbose_name='Post'
        verbose_name_plural="Post's"
        db_table='Post'

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    id_post = models.ForeignKey(Post, on_delete=models.CASCADE )
    categoria = models.CharField(max_length=2,choices=nombres_categorias)

    def __str__(self):
        return self.categoria
    
    class Meta:
        verbose_name='Categoria'
        verbose_name_plural="Categorias"
        db_table='Categoria'




