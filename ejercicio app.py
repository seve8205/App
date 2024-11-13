# Lista para almacenar los productos
productos = []

# Función principal para el sistema de inventario (NO ELIMINAR)
def main():
    # Se inicializa la variable opcion, que va a controlar el menú de opciones
    opcion = 0
    
    # Se define el bucle principal del menú, se repite hasta que la opción seleccionada sea 3 (Salir)
    while opcion != 3:
        # Se muestran las opciones del menú
        print("\n--- Menú de Inventario ---")
        print("1. Agregar producto")  # Opción para agregar un nuevo producto
        print("2. Mostrar productos")  # Opción para mostrar la lista de productos
        print("3. Salir")  # Opción para salir del programa

        # Se solicita al usuario que ingrese una opción
        opcion = int(input("Su opcion: "))

        # Si el usuario elige la opción 1 (Agregar producto)
        if opcion == 1:
            # Se pide al usuario los detalles del producto
            nombre_producto = input("Ingrese el nombre del producto: ")
            stock_producto = int(input("Ingrese la cantidad del producto: "))

            # Se agrega el producto a la lista 'productos' como una lista de dos elementos [nombre, cantidad]
            productos.append([nombre_producto, stock_producto])

            # Se notifica que el producto ha sido agregado
            print("Producto agregado con éxito.")
        
        # Si el usuario elige la opción 2 (Mostrar productos)
        elif opcion == 2:
            # Se verifica si hay productos registrados en la lista
            if len(productos) == 0:
                print("No hay productos registrados.")  # Se imprime si la lista está vacía
            else:
                # Si hay productos, mostrar la lista
                print("\n--- Lista de productos ---")
                # SE recorre la lista de productos y se muestra cada uno
                for i, producto in enumerate(productos):
                    # Se muestra el índice, el nombre y la cantidad de cada producto
                    print("Producto", i + 1, "Nombre:", producto[0], "Cantidad:", producto[1])
        
        # Si el usuario elige la opción 3 (Salir)
        elif opcion == 3:
            print("Saliendo del sistema de inventario...")  # Se ve el mensaje de salida
        else:
            # Si el usuario ingresa una opción inválida
            print("Opción inválida")

    # Se muestra un Mensaje cuando el programa termina
    print("Programa finalizado")

# Ejecución de la función main() - (NO ELIMINAR)
if __name__ == "__main__":
    main()

