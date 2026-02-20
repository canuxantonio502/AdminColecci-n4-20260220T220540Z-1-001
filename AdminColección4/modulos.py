from datos import *

def pausar():
    input("\nPresione ENTER para continuar...")
    print("\n" * 3)

def mostrar_menu():
    menu1 = """===========================================
    Administrador de colección
===========================================
1. Añadir un Nuevo Elemento
2. Ver todos los Elementos
3. Buscar un Elemento
4. Editar un Elemento
5. Eliminar un Elemento
6. Ver Elementos por Género
7. Guardar y Cargar Colecciòn
8. Salir
==========================================="""
    print(menu1)


def mostrar_separador():
    print("===========================================")


def pedir_opcion():
    opc = int(input("Selecciona una opción (1-8): "))
    mostrar_separador()
    return opc


def aniadir_elementos_menu():
    menu2 = """=====================================
    Añadir un Nuevo Elemento
=====================================
¿Qué tipo de elemento deseas añadir?
1. Libro
2. Película
3. Música
4. Regresar al Menú Principal
====================================="""
    print(menu2)
    opc2 = int(input("Seleccione una opción (1-4): "))
    return opc2

def aniadir_elementos(opci, datos):
    while True:
        if opci == 1:
            nombre = input("Nombre del libro: ")
            autor = input("Autor del libro: ")
            genero = input("Género del libro: ")
            valoracion = float(input("Valoración del libro: "))

            nuevo = {
                "Nombre": nombre,
                "Creador": autor,
                "Género": genero, 
                "Valoración": valoracion
            }
            datos["Libros"].append(nuevo)
            print("Libro agregado exitosamente.")
            pausar()
            return
        elif opci == 2:
            nombre = input("Nombre de la película: ")
            director = input("Director de la película: ")
            genero = input("Género de la película: ")
            valoracion = float(input("Valoración de la película: "))

            nuevo = {
                "Nombre": nombre,
                "Creador": director,
                "Género": genero, 
                "Valoración": valoracion
            }
            datos["Películas"].append(nuevo)
            print("Película agregada exitosamente.")
            pausar()
            return
        elif opci == 3:
            nombre = input("Nombre de la canción: ")
            artista = input("Artista de la canción: ")
            genero = input("Género de la canción: ")
            valoracion = float(input("Valoración de la canción: "))

            nuevo = {
                "Nombre": nombre,
                "Creador": artista,
                "Género": genero, 
                "Valoración": valoracion
            }
            datos["Canciones"].append(nuevo)
            print("Canción agregada exitosamente.")
            pausar()
            return
        elif opci == 4:
            print("Regresando al Menú Principal.")
            break
        else:
            print("Opción inválida.")
            pausar()
            return


def ver_elementos_menu():
    menu3 = """=====================================
    Ver Todos los Elementos
=====================================
¿Qué categoría deseas ver?
1. Ver Todos los Libros
2. Ver Todas las Pelìculas
3. Ver Toda la Música
4. Regresar al Menú Principal
====================================="""
    print(menu3)
    opc3 = int(input("Seleccione una opción (1-4): "))
    return opc3

def ver_elementos(opci, datos):
        if opci == 1:
            categoria = "Libros"
        elif opci == 2:
            categoria = "Películas"
        elif opci == 3:
            categoria = "Canciones"
        elif opci == 4:
            print("Regresando al Menù Principal")
            return
        else:
            print("Opción inválida.")
            return
        
        lista = datos[categoria]
        if not lista:
            print("No hay elementos en esta lista.")
            return
        print(f"\nElementos en {categoria}:\n")
        for i, elemento in enumerate(lista, start=1):
            print(f"{i}.")
            print(f"    Nombre: {elemento['Nombre']}")
            print(f"    Creador: {elemento['Creador']}")
            print(f"    Género: {elemento['Género']}")
            print(f"    Valoración: {elemento['Valoración']}")
        pausar()

