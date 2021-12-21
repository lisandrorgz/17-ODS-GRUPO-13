from django.contrib import admin
from .models import Post, Usuario, PostView, Like, Comment  # ,Categoria
admin.site.register(Post)
#admin.site.register(Categoria)
admin.site.register(Usuario)
admin.site.register(PostView)
admin.site.register(Like)
admin.site.register(Comment)