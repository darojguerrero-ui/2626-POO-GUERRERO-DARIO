"""
Módulo: restaurante.py
Descripción: Contiene la clase Restaurante que administra una lista de productos
             (Platillos y Bebidas) del restaurante.
"""


class Restaurante:
    """
    Clase que administra los productos disponibles en el restaurante.
    
    Atributos:
        nombre (str): Nombre del restaurante
        productos (list): Lista de productos (Platillos y Bebidas)
    """
    
    def __init__(self, nombre):
        """
        Constructor de la clase Restaurante.
        
        Args:
            nombre (str): Nombre del restaurante
        """
        self.nombre = nombre
        self.productos = []  # Lista para almacenar productos
    
    def agregar_producto(self, producto):
        """
        Agrega un producto a la lista del restaurante.
        
        Args:
            producto: Un objeto de tipo Producto (Platillo o Bebida)
        """
        self.productos.append(producto)
        print(f"✓ {producto.nombre} agregado al restaurante.")
    
    def eliminar_producto(self, nombre_producto):
        """
        Elimina un producto de la lista por su nombre.
        
        Args:
            nombre_producto (str): Nombre del producto a eliminar
        """
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                self.productos.remove(producto)
                print(f"✓ {nombre_producto} eliminado del restaurante.")
                return
        print(f"✗ Producto '{nombre_producto}' no encontrado.")
    
    def obtener_producto_por_nombre(self, nombre_producto):
        """
        Busca y retorna un producto por su nombre.
        
        Args:
            nombre_producto (str): Nombre del producto a buscar
            
        Returns:
            Producto: El producto encontrado o None si no existe
        """
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                return producto
        return None
    
    def mostrar_menu(self):
        """
        Muestra todos los productos registrados en el restaurante.
        Demuestra polimorfismo al llamar mostrar_informacion() en cada producto,
        que será ejecutado según el tipo específico del objeto (Platillo o Bebida).
        """
        print(f"\n{'=' * 60}")
        print(f"MENÚ DEL RESTAURANTE: {self.nombre}")
        print(f"{'=' * 60}\n")
        
        if not self.productos:
            print("No hay productos registrados.")
            return
        
        for i, producto in enumerate(self.productos, 1):
            print(f"{i}. {producto.mostrar_informacion()}")
            print("-" * 60)
    
    def obtener_cantidad_productos(self):
        """
        Retorna la cantidad total de productos registrados.
        
        Returns:
            int: Cantidad de productos
        """
        return len(self.productos)
    
    def obtener_productos_disponibles(self):
        """
        Retorna una lista de productos disponibles.
        
        Returns:
            list: Lista de productos disponibles
        """
        return [p for p in self.productos if p.disponibilidad]
