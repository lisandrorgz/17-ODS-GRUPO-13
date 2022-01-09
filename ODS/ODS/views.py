# from django.contrib.auth.decorators    import login_required
from django.shortcuts                  import render, redirect, reverse
from django.views.generic.base         import TemplateView
from django.views.generic              import ListView, CreateView
from Usuarios.models                   import Usuario, Post
from Usuarios.models                   import CommentForm
from Usuarios.forms                           import PostForm

# inicio basado en funcion
# @login_required()
# def inicio(request):
#     context = {'17ODS': Usuario.objects.all() }
#     return render(request, "inicio.html", context)

class Inicio(TemplateView):
    template_name = "inicio.html"

class Login(TemplateView):
    template_name = "login.html"
    def get_context_data(self, **kwargs):
        context = super(Login, self).get_context_data(**kwargs)
        context['id'] = self.kwargs.get('id')

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

class ForoAdmin(CreateView):
    template_name = "admin/foroadmin.html"
    model = Post
    context_object_name = "post"

class ForoUsuario(CreateView):
    template_name = "foro.html"
    model = Post
    form_class = PostForm



