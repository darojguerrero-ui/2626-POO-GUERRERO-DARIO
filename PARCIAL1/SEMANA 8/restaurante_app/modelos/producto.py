from abc import ABC, abstractmethod

class Producto(ABC):
    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float):
        if not codigo or not nombre or not categoria or precio <= 0:
            raise ValueError("Todos los campos de Producto deben ser válidos.")
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    @abstractmethod
    def mostrar_informacion(self) -> str:
        """
        Método abstracto para mostrar la información detallada del producto.
        Debe ser implementado por las subclases.
        """
        pass

    def __str__(self) -> str:
        return f"Código: {self.codigo} | Nombre: {self.nombre} | Categoría: {self.categoria} | Precio: ${self.precio:.2f}"
