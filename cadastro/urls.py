from django.urls import path

from cadastro import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teste', views.teste, name='teste'),
    path('print', views.print_em_html, name='print'),

    #Curso
    path('listar_curso', views.listarCursos, name= 'listarCursos'),
    path('incluir_curso', views.incluirCurso, name='incluirCurso'),
    path('editar_curso/<int:id>', views.editarCurso, name='editarCurso'),
    path('excluir_curso/<int:id>', views.excluirCurso, name='excluirCurso'),
    
    #Turma
    path('listar_turma', views.listarTurmas, name= 'listarTurmas'),

    #aluno
    path('listar_aluno', views.listarAluno, name= 'listarAluno'),
    path('incluir_aluno', views.incluirAluno, name='incluirAluno'),
    path('editar_aluno/<int:id>', views.editarAluno, name='editarAluno'),
    path('excluir_aluno/<int:id>', views.excluirAluno, name='excluirAluno'),

    #Professor
    path('listar_professor', views.listarProfessor, name= 'listarProfessor'),
    path('incluir_professor', views.incluirProfessor, name='incluirProfessor'),
    path('editar_professor/<int:id>', views.editarProfessor, name='editarProfessor'),
    path('excluir_professor/<int:id>', views.excluirProfessor, name='excluirProfessor'),
]
