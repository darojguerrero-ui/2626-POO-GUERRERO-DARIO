"""
Módulo: main.py
Descripción: Punto de entrada del programa restaurante_app.
             Este archivo crea instancias de productos y demuestra el funcionamiento
             del sistema con la aplicación de herencia, encapsulación y polimorfismo.
"""

from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante


def imprimir_separador(titulo=""):
    """Imprime un separador visual decorativo."""
    if titulo:
        print(f"\n{'=' * 70}")
        print(f"  {titulo}")
        print(f"{'=' * 70}\n")
    else:
        print(f"{'-' * 70}\n")


def main():
    """
    Función principal que ejecuta el programa.
    Crea productos, los agrega al restaurante y demuestra todas las funcionalidades.
    """
    
    # SECCIÓN 1: INTRODUCCIÓN Y CREACIÓN DEL RESTAURANTE
    imprimir_separador("BIENVENIDA AL SISTEMA RESTAURANTE_APP")
    print("Sistema de Gestión de Productos de Restaurante")
    print("Demostrando: Herencia, Encapsulación y Polimorfismo en Python\n")
    
    restaurante = Restaurante("Restaurant Delicioso")
    print(f"✓ Restaurante '{restaurante.nombre}' creado exitosamente.\n")
    
    
    # SECCIÓN 2: CREAR INSTANCIAS DE PRODUCTOS
    imprimir_separador("CREANDO PRODUCTOS DEL RESTAURANTE")
    
    print("📋 Creando Platillos (heredan de Producto):")
    platillo_1 = Platillo(
        nombre="Pollo a la Parmesana",
        precio=15.99,
        calorias=850,
        tiempo_preparacion=25
    )
    print(f"   ✓ {platillo_1.nombre} creado")
    print(f"     - Atributos: nombre={platillo_1.nombre}, precio=${platillo_1.obtener_precio():.2f}")
    print(f"     - Atributos específicos: calorias={platillo_1.calorias}, tiempo_preparacion={platillo_1.tiempo_preparacion} min\n")
    
    platillo_2 = Platillo(
        nombre="Pasta Carbonara",
        precio=12.50,
        calorias=720,
        tiempo_preparacion=20
    )
    print(f"   ✓ {platillo_2.nombre} creado")
    print(f"     - Atributos: nombre={platillo_2.nombre}, precio=${platillo_2.obtener_precio():.2f}")
    print(f"     - Atributos específicos: calorias={platillo_2.calorias}, tiempo_preparacion={platillo_2.tiempo_preparacion} min\n")
    
    print("📋 Creando Bebidas (heredan de Producto):")
    bebida_1 = Bebida(
        nombre="Jugo de Naranja Natural",
        precio=4.50,
        volumen_ml=300,
        tipo_bebida="Fría"
    )
    print(f"   ✓ {bebida_1.nombre} creado")
    print(f"     - Atributos: nombre={bebida_1.nombre}, precio=${bebida_1.obtener_precio():.2f}")
    print(f"     - Atributos específicos: volumen_ml={bebida_1.volumen_ml}, tipo_bebida={bebida_1.tipo_bebida}\n")
    
    bebida_2 = Bebida(
        nombre="Café Expreso",
        precio=3.00,
        volumen_ml=100,
        tipo_bebida="Caliente"
    )
    print(f"   ✓ {bebida_2.nombre} creado")
    print(f"     - Atributos: nombre={bebida_2.nombre}, precio=${bebida_2.obtener_precio():.2f}")
    print(f"     - Atributos específicos: volumen_ml={bebida_2.volumen_ml}, tipo_bebida={bebida_2.tipo_bebida}\n")
    
    
    # SECCIÓN 3: AGREGAR PRODUCTOS AL RESTAURANTE
    imprimir_separador("AGREGANDO PRODUCTOS AL RESTAURANTE")
    restaurante.agregar_producto(platillo_1)
    restaurante.agregar_producto(platillo_2)
    restaurante.agregar_producto(bebida_1)
    restaurante.agregar_producto(bebida_2)
    print(f"✓ Total de productos agregados: {restaurante.obtener_cantidad_productos()}\n")
    
    
    # SECCIÓN 4: MOSTRAR MENÚ INICIAL (POLIMORFISMO)
    imprimir_separador("MENÚ INICIAL DEL RESTAURANTE - POLIMORFISMO EN ACCIÓN")
    print("Nota: El método mostrar_informacion() se ejecuta de forma diferente")
    print("según el tipo específico del objeto (Platillo o Bebida).\n")
    restaurante.mostrar_menu()
    
    
    # SECCIÓN 5: DEMOSTRACIÓN DE ENCAPSULACIÓN
    imprimir_separador("DEMOSTRANDO ENCAPSULACIÓN")
    print("El atributo __precio es PRIVADO (encapsulado).")
    print("Solo puede ser accedido a través de métodos específicos.\n")
    
    print(f"Accediendo a precios mediante obtener_precio():")
    print(f"  • {platillo_1.nombre}: ${platillo_1.obtener_precio():.2f}")
    print(f"  • {platillo_2.nombre}: ${platillo_2.obtener_precio():.2f}")
    print(f"  • {bebida_1.nombre}: ${bebida_1.obtener_precio():.2f}")
    print(f"  • {bebida_2.nombre}: ${bebida_2.obtener_precio():.2f}\n")
    
    print("❌ Intentando acceder directamente a __precio (fallará):")
    try:
        precio_directo = platillo_1.__precio
        print(f"   Esto no debería funcionar...")
    except AttributeError:
        print(f"   ✓ AttributeError capturado: El atributo '__precio' no existe directamente")
        print(f"     (Python maneja el name mangling para atributos privados)\n")
    
    
    # SECCIÓN 6: MODIFICACIÓN DE PRECIOS CON VALIDACIÓN
    imprimir_separador("DEMOSTRANDO VALIDACIÓN DE PRECIOS")
    
    print("CASO 1: Cambiar precio a un valor válido (positivo)")
    print(f"  Precio actual de {bebida_2.nombre}: ${bebida_2.obtener_precio():.2f}")
    print(f"  Intentando cambiar a $3.50...\n")
    try:
        bebida_2.cambiar_precio(3.50)
        print(f"  ✓ Éxito: Nuevo precio: ${bebida_2.obtener_precio():.2f}\n")
    except ValueError as e:
        print(f"  ✗ Error: {e}\n")
    
    print("CASO 2: Intentar establecer precio negativo")
    print(f"  Precio actual de {bebida_1.nombre}: ${bebida_1.obtener_precio():.2f}")
    print(f"  Intentando cambiar a -$5.00 (INVÁLIDO)...\n")
    try:
        bebida_1.cambiar_precio(-5.00)
        print(f"  ✗ Esto no debería funcionar\n")
    except ValueError as e:
        print(f"  ✓ Validación funcionando: {e}\n")
    
    print("CASO 3: Intentar establecer precio igual a cero")
    print(f"  Precio actual de {platillo_1.nombre}: ${platillo_1.obtener_precio():.2f}")
    print(f"  Intentando cambiar a $0.00 (INVÁLIDO)...\n")
    try:
        platillo_1.cambiar_precio(0.00)
        print(f"  ✗ Esto no debería funcionar\n")
    except ValueError as e:
        print(f"  ✓ Validación funcionando: {e}\n")
    
    print("CASO 4: Cambiar precio a un valor válido")
    print(f"  Precio actual de {platillo_1.nombre}: ${platillo_1.obtener_precio():.2f}")
    print(f"  Intentando cambiar a $16.99...\n")
    try:
        platillo_1.cambiar_precio(16.99)
        print(f"  ✓ Éxito: Nuevo precio: ${platillo_1.obtener_precio():.2f}\n")
    except ValueError as e:
        print(f"  ✗ Error: {e}\n")
    
    
    # SECCIÓN 7: MODIFICACIÓN DE DISPONIBILIDAD
    imprimir_separador("DEMOSTRANDO CAMBIO DE DISPONIBILIDAD")
    
    print(f"Estado actual de {platillo_2.nombre}: {'Disponible' if platillo_2.disponibilidad else 'No disponible'}")
    print(f"Cambiando disponibilidad a False...\n")
    platillo_2.cambiar_disponibilidad(False)
    print(f"✓ Nuevo estado: {'Disponible' if platillo_2.disponibilidad else 'No disponible'}\n")
    
    print(f"Estado actual de {bebida_2.nombre}: {'Disponible' if bebida_2.disponibilidad else 'No disponible'}")
    print(f"Cambiando disponibilidad a True...\n")
    bebida_2.cambiar_disponibilidad(True)
    print(f"✓ Nuevo estado: {'Disponible' if bebida_2.disponibilidad else 'No disponible'}\n")
    
    
    # SECCIÓN 8: BÚSQUEDA DE PRODUCTOS
    imprimir_separador("BUSCANDO PRODUCTOS POR NOMBRE")
    
    producto_buscado = restaurante.obtener_producto_por_nombre("Café Expreso")
    if producto_buscado:
        print(f"✓ Producto encontrado: {producto_buscado.nombre}")
        print(f"  Precio: ${producto_buscado.obtener_precio():.2f}")
        print(f"  Disponible: {'Sí' if producto_buscado.disponibilidad else 'No'}\n")
    
    producto_no_existe = restaurante.obtener_producto_por_nombre("Pizza")
    if producto_no_existe:
        print(f"✓ Producto encontrado: {producto_no_existe.nombre}\n")
    else:
        print(f"✗ Producto 'Pizza' no encontrado en el restaurante\n")
    
    
    # SECCIÓN 9: PRODUCTOS DISPONIBLES
    imprimir_separador("CONSULTANDO PRODUCTOS DISPONIBLES")
    
    productos_disponibles = restaurante.obtener_productos_disponibles()
    print(f"Total de productos disponibles: {len(productos_disponibles)}\n")
    for i, producto in enumerate(productos_disponibles, 1):
        print(f"{i}. {producto.nombre} - ${producto.obtener_precio():.2f}")
    print()
    
    
    # SECCIÓN 10: MENÚ FINAL ACTUALIZADO
    imprimir_separador("MENÚ FINAL DEL RESTAURANTE - DESPUÉS DE CAMBIOS")
    restaurante.mostrar_menu()
    
    
    # SECCIÓN 11: RESUMEN ESTADÍSTICO
    imprimir_separador("RESUMEN FINAL DEL SISTEMA")
    
    total_productos = restaurante.obtener_cantidad_productos()
    disponibles = len(restaurante.obtener_productos_disponibles())
    no_disponibles = total_productos - disponibles
    
    print(f"📊 ESTADÍSTICAS DEL RESTAURANTE '{restaurante.nombre}':")
    print(f"   • Total de productos: {total_productos}")
    print(f"   • Productos disponibles: {disponibles}")
    print(f"   • Productos no disponibles: {no_disponibles}\n")
    
    # Calcular precio promedio
    precio_total = sum(p.obtener_precio() for p in restaurante.productos)
    precio_promedio = precio_total / total_productos if total_productos > 0 else 0
    
    print(f"💰 INFORMACIÓN DE PRECIOS:")
    print(f"   • Precio total de inventario: ${precio_total:.2f}")
    print(f"   • Precio promedio: ${precio_promedio:.2f}\n")
    
    # Productos por tipo
    platillos = [p for p in restaurante.productos if isinstance(p, Platillo)]
    bebidas = [p for p in restaurante.productos if isinstance(p, Bebida)]
    
    print(f"🍽️  DESGLOSE POR TIPO:")
    print(f"   • Platillos: {len(platillos)}")
    for p in platillos:
        print(f"     - {p.nombre}: ${p.obtener_precio():.2f} ({p.calorias} kcal)")
    print(f"\n   • Bebidas: {len(bebidas)}")
    for b in bebidas:
        print(f"     - {b.nombre}: ${b.obtener_precio():.2f} ({b.volumen_ml} ml)")
    print()
    
    
    # SECCIÓN 12: INFORMACIÓN SOBRE PRINCIPIOS POO
    imprimir_separador("PRINCIPIOS DE POO DEMOSTRADOS")
    
    print("1️⃣  HERENCIA:")
    print("   • Platillo hereda de Producto")
    print("   • Bebida hereda de Producto")
    print("   • Ambas acceden a métodos de la clase padre mediante super()\n")
    
    print("2️⃣  ENCAPSULACIÓN:")
    print("   • El atributo __precio es privado en Producto")
    print("   • Se accede a través de obtener_precio()")
    print("   • Se modifica a través de cambiar_precio() con validación\n")
    
    print("3️⃣  POLIMORFISMO:")
    print("   • El método mostrar_informacion() es sobrescrito en cada clase hija")
    print("   • Cada una muestra información específica de su tipo")
    print("   • El restaurante ejecuta el método apropiado según el tipo de objeto\n")
    
    print("4️⃣  VALIDACIÓN Y SEGURIDAD:")
    print("   • Los precios no pueden ser negativos ni cero")
    print("   • Se lanzan excepciones ValueError para casos inválidos")
    print("   • El cliente debe manejar los errores correctamente\n")
    
    
    # SECCIÓN 13: DESPEDIDA
    imprimir_separador("FIN DE LA DEMOSTRACIÓN")
    print(f"{'*' * 70}")
    print(f"*{'¡Gracias por usar Restaurant Delicioso!'.center(68)}*")
    print(f"*{'Sistema desarrollado por: Dario Javier Guerrero Palma'.center(68)}*")
    print(f"*{'Tema: Programación Orientada a Objetos en Python'.center(68)}*")
    print(f"{'*' * 70}\n")


if __name__ == "__main__":
    main()
