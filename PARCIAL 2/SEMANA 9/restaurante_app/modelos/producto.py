from dataclasses import dataclass

@dataclass
class Producto:
    """Representa un producto del restaurante.

    Atributos:
        codigo: identificador único del producto (str)
        nombre: nombre del producto (str)
        categoria: categoría a la que pertenece (str)
        precio: precio en moneda local (float)
    """
    codigo: str
    nombre: str
    categoria: str
    precio: float

    def __str__(self) -> str:
        return f"{self.codigo} - {self.nombre} ({self.categoria}) - ${self.precio:.2f}"
