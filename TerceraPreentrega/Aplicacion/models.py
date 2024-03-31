from django.db import models

# Create your models here.
class Curso (models.Model):
    nombre=models.CharField(max_length=30)
    camada=models.IntegerField()

class Profesores(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    materia=models.CharField(max_length=30)

class Alumnos(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)