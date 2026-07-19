"""
Módulo: platillo.py
Descripción: Contiene la clase Platillo que hereda de Producto y añade atributos
             específicos para representar comidas o platos del restaurante.
"""

from .producto import Producto


class Platillo(Producto):
    """
    Clase que hereda de Producto y representa un platillo (comida) del restaurante.
    
    Atributos heredados:
        nombre, __precio, disponibilidad
    
    Atributos propios:
        calorias (int): Cantidad de calorías del platillo
        tiempo_preparacion (int): Tiempo de preparación en minutos
    """
    
    def __init__(self, nombre, precio, calorias, tiempo_preparacion, disponibilidad=True):
        """
        Constructor de la clase Platillo.
        
        Args:
            nombre (str): Nombre del platillo
            precio (float): Precio del platillo
            calorias (int): Cantidad de calorías
            tiempo_preparacion (int): Tiempo de preparación en minutos
            disponibilidad (bool): Estado de disponibilidad (por defecto True)
        """
        super().__init__(nombre, precio, disponibilidad)  # Llamar al constructor de la clase padre
        self.calorias = calorias
        self.tiempo_preparacion = tiempo_preparacion
    
    def mostrar_informacion(self):
        """
        Sobrescribe el método mostrar_informacion() para incluir atributos específicos del platillo.
        Demuestra polimorfismo al implementar el método de forma diferente.
        
        Returns:
            str: Información formateada del platillo incluyendo calorías y tiempo de preparación
        """
        estado = "Disponible" if self.disponibilidad else "No disponible"
        return (f"🍽️  PLATILLO: {self.nombre}\n"
                f"   Precio: ${self.obtener_precio():.2f}\n"
                f"   Calorías: {self.calorias} kcal\n"
                f"   Tiempo de preparación: {self.tiempo_preparacion} minutos\n"
                f"   Estado: {estado}")
