import time
import random
import string
from ordenamiento import insertion_sort_productos
from busqueda import busqueda_lineal_productos

# Generar un nombre aleatorio
def generar_nombre():
    return ''.join(random.choices(string.ascii_uppercase, k=5))

# Generar una lista de productos aleatorios
def generar_productos(n):
    return [{"nombre": generar_nombre(), "precio": random.randint(1000, 50000)} for _ in range(n)]

# Evaluar tiempo para ordenar y buscar sobre listas grandes
def evaluar_rendimiento(n):
    productos = generar_productos(n)
    nombre_objetivo = productos[n // 2]["nombre"]  # Tomar uno existente para asegurar resultado

    # Tiempo de ordenamiento
    inicio_orden = time.time()
    productos_ordenados = insertion_sort_productos(productos.copy())
    fin_orden = time.time()

    # Tiempo de búsqueda
    inicio_busqueda = time.time()
    producto = busqueda_lineal_productos(productos_ordenados, nombre_objetivo)
    fin_busqueda = time.time()

    return {
        "cantidad": n,
        "tiempo_ordenamiento": round(fin_orden - inicio_orden, 6),
        "tiempo_busqueda": round(fin_busqueda - inicio_busqueda, 6),
        "encontrado": producto is not None
    }

# Probar con distintos tamaños
tamaños = [100, 500, 1000, 2000, 5000]
resultados = []

print("\n📊 Comparación de tiempos según cantidad de productos:\n")

for n in tamaños:
    resultado = evaluar_rendimiento(n)
    resultados.append(resultado)
    print(f"- {n} productos → Ordenamiento: {resultado['tiempo_ordenamiento']}s | Búsqueda: {resultado['tiempo_busqueda']}s")



