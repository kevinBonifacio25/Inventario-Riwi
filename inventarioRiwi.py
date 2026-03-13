

inventario = {}         
transacciones = []       

def agregar_producto():
    while True:
        nombre = input("Nombre del producto: ").strip()
        if nombre.isalpha():
            print(f"Nombre válido: {nombre}")
            break
        else:
            print("Error: Solo se permiten letras (a-z, A-Z). Inténtalo de nuevo.")
        

    if nombre in inventario:
        print("El producto ya existe. Se actualizará la cantidad.")

        while True:
            try:
                cantidad = int(input("Cantidad a agregar: "))
                if cantidad <= 0:
                    print("La cantidad debe ser mayor que 0.")
                    continue
                break
            except ValueError:
                print("Cantidad inválida.")
                
            
            
        inventario[nombre]["cantidad"] += cantidad
        transacciones.append(f"Agregado {cantidad} unidades a {nombre}")
    else:
        while True:
            try:
                cantidad = int(input("Cantidad a agregar: "))
                if cantidad <= 0:
                    print("La cantidad debe ser mayor que 0.")
                    continue
                break
            except ValueError:
                print("Cantidad inválida.")
        while True:       
            try:
                precio = float(input("Precio por unidad: "))
                if precio <= 0:
                    print("El precio debe ser mayor que 0.")
                    continue
                break
            except ValueError:
                print("Precio inválido.")



        inventario[nombre] = {"cantidad": cantidad, "precio": precio}
        transacciones.append(f"Creado producto {nombre} con {cantidad} unidades a {precio}")
    print("/n")
    print("producto agregado exitosamente.")        


def mostrar_inventario():
    if not inventario:
        print("No hay productos en el inventario.")
        return
    print("--- Inventario actual ---")
    for nombre, datos in inventario.items():
        print(f"- {nombre}: {datos['cantidad']} unidades, precio: {datos['precio']}")
    print("/n")

def vender_producto():

    while True:
        nombre = input("Producto a vender: ").strip()
        if nombre.isalpha():
            print(f"Nombre válido: {nombre}")
            break
        else:
            print("Error: Solo se permiten letras (a-z, A-Z). Inténtalo de nuevo.")
            
    
    if nombre not in inventario:
        print("Ese producto no existe.")
        return
    
    while True:
        try:
            cantidad = int(input("Cantidad a vender: "))
            if cantidad <= 0:
                print("La cantidad debe ser mayor que 0.")
                continue
            break
        except ValueError:
            print("Cantidad inválida.")
        
    stock_actual = inventario[nombre]["cantidad"]
    precio = inventario[nombre]["precio"]

    if cantidad <= 0:
        print("La cantidad debe ser mayor que 0.")
        return
    if cantidad > stock_actual:
        print("No hay suficiente stock.")
        return

    inventario[nombre]["cantidad"] -= cantidad
    total_venta = cantidad * precio
    print(f"Venta realizada. Total: {total_venta}")
    transacciones.append(f"Vendido {cantidad} de {nombre} por {total_venta}")

def mostrar_resumen():
    print("RESUMEN DE TRANSACCIONES")
    if not transacciones:
        print("No se realizaron transacciones.")
    else:
        for t in transacciones:
            print("- " + t)

    # Valor total del inventario actual
    valor_total = 0
    for nombre, datos in inventario.items():
        valor_total += datos["cantidad"] * datos["precio"]
    print(f"Valor total del inventario actual: {valor_total}")
    print("/n")

def menu():
    while True:
        print("MENÚ ")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Vender producto")
        print("4. Mostrar resumen y salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            vender_producto()
        elif opcion == "4":
            mostrar_resumen()
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


menu()
