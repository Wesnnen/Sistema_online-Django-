
from django.forms import ModelForm

from cadastro.models import Curso


class CursosForm(ModelForm):
    class Meta:
        model = Curso #referente ao banco de dados
        fields = '__all__'# referente a tudo da tabela (nome, valor)