from django.shortcuts         import render
from django.views.generic     import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm

class ListarAdmin(ListView):
    template_name = "templates/foroadmin.html"
    model = Post
    form_class = PostForm

    def get_queryset(self):
        return Post.objects.all()

class CrearAdmin(CreateView):
    template_name = "templates/crearpostadmin.html"
    model = Post
    form_class = PostForm


