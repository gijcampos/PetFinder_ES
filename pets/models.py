from django.db import models
from usuarios.models import Cadastro as Tutor

class Pets(models.Model):
    nome = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    raca = models.CharField(max_length=50, blank=True, null=True)
    idade = models.IntegerField(blank=True, null=True)
    id_disp_rastreamento = models.CharField(max_length=100, blank=True, null=True, unique=True)

    #relaciona um tutor para ter varios pets
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, related_name='pets')

    def __str__(self):
        return f"{self.nome} ({self.especie})"