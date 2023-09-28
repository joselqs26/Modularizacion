def dar_de_baja_estudiante_de_curso(curso, estudiante):
    if estudiante in curso.estudiantes.all():
        costo_curso = curso.coste

        estudiante.pagoMatricula -= costo_curso
        estudiante.save()

        curso.estudiantes.remove(estudiante)

        curso.save()

def inscribir_estudiante_en_curso(curso, estudiante):
    costo_curso = curso.coste
    
    estudiante.pagoMatricula += costo_curso
    estudiante.save()
    
    curso.estudiantes.add(estudiante)

def contratar_profesor_en_curso(curso, profesor):
    despedir_profesor_de_curso(curso)
    
    profesor.sueldo += curso.coste * 0.1 
    profesor.save()

    curso.profesor = profesor
    curso.save()

def despedir_profesor_de_curso(curso):
    profesor = curso.profesor
    
    if profesor:
        profesor.sueldo -= curso.coste * 0.1
        profesor.save()

        curso.profesor = None
        curso.save()
        
        return profesor
    else:
        return None
