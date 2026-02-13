# Plantillas Thymeleaf (para copiar al proyecto)

Estas plantillas están pensadas para que el CRUD se vea **pulido** sin perder lo didáctico.

## Dónde copiarlas
En tu proyecto Spring Boot:

- `src/main/resources/templates/recursos/list.html`
- `src/main/resources/templates/recursos/form.html`
- `src/main/resources/static/css/app.css`

> Tip: crea la carpeta `templates/recursos/` antes de pegar los archivos.

## Requisitos
- Dependencia: **Thymeleaf**
- Dependencia: **Spring Web**
- Controlador que retorne vistas:
  - `return "recursos/list";`
  - `return "recursos/form";`

## Convención de nombres (para que funcione “a la primera”)
- En el listado, el modelo usa: `resources` (lista)
- En el formulario, el modelo usa: `resource` (objeto)

## Nota
- Bootstrap se carga por CDN.
- El botón “Eliminar” usa `<form method="post">` para evitar borrar por GET.
