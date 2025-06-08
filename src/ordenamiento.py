def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        clave = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > clave:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = clave
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    medio = len(arr) // 2
    izquierda = merge_sort(arr[:medio])
    derecha = merge_sort(arr[medio:])

    return merge(izquierda, derecha)

def merge(izq, der):
    resultado = []
    i = j = 0

    while i < len(izq) and j < len(der):
        if izq[i] < der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1

    resultado += izq[i:]
    resultado += der[j:]
    return resultado

#Algoritmo de busqueda con productos
def bubble_sort_productos(lista):
    n = len(lista)
    for i in range(n):
        for j in range(n - i - 1):
            if lista[j]["precio"] > lista[j + 1]["precio"]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def insertion_sort_productos(lista):
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        while j >= 0 and lista[j]["precio"] > actual["precio"]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = actual
    return lista

def merge_sort_productos(lista):
    if len(lista) <= 1:
        return lista

    mid = len(lista) // 2
    izq = merge_sort_productos(lista[:mid])
    der = merge_sort_productos(lista[mid:])

    return merge(izq, der)

def merge(izq, der):
    resultado = []
    i = j = 0

    while i < len(izq) and j < len(der):
        if izq[i]["precio"] < der[j]["precio"]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1

    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    return resultado

