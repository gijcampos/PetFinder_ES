from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_pets, name='listar_pets'),
    path('cadastrar/', views.cadastrar_pets, name='cadastrar_pets'),
]