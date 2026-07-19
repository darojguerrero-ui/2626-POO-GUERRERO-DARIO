"""
Módulo: cliente.py
Descripción: Contiene la clase Cliente implementada mediante el decorador @dataclass
             para representar clientes del restaurante.
"""

from dataclasses import dataclass


@dataclass
class Cliente:
    """
    Clase que representa un cliente del restaurante.
    
    Implementada mediante el decorador @dataclass que automáticamente genera:
    - Constructor __init__()
    - Métodos __repr__() y __eq__()
    - Otros métodos útiles para comparación y representación
    
    Atributos:
        id_cliente (int): Identificador único del cliente
        nombre (str): Nombre del cliente
        correo (str): Correo electrónico del cliente
    """
    
    id_cliente: int
    nombre: str
    correo: str
    
    def mostrar_informacion(self):
        """
        Método para mostrar la información del cliente de forma legible.
        
        Returns:
            str: Información formateada del cliente
        """
        return (f"Cliente ID: {self.id_cliente}\n"
                f"  Nombre: {self.nombre}\n"
                f"  Correo: {self.correo}")
