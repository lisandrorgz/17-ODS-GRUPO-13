from django.urls import path
from Usuarios.views import (
     Registrarme,
     PostListView, 
     PostDetailView, 
     PostCreateView, 
#     PostUpdateView, 
#     PostDeleteView
)

app_name = "usuarios"

urlpatterns = [
     path('Registrarme/', Registrarme.as_view(), name='registrarme'),
     path('create', PostCreateView.as_view(), name='create'),
     path('list', PostListView.as_view(), name='list'),
     path('<slug>/', PostDetailView.as_view(), name='detail'),
     # path('<slug>/update', PostUpdateView.as_view(), name='update'),
     # path('<slug>/delete', PostDeleteView.as_view(), name='delete'),
     

]
