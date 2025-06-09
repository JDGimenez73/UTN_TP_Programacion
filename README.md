# UTN_TP_Programacion
Repositorio destinado a la carrera de programacion

# 🔍 Algoritmos de Búsqueda y Ordenamiento

Este proyecto corresponde al **Trabajo Integrador de la materia Programación I**  
(Tecnicatura Universitaria en Programación a Distancia).

Se desarrolló un caso práctico realista y completo para comparar distintos algoritmos de ordenamiento en Python.  
También se implementó una búsqueda lineal para localizar un producto por nombre.

---

## 📦 Caso Práctico Implementado

### Contexto

Se parte de una lista de productos con nombre y precio, que simula un pequeño catálogo.

### Funcionalidades

- Visualización de productos disponibles.
- Ordenamiento de la lista por precio con 3 algoritmos distintos:
  - **Insertion Sort**
  - **Bubble Sort**
  - **Merge Sort**
- Búsqueda de un producto por nombre usando **búsqueda lineal**.
- Medición de tiempo para:
  - El ordenamiento de la lista
  - La búsqueda del producto

### Comparación interactiva

El usuario elige un producto por su nombre y el sistema:
- Aplica los tres algoritmos de ordenamiento por separado
- Muestra el tiempo tomado por cada uno
- Realiza la búsqueda sobre la lista ordenada y muestra los tiempos

---

## 🧪 Ejemplo de Salida
🛒 Lista de productos disponibles:

Mouse ($2500)

Teclado ($4500)

Monitor ($32000)

Notebook ($210000)

Parlantes ($7800)

🔍 Ingrese el nombre del producto a buscar: Teclado

📊 Comparativa por método de ordenamiento:

🔧 Insertion Sort:
⏱️ Ordenamiento: 0.000013 segundos
🔎 Búsqueda: 0.000002 segundos
✅ Producto encontrado: Teclado ($4500)

🔧 Bubble Sort:
⏱️ Ordenamiento: 0.000018 segundos
🔎 Búsqueda: 0.000003 segundos
✅ Producto encontrado: Teclado ($4500)

🔧 Merge Sort:
⏱️ Ordenamiento: 0.000009 segundos
🔎 Búsqueda: 0.000002 segundos
✅ Producto encontrado: Teclado ($4500)

## 📂 Estructura del Proyecto

├── src/
│ ├── ordenamiento.py # Función Insertion Sort adaptada para productos
│ ├── busqueda.py # Búsqueda lineal por nombre de producto
│ ├── main.py # Caso práctico interactivo (catálogo)
│ └── test_algoritmos.py # Medición de tiempos y rendimiento
│
├── Informe_Trabajo_Integrador.docx # Documento teórico del trabajo
├── requirements.txt # Dependencias mínimas
└── README.md # Este archivo

---

## 🧪 Caso Práctico

- Se creó un catálogo de productos (nombre + precio).
- Se ordenó la lista por precio con `Insertion Sort`.
- Se buscó un producto por su nombre usando búsqueda lineal.
- Se midió el tiempo de ejecución de ambos procesos.
- En un script separado, se generaron listas de hasta 5000 productos para comparar rendimientos.

---

## ▶️ Video explicativo

🎥 Mira la presentación y explicación completa del trabajo en Drive:  
🔗 https://drive.google.com/drive/folders/1lpfo3lyDXjXWgyDJHhrYh5XYw30I7llp

---

---

## ▶️ Cómo ejecutar

1. Clonar el repositorio:
```bash
git clone https://github.com/tu-usuario/algoritmos-busqueda-ordenamiento.git

cd algoritmos-busqueda-ordenamiento/src

Ejecutá el caso práctico
python src/main.py

Ejecutá las pruebas de rendimiento
python src/test_algoritmos.py


📈 Resultados (ejemplo)
| Cantidad de Productos | Tiempo de Ordenamiento | Tiempo de Búsqueda |
| --------------------- | ---------------------- | ------------------ |
| 100                   | 0.0023 s               | 0.00001 s          |
| 500                   | 0.0452 s               | 0.00004 s          |
| 1000                  | 0.1753 s               | 0.00008 s          |
| 5000                  | 4.1810 s               | 0.00041 s          |

🧠 Reflexiones
La comparación ayudó a visualizar el impacto real de la complejidad algorítmica.

Merge Sort fue el más rápido en todos los casos.

La búsqueda lineal demostró ser rápida en listas pequeñas, pero no escalable.

El diseño orientado a un caso real facilitó la comprensión.
