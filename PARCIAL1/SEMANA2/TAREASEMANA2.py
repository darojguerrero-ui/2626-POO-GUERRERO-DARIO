class CuentaBancaria:
    """Representa una cuenta bancaria simple."""

    def __init__(self, titular: str, saldo_inicial: float = 0.0):
        self.titular = titular
        self.saldo = float(saldo_inicial)

    def depositar(self, cantidad: float) -> None:
        """Deposita dinero en la cuenta."""
        if cantidad <= 0:
            raise ValueError("La cantidad a depositar debe ser positiva.")
        self.saldo += cantidad

    def retirar(self, cantidad: float) -> None:
        """Retira dinero de la cuenta si hay saldo suficiente."""
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser positiva.")
        if cantidad > self.saldo:
            raise ValueError("Saldo insuficiente para realizar el retiro.")
        self.saldo -= cantidad

    def mostrar_saldo(self) -> str:
        """Devuelve una cadena con el saldo actual."""
        return f"Titular: {self.titular}, Saldo actual: ${self.saldo:.2f}"

    def __str__(self) -> str:
        return self.mostrar_saldo()


if __name__ == "__main__":
    cuenta = CuentaBancaria(titular="Dario Guerrero", saldo_inicial=150.0)
    print("Cuenta creada:")
    print(cuenta)

    print("\nDepositando $50.00...")
    cuenta.depositar(50.0)
    print(cuenta)

    print("\nRetirando $30.50...")
    cuenta.retirar(30.5)
    print(cuenta)
