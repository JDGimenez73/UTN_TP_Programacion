import time
from ordenamiento import bubble_sort_productos, insertion_sort_productos, merge_sort_productos
from busqueda import busqueda_lineal_productos

# Lista base de productos
productos_base = [
    {"nombre": "Mouse", "precio": 2500},
    {"nombre": "Teclado", "precio": 4500},
    {"nombre": "Monitor", "precio": 32000},
    {"nombre": "Notebook", "precio": 210000},
    {"nombre": "Parlantes", "precio": 7800},
]
# Mostrar productos disponibles
print("\n🛒 Lista de productos disponibles:")
for p in productos_base:
    print(f"- {p['nombre']} (${p['precio']})")
# Solicitar nombre a buscar
nombre_a_buscar = input("🔍 Ingrese el nombre del producto a buscar: ")

# Almacenar resultados por método
resultados = {}

# Insertion Sort
lista = productos_base.copy()
inicio_orden = time.time()
insertion_sort_productos(lista)
fin_orden = time.time()

inicio_busq = time.time()
producto = busqueda_lineal_productos(lista, nombre_a_buscar)
fin_busq = time.time()

resultados["Insertion Sort"] = {
    "ordenamiento": round(fin_orden - inicio_orden, 6),
    "busqueda": round(fin_busq - inicio_busq, 6),
    "encontrado": producto
}

# Bubble Sort
lista = productos_base.copy()
inicio_orden = time.time()
bubble_sort_productos(lista)
fin_orden = time.time()

inicio_busq = time.time()
producto = busqueda_lineal_productos(lista, nombre_a_buscar)
fin_busq = time.time()

resultados["Bubble Sort"] = {
    "ordenamiento": round(fin_orden - inicio_orden, 6),
    "busqueda": round(fin_busq - inicio_busq, 6),
    "encontrado": producto
}

# Merge Sort
lista = productos_base.copy()
inicio_orden = time.time()
lista_ordenada = merge_sort_productos(lista)
fin_orden = time.time()

inicio_busq = time.time()
producto = busqueda_lineal_productos(lista_ordenada, nombre_a_buscar)
fin_busq = time.time()

resultados["Merge Sort"] = {
    "ordenamiento": round(fin_orden - inicio_orden, 6),
    "busqueda": round(fin_busq - inicio_busq, 6),
    "encontrado": producto
}

# Mostrar resultados
print("\n📊 Comparativa por método de ordenamiento:\n")
for metodo, info in resultados.items():
    print(f"🔧 {metodo}:")
    print(f"  ⏱️ Ordenamiento: {info['ordenamiento']} segundos")
    print(f"  🔎 Búsqueda: {info['busqueda']} segundos")
    if info["encontrado"]:
        print(f"  ✅ Producto encontrado: {info['encontrado']['nombre']} (${info['encontrado']['precio']})")
    else:
        print("  ❌ Producto no encontrado.")
    print()
