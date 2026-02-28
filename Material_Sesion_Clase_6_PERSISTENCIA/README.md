# Material Sesion de Clase 6 — Persistencia, Login y Roles

**Semana 6 · Unidad 6 · Desarrollo web con Spring Boot II**

## Contenido de esta carpeta

| Archivo | Descripcion |
|---------|-------------|
| `index.html` | Guia interactiva completa: mapa, login, roles, condicional, consultas, graficos, diagramas y quiz |
| `clase.html` | Guia docente con guion sugerido de 120-150 minutos |
| `cheatsheet.html` | Referencia rapida de anotaciones, consultas, roles y errores comunes |
| `ejercicios.html` | 10 ejercicios paso a paso: desde dependencias hasta graficos |
| `entregable_equipo.html` | Formulario de entrega con checklist, rubrica y espacios de reflexion |
| `styles.css` | Estilos compartidos (paleta indigo, cards, hotspots, roles) |

## Aprendizajes esperados

- Implementa persistencia de datos en una base de datos sencilla (H2).
- Desarrolla login con Spring Security y usuarios en memoria.
- Configura roles (ADMIN, USER) y protege rutas.
- Muestra/oculta elementos HTML segun el rol (`sec:authorize`).
- Busca y filtra datos con metodos JPA (`findByTipo`, `findByTituloContainingIgnoreCase`).
- Visualiza datos en graficos con Chart.js.

## Dependencias nuevas (Semana 6)

```xml
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-security</artifactId>
</dependency>
<dependency>
  <groupId>org.thymeleaf.extras</groupId>
  <artifactId>thymeleaf-extras-springsecurity6</artifactId>
</dependency>
```

## Estructura del proyecto (acumulada)

```
src/main/java/.../
  configuracion/
    SeguridadConfig.java          ← NUEVO
  controlador/
    LoginControlador.java         ← NUEVO
    RecursoDidacticoControlador.java
  modelo/
    RecursoDidactico.java
  repositorio/
    RecursoDidacticoRepositorio.java

src/main/resources/
  templates/
    login.html                    ← NUEVO
    recursos/
      lista.html                  (modificado: sec:authorize)
      formulario.html
      estadisticas.html           ← NUEVO
  static/css/
    estilos.css
  application.properties
```

## Usuarios de prueba

| Usuario | Contrasena | Rol | Permisos |
|---------|-----------|-----|----------|
| admin | admin123 | ADMIN | CRUD completo + estadisticas |
| docente | docente123 | USER | Listar + crear |

## Como usar

1. Abrir `index.html` en el navegador para la guia interactiva completa.
2. Seguir los ejercicios en `ejercicios.html` en orden (cada uno construye sobre el anterior).
3. Consultar `cheatsheet.html` como referencia rapida durante la practica.
4. Entregar evidencias en `entregable_equipo.html`.

## Archivos complementarios (raiz del repositorio)

- `PEM en TIC_Sesion de Clase 6 Programacion I.docx` — documento formal de la sesion
- `PEM en TIC_Guia de Aprendizaje 6 Programacion 1.docx` — guia de aprendizaje formal
