from .                                    import views
from django.conf                          import settings
from django.conf.urls.static              import static
from django.contrib                       import admin
from django.contrib.auth                  import views as auth_views
from django.contrib.auth.views            import logout_then_login
from django.urls                          import path, include
# from Usuarios.views import (
#     PostListView, 
#     PostDetailView, 
#     PostCreateView, 
#     PostUpdateView, 
#     PostDeleteView
# )

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.inicio, name="inicio"),
    path('users/', include('Usuarios.urls', namespace='usuarios')),
    path('accounts/', include('allauth.urls')),
    path('', views.Inicio.as_view(), name="inicio"),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
	path('logout/', auth_views.logout_then_login, name = "logout"),
    path('foro/', views.Foro.as_view(), name="foro" ),
    path('foroadmin/', views.ForoAdmin.as_view(), name="foroadmin")
    # path('', PostListView.as_view(), name='list'),
    # path('<slug>/', PostDetailView.as_view(), name='detail'),
    # path('<slug>/update', PostUpdateView.as_view(), name='update'),
    # path('<slug>/delete', PostDeleteView.as_view(), name='delete'),
    # path('create/', PostCreateView.as_view(), name='create')
]


# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

