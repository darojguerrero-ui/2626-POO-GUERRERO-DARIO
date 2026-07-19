"""
Módulo: main.py
Descripción: Punto de entrada del programa. Implementa un menú interactivo que permite
             registrar, listar y buscar productos y clientes del restaurante.
"""

from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def mostrar_menu():
    """
    Muestra el menú principal del sistema de restaurante.
    """
    print("\n" + "=" * 50)
    print("        SISTEMA DE RESTAURANTE".center(50))
    print("=" * 50)
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("-" * 50)
    print("4. Registrar cliente")
    print("5. Listar clientes")
    print("6. Buscar cliente")
    print("-" * 50)
    print("7. Salir")
    print("=" * 50)


def registrar_producto(restaurante):
    """
    Solicita datos al usuario y crea un nuevo producto mediante el constructor.
    
    Args:
        restaurante (Restaurante): Instancia del restaurante
    """
    print("\n--- REGISTRAR PRODUCTO ---")
    try:
        nombre = input("Nombre del producto: ").strip()
        if not nombre:
            print("✗ El nombre no puede estar vacío.")
            return
        
        categoria = input("Categoría (ej: Comida, Bebida, Postre): ").strip()
        if not categoria:
            print("✗ La categoría no puede estar vacía.")
            return
        
        try:
            precio = float(input("Precio: $"))
        except ValueError:
            print("✗ El precio debe ser un número válido.")
            return
        
        # Crear objeto mediante el constructor
        producto = Producto(nombre, categoria, precio)
        
        # Registrar en la clase de servicio
        if restaurante.registrar_producto(producto):
            print(f"✓ Producto '{nombre}' registrado exitosamente.")
        else:
            print(f"✗ El producto '{nombre}' ya existe.")
    
    except ValueError as e:
        print(f"✗ Error: {e}")


def listar_productos(restaurante):
    """
    Lista todos los productos registrados en el restaurante.
    
    Args:
        restaurante (Restaurante): Instancia del restaurante
    """
    print("\n--- LISTAR PRODUCTOS ---")
    productos = restaurante.listar_productos()
    
    if not productos:
        print("No hay productos registrados.")
        return
    
    print(f"\nTotal de productos: {restaurante.obtener_cantidad_productos()}\n")
    for i, producto in enumerate(productos, 1):
        print(f"{i}. {producto.mostrar_informacion()}")
        print("-" * 40)


def buscar_producto(restaurante):
    """
    Busca productos por nombre en el restaurante.
    
    Args:
        restaurante (Restaurante): Instancia del restaurante
    """
    print("\n--- BUSCAR PRODUCTO ---")
    nombre = input("Ingrese el nombre del producto a buscar: ").strip()
    
    if not nombre:
        print("✗ Debe ingresar un nombre para buscar.")
        return
    
    resultados = restaurante.buscar_producto(nombre)
    
    if not resultados:
        print(f"✗ No se encontraron productos con '{nombre}'.")
        return
    
    print(f"\nResultados encontrados: {len(resultados)}\n")
    for i, producto in enumerate(resultados, 1):
        print(f"{i}. {producto.mostrar_informacion()}")
        print("-" * 40)


def registrar_cliente(restaurante):
    """
    Solicita datos al usuario y crea un nuevo cliente mediante @dataclass.
    
    Args:
        restaurante (Restaurante): Instancia del restaurante
    """
    print("\n--- REGISTRAR CLIENTE ---")
    try:
        try:
            id_cliente = int(input("ID del cliente (número): "))
        except ValueError:
            print("✗ El ID debe ser un número entero.")
            return
        
        nombre = input("Nombre del cliente: ").strip()
        if not nombre:
            print("✗ El nombre no puede estar vacío.")
            return
        
        correo = input("Correo electrónico: ").strip()
        if not correo:
            print("✗ El correo no puede estar vacío.")
            return
        
        # Crear objeto usando @dataclass
        cliente = Cliente(id_cliente, nombre, correo)
        
        # Registrar en la clase de servicio
        if restaurante.registrar_cliente(cliente):
            print(f"✓ Cliente '{nombre}' registrado exitosamente.")
        else:
            print(f"✗ El cliente con ID {id_cliente} ya existe.")
    
    except ValueError as e:
        print(f"✗ Error: {e}")


def listar_clientes(restaurante):
    """
    Lista todos los clientes registrados en el restaurante.
    
    Args:
        restaurante (Restaurante): Instancia del restaurante
    """
    print("\n--- LISTAR CLIENTES ---")
    clientes = restaurante.listar_clientes()
    
    if not clientes:
        print("No hay clientes registrados.")
        return
    
    print(f"\nTotal de clientes: {restaurante.obtener_cantidad_clientes()}\n")
    for i, cliente in enumerate(clientes, 1):
        print(f"{i}. {cliente.mostrar_informacion()}")
        print("-" * 40)


def buscar_cliente(restaurante):
    """
    Busca clientes por nombre en el restaurante.
    
    Args:
        restaurante (Restaurante): Instancia del restaurante
    """
    print("\n--- BUSCAR CLIENTE ---")
    nombre = input("Ingrese el nombre del cliente a buscar: ").strip()
    
    if not nombre:
        print("✗ Debe ingresar un nombre para buscar.")
        return
    
    resultados = restaurante.buscar_cliente(nombre)
    
    if not resultados:
        print(f"✗ No se encontraron clientes con '{nombre}'.")
        return
    
    print(f"\nResultados encontrados: {len(resultados)}\n")
    for i, cliente in enumerate(resultados, 1):
        print(f"{i}. {cliente.mostrar_informacion()}")
        print("-" * 40)


def main():
    """
    Función principal que ejecuta el menú interactivo del sistema.
    
    Demuestra el flujo:
    input() → constructor → objeto → registro → consulta
    """
    
    # Crear instancia del restaurante
    restaurante = Restaurante("Restaurant Delicioso")
    
    print("=" * 50)
    print(f"Bienvenido a {restaurante.nombre}".center(50))
    print("=" * 50)
    
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ").strip()
        
        if opcion == "1":
            registrar_producto(restaurante)
        
        elif opcion == "2":
            listar_productos(restaurante)
        
        elif opcion == "3":
            buscar_producto(restaurante)
        
        elif opcion == "4":
            registrar_cliente(restaurante)
        
        elif opcion == "5":
            listar_clientes(restaurante)
        
        elif opcion == "6":
            buscar_cliente(restaurante)
        
        elif opcion == "7":
            print("\n" + "=" * 50)
            print("¡Gracias por usar el sistema de restaurante!".center(50))
            print(f"Productos registrados: {restaurante.obtener_cantidad_productos()}".center(50))
            print(f"Clientes registrados: {restaurante.obtener_cantidad_clientes()}".center(50))
            print("=" * 50)
            print("Hasta luego.")
            break
        
        else:
            print("✗ Opción no válida. Por favor, seleccione una opción del 1 al 7.")


if __name__ == "__main__":
    main()
