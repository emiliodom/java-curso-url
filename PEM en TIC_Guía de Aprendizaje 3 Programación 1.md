+--------------------------------------------------------------------------+
| ### Universidad Rafael Landívar                                          |
|                                                                          |
| Facultad de Humanidades                                                  |
|                                                                          |
| Departamento de Educación                                                |
|                                                                          |
| **Guía de aprendizaje núm. 3**                                           |
|                                                                          |
| **Semana 3 – Unidad 3**                                                  |
|                                                                          |
| **Fecha de entrega: Viernes 6 de febrero de 2026**                       |
|                                                                          |
| +----------------------------+-----------------------------------------+ |
| | Profesorados con           | Nombre del curso: Introducción al       | |
| | Especialidad en TIC        | Desarrollo Web con Java                 | |
| |                            |                                         | |
| | **Año Psicopedagógico**    | Enfoque Pedagógico para Docentes       | |
| +============================+=========================================+ |
+--------------------------------------------------------------------------+

![Transformación Digital -- Universidad Rafael
Landívar](media/image1.png){width="3.2336996937882763in"
height="1.3760411198600175in"}![gráficos de color
degradado](media/image2.png){width="8.268055555555556in"
height="1.5618055555555554in"}

![Libro abierto](media/image4.png){width="0.5729166666666666in"
height="0.5729166666666666in"}

**PARTE INTRODUCTORIA**

***"Un buen diseño no es el más complejo; es el que se puede explicar y mantener. Si puedes enseñarlo, puedes construirlo."***

**Nota pedagógica (perfil del curso):** Esta guía está diseñada para futuros **docentes de Tecnología (TIC)**. El objetivo es lograr dos cosas en la Semana 3:

1) Mantener **MVC como mapa mental mínimo** (quién hace qué) para no perderse.
2) Tener un **primer arranque real de Spring Boot** (entorno + primer build + primer endpoint) para que la Semana 4 sea menos intimidante.

+---------------------------------+------------------------------------+
| **Aprendizajes esperados**      | **Productos que evidencian el      |
|                                 | aprendizaje**                      |
+=================================+====================================+
| **Comprende patrones de diseño y| *Checklist de entorno listo +        |
| separación de responsabilidades**| capturas/nota de verificación:*      |
| en aplicaciones web.**          | `java -version`, `javac -version`.* |
+---------------------------------+------------------------------------+
| **Usa MVC como mapa mental      | *Mini-explicación (8–12 líneas):*    |
| mínimo (quién hace qué) y lo    | ¿Dónde vive el Controller y por qué |
| conecta con Spring Boot.**      | eso es MVC mínimo?                  |
+---------------------------------+------------------------------------+
| **Genera, ejecuta y prueba un   | *Evidencia de primer arranque:*      |
| proyecto Spring Boot por primera| `.\mvnw.cmd spring-boot:run` corriendo |
| vez (primer build exitoso).**   | + captura del log/terminal.*         |
+---------------------------------+------------------------------------+
| **Crea y prueba un endpoint     | *Evidencia de endpoint:* captura de  |
| REST simple (`/hello`).**       | navegador o `curl` mostrando la      |
|                                 | respuesta de `/hello`.*              |
+---------------------------------+------------------------------------+

+-----------------------------------------------------------------------+
| ![Libros](media/image6.png){width="0.4895833333333333in"              |
| height="0.4895833333333333in"}**PRIMERA PARTE: REFUERZO DE            |
| APRENDIZAJES (PATRONES + SEPARACIÓN DE RESPONSABILIDADES)**            |
|                                                                       |
| **Propósito de la actividad:** Entender (sin memorizar listas) qué es  |
| un patrón de diseño y por qué la separación de responsabilidades es     |
| clave para enseñar y construir aplicaciones web mantenibles, y usar MVC |
| como un mapa mental mínimo para iniciar Spring Boot con menos fricción. |
|                                                                       |
| **Actividades (Instrucciones):**                                      |
|                                                                       |
| 1) **Lectura guiada (20–30 min)**                                     |
|   - Lee el material de la sesión (HTML):                               |
|     - `Material_Sesion_Clase_3_MVC/clase.html`                          |
|     - `Material_Sesion_Clase_3_MVC/cheatsheet.html`                     |
|   - Responde en 5–7 líneas: ¿Qué problema resuelve “separar            |
|     responsabilidades”?                                                |
|                                                                       |
| 2) **MVC mínimo (15–20 min)**                                         |
|   - Toma el caso: “Registro de voluntarios para una entidad sin fines  |
|     de lucro”.                                                        |
|   - Clasifica al menos 9 elementos en 3 columnas (Modelo / Vista /     |
|     Controlador):                                                     |
|       - *Datos:* nombre, teléfono, fecha de ingreso, área, etc.        |
|       - *Acciones:* registrar, listar, buscar, editar.                 |
|       - *Pantallas:* formulario, listado, detalle.                     |
|   - Cierra con 1 frase: ¿qué parte sería el **Controller** en Spring?  |
|                                                                       |
| **Recursos:**                                                         |
| - Material HTML de la Sesión 3.                                        |
| - Programa del curso: Semana 3 (patrones, MVC).                        |
|                                                                       |
| **Evaluación (Formativa):**                                           |
| *Claridad conceptual: que se note que entiendes “quién hace qué”       |
| dentro del sistema.*                                                   |
+=======================================================================+

