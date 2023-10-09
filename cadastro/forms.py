
from django.forms import ModelForm

from cadastro.models import Aluno, Curso, Professor


class CursosForm(ModelForm):
    class Meta:
        model = Curso #referente ao banco de dados
        fields = '__all__'# referente a tudo da tabela (nome, valor)

class AlunoForm(ModelForm):
    class Meta:
        model = Aluno #referente ao banco de dados
        fields = '__all__'# referente a tudo da tabela (nome, valor)

class ProfessorForm(ModelForm):
    class Meta:
        model = Professor #referente ao banco de dados
        fields = '__all__'# referente a tudo da tabela (nome, valor)