import sqlite3


# Función para crear la base de datos y la tabla
def create_database():
    conn = sqlite3.connect('inventory.db')  # Conecta a la base de datos
    cursor = conn.cursor()  # Crea un cursor para ejecutar comandos SQL

    # Ejecuta la sentencia SQL para crear la tabla
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Columna ID, será autoincremental
            name TEXT NOT NULL,  -- Columna nombre del producto
            quantity INTEGER NOT NULL,  -- Columna cantidad de producto
            price REAL NOT NULL  -- Columna precio del producto
        )
    ''')

    conn.commit()  # Guarda los cambios realizados en la base de datos
    conn.close()  # Cierra la conexión con la base de datos


# Función para agregar un producto
def add_product(name, quantity, price):
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO products (name, quantity, price) VALUES (?, ?, ?) 
    ''', (name, quantity, price)) # ? Son marcadores de posición, ayudan a prevenir ataques de inyeccion SQL

    conn.commit()
    conn.close()
    print("Producto agregado exitosamente.")


# Función para listar todos los productos
def list_products():
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')  # Ejecuta la consulta SQL para obtener todos los productos
    products = cursor.fetchall() # Obtiene todos los resultados de la consulta y los guarda en la lista
    conn.close()

    if not products:
        print("No hay productos en el inventario.")
    else:
        for product in products:
            print(f"ID: {product[0]}, Nombre: {product[1]}, Cantidad: {product[2]}, Precio: {product[3]}")


# Función para actualizar un producto
def update_product(product_id, name=None, quantity=None, price=None):
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()

    if name:
        cursor.execute('UPDATE products SET name = ? WHERE id = ?', (name, product_id))
    if quantity is not None:
        cursor.execute('UPDATE products SET quantity = ? WHERE id = ?', (quantity, product_id))
    if price is not None:
        cursor.execute('UPDATE products SET price = ? WHERE id = ?', (price, product_id))

    conn.commit()
    conn.close()
    print("Producto actualizado exitosamente.")


# Función para eliminar un producto
def delete_product(product_id):
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products WHERE id = ?', (product_id,))
    product = cursor.fetchone()

    if product:
        cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
        conn.commit()
        print("Producto eliminado exitosamente.")
    else:
        print(f"No se encontró el producto con ID {product_id}.")

    conn.close()

