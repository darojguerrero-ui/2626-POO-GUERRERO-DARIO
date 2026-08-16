from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.usuario import Usuario

def mostrar_menu(rest: Restaurante) -> None:
    print("========================================")
    print("       SISTEMA DE RESTAURANTE")
    print("========================================")
    for key in sorted(rest.MENU_MAP):
        print(f"{key}. {rest.MENU_MAP[key]}")
        if key == 5:
            print("----------------------------------------")
        if key == 7:
            print("----------------------------------------")

def solicitar_texto(prompt: str) -> str:
    return input(prompt).strip()

def solicitar_float(prompt: str) -> float:
    while True:
        try:
            valor = float(input(prompt))
            return valor
        except ValueError:
            print("Entrada inválida. Ingrese un número válido.")

def opcion_registrar_producto(rest: Restaurante) -> None:
    print("-- Registrar producto --")
    codigo = solicitar_texto("Código: ")
    nombre = solicitar_texto("Nombre: ")
    categoria = solicitar_texto("Categoría: ")
    precio = solicitar_float("Precio: ")
    producto = Producto(codigo=codigo, nombre=nombre, categoria=categoria, precio=precio)
    if rest.registrar_producto(producto):
        print("Producto registrado correctamente.")
    else:
        print("Error: ya existe un producto con ese código.")

def opcion_buscar_producto(rest: Restaurante) -> None:
    print("-- Buscar producto --")
    codigo = solicitar_texto("Código: ")
    prod = rest.buscar_producto(codigo)
    if prod:
        print("Producto encontrado:", prod)
    else:
        print("Producto no encontrado.")

def opcion_actualizar_producto(rest: Restaurante) -> None:
    print("-- Actualizar producto --")
    codigo = solicitar_texto("Código del producto a actualizar: ")
    prod = rest.buscar_producto(codigo)
    if not prod:
        print("Producto no encontrado.")
        return
    print("Dejar campo vacío para mantener el valor actual.")
    nombre = input(f"Nombre [{prod.nombre}]: ").strip() or None
    categoria = input(f"Categoría [{prod.categoria}]: ").strip() or None
    precio_input = input(f"Precio [{prod.precio}]: ").strip()
    precio = None
    if precio_input:
        try:
            precio = float(precio_input)
        except ValueError:
            print("Precio inválido. No se actualizó el precio.")
    if rest.actualizar_producto(codigo, nombre=nombre, categoria=categoria, precio=precio):
        print("Producto actualizado.")
    else:
        print("No se pudo actualizar el producto.")

def opcion_eliminar_producto(rest: Restaurante) -> None:
    print("-- Eliminar producto --")
    codigo = solicitar_texto("Código: ")
    if rest.eliminar_producto(codigo):
        print("Producto eliminado.")
    else:
        print("Producto no encontrado.")

def opcion_listar_productos(rest: Restaurante) -> None:
    print("-- Listado de productos --")
    productos = rest.listar_productos()
    if not productos:
        print("No hay productos registrados.")
        return
    for p in productos:
        print(p)

def opcion_registrar_usuario(rest: Restaurante) -> None:
    print("-- Registrar usuario --")
    identificacion = solicitar_texto("Identificación: ")
    nombre = solicitar_texto("Nombre: ")
    correo = solicitar_texto("Correo: ")
    celular = solicitar_texto("Celular: ")
    usuario = Usuario(identificacion=identificacion, nombre=nombre, correo=correo, celular=celular)
    if rest.registrar_usuario(usuario):
        print("Usuario registrado correctamente.")
    else:
        print("Error: ya existe un usuario con esa identificación.")

def opcion_listar_usuarios(rest: Restaurante) -> None:
    print("-- Listado de usuarios --")
    usuarios = rest.listar_usuarios()
    if not usuarios:
        print("No hay usuarios registrados.")
        return
    for u in usuarios:
        print(u)

def opcion_mostrar_categorias(rest: Restaurante) -> None:
    print("-- Categorías únicas --")
    categorias = rest.categorias_unicas()
    if not categorias:
        print("No hay categorías registradas.")
        return
    for c in sorted(categorias):
        print(c)

def main() -> None:
    rest = Restaurante()
    acciones = {
        1: opcion_registrar_producto,
        2: opcion_buscar_producto,
        3: opcion_actualizar_producto,
        4: opcion_eliminar_producto,
        5: opcion_listar_productos,
        6: opcion_registrar_usuario,
        7: opcion_listar_usuarios,
        8: opcion_mostrar_categorias,
    }

    while True:
        try:
            mostrar_menu(rest)
            seleccion = input("Seleccione una opción: ").strip()
            if not seleccion:
                continue
            try:
                opcion = int(seleccion)
            except ValueError:
                print("Opción inválida. Ingrese el número de la opción.")
                continue
            if opcion == 9:
                print("Saliendo...")
                break
            accion = acciones.get(opcion)
            if accion:
                accion(rest)
            else:
                print("Opción no válida.")
        except KeyboardInterrupt:
            print("\nInterrupción por teclado. Saliendo...")
            break

if __name__ == '__main__':
    main()
