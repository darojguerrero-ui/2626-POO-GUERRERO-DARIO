from modelos.producto import Producto

class Bebida(Producto):
    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float, tamano: str, tipo_envase: str):
        super().__init__(codigo, nombre, categoria, precio)
        if not tamano or not tipo_envase:
            raise ValueError("El tamaño y el tipo de envase de la Bebida deben ser válidos.")
        self.tamano = tamano
        self.tipo_envase = tipo_envase

    def mostrar_informacion(self) -> str:
        """
        Sobrescribe el método para mostrar información específica de la bebida.
        """
        return (f"{super().__str__()} | Tamaño: {self.tamano} | Tipo de Envase: {self.tipo_envase}")
