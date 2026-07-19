# Programación Orientada a Objetos - Clase Mascota
# Autor: Dario Guerrero
# Descripción: Definición de la clase Mascota con atributos y métodos

class Mascota:
    """
    Clase Mascota que representa una mascota con sus atributos y comportamientos.

    Atributos:
        nombre (str): El nombre de la mascota
        especie (str): La especie de la mascota (perro, gato, ave, etc.)
        edad (int): La edad de la mascota en años

    Métodos:
        mostrar_informacion(): Muestra la información completa de la mascota
        hacer_sonido(): Hace que la mascota emita un sonido según su especie
    """

    def __init__(self, nombre, especie, edad):
        """
        Constructor de la clase Mascota.

        Args:
            nombre (str): Nombre de la mascota
            especie (str): Especie de la mascota
            edad (int): Edad de la mascota
        """
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def mostrar_informacion(self):
        """
        Muestra la información completa de la mascota de forma organizada.
        """
        print("\n" + "="*50)
        print("INFORMACIÓN DE LA MASCOTA")
        print("="*50)
        print(f"Nombre:     {self.nombre}")
        print(f"Especie:    {self.especie}")
        print(f"Edad:       {self.edad} años")
        print("="*50)

    def hacer_sonido(self):
        """
        Hace que la mascota emita un sonido característico según su especie.
        Implementa polimorfismo mediante la abstracción del tipo de animal.
        """
        sonidos = {
            "perro": "¡Guau guau!",
            "gato": "¡Miau miau!",
            "ave": "¡Pío pío!",
            "pajaro": "¡Pío pío!",
            "conejo": "¡Tictic tictic!",
            "caballo": "¡Iiiiii!",
            "vaca": "¡Muuu!",
            "cerdo": "¡Oinc oinc!",
            "oveja": "¡Beeee!"
        }

        # Obtener el sonido correspondiente o un sonido genérico
        especie_lower = self.especie.lower()
        sonido = sonidos.get(especie_lower, "¡Hace sonidos características!")

        print(f"\n{self.nombre} dice: {sonido}")

    def obtener_descripcion(self):
        """
        Retorna una descripción textual de la mascota.

        Returns:
            str: Descripción de la mascota
        """
        return f"{self.nombre} es un/a {self.especie} de {self.edad} años"

    def envejecer(self):
        """
        Incrementa la edad de la mascota en un año.
        """
        self.edad += 1
        print(f"\n{self.nombre} ha cumplido un año más. Ahora tiene {self.edad} años.")

