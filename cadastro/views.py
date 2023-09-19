
from django.http import HttpResponse
from django.shortcuts import redirect, render
from cadastro.forms import CursosForm

from cadastro.models import Curso

# Create your views here.


def index(request):
    return HttpResponse("Olá, Mundo! Agora estou na web")

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
        pass
    return redirect('listarCursos')



