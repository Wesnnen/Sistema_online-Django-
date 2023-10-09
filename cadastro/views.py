
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from cadastro.forms import AlunoForm, CursosForm, ProfessorForm

from cadastro.models import Aluno, Curso, Professor, Turma

# Create your views here.


def index(request):
    #return HttpResponse("Olá, Mundo! Agora estou na web")
    return render(request, "inicio.html")

def teste(request):
    return HttpResponse("teste")

def print_em_html(request):
    return HttpResponse("<h2>Um título</h2>")

def listarCursos(request):
    cursos = Curso.objects.all().order_by('nome')
    return render(request, "listar_curso.html", {'lista':cursos})

#função que vai no banco de dados e salva 
def incluirCurso(request):
    if request.method == 'POST':
        form = CursosForm(request.POST) # linha que faz a save
        if form.is_valid():
            try:
                form.save() #linha que salva no db
                model = form.instance
                return redirect('listarCursos')
            except:
                pass
    else:
        form = CursosForm()
    return render(request,"incluir_cursos.html", {'form': form })

def editarCurso(request,id):
    curso = Curso.objects.get(codigo = id)
    form = CursosForm(instance=curso)
    if request.method == "POST":
        form = CursosForm(request.POST, instance=curso) # linha que faz a edição
        if form.is_valid():
            try:
                form.save()
                return redirect('listarcursos')
            except:
                pass

    return render(request, "incluir_cursos.html", {'form' : form })


def excluirCurso(request,id):
    curso = Curso.objects.get(codigo = id)
    try:
        curso.delete()
    except:
        messages.error(request, "Não e possivel excluir.")
    return redirect('listarCursos')

def listarTurmas(request):
    turmas = Turma.objects.all()
    return render(request, 'listar_turmas.html', {'turmas' : turmas})



#------------------------------------------------------------------------
#Professor
def listarProfessor(request):
    professor = Professor.objects.all().order_by('Nome')
    return render(request, 'listar_professores.html', {'professor' : professor})

def incluirProfessor(request):
    if request.method == 'POST':
        form = ProfessorForm(request.POST) # linha que faz a save
        if form.is_valid():
            try:
                form.save() #linha que salva no db
                model = form.instance
                return redirect('listarProfessor')
            except:
                pass
    else:
        form = ProfessorForm()
    return render(request,"incluir_professor.html", {'form': form })

def editarProfessor(request, id):
    professor = Professor.objects.get(id = id)
    form = ProfessorForm(instance=professor)
    
    if request.method == "POST":
        form = ProfessorForm(request.POST, instance=professor) # linha que faz a edição
        if form.is_valid():
            try:
                form.save()
                return redirect('listarProfessor')
            except:
                pass

    return render(request, "incluir_professor.html", {'form' : form })


def excluirProfessor(request, id):
    professor = Professor.objects.get(id = id)
    try:
        professor.delete()
    except:
        messages.error(request, "Não e possivel excluir.")
    return redirect('listarProfessor')

#_______________________________________________________________________________
#Aluno
def listarAluno(request):
    aluno = Aluno.objects.all()
    return render(request, 'listar_alunos.html', {'aluno' : aluno})

def incluirAluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST) # linha que faz o save
        if form.is_valid():
            try:
                form.save() #linha que salva no db
                model = form.instance
                return redirect('listarAluno')
            except:
                pass
    else:
        form = AlunoForm()
    return render(request,"incluir_aluno.html", {'form': form })

def editarAluno(request,id):
    aluno = Aluno.objects.get(id = id)
    form = AlunoForm(instance=aluno)
    
    if request.method == "POST":
        form = AlunoForm(request.POST, instance=aluno) # linha que faz a edição
        if form.is_valid():
            try:
                form.save()
                return redirect('listarAluno')
            except:
                pass

    return render(request, "incluir_aluno.html", {'form' : form })

def excluirAluno(request,id):
    aluno = Aluno.objects.get(id = id)
    try:
        aluno.delete()
    except:
        messages.error(request, "Não e possivel excluir.")
    return redirect('listarAluno')

