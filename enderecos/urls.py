from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar_endereco, name='cadastrar_endereco'),
    path('editar/<int:id>/', views.editar_endereco, name='editar_endereco'),
    path('excluir/<int:id>/', views.excluir_endereco, name='excluir_endereco')    
]