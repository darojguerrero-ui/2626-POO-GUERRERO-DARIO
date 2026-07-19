# Sistema de Restaurante - Programación Orientada a Objetos (POO)

## Información del Estudiante
**Nombre:** Dario Javier Guerrero Palma  
**Actividad:** Actividad Evaluable - Semana 6  
**Tema:** Implementación de Herencia, Encapsulación y Polimorfismo en Python

---

## Descripción del Sistema

El sistema **restaurante_app** es una aplicación desarrollada en Python que implementa principios fundamentales de la Programación Orientada a Objetos (POO). El sistema gestiona productos disponibles en un restaurante, permitiendo administrar platillos y bebidas con sus respectivas características y precios.

El objetivo es demostrar cómo los principios de **herencia**, **encapsulación** y **polimorfismo** pueden ser aplicados efectivamente en un proyecto modular y escalable.

---

## Estructura del Proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py           # Inicializador del módulo
│   ├── producto.py           # Clase padre Producto
│   ├── platillo.py           # Clase Platillo (hereda de Producto)
│   └── bebida.py             # Clase Bebida (hereda de Producto)
├── servicios/
│   ├── __init__.py           # Inicializador del módulo
│   └── restaurante.py        # Clase Restaurante (servicio)
└── main.py                   # Punto de entrada del programa
```

---

## Relación de Herencia Implementada

```
                    Producto (Clase Padre)
                   /            \
                  /              \
            Platillo          Bebida
           (Clase Hija)    (Clase Hija)
```

### Descripción:

- **Producto**: Clase padre que define los atributos comunes: `nombre`, `__precio` (privado) y `disponibilidad`.
- **Platillo**: Hereda de Producto y agrega atributos específicos: `calorias` y `tiempo_preparacion`.
- **Bebida**: Hereda de Producto y agrega atributos específicos: `volumen_ml` y `tipo_bebida`.

---

## Principios de POO Implementados

### 1. **Herencia**

Las clases `Platillo` y `Bebida` heredan de la clase `Producto` utilizando el mecanismo de herencia de Python:

```python
class Platillo(Producto):
    def __init__(self, nombre, precio, calorias, tiempo_preparacion, disponibilidad=True):
        super().__init__(nombre, precio, disponibilidad)
        self.calorias = calorias
        self.tiempo_preparacion = tiempo_preparacion
```

El uso de `super()` permite reutilizar la lógica de inicialización de la clase padre, evitando duplicación de código.

### 2. **Encapsulación**

El atributo `__precio` en la clase `Producto` es privado (encapsulado) y solo puede ser accedido y modificado a través de métodos específicos:

```python
def obtener_precio(self):
    """Acceso al precio encapsulado"""
    return self.__precio

def cambiar_precio(self, nuevo_precio):
    """Modificación del precio con validación"""
    if nuevo_precio <= 0:
        raise ValueError("El precio debe ser mayor a cero.")
    self.__precio = nuevo_precio
```

Este enfoque protege la integridad de los datos y permite validar cambios antes de aplicarlos.

### 3. **Polimorfismo**

El método `mostrar_informacion()` es sobrescrito en las clases hijas para mostrar información específica según el tipo de producto:

**En Producto (clase padre):**
```python
def mostrar_informacion(self):
    estado = "Disponible" if self.disponibilidad else "No disponible"
    return f"Nombre: {self.nombre} | Precio: ${self.__precio:.2f} | Estado: {estado}"
```

**En Platillo:**
```python
def mostrar_informacion(self):
    # Muestra información específica del platillo
    return f"🍽️  PLATILLO: {self.nombre}\n   Precio: ${self.obtener_precio():.2f}\n..."
```

**En Bebida:**
```python
def mostrar_informacion(self):
    # Muestra información específica de la bebida
    return f"🥤 BEBIDA: {self.nombre}\n   Precio: ${self.obtener_precio():.2f}\n..."
```

**Uso polimórfico en Restaurante:**
```python
for producto in self.productos:
    print(producto.mostrar_informacion())  # Se ejecuta según el tipo específico
