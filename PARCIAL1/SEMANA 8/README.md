# Sistema de Gestión de Restaurante (Semana 8)

## Estudiante
Dario Javier Guerrero Palma

## Descripción del Sistema
Este proyecto desarrolla una versión mejorada de un sistema de gestión para un restaurante, aplicando los principios de la Programación Orientada a Objetos (POO) en Python. El sistema permite registrar y listar productos (incluyendo bebidas como un tipo especializado de producto) y clientes a través de un menú interactivo ejecutado desde la consola.

El objetivo principal es demostrar una correcta distribución de responsabilidades entre las clases, la aplicación de herencia para extender funcionalidades (clase `Bebida` heredando de `Producto`), y el uso de polimorfismo para manejar objetos de diferentes tipos de manera uniforme. Se busca evidenciar cómo un diseño modular y la aplicación de principios SOLID contribuyen a un código más organizado, mantenible y escalable.

## Estructura del Proyecto
El proyecto sigue una estructura modular para organizar el código de manera lógica y separar las responsabilidades.

```
.
├── restaurante_app/
│   ├── modelos/
│   │   ├── __init__.py
│   │   ├── producto.py       # Clase base para todos los productos
│   │   ├── bebida.py         # Clase hija de Producto para bebidas
│   │   └── cliente.py        # Clase para representar clientes
│   ├── servicios/
│   │   ├── __init__.py
│   │   └── restaurante.py    # Clase de servicio para la gestión centralizada
│   └── main.py               # Punto de entrada del programa y menú interactivo
└── README.md                 # Documentación del proyecto
```

## Responsabilidad de Cada Clase

*   **`modelos/producto.py` (Clase `Producto`)**:
    *   **Responsabilidad**: Representar los datos comunes de cualquier producto ofrecido en el restaurante (código, nombre, categoría, precio). Actúa como la clase base para otros tipos de productos.
    *   **Métodos clave**: `__init__` (constructor), `mostrar_informacion()` (método abstracto para mostrar detalles).

*   **`modelos/bebida.py` (Clase `Bebida`)**:
    *   **Responsabilidad**: Representar una especialización de `Producto`, incorporando atributos específicos de una bebida (tamaño, tipo de envase). Hereda de `Producto`.
    *   **Métodos clave**: `__init__` (constructor que llama al de la clase base), `mostrar_informacion()` (sobrescrito para incluir detalles de bebida).

*   **`modelos/cliente.py` (Clase `Cliente`)**:
    *   **Responsabilidad**: Representar la información de un cliente registrado en el sistema (identificación, nombre, correo).
    *   **Métodos clave**: `__init__` (constructor), `mostrar_informacion()` (para mostrar detalles del cliente).

*   **`servicios/restaurante.py` (Clase `Restaurante`)**:
    *   **Responsabilidad**: Actuar como el servicio principal del sistema, gestionando las colecciones de productos y clientes. Se encarga de la lógica de negocio como registrar, validar y listar.
    *   **Métodos clave**: `__init__`, `registrar_producto()`, `listar_productos()`, `registrar_cliente()`, `listar_clientes()`.

*   **`main.py`**:
    *   **Responsabilidad**: Ser el punto de arranque del programa. Gestiona la interacción con el usuario a través de un menú de consola, solicita datos, crea objetos y delega las operaciones de negocio a la clase `Restaurante`. No contiene lógica de gestión de colecciones.

## Relación entre `Producto` y `Bebida`
La clase `Bebida` hereda de la clase `Producto`. Esto significa que una `Bebida` "es un" `Producto`, extendiendo sus características con atributos específicos como `tamaño` y `tipo_envase`. Esta relación de herencia permite que los objetos `Bebida` puedan ser tratados como objetos `Producto` en contextos generales (como en la lista de productos del `Restaurante`), pero también pueden mostrar su información específica cuando se invoca su método `mostrar_informacion()` sobrescrito. Esta es una aplicación clave del polimorfismo y el Principio de Sustitución de Liskov.

## Principios SOLID Aplicados

*   **S - Principio de Responsabilidad Única (SRP)**:
    *   Cada clase tiene una única razón para cambiar. `Producto` y `Bebida` se encargan de sus propios datos y cómo se muestran. `Cliente` gestiona sus propios datos. `Restaurante` se encarga exclusivamente de la gestión de colecciones y la lógica de negocio (registro, validación, listado). `main.py` se enfoca solo en la interacción con el usuario y la orquestación.

*   **O - Principio Abierto/Cerrado (OCP)**:
    *   El sistema está abierto a la extensión pero cerrado a la modificación. La incorporación de `Bebida` como un nuevo tipo de producto no requirió modificar la clase `Restaurante` ni su método `registrar_producto`. `Restaurante` puede manejar `Bebida`s porque estas se comportan como `Producto`s, extendiendo el sistema sin alterar el código existente.

*   **L - Principio de Sustitución de Liskov (LSP)**:
    *   Los objetos de una superclase (`Producto`) pueden ser reemplazados por objetos de sus subclases (`Bebida`) sin alterar la corrección del programa. El método `listar_productos()` en la clase `Restaurante` invoca `mostrar_informacion()` en cada objeto de su lista de productos. Tanto `Producto` como `Bebida` implementan este método, y el sistema funciona correctamente sin necesidad de verificar el tipo específico de cada objeto.

## Instrucciones de Ejecución

Para ejecutar el sistema:

1.  Asegúrate de tener Python instalado (versión 3.x recomendada).
2.  Navega hasta el directorio `restaurante_app` en tu terminal.
    ```bash
    cd SEMANA 8/restaurante_app
    ```
3.  Ejecuta el archivo `main.py`:
    ```bash
    python main.py
    ```
4.  Sigue las instrucciones del menú interactivo en la consola.

## Reflexión sobre la Importancia de Diseñar Proyectos Mantenibles
Diseñar proyectos mantenibles es crucial para el éxito a largo plazo de cualquier software. Un código bien estructurado, que sigue principios como SOLID, facilita enormemente la lectura, comprensión, depuración y modificación.

La aplicación de identificadores descriptivos, tipos de datos adecuados y una clara separación de responsabilidades (SRP) reduce la complejidad cognitiva y el riesgo de errores. La capacidad de extender el sistema con nuevas funcionalidades sin alterar el código existente (OCP) y la garantía de que las subclases se comportarán como sus superclases (LSP) hacen que el software sea más robusto y menos propenso a introducir fallos al evolucionar.

En un entorno de desarrollo colaborativo, la mantenibilidad es aún más vital, ya que permite que múltiples desarrolladores trabajen en el mismo proyecto de manera eficiente, integrando sus cambios con menos conflictos y mayor confianza. En última instancia, un diseño mantenible se traduce en un menor costo de desarrollo y una mayor vida útil del software.
