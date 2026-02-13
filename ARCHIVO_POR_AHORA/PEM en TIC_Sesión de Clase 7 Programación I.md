+----------------------------------------------------------------------------------+
| ### Universidad Rafael Landívar                                                  |
|                                                                                  |
| Facultad de Humanidades                                                          |
|                                                                                  |
| Departamento de Educación                                                        |
|                                                                                  |
| +------------------------------------+-----------------------------------------+ |
| | ### Profesorados con Especialidad  | ### Nombre del curso: Programación de   | |
| | ### en TIC                         | ### Aplicaciones Web                     | |
| |                                    |                                         | |
| |                                    | Número de créditos: 4                   | |
| |                                    |                                         | |
| |                                    | Ciclo y módulo: Cuarto ciclo            | |
| +====================================+=========================================+ |
+----------------------------------------------------------------------------------+

![Transformación Digital -- Universidad Rafael
Landívar](media/image1.png){width="3.2336996937882763in"
height="1.3760411198600175in"}![gráficos de color
degradado](media/image2.png){width="8.268055555555556in"
height="1.5618055555555554in"}

**Secuencia de aprendizaje**

Sesión presencial/**[sincrónica]{.underline}** #7

+----------------+------------------------------------------------------------+
|                | ![Cabeza con                                               |
|                | engranajes](media/image4.svg){width="0.4583333333333333in" |
|                | height="0.4583333333333333in"}**Información importante**   |
+================+============================================================+
| **Aprendizajes | - Comprender y aplicar conceptos HTTP, métodos REST, y     |
| esperados**    |   configuración de bases de datos visuales con NocoDB.    |
|                |                                                            |
|                | - Integrar aplicaciones React con backends usando          |
|                |   variables de entorno y operaciones CRUD básicas.        |
|                |                                                            |
|                | - Desarrollar estrategias didácticas para enseñar          |
|                |   integración frontend-backend a futuros docentes TIC.    |
+----------------+------------------------------------------------------------+
| **Contenidos   | Fundamentos HTTP: GET, POST, status codes, CORS.          |
| temáticos**    |                                                            |
|                | NocoDB como base de datos visual y configuración de APIs.  |
|                |                                                            |
|                | Variables de entorno con Vite y seguridad en desarrollo.   |
|                |                                                            |
|                | Integración React-NocoDB con operaciones CRUD básicas.     |
|                |                                                            |
|                | Features opcionales: impresión, export, edición en vivo.   |
+----------------+------------------------------------------------------------+
| **Habilidades  | - Capacidad para configurar y gestionar bases de datos     |
| y destrezas**  |   visuales usando NocoDB con interfaz intuitiva.          |
|                |                                                            |
|                | - Habilidad para realizar peticiones HTTP desde React      |
|                |   usando fetch() o axios con manejo apropiado de errores.  |
|                |                                                            |
|                | - Destreza para configurar variables de entorno de forma   |
|                |   segura y manejar configuraciones sensibles.             |
+----------------+------------------------------------------------------------+
| **Valores y    | Responsabilidad en el manejo seguro de datos y variables   |
| actitudes**    | de configuración sensibles.                               |
|                |                                                            |
|                | Compromiso con las buenas prácticas de desarrollo         |
|                | backend-frontend y seguridad.                             |
|                |                                                            |
|                | Innovación en la aplicación de tecnologías de base de     |
|                | datos visuales para proyectos educativos.                 |
+----------------+------------------------------------------------------------+
| **Productos    | *Plan de clase React conectado con base de datos NocoDB,   |
| que evidencian | variables de entorno configuradas, operaciones CRUD        |
| el             | funcionando, y documentación del proceso de integración    |
| aprendizaje**  | para replicación por otros docentes.*                      |
+----------------+------------------------------------------------------------+

  -----------------------------------------------------------------------
  ![Internet](media/image6.svg){width="0.5104166666666666in"
  height="0.5104166666666666in"}**Desarrollo de la secuencia**
  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

1.  **Activación de presaberes**

*Actividad: Discusión sobre experiencias familiares con aplicaciones
que guardan datos (WhatsApp, redes sociales, Google Drive) y analogía
con cómo las aplicaciones web "conversan" con servidores para
almacenar información.*

*Tiempo estimado: 15 minutos*

*Recursos: Demostración visual de peticiones HTTP usando Chrome
DevTools en sitios web familiares como YouTube o Google.*

*Actividad que realizará el estudiante: Identificar aplicaciones que
usan en su vida diaria que requieren "conversación" con servidores
y reflexionar sobre el proceso de guardar/recuperar datos.*

2.  **Retroalimentación**

*Actividad: Preguntas y respuestas para conectar conceptos familiares
de aplicaciones móviles con desarrollo web y comunicación HTTP.*

*Tiempo estimado: 10 minutos*

*Recursos: Foro de discusión en el aula virtual.*

*Actividad que realizará el estudiante: Formular preguntas y resolver
dudas sobre los conceptos discutidos.*

3.  **Construcción del conocimiento**

***Actividad 1: Setup de NocoDB y Conceptos HTTP***

*Actividad: Instalación guiada de NocoDB usando analogías educativas
(base de datos como "cuaderno digital del aula"), configuración de
primera tabla "LessonPlans", y explicación de HTTP como "conversaciones"
entre aplicaciones.*

*Tiempo estimado: 40 minutos*

*Recursos: NocoDB instalado localmente o en la nube, Chrome DevTools
para visualizar peticiones HTTP, terminal para comandos básicos.*

*Actividad que realizará el estudiante: Instalar NocoDB, crear tabla
"LessonPlans" con campos básicos (título, objetivos, actividades),
explorar la API generada automáticamente, y comprender status codes
HTTP usando analogías de comunicación.*

*Evaluación: Verificación de instalación exitosa de NocoDB, creación
correcta de la tabla con campos apropiados, y comprensión demostrada
de conceptos HTTP básicos mediante explicaciones con analogías.*

***Actividad 2: Variables de Entorno y Primera Conexión***

*Actividad: Configuración de variables de entorno en proyecto Vite
React, creación de archivo .env con URL de NocoDB, y primera petición
HTTP usando fetch() para obtener datos de la tabla creada.*

*Tiempo estimado: 35 minutos*

*Recursos: Proyecto React existente (plan de clase de sesiones
anteriores), editor VS Code, documentación de Vite sobre variables
de entorno.*

*Actividad que realizará el estudiante: Crear archivo .env.local con
VITE_NOCODB_URL, configurar fetch básico para obtener datos, manejar
CORS si es necesario, y mostrar datos en componente React simple.*

*Evaluación: Funcionamiento correcto de conexión entre React y NocoDB,
configuración apropiada de variables de entorno, y implementación
exitosa de primera petición GET.*

4.  **Aplicación del conocimiento**

***Actividad 1: Implementación CRUD Completa***

*Actividad: Desarrollo individual donde los estudiantes implementan
operaciones CREATE y READ completas en su plan de clase React,
conectando formularios para crear nuevos planes y listas para
mostrar planes existentes desde NocoDB.*

*Tiempo estimado: 45 minutos*

*Recursos: Proyecto React con Framer Motion, NocoDB configurado,
VS Code, Chrome DevTools para debugging de peticiones HTTP.*

*Actividad que realizará el estudiante: Crear formulario React para
agregar planes de clase (POST), implementar lista de planes existentes
(GET), manejar estados de loading y error, y verificar funcionamiento
completo de integración.*

*Evaluación: Verificación de funcionamiento completo de operaciones
CRUD básicas, manejo apropiado de errores HTTP, y integración exitosa
entre frontend React y backend NocoDB.*

***Actividad 2: Documentación y Features Opcionales***

*Actividad: Presentación del plan de clase conectado con demostración
de operaciones CRUD, documentación del proceso de setup para otros
docentes, y exploración breve de features opcionales (impresión,
export, edición en vivo).*

*Tiempo estimado: 20 minutos*

*Recursos: Aplicación funcional, README.md creado, aula virtual para
compartir pantalla.*

*Actividad que realizará el estudiante: Demostrar plan de clase
conectado funcionando, explicar proceso de configuración de variables
de entorno, mostrar operaciones CRUD, y mencionar brevemente
posibilidades de extensión con features opcionales.*

*Evaluación: Calidad de la demostración, claridad en la documentación
para replicación, y comprensión de posibilidades de extensión del
proyecto.*

5.  **Reflexión sobre mi proceso de aprendizaje**

*Actividad: Reflexión escrita donde los estudiantes describen los
desafíos y aprendizajes clave sobre integración frontend-backend,
conceptos HTTP aprendidos, y potencial pedagógico de aplicaciones
conectadas con bases de datos.*

*Tiempo estimado: 10 minutos*

*Recursos: Plataforma de aula virtual para entregar la reflexión.*

*Actividad que realizará el estudiante: Redactar reflexión sobre
experiencia con NocoDB, comprensión de HTTP y CRUD, y ideas para
aplicar estos conceptos en contextos educativos futuros.*

*Evaluación: Evaluación cualitativa basada en comprensión de conceptos
técnicos y reflexión pedagógica sobre aplicación en aula.*

6.  **Introducción al siguiente tema**

*Actividad: Presentación breve sobre testing, quality assurance, y
preparación para proyecto final integrador con todas las tecnologías
aprendidas.*

*Tiempo estimado: 5 minutos*

*Recursos: Slides sobre testing en aplicaciones web, quality assurance
y metodologías de desarrollo.*

*Actividad que realizará el estudiante: Tomar notas sobre conceptos
de testing y reflexionar sobre importancia de quality assurance en
proyectos educativos.*

7.  **Actividad de cierre y despedida**

*Actividad: Recapitulación de conceptos HTTP, NocoDB, variables de
entorno, y espacio para preguntas finales sobre integración
frontend-backend.*

*Tiempo estimado: 5 minutos*

*Recursos: Resumen visual de conceptos aprendidos, foro de preguntas
en el aula virtual.*
virtual.*

*Actividad que realizará el estudiante: Formular preguntas finales y
resumir lo aprendido durante la sesión.*
