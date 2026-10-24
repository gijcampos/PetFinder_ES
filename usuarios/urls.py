from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login_view, name='login'),
    path('editar/<int:id>/', views.editar_perfil, name='editar_perfil'),
    path('excluir/<int:id>/', views.excluir_perfil, name='excluir_perfil'),
]