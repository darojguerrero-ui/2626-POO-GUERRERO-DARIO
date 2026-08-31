from __future__ import annotations

from typing import Any, Dict


class Venta:
    """Representa la relación entre un usuario y un producto vendido."""

    def __init__(self, usuario_id: str, producto_codigo: str, cantidad: int) -> None:
        if not isinstance(usuario_id, str) or not usuario_id.strip():
            raise ValueError("usuario_id inválido")
        if not isinstance(producto_codigo, str) or not producto_codigo.strip():
            raise ValueError("producto_codigo inválido")
        if not isinstance(cantidad, int) or cantidad <= 0:
            raise ValueError("cantidad inválida: debe ser un entero positivo")

        self.usuario_id = usuario_id.strip()
        self.producto_codigo = producto_codigo.strip()
        self.cantidad = cantidad

    def to_dict(self) -> Dict[str, Any]:
        return {
            "usuario_id": self.usuario_id,
            "producto_codigo": self.producto_codigo,
            "cantidad": self.cantidad,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Venta":
        try:
            return cls(
                usuario_id=str(data["usuario_id"]),
                producto_codigo=str(data["producto_codigo"]),
                cantidad=int(data["cantidad"]),
            )
        except KeyError as exc:
            raise KeyError(f"Falta clave en registro: {exc}") from exc
        except (TypeError, ValueError) as exc:
            raise ValueError(f"Datos inválidos para Venta: {exc}") from exc

    def __str__(self) -> str:
        return (
            f"Venta(usuario_id={self.usuario_id}, producto_codigo={self.producto_codigo}, "
            f"cantidad={self.cantidad})"
        )
