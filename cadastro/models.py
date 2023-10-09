from django.db import models

# Create your models here.

class Curso(models.Model):
    codigo = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=200, null=False)
    valor = models.DecimalField( max_digits=11,decimal_places=2, null=False)

    def __str__(self):
        return self.nome

class Turma(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING)
    dataInicio = models.DateTimeField(null=False)
    dataTermino = models.DateTimeField(null=False)

    def __str__(self):
        return f"{self.curso.nome} - {self.dataInicio} - {self.dataTermino}"
    

class Professor(models.Model):
    Nome= models.CharField(max_length=150, null=False)
    telefone = models.DecimalField(max_digits=13, decimal_places=0)

    def __str__(self):
        return F"{self.Nome} - {self.telefone}"

class Aluno(models.Model):
    Nome= models.CharField(max_length=150, null=False)
    telefone = models.DecimalField(max_digits=13, decimal_places=0)
    email = models.CharField(max_length=200, null=False)

    def __str__(self):
        return F"{self.Nome} - {self.telefone} - {self.email}"