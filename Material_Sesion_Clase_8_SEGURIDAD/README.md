# Material Sesión de Clase 8 — Seguridad, QA y Mantenimiento

Material de apoyo para la **Sesión 8** del curso *Introducción al Desarrollo Web con Java* (PEM en TIC, Universidad Rafael Landívar).

## Tema
**Seguridad básica con Spring Security, getters/setters calculados, QA manual y redeploy seguro.**

## Archivos incluidos

| Archivo | Descripción |
|---------|-------------|
| `index.html` | Guía interactiva principal con secciones de seguridad, campos calculados, QA, redeploy, diagramas, quiz y checklist. |
| `clase.html` | Guía docente con guión sugerido (120–150 min) en formato acordeón (7 secciones). |
| `ejercicios.html` | 10 ejercicios paso a paso + 1 bonus (sec:authorize). |
| `cheatsheet.html` | Resumen rápido: anotaciones, código, errores comunes y checklist de QA. |
| `entregable_equipo.html` | Formulario de entrega por equipo con checklist, rúbrica y campos de evidencia. |
| `styles.css` | Estilos personalizados (paleta índigo/azul). |
| `README.md` | Este archivo. |

## Temas cubiertos

1. **Seguridad básica con Spring Security**
   - Dependencia `spring-boot-starter-security`
   - `SecurityConfig.java` con `SecurityFilterChain`
   - Roles (USER, ADMIN) con `InMemoryUserDetailsManager`
   - BCrypt para contraseñas
   - Login/logout personalizados con Thymeleaf
   - `sec:authorize` para contenido condicional

2. **Getters y Setters con campos calculados**
   - Getter calculado con `@Transient` (no se guarda en BD)
   - Ejemplos: `getTotal()`, `getEdad()`, `getEstado()`
   - Setter con transformación: `trim()`, `toUpperCase()`, `replaceAll()`
   - Cuándo usar cada técnica

3. **QA y Testing manual**
   - Checklist de 8+ puntos antes de deploy
   - Errores comunes de seguridad y soluciones
   - Buenas prácticas de mantenimiento

4. **Redeploy seguro**
   - Ciclo: cambiar → probar → commit → push → verificar
   - Zero-downtime deploy en Render
   - Rollback en caso de fallo

## Pre-requisitos del estudiante

- App Spring Boot funcional con CRUD (Semanas 4-6)
- Deploy existente en Render con Docker (Semana 7)
- Git configurado y funcional

## Cómo usar

1. Abrir `index.html` en un navegador.
2. Navegar por las secciones con los botones del hero.
3. Usar el quiz interactivo para autoevaluación.
4. Seguir los ejercicios en `ejercicios.html` paso a paso.
5. Completar el entregable en `entregable_equipo.html`.

## Paleta de colores

- Acento: `#6366f1` (índigo)
- Acento oscuro: `#4f46e5`
- Fondo hero: gradiente púrpura-índigo
