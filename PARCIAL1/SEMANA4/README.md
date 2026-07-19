# Sistema de Gestion de Restaurante

## Descripcion

Sistema basico de gestion de restaurante desarrollado en Python utilizando Programacion Orientada a Objetos (POO). Demuestra la organizacion de un proyecto en modulos, separacion de responsabilidades e integracion de archivos mediante importaciones.

## Estructura del Proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py          # Clase Producto
│   └── cliente.py           # Clase Cliente
├── servicios/
│   ├── __init__.py
│   └── restaurante.py       # Clase Restaurante
└── main.py                  # Punto de entrada del programa
```

## Clases Principales

### 1. Producto (modelos/producto.py)

Representa un plato, bebida o producto disponible en el restaurante.

**Atributos:**
- `id_producto`: Identificador unico del producto
- `nombre`: Nombre del producto
- `categoria`: Categoria (Entrada, Plato Principal, Postre, Bebida)
- `precio`: Precio del producto
- `disponible`: Estado de disponibilidad (bool)

**Metodos principales:**
- `__init__()`: Constructor
- `cambiar_disponibilidad()`: Cambia el estado de disponibilidad
- `actualizar_precio()`: Actualiza el precio del producto
- `obtener_informacion()`: Retorna informacion como diccionario
- `__str__()`: Representacion en texto del producto

### 2. Cliente (modelos/cliente.py)

Representa una persona que realiza o consume un pedido en el restaurante.

**Atributos:**
- `id_cliente`: Identificador unico del cliente
- `nombre`: Nombre completo del cliente
- `email`: Correo electronico
- `telefono`: Numero de telefono
- `registro_activo`: Estado del registro
- `pedidos`: Lista de pedidos realizados

**Metodos principales:**
- `__init__()`: Constructor
- `actualizar_contacto()`: Actualiza email y/o telefono
- `registrar_pedido()`: Registra un nuevo pedido
- `obtener_informacion()`: Retorna informacion como diccionario
- `__str__()`: Representacion en texto del cliente

### 3. Restaurante (servicios/restaurante.py)

Gestiona las operaciones principales del sistema.

**Atributos:**
- `nombre`: Nombre del restaurante
- `productos`: Lista de productos en catalogo
- `clientes`: Lista de clientes registrados
- `total_ventas`: Total acumulado de ventas

**Metodos principales:**
- `__init__()`: Constructor
- `agregar_producto()`: Agrega un producto al catalogo
- `registrar_cliente()`: Registra un nuevo cliente
- `obtener_producto_por_id()`: Busca producto por ID
- `obtener_cliente_por_id()`: Busca cliente por ID
- `listar_productos_disponibles()`: Lista productos disponibles
- `listar_productos_por_categoria()`: Filtra productos por categoria
- `registrar_venta()`: Registra una venta
- `mostrar_catalogo_productos()`: Muestra catalogo formateado
- `mostrar_clientes_registrados()`: Muestra lista de clientes
- `mostrar_resumen_sistema()`: Muestra resumen general
- `__str__()`: Representacion en texto del restaurante

## Funcionalidades Demostrables

El programa `main.py` demuestra:

1. **Creacion de objetos**: Instanciacion de productos, clientes y restaurante
2. **Gestion de productos**: Agregar productos al catalogo, cambiar disponibilidad, actualizar precios
3. **Registro de clientes**: Registrar nuevos clientes, actualizar informacion de contacto
4. **Operaciones comerciales**: Registrar ventas, rastrear pedidos
5. **Consultas y reportes**: Listar productos disponibles, mostrar clientes, generar resumenes
6. **Metodos especiales**: Uso de `__str__()` para representacion en texto
7. **Importaciones modulares**: Uso correcto de imports entre archivos

## Como Ejecutar

1. Navegar a la carpeta del proyecto:
   ```
   cd restaurante_app
   ```

2. Ejecutar el programa principal:
   ```
   python main.py
   ```

## Requisitos Cumplidos

✓ Proyecto estructurado con carpetas modelos y servicios
✓ Dos clases en modelos (Producto, Cliente)
✓ Una clase en servicios (Restaurante)
✓ Constructores `__init__()` implementados
✓ Atributos pertinentes segun el contexto del restaurante
✓ Metodos para gestionar informacion
✓ Metodo especial `__str__()` implementado en todas las clases
✓ Importaciones correctas entre archivos
✓ Creacion de objetos desde main.py
✓ Objetos agregados al servicio principal
✓ Informacion mostrada de forma organizada en consola
✓ Comentarios explicativos en el codigo

## Ejemplo de Uso

```python
# Crear restaurante
restaurante = Restaurante("La Buena Mesa")

# Crear productos
filete = Producto(1, "Filete Mignon", "Plato Principal", 24.99)
cafe = Producto(2, "Cafe Expreso", "Bebida", 3.50)

# Agregar productos
restaurante.agregar_producto(filete)
restaurante.agregar_producto(cafe)

# Crear cliente
cliente = Cliente(101, "Juan Perez", "juan@email.com", "555-0101")

# Registrar cliente
restaurante.registrar_cliente(cliente)

# Registrar venta
restaurante.registrar_venta(101, 1, 1)

# Mostrar informacion
print(restaurante)
```

## Autor

Desarrollado como actividad de aprendizaje de POO en Python.

