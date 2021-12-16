from django.contrib import admin
from .models import Post, Categoria, User, PostView, Comment, Like 

admin.site.register(Post)
admin.site.register(Categoria)
admin.site.register(User)
admin.site.register(PostView)
admin.site.register(Comment)
admin.site.register(Like)
