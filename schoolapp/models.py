from django.db import models
from django.core.exceptions import ValidationError
from .utils import dar_de_baja_estudiante_de_curso, inscribir_estudiante_en_curso, contratar_profesor_en_curso, despedir_profesor_de_curso

class Institucion(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Profesor(models.Model):
    nombre = models.CharField(max_length=255)
    edad = models.IntegerField()
    cedula = models.CharField(max_length=20)
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre
    
    def contratar_profesor_en_curso(self, curso):
        contratar_profesor_en_curso(curso, self)

    def despedir_profesor_de_curso(self, curso):
        return despedir_profesor_de_curso(curso)

class Estudiante(models.Model):
    nombre = models.CharField(max_length=255)
    edad = models.IntegerField()
    cedula = models.CharField(max_length=20)
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    pagoMatricula = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

class Curso(models.Model):
    nombre = models.CharField(max_length=255)
    coste = models.DecimalField(max_digits=10, decimal_places=2)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    estudiantes = models.ManyToManyField(Estudiante)

    def __str__(self):
        return self.nombre
    
    def dar_de_baja_estudiante(self, estudiante):
        dar_de_baja_estudiante_de_curso(self, estudiante)

    def inscribir_estudiante(self, estudiante):
        if estudiante in self.estudiantes.all():
            raise ValidationError("El estudiante ya está inscrito en este curso.")
        
        # Si el estudiante no está inscrito, procede a la inscripción
        inscribir_estudiante_en_curso(self, estudiante)
