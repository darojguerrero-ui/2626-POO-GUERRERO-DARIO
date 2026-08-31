from typing import Optional

class Usuario:
    def __init__(self, username: str, nombre: Optional[str] = None) -> None:
        if not isinstance(username, str) or not username.strip():
            raise ValueError("username inválido")
        self.username = username.strip()
        self.nombre = nombre or ""