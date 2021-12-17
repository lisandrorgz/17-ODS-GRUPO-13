from django.shortcuts import render
from django.urls import reverse_lazy
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
    template_name = 'posts/post_create.html'
    success_url = reverse_lazy('Usuarios:post_list')

class PostUpdateView(UpdateView):
    model = Post 
    template_name = 'posts/post_update.html'

class PostDeleteView(DeleteView):
    model = Post 
    template_name = 'posts/post_delete.html'
