# Material — Sesión de Clase 4 (CRUD inicial + H2 persistente + Thymeleaf + Bootstrap)

Abrir `index.html` en el navegador.

## Objetivo
Construir el **inicio real de un CRUD** en Spring Boot (con pantallas) usando el stack:

- **Base de datos:** H2 en **modo archivo** (persistente) para que “se sienta” como SQLite.
- **Backend:** Spring Boot + Spring MVC + Spring Data JPA.
- **Frontend (vistas):** Thymeleaf + Bootstrap (UI pulida, rápida y didáctica).

## Resultado visible (meta)
Al final de la sesión, el equipo debe poder:

- Ver un **listado** (Read)
- Crear un registro desde un **formulario** (Create)
- Editar (Update) y eliminar (Delete) de forma básica
- Abrir **H2 Console** y comprobar que los datos se guardan en archivo

## Archivos
- `index.html`: portada y navegación
- `preparar_pc.html`: configuración del proyecto (dependencias + `application.properties` + H2 Console)
- `clase.html`: guía para impartir la sesión (docente)
- `ejercicios.html`: práctica guiada (CRUD inicial)
- `cheatsheet.html`: comandos + estructura + troubleshooting
- `entregable_equipo.html`: plantilla de evidencias del equipo
- `styles.css`: estilos del material
- `plantillas_thymeleaf/`: plantillas ejemplo (para copiar al proyecto Spring)

> Nota: El material está diseñado para funcionar offline salvo por librerías CSS/JS cargadas por CDN (Bootstrap).
