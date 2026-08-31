import json
import os
from typing import Any, List, Type, TypeVar

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta

T = TypeVar("T")


class ArchivoServicio:
    def __init__(self, directorio: str | None = None) -> None:
        if directorio is None:
            directorio = os.path.join(os.path.dirname(os.path.dirname(__file__)), "datos")

        if directorio.endswith(".json"):
            self.directorio = os.path.dirname(directorio) or "."
        else:
            self.directorio = directorio

        self.productos_path = os.path.join(self.directorio, "productos.json")
        self.usuarios_path = os.path.join(self.directorio, "usuarios.json")
        self.ventas_path = os.path.join(self.directorio, "ventas.json")

    def cargar(self) -> List[Producto]:
        return self.cargar_productos()

    def guardar(self, productos: List[Producto]) -> None:
        self.guardar_productos(productos)

    def _crear_directorio(self) -> None:
        os.makedirs(self.directorio, exist_ok=True)

    def _cargar_json(self, path: str, tipo: Type[T], nombre: str) -> List[T]:
        if not os.path.exists(path):
            return []
        try:
            with open(path, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError as exc:
            raise ValueError(f"JSON inválido en {nombre}: {exc}") from exc
        except PermissionError as exc:
            raise PermissionError(f"Sin permisos para leer {nombre}: {exc}") from exc

        if datos is None:
            return []
        if not isinstance(datos, list):
            raise ValueError(f"El contenido de {nombre} debe ser una lista")

        objetos: List[T] = []
        for elemento in datos:
            try:
                objetos.append(tipo.from_dict(elemento))
            except (KeyError, TypeError, ValueError) as exc:
                raise ValueError(f"Registro inválido en {nombre}: {exc}") from exc
        return objetos

    def _guardar_json(self, path: str, datos: List[Any], nombre: str) -> None:
        try:
            self._crear_directorio()
            with open(path, "w", encoding="utf-8") as archivo:
                json.dump(datos, archivo, ensure_ascii=False, indent=2)
        except PermissionError as exc:
            raise PermissionError(f"Sin permisos para escribir {nombre}: {exc}") from exc

    def cargar_productos(self) -> List[Producto]:
        return self._cargar_json(self.productos_path, Producto, "productos.json")

    def guardar_productos(self, productos: List[Producto]) -> None:
        self._guardar_json(self.productos_path, [p.to_dict() for p in productos], "productos.json")

    def cargar_usuarios(self) -> List[Usuario]:
        return self._cargar_json(self.usuarios_path, Usuario, "usuarios.json")

    def guardar_usuarios(self, usuarios: List[Usuario]) -> None:
        self._guardar_json(self.usuarios_path, [u.to_dict() for u in usuarios], "usuarios.json")

    def cargar_ventas(self) -> List[Venta]:
        return self._cargar_json(self.ventas_path, Venta, "ventas.json")

    def guardar_ventas(self, ventas: List[Venta]) -> None:
        self._guardar_json(self.ventas_path, [v.to_dict() for v in ventas], "ventas.json")