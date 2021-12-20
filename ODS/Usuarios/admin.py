from django.contrib import admin
from .models import Post, Usuario, PostView, Comment, Like  # ,Categoria
admin.site.register(Post)
#admin.site.register(Categoria)
admin.site.register(Usuario)
admin.site.register(PostView)
admin.site.register(Comment)
admin.site.register(Like)
