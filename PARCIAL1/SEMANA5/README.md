# Sistema Básico de Gestión de Restaurante

## Estudiante
DARIO JAVIER GUERRERO PALMA

## Descripción del Sistema
Este proyecto implementa un sistema básico de gestión para un restaurante utilizando Programación Orientada a Objetos (POO) en Python. El objetivo principal es demostrar la aplicación de principios de POO, como clases, objetos, encapsulamiento, y modularidad, junto con el uso de identificadores descriptivos y tipos de datos adecuados.

El sistema permite:
*   Representar productos (platos, bebidas) con su nombre, precio y disponibilidad.
*   Representar clientes con su ID, nombre, email y teléfono.
*   Administrar y gestionar listas de productos y clientes a través de una clase de servicio principal (`Restaurante`).
*   Agregar, mostrar y actualizar información básica de productos y clientes.

## Estructura del Proyecto
El proyecto está organizado de forma modular para separar las responsabilidades y facilitar la comprensión y el mantenimiento.

```
.
├── restaurante_app/
│   ├── modelos/
│   │   ├── __init__.py
│   │   ├── producto.py       # Define la clase Producto
│   │   └── cliente.py        # Define la clase Cliente
│   ├── servicios/
│   │   ├── __init__.py
│   │   └── restaurante.py    # Define la clase Restaurante para la gestión
│   └── main.py               # Punto de entrada del programa
└── README.md                 # Este archivo
```

### Responsabilidades:
*   **`modelos/`**: Contiene las definiciones de las clases que representan las entidades principales del negocio (Producto, Cliente).
*   **`servicios/`**: Contiene la lógica de negocio y las clases que gestionan las interacciones entre las entidades (Restaurante).
*   **`main.py`**: Es el script principal que inicializa el sistema, crea objetos, interactúa con el servicio `Restaurante` y muestra los resultados.

## Tipos de Datos Utilizados en las Clases

### Clase `Producto` (en `modelos/producto.py`)
*   `nombre`: `str` (cadena de texto para el nombre del producto)
*   `precio`: `float` (número decimal para el precio del producto)
*   `disponible`: `bool` (booleano para indicar si el producto está disponible o no)

### Clase `Cliente` (en `modelos/cliente.py`)
*   `id_cliente`: `int` (número entero para el identificador único del cliente)
*   `nombre`: `str` (cadena de texto para el nombre completo del cliente)
*   `email`: `str` (cadena de texto para la dirección de correo electrónico del cliente)
*   `telefono`: `str` (cadena de texto para el número de teléfono del cliente)

### Clase `Restaurante` (en `servicios/restaurante.py`)
*   `nombre_restaurante`: `str` (cadena de texto para el nombre del restaurante)
*   `productos`: `list[Producto]` (una lista que almacena objetos de la clase `Producto`)
*   `clientes`: `list[Cliente]` (una lista que almacena objetos de la clase `Cliente`)

## Reflexión sobre la Importancia de Identificadores Descriptivos, Tipos de Datos Adecuados y Listas

En el desarrollo de software, especialmente en proyectos modulares con Python, la elección y aplicación de identificadores descriptivos, tipos de datos adecuados y estructuras de datos como las listas son fundamentales por varias razones:

1.  **Legibilidad y Mantenibilidad**: Los identificadores descriptivos (ej. `nombre_restaurante` en lugar de `n` o `x`) hacen que el código sea mucho más fácil de leer y entender, tanto para el desarrollador original como para otros colaboradores. Esto reduce el tiempo y el esfuerzo necesarios para depurar, modificar o extender el sistema en el futuro.

2.  **Claridad y Prevención de Errores**: Utilizar tipos de datos adecuados (`float` para precios, `bool` para disponibilidad) asegura que los datos se almacenen y manipulen de la manera correcta, evitando errores lógicos y facilitando la validación. Las anotaciones de tipo (`nombre: str`) mejoran la claridad y permiten a las herramientas de desarrollo (IDEs) ofrecer mejores sugerencias y detección temprana de errores.

3.  **Organización y Gestión de Colecciones**: Las listas (`list[Producto]`, `list[Cliente]`) son esenciales para almacenar y gestionar colecciones de objetos de manera eficiente. Permiten agrupar elementos relacionados, iterar sobre ellos y aplicar operaciones conjuntas, lo cual es crucial en sistemas donde se manejan múltiples instancias de una misma entidad (varios productos, varios clientes).

4.  **Modularidad y Escalabilidad**: La combinación de estos elementos contribuye a un diseño modular. Al tener clases bien definidas con atributos de tipos claros y métodos que operan sobre ellos, y al usar listas para gestionar colecciones, cada parte del sistema tiene una responsabilidad clara. Esto facilita la adición de nuevas funcionalidades o la modificación de las existentes sin afectar drásticamente otras partes del código, haciendo el sistema más escalable y robusto.

En resumen, estas prácticas no son meras formalidades, sino pilares para construir software de calidad, comprensible y sostenible a largo plazo.
