from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

def ejecutar_sistema():
    """
    Punto de entrada principal para ejecutar la simulación del sistema de gestión de restaurante.
    """
    # 1. Instanciar el servicio
    mi_restaurante = Restaurante("La Delicia de Dario")

    # 2. Crear y agregar productos
    try:
        p1 = Producto("Arroz Marinero", 12.50)
        p2 = Producto("Ceviche Mixto", 10.00)
        p3 = Producto("Soda", 1.50, disponible=False)
        
        mi_restaurante.agregar_producto(p1)
        mi_restaurante.agregar_producto(p2)
        mi_restaurante.agregar_producto(p3)

        # Intento de crear un producto con precio inválido
        # p_error = Producto("Error", -5.00) 
    except ValueError as e:
        print(f"Error de validación: {e}")

    # 3. Registrar un cliente
    cliente1 = Cliente(1, "Dario Guerrero", "dario.guerrero@email.com", "0987654321")
    mi_restaurante.agregar_cliente(cliente1)

    # 4. Mostrar resultados
    mi_restaurante.mostrar_menu()

if __name__ == "__main__":
    ejecutar_sistema()