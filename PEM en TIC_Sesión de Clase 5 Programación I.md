+--------------------------------------------------------------------------+
| ### Universidad Rafael Landivar                                          |
|                                                                          |
| Facultad de Humanidades                                                  |
|                                                                          |
| Departamento de Educacion                                                |
|                                                                          |
| +----------------------------+-----------------------------------------+ |
| | Profesorados con           | Nombre del curso: Introduccion al       | |
| | Especialidad en TIC        | Desarrollo Web con Java                 | |
| |                            | Numero de creditos: 4                   | |
| |                            |                                         | |
| |                            | Ciclo y modulo: Cuarto ciclo            | |
| +============================+=========================================+ |
+--------------------------------------------------------------------------+

![Transformacion Digital -- Universidad Rafael
Landivar](media/image1.png){width="3.2336996937882763in"
height="1.3760411198600175in"}![graficos de color
degradado](media/image2.png){width="8.268055555555556in"
height="1.5618055555555554in"}

**Secuencia de aprendizaje**

Sesion presencial/**[sincronica]{.underline}** #5

**Tema:** Rutas y controladores en Spring Boot + formularios GET/POST + por que de imports y dependencias

**Enfoque del curso (perfil del estudiante):** formacion de docentes TIC. Priorizamos comprension, capacidad de ensenar y evidencias por proceso.

+----------------+------------------------------------------------------------+
|                | ![Cabeza con                                               |
|                | engranajes](media/image4.png){width="0.4583333333333333in" |
|                | height="0.4583333333333333in"}**Informacion importante**  |
+================+============================================================+
| **Aprendizajes | - Identifica rutas y controladores en un proyecto Spring    |
| esperados**    |   Boot y explica su proposito con ejemplos.                |
|                |                                                            |
|                | - Conecta un formulario HTML con un metodo POST del         |
|                |   Controlador y guarda informacion de forma segura.        |
|                |                                                            |
|                | - Explica por que se usan imports y dependencias clave      |
|                |   (web, thymeleaf, data-jpa, h2) en el proyecto.           |
|                |                                                            |
|                | - Reconoce errores comunes de rutas y plantillas y aplica   |
|                |   pasos de diagnostico ordenados.                          |
+----------------+------------------------------------------------------------+
| **Contenidos   | - Spring MVC: @Controller, @GetMapping, @PostMapping.       |
| tematicos**    |                                                            |
|                | - Rutas, path variables y Model.                           |
|                |                                                            |
|                | - Formularios (GET/POST) y validacion basica.              |
|                |                                                            |
|                | - Dependencias y imports esenciales.                       |
|                |                                                            |
|                | - Flujo MVC explicado para docencia.                       |
+----------------+------------------------------------------------------------+
| **Habilidades  | - Disenar rutas coherentes y nombrarlas con claridad.       |
| y destrezas**  |                                                            |
|                | - Conectar vistas con controladores sin errores 404.        |
|                |                                                            |
|                | - Detectar por que una vista no carga o por que un POST     |
|                |   no guarda.                                                |
+----------------+------------------------------------------------------------+
| **Valores y    | - Orden y precision al explicar un flujo tecnico.           |
| actitudes**    |                                                            |
|                | - Paciencia y metodo al depurar.                            |
+----------------+------------------------------------------------------------+
| **Productos    | *Mapa MVC de rutas + evidencia de formulario funcional +    |
| que evidencian | mini-explicacion didactica (3-5 parrafos).*                 |
| el             |                                                            |
| aprendizaje**  |                                                            |
+----------------+------------------------------------------------------------+

  -----------------------------------------------------------------------
  ![Internet](media/image6.png){width="0.5104166666666666in"
  height="0.5104166666666666in"}**Desarrollo de la secuencia**
  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

1.  **Activacion de presaberes**

*Actividad: "De URL a Controlador" (lluvia de ideas rapida).* 

*Tiempo estimado: 10 minutos*

*Recursos: Pizarra o diapositiva con un navegador y un ejemplo de URL.*

*Actividad que realizara el estudiante: explicar con sus palabras que ocurre cuando escribe `/recursos` en el navegador (ruta -> controlador -> vista).*

2.  **Retroalimentacion**

*Actividad: repaso de estructura y errores comunes (10 min).*

*Tiempo estimado: 10 minutos*

*Recursos: Material HTML Sesion 5 (`Material_Sesion_Clase_5_RUTAS/index.html`).*

*Actividad que realizara el estudiante: identificar 3 errores que ya han vivido (Whitelabel, 404, plantilla no encontrada) y escribir 1 causa probable de cada uno.*

3.  **Construccion del conocimiento (hands-on)**

***Actividad 1: Mapa MVC con rutas reales (15 min)***

*Tiempo estimado: 15 minutos*

*Recursos: seccion "Mapa MVC" del HTML de la sesion.*

*Actividad que realizara el estudiante: completar un mapa en 1 linea con las rutas `/recursos` y `/recursos/nuevo` y dibujar el flujo Vista -> Controlador -> Repositorio -> BD.*

*Evaluacion: preguntas rapidas (que metodo recibe GET, cual recibe POST).*

***Actividad 2: Anatomia de un Controlador (25 min)***

*Tiempo estimado: 25 minutos*

*Recursos: seccion "Imports y dependencias" del HTML.*

*Actividad que realizara el estudiante: explicar cada import con una frase corta. Ejemplo: `Model` = bolsa de datos para la vista. `@GetMapping` = ruta para mostrar una pagina.*

*Evaluacion: mini-explicacion oral (1 minuto por equipo).*

***Actividad 3: Formularios GET/POST paso a paso (35 min)***

*Tiempo estimado: 35 minutos*

*Recursos: seccion "Formulario conectado" del HTML + proyecto Spring Boot del equipo.*

*Actividad que realizara el estudiante: crear o reforzar el formulario con `th:object` y `th:field`, y enlazarlo con un metodo POST que guarda la entidad. Incluir validacion basica (required) y manejo de null en booleanos.*

*Evaluacion: evidencia de que el POST guarda y regresa a `/recursos`.*

***Actividad 4: Diagnostico guiado (15 min)***

*Tiempo estimado: 15 minutos*

*Recursos: checklist de errores en el HTML.*

*Actividad que realizara el estudiante: aplicar un proceso en 4 pasos ante un error simulado: 1) leer mensaje, 2) ubicar archivo, 3) revisar ruta y plantilla, 4) probar de nuevo.*

4.  **Aplicacion del conocimiento**

***Actividad 1: Mini-reto con rutas (25 min)***

*Tiempo estimado: 25 minutos*

*Recursos: HTML de la sesion.*

*Actividad que realizara el estudiante: agregar una ruta nueva `/recursos/ayuda` que muestre una vista con instrucciones de uso del CRUD. Explicar por que se agrego cada import y como se relaciona con MVC.*

*Evaluacion: vista funcional + explicacion de 5 lineas.*

5.  **Reflexion sobre mi proceso de aprendizaje**

*Actividad: "Como explicaria esto a un estudiante de secundaria".*

*Tiempo estimado: 10 minutos*

*Actividad que realizara el estudiante: redactar 1 analogia para explicar Controlador y 1 analogia para explicar Repositorio, sin usar palabras tecnicas.*

6.  **Introduccion al siguiente tema**

*Actividad: adelanto Semana 6 (persistencia y roles).*

*Tiempo estimado: 5 minutos*

*Actividad que realizara el estudiante: anotar que parte del CRUD quiere fortalecer antes de pasar a roles.*

7.  **Actividad de cierre y despedida**

*Actividad: ticket de salida.*

*Tiempo estimado: 5 minutos*

*Actividad que realizara el estudiante: escribir una micro-guia de 4 pasos para crear una ruta nueva en Spring Boot.
