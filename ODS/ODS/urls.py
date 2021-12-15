from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import logout_then_login
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name="inicio"),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
	path('logout/', auth_views.logout_then_login, name = "logout"),
    path('foro/', views.foro, name="foro" )
]
