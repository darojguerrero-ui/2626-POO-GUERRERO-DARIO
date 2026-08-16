from typing import List, Optional, Tuple, Dict, Set
from modelos.producto import Producto
from modelos.usuario import Usuario

class Restaurante:
    """Servicio que administra colecciones de productos y usuarios.

    Uso de estructuras de datos:
    - list: almacenar colecciones dinámicas (_productos, _usuarios)
    - tuple: MENU_OPTIONS, información estable del sistema
    - dict: MENU_MAP, relación clave->valor entre número y opción
    - set: categorias_unicas(), obtener categorías sin duplicados
    """
    MENU_OPTIONS: Tuple[str, ...] = (
        "Registrar producto",
        "Buscar producto",
        "Actualizar producto",
        "Eliminar producto",
        "Listar productos",
        "Registrar usuario",
        "Listar usuarios",
        "Mostrar categorías",
        "Salir",
    )

    # dict que mapea número de opción a texto (ejemplo de dict en el sistema)
    MENU_MAP: Dict[int, str] = {i + 1: opt for i, opt in enumerate(MENU_OPTIONS)}

    def __init__(self) -> None:
        # listas para colecciones dinámicas
        self._productos: List[Producto] = []
        self._usuarios: List[Usuario] = []

    # Operaciones sobre productos
    def registrar_producto(self, producto: Producto) -> bool:
        """Registra un producto si su código no existe. Retorna True si se añadió."""
        if any(p.codigo == producto.codigo for p in self._productos):
            return False
        self._productos.append(producto)
        return True

    def buscar_producto(self, codigo: str) -> Optional[Producto]:
        """Busca un producto por código y lo retorna, o None si no existe."""
        for p in self._productos:
            if p.codigo == codigo:
                return p
        return None

    def actualizar_producto(
        self,
        codigo: str,
        nombre: Optional[str] = None,
        categoria: Optional[str] = None,
        precio: Optional[float] = None,
    ) -> bool:
        """Actualiza los campos proporcionados de un producto existente."""
        prod = self.buscar_producto(codigo)
        if not prod:
            return False
        if nombre is not None:
            prod.nombre = nombre
        if categoria is not None:
            prod.categoria = categoria
        if precio is not None:
            prod.precio = precio
        return True

    def eliminar_producto(self, codigo: str) -> bool:
        """Elimina producto por código. Retorna True si se eliminó."""
        prod = self.buscar_producto(codigo)
        if not prod:
            return False
        self._productos.remove(prod)
        return True

    def listar_productos(self) -> List[Producto]:
        """Retorna una copia de la lista de productos (no exponer la referencia interna)."""
        return list(self._productos)

    # Operaciones sobre usuarios
    def registrar_usuario(self, usuario: Usuario) -> bool:
        """Registra un usuario si su identificación no está en uso."""
        if any(u.identificacion == usuario.identificacion for u in self._usuarios):
            return False
        self._usuarios.append(usuario)
        return True

    def listar_usuarios(self) -> List[Usuario]:
        return list(self._usuarios)

    # Ejemplo de uso de set para obtener categorías únicas
    def categorias_unicas(self) -> Set[str]:
        return {p.categoria for p in self._productos}
