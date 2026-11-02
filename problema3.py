# Función que recibe dos listas de enteros y devuelve un diccionario
# con la intersección, la unión y la diferencia simétrica de los conjuntos.
def operacionesConjuntos (lista1, lista2):

    # Convertimos las listas en conjuntos
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)

    # 1. Intersección: elementos comunes
    interseccion = conjunto1.intersection(conjunto2)

    # 2. Unión: todos los elementos sin duplicados
    union = conjunto1.union(conjunto2)

    # 3. Diferencia simétrica: elementos que están en uno u otro
    # pero no en ambos
    diferenciaSimetrica = conjunto1.symmetric_difference(conjunto2)

    # Creamos el diccionario con los resultados
    resultado = {
        "Intersección": interseccion,
        "Unión": union,
        "Diferencia simétrica": diferenciaSimetrica
    }

    # Devolvemos el diccionario
    return resultado 

# Probamos la función
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

resultado = operacionesConjuntos(lista1, lista2)

# Mostramos los resultados
for operacion, conjunto in resultado.items():
    print(operacion, ":", conjunto)