# Portal de Materiales (frontend)

Abre el archivo [index.html](index.html) en la raíz para navegar por carpetas de materiales y documentos.

## Recomendación

- Para una navegación más estable (y evitar restricciones del navegador al abrir archivos locales), abre el portal con un servidor local.
- En VS Code, la opción más fácil es la extensión **Live Server** y luego “Open with Live Server” sobre `index.html`.

## Cómo agregar nuevos materiales

1. Crea una carpeta nueva en la raíz (ej.: `Material_Sesion_Clase_3_X/`).
2. Asegura que tenga un `index.html` como entrada.
3. Duplica una tarjeta en `index.html` y ajusta:
   - `data-title`
   - `data-tags`
   - enlaces (`href`)

## Nota sobre enlaces con espacios

En `index.html` los enlaces a archivos con espacios van con URL-encoding (por ejemplo `Formato%20programa%20de%20curso.md`).
