# Punto de arranque del sistema de gestion de restaurante
# Demuestra el funcionamiento del sistema con ejemplos de uso

from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.cliente import Cliente

def main():
    """Funcion principal que ejecuta la demostracion del sistema."""

    # Crear una instancia del restaurante
    restaurante = Restaurante("La Buena Mesa")
    print(f"\n!Bienvenido a {restaurante.nombre}!\n")

    # ========== AGREGAR PRODUCTOS AL CATALOGO ==========
    print("Agregando productos al catalogo...")

    # Productos de entrada
    producto1 = Producto(1, "Tabla de Quesos", "Entrada", 12.99)
    producto2 = Producto(2, "Tabla de Embutidos", "Entrada", 14.99)

    # Productos principales
    producto3 = Producto(3, "Filete Mignon", "Plato Principal", 24.99)
    producto4 = Producto(4, "Salmon a la Mantequilla", "Plato Principal", 22.50)
    producto5 = Producto(5, "Pasta Carbonara", "Plato Principal", 16.99)

    # Postres
    producto6 = Producto(6, "Tiramisu", "Postre", 8.50)
    producto7 = Producto(7, "Flan Casero", "Postre", 6.99)

    # Bebidas
    producto8 = Producto(8, "Cafe Expreso", "Bebida", 3.50)
    producto9 = Producto(9, "Jugo Natural", "Bebida", 5.99)
    producto10 = Producto(10, "Vino Tinto", "Bebida", 18.00)

    # Agregar todos los productos al restaurante
    productos_lista = [producto1, producto2, producto3, producto4, producto5,
                       producto6, producto7, producto8, producto9, producto10]

    for producto in productos_lista:
        if restaurante.agregar_producto(producto):
            print(f"  . {producto.nombre} agregado")

    # ========== REGISTRAR CLIENTES ==========
    print("\nRegistrando clientes...")

    cliente1 = Cliente(101, "Juan Perez", "juan@email.com", "555-0101")
    cliente2 = Cliente(102, "Maria Gonzalez", "maria@email.com", "555-0102")
    cliente3 = Cliente(103, "Carlos Lopez", "carlos@email.com", "555-0103")
    cliente4 = Cliente(104, "Ana Martinez", "ana@email.com", "555-0104")

    clientes_lista = [cliente1, cliente2, cliente3, cliente4]

    for cliente in clientes_lista:
        if restaurante.registrar_cliente(cliente):
            print(f"  . {cliente.nombre} registrado")

    # ========== REALIZAR ALGUNAS OPERACIONES ==========
    print("\nRealizando operaciones en el sistema...")

    # Registrar algunas ventas
    restaurante.registrar_venta(101, 1, 1)
    restaurante.registrar_venta(101, 3, 1)
    restaurante.registrar_venta(101, 8, 1)
    restaurante.registrar_venta(102, 4, 2)
    restaurante.registrar_venta(102, 6, 1)
    restaurante.registrar_venta(103, 5, 1)
    restaurante.registrar_venta(103, 10, 1)
    restaurante.registrar_venta(104, 2, 1)
    restaurante.registrar_venta(104, 9, 2)
    print("  . Ventas registradas")

    # Cambiar disponibilidad de un producto
    producto7.cambiar_disponibilidad()
    print(f"  . Disponibilidad de '{producto7.nombre}' modificada")

    # Actualizar contacto de un cliente
    cliente1.actualizar_contacto(email="juan.nuevo@email.com")
    print(f"  . Contacto de {cliente1.nombre} actualizado")

    # ========== MOSTRAR RESULTADOS ==========

    # Mostrar catalogo de productos
    restaurante.mostrar_catalogo_productos()

    # Mostrar clientes registrados
    restaurante.mostrar_clientes_registrados()

    # Mostrar productos disponibles
    print(f"\n{'='*60}")
    print("PRODUCTOS DISPONIBLES")
    print(f"{'='*60}")
    disponibles = restaurante.listar_productos_disponibles()
    for producto in disponibles:
        print(f"  . {producto}")

    # Mostrar productos por categoria
    print(f"\n{'='*60}")
    print("PRODUCTOS - CATEGORIA 'BEBIDA'")
    print(f"{'='*60}")
    bebidas = restaurante.listar_productos_por_categoria("Bebida")
    for bebida in bebidas:
        print(f"  . {bebida}")

    # Mostrar informacion de un cliente especifico
    print(f"\n{'='*60}")
    print(f"INFORMACION DETALLADA - {cliente1.nombre.upper()}")
    print(f"{'='*60}")
    info_cliente = cliente1.obtener_informacion()
    for clave, valor in info_cliente.items():
        print(f"  {clave.capitalize()}: {valor}")

    # Mostrar informacion de un producto especifico
    print(f"\n{'='*60}")
    print(f"INFORMACION DETALLADA - {producto3.nombre.upper()}")
    print(f"{'='*60}")
    info_producto = producto3.obtener_informacion()
    for clave, valor in info_producto.items():
        print(f"  {clave.capitalize()}: {valor}")

    # Mostrar resumen del sistema
    restaurante.mostrar_resumen_sistema()

    # Mostrar representacion en string del restaurante
    print(f"Estado: {restaurante}")

if __name__ == "__main__":
    main()

