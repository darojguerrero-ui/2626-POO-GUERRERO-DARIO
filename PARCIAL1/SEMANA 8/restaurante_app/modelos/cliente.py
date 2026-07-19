class Cliente:
    def __init__(self, identificacion: str, nombre: str, correo: str):
        if not identificacion or not nombre or not correo:
            raise ValueError("Todos los campos de Cliente deben ser válidos.")
        self.identificacion = identificacion
        self.nombre = nombre
        self.correo = correo

    def mostrar_informacion(self) -> str:
        """
        Muestra la información detallada del cliente.
        """
        return f"ID: {self.identificacion} | Nombre: {self.nombre} | Correo: {self.correo}"

    def __str__(self) -> str:
        return self.mostrar_informacion()
