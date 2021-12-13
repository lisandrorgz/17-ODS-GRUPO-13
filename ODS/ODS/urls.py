from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', views.inicio),
    path('login/', views.login)
]
