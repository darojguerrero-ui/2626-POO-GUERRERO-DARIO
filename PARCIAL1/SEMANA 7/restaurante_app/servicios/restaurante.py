"""
Módulo: restaurante.py
Descripción: Contiene la clase Restaurante encargada de administrar productos y clientes.
             Implementa métodos para registrar, listar y buscar registros.
"""


class Restaurante:
    """
    Clase de servicio que administra los productos y clientes del restaurante.
    
    Atributos:
        nombre (str): Nombre del restaurante
        productos (list): Lista de productos registrados
        clientes (list): Lista de clientes registrados
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
    
    # ==================== MÉTODOS DE PRODUCTOS ====================
    
    def registrar_producto(self, producto):
        """
        Registra un producto en la lista del restaurante.
        
        Args:
            producto: Objeto de tipo Producto
            
        Returns:
            bool: True si el registro fue exitoso, False en caso contrario
        """
        if producto not in self.productos:
            self.productos.append(producto)
            return True
        return False
    
    def listar_productos(self):
        """
        Retorna la lista de todos los productos registrados.
        
        Returns:
            list: Lista de productos
        """
        return self.productos
    
    def buscar_producto(self, nombre):
        """
        Busca un producto por nombre (búsqueda parcial).
        
        Args:
            nombre (str): Nombre o parte del nombre del producto a buscar
            
        Returns:
            list: Lista de productos que coinciden con la búsqueda
        """
        resultado = [
            p for p in self.productos
            if nombre.lower() in p.nombre.lower()
        ]
        return resultado
    
    def obtener_producto_por_nombre_exacto(self, nombre):
        """
        Busca un producto por nombre exacto.
        
        Args:
            nombre (str): Nombre exacto del producto
            
        Returns:
            Producto: El producto encontrado o None
        """
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                return producto
        return None
    
    def eliminar_producto(self, nombre):
        """
        Elimina un producto de la lista por nombre.
        
        Args:
            nombre (str): Nombre del producto a eliminar
            
        Returns:
            bool: True si se eliminó, False si no se encontró
        """
        producto = self.obtener_producto_por_nombre_exacto(nombre)
        if producto:
            self.productos.remove(producto)
            return True
        return False
    
    def obtener_cantidad_productos(self):
        """
        Retorna la cantidad total de productos registrados.
        
        Returns:
            int: Cantidad de productos
        """
        return len(self.productos)
    
    # ==================== MÉTODOS DE CLIENTES ====================
    
    def registrar_cliente(self, cliente):
        """
        Registra un cliente en la lista del restaurante.
        
        Args:
            cliente: Objeto de tipo Cliente
            
        Returns:
            bool: True si el registro fue exitoso, False en caso contrario
        """
        # Verificar que no exista un cliente con el mismo ID
        if not any(c.id_cliente == cliente.id_cliente for c in self.clientes):
            self.clientes.append(cliente)
            return True
        return False
    
    def listar_clientes(self):
        """
        Retorna la lista de todos los clientes registrados.
        
        Returns:
            list: Lista de clientes
        """
        return self.clientes
    
    def buscar_cliente(self, nombre):
        """
        Busca un cliente por nombre (búsqueda parcial).
        
        Args:
            nombre (str): Nombre o parte del nombre del cliente a buscar
            
        Returns:
            list: Lista de clientes que coinciden con la búsqueda
        """
        resultado = [
            c for c in self.clientes
            if nombre.lower() in c.nombre.lower()
        ]
        return resultado
    
    def obtener_cliente_por_id(self, id_cliente):
        """
        Busca un cliente por ID.
        
        Args:
            id_cliente (int): ID del cliente
            
        Returns:
            Cliente: El cliente encontrado o None
        """
        for cliente in self.clientes:
            if cliente.id_cliente == id_cliente:
                return cliente
        return None
    
    def obtener_cliente_por_nombre_exacto(self, nombre):
        """
        Busca un cliente por nombre exacto.
        
        Args:
            nombre (str): Nombre exacto del cliente
            
        Returns:
            Cliente: El cliente encontrado o None
        """
        for cliente in self.clientes:
            if cliente.nombre.lower() == nombre.lower():
                return cliente
        return None
    
    def eliminar_cliente(self, id_cliente):
        """
        Elimina un cliente de la lista por ID.
        
        Args:
            id_cliente (int): ID del cliente a eliminar
            
        Returns:
            bool: True si se eliminó, False si no se encontró
        """
        cliente = self.obtener_cliente_por_id(id_cliente)
        if cliente:
            self.clientes.remove(cliente)
            return True
        return False
    
    def obtener_cantidad_clientes(self):
        """
        Retorna la cantidad total de clientes registrados.
        
        Returns:
            int: Cantidad de clientes
        """
        return len(self.clientes)
