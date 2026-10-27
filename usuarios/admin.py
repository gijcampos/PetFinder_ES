from django.contrib import admin
from .models import Usuario, Tutor, Endereco

admin.site.register(Usuario)
admin.site.register(Tutor)
admin.site.register(Endereco)

# ContatoEmergencia usa PK composta (igual ao Banco_dados.sql),
# que o admin do Django nao suporta. E gerenciada junto com o Tutor.