![Piezas de rompecabezas](media/image8.png){width="0.5833333333333334in"
height="0.5833333333333334in"}

**SEGUNDA PARTE: CONSTRUCCIÓN DEL PROYECTO (DISEÑO MVC PARA EL PROYECTO FINAL)**

**Propósito de la actividad:** Lograr un primer arranque real de Spring Boot (sin “magia”), pero cuidando el mapa mental mínimo de MVC para organizar el proyecto.

**Entregable principal (equipo, 3–4 integrantes): evidencias del primer arranque**

1) **Checklist de entorno listo (individual):**
- Captura o nota con salida de: `java -version` y `javac -version`.
- Anotar editor/IDE usado (VS Code / IntelliJ / Eclipse).

2) **Proyecto generado con Spring Initializr (equipo):**
- Configuración usada (Project, Java, Boot, Group, Artifact, dependencias).
- Evidencia de que el proyecto compila/corre.

3) **Primer run (equipo):**
- Ejecutar: `.\mvnw.cmd spring-boot:run`.
- Captura del log donde se vea “Started …” y el puerto.

4) **Primer endpoint (equipo):**
- Crear un endpoint `/hello` y probarlo en el navegador.
- Evidencia de respuesta (captura de navegador o comando `curl`).

5) **MVC mínimo (equipo):**
- En 8–12 líneas, explicar dónde está el **Controller** (y qué representa el **Model**) en su proyecto.

6) **Reflexión docente (individual, 200–300 palabras):**
- ¿Qué parte fue más difícil (instalación, terminal, dependencias, puertos) y cómo la enseñarías?
- ¿Qué error típico anticipas en estudiantes novatos?

**Evaluación (rúbrica rápida 100 pts):**
- Entorno verificado (capturas y coherencia): 20
- Proyecto generado correctamente (configuración + estructura): 20
- Primer run exitoso (log + puerto): 25
- Endpoint `/hello` probado: 25
- Explicación didáctica (MVC mínimo + reflexión): 10

![Cronómetro](media/image6.png){width="0.4895833333333333in"
height="0.4895833333333333in"}

**CRONOGRAMA (10 horas)**

  -----------------------------------------------------------------------
  **Actividad**                             **Tiempo**     **Aprendizaje**
  ----------------------------------------  ------------   ------------------------------
  Lectura guiada + notas                     1.5 horas     Patrones, responsabilidades y mapa mental
  MVC mínimo (clasificación + flujo)         1.5 horas     “Quién hace qué” (sin memorizar)
  Entorno listo (JDK 17 + verificación)      2.0 horas     Preparación técnica
  Spring Initializr (generar proyecto)       1.5 horas     Estructura del proyecto
  Primer run (mvnw) + troubleshooting        2.0 horas     Build/Run exitoso
  Endpoint /hello + evidencia                1.0 hora      Primer resultado visible
  Reflexión docente individual               0.5 horas     Metacognición y evaluación por proceso
                                            Total: 10 horas
  -----------------------------------------------------------------------

![Libros en estantería](media/image4.png){width="0.4895833333333333in"
height="0.4895833333333333in"}

**RECURSOS DE APOYO**

- Material HTML de la Sesión 3: `Material_Sesion_Clase_3_MVC/`
- Preparar PC (JDK 17, PATH/JAVA_HOME, errores frecuentes): `Material_Sesion_Clase_3_MVC/preparar_pc.html`
- Spring Initializr (para explorar estructura): https://start.spring.io/
- Documentación (referencia): https://spring.io/projects/spring-boot
