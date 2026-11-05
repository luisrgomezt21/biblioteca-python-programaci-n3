import json
import os

ARCHIVO_DATOS = "datos/libros.json"

def cargar_datos():

    if not os.path.exists(ARCHIVO_DATOS):
        return []
    try:
        with open(ARCHIVO_DATOS, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def guardar_datos(libros):

    os.makedirs("datos", exist_ok=True)
    with open(ARCHIVO_DATOS, "w", encoding="utf-8") as archivo:
        json.dump(libros, archivo, indent=4, ensure_ascii=False)