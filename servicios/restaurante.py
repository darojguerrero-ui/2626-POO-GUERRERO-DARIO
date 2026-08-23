from typing import List, Optional
from modelos.producto import Producto

class Restaurante:
    def __init__(self, productos: Optional[List[Producto]] = None) -> None:
        self.productos: List[Producto] = productos or []

    def listar(self) -> List[Producto]:
        return self.productos

    def buscar_por_id(self, id: int) -> Optional[Producto]:
        for p in self.productos:
            if p.id == id:
                return p
        return None

    def registrar(self, producto: Producto) -> None:
        if self.buscar_por_id(producto.id) is not None:
            raise ValueError("ID de producto ya existe")
        self.productos.append(producto)

    def actualizar(self, id: int, nombre: Optional[str] = None, precio: Optional[float] = None, stock: Optional[int] = None) -> Producto:
        p = self.buscar_por_id(id)
        if p is None:
            raise ValueError("Producto no encontrado")
        new_nombre = nombre if nombre is not None else p.nombre
        new_precio = precio if precio is not None else p.precio
        new_stock = stock if stock is not None else p.stock
        actualizado = Producto(id, new_nombre, new_precio, new_stock)
        idx = self.productos.index(p)
        self.productos[idx] = actualizado
        return actualizado

    def eliminar(self, id: int) -> None:
        p = self.buscar_por_id(id)
        if p is None:
            raise ValueError("Producto no encontrado")
        self.productos.remove(p)