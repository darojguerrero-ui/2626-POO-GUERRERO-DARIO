# Programación Tradicional vs Programación Orientada a Objetos

**Estudiante:** Dario Guerrero  
**Materia:** Programación Orientada a Objetos (POO)  
**Semana:** 3 - Parcial 1  
**Fecha:** Junio 2026

---

## 📋 Descripción de los Programas Desarrollados

Este proyecto presenta dos soluciones equivalentes para un sistema de gestión de mascotas, demostrando las diferencias fundamentales entre dos paradigmas de programación.

### **Programa 1: Programación Tradicional** 📂 `programacion_tradicional/`

**Archivo:** `tradicional.py`

Un programa desarrollado utilizando **variables y funciones**, sin uso de clases ni objetos. Este enfoque sigue el paradigma de programación procedural.

#### ✨ Características:
- **Variables globales**: Lista `mascotas` para almacenar datos
- **Funciones independientes**:
  - `registrar_mascota()`: Captura datos por teclado
  - `mostrar_todas_mascotas()`: Muestra el listado completo
  - `mostrar_mascota_especifica()`: Búsqueda por nombre
  - `buscar_por_tipo()`: Filtrado por especie
  - `mostrar_estadisticas()`: Genera reportes
  - `mostrar_menu()`: Menú principal interactivo

#### 🎯 Datos capturados:
- Nombre, tipo, edad, raza, peso, color y dueño

#### 🚀 Ejecución:
```bash
python tradicional.py
```

---

### **Programa 2: Programación Orientada a Objetos** 📂 `programacion_poo/`

**Archivos:** `main.py` y `mascota.py`

Una solución equivalente desarrollada con **clases y objetos**, demostrando los principios fundamentales de la POO (encapsulación, abstracción, herencia y polimorfismo).

#### ✨ Características:

**Clase `Mascota` (mascota.py):**
- **Atributos:**
  - `nombre`: Identificador único de la mascota
  - `especie`: Tipo de animal (perro, gato, ave, etc.)
  - `edad`: Edad en años

- **Métodos:**
  - `__init__()`: Constructor que inicializa los atributos
  - `mostrar_informacion()`: Presenta datos de forma organizada
  - `hacer_sonido()`: Emite sonidos característicos según la especie
  - `obtener_descripcion()`: Retorna descripción textual
  - `envejecer()`: Incrementa la edad en un año

**Programa Principal (main.py):**
- Crea al menos 3 objetos diferentes de la clase `Mascota`
- Demuestra la creación, manipulación e interacción con objetos
- Ejecuta todos los métodos disponibles

#### 🚀 Ejecución:
```bash
python main.py
```

---

## 🔍 Análisis Comparativo: PT vs POO

### **Programación Tradicional (PT)**

#### ✅ Ventajas:
1. **Simpleza**: Fácil de entender para principiantes
2. **Directa**: Código más literal y procedural
3. **Menos overhead**: Menos abstracción, más directo
4. **Rápida para pequeños proyectos**: Implementación ágil

#### ❌ Desventajas:
1. **Difícil de escalar**: Aumenta la complejidad rápidamente
2. **Bajo nivel de reutilización**: Duplicación de código
3. **Difícil de mantener**: Cambios en estructura afectan todo
4. **Sin encapsulación**: Datos expuestos y vulnerable
5. **Bajo nivel de abstracción**: Detalles de implementación visibles

#### 💾 Estructura de datos:
```python
mascotas = [
    {"nombre": "Max", "especie": "Perro", ...},
    {"nombre": "Whiskers", "especie": "Gato", ...}
]
```

---

### **Programación Orientada a Objetos (POO)**

#### ✅ Ventajas:
1. **Modularidad**: Código organizado en clases reutilizables
2. **Encapsulación**: Datos protegidos dentro de objetos
3. **Escalabilidad**: Fácil de extender con nuevas clases
4. **Mantenibilidad**: Cambios localizados en clases específicas
5. **Reutilización**: Herencia y composición de código
6. **Abstracción**: Interface clara sin detalles internos
7. **Polimorfismo**: Múltiples formas de comportamiento

#### ❌ Desventajas:
1. **Curva de aprendizaje**: Más conceptos que entender
2. **Mayor overhead**: Más recursos iniciales
3. **Complejidad innecesaria**: En proyectos muy pequeños
4. **Overhead de memoria**: Los objetos ocupan más espacio

#### 💾 Estructura de datos:
```python
mascota1 = Mascota("Max", "Perro", 3)
mascota2 = Mascota("Whiskers", "Gato", 2)
```

---

## 📊 Tabla Comparativa

| Aspecto | Programación Tradicional | Programación Orientada a Objetos |
|--------|--------------------------|-----------------------------------|
| **Paradigma** | Procedural | Orientado a Objetos |
| **Unidad básica** | Función | Clase/Objeto |
| **Encapsulación** | No | Sí ✓ |
| **Reutilización** | Baja | Alta ✓ |
| **Escalabilidad** | Limitada | Excelente ✓ |
| **Mantenibilidad** | Difícil | Fácil ✓ |
| **Complejidad inicial** | Baja ✓ | Media |
| **Abstracción** | Baja | Excelente ✓ |
| **Herencia** | No | Sí ✓ |
| **Polimorfismo** | No | Sí ✓ |

---

## 🧠 Reflexión y Conclusiones

### **¿Cuándo usar Programación Tradicional?**
- Scripts simples y únicos
- Tareas de automatización pequeñas
- Prototipos rápidos
- Proyectos con ciclo de vida corto
- Cuando se requiere máximo rendimiento con mínima abstracción

### **¿Cuándo usar Programación Orientada a Objetos?**
- Aplicaciones de mediano a gran tamaño
- Software que requiere mantenimiento a largo plazo
- Proyectos con múltiples desarrolladores
- Cuando se necesita extensibilidad y escalabilidad
- Sistemas complejos con múltiples entidades relacionadas

### **Aprendizaje clave**

El desarrollo de estos dos programas paralelos ha demostrado que:

1. **La POO proporciona una mejor organización**: La clase `Mascota` encapsula toda la lógica relacionada con las mascotas, haciendo el código más coherente.

2. **La reutilización es más efectiva**: En POO, crear nuevas mascotas es tan simple como instanciar la clase. En PT, se debe manipular estructuras de datos manualmente.

3. **La mantenibilidad se mejora significativamente**: Un cambio en la estructura de datos de una mascota en POO afecta solo a la clase, mientras que en PT afecta todas las funciones que la usan.

4. **El polimorfismo facilita la extensión**: El método `hacer_sonido()` puede adaptarse fácilmente a nuevas especies sin modificar el código existente.

5. **La abstracción es fundamental**: PT expone todos los detalles; POO oculta la complejidad tras interfaces sencillas.

### **Conclusión**

Aunque ambos paradigmas pueden resolver el mismo problema, **la Programación Orientada a Objetos ofrece ventajas significativas** para aplicaciones que necesitan crecer, cambiar y mantenerse a lo largo del tiempo. Sin embargo, para problemas simples, PT puede ser más directo y eficiente.

**La elección depende del contexto, el tamaño del proyecto y los requisitos futuros.**

---

## 📁 Estructura del Proyecto

```
SEMANA3/
├── programacion_tradicional/
│   └── tradicional.py
├── programacion_poo/
│   ├── main.py
│   └── mascota.py
└── README.md
```

---

## 👨‍💻 Autor
**Dario Guerrero**  
Estudiante de Programación Orientada a Objetos  
Universidad Estatal de Ambato

---

*Documento generado en Junio de 2026*

