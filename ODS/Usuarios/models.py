from django.db import models
from django.db.models.fields import CharField, AutoField
from .choices import roles

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=150, default="USERNAME")
    correo = models.CharField(max_length=150, default="EMAIL")
    contraseña = models.CharField(max_length=150, default="PASSWORD")
    rol = models.CharField(max_length=1, choices=roles, default='R')
    on_delete = models.PROTECT
    
    def __str__(self):
        return self.nombre_usuario

    class Meta:
        verbose_name='Usuario'
        verbose_name_plural='Usuarios'
        db_table='Usuario'

class Post(models.Model):
    id_post = models.AutoField(primary_key=True)
    titulo_post = models.CharField(max_length=20, default="TituloPost")
    id_usuario = models.ForeignKey(Usuario, null=True, blank=True,on_delete=models.CASCADE) #el on_delete sirve para que al momento de eliminar un usuario, se elimine el post
    fecha_hora = models.DateTimeField(verbose_name="FECHA,HORA")

    def __str__(self):
        return self.titulo_post
    
    class Meta:
        verbose_name='Post'
        verbose_name_plural="Post's"
        db_table='Post'

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    id_post = models.ForeignKey(Post, null=True, blank=True,on_delete=models.CASCADE)
    nombre_categoria = models.CharField(max_length=150, default="NombreCategoria")

    def __str__(self):
        return self.nombre_categoria
    
    class Meta:
        verbose_name='Categoria'
        verbose_name_plural="Categorias"
        db_table='Categoria'
    




        



        






