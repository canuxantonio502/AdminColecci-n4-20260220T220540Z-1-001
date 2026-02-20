import json

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
