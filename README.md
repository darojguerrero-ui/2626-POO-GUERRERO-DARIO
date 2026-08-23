Proyecto restaurante_app - Semana 10

Mejora: persistencia de productos en datos/productos.json usando JSON.

Flujo principal:
- main.py crea ArchivoServicio y carga productos al iniciar.
- Productos se reconstruyen como objetos Producto.
- Al registrar/actualizar/eliminar, se guarda el archivo mediante ArchivoServicio.

Manejo de errores implementado: FileNotFoundError, json.JSONDecodeError, PermissionError, KeyError y ValueError (validaciones).