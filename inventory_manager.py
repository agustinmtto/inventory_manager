from inventory_functions import create_database, add_product, list_products, update_product, delete_product


def main():
    # Crear la base de datos y la tabla si no existen
    create_database()

    while True:
        print("\nSistema de Gestión de Inventario")
        print("1. Agregar producto")
        print("2. Listar productos")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Salir")

        op = input("Seleccione una opción: ")

        if op == "1":
            name = input("Nombre del producto: ")
            quantity = int(input("Cantidad: "))
            price = float(input("Precio: "))
            add_product(name, quantity, price)

        elif op == "2":
            list_products()

        elif op == "3":
            product_id = int(input("ID del producto a actualizar: "))
            name = input("Nuevo nombre (o Enter para omitir): ")
            quantity = input("Nueva cantidad (o Enter para omitir): ")
            price = input("Nuevo precio (o Enter para omitir): ")

            # version simplificada de los ifs, si no existe la variable, se le asigna None
            update_product(
                product_id,
                name=name if name else None,
                quantity=int(quantity) if quantity else None,
                price=float(price) if price else None
            )

        elif op == "4":
            product_id = int(input("ID del producto a eliminar: "))
            delete_product(product_id)

        elif op == "5":
            print("Saliendo del sistema.")
            break

        else:
            print("Opción no válida, por favor intente de nuevo.")


if __name__ == "__main__":
    main()
