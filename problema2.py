# Importamos librería para interactuar con sistema operativo y rutas de archivos 
import os
# Importamos librería para trabajar con cadenas de caracteres
import string 

# Función que recibe una lista de palabras y la ruta de un fichero.
# Lee y procesa el fichero, eliminando los signos de puntuación,
# convirtiendo el texto a minúsculas y contando las apariciones de cada palabra.
# Devuelve un diccionario con las frecuencias obtenidas, ordenado alfabéticamente.
def frecuenciaPalabras(listaPalabras, rutaFichero):

    # 1. Abrir y leer el fichero
    with open(rutaFichero, "r", encoding="utf-8") as fichero:
        texto = fichero.read()

    # 2. Convertir texto a minúsculas
    texto = texto.lower()

    # 3. Eliminar signos de puntuación
    textoLimpio = texto.translate(str.maketrans('', '', string.punctuation))

    # 4. Crear diccionario de frecuencias
    frecuencia = {}

    for palabra in listaPalabras:
        palabra = palabra.lower()
        frecuencia[palabra] = 0

    # 5. Separar el texto en palabras
    palabrasTexto = textoLimpio.split()

    # 6. Contar las apariciones
    for palabra in palabrasTexto:
        if palabra in frecuencia:
            frecuencia[palabra] += 1

    # 7. Ordenar alfabéticamente
    frecuencia = dict(sorted(frecuencia.items()))

    # 8. Devolver el diccionario
    return frecuencia

# Probamos la función
palabras = ["gatos", "casa", "comida", "jugar", "día", "perros"]

# Construimos la ruta absoluta del archivo de texto para localizarlo en el mismo directorio donde se encuentra el script
ruta = os.path.join(os.path.dirname(os.path.abspath(__file__)), "texto.txt")

# Llamamos a la función con las palabras a contar y la ruta del fichero
resultado = frecuenciaPalabras(palabras, ruta)

# Mostramos palabras y frecuencia
for palabra, frecuencia in resultado.items():
    print(palabra, ":", frecuencia)