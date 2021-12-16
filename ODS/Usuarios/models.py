from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import *
from django.db.models.fields.files import ImageField
from .choices import roles, nombres_categorias


class User(AbstractUser):  
    pass

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name='Usuario'
        verbose_name_plural='Usuarios'
        db_table='Usuario'

class Post(models.Model):
    id_post = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo_post = models.CharField(max_length=20, help_text="Maximo 20 caracteres por titulo de Post")
    fecha_hora = models.DateTimeField(verbose_name="FECHA,HORA", auto_now_add=True)
    slug = models.SlugField()
    

    def __str__(self):
        return self.titulo_post

    class Meta:
        verbose_name='Post'
        verbose_name_plural="Post's"
        db_table='Post'

class Comment(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.user.username

class PostView(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username

class Like(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
        
    def __str__(self):
        return self.user.username

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
