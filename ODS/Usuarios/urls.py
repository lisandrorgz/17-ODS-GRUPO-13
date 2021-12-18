from django.urls                  import path
from Usuarios.views               import (
PostListView, 
PostCreateView,
Registrarme)
# PostDetailView, #  PostUpdateView, # PostDeleteView
                              
app_name = "usuarios"


urlpatterns = [
path('', PostListView.as_view(), name='list'),
# path('<slug>/', PostDetailView.as_view(), name='detail'),
# path('<slug>/update', PostUpdateView.as_view(), name='update'),
# path('<slug>/delete', PostDeleteView.as_view(), name='delete'),
path('create/', PostCreateView.as_view(), name='create'),
path('Registrarme/', Registrarme.as_view(), name='registrarme')

]
