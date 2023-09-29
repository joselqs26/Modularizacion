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
