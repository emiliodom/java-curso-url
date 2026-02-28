# Material Sesión de Clase 7 — Despliegue (Deploy) en Render

## Semana 7 · Unidad 7 — Despliegue de la aplicación web

**Tema central:** Publicar la aplicación Spring Boot en internet usando Render (plan gratuito).

---

## Archivos en esta carpeta

| Archivo | Descripción |
|---|---|
| `index.html` | Guía interactiva principal — mapa del deploy, terminal simulada, diagramas, quiz, checklist |
| `clase.html` | Guía de facilitación docente — guión de 120-150 min con 7 secciones |
| `ejercicios.html` | 10 ejercicios paso a paso — de localhost a URL pública |
| `cheatsheet.html` | Referencia rápida — comandos Git, configuración Render, errores comunes |
| `entregable_equipo.html` | Entregable por equipo — checklist, rúbrica, URL pública, reflexión |
| `styles.css` | Hoja de estilos compartida (paleta esmeralda/verde) |
| `README.md` | Este archivo |

## Aprendizajes esperados

- Publica la aplicación web en internet
- Ejecuta el flujo Git: add → commit → push
- Configura un Web Service en Render
- Diagnostica errores comunes de deploy leyendo logs

## Requisitos de la app para deploy en Render

### Archivo: `system.properties` (raíz del proyecto)
```properties
java.runtime.version=17
```

### Ajustes en `application.properties`
```properties
server.port=${PORT:8080}
spring.datasource.url=jdbc:h2:mem:proddb
spring.datasource.driver-class-name=org.h2.Driver
spring.jpa.hibernate.ddl-auto=update
spring.h2.console.enabled=true
spring.h2.console.settings.web-allow-others=true
```

### Configuración de Render
| Campo | Valor |
|---|---|
| Build Command | `./mvnw clean install -DskipTests` |
| Start Command | `java -jar target/*.jar` |
| Plan | Free |
| Variable | `JAVA_TOOL_OPTIONS=-Xmx256m` |

## Flujo de deploy

```
Código listo → git add . → git commit -m "..." → git push origin main → Render detecta → Build → ¡En vivo!
```

## Estructura del proyecto para deploy

```
mi-proyecto/
├── pom.xml
├── system.properties          ← NUEVO (Java 17)
├── .gitignore
├── mvnw / mvnw.cmd
├── src/
│   └── main/
│       ├── java/              (código fuente)
│       └── resources/
│           ├── application.properties   ← MODIFICADO
│           └── templates/
└── target/                    ← NO subir (está en .gitignore)
```

## Cómo usar este material

1. Abrir `index.html` con Live Server o doble clic.
2. Navegar las secciones interactivas (terminal simulada, quiz, checklist).
3. Usar `clase.html` como guión de facilitación.
4. Asignar `ejercicios.html` como práctica guiada.
5. Recoger evidencias en `entregable_equipo.html`.

## Paleta de color

- Verde esmeralda (`#10b981`) — diferente de Semana 5 (naranja) y Semana 6 (índigo)
- Temática: "ir en vivo", "lanzamiento", "publicar"
