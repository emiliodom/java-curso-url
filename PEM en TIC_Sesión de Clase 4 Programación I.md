+--------------------------------------------------------------------------+
| ### Universidad Rafael Landívar                                          |
|                                                                          |
| Facultad de Humanidades                                                  |
|                                                                          |
| Departamento de Educación                                                |
|                                                                          |
| +----------------------------+-----------------------------------------+ |
| | Profesorados con           | Nombre del curso: Introducción al       | |
| | Especialidad en TIC        | Desarrollo Web con Java                 | |
| |                            | Número de créditos: 4                   | |
| |                            |                                         | |
| |                            | Ciclo y módulo: Cuarto ciclo            | |
| +============================+=========================================+ |
+--------------------------------------------------------------------------+

![Transformación Digital -- Universidad Rafael
Landívar](media/image1.png){width="3.2336996937882763in"
height="1.3760411198600175in"}![gráficos de color
degradado](media/image2.png){width="8.268055555555556in"
height="1.5618055555555554in"}

**Secuencia de aprendizaje**

Sesión presencial/**[sincrónica]{.underline}** #4

**Tema:** Inicios del CRUD en Spring Boot (H2 archivo + Thymeleaf + Bootstrap) + troubleshooting

**Enfoque del curso (perfil del estudiante):** formación de docentes TIC. Priorizamos comprensión, capacidad de enseñar y evidencias por proceso.

+----------------+------------------------------------------------------------+
|                | ![Cabeza con                                               |
|                | engranajes](media/image4.png){width="0.4583333333333333in" |
|                | height="0.4583333333333333in"}**Información importante**   |
+================+============================================================+
| **Aprendizajes | - Prepara y verifica el entorno de desarrollo (Java 17,     |
| esperados**    |   mvnw, logs).                                              |
|                |                                                            |
|                | - Comprende la estructura de un proyecto Spring Boot y      |
|                |   ubica responsabilidades (Controller/Service/Repository).  |
|                |                                                            |
|                | - Configura H2 en modo archivo y usa H2 Console para        |
|                |   verificar persistencia.                                   |
|                |                                                            |
|                | - Implementa un CRUD mínimo con pantallas: listar, crear,   |
|                |   (editar/eliminar opcional) con Thymeleaf + Bootstrap.     |
|                |                                                            |
|                | - Aplica comandos de compilación/limpieza y troubleshooting |
|                |   (puertos, --debug, logs).                                 |
+----------------+------------------------------------------------------------+
| **Contenidos   | - Spring Boot: estructura del proyecto, dependencias.       |
| temáticos**    |                                                            |
|                | - Spring MVC (vistas): Thymeleaf.                            |
|                |                                                            |
|                | - Persistencia: Spring Data JPA + H2 (archivo).              |
|                |                                                            |
|                | - CRUD básico (Create/Read/Update/Delete).                   |
|                |                                                            |
|                | - Comandos Maven Wrapper + troubleshooting.                  |
+----------------+------------------------------------------------------------+
| **Habilidades  | - Configurar properties y validar con consola/endpoint.      |
| y destrezas**  |                                                            |
|                | - Crear entity + repository + controller con vistas.         |
|                |                                                            |
|                | - Leer logs y diagnosticar errores comunes.                  |
+----------------+------------------------------------------------------------+
| **Valores y    | - Orden y claridad al explicar un sistema.                   |
| actitudes**    |                                                            |
|                | - Perseverancia ante errores técnicos (diagnóstico).         |
|                |                                                            |
|                | - Trabajo colaborativo y documentación de evidencias.        |
+----------------+------------------------------------------------------------+
| **Productos    | *CRUD inicial funcionando + evidencias (capturas/logs) +     |
| que evidencian | bitácora de troubleshooting + mini-explicación didáctica.*  |
| el             |                                                            |
| aprendizaje**  |                                                            |
+----------------+------------------------------------------------------------+

  -----------------------------------------------------------------------
  ![Internet](media/image6.png){width="0.5104166666666666in"
  height="0.5104166666666666in"}**Desarrollo de la secuencia**
  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

1.  **Activación de presaberes**

*Actividad: “De endpoint a app real” (lluvia de ideas rápida).* 

*Tiempo estimado: 10 minutos*

*Recursos: Pizarra o diapositiva con el flujo Vista→Controller→Service→Repository→DB.*

*Actividad que realizará el estudiante: mencionar qué le falta a una app real (datos, pantallas, operaciones, persistencia) y conectar con lo ya logrado en Semana 3 (server + endpoint).* 

2.  **Retroalimentación**

*Actividad: Reforzar comandos y lectura de logs (5–10 min).*

*Tiempo estimado: 10 minutos*

*Recursos: Material HTML Sesión 4 (cheat sheet).*

*Actividad que realizará el estudiante: ejecutar `.\mvnw.cmd clean` y `.\mvnw.cmd spring-boot:run` (o mostrar evidencia si ya lo tiene) y localizar en el log el “Started …” y el puerto.*

3.  **Construcción del conocimiento (hands-on)**

***Actividad 1: Estructura del proyecto (15 min)***

*Tiempo estimado: 15 minutos*

*Recursos: `Material_Sesion_Clase_4_CRUD/clase.html` (sección de estructura).*

*Actividad que realizará el estudiante: ubicar carpetas y escribir en 1 frase qué hace cada una (controller/service/repository/model/templates/static).*

*Evaluación: preguntas rápidas (¿dónde vive una vista? ¿dónde vive una tabla?).*

***Actividad 2: H2 persistente + H2 Console (20 min)***

*Tiempo estimado: 20 minutos*

*Recursos: `Material_Sesion_Clase_4_CRUD/preparar_pc.html`.*

*Actividad que realizará el estudiante:* 
- Configurar `application.properties` con H2 en archivo.
- Arrancar app y abrir `/h2-console`.
- Conectar con el JDBC URL correcto.

*Evaluación: evidencia de acceso a consola.*

***Actividad 3: CRUD mínimo con pantallas (45–55 min)***

*Tiempo estimado: 45–55 minutos*

*Recursos: `Material_Sesion_Clase_4_CRUD/ejercicios.html` + plantillas de ejemplo en `plantillas_thymeleaf/`.*

*Actividad que realizará el estudiante:*
- Crear Entity `DidacticResource` (Recurso didáctico).
- Crear Repository `DidacticResourceRepository`.
- Crear Controller MVC con rutas `/recursos` y `/recursos/new`.
- Crear templates `recursos/list` y `recursos/form` usando Bootstrap.
- Probar Read/Create y guardar 3 registros.

*Evaluación: verificación práctica (pantallas + registros + persistencia).*

4.  **Aplicación del conocimiento**

***Actividad 1: Trabajo en equipos + evidencias (25–30 min)***

*Tiempo estimado: 25–30 minutos*

*Recursos: `Material_Sesion_Clase_4_CRUD/entregable_equipo.html`.*

*Actividad que realizará el estudiante: completar checklist, adjuntar capturas, y redactar mini-explicación didáctica del flujo.*

*Evaluación: checklist + coherencia de evidencias.*

5.  **Reflexión sobre mi proceso de aprendizaje**

*Actividad: “Bitácora de troubleshooting” (metacognición).*

*Tiempo estimado: 10 minutos*

*Recursos: Cheat sheet.*

*Actividad que realizará el estudiante: registrar 3 aprendizajes/errores y el comando o cambio aplicado (clean, --debug, netstat, rutas de templates, JDBC URL).*

*Evaluación: formativa (claridad y capacidad de explicar el diagnóstico).*

6.  **Introducción al siguiente tema**

*Actividad: “Semana 5: mejorar el CRUD” (Service layer, validaciones, mensajes, mejores prácticas).*

*Tiempo estimado: 5 minutos*

*Recursos: resumen del flujo y piezas del CRUD.*

*Actividad que realizará el estudiante: anotar qué parte quedó frágil (vistas, DB, rutas) y qué quiere reforzar.*

7.  **Actividad de cierre y despedida**

*Actividad: Ticket de salida.*

*Tiempo estimado: 5 minutos*

*Actividad que realizará el estudiante: escribir 1 analogía docente para explicar CRUD y 1 comando que usaría si la app no arranca.*
