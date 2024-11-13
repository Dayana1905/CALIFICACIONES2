from django.contrib import admin

# Register your models here.
from django.db import models

class Estudiantes(models.Model):
    cedula = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=30, blank=False)
    apellido = models.TextField()
    edad = models.IntegerField()
    direccion = models.TextField()
    telefono = models.CharField(max_length=16)

    def __str__(self):
        return self.nombre

class Docente(models.Model):
    cedula = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=30, blank=False)
    apellido = models.TextField()

    def __str__(self):
        return self.nombre

class Materia(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True)
    docente = models.ForeignKey(Docente, related_name='materias', on_delete=models.RESTRICT)

    def __str__(self):
        return self.nombre

class Calificaciones(models.Model):
    estudiante = models.ForeignKey(Estudiantes, on_delete=models.RESTRICT)
    materia = models.ForeignKey(Materia, on_delete=models.RESTRICT)
    nota = models.FloatField()

   
