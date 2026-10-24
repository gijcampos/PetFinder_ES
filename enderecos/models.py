from django.db import models
from usuarios.models import Cadastro as Tutor

class Enderecos(models.Model):
    # Relacionamento entre um Tutor e um endereco
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, related_name='enderecos')

    cep = models.CharField(max_length=9)
    logradouro = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.logradouro}, {self.numero} - {self.cidade}/{self.estado}"