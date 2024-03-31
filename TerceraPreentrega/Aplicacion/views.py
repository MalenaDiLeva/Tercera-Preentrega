from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from Aplicacion.models import Curso
from Aplicacion.models import Profesores
from Aplicacion.models import Alumnos
from django.http import HttpResponse
from django.template import loader
from Aplicacion.forms import Curso_formulario
from Aplicacion.forms import Profesores_formulario
from Aplicacion.forms import Alumnos_formulario

# Create your views here.



def inicio(request):
    return render( request , "padre.html")

def ver_cursos(request):
    cursos=Curso.objects.all()
    dicc={"cursos": cursos}
    plantilla=loader.get_template("cursos.html")
    documento=plantilla.render(dicc)
    return HttpResponse(documento)

def alta_curso(request,nombre):
    curso = Curso(nombre=nombre , camada=234512)
    curso.save()
    texto = f"Se guardo en la BD el curso: {curso.nombre} {curso.camada}"
    return HttpResponse(texto)

def ver_alumnos(request):
    alumnos=Alumnos.objects.all()
    dicc={"alumnos": alumnos}
    plantilla=loader.get_template("alumnos.html")
    documento=plantilla.render(dicc)
    return HttpResponse(documento)


def ver_profesores(request):
    profesores=Profesores.objects.all()
    dicc={"profesores": profesores}
    plantilla=loader.get_template("profesores.html")
    documento=plantilla.render(dicc)
    return HttpResponse(documento)


def curso_formulario(request):
    if request.method=="POST":
        mi_formulario=Curso_formulario(request.POST)
        if mi_formulario.is_valid():
            datos=mi_formulario.cleaned_data

            curso=Curso(nombre=datos["nombre"], camada=datos["camada"])
            curso.save()
            return render(request, "formulario.html")

    return render (request, "formulario.html")



def formulario_profesores(request):
    if request.method=="POST":
        formulario=Profesores_formulario(request.POST)
        if formulario.is_valid():
            referencias=formulario.cleaned_data

            profesores=Profesores(nombre=referencias["nombre"], apellido=referencias["apellido"], materia=referencias["materia"])
            profesores.save()
            return render(request, "altaprofesores.html")

    return render (request, "altaprofesores.html")

def alumnos_formulario(request):
    if request.method=="POST":
        form=Alumnos_formulario(request.POST)
        if form.is_valid():
            data=form.cleaned_data

            alumnos=Alumnos(nombre=data["nombre"], apellido=data["apellido"])
            alumnos.save()
            return render(request, "altaalumnos.html")

    return render (request, "altaalumnos.html")




def buscar_curso(request):

    return render(request, "buscar_curso.html")

def buscar(request):
    if request.GET["nombre"]:
            nombre=request.GET["nombre"]
            cursos = Curso.objects.filter(nombre__icontains= nombre)
            return render (request, "resultado_busqueda.html", {"cursos": cursos})

    else:
        return HttpResponse ("Ingrese en nombre del curso")
    

def buscar_alumnos(request):

    return render(request, "buscar_alumnos.html")

def buscar_a(request):
    if request.GET["apellido"]:
            apellido=request.GET["apellido"]
            alumnos = Alumnos.objects.filter(apellido__icontains= apellido)
            return render (request, "busqueda_a.html", {"alumnos": alumnos})

    else:
        return HttpResponse ("Ingrese el nombre del alumno")
    
def buscar_profesores(request):
    return render(request, "buscar_profesores.html")

def buscar_p(request):
    if request.GET["apellido"]:
            apellido=request.GET["apellido"]
            profesores = Profesores.objects.filter(apellido__icontains= apellido)
            return render (request, "busqueda_p.html", {"profesores": profesores})

    else:
        return HttpResponse ("Ingrese el nombre del profesor")

