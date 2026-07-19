from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    def __init__(self, nombre_restaurante: str):
        self.nombre_restaurante = nombre_restaurante
        self.productos: list[Producto] = []
        self.clientes: list[Cliente] = []

    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)
        print(f"Producto '{producto.nombre}' agregado con éxito.")

    def agregar_cliente(self, cliente: Cliente):
        self.clientes.append(cliente)
        print(f"Cliente '{cliente.nombre}' registrado.")

    def mostrar_menu(self):
        print(f"\n--- MENÚ DE {self.nombre_restaurante.upper()} ---")
        if not self.productos:
            print("No hay productos disponibles.")
        for p in self.productos:
            estado = "Disponible" if p.disponible else "Agotado"
            print(f"- {p.nombre:15} | Precio: ${p.precio:>6.2f} | [{estado}]")