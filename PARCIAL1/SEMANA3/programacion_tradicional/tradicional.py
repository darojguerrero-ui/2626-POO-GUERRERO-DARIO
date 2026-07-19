# Programación Tradicional - Gestión de Mascotas
# Sin uso de clases ni objetos
# Autor: Dario Guerrero
# Descripción: Sistema para registrar y mostrar información de mascotas

# Variables globales para almacenar información de mascotas
mascotas = []

def registrar_mascota():
    """
    Función para registrar una nueva mascota solicitando datos por teclado
    """
    print("\n" + "="*50)
    print("REGISTRAR NUEVA MASCOTA")
    print("="*50)

    # Solicitar datos por teclado
    nombre = input("Ingrese el nombre de la mascota: ").strip()
    tipo = input("Ingrese el tipo de mascota (perro, gato, ave, etc.): ").strip()
    edad = input("Ingrese la edad de la mascota: ").strip()
    raza = input("Ingrese la raza de la mascota: ").strip()
    peso = input("Ingrese el peso de la mascota (kg): ").strip()
    color = input("Ingrese el color de la mascota: ").strip()
    dueño = input("Ingrese el nombre del dueño: ").strip()

    # Crear un diccionario con los datos de la mascota
    mascota = {
        "nombre": nombre,
        "tipo": tipo,
        "edad": edad,
        "raza": raza,
        "peso": peso,
        "color": color,
        "dueño": dueño
    }

    # Agregar la mascota a la lista
    mascotas.append(mascota)
    print("\n✓ ¡Mascota registrada exitosamente!")


def mostrar_todas_mascotas():
    """
    Función para mostrar la información de todas las mascotas registradas
    """
    print("\n" + "="*70)
    print("LISTADO DE MASCOTAS REGISTRADAS")
    print("="*70)

    if len(mascotas) == 0:
        print("\nNo hay mascotas registradas aún.")
        return

    for indice, mascota in enumerate(mascotas, 1):
        print(f"\n--- Mascota #{indice} ---")
        print(f"Nombre:     {mascota['nombre']}")
        print(f"Tipo:       {mascota['tipo']}")
        print(f"Edad:       {mascota['edad']}")
        print(f"Raza:       {mascota['raza']}")
        print(f"Peso:       {mascota['peso']} kg")
        print(f"Color:      {mascota['color']}")
        print(f"Dueño:      {mascota['dueño']}")


def mostrar_mascota_especifica():
    """
    Función para mostrar la información de una mascota específica
    """
    if len(mascotas) == 0:
        print("\nNo hay mascotas registradas.")
        return

    print("\n" + "="*50)
    nombre_buscar = input("Ingrese el nombre de la mascota a buscar: ").strip()

    encontrada = False
    for mascota in mascotas:
        if mascota['nombre'].lower() == nombre_buscar.lower():
            print("\n" + "="*50)
            print("INFORMACIÓN DE LA MASCOTA")
            print("="*50)
            print(f"Nombre:     {mascota['nombre']}")
            print(f"Tipo:       {mascota['tipo']}")
            print(f"Edad:       {mascota['edad']}")
            print(f"Raza:       {mascota['raza']}")
            print(f"Peso:       {mascota['peso']} kg")
            print(f"Color:      {mascota['color']}")
            print(f"Dueño:      {mascota['dueño']}")
            encontrada = True
            break

    if not encontrada:
        print(f"\n✗ No se encontró una mascota con el nombre '{nombre_buscar}'")


def buscar_por_tipo():
    """
    Función para mostrar mascotas según su tipo
    """
    if len(mascotas) == 0:
        print("\nNo hay mascotas registradas.")
        return

    print("\n" + "="*50)
    tipo_buscar = input("Ingrese el tipo de mascota a buscar: ").strip()

    mascotas_encontradas = [m for m in mascotas if m['tipo'].lower() == tipo_buscar.lower()]

    if len(mascotas_encontradas) == 0:
        print(f"\n✗ No se encontraron mascotas del tipo '{tipo_buscar}'")
    else:
        print("\n" + "="*70)
        print(f"MASCOTAS DEL TIPO: {tipo_buscar.upper()}")
        print("="*70)
        for indice, mascota in enumerate(mascotas_encontradas, 1):
            print(f"\n--- {tipo_buscar} #{indice} ---")
            print(f"Nombre:     {mascota['nombre']}")
            print(f"Edad:       {mascota['edad']}")
            print(f"Raza:       {mascota['raza']}")
            print(f"Color:      {mascota['color']}")
            print(f"Dueño:      {mascota['dueño']}")


def mostrar_estadisticas():
    """
    Función para mostrar estadísticas de las mascotas
    """
    if len(mascotas) == 0:
        print("\nNo hay mascotas registradas.")
        return

    print("\n" + "="*50)
    print("ESTADÍSTICAS")
    print("="*50)
    print(f"Total de mascotas registradas: {len(mascotas)}")

    tipos = {}
    for mascota in mascotas:
        tipo = mascota['tipo'].lower()
        tipos[tipo] = tipos.get(tipo, 0) + 1

    print("\nDistribución por tipo:")
    for tipo, cantidad in tipos.items():
        print(f"  - {tipo.capitalize()}: {cantidad}")


def mostrar_menu():
    """
    Función para mostrar el menú principal
    """
    print("\n" + "="*50)
    print("SISTEMA DE GESTIÓN DE MASCOTAS")
    print("="*50)
    print("1. Registrar nueva mascota")
    print("2. Mostrar todas las mascotas")
    print("3. Buscar mascota por nombre")
    print("4. Buscar mascotas por tipo")
    print("5. Ver estadísticas")
    print("6. Salir")
    print("="*50)


def main():
    """
    Función principal que controla el flujo del programa
    """
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ").strip()

        if opcion == "1":
            registrar_mascota()
        elif opcion == "2":
            mostrar_todas_mascotas()
        elif opcion == "3":
            mostrar_mascota_especifica()
        elif opcion == "4":
            buscar_por_tipo()
        elif opcion == "5":
            mostrar_estadisticas()
        elif opcion == "6":
            print("\n¡Hasta luego!")
            break
        else:
            print("\n✗ Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()
