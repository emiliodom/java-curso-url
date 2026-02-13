+--------------------------------------------------------------------------+
| ### Universidad Rafael Landívar                                          |
|                                                                          |
| Facultad de Humanidades                                                  |
|                                                                          |
| Departamento de Educación                                                |
|                                                                          |
| **Guía de aprendizaje núm. 4**                                           |
|                                                                          |
| **Semana 4 – Unidad 4**                                                  |
|                                                                          |
| **Fecha de entrega: Viernes 13 de febrero de 2026**                      |
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

***"Un CRUD no es una lista de funciones; es un flujo completo que se puede explicar y verificar: ver, crear, editar y borrar, con datos que persisten."***

**Contexto (conexión con Semana 3):** Ya logramos el primer arranque real de Spring Boot y un endpoint funcional. En Semana 4 reforzamos los conceptos de estructura y avanzamos al **inicio del CRUD** con un stack didáctico, sencillo de montar y suficientemente “real” para motivar:

- **DB:** H2 en modo **archivo** (persistente) → sin instalaciones externas.
- **Vistas:** Thymeleaf + **Bootstrap** → UI pulida rápidamente.
- **Reto avanzado (proyecto final):** cambiar Bootstrap por Tailwind (si el equipo está cómodo con setup adicional).

+---------------------------------+------------------------------------+
| **Aprendizajes esperados**      | **Productos que evidencian el      |
|                                 | aprendizaje**                      |
+=================================+====================================+
| **Prepara y verifica el entorno | *Captura/nota de verificación:*     |
| de desarrollo para Spring Boot**| `java -version`, `.\mvnw.cmd -v`.*    |
+---------------------------------+------------------------------------+
| **Comprende la estructura de un | *Mapa de estructura (1 página):*     |
| proyecto Spring Boot (capas y   | Controller/Service/Repository/Model |
| responsabilidades).**           | + templates/static.*                |
+---------------------------------+------------------------------------+
| **Configura una base H2         | *Evidencia H2 Console:* captura de   |
| persistente (archivo) y usa     | `/h2-console` conectada con JDBC URL|
| H2 Console como herramienta.**  | correcto.*                          |
+---------------------------------+------------------------------------+
| **Implementa el inicio del CRUD | *Evidencia CRUD (mínimo):* pantalla  |
| con pantallas (Read/Create) y   | de listado + formulario + 3 registros|
| comprende el flujo completo.**  | guardados.*                         |
+---------------------------------+------------------------------------+
| **Aplica comandos de compilación| *Bitácora de troubleshooting:* 3     |
| y troubleshooting (limpieza,    | errores (o riesgos) + comando usado |
| logs, puertos).**               | para resolverlos.*                  |
+---------------------------------+------------------------------------+

+-----------------------------------------------------------------------+
| ![Libros](media/image6.png){width="0.4895833333333333in"              |
| height="0.4895833333333333in"}**PRIMERA PARTE: REFUERZO (ENTORNO +    |
| ESTRUCTURA + CONCEPTOS CRUD)**                                         |
|                                                                       |
| **Propósito de la actividad:** reforzar la estructura mental del       |
| proyecto Spring Boot y preparar el terreno para un CRUD completo,      |
| priorizando comprensión y capacidad de enseñar (docencia TIC).         |
|                                                                       |
| **Actividades (Instrucciones):**                                      |
|                                                                       |
| 1) **Lectura guiada (25–35 min)**                                     |
|   - Abrir el material HTML de la semana:                               |
|     - `Material_Sesion_Clase_4_CRUD/clase.html`                         |
|     - `Material_Sesion_Clase_4_CRUD/preparar_pc.html`                   |
|     - `Material_Sesion_Clase_4_CRUD/cheatsheet.html`                    |
|   - Responder (6–10 líneas): ¿qué hace cada capa?                       |
|     - Controller / Service / Repository / Model / templates             |
|                                                                       |
| 2) **Mini-mapa del CRUD (15–20 min)**                                  |
|   - Para la entidad “Libro” (o “Recurso didáctico”), escribir:          |
|     - Datos (campos)                                                    |
|     - Pantallas (listado, formulario)                                   |
|     - Acciones (Create/Read/Update/Delete)                              |
|   - Dibujar el flujo en 1 línea:                                        |
|     *Vista → Controller → Service → Repository → DB*                    |
|                                                                       |
| **Recursos:** Material HTML (Sesión 4) y notas de Sesión 3.             |
|                                                                       |
| **Evaluación (Formativa):** claridad del mapa (no memorizar, explicar). |
+=======================================================================+

![Piezas de rompecabezas](media/image8.png){width="0.5833333333333334in"
height="0.5833333333333334in"}

**SEGUNDA PARTE: CONSTRUCCIÓN DEL PROYECTO (INICIO DEL CRUD)**

**Propósito de la actividad:** construir un CRUD mínimo pero completo (con pantallas) y datos persistentes, usando un stack didáctico que minimiza fricción técnica.

**Entregable principal (equipo, 3–4 integrantes): CRUD inicial con evidencias**

1) **Comandos y ejecución (equipo):**
- Ejecutar y evidenciar:
  - `.\mvnw.cmd clean`
  - `.\mvnw.cmd spring-boot:run`
- Captura del log donde se vea “Started …” y puerto.

2) **H2 persistente (equipo):**
- Configurar en `application.properties`:
  - `spring.datasource.url=jdbc:h2:file:./data/semana4db`
  - `spring.jpa.hibernate.ddl-auto=update`
  - `spring.h2.console.enabled=true`
- Evidencia: captura de `/h2-console` conectada con JDBC URL correcto.

3) **CRUD mínimo con pantallas (equipo):**
- Rutas sugeridas: `/recursos`, `/recursos/new`.
- Evidencia: captura del listado con al menos 3 registros creados.

4) **UI pulida (equipo):**
- Usar Bootstrap en templates Thymeleaf.
- Evidencia: captura de formulario y tabla con estilos.

5) **Troubleshooting (equipo):**
- Registrar una mini-bitácora (3 ítems):
  - “Qué falló / Qué decía el error / Cómo lo resolvimos (comando o ajuste)”
- Comandos recomendados:
  - `.\mvnw.cmd clean spring-boot:run`
  - `.\mvnw.cmd spring-boot:run -Dspring-boot.run.arguments="--debug"`
  - `netstat -ano | findstr :8080` y `taskkill /PID <id> /F`

6) **Reflexión docente individual (200–300 palabras):**
- ¿Qué parte del flujo CRUD es más difícil de explicar?
- ¿Qué analogía usarías (biblioteca, secretaría, registro de estudiantes)?
- ¿Qué error típico anticipas y cómo lo “diagnosticarías” con calma?

**Evaluación (rúbrica rápida 100 pts):**
- Proyecto corre (comandos + log + estabilidad): 20
- H2 persistente + evidencia en consola: 20
- Read + Create con pantallas: 30
- Update/Delete (o aproximación clara y documentada): 20
- Explicación didáctica + reflexión: 10

![Cronómetro](media/image6.png){width="0.4895833333333333in"
height="0.4895833333333333in"}

**CRONOGRAMA (10 horas)**

  -----------------------------------------------------------------------
  **Actividad**                             **Tiempo**     **Aprendizaje**
  ----------------------------------------  ------------   ------------------------------
  Lectura guiada + mapa de capas             2.0 horas     Estructura y responsabilidades
  Configuración H2 persistente + consola     2.0 horas     Persistencia y herramienta de verificación
  CRUD mínimo (Read/Create) con pantallas    4.0 horas     Flujo completo + evidencia visible
  Update/Delete (extra) + refinamiento UI    1.5 horas     Completar ciclo CRUD + pulido
  Bitácora + reflexión docente               0.5 horas     Metacognición y diagnóstico
                                            Total: 10 horas
  -----------------------------------------------------------------------

![Libros en estantería](media/image4.png){width="0.4895833333333333in"
height="0.4895833333333333in"}

**RECURSOS DE APOYO**

- Material HTML Sesión 4: `Material_Sesion_Clase_4_CRUD/`
- Plantillas Thymeleaf (copiar al proyecto): `Material_Sesion_Clase_4_CRUD/plantillas_thymeleaf/`
- Material Sesión 3 (recordatorio primer run + endpoint): `Material_Sesion_Clase_3_MVC/`
- Spring Initializr: https://start.spring.io/
- Spring Boot (referencia): https://spring.io/projects/spring-boot