def buscar_elemento_menu():
    menu4 = """===========================================
    Buscar un Elemento
===========================================
¿Cómo deseas buscar?
1. Buscar por Título
2. Buscar por Autor/Director/Artista
3. Buscar por Género
4. Regresar al Menú Principal
==========================================="""
    print(menu4)
    opc4 = int(input("Selecciona una opción (1-4):"))
    return opc4

def buscar_elemento(opci, datos):
    if opci == 1:
        campo = "Nombre"
        valor = input("Ingrese el nombre a buscar: ").lower()
    elif opci == 2:
        campo = "Creador"
        valor = input("Ingrese el autor/director/artista a buscar: ").lower()
    elif opci == 3:
        campo = "Género"
        valor = input("Ingrese el nombre a buscar: ").lower()
    elif opci == 4:
        print("Regresando al Menù Principal")
        return
    else:
        print("Opción inválida.")
        return
        
    encontrado = False

    for categoria in datos:
        for elemento in datos[categoria]:

            if valor in elemento[campo].lower():
                print("\n====================================")
                print(f"Categoría: {categoria}")
                print(f"Nombre: {elemento['Nombre']}")
                print(f"Creador: {elemento['Creador']}")
                print(f"Género: {elemento['Género']}")
                print(f"Valoración: {elemento['Valoración']}")
                encontrado = True
                pausar()

    if not encontrado:
        print("No se encontraron coincidencias.")
        pausar()


# def editar_elemento_menu():
#     menu5 = """===========================================
#     Editar un Elemento
# ===========================================
# ¿Qué tipo de cambio deseas realizar?
# 1. Editar Título
# 2. Editar Autor/Director/Artista
# 3. Editar Género
# 4. Editar Valoración
# 5. Regresar al Menú Principal
# ==========================================="""
#    print(menu5)
#    opc5 = int(input("Selecciona una opción (1-5):"))
#    return opc5

def editar_elemento(datos):
    nombre_buscar = input("Ingrese el elemento a editar: ").lower()

    for categoria in datos:
        for elemento in datos[categoria]:
            if nombre_buscar == elemento["Nombre"].lower():

                print("Elemento encontrado: ")
                print(f"1. Nombre: {elemento['Nombre']}")
                print(f"2. Creador: {elemento['Creador']}")
                print(f"3. Género: {elemento['Género']}")
                print(f"4. Valoración: {elemento['Valoración']}")

                opcion = int(input("\n¿Qué desea editar? (1-4)"))

                if opcion == 1:
                    elemento["Nombre"] = input("Nuevo nombre: ")
                elif opcion == 2:
                    elemento["Creador"] = input("Nuevo autor: ")
                elif opcion == 3:
                    elemento["Género"] = input("Nuevo género: ")
                elif opcion == 4:
                    elemento["Valoración"] = float(input("Nueva valoración: "))
                else:
                    print("Opción inválida.")
                    return
                
                mostrar_separador()
                print("Elemento actualizado correctamente.")
                pausar()
                return
            
    print("No se encontró el elemento descrito.")
    pausar()


def eliminar_elemento_menu():
    menu6 = """===========================================
    Eliminar un Elemento
===========================================
¿Cómo deseas eliminar?
1. Eliminar por Título
2. Eliminar por Identificador Único
3. Regresar al Menú Principal
==========================================="""
    print(menu6)
    opc6 = int(input("Selecciona una opción (1-3):"))
    return opc6

def eliminar_elemento(opci, datos):
        if opci == 1:

            nombre_buscar = input("Ingrese el nombre del elemento a eliminar: ").lower()

            for categoria in datos:
                for i, elemento in enumerate(datos[categoria]):
                    if nombre_buscar == elemento["Nombre"].lower():

                        print("\nElemento encontrado: ")
                        print(f"1. Nombre: {elemento['Nombre']}")
                        print(f"2. Creador: {elemento['Creador']}")
                        print(f"3. Género: {elemento['Género']}")
                        print(f"4. Valoración: {elemento['Valoración']}")

                        confirmacion = input("\n¿Está seguro de eliminarlo (S/N):").lower()

                        if confirmacion == "s" or "si":
                            datos[categoria].pop(i)
                            print("Elemento eliminado correctamente.")
                            pausar()
                        else:
                            print("Eliminaciòn cancelada")
                            pausar()

                        return
            
            print("No se encontró el elemento.")
            pausar()

        elif opci == 2:
            nombre_buscar = input("Ingrese el nombre del elemento a eliminar: ").lower()

            for categoria in datos:
                for i, elemento in enumerate(datos[categoria]):
                    if nombre_buscar == elemento["Nombre"].lower():

                        print("\nElemento encontrado: ")
                        print(f"1. Nombre: {elemento['Nombre']}")
                        print(f"2. Creador: {elemento['Creador']}")
                        print(f"3. Género: {elemento['Género']}")
                        print(f"4. Valoración: {elemento['Valoración']}")

                        confirmacion = input("\n¿Está seguro de eliminarlo (S/N):").lower()

                        if confirmacion == "s":
                            datos[categoria].pop(i)
                            print("Elemento eliminado correctamente.")
                            pausar()
                        else:
                            print("Eliminaciòn cancelada")
                            pausar()

                        return
            
            print("No se encontró el elemento.")
            pausar()
        elif opci == 3:
            print("Regresando al Menù Principal")
            return
        else:
            print("Opción inválida.")
            pausar()


def ver_categorias_menu():
    menu7 = """===========================================
    Ver Elementos por Categoría
===========================================
¿Qué categoría deseas ver?
1. Ver Libros
2. Ver Películas
3. Ver Música
4. Regresar al Menú Principal
==========================================="""
    print(menu7)
    opc7 = int(input("Selecciona una opción (1-4):"))
    return opc7

def ver_categorias(opci, datos):

    mapa = {
        1: "Libros",
        2: "Películas",
        3: "Canciones"
    }

    if opci == 4:
        print("Regresando al menú principal.")
        return
    
    categoria = mapa.get(opci)

    if not categoria:
        print("Opción inválida.")
        pausar()
        return        ################################
    
    lista = datos[categoria]

    if not lista:
        print("No hay elementos en esta categoría.")
        pausar()
        return
    
    generos = set()

    for elemento in lista:
        generos.add(elemento["Género"])

    print(f"\nGéneros disponibles en {categoria}: ")
    for genero in sorted(generos):
        print(f"\n- {genero}")

    genero_buscar = input("\nIngrese el género que desea filtrar: ").lower()

    encontrados = False

    print(f"\nResultados:\n")

    for elemento in lista:
        if genero_buscar in elemento["Género"].lower():
            print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
            print(f"1. Nombre: {elemento['Nombre']}")
            print(f"2. Creador: {elemento['Creador']}")
            print(f"3. Género: {elemento['Género']}")
            print(f"4. Valoración: {elemento['Valoración']}")
            encontrados = True
    pausar()

    if not encontrados:
        print("No se encontraron elementos con ese género.")
        pausar()


def guardar_cargar_menu():
    menu8 = """===========================================
    Guardar y Cargar Colección
===========================================
¿Qué deseas hacer?
1. Guardar la Colección Actual
2. Cargar una Colección Guardada
3. Regresar al Menú Principal
==========================================="""
    print(menu8)
    opc8 = int(input("Selecciona una opción (1-3):"))
    return opc8

def guardar_cargar(opci, datos):

        if opci == 1:
            guardar_datos(datos)
            print("Datos guardados correctamente.")
            pausar()
            return datos
        
        elif opci == 2:
            datos = cargar_datos()
            print("Colecciòn cargada correctamente.")
            pausar()
            return datos
        
        elif opci == 3:
            print("Regresando al Menù Principal")
            return datos
        
        else:
            print("Opción inválida.")
            return datos