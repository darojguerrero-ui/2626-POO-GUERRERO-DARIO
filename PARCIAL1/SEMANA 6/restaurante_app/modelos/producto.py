"""
Módulo: producto.py
Descripción: Contiene la clase padre Producto que define los atributos y métodos comunes
             para todos los productos disponibles en el restaurante.
"""


class Producto:
    """
    Clase padre que representa un producto general del restaurante.
    
    Atributos:
        nombre (str): Nombre del producto
        __precio (float): Precio del producto (encapsulado/privado)
        disponibilidad (bool): Indica si el producto está disponible
    """
    
    def __init__(self, nombre, precio, disponibilidad=True):
        """
        Constructor de la clase Producto.
        
        Args:
            nombre (str): Nombre del producto
            precio (float): Precio del producto
            disponibilidad (bool): Estado de disponibilidad (por defecto True)
        """
        self.nombre = nombre
        self.__precio = precio  # Atributo encapsulado (privado)
        self.disponibilidad = disponibilidad
    
    def obtener_precio(self):
        """
        Método para acceder al precio encapsulado.
        
        Returns:
            float: El precio del producto
        """
        return self.__precio
    
    def cambiar_precio(self, nuevo_precio):
        """
        Método para modificar el precio con validación.
        Valida que el precio no sea negativo ni igual a cero.
        
        Args:
            nuevo_precio (float): El nuevo precio del producto
            
        Raises:
            ValueError: Si el precio es menor o igual a cero
        """
        if nuevo_precio <= 0:
            raise ValueError("El precio debe ser mayor a cero.")
        self.__precio = nuevo_precio
    
    def cambiar_disponibilidad(self, disponibilidad):
        """
        Método para cambiar la disponibilidad del producto.
        
        Args:
            disponibilidad (bool): Estado de disponibilidad
        """
        self.disponibilidad = disponibilidad
    
    def mostrar_informacion(self):
        """
        Método para mostrar la información del producto.
        Este método será sobrescrito en las clases hijas.
        
        Returns:
            str: Información formateada del producto
        """
        estado = "Disponible" if self.disponibilidad else "No disponible"
        return f"Nombre: {self.nombre} | Precio: ${self.__precio:.2f} | Estado: {estado}"
