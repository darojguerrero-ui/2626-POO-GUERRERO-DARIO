from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

def mostrar_menu():
    """Muestra el menú principal del sistema."""
    print("\n========================================")
    print("        SISTEMA DE RESTAURANTE")
    print("========================================")
    print("1. Registrar producto")
    print("2. Registrar bebida")
    print("3. Registrar cliente")
    print("----------------------------------------")
    print("4. Listar productos")
    print("5. Listar clientes")
    print("----------------------------------------")
    print("6. Salir")
    print("========================================")

def registrar_producto_menu(restaurante: Restaurante):
    """Solicita datos para registrar un producto."""
    print("\n--- Registrar Producto ---")
    try:
        codigo = input("Ingrese código del producto: ").strip()
        nombre = input("Ingrese nombre del producto: ").strip()
        categoria = input("Ingrese categoría del producto: ").strip()
        precio = float(input("Ingrese precio del producto: "))
        
        producto = Producto(codigo, nombre, categoria, precio)
        restaurante.registrar_producto(producto)
    except ValueError as e:
        print(f"Error al registrar producto: {e}. Asegúrese de ingresar datos válidos.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

def registrar_bebida_menu(restaurante: Restaurante):
    """Solicita datos para registrar una bebida."""
    print("\n--- Registrar Bebida ---")
    try:
        codigo = input("Ingrese código de la bebida: ").strip()
        nombre = input("Ingrese nombre de la bebida: ").strip()
        categoria = input("Ingrese categoría de la bebida: ").strip()
        precio = float(input("Ingrese precio de la bebida: "))
        tamano = input("Ingrese tamaño de la bebida (ej. 330ml, 1L): ").strip()
        tipo_envase = input("Ingrese tipo de envase de la bebida (ej. Botella, Lata): ").strip()

        bebida = Bebida(codigo, nombre, categoria, precio, tamano, tipo_envase)
        restaurante.registrar_producto(bebida) # Se registra como producto
    except ValueError as e:
        print(f"Error al registrar bebida: {e}. Asegúrese de ingresar datos válidos.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

def registrar_cliente_menu(restaurante: Restaurante):
    """Solicita datos para registrar un cliente."""
    print("\n--- Registrar Cliente ---")
    try:
        identificacion = input("Ingrese identificación del cliente: ").strip()
        nombre = input("Ingrese nombre del cliente: ").strip()
        correo = input("Ingrese correo electrónico del cliente: ").strip()

        cliente = Cliente(identificacion, nombre, correo)
        restaurante.registrar_cliente(cliente)
    except ValueError as e:
        print(f"Error al registrar cliente: {e}. Asegúrese de ingresar datos válidos.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

def main():
    restaurante = Restaurante()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            registrar_producto_menu(restaurante)
        elif opcion == '2':
            registrar_bebida_menu(restaurante)
        elif opcion == '3':
            registrar_cliente_menu(restaurante)
        elif opcion == '4':
            restaurante.listar_productos()
        elif opcion == '5':
            restaurante.listar_clientes()
        elif opcion == '6':
            print("Saliendo del sistema. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
