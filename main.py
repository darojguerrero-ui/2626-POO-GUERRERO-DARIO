from pathlib import Path

from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante import Restaurante

BASE_DIR = Path(__file__).resolve().parent
DATOS_DIR = BASE_DIR / "datos"


def solicitar_texto(prompt: str) -> str:
    return input(prompt).strip()


def solicitar_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ingrese un número entero válido.")


def solicitar_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ingrese un número válido.")


def mostrar_menu() -> None:
    print("\n--- Menú Restaurante ---")
    print("1. Listar productos")
    print("2. Registrar producto")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Registrar usuario")
    print("6. Listar usuarios")
    print("7. Vender producto")
    print("8. Consultar ventas de un usuario")
    print("9. Salir")


def main() -> None:
    archivo = ArchivoServicio(str(DATOS_DIR))
    try:
        productos = archivo.cargar_productos()
        usuarios = archivo.cargar_usuarios()
        ventas = archivo.cargar_ventas()
    except (PermissionError, ValueError) as exc:
        print(f"Error al cargar los datos: {exc}")
        productos = []
        usuarios = []
        ventas = []

    restaurante = Restaurante(productos=productos, usuarios=usuarios, ventas=ventas)

    while True:
        try:
            mostrar_menu()
            opcion = input("Seleccione una opción: ").strip()
            if opcion == "1":
                productos_actuales = restaurante.listar_productos()
                if not productos_actuales:
                    print("No hay productos registrados.")
                    continue
                for producto in productos_actuales:
                    print(producto)
            elif opcion == "2":
                codigo = solicitar_texto("Código del producto: ")
                nombre = solicitar_texto("Nombre del producto: ")
                precio = solicitar_float("Precio: ")
                stock = solicitar_int("Stock: ")
                producto = Producto(codigo=codigo, nombre=nombre, precio=precio, stock=stock)
                restaurante.registrar_producto(producto)
                archivo.guardar_productos(restaurante.listar_productos())
                print("Producto registrado correctamente.")
            elif opcion == "3":
                codigo = solicitar_texto("Código del producto a actualizar: ")
                producto = restaurante.buscar_producto(codigo)
                if producto is None:
                    print("Producto no encontrado.")
                    continue
                nombre = input(f"Nombre [{producto.nombre}]: ").strip() or None
                precio_input = input(f"Precio [{producto.precio}]: ").strip()
                precio = float(precio_input) if precio_input else None
                stock_input = input(f"Stock [{producto.stock}]: ").strip()
                stock = int(stock_input) if stock_input else None
                restaurante.actualizar_producto(codigo, nombre=nombre, precio=precio, stock=stock)
                archivo.guardar_productos(restaurante.listar_productos())
                print("Producto actualizado correctamente.")
            elif opcion == "4":
                codigo = solicitar_texto("Código del producto a eliminar: ")
                if restaurante.eliminar_producto(codigo):
                    archivo.guardar_productos(restaurante.listar_productos())
                    print("Producto eliminado correctamente.")
                else:
                    print("Producto no encontrado.")
            elif opcion == "5":
                identificacion = solicitar_texto("Identificación del usuario: ")
                nombre = solicitar_texto("Nombre del usuario: ")
                correo = solicitar_texto("Correo (opcional): ") or None
                celular = solicitar_texto("Celular (opcional): ") or None
                usuario = Usuario(identificacion=identificacion, nombre=nombre, correo=correo, celular=celular)
                restaurante.registrar_usuario(usuario)
                archivo.guardar_usuarios(restaurante.listar_usuarios())
                print("Usuario registrado correctamente.")
            elif opcion == "6":
                usuarios = restaurante.listar_usuarios()
                if not usuarios:
                    print("No hay usuarios registrados.")
                    continue
                for usuario in usuarios:
                    print(usuario)
            elif opcion == "7":
                codigo = solicitar_texto("Código del producto: ")
                identificacion = solicitar_texto("Identificación del usuario: ")
                cantidad = solicitar_int("Cantidad: ")
                resultado = restaurante.vender_producto(codigo, identificacion, cantidad)
                if resultado:
                    archivo.guardar_productos(restaurante.listar_productos())
                    archivo.guardar_ventas(restaurante.listar_ventas())
                    print("Venta registrada correctamente.")
                else:
                    print("La venta no se puede completar. Verifique usuario, producto, cantidad y stock.")
            elif opcion == "8":
                identificacion = solicitar_texto("Identificación del usuario: ")
                ventas_usuario = restaurante.ventas_por_usuario(identificacion)
                if not ventas_usuario:
                    print("No se registraron ventas para ese usuario.")
                    continue
                for venta in ventas_usuario:
                    producto = restaurante.buscar_producto(venta.producto_codigo)
                    nombre_producto = producto.nombre if producto else "Producto no disponible"
                    print(f"- {venta.producto_codigo} | {nombre_producto} | Cantidad: {venta.cantidad}")
            elif opcion == "9":
                print("Saliendo...")
                break
            else:
                print("Opción inválida.")
        except KeyboardInterrupt:
            print("\nInterrupción por teclado. Saliendo...")
            break
        except (PermissionError, ValueError) as exc:
            print(f"Error: {exc}")


if __name__ == "__main__":
    main()