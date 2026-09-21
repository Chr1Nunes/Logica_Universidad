Universo = {
    "Estudiantes": {
        "Christian": ["Arquitectura_Computadoras", "Programacion", "Sistemas Computacionales", "Punto de venta"],
        "Luis": ["Programacion", "Electronica", "Clean Code"],
        "Ana": ["Fisica", "Administracion", "Algebra basica"],
        "Maria": ["Arquitectura_Computadoras", "Sistemas Computacionales", "estacion meteorologica"]
    },
    "Profesores": {
        "Lopez": ["Programacion"],
        "Sanchez": ["Fisica"],
        "Gomez": ["Arquitectura_Computadoras", "estacion meteorologica"]
    },
    "Materias": {
        "Fisica": ["207", "08:00"],
        "Programacion": ["Lab4", "10:00", "Python"],
        "Arquitectura_Computadoras": ["204", "12:00", "C#"]
    },
    "Aulas": {
        "207": ["Fisica"],
        "Lab4": ["Programacion"],
        "204": ["Arquitectura_Computadoras"]
    },
    "Carreras": {
        "Administracion": ["Ana"],
        "Sistemas Computacionales": ["Christian", "Maria"],
        "Electronica": ["Luis"]
    },
    "Proyectos": {
        "Punto de venta": ["Dart", "Christian"],
        "estacion meteorologica": ["Python", "Maria"]
    },
    "Horarios": {
        "08:00": ["Fisica"],
        "10:00": ["Programacion"],
        "12:00": ["Arquitectura_Computadoras"]
    },
    "Libros": {
        "Clean Code": ["Luis"],
        "Algebra basica": ["Ana"]
    },
    "Lenguajes": {
        "Dart": ["Punto de venta"],
        "Python": ["Programacion", "estacion meteorologica"],
        "C#": ["Arquitectura_Computadoras"]
    }
}

def Estudiante(x):
    for estudiante, relaciones in Universo["Estudiantes"].items():
        print(estudiante, type(estudiante))
        if estudiante == x:
            return True
    return False

def Profesor(x):
    for profesor, relaciones in Universo["Profesores"].items():
        print(profesor, type(profesor))
        if profesor == x:
            return True
    return False


def Aula(x, y):
    for salon, materias in Universo["Aulas"].items():
        print(salon, type(salon))
        if salon == y:
            for materia in materias:
                print(materia, type(materia))
            if materia == x:
                return True
    return False


def Cursa(x, y):
    for estudiante, datos in Universo["Estudiantes"].items():
        print(estudiante, type(estudiante))
        if estudiante == x:
            for dato in datos:
                print(dato, type(dato))
                if dato == y:
                    return True
    return False

def Carrera(x, y):
    for carrera, estudiantes in Universo["Carreras"].items():
        print(carrera, type(carrera))
        if carrera == y:
            for estudiante in estudiantes:
                print(estudiante, type(estudiante))
                if estudiante == x:
                    return True
    return False

def Horario(x, y):
    for hora, materias in Universo["Horarios"].items():
        print(hora, type(hora))
        if hora == y:
            for materia in materias:
                print(materia, type(materia))
                if materia == x:
                    return True
    return False

def Biblioteca(x, y):
    for libro, estudiantes in Universo["Libros"].items():
        print(libro, type(libro))
        if libro == y:
            for estudiante in estudiantes:
                print(estudiante, type(estudiante))
                if estudiante == x:
                    return True
    return False


# Consultas
print(Estudiante("Christian"))
print(Estudiante("Lopez"))
print()

print(Profesor("Lopez"))
print(Profesor("Ana"))
print()

print(Aula("Programacion", "Lab4"))
print(Aula("Fisica", "Lab4"))
print()

print(Cursa("Christian", "Programacion")) 
print(Cursa("Luis", "Fisica"))
print()

print(Carrera("Christian", "Sistemas Computacionales"))
print(Carrera("Christian", "Administracion"))
print()

print(Horario("Fisica", "08:00"))
print(Horario("Fisica", "20:00"))
print()

print(Biblioteca("Luis", "Clean Code"))
print(Biblioteca("Luis", "Dart"))
