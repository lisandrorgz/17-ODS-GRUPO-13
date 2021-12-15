from django.shortcuts import render
from django.views.generic.base import TemplateView



class Inicio(TemplateView):
    template_name = "inicio.html"

class Login(TemplateView):
    template_name = "login.html"

class Foro(TemplateView):
    template_name = "foro.html"

