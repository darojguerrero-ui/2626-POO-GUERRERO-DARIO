# Sistema de Restaurante - Programación Orientada a Objetos (POO) - Semana 7

## Información del Estudiante
**Nombre:** Dario Javier Guerrero Palma  
**Actividad:** Actividad Evaluable - Semana 7  
**Tema:** Constructores, Decoradores, Propiedades, Setters, Dataclasses y Arquitectura por Capas en Python

---

## Descripción del Sistema

El sistema **restaurante_app** (versión Semana 7) es una aplicación avanzada en Python que implementa conceptos intermedios de Programación Orientada a Objetos. El sistema permite gestionar productos y clientes de un restaurante mediante una interfaz de menú interactivo ejecutada desde consola.

El objetivo es evidenciar:
- **Constructores tradicionales** con parámetros y validación
- **Decoradores @property y @setter** para control de atributos
- **Decorador @dataclass** para simplificar la creación de clases
- **Arquitectura por capas** (modelos, servicios, interfaz)
- **Validación de datos** en setters
- **Menú interactivo** que demuestra el ciclo completo: input → constructor → objeto → almacenamiento → consulta

---

## Estructura del Proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py           # Inicializador del módulo
│   ├── producto.py           # Clase Producto con @property y @setter
│   └── cliente.py            # Clase Cliente con @dataclass
├── servicios/
│   ├── __init__.py           # Inicializador del módulo
│   └── restaurante.py        # Clase Restaurante (lógica de negocio)
└── main.py                   # Interfaz interactiva (punto de entrada)
```

---

## Componentes Principales

### 1. Clase `Producto` (modelos/producto.py)

**Características:**
- Constructor tradicional `__init__()` con parámetros
- Atributos privados: `__nombre`, `__categoria`, `__precio`, `__disponible`
- Decoradores `@property` para acceso controlado
- Decoradores `@setter` con validaciones

**Validaciones implementadas:**
- Nombre no vacío
- Categoría no vacía
- Precio mayor a cero
- Disponibilidad como booleano

**Métodos:**
```python
# Acceso a atributos mediante @property
producto.nombre
producto.categoria
producto.precio
producto.disponible

# Modificación mediante @setter (con validación)
producto.nombre = "Nuevo nombre"
producto.precio = 25.50

# Método para mostrar información
producto.mostrar_informacion()
```

### 2. Clase `Cliente` (modelos/cliente.py)

**Características:**
- Decorador `@dataclass` que genera automáticamente:
  - Constructor `__init__()`
  - Método `__repr__()`
  - Método `__eq__()`
  - Otros métodos útiles

**Atributos:**
- `id_cliente` (int): Identificador único
- `nombre` (str): Nombre del cliente
- `correo` (str): Correo electrónico

**Ventajas del @dataclass:**
- Código más limpio y conciso
- Menos código repetitivo
- Funcionalidad automática completa

```python
# Crear cliente (el @dataclass genera todo automáticamente)
cliente = Cliente(id_cliente=1, nombre="Juan", correo="juan@email.com")
cliente.mostrar_informacion()
```

### 3. Clase `Restaurante` (servicios/restaurante.py)

**Responsabilidad:** Administrar listas de productos y clientes

**Métodos para Productos:**
- `registrar_producto(producto)` - Agregar nuevo producto
- `listar_productos()` - Obtener lista completa
- `buscar_producto(nombre)` - Búsqueda parcial
- `obtener_producto_por_nombre_exacto(nombre)` - Búsqueda exacta
- `eliminar_producto(nombre)` - Remover producto
- `obtener_cantidad_productos()` - Contar productos

**Métodos para Clientes:**
- `registrar_cliente(cliente)` - Agregar nuevo cliente
- `listar_clientes()` - Obtener lista completa
- `buscar_cliente(nombre)` - Búsqueda parcial
- `obtener_cliente_por_id(id)` - Búsqueda por ID
- `obtener_cliente_por_nombre_exacto(nombre)` - Búsqueda exacta
- `eliminar_cliente(id)` - Remover cliente
- `obtener_cantidad_clientes()` - Contar clientes

### 4. Menú Interactivo (main.py)

**Flujo del Sistema:**

```
Usuario selecciona opción
        ↓
input() solicita datos
        ↓
Constructor del modelo crea objeto
        ↓
Objeto se registra en Restaurante
        ↓
Datos se consultan/buscan/listan
```

**Opciones del menú:**

```
========================================
        SISTEMA DE RESTAURANTE
========================================
1. Registrar producto
2. Listar productos
3. Buscar producto
----------------------------------------
4. Registrar cliente
5. Listar clientes
6. Buscar cliente
----------------------------------------
7. Salir
========================================
```

---

## Cómo Ejecutar el Programa

### Requisitos
- Python 3.7 o superior
- No requiere librerías externas (usa @dataclass de la librería estándar)

### Ejecución

1. Navega a la carpeta del proyecto:
```bash
cd restaurante_app
```

2. Ejecuta el programa principal:
```bash
python main.py
```

3. Sigue las instrucciones del menú interactivo

---

## Ejemplos de Uso

### Registrar un Producto

```
Seleccione una opción: 1

--- REGISTRAR PRODUCTO ---
Nombre del producto: Pasta Carbonara
Categoría (ej: Comida, Bebida, Postre): Comida
Precio: $15.99
✓ Producto 'Pasta Carbonara' registrado exitosamente.
```

### Listar Productos

```
Seleccione una opción: 2

--- LISTAR PRODUCTOS ---
Total de productos: 2

1. Producto: Pasta Carbonara
  Categoría: Comida
  Precio: $15.99
  Estado: Disponible
----------------------------------------
2. Producto: Jugo de Naranja
  Categoría: Bebida
  Precio: $4.50
  Estado: Disponible
----------------------------------------
```

### Buscar Producto

```
Seleccione una opción: 3

--- BUSCAR PRODUCTO ---
Ingrese el nombre del producto a buscar: Pasta

Resultados encontrados: 1

1. Producto: Pasta Carbonara
  Categoría: Comida
  Precio: $15.99
  Estado: Disponible
----------------------------------------
```

### Registrar un Cliente

```
Seleccione una opción: 4

--- REGISTRAR CLIENTE ---
ID del cliente (número): 1
Nombre del cliente: Juan Pérez
Correo electrónico: juan@email.com
✓ Cliente 'Juan Pérez' registrado exitosamente.
```

### Listar Clientes

```
Seleccione una opción: 5

--- LISTAR CLIENTES ---
Total de clientes: 1

1. Cliente ID: 1
  Nombre: Juan Pérez
  Correo: juan@email.com
----------------------------------------
```

---

## Conceptos Clave Implementados

### 1. **Constructor Tradicional (`__init__`)**

Utilizado en la clase `Producto` para inicializar objetos con validación:

```python
def __init__(self, nombre, categoria, precio, disponible=True):
    self.__nombre = nombre
    self.__categoria = categoria
    self.__precio = precio
    self.__disponible = disponible
```

### 2. **Decorador @property**

Permite acceso controlado a atributos privados:

```python
@property
def nombre(self):
    return self.__nombre
```

### 3. **Decorador @setter**

Permite modificación con validaciones:

```python
@nombre.setter
def nombre(self, valor):
    if not valor or not valor.strip():
        raise ValueError("El nombre del producto no puede estar vacío.")
    self.__nombre = valor.strip()
```

### 4. **Decorador @dataclass**

Simplifica la creación de clases con atributos:

```python
@dataclass
class Cliente:
    id_cliente: int
    nombre: str
    correo: str
