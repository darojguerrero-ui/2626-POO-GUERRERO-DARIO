# Modulo de la clase Cliente
# Representa una persona que realiza o consume un pedido en el restaurante

class Cliente:
    """
    Clase que representa un cliente del restaurante.

    Atributos:
        id_cliente (int): Identificador unico del cliente
        nombre (str): Nombre completo del cliente
        email (str): Correo electronico del cliente
        telefono (str): Numero de telefono del cliente
        registro_activo (bool): Indica si el cliente esta registrado activamente
        pedidos (list): Lista de pedidos del cliente
    """

    def __init__(self, id_cliente, nombre, email, telefono):
        """
        Constructor de la clase Cliente.

        Args:
            id_cliente (int): Identificador unico del cliente
            nombre (str): Nombre completo del cliente
            email (str): Correo electronico del cliente
            telefono (str): Numero de telefono del cliente
        """
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.registro_activo = True
        self.pedidos = []

    def actualizar_contacto(self, email=None, telefono=None):
        """
        Actualiza la informacion de contacto del cliente.

        Args:
            email (str): Nuevo email del cliente (opcional)
            telefono (str): Nuevo telefono del cliente (opcional)
        """
        if email:
            self.email = email
        if telefono:
            self.telefono = telefono

    def registrar_pedido(self, id_pedido):
        """
        Registra un nuevo pedido para el cliente.

        Args:
            id_pedido (int): Identificador del pedido
        """
        self.pedidos.append(id_pedido)

    def obtener_informacion(self):
        """Retorna la informacion del cliente en formato de diccionario."""
        return {
            'id': self.id_cliente,
            'nombre': self.nombre,
            'email': self.email,
            'telefono': self.telefono,
            'activo': 'Si' if self.registro_activo else 'No',
            'total_pedidos': len(self.pedidos)
        }

    def __str__(self):
        """Representacion en texto del cliente."""
        estado = "Activo" if self.registro_activo else "Inactivo"
        return f"{self.nombre} ({self.email} - {self.telefono}) - {estado}"

