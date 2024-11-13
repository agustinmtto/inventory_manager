# Sistema de Gestión de Inventario en Python

Este proyecto es un **Sistema de Gestión de Inventario** desarrollado en **Python**. El sistema permite agregar, listar, actualizar y eliminar productos de un inventario almacenado en una base de datos SQLite.

## Objetivo del Proyecto

El objetivo principal de este proyecto fue **aprender a trabajar con bases de datos SQL** y aplicar esos conocimientos en un sistema funcional. A través de este proyecto, se ha aprendido a gestionar una base de datos SQLite, realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) y gestionar datos persistentes utilizando SQL.

## Características

- **Agregar productos**: Permite agregar nuevos productos al inventario con nombre, cantidad y precio.
- **Listar productos**: Muestra todos los productos almacenados en el inventario.
- **Actualizar productos**: Permite actualizar la información de un producto, como la cantidad o el precio.
- **Eliminar productos**: Elimina productos del inventario.
- **Base de datos SQLite**: Los productos se almacenan de manera persistente en una base de datos SQLite.

## Tecnologías utilizadas

- **Python**: Lenguaje de programación utilizado para el desarrollo del sistema.
- **SQLite**: Base de datos ligera utilizada para almacenar los datos del inventario.

## Requisitos

- Python 3.x
- Librería `sqlite3` (incluida en la instalación de Python)

## Instrucciones de uso

1. **Clonar el repositorio**:
   
   Para comenzar a usar el sistema, primero clona el repositorio a tu máquina local:

   ```bash
   git clone https://github.com/usuario/mi-repositorio.git
    ```
   2. Crear la base de datos:

      Si es la primera vez que usas el sistema, debes crear la base de datos. Para hacerlo, simplemente ejecuta el script que crea la base de datos e inicializa la tabla de productos:
   ```bash
   python inventory_functions.py
   ```
   3. Ejecutar el sistema:
      
      Luego, ejecuta el script principal para interactuar con el sistema de gestión de inventario:
   ```bash
   python inventory_manager.py
   ```
   4. Opciones disponibles:

      El sistema ofrece un menú de opciones para gestionar los productos. Las opciones incluyen agregar, listar, actualizar y eliminar productos del inventario.


