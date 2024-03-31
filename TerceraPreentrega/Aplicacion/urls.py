from django.urls import path
from.import views

from django.urls import path
from.import views

urlpatterns=[
    path("alta_curso", views.curso_formulario),
    path("", views.inicio, name="home"),
    path("ver_cursos", views.ver_cursos, name="cursos"),
    path("ver_alumnos", views.ver_alumnos, name= "alumnos"),
    path("ver_profesores", views.ver_profesores, name="profesores"),
    path("alta_profesores", views.formulario_profesores),
    path("alta_alumnos", views.alumnos_formulario),
    path("buscar_curso", views.buscar_curso),
    path("buscar", views.buscar),
    path("buscar_alumnos", views.buscar_alumnos),
    path("buscar_a", views.buscar_a),
    path("buscar_profesores", views.buscar_profesores),
    path("buscar_p", views.buscar_p)
   
]