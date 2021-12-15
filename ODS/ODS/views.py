from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from Usuarios.models import BlogUser, Post



class Inicio(TemplateView):
    template_name = "inicio.html"

class Login(TemplateView):
    template_name = "login.html"

class Foro(TemplateView):
    template_name = "foro.html"
    def get_context_data(self, **kwargs):
        context = super(Foro, self).get_context_data(**kwargs)
        context["usuarios"] = BlogUser.objects.all()
        return context 

class ForoAdmin(ListView):
    template_name = "admin/foroadmin.html"
    model = Post

