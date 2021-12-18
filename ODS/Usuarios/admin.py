from django.contrib import admin
from .models import Post, Categoria, Usuario, PostView, Comment, Like 

admin.site.register(Post)
admin.site.register(Categoria)
admin.site.register(Usuario)
admin.site.register(PostView)
admin.site.register(Comment)
admin.site.register(Like)
