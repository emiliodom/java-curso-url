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

Sesión presencial/**[sincrónica]{.underline}** #3

**Tema:** Patrones de diseño aplicados a la web (MVC mínimo) + primer arranque de Spring Boot (entorno y “Hello World”)

**Enfoque del curso (perfil del estudiante):** Formación de docentes de Tecnología (TIC). El objetivo es comprender y enseñar la organización de aplicaciones web (no formar programadores profesionales).

+----------------+------------------------------------------------------------+
|                | ![Cabeza con                                               |
|                | engranajes](media/image4.png){width="0.4583333333333333in" |
|                | height="0.4583333333333333in"}**Información importante**   |
+================+============================================================+
| **Aprendizajes | - Comprende qué es un patrón de diseño y por qué se usa.   |
| esperados**    |                                                            |
|                | - Usa MVC como “mapa mental” mínimo para no perderse al    |
|                |   iniciar un proyecto web (quién hace qué).                |
|                |                                                            |
|                | - Prepara el entorno mínimo para Spring Boot (JDK 17 +     |
|                |   editor/IDE) y verifica versiones.                        |
|                |                                                            |
|                | - Genera un proyecto con Spring Initializr y lo ejecuta    |
|                |   por primera vez (primer build exitoso).                  |
|                |                                                            |
|                | - Crea un endpoint “Hello” con un controlador simple y lo  |
|                |   prueba en el navegador.                                  |
+----------------+------------------------------------------------------------+
| **Contenidos   | - MVC y separación de responsabilidades (mínimo viable).   |
| temáticos**    |                                                            |
|                | - Preparación del entorno Spring Boot (JDK 17, editor/IDE, |
|                |   terminal, proyecto).                                     |
|                |                                                            |
|                | - Spring Initializr como generador de proyecto (“como un   |
|                |   create-react-app” para Spring).                           |
|                |                                                            |
|                | - Primer build y ejecución (mvnw / wrapper).               |
|                |                                                            |
|                | - Primer controlador y prueba de endpoint.                 |
+----------------+------------------------------------------------------------+
| **Habilidades  | - Verificar instalaciones (java -version, javac -version). |
| y destrezas**  |                                                            |
|                | - Generar un proyecto y ejecutarlo por primera vez.        |
|                |                                                            |
|                | - Crear un controlador mínimo y probarlo.                  |
|                |                                                            |
|                | - Explicar el rol de Controller/Model (MVC mínimo) de      |
|                |   forma didáctica.                                         |
+----------------+------------------------------------------------------------+
| **Valores y    | - Orden y claridad en la organización de ideas.            |
| actitudes**    |                                                            |
|                | - Colaboración y escucha (diseño en equipo).               |
|                |                                                            |
|                | - Paciencia ante la complejidad (lo difícil se divide).    |
+----------------+------------------------------------------------------------+
| **Productos    | *Evidencia de entorno listo (captura/nota de versiones) +  |
| que evidencian | proyecto Spring Boot generado y ejecutado + endpoint       |
| el             | “Hello” funcionando.*                                     |
| aprendizaje**  | *Mini-explicación: ¿dónde está el Controller y por qué     |
|                | eso es MVC mínimo?*                                        |
+----------------+------------------------------------------------------------+

  -----------------------------------------------------------------------
  ![Internet](media/image6.png){width="0.5104166666666666in"
  height="0.5104166666666666in"}**Desarrollo de la secuencia**
  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

1.  **Activación de presaberes**

*Actividad: “Una escuela también tiene MVC” — analogía por roles.*

*Tiempo estimado: 10 minutos*

*Recursos: Pizarra / diapositiva con roles (Director, Docente, Estudiante, Secretaría).*

*Actividad que realizará el estudiante: Proponer ejemplos de “roles” y “responsabilidades” en una institución educativa (qué hace cada rol y qué no debería hacer).*

2.  **Retroalimentación**

*Actividad: Conectar con lo visto: Java básico (Semana 1) y GitHub (Semana 2) como “herramientas”, y la necesidad de organizar el proyecto para que sea mantenible y evaluable (proceso).*

*Tiempo estimado: 10 minutos*

*Recursos: Ejemplo simple de “código desordenado” vs “código organizado” (captura o texto).* 

*Actividad que realizará el estudiante: Identificar 2 señales de desorden (todo en un solo archivo, nombres confusos, difícil de explicar) y 2 señales de buen diseño (responsabilidades separadas, nombres claros).*

3.  **Construcción del conocimiento (hands-on)**

***Actividad 1 (mínima): MVC como mapa mental (15 min)***

*Actividad: Explicación breve de MVC y separación de responsabilidades, pero solo lo necesario para iniciar Spring Boot sin perderse: Controller = “entrada”; Model = “datos”; (Service/Repository se introduce solo como vocabulario).* 

*Tiempo estimado: 15 minutos*

*Recursos: Pizarra + cheat sheet de la sesión.*

*Actividad que realizará el estudiante: En 3 minutos, escribir un ejemplo de cada uno (Modelo, Vista, Controlador) del caso “voluntarios”.*

*Evaluación: Preguntas rápidas (¿dónde va una URL? ¿dónde van los datos?).*

***Actividad 2: Checklist de entorno (20–25 min)***

*Actividad: Preparación del entorno mínimo para Spring Boot en Windows (enfoque práctico).*

*Tiempo estimado: 20–25 minutos*

*Recursos: Guía paso a paso (material HTML) + “Preparar PC”: `Material_Sesion_Clase_3_MVC/preparar_pc.html`.*

*Actividad que realizará el estudiante:*
- Instalar JDK 17 (recomendado: Temurin).
- Verificar: `java -version` y `javac -version`.
- Verificar que puede abrir un proyecto en editor/IDE.

***Actividad 3: “Create-react-app” de Spring — Spring Initializr (25–30 min)***

*Actividad: Generar un proyecto Spring Boot desde https://start.spring.io/ y explicar qué genera (carpetas y archivos).*

*Tiempo estimado: 25–30 minutos*

*Recursos: Navegador + Spring Initializr.*

*Actividad que realizará el estudiante:* generar el ZIP con **Spring Web**, descomprimir, abrir carpeta.

***Actividad 4: Primer build y primer run (25–35 min)***

*Actividad: Ejecutar el proyecto por primera vez usando el Maven Wrapper (sin instalar Maven aparte).*

*Tiempo estimado: 25–35 minutos*

*Recursos: Terminal (Windows) + comandos de la guía.*

*Actividad que realizará el estudiante:* correr `.\mvnw.cmd spring-boot:run` y verificar `http://localhost:8080/`.

***Actividad 5: Primer endpoint (20–25 min)***

*Actividad: Crear un controlador mínimo `HelloController` con un endpoint `/hello` y probarlo en el navegador.*

*Tiempo estimado: 20–25 minutos*

*Recursos: Material HTML con ejemplo.*

*Actividad que realizará el estudiante:* crear el archivo, reiniciar la app y probar `http://localhost:8080/hello`.

4.  **Aplicación del conocimiento**

***Actividad 1 (principal): Evidencia de primer arranque + mini MVC***

*Actividad: En equipos de 3–4, completar el entregable con evidencias del entorno, ejecución y endpoint, y una mini-explicación MVC (solo Controller/Model y flujo request/response).*

*Tiempo estimado: 25–30 minutos*

*Recursos: Plantilla de entregable (HTML).*

*Actividad que realizará el estudiante:* completar checklist y registrar capturas/links. 

*Evaluación: Checklist (app corre, endpoint responde, explicación clara y didáctica).*

5.  **Reflexión sobre mi proceso de aprendizaje**

*Actividad: “Cómo lo enseñaría” (metacognición docente).*

*Tiempo estimado: 10 minutos*

*Recursos: Preguntas guía.*

*Actividad que realizará el estudiante: Responder por escrito:
- ¿Qué parte de MVC fue más confusa y por qué?
- ¿Qué analogía usarías para explicarlo en secundaria?
- ¿Qué error típico anticipas en estudiantes novatos?

*Evaluación: Formativa (claridad y honestidad reflexiva).*

6.  **Introducción al siguiente tema**

*Actividad: “Semana 4: Spring Boot con más estructura” — qué sigue después del primer run.*

*Tiempo estimado: 5 minutos*

*Recursos: Checklist (JDK 17 listo + proyecto ya generado + app ya ejecutada).*

*Actividad que realizará el estudiante: Anotar qué parte fue el mayor obstáculo (instalación, terminal, dependencias, puertos) y qué necesita para avanzar (IDE, permisos, internet).*

7.  **Actividad de cierre y despedida**

*Actividad: Ticket de salida.*

*Tiempo estimado: 5 minutos*

*Recursos: Chat / papel.*

*Actividad que realizará el estudiante: Escribir:
- 1 cosa que ahora entiende de MVC.
- 1 cosa que le gustaría ver aplicada en Spring Boot.
