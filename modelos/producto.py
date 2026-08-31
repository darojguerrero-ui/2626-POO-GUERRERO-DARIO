from __future__ import annotations

from typing import Any, Dict


class Producto:
    """Representa un producto del restaurante y su stock disponible."""

    def __init__(self, codigo: str | None = None, nombre: str = "", precio: float = 0.0, stock: int = 0, **kwargs: Any) -> None:
        if codigo is None and "id" in kwargs:
            codigo = kwargs["id"]
        if not isinstance(codigo, str) or not codigo.strip():
            raise ValueError("codigo inválido: debe ser texto no vacío")
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("nombre inválido: debe ser texto no vacío")
        if not isinstance(precio, (int, float)) or precio < 0:
            raise ValueError("precio inválido: debe ser número no negativo")
        if not isinstance(stock, int) or stock < 0:
            raise ValueError("stock inválido: debe ser entero no negativo")

        self.codigo = codigo.strip()
        self.nombre = nombre.strip()
        self.precio = float(precio)
        self.stock = stock

    @property
    def id(self) -> str:
        return self.codigo

    @id.setter
    def id(self, value: str) -> None:
        self.codigo = str(value).strip()

    def vender(self, cantidad: int) -> None:
        if not isinstance(cantidad, int) or cantidad <= 0:
            raise ValueError("La cantidad a vender debe ser un entero positivo")
        if cantidad > self.stock:
            raise ValueError("No hay stock suficiente para vender esa cantidad")
        self.stock -= cantidad

    def to_dict(self) -> Dict[str, Any]:
        return {
            "codigo": self.codigo,
            "id": self.codigo,
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Producto":
        try:
            codigo = data.get("codigo", data.get("id"))
            nombre = data["nombre"]
            precio = data["precio"]
            stock = data["stock"]
            return cls(
                codigo=str(codigo),
                nombre=str(nombre),
                precio=float(precio),
                stock=int(stock),
            )
        except KeyError as exc:
            raise KeyError(f"Falta clave en registro: {exc}") from exc
        except (TypeError, ValueError) as exc:
            raise ValueError(f"Datos inválidos para Producto: {exc}") from exc

    def __str__(self) -> str:
        return f"{self.codigo} - {self.nombre} - ${self.precio:.2f} (stock: {self.stock})"