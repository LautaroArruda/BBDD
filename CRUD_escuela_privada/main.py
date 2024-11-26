from BD.conexion import Conexion
import funciones  # Importar el módulo que contiene la función buscarPorDni
import os
def menuPrincipal():
    while True:
        print("\nEscuela Privada")
        print("[1]. Ingresar datos")
        print("[2]. Modificar datos")
        print("[3]. Mostrar datos")
        print("[4]. Eliminar datos")
        print("[5]. Salir")
        opcion = int(input("Seleccione una opción: "))

        if opcion < 1 or opcion > 5:
            print("Opcion incorrecta, ingrese nuevamente")
        elif opcion == 5:
            print("Saliendo del sistema")
            break
        else:
            ejecutarOpcion(opcion)

def ejecutarOpcion(opcion):
    if opcion == 3:  # Mostrar datos
        while True:
            print("\nElija una opción")
            print("[1]. Mostrar todos los datos de alumnos")
            print("[2]. Mostrar todos los datos de profesores")
            print("[3]. Buscar en específico")
            print("[4]. Atrás")
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                print("Ver alumnos")  # Llama a la funcion mostrar todos los alumnos
            elif opcion == 2:
                print("Ver profesores")  # Llama a la funcion mostrar todos los profesores
            elif opcion == 3:  # Buscar en especifico
                while True:
                    print("\n¿De quien quiere ver sus datos?")
                    print("[1]. Alumno")
                    print("[2]. Profesor")
                    print("[3]. Atrás")
                    opcion = int(input("Seleccione una opcion: "))
                    # Buscar datos de alumno
                    if opcion==1:
                        # Limpiar la consola
                        os.system("cls")
                        print("Que datos desea ver?")
                        print("[1]. Buscar por legajo")
                        print("[2]. Buscar por DNI")
                        print("[3]. Buscar por Nombre")         
                        print("[4]. buscar por apellido")
                        print("[5]. Buscar por genero")
                        print("[6]. Volver al menu principal")
                        opcion2 = int(input("Seleccione una opción: "))
                        #Legajo alumno
                        if(opcion2 ==1):
                            comandoSQL = "legajo"
                            dato= input("Ingresar legajo: ")
                            #Legajo alumno
                            if len(dato) !=5 or not dato.isdigit():
                                while(len(dato) !=5 or not dato.isdigit()):
                                    print("El legajo debe contener 5 digitos.")
                                    dato = input("Ingrese el legajo: ")
                            funciones.buscarEspecificoAlumnos(dato, comandoSQL)

                        #DNI alumno
                        elif opcion2 == 2:
                            comandoSQL = "dni"
                            dato = input("Ingrese el DNI: ")
                            if len(dato) !=8 or not dato.isdigit():
                                while(len(dato) !=8 or not dato.isdigit()):
                                    print("El DNI debe contener 8 digitos.")
                                    dato = input("Ingrese el DNI: ")
                            funciones.buscarEspecificoAlumnos(dato, comandoSQL)

                        #Nombre alumno
                        elif opcion2 ==3:
                            comandoSQL="nombre"
                            dato = input("Ingrese el nombre: ")
                            while not dato.replace(" ", "").isalpha() or len(dato.split()) > 3:
                                print("Por favor, solo ingrese caracteres y maximo 3 nombres.")
                                dato = input("Ingresar nombre: ")
                            funciones.buscarEspecificoAlumnos(dato.title(), comandoSQL)

                        #Apellido alumno
                        elif opcion2 ==4:
                            comandoSQL = "apellido"
                            dato= input("Ingresar apellido: ")
                            while not dato.replace(" ", "").isalpha() or len(dato.split()) > 3:
                                print("Por favor, solo ingrese caracteres y maximo 2 apellido.")
                                dato = input("Ingresar apellido: ")
                            funciones.buscarEspecificoAlumnos(dato.title(), comandoSQL)

                        #arreglar validacion de no binario y que solo sean esos generos
                        #Genero alumno
                        if opcion2 == 5:
                            comandoSQL = "genero"
                            dato.title= input("Ingresar genero (masculino, femenino, transgero y no binario): ")
                            while not dato.replace(" ", "").isalpha() or not (dato.title == "masculino" or dato.title == "femenino" or dato.title == "transgero" or dato.title == "no binario"):
                                print("Porfavor solo ingresar caracteres.")
                                dato= input("Ingresar genero (masculino, femenino, transgero y no binario): ")
                            funciones.buscarEspecificoAlumnos(dato, comandoSQL)

                    elif opcion == 2:
                        # Limpiar la consola
                        os.system("cls")
                        print("Que datos desea ver?")
                        print("[1]. Buscar por legajo")
                        print("[2]. Buscar por DNI")
                        print("[3]. Buscar por Nombre")
                        print("[4]. buscar por apellido")
                        print("[5]. Buscar por matricula")
                        print("[6]. Volver al menu principal")
                        opcion2 = int(input("Seleccione una opción: "))

                        #Legajo profesor
                        if opcion2 == 1 :
                            comandoSQL = "idProfesor"
                            dato = input ("Ingresar legajo: ")
                            while(not dato.isdigit()):
                                print("porfavor solo ingresar numeros")
                                dato = input ("Ingresar legajo: ")
                            funciones.buscarEspecificoProfesor(dato, comandoSQL)
                                
                        #DNI profesor
                        elif opcion2 == 2 :
                            comandoSQL = "dni"
                            dato = input("Ingresar DNI: ")
                            if  len(dato) !=8 or not dato.isdigit():
                                while(len(dato) !=8 or not dato.isdigit()):
                                    print("El legajo debe contener 8 digitos.")
                                    dato = input("Ingrese el legajo: ")
                            funciones.buscarEspecificoProfesor(dato, comandoSQL)

                        #Nombre profesor
                        elif opcion2 == 3 :
                            comandoSQL = "nombre"
                            dato = input("Ingresar nombre: ")
                            while not dato.replace(" ", "").isalpha() or len(dato.split()) > 3:
                                print("Por favor, solo ingrese caracteres y maximo 3 nombres.")
                                dato = input("Ingresar nombre: ")
                            funciones.buscarEspecificoProfesor(dato.title(), comandoSQL)

                        #Apellido profesor
                        elif opcion2 == 4 :
                            comandoSQL = "apellido"
                            dato = input("Ingresar apellido")
                            while not dato.replace(" ", "").isalpha() or len(dato.split()) > 3:
                                print("Por favor, solo ingrese caracteres y maximo 2 apellido.")
                                dato = input("Ingresar apellido: ")
                            funciones.buscarEspecificoProfesor(dato.title(), comandoSQL)
                        
                        #Matricula profesor
                        elif opcion2 == 5 :
                            comandoSQL = "matricula"
                            dato = input("Ingresar matricula: ")
                            if  len(dato) !=8 or not dato.isdigit():
                                while(len(dato) !=8 or not dato.isdigit()):
                                    print("El legajo debe contener 8 digitos.")
                                    dato = input("Ingrese el legajo: ")
                            funciones.buscarEspecificoProfesor(dato, comandoSQL)

    elif opcion == 4:  # Eliminar datos
        while True:
            print("\n¿A quién desea dar de baja?")
            print("[1]. Dar de baja a un alumno")
            print("[2]. Dar de baja a un profesor")
            print("[3]. Atras")
            opcion = int(input("Seleccione una opción: "))
            #Eliminar Alumno
            if opcion == 1:
                funciones.motrarAlumnos()
                dato = input("Ingrese el legajo del Alumno que desea eliminar: ")
                while dato.isdigit() != True:
                    print("El Legajo tiene que contener solo 5 numeros enteros")
                    dato = input("Ingrese el Legajo del Alumno que desea eliminar: ")
                funciones.eliminarAlumno(dato)
            #Eliminar Profesor                
            elif opcion ==2:    
                funciones.motrarProfes()
                dato = input("Ingrese el ID del Profesor que desea eliminar: ")
                while dato.isdigit() != True:
                    print("El id tiene que contener solo numeros enteros")
                    dato = input("Ingrese el ID del Profesor que desea eliminar: ")   
                funciones.eliminarProfe(dato)
            #Volver al menu principal 
            elif opcion == 3:
                print("Volviendo al menú principal")
                break
            else:
                print("Opcion no valida")
# Ejecutar el menu principal
menuPrincipal()
