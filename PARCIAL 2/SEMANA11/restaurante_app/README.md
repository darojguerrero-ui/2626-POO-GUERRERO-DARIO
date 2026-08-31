Autor: Dario Guerrero
# Proyecto restaurante_app - Semana 11

## Objetivo
Esta versión evoluciona la aplicación anterior para incluir usuarios, ventas y persistencia completa con JSON. El sistema conserva la administración de productos y agrega la relación principal entre usuario y producto mediante ventas.

## Estructura principal
- `modelos/producto.py`: representa un producto con código, nombre, precio y stock.
- `modelos/usuario.py`: representa un usuario registrado.
- `modelos/venta.py`: guarda la relación usuario + producto + cantidad vendida.
- `servicios/restaurante.py`: centraliza toda la lógica de negocio.
- `servicios/archivo_servicio.py`: carga y guarda productos, usuarios y ventas desde JSON.
- `main.py`: coordina el menú interactivo con `input()` para usuario y consola.
- `datos/*.json`: archivos de persistencia para cada colección.

## Funcionalidades
- Registro, listado, actualización y eliminación de productos.
- Registro y listado de usuarios.
- Validación de stock antes de vender.
- Registro de ventas en una colección de objetos `Venta`.
- Consulta de ventas por usuario y recorrido de la colección.
- Persistencia de productos, usuarios y ventas en archivos JSON.
- Recuperación automática de la información al iniciar la aplicación.

## Persistencia
La aplicación guarda los cambios tras cada operación que modifica los datos:
- productos -> `datos/productos.json`
- usuarios -> `datos/usuarios.json`
- ventas -> `datos/ventas.json`

El archivo `ArchivoServicio` usa `json.load()`, `json.dump()`, `with open(..., encoding="utf-8")` para leer y escribir los registros.

## Reglas de negocio
- Un usuario debe existir antes de vender.
- Un producto debe existir antes de vender.
- La cantidad solicitada debe ser mayor que cero.
- El stock no puede quedar en valores negativos.
- Si la venta supera el stock disponible, la operación se rechaza.

## Ejecución
1. Ubicarse en la carpeta del proyecto.
2. Ejecutar:
   `python main.py`
3. Usar el menú para registrar productos, usuarios y ventas.

## Manejo de errores
Se controla la lectura y escritura de archivos gestionando excepciones de tipo:
- `FileNotFoundError`
- `json.JSONDecodeError`
- `PermissionError`
- `KeyError`
- `ValueError`

## Verificación funcional
Se debe comprobar que:
- al vender un producto, el stock disminuye;
- la venta queda registrada en `ventas.json`;
- la consulta por usuario devuelve solo sus ventas;
- tras cerrar y volver a abrir el programa, los datos recuperados siguen disponibles.