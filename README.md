Sistema de Gestión de Inventario

Un sistema de inventario simple y funcional desarrollado en Python. Permite agregar productos, realizar ventas, consultar el inventario actual y revisar el historial de transacciones.
✨ Características

    Gestión de productos: Agregar nuevos productos o actualizar cantidades existentes

    Control de stock: Validación automática de stock disponible

    Ventas: Registro de ventas con cálculo automático del total

    Historial completo: Seguimiento de todas las transacciones realizadas

    Validaciones robustas: Entrada de datos segura con manejo de errores

    Interfaz de consola intuitiva: Menú interactivo fácil de usar

📋 Funcionalidades
Opción	Descripción
1. Agregar producto	Crea productos nuevos o suma cantidad a existentes
2. Mostrar inventario	Lista todos los productos con stock y precios
3. Vender producto	Registra ventas respetando el stock disponible
4. Mostrar resumen	Historial de transacciones + valor total del inventario
🚀 Requisitos

    Python 3.6 o superior

    No requiere librerías externas

🛠️ Instalación

    Clona o descarga el repositorio

    Abre la terminal en la carpeta del proyecto

    Ejecuta: python inventario.py

📖 Ejemplo de Uso

text
MENÚ
1. Agregar producto
2. Mostrar inventario
3. Vender producto
4. Mostrar resumen y salir
Elige una opción: 1
Nombre del producto: Camisa
Cantidad a agregar: 50
Precio por unidad: 25.50
producto agregado exitosamente.

🧪 Ejemplo de Salida - Inventario

text
--- Inventario actual ---
- Camisa: 50 unidades, precio: 25.5
- Pantalon: 30 unidades, precio: 45.0

🔒 Validaciones Implementadas

    Nombres solo con letras (a-z, A-Z)

    Cantidades y precios mayores a 0

    Stock suficiente para ventas

    Manejo de entradas inválidas

📊 Resumen de Transacciones

El sistema mantiene un registro completo de:

text
- Creado producto Camisa con 50 unidades a 25.5
- Vendido 5 de Camisa por 127.5
- Agregado 20 unidades a Camisa
Valor total del inventario actual: 2000.5
