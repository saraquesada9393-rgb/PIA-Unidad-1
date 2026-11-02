# Función que recibe una lista de números enteros y devuelve otra lista, 
# ordenada de menor a mayor, sin valores negativos ni repetidos.
def procesarLista(lista):

    # 1. Eliminar números negativos
    listaPositivos = []

    for numero in lista:
        if numero >= 0:
            listaPositivos.append(numero)

    # 2. Eliminar números repetidos
    listaSinRepetidos = []

    for numero in listaPositivos:
        if numero not in listaSinRepetidos:
            listaSinRepetidos.append(numero)

    # 3. Ordenar de menor a mayor
    listaSinRepetidos.sort()

    # 4. Devolver la lista resultante
    return listaSinRepetidos

# Probamos la función
lista = [4, -1, 2, 4, 3, -5, 2]

print(procesarLista(lista))