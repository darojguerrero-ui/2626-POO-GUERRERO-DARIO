from dataclasses import dataclass

@dataclass
class Usuario:
    """Representa una persona registrada en el sistema.

    Atributos:
        identificacion: id único del usuario (str)
        nombre: nombre completo (str)
        correo: correo electrónico (str)
        celular: número de teléfono celular (str)
    """
    identificacion: str
    nombre: str
    correo: str
    celular: str

    def __str__(self) -> str:
        return f"{self.identificacion} - {self.nombre} <{self.correo}> - Cel: {self.celular}"
