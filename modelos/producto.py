from typing import Dict, Any

class Producto:
    def __init__(self, id: int, nombre: str, precio: float, stock: int) -> None:
        if not isinstance(id, int) or id <= 0:
            raise ValueError("id inválido: debe ser entero positivo")
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("nombre inválido: debe ser texto no vacío")
        if not isinstance(precio, (int, float)) or precio < 0:
            raise ValueError("precio inválido: debe ser número no negativo")
        if not isinstance(stock, int) or stock < 0:
            raise ValueError("stock inválido: debe ser entero no negativo")
        self.id = id
        self.nombre = nombre.strip()
        self.precio = float(precio)
        self.stock = stock

    def to_dict(self) -> Dict[str, Any]:
        return {"id": self.id, "nombre": self.nombre, "precio": self.precio, "stock": self.stock}

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Producto":
        try:
            return cls(int(data["id"]), data["nombre"], float(data["precio"]), int(data["stock"]))
        except KeyError as e:
            raise KeyError(f"Falta clave en registro: {e}") from e
        except (TypeError, ValueError) as e:
            raise ValueError(f"Datos inválidos para Producto: {e}") from e

    def __str__(self) -> str:
        return f"{self.id}: {self.nombre} - ${self.precio:.2f} (stock: {self.stock})"