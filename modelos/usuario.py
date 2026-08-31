from __future__ import annotations

from typing import Any, Dict, Optional


class Usuario:
    """Representa a la persona registrada que puede realizar una compra."""

    def __init__(
        self,
        identificacion: Optional[str] = None,
        nombre: str = "",
        correo: Optional[str] = None,
        celular: Optional[str] = None,
        **kwargs: Any,
    ) -> None:
        if identificacion is None and "username" in kwargs:
            identificacion = kwargs["username"]
        if not isinstance(identificacion, str) or not identificacion.strip():
            raise ValueError("identificacion inválida")
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("nombre inválido")

        self.identificacion = identificacion.strip()
        self.nombre = nombre.strip()
        self.correo = (correo or "").strip()
        self.celular = (celular or "").strip()
        self.username = self.identificacion

    @property
    def id(self) -> str:
        return self.identificacion

    @id.setter
    def id(self, value: str) -> None:
        self.identificacion = str(value).strip()
        self.username = self.identificacion

    def to_dict(self) -> Dict[str, Any]:
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "correo": self.correo,
            "celular": self.celular,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Usuario":
        try:
            identificacion = data.get("identificacion", data.get("username"))
            nombre = data["nombre"]
            return cls(
                identificacion=str(identificacion),
                nombre=str(nombre),
                correo=data.get("correo"),
                celular=data.get("celular"),
            )
        except KeyError as exc:
            raise KeyError(f"Falta clave en registro: {exc}") from exc
        except (TypeError, ValueError) as exc:
            raise ValueError(f"Datos inválidos para Usuario: {exc}") from exc

    def __str__(self) -> str:
        return f"{self.identificacion} - {self.nombre}"
