# from django.contrib.auth.decorators    import login_required
from django.shortcuts                  import render, redirect, reverse
from django.views.generic.base         import TemplateView
from django.views.generic              import ListView
from Usuarios.models                   import Usuario, Post
from Usuarios.models                   import CommentForm

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

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            form.instance.post = post
            form.save()

            return redirect(reverse('post', kwargs={
                'slug': post.slug
             }))


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["usuarios"] = Usuario.objects.all()
        return context 

class ForoAdmin(ListView):
    template_name = "admin/foroadmin.html"
    model = Post

