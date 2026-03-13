# 🧾 Sistema de Inventario en Python

Un programa simple de **gestión de inventario en consola** desarrollado en **Python**.  
Permite agregar productos, visualizar el inventario, vender productos y mostrar un resumen de transacciones.

Este proyecto es ideal como **práctica para principiantes** que están aprendiendo:
- Variables
- Diccionarios
- Listas
- Funciones
- Validación de datos
- Bucles (`while`)
- Manejo de errores (`try / except`)

---

# 📦 Características

El sistema permite:

✔ Agregar nuevos productos al inventario  
✔ Actualizar la cantidad de productos existentes  
✔ Registrar ventas  
✔ Mostrar el inventario actual  
✔ Guardar un historial de transacciones  
✔ Calcular el valor total del inventario  

---

# 🛠 Tecnologías utilizadas

- **Python 3**
- Ejecución en **terminal / consola**
- Uso de estructuras de datos:
  - Diccionarios
  - Listas

---

# 📂 Estructura del programa

El programa utiliza dos estructuras principales:

```python
inventario = {}
transacciones = []

#Inventario

Diccionario que almacena los productos.

Ejemplo:

{
    "Manzana": {"cantidad": 10, "precio": 2.5},
    "Banana": {"cantidad": 20, "precio": 1.5}
}

#transacciones

Lista que guarda el historial de operaciones realizadas.

Ejemplo:

[
 "Creado producto Manzana con 10 unidades a 2.5",
 "Vendido 2 de Manzana por 5.0"
]
