import json
import os
import requests  # Nueva librería para manejar APIs

class Ingestiones:
    def __init__(self):
        self.ruta_static = "src/pad/static/"

    def leer_json(self):
        """Lee un archivo JSON y lo devuelve como un diccionario."""
        ruta_json = os.path.join(self.ruta_static, "json/datos_persona.json")
        try:
            with open(ruta_json, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {ruta_json}")
            return {}
        except json.JSONDecodeError:
            print(f"Error: El archivo {ruta_json} no es un JSON válido")
            return {}

    def leer_txt(self):
        """Lee un archivo de texto y lo devuelve como una cadena."""
        ruta_txt = os.path.join(self.ruta_static, "txt/info.txt")
        try:
            with open(ruta_txt, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {ruta_txt}")
            return ""

    def leer_varios_txt(self, nombre=""):
        """Lee cualquier archivo de texto dentro de /txt/"""
        ruta_txt = os.path.join(self.ruta_static, "txt", nombre)
        try:
            with open(ruta_txt, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {ruta_txt}")
            return ""

    def leer_api(self, url=""):
        """Consume datos de una API y devuelve el contenido en JSON"""
        if not url:
            print("Error: La URL no puede estar vacía")
            return None
        
        try:
            response = requests.get(url, timeout=5)  # Timeout de 5 segundos
            response.raise_for_status()  # Lanza error si el status es 4xx o 5xx
            return response.json()  # Retorna los datos en formato JSON
        except requests.exceptions.RequestException as e:
            print(f"Error al consumir la API: {e}")
            return None

    def escribir_json(self, datos, nombre="datos_salida.json"):
        """Escribe un diccionario en un archivo JSON"""
        ruta_json = os.path.join(self.ruta_static, "json", nombre)
        try:
            with open(ruta_json, "w", encoding="utf-8") as f:
                json.dump(datos, f, indent=4, ensure_ascii=False)
            print(f"Archivo JSON guardado en: {ruta_json}")
        except Exception as e:
            print(f"Error al escribir JSON: {e}")

    def escribir_txt(self, nombre, datos):
        """Escribe datos en un archivo de texto"""
        ruta_txt = os.path.join(self.ruta_static, "txt", f"{nombre}.txt")
        try:
            with open(ruta_txt, "w", encoding="utf-8") as f:
                if isinstance(datos, list):
                    f.writelines("\n".join(datos))
                else:
                    f.write(str(datos))
            print(f"Archivo guardado en: {ruta_txt}")
        except Exception as e:
            print(f"Error al escribir TXT: {e}")

# Instancia de la clase
inges = Ingestiones()

# Leer JSON
datos_json = inges.leer_json()
print(datos_json)

print("************************************************************")

# Leer TXT
datos_txt = inges.leer_txt()
print(datos_txt)

print("************************************************************")

# Leer otro archivo TXT
nombre_archivo = "info copy.txt"
datos_txt_dos = inges.leer_varios_txt(nombre_archivo)
print(datos_txt_dos)

print("************************************************************")

# Leer datos desde una API pública de ejemplo
api_url = "https://restcountries.com/v3.1/all"
datos_api = inges.leer_api(api_url)
print("Datos obtenidos de la API:", datos_api)

print("************************************************************")

# Guardar datos en archivos TXT y JSON
inges.escribir_txt(nombre="archivo_json", datos=json.dumps(datos_json, indent=4, ensure_ascii=False))
inges.escribir_txt(nombre="archivo_txt", datos=datos_txt)
inges.escribir_txt(nombre="archivo_txt_copy", datos=datos_txt_dos)

# Guardar datos de la API en un JSON
if datos_api:
    inges.escribir_json(datos_api, nombre="datos_api.json")

# final_activity.py
# Ejecutar el script de la actividad_1.py
# prueba final