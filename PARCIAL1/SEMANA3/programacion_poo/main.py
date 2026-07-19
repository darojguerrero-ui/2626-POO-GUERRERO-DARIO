# Programación Orientada a Objetos - Programa Principal
# Autor: Dario Guerrero
# Descripción: Programa que demuestra el uso de clases, objetos, atributos y métodos

from mascota import Mascota

def main():
    """
    Función principal que crea objetos de la clase Mascota
    y ejecuta sus métodos.
    """

    print("\n" + "="*70)
    print("SISTEMA DE GESTIÓN DE MASCOTAS - ORIENTADO A OBJETOS")
    print("="*70)

    # Crear el primer objeto de la clase Mascota
    print("\n>>> Creando primer objeto Mascota...")
    mascota1 = Mascota("Max", "Perro", 3)

    # Crear el segundo objeto de la clase Mascota
    print(">>> Creando segundo objeto Mascota...")
    mascota2 = Mascota("Whiskers", "Gato", 2)

    # Crear un tercer objeto para demostrar más funcionalidad
    print(">>> Creando tercer objeto Mascota...")
    mascota3 = Mascota("Tweety", "Ave", 1)

    # Demostración con el primer objeto (Perro)
    print("\n" + "="*70)
    print("DEMOSTRACIÓN CON EL PRIMER OBJETO - MASCOTA1")
    print("="*70)

    mascota1.mostrar_informacion()
    mascota1.hacer_sonido()
    print(f"\nDescripción: {mascota1.obtener_descripcion()}")

    # Demostración con el segundo objeto (Gato)
    print("\n" + "="*70)
    print("DEMOSTRACIÓN CON EL SEGUNDO OBJETO - MASCOTA2")
    print("="*70)

    mascota2.mostrar_informacion()
    mascota2.hacer_sonido()
    print(f"\nDescripción: {mascota2.obtener_descripcion()}")

    # Demostración con el tercer objeto (Ave)
    print("\n" + "="*70)
    print("DEMOSTRACIÓN CON EL TERCER OBJETO - MASCOTA3")
    print("="*70)

    mascota3.mostrar_informacion()
    mascota3.hacer_sonido()
    print(f"\nDescripción: {mascota3.obtener_descripcion()}")

    # Demostración de método adicional
    print("\n" + "="*70)
    print("DEMOSTRACIÓN DE MÉTODO: ENVEJECER")
    print("="*70)

    mascota1.envejecer()
    mascota2.envejecer()
    mascota3.envejecer()

    # Mostrar información actualizada
    print("\n" + "="*70)
    print("INFORMACIÓN ACTUALIZADA DESPUÉS DE ENVEJECER")
    print("="*70)

    print(f"\n{mascota1.obtener_descripcion()}")
    print(f"{mascota2.obtener_descripcion()}")
    print(f"{mascota3.obtener_descripcion()}")

    # Resumen de objetos creados
    print("\n" + "="*70)
    print("RESUMEN DE OBJETOS CREADOS")
    print("="*70)

    mascotas = [mascota1, mascota2, mascota3]

    print(f"\nTotal de mascotas creadas: {len(mascotas)}\n")

    for indice, mascota in enumerate(mascotas, 1):
        print(f"{indice}. {mascota.obtener_descripcion()}")

    print("\n" + "="*70)
    print("FIN DEL PROGRAMA")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()