```

---

## Componentes Principales

### Clase `Producto`
- **Responsabilidad**: Define los atributos comunes y la interfaz base para todos los productos.
- **Atributos**:
  - `nombre`: Nombre del producto
  - `__precio`: Precio (privado/encapsulado)
  - `disponibilidad`: Estado de disponibilidad
- **Métodos**: `obtener_precio()`, `cambiar_precio()`, `cambiar_disponibilidad()`, `mostrar_informacion()`

### Clase `Platillo`
- **Responsabilidad**: Representa un platillo específico del restaurante.
- **Atributos adicionales**:
  - `calorias`: Cantidad de calorías
  - `tiempo_preparacion`: Tiempo en minutos
- **Método sobrescrito**: `mostrar_informacion()` personalizado para platillos

### Clase `Bebida`
- **Responsabilidad**: Representa una bebida específica del restaurante.
- **Atributos adicionales**:
  - `volumen_ml`: Volumen en mililitros
  - `tipo_bebida`: Tipo de bebida (fría, caliente, etc.)
- **Método sobrescrito**: `mostrar_informacion()` personalizado para bebidas

### Clase `Restaurante`
- **Responsabilidad**: Administra la lista de productos y proporciona servicios.
- **Métodos principales**:
  - `agregar_producto()`: Añade un producto al restaurante
  - `eliminar_producto()`: Elimina un producto
  - `obtener_producto_por_nombre()`: Busca un producto
  - `mostrar_menu()`: Muestra todos los productos (demuestra polimorfismo)
  - `obtener_productos_disponibles()`: Retorna productos disponibles

---

## Cómo Ejecutar el Programa

### Requisitos
- Python 3.7 o superior
- No requiere librerías externas

### Ejecución

1. Navega a la carpeta del proyecto:
```bash
cd restaurante_app
```

2. Ejecuta el programa principal:
```bash
python main.py
```

### Salida Esperada
El programa mostrará:
- Un menú formateado con todos los productos
- Información específica de platillos (calorías, tiempo de preparación)
- Información específica de bebidas (volumen, tipo)
- Demostraciones de encapsulación (acceso y modificación de precio con validación)
- Manejo de errores cuando se intenta establecer precios inválidos
- Cambios en disponibilidad de productos

---

## Reflexión sobre la Importancia de POO en Python

La aplicación de principios de Programación Orientada a Objetos es fundamental en el desarrollo de software moderno por las siguientes razones:

### **Mantenibilidad**
La estructura modular y las clases bien definidas hacen que el código sea más fácil de entender y mantener. Cambios futuros se pueden realizar en lugares específicos sin afectar al resto del sistema.

### **Reutilización de Código**
La herencia permite compartir funcionalidad común entre clases, evitando duplicación de código. En este proyecto, `Platillo` y `Bebida` reutilizan los métodos y atributos de `Producto`.

### **Encapsulación y Seguridad**
Al proteger atributos como `__precio` con métodos de acceso, garantizamos que solo se realicen operaciones válidas. Las validaciones garantizan la integridad de los datos.

### **Escalabilidad**
El diseño modular permite añadir nuevas clases (ej: `Postre`, `Entrada`) sin modificar el código existente. Simplemente heredarían de `Producto`.

### **Polimorfismo**
La capacidad de los objetos de diferentes tipos para responder al mismo mensaje (`mostrar_informacion()`) proporciona flexibilidad y extensibilidad. El código del `Restaurante` no necesita conocer los tipos específicos de productos.

### **Facilita el Trabajo en Equipo**
Un proyecto bien estructurado con separación de responsabilidades permite que múltiples desarrolladores trabajen en paralelo sin conflictos.

---

## Consideraciones de Diseño

1. **Atributos Privados**: El `__precio` es privado para evitar cambios no validados.
2. **Uso de `super()`**: Permite reutilizar la lógica del constructor padre.
3. **Métodos Descriptivos**: Los nombres de métodos y atributos son claros y descriptivos.
4. **Validación de Datos**: Se valida que los precios sean positivos.
5. **Separación de Responsabilidades**: Cada clase tiene una responsabilidad clara y única.

---

## Ejemplo de Uso

```python
# Crear productos
platillo = Platillo("Pasta", 12.50, 720, 20)
bebida = Bebida("Café", 3.00, 100, "Caliente")

# Crear restaurante y agregar productos
restaurante = Restaurante("Mi Restaurante")
restaurante.agregar_producto(platillo)
restaurante.agregar_producto(bebida)

# Mostrar menú (polimorfismo en acción)
restaurante.mostrar_menu()

# Acceder al precio encapsulado
print(platillo.obtener_precio())  # 12.5

# Modificar precio con validación
platillo.cambiar_precio(13.00)  # ✓ Éxito
platillo.cambiar_precio(-5.00)  # ✗ Error: precio debe ser mayor a cero
```

---

## Conclusión

Este proyecto demuestra de manera práctica cómo los principios fundamentales de la Programación Orientada a Objetos —herencia, encapsulación y polimorfismo— pueden ser aplicados para crear un sistema modular, mantenible y escalable. El uso correcto de estas técnicas es esencial para el desarrollo de aplicaciones profesionales en Python.

---

**Autor:** Dario Javier Guerrero Palma  
**Fecha:** 2026  
**Lenguaje:** Python 3.7+
