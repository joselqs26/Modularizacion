def dar_de_baja_estudiante_de_curso(curso, estudiante):
    if estudiante in curso.estudiantes.all():
        costo_curso = curso.coste

        estudiante.pagoMatricula -= costo_curso
        estudiante.save()

        curso.estudiantes.remove(estudiante)

        curso.save()

def inscribir_estudiante_en_curso(curso, estudiante):
    costo_curso = curso.coste
    cruce_de_horario = False
    
    horario_nuevo_curso = (curso.inicio_clase, curso.fin_clase)
    horarios_estudiante = consultar_horario_de_estudiante(estudiante)
    
    for horario in horarios_estudiante:
        horario_existente = (horario['inicio_clase'], horario['fin_clase'])
        if (horario_nuevo_curso[0] < horario_existente[1]) and (horario_nuevo_curso[1] > horario_existente[0]):
            cruce_de_horario = True  # Se encontró superposición
    
    if not cruce_de_horario:
        estudiante.pagoMatricula += costo_curso
        estudiante.save()
        
        curso.estudiantes.add(estudiante)

def consultar_horario_de_estudiante(estudiante):
    cursos_inscritos = estudiante.curso_set.all()
    horarios = []

    for curso in cursos_inscritos:
        horarios.append({
            'curso': curso.nombre,
            'inicio_clase': curso.inicio_clase,
            'fin_clase': curso.fin_clase,
        })

    return horarios