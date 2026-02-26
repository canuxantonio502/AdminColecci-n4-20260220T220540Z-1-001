from datos import *
from modulos import *

datos = cargar_datos()

while True:
    try:
        mostrar_menu()
        opc = pedir_opcion()
        if opc == 1:
            opci = aniadir_elementos_menu()
            aniadir_elementos(opci, datos)
        elif opc == 2:
            opci = ver_elementos_menu()
            ver_elementos(opci, datos)
        elif opc == 3:
            opci = buscar_elemento_menu()
            buscar_elemento(opci, datos)
        elif opc == 4:
            editar_elemento(datos)
        elif opc == 5:
            opci = eliminar_elemento_menu()
            eliminar_elemento(opci, datos)
        elif opc == 6:
            opci = ver_categorias_menu()
            ver_categorias(opci, datos)
        elif opc == 7:
            opci = guardar_cargar_menu()
            datos = guardar_cargar(opci, datos)
        elif opc == 8:
            estadisticas_generales(datos)
        elif opc == 9:
            print("Gracias por utilizar nuestros servicios...")
            mostrar_separador()
            break
        else:
            print("Opción inválida.")
    except Exception:
         print("ERROR VALUE: Ingrese un caracter válido.")
         pausar()
