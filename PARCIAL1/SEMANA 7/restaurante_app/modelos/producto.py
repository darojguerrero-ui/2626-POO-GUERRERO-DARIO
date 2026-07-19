"""
Módulo: producto.py
Descripción: Contiene la clase Producto con constructor tradicional, 
             decoradores @property y @setter para acceso y modificación controlada.
"""


class Producto:
    """
    Clase que representa un producto del restaurante.
    
    Implementa:
    - Constructor tradicional __init__()
    - Decoradores @property para acceso controlado a atributos
    - Decoradores @setter para modificación con validaciones
    
    Atributos privados:
        __nombre (str): Nombre del producto
        __categoria (str): Categoría del producto
        __precio (float): Precio del producto
        __disponible (bool): Disponibilidad del producto
    """
    
    def __init__(self, nombre, categoria, precio, disponible=True):
        """
        Constructor tradicional de la clase Producto.
        
        Args:
            nombre (str): Nombre del producto
            categoria (str): Categoría del producto
            precio (float): Precio del producto
            disponible (bool): Estado de disponibilidad (por defecto True)
        """
        self.__nombre = nombre
        self.__categoria = categoria
        self.__precio = precio
        self.__disponible = disponible
    
    # PROPIEDADES Y SETTERS PARA NOMBRE
    @property
    def nombre(self):
        """
        Propiedad para acceder al nombre del producto.
        
        Returns:
            str: El nombre del producto
        """
        return self.__nombre
    
    @nombre.setter
    def nombre(self, valor):
        """
        Setter para modificar el nombre del producto con validación.
        
        Args:
            valor (str): Nuevo nombre del producto
            
        Raises:
            ValueError: Si el nombre está vacío
        """
        if not valor or not valor.strip():
            raise ValueError("El nombre del producto no puede estar vacío.")
        self.__nombre = valor.strip()
    
    # PROPIEDADES Y SETTERS PARA CATEGORÍA
    @property
    def categoria(self):
        """
        Propiedad para acceder a la categoría del producto.
        
        Returns:
            str: La categoría del producto
        """
        return self.__categoria
    
    @categoria.setter
    def categoria(self, valor):
        """
        Setter para modificar la categoría del producto con validación.
        
        Args:
            valor (str): Nueva categoría del producto
            
        Raises:
            ValueError: Si la categoría está vacía
        """
        if not valor or not valor.strip():
            raise ValueError("La categoría del producto no puede estar vacía.")
        self.__categoria = valor.strip()
    
    # PROPIEDADES Y SETTERS PARA PRECIO
    @property
    def precio(self):
        """
        Propiedad para acceder al precio del producto.
        
        Returns:
            float: El precio del producto
        """
        return self.__precio
    
    @precio.setter
    def precio(self, valor):
        """
        Setter para modificar el precio del producto con validación.
        
        Args:
            valor (float): Nuevo precio del producto
            
        Raises:
            ValueError: Si el precio es menor o igual a cero
        """
        try:
            valor_float = float(valor)
            if valor_float <= 0:
                raise ValueError("El precio debe ser mayor que cero.")
            self.__precio = valor_float
        except (TypeError, ValueError):
            raise ValueError("El precio debe ser un número válido mayor que cero.")
    
    # PROPIEDADES Y SETTERS PARA DISPONIBILIDAD
    @property
    def disponible(self):
        """
        Propiedad para acceder al estado de disponibilidad.
        
        Returns:
            bool: True si el producto está disponible, False en caso contrario
        """
        return self.__disponible
    
    @disponible.setter
    def disponible(self, valor):
        """
        Setter para modificar el estado de disponibilidad.
        
        Args:
            valor (bool): Nuevo estado de disponibilidad
        """
        self.__disponible = bool(valor)
    
    def mostrar_informacion(self):
        """
        Método para mostrar la información del producto de forma legible.
        
        Returns:
            str: Información formateada del producto
        """
        estado = "Disponible" if self.__disponible else "No disponible"
        return (f"Producto: {self.__nombre}\n"
                f"  Categoría: {self.__categoria}\n"
                f"  Precio: ${self.__precio:.2f}\n"
                f"  Estado: {estado}")
