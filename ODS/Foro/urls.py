from django.urls import path
from .views import *

app_name = "Foro"

urlpatterns = [
     path('foroadmin', ListarAdmin.as_view(), name='listaradmin'),

]


