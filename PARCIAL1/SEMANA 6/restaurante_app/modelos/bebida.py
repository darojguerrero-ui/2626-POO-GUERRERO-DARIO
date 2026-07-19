"""
Módulo: bebida.py
Descripción: Contiene la clase Bebida que hereda de Producto y añade atributos
             específicos para representar bebidas disponibles en el restaurante.
"""

from .producto import Producto


class Bebida(Producto):
    """
    Clase que hereda de Producto y representa una bebida del restaurante.
    
    Atributos heredados:
        nombre, __precio, disponibilidad
    
    Atributos propios:
        volumen_ml (int): Volumen de la bebida en mililitros
        tipo_bebida (str): Tipo de bebida (fría, caliente, alcohólica, etc.)
    """
    
    def __init__(self, nombre, precio, volumen_ml, tipo_bebida, disponibilidad=True):
        """
        Constructor de la clase Bebida.
        
        Args:
            nombre (str): Nombre de la bebida
            precio (float): Precio de la bebida
            volumen_ml (int): Volumen en mililitros
            tipo_bebida (str): Tipo de bebida
            disponibilidad (bool): Estado de disponibilidad (por defecto True)
        """
        super().__init__(nombre, precio, disponibilidad)  # Llamar al constructor de la clase padre
        self.volumen_ml = volumen_ml
        self.tipo_bebida = tipo_bebida
    
    def mostrar_informacion(self):
        """
        Sobrescribe el método mostrar_informacion() para incluir atributos específicos de la bebida.
        Demuestra polimorfismo al implementar el método de forma diferente.
        
        Returns:
            str: Información formateada de la bebida incluyendo volumen y tipo
        """
        estado = "Disponible" if self.disponibilidad else "No disponible"
        return (f"🥤 BEBIDA: {self.nombre}\n"
                f"   Precio: ${self.obtener_precio():.2f}\n"
                f"   Volumen: {self.volumen_ml} ml\n"
                f"   Tipo: {self.tipo_bebida}\n"
                f"   Estado: {estado}")
