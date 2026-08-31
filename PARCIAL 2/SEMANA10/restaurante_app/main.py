from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante import Restaurante
from modelos.producto import Producto

DATOS_PATH = "/2626-POO-GUERRERO-DARIO-/PARCIAL 2/SEMANA10/restaurante_app/datos/productos.json"


def solicitar_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ingrese un número entero válido")


def solicitar_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ingrese un número válido")


def main() -> None:
    archivo = ArchivoServicio(DATOS_PATH)
    productos_iniciales = archivo.cargar()
    restaurante = Restaurante(productos_iniciales)
    print("Productos cargados:")
    for p in restaurante.listar():
        print(" ", p)

    while True:
        print("\n--- Menú ---")
        print("1. Listar productos")
        print("2. Registrar producto")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Salir")
        opc = input("Seleccione opción: ").strip()
        if opc == "1":
            for p in restaurante.listar():
                print(p)
        elif opc == "2":
            try:
                id_ = solicitar_int("ID: ")
                nombre = input("Nombre: ").strip()
                precio = solicitar_float("Precio: ")
                stock = solicitar_int("Stock: ")
                prod = Producto(id_, nombre, precio, stock)
                restaurante.registrar(prod)
                archivo.guardar(restaurante.listar())
                print("Producto registrado y guardado.")
            except Exception as e:
                print(f"No se pudo registrar producto: {e}")
        elif opc == "3":
            try:
                id_ = solicitar_int("ID a actualizar: ")
                p = restaurante.buscar_por_id(id_)
                if not p:
                    print("Producto no encontrado")
                    continue
                nombre = input(f"Nombre [{p.nombre}]: ").strip() or None
                precio_input = input(f"Precio [{p.precio}]: ").strip()
                precio = float(precio_input) if precio_input else None
                stock_input = input(f"Stock [{p.stock}]: ").strip()
                stock = int(stock_input) if stock_input else None
                restaurante.actualizar(id_, nombre=nombre, precio=precio, stock=stock)
                archivo.guardar(restaurante.listar())
                print("Producto actualizado y guardado.")
            except Exception as e:
                print(f"No se pudo actualizar: {e}")
        elif opc == "4":
            try:
                id_ = solicitar_int("ID a eliminar: ")
                restaurante.eliminar(id_)
                archivo.guardar(restaurante.listar())
                print("Producto eliminado y cambios guardados.")
            except Exception as e:
                print(f"No se pudo eliminar: {e}")
        elif opc == "5":
            print("Saliendo...")
            break
        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()