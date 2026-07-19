from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente

class Restaurante:
    def __init__(self):
        self.productos: list[Producto] = []
        self.clientes: list[Cliente] = []

    def registrar_producto(self, producto: Producto) -> bool:
        """
        Registra un producto (o bebida) en la lista de productos del restaurante.
        Valida que el código del producto no se repita.
        """
        if any(p.codigo == producto.codigo for p in self.productos):
            print(f"Error: Ya existe un producto con el código '{producto.codigo}'.")
            return False
        self.productos.append(producto)
        print(f"Producto '{producto.nombre}' registrado exitosamente.")
        return True

    def listar_productos(self):
        """
        Lista todos los productos (incluyendo bebidas) registrados en el restaurante.
        Utiliza polimorfismo llamando a mostrar_informacion().
        """
        if not self.productos:
            print("\nNo hay productos registrados en el restaurante.")
            return
        print("\n--- Listado de Productos ---")
        for producto in self.productos:
            print(producto.mostrar_informacion())

    def registrar_cliente(self, cliente: Cliente) -> bool:
        """
        Registra un cliente en la lista de clientes del restaurante.
        Valida que la identificación del cliente no se repita.
        """
        if any(c.identificacion == cliente.identificacion for c in self.clientes):
            print(f"Error: Ya existe un cliente con la identificación '{cliente.identificacion}'.")
            return False
        self.clientes.append(cliente)
        print(f"Cliente '{cliente.nombre}' registrado exitosamente.")
        return True

    def listar_clientes(self):
        """
        Lista todos los clientes registrados en el restaurante.
        """
        if not self.clientes:
            print("\nNo hay clientes registrados en el restaurante.")
            return
        print("\n--- Listado de Clientes ---")
        for cliente in self.clientes:
            print(cliente.mostrar_informacion())
