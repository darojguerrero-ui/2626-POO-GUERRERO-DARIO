Nombre: Dario Guerrero

Descripción:
Proyecto restaurante_app para la administración básica de productos y usuarios desde consola.

Estructura del proyecto:
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py    # clase Producto (codigo, nombre, categoria, precio)
│   └── usuario.py     # clase Usuario (identificacion, nombre, correo, celular)
├── servicios/
│   ├── __init__.py
│   └── restaurante.py # clase Restaurante (administra listas de productos y usuarios)
└── main.py            # punto de entrada con menú interactivo

Uso de estructuras de datos:
- list: se utilizan en Restaurante para almacenar dinámicamente la colección de productos y la de usuarios.
- tuple: MENU_OPTIONS en Restaurante representa las opciones del menú que no cambian durante la ejecución.
- dict: MENU_MAP en Restaurante y el diccionario 'acciones' en main.py asocian números de opción con descripciones o funciones (clave->valor).
- set: categorias_unicas() devuelve un conjunto con las categorías de productos sin duplicados.

Ejecución:
Desde la carpeta restaurante_app ejecutar:
python main.py

Reflexión:
Seleccionar la estructura de datos adecuada facilita operaciones eficientes: listas para colecciones ordenadas y modificables; tuplas para datos constantes; diccionarios para búsquedas por clave; conjuntos para obtener elementos únicos.
