from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *      #Post, PostView, Like, Comment
from .forms import *

class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'

class PostDetailView(DetailView):
    model = Post 
    template_name = 'posts/post_detail.html'

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm 
    template_name = 'posts/post_form.html'
    success_url = reverse_lazy('Usuarios:post_list')

class PostUpdateView(UpdateView):
    model = Post 
    template_name = 'posts/post_update.html'

class PostDeleteView(DeleteView):
    model = Post 
    template_name = 'posts/post_delete.html'

class Registrarme(CreateView):
    model = Usuario
    form_class = UsuarioForm 
    template_name = 'usuarios/registrar.html'
    #success_url = reverse_lazy('Usuarios:post_list')

    #def get_success_url(self, **kwargs):
     #   return reverse_lazy ('post:post_create.html')
