# Modulo de la clase Restaurante
# Gestiona los productos y clientes registrados en el sistema

from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    """
    Clase que gestiona las operaciones principales del restaurante.

    Atributos:
        nombre (str): Nombre del restaurante
        productos (list): Lista de productos disponibles
        clientes (list): Lista de clientes registrados
        total_ventas (float): Total acumulado de ventas
    """

    def __init__(self, nombre):
        """
        Constructor de la clase Restaurante.

        Args:
            nombre (str): Nombre del restaurante
        """
        self.nombre = nombre
        self.productos = []
        self.clientes = []
        self.total_ventas = 0.0

    def agregar_producto(self, producto):
        """
        Agrega un nuevo producto al catalogo del restaurante.

        Args:
            producto (Producto): Objeto Producto a agregar

        Returns:
            bool: True si se agrego exitosamente, False si el ID ya existe
        """
        for p in self.productos:
            if p.id_producto == producto.id_producto:
                return False

        self.productos.append(producto)
        return True

    def registrar_cliente(self, cliente):
        """
        Registra un nuevo cliente en el restaurante.

        Args:
            cliente (Cliente): Objeto Cliente a registrar

        Returns:
            bool: True si se registro exitosamente, False si el ID ya existe
        """
        for c in self.clientes:
            if c.id_cliente == cliente.id_cliente:
                return False

        self.clientes.append(cliente)
        return True

    def obtener_producto_por_id(self, id_producto):
        """
        Busca un producto por su ID.

        Args:
            id_producto (int): ID del producto a buscar

        Returns:
            Producto: El objeto producto si existe, None en caso contrario
        """
        for producto in self.productos:
            if producto.id_producto == id_producto:
                return producto
        return None

    def obtener_cliente_por_id(self, id_cliente):
        """
        Busca un cliente por su ID.

        Args:
            id_cliente (int): ID del cliente a buscar

        Returns:
            Cliente: El objeto cliente si existe, None en caso contrario
        """
        for cliente in self.clientes:
            if cliente.id_cliente == id_cliente:
                return cliente
        return None

    def listar_productos_disponibles(self):
        """
        Retorna una lista de todos los productos disponibles.

        Returns:
            list: Lista de productos disponibles
        """
        return [p for p in self.productos if p.disponible]

    def listar_productos_por_categoria(self, categoria):
        """
        Retorna una lista de productos de una categoria especifica.

        Args:
            categoria (str): Categoria de productos a listar

        Returns:
            list: Lista de productos de la categoria especificada
        """
        return [p for p in self.productos if p.categoria == categoria and p.disponible]

    def registrar_venta(self, id_cliente, id_producto, cantidad=1):
        """
        Registra una venta del restaurante.

        Args:
            id_cliente (int): ID del cliente que realiza la compra
            id_producto (int): ID del producto vendido
            cantidad (int): Cantidad de unidades vendidas

        Returns:
            bool: True si la venta se registro exitosamente
        """
        cliente = self.obtener_cliente_por_id(id_cliente)
        producto = self.obtener_producto_por_id(id_producto)

        if cliente and producto and producto.disponible:
            monto_venta = producto.precio * cantidad
            self.total_ventas += monto_venta
            cliente.registrar_pedido(id_producto)
            return True
        return False

    def mostrar_catalogo_productos(self):
        """Muestra el catalogo completo de productos del restaurante."""
        print(f"\n{'='*60}")
        print(f"CATALOGO DE PRODUCTOS - {self.nombre.upper()}")
        print(f"{'='*60}")

        if not self.productos:
            print("No hay productos registrados.")
        else:
            categorias = set(p.categoria for p in self.productos)
            for categoria in categorias:
                print(f"\n{categoria.upper()}")
                print("-" * 60)
                for producto in self.productos:
                    if producto.categoria == categoria:
                        print(f"  {producto}")

    def mostrar_clientes_registrados(self):
        """Muestra la lista de clientes registrados en el restaurante."""
        print(f"\n{'='*60}")
        print(f"CLIENTES REGISTRADOS - {self.nombre.upper()}")
        print(f"{'='*60}")

        if not self.clientes:
            print("No hay clientes registrados.")
        else:
            for cliente in self.clientes:
                print(f"  {cliente}")

    def mostrar_resumen_sistema(self):
        """Muestra un resumen general del sistema del restaurante."""
        print(f"\n{'='*60}")
        print(f"RESUMEN DEL SISTEMA - {self.nombre.upper()}")
        print(f"{'='*60}")
        print(f"Total de productos en catalogo: {len(self.productos)}")
        print(f"Productos disponibles: {len(self.listar_productos_disponibles())}")
        print(f"Total de clientes registrados: {len(self.clientes)}")
        print(f"Total de ventas acumuladas: ${self.total_ventas:.2f}")
        print(f"{'='*60}\n")

    def __str__(self):
        """Representacion en texto del restaurante."""
        return f"Restaurante: {self.nombre} | Productos: {len(self.productos)} | Clientes: {len(self.clientes)}"

