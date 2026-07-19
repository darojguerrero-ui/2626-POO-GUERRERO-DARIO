from dataclasses import dataclass

@dataclass
class Producto:
    nombre: str
    precio: float
    disponible: bool = True

    def __post_init__(self):
        """Validación después de la inicialización de la dataclass."""
        if self.precio < 0:
            raise ValueError(f"El precio del producto '{self.nombre}' no puede ser negativo.")