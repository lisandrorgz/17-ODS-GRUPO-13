# from django.contrib.auth.decorators    import login_required
from django.shortcuts                  import render
from django.views.generic.base         import TemplateView
from django.views.generic              import ListView
from Usuarios.models                   import Usuario, Post

# inicio basado en funcion
# @login_required()
# def inicio(request):
#     context = {'17ODS': Usuario.objects.all() }
#     return render(request, "inicio.html", context)

class Inicio(TemplateView):
    template_name = "inicio.html"

class Login(TemplateView):
    template_name = "login.html"

class Foro(TemplateView):
    template_name = "foro.html"
    model = Post
    # def get_context_data(self, **kwargs):
    #     context = super(Post, self).get_context_data(**kwargs)
    #     context["usuarios"] = Usuario.objects.all()
    #     return context 

class ForoAdmin(ListView):
    template_name = "admin/foroadmin.html"
    model = Post

