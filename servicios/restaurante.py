from __future__ import annotations

from typing import List, Optional

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class Restaurante:
    """Servicio encargado de administrar productos, usuarios y ventas del restaurante."""

    def __init__(
        self,
        productos: Optional[List[Producto]] = None,
        usuarios: Optional[List[Usuario]] = None,
        ventas: Optional[List[Venta]] = None,
    ) -> None:
        self._productos = list(productos or [])
        self._usuarios = list(usuarios or [])
        self._ventas = list(ventas or [])

    def listar(self) -> List[Producto]:
        return self.listar_productos()

    def listar_productos(self) -> List[Producto]:
        return list(self._productos)

    def listar_usuarios(self) -> List[Usuario]:
        return list(self._usuarios)

    def listar_ventas(self) -> List[Venta]:
        return list(self._ventas)

    def buscar_por_id(self, codigo: str) -> Optional[Producto]:
        return self.buscar_producto(str(codigo))

    def buscar_producto(self, codigo: str) -> Optional[Producto]:
        for producto in self._productos:
            if producto.codigo == str(codigo):
                return producto
        return None

    def buscar_usuario(self, identificacion: str) -> Optional[Usuario]:
        for usuario in self._usuarios:
            if usuario.identificacion == str(identificacion):
                return usuario
        return None

    def registrar(self, producto: Producto) -> None:
        self.registrar_producto(producto)

    def registrar_producto(self, producto: Producto) -> bool:
        if self.buscar_producto(producto.codigo) is not None:
            raise ValueError("El código del producto ya existe")
        self._productos.append(producto)
        return True

    def actualizar(self, codigo: str, nombre: Optional[str] = None, precio: Optional[float] = None, stock: Optional[int] = None) -> Producto:
        producto = self.buscar_producto(codigo)
        if producto is None:
            raise ValueError("Producto no encontrado")
        if nombre is not None:
            producto.nombre = nombre
        if precio is not None:
            valor = float(precio)
            if valor < 0:
                raise ValueError("El precio no puede ser negativo")
            producto.precio = valor
        if stock is not None:
            valor_stock = int(stock)
            if valor_stock < 0:
                raise ValueError("El stock no puede ser negativo")
            producto.stock = valor_stock
        return producto

    def actualizar_producto(self, codigo: str, nombre: Optional[str] = None, precio: Optional[float] = None, stock: Optional[int] = None) -> bool:
        try:
            self.actualizar(codigo, nombre=nombre, precio=precio, stock=stock)
            return True
        except ValueError:
            return False

    def eliminar(self, codigo: str) -> None:
        producto = self.buscar_producto(codigo)
        if producto is None:
            raise ValueError("Producto no encontrado")
        self._productos.remove(producto)

    def eliminar_producto(self, codigo: str) -> bool:
        try:
            self.eliminar(codigo)
            return True
        except ValueError:
            return False

    def registrar_usuario(self, usuario: Usuario) -> bool:
        if self.buscar_usuario(usuario.identificacion) is not None:
            raise ValueError("La identificación del usuario ya existe")
        self._usuarios.append(usuario)
        return True

    def eliminar_usuario(self, identificacion: str) -> bool:
        usuario = self.buscar_usuario(identificacion)
        if usuario is None:
            return False
        self._usuarios.remove(usuario)
        return True

    def vender_producto(self, codigo_producto: str, identificacion_usuario: str, cantidad: int) -> bool:
        usuario = self.buscar_usuario(identificacion_usuario)
        producto = self.buscar_producto(codigo_producto)

        if usuario is None or producto is None:
            return False
        if not isinstance(cantidad, int) or cantidad <= 0:
            return False
        if producto.stock < cantidad:
            return False

        venta = Venta(usuario.identificacion, producto.codigo, cantidad)
        self._ventas.append(venta)
        producto.vender(cantidad)
        return True

    def ventas_por_usuario(self, identificacion_usuario: str) -> List[Venta]:
        ventas_usuario: List[Venta] = []
        for venta in self._ventas:
            if venta.usuario_id == str(identificacion_usuario):
                ventas_usuario.append(venta)
        return ventas_usuario