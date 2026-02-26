import json
from modulos import pausar

ruta = "coleccion.json"

def cargar_datos():
    try:
        with open (ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {
            "Libros": [],
            "Películas": [],
            "Canciones": []
        }
    
def guardar_datos(datos):
    with open (ruta, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)


def estadisticas_generales(datos):

    total_elementos = 0
    suma_valoraciones = 0

    libros = len(datos["Libros"])
    peliculas = len(datos["Películas"])
    musica = len(datos["Canciones"])

    total_elementos = libros + peliculas + musica

    for categoria in datos:
        for elemento in datos[categoria]:
            suma_valoraciones += elemento["Valoración"]

    if total_elementos > 0:
        promedio = round(suma_valoraciones / total_elementos, 2)
    else:
        promedio = 0

    estadisticas = {
        "total": total_elementos,
        "libros": libros,
        "peliculas": peliculas,
        "musica": musica,
        "promedio_valoraciones": promedio
    }

    with open("estadisticas.json", "w", encoding="utf-8") as archivo:
        json.dump(estadisticas, archivo, indent=4, ensure_ascii=False)

    print("Estadísticas guardadas en 'estadisticas.json'.")
    pausar()