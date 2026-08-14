# 1) Hacer un programa que gestiones datos para una escuela. El programa tiene que ser capaz
# de:
# a) Llevar un registro de todos los datos de alumnos de la escuela (Nombre, Apellido,
# fecha de nacimiento, DNI, Nombre de Tutor, registro de todas las notas, cantidad de
# faltas, cantidad de amonestaciones recibidas.
# b) Mostrar los datos de cada alumno
# c) Modificar los datos de los alumnos
# d) Agregar alumnos
# e) Expulsar alumnos
# f) Dar Persistencia a los Datos del programa mediante la implementación Archivos
# El trabajo practico se deberá subir a un repositorio de GitHub Publico, y se entregara
# únicamente la dirección del repositorio (No de la pagina).

alumnos = []

while True:
    print("1. Mostrar alumnos")
    print("2. agregar alumnos")
    print("3. modificar alumnos")
    print("4. expulsar alumnos")
    print("5. guardar y salir")
    opcion = input("opcion: ")
    if opcion == "1":
        print(alumnos)
        archivo= open("alumnos.txt" , "r")
        datos = archivo.read()
        archivo.close()
        print(datos)
    elif opcion =="2":
        alumno = {"nombre": input("nombre:"),
        "apellido" : input("apellido:"),
        "fecha": input("fecha de nacimiento: "),
        "dni": input("dni: "),
        "tutor": input("tutor:"),
        "notas": input("notas: "),
        "faltas": input("faltas: "),
        "amonestaciones": input("amonestaciones: ")
        }      
        alumnos.append(alumno)      

    elif opcion =="3":
        dni = input("dni del alumno:")
        for alumno in alumnos:
             if alumno["dni"] == dni:
                alumno["nombre"] = input("nuevo nombre: ")
                alumno["apellido"] = input("nuevo apellido: ")
                alumno["fecha"] = input("nueva fecha: ")
                alumno["tutor"] = input("nuevo tutor: ")
                alumno["notas"] = input("nuevas notas: ")
                alumno["faltas"] = input("nuevas faltas: ")
                alumno["amonestaciones"] = input("nuevas amonestaciones: ")
    elif opcion == "4":
        dni= input("dni del alumno:")
        for alumno in alumnos:
            if alumno["dni"] == dni:
                alumnos.remove(alumno)
    elif opcion == "5":
        archivo = open("alumnos.txt" , "w")
        archivo.write(str(alumnos))
        archivo.close()

        print("datos guardados")
        break
    