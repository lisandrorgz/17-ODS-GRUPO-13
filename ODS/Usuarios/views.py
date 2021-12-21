from django.shortcuts                import render
from django.conf import settings
from django.urls                     import reverse_lazy
from django.contrib.auth.mixins      import LoginRequiredMixin
from django.views.generic            import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models                         import *      #Post, PostView, Like, Comment
from .forms                          import *
from core.mixins                     import AdminRequiredMixins
from ODS                             import settings


class PostListView(LoginRequiredMixin, AdminRequiredMixins, ListView):
    model = Post
    paginate_by = 5
    ordering = ['-fecha_hora']
    template_name = 'posts/post_list.html'

class PostDetailView(DetailView):
    model = Post 
    template_name = 'posts/post_detail.html'


class PostCreateView(LoginRequiredMixin, AdminRequiredMixins, CreateView):
    model = Post
    form_class = PostForm 
    template_name = 'posts/post_form.html'
    success_url = reverse_lazy('usuarios:list')
    # permisos_requeridos=['add_users']

    login_url = settings.LOGIN_URL

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post 
    template_name = 'posts/post_update.html'

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post 
    template_name = 'posts/post_delete.html'

class Registrarme(CreateView):
    model = Usuario
    form_class = UsuarioForm 
    template_name = 'usuarios/registrar.html'

    success_url = reverse_lazy('usuarios:list')

    #def get_success_url(self, **kwargs):
        #return reverse_lazy ('post:post_create.html')

