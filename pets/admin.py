from django.contrib import admin
from .models import (
    Pet,
    HistoricoLocalizacao,
    Clinica,
    Agendamento,
    Notificacao,
)

admin.site.register(Pet)
admin.site.register(HistoricoLocalizacao)
admin.site.register(Clinica)
admin.site.register(Agendamento)
admin.site.register(Notificacao)

# HorarioFuncionamento e TutorClinica usam PK composta (igual ao Banco_dados.sql),
# que o admin do Django nao suporta. Sao gerenciadas junto com a Clinica/Tutor.