```

Genera automáticamente:
- Constructor `__init__()` con parámetros para cada atributo
- Método `__repr__()` para representación legible
- Método `__eq__()` para comparación
- Método `__hash__()` opcional

### 5. **Arquitectura por Capas**

```
┌─────────────────────────────────────┐
│   main.py (Interfaz de Usuario)    │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│ servicios/restaurante.py (Lógica)  │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│  modelos/ (Entidades del Negocio)  │
└─────────────────────────────────────┘
```

---

## Validaciones Implementadas

### En Producto (mediante @setter):

1. **Nombre:**
   - ✓ No puede estar vacío
   - ✓ Se elimina espacios en blanco

2. **Categoría:**
   - ✓ No puede estar vacía
   - ✓ Se elimina espacios en blanco

3. **Precio:**
   - ✓ Debe ser numérico
   - ✓ Debe ser mayor que cero
   - ✓ Manejo de errores de tipo

4. **Disponibilidad:**
   - ✓ Se convierte automáticamente a booleano

### En Cliente (mediante @dataclass):

- Los atributos son inmutables después de la creación
- Se puede usar `@dataclass(frozen=True)` para mayor control

### En Restaurante:

- Se evita registrar productos/clientes duplicados
- Se valida que IDs de clientes sean únicos
- Se proporciona feedback al usuario

---

## Flujo Completo del Sistema

### Ciclo de Vida de un Objeto

```
1. Usuario selecciona opción "Registrar producto"
   ↓
2. Sistema solicita: nombre, categoría, precio
   ↓
3. Usuario ingresa datos mediante input()
   ↓
4. Constructor Producto.__init__() crea objeto
   ↓
5. Setters validan automáticamente los datos
   ↓
6. Objeto se almacena en restaurante.productos
   ↓
7. Usuario puede listar o buscar el producto
   ↓
8. Métodos de Restaurante consultan la lista
```

---

## Diferencias entre Semana 6 y Semana 7

| Aspecto | Semana 6 | Semana 7 |
|--------|----------|----------|
| Constructores | Solo heredancia con super() | Tradicionales con parámetros |
| Control de atributos | Encapsulación básica | @property y @setter |
| Clases de datos | Clases tradicionales | @dataclass |
| Interacción | Demostración de POO | Menú interactivo |
| Entrada de datos | Precargada en código | input() del usuario |
| Ciclo de vida | Mostrar información | Crear → Almacenar → Consultar |

---

## Requisitos Cumplidos

✅ Estructura modular con carpetas (modelos, servicios)  
✅ Clase Producto con constructor `__init__()`  
✅ Decoradores `@property` y `@setter` en Producto  
✅ Validaciones en setters (nombre, categoría, precio)  
✅ Clase Cliente con `@dataclass`  
✅ Clase Restaurante con métodos CRUD  
✅ Menú interactivo con 7 opciones  
✅ Entrada de datos mediante `input()`  
✅ Objetos creados dinámicamente en runtime  
✅ Almacenamiento en listas  
✅ Búsqueda y listado de registros  
✅ Comentarios explicativos  
✅ Convenciones de nombres Python  
✅ README.md con documentación completa  

---

## Reflexión: Importancia de Estos Conceptos

### @property y @setter

Permiten:
- **Encapsulación transparente:** Acceso a atributos como si fueran públicos pero con control
- **Validación automática:** Cada modificación pasa por lógica de validación
- **Evolución sin romper interfaz:** Cambiar implementación sin afectar código cliente

### @dataclass

Proporciona:
- **Código limpio:** Menos boilerplate
- **Menos errores:** Generación automática de métodos
- **Mejor legibilidad:** Enfoque en el dominio del negocio

### Arquitectura por Capas

Facilita:
- **Separación de responsabilidades:** Cada capa tiene un propósito claro
- **Mantenibilidad:** Cambios en una capa no afectan otras
- **Testabilidad:** Cada componente se puede probar independientemente
- **Escalabilidad:** Fácil agregar funcionalidad

---

## Conclusión

Este proyecto demuestra cómo los conceptos intermedios de POO en Python —constructores, decoradores, propiedades, dataclasses y arquitectura por capas— se combinan para crear un sistema modular, mantenible y profesional. La estructura permite que futuros desarrolladores comprendan fácilmente el código y agreguen nuevas funcionalidades sin afectar el sistema existente.

---

**Autor:** Dario Javier Guerrero Palma  
**Fecha:** 2026  
**Lenguaje:** Python 3.7+  
**Tema:** Programación Orientada a Objetos - Arquitectura por Capas
