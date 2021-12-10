from django.shortcuts import render
from Usuarios.models import Usuario

def inicio(request):
    usuarios_ = Usuario.objects.all
    context = {
        'usuarios':usuarios_
    }
    return render(request, 'inicio.html', context)
