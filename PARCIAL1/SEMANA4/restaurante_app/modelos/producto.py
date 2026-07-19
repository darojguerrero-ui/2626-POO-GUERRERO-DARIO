# Modulo de la clase Producto
# Representa un plato, bebida o producto disponible en el restaurante

class Producto:
    """
    Clase que representa un producto disponible en el restaurante.

    Atributos:
        id_producto (int): Identificador unico del producto
        nombre (str): Nombre del producto
        categoria (str): Categoria del producto (Entrada, Plato Principal, Postre, Bebida)
        precio (float): Precio del producto
        disponible (bool): Indica si el producto esta disponible
    """

    def __init__(self, id_producto, nombre, categoria, precio, disponible=True):
        """
        Constructor de la clase Producto.

        Args:
            id_producto (int): Identificador unico del producto
            nombre (str): Nombre del producto
            categoria (str): Categoria del producto
            precio (float): Precio del producto
            disponible (bool): Estado de disponibilidad (por defecto True)
        """
        self.id_producto = id_producto
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.disponible = disponible

    def cambiar_disponibilidad(self):
        """Cambia el estado de disponibilidad del producto."""
        self.disponible = not self.disponible

    def actualizar_precio(self, nuevo_precio):
        """
        Actualiza el precio del producto.

        Args:
            nuevo_precio (float): El nuevo precio del producto

        Returns:
            bool: True si se actualizo correctamente, False si el precio es invalido
        """
        if nuevo_precio > 0:
            self.precio = nuevo_precio
            return True
        return False

    def obtener_informacion(self):
        """Retorna la informacion del producto en formato de diccionario."""
        return {
            'id': self.id_producto,
            'nombre': self.nombre,
            'categoria': self.categoria,
            'precio': self.precio,
            'disponible': 'Si' if self.disponible else 'No'
        }

    def __str__(self):
        """Representacion en texto del producto."""
        estado = "Disponible" if self.disponible else "No disponible"
        return f"{self.nombre} ({self.categoria}) - ${self.precio:.2f} - {estado}"

