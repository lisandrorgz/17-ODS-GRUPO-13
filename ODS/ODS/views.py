from django.shortcuts import render

def inicio(request):
    return render(request, 'inicio.html')

def login(request):
    x = request.GET.get("username", None)
    print(x)
    return render(request, 'login.html')
