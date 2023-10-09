from django.contrib import admin

from cadastro.models import Aluno, Curso, Professor, Turma

# Register your models here.
admin.site.register(Curso)
admin.site.register(Turma)
admin.site.register(Professor)
admin.site.register(Aluno)
