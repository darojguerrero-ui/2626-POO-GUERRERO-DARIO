import json
import os
from typing import List
from modelos.producto import Producto

class ArchivoServicio:
    def __init__(self, path: str) -> None:
        self.path = path

    def cargar(self) -> List[Producto]:
        if not os.path.exists(self.path):
            return []
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                data = json.load(f)
            if not isinstance(data, list):
                raise ValueError("El contenido JSON debe ser una lista de productos")
            productos: List[Producto] = []
            for rec in data:
                try:
                    prod = Producto.from_dict(rec)
                    productos.append(prod)
                except (KeyError, ValueError) as e:
                    print(f"Registro omitido por error: {e}")
            return productos
        except FileNotFoundError:
            return []
        except json.JSONDecodeError as e:
            print(f"Error al decodificar JSON: {e}")
            return []
        except PermissionError as e:
            print(f"Permiso denegado al leer archivo: {e}")
            return []

    def guardar(self, productos: List[Producto]) -> None:
        try:
            os.makedirs(os.path.dirname(self.path), exist_ok=True)
            with open(self.path, "w", encoding="utf-8") as f:
                json.dump([p.to_dict() for p in productos], f, ensure_ascii=False, indent=2)
        except PermissionError as e:
            print(f"Permiso denegado al escribir archivo: {e}")
            raise