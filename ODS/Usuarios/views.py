from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, PostView, Like, Comment

class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'

class PostDetailView(DetailView):
    model = Post 
    template_name = 'posts/post_detail.html'

class PostCreateView(CreateView):
    model = Post 
    template_name = 'posts/post_create.html'

class PostUpdateView(UpdateView):
    model = Post 
    template_name = 'posts/post_update.html'

class PostDeleteView(DeleteView):
    model = Post 
    template_name = 'posts/post_delete.html'
