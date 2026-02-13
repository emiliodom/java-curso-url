+--------------------------------------------------------------------------+
| ### Universidad Rafael Landívar                                          |
|                                                                          |
| Facultad de Humanidades                                                  |
|                                                                          |
| Departamento de Educación                                                |
|                                                                          |
| **Guía de aprendizaje núm. 7**                                           |
|                                                                          |
| **Fecha de entrega: Viernes 11 de Octubre de 2024**                      |
|                                                                          |
| +----------------------------+-----------------------------------------+ |
| | Profesorados con           | Nombre del curso: Programación de       | |
| | Especialidad en TIC        | Aplicaciones Web                        | |
| |                            |                                         | |
| | **Año Psicopedagógico**    | Enfoque Pedagógico para Docentes       | |
| +============================+=========================================+ |
+--------------------------------------------------------------------------+

![Transformación Digital -- Universidad Rafael
Landívar](media/image1.png){width="3.2336996937882763in"
height="1.3760411198600175in"}![gráficos de color
degradado](media/image2.png){width="8.268055555555556in"
height="1.5618055555555554in"}

![Libro abierto](media/image4.svg){width="0.5729166666666666in"
height="0.5729166666666666in"}

**PARTE INTRODUCTORIA**

***\"Los datos son el corazón de las aplicaciones modernas, y como educadores, debemos enseñar a nuestros estudiantes a manejarlos con responsabilidad y creatividad.\" --- Filosofía de la era digital educativa***

+---------------------------------+------------------------------------+
| **Aprendizajes esperados**      | **Productos que evidencian el      |
|                                 | aprendizaje**                      |
+=================================+====================================+
| **Comprender los fundamentos de| *Plan de clase React conectado con |
| comunicación HTTP y gestión de | base de datos NocoDB, variables de |
| bases de datos para crear       | entorno configuradas, y documenta- |
| aplicaciones educativas         | ción del proceso de integración    |
| dinámicas y conectadas.**       | backend-frontend para otros        |
|                                 | docentes.*                         |
+---------------------------------+                                    |
| **Integrar servicios backend   |                                    |
| con aplicaciones frontend      |                                    |
| usando herramientas visuales y  |                                    |
| accesibles como NocoDB, con     |                                    |
| enfoque pedagógico para futuros |                                    |
| educadores TIC.**               |                                    |
+---------------------------------+------------------------------------+
| implementación inicial.**       |                                    |
+---------------------------------+------------------------------------+

+-----------------------------------------------------------------------+
| ![Libros](media/image6.svg){width="0.4895833333333333in"              |
| height="0.4895833333333333in"}**PRIMERA PARTE: FUNDAMENTOS HTTP Y     |
| NOCODB**                                                              |
|                                                                       |
| **Propósito de la actividad:** Comprender los conceptos fundamentales |
| de comunicación entre aplicaciones web (HTTP) y bases de datos        |
| visuales (NocoDB) usando analogías educativas familiares para futuros |
| docentes TIC.                                                         |
|                                                                       |
| **Actividades (Instrucciones):**                                      |
|                                                                       |
| 1.  **HTTP como "conversaciones digitales":**                         |
|                                                                       |
| - Comprensión de HTTP como protocolo de comunicación (conversación    |
|   entre aplicación web y servidor como diálogo estudiante-profesor)   |
|                                                                       |
| - Métodos HTTP básicos: GET (preguntar), POST (entregar tarea),       |
|   PUT (corregir tarea), DELETE (borrar contenido)                     |
|                                                                       |
| - Status codes como "respuestas del profesor": 200 (correcto),        |
|   404 (no encontrado), 500 (error del sistema)                       |
|                                                                       |
| 2.  **NocoDB como "cuaderno digital inteligente":**                   |
|                                                                       |
| - Instalación y configuración de NocoDB (interfaz visual para         |
|   gestionar bases de datos como hojas de cálculo)                     |
|                                                                       |
| - Creación de tabla "LessonPlans" con campos: título, objetivos,      |
|   actividades, recursos, tiempo estimado                              |
|                                                                       |
| - Comprensión de CORS como "permisos de acceso" entre aplicaciones    |
|                                                                       |
| - Configuración de webhooks como "notificaciones automáticas"         |
|                                                                       |
| **Recursos:**                                                         |
|                                                                       |
| **🗄️ NocoDB y Base de Datos:**                                        |
| - **NocoDB**: <https://nocodb.com/> - Base de datos visual            |
| - **HTTP Status Codes**: <https://httpstatuses.com/> - Referencia    |
| - **CORS Explained**: Configuración de permisos entre aplicaciones    |
|                                                                       |
| **🌐 Variables de Entorno:**                                          |
| - **dotenv**: Gestión segura de configuraciones sensibles             |
| - **Environment Variables**: Separación de configuración y código     |
|                                                                       |
| **Evaluación (Cualitativa o cuantitativa; formativa o sumativa):**    |
|                                                                       |
| Formativa: Verificación de instalación exitosa de NocoDB, creación    |
| de base de datos "LessonPlans", y comprensión de conceptos HTTP       |
| mediante explicaciones con analogías educativas.                      |
|                                                                       |
| Cualitativa: Evaluación del plan del sitio web y de la implementación |
| inicial, considerando la claridad, coherencia y la aplicación         |
| efectiva de tecnologías web.                                          |
+=======================================================================+

![Piezas de rompecabezas](media/image8.svg){width="0.5833333333333334in"
height="0.5833333333333334in"}

**SEGUNDA PARTE: INTEGRACIÓN FRONTEND-BACKEND**

1.  **Descripción del proyecto:** Conexión del plan de clase React
    (desarrollado en sesiones anteriores) con una base de datos NocoDB,
    implementando variables de entorno para configuración segura y
    operaciones CRUD básicas.

2.  **Fase del proyecto: Integración con datos dinámicos:** Transformar
    el plan de clase estático en una aplicación dinámica que almacene
    y recupere información desde una base de datos visual.

3.  **Actividades para desarrollar:**

    a.  **Configuración de variables de entorno:**
        - Creación de archivo .env para URLs de API, claves secretas
        - Configuración de VITE_API_URL para conexión con NocoDB
        - Uso de import.meta.env para acceder a variables en Vite
        - Manejo seguro de credenciales (qué NO subir a Git)

    b.  **Integración con NocoDB API:**
        - Conexión HTTP desde React usando fetch() o axios
        - Implementación de GET para obtener planes de clase
        - Implementación de POST para crear nuevos planes
        - Manejo de CORS y headers de autenticación

    c.  **Operaciones CRUD educativas:**
        - **Create**: Formulario para crear nuevo plan de clase
        - **Read**: Mostrar lista de planes existentes
        - **Update**: Editar plan seleccionado (feature opcional)
        - **Delete**: Eliminar plan con confirmación

    d.  **Features opcionales (mención breve):**
        - **Impresión**: react-to-print para generar PDF del plan
        - **Export**: Exportar a diferentes formatos (docx, excel)
        - **Edición en vivo**: Editor tipo Notion con react-quill
        - *Nota: Estas son funcionalidades avanzadas opcionales*

4.  **Evaluación:** Funcionamiento de conexión NocoDB, correcta
    configuración de variables de entorno, implementación exitosa de
    operaciones CRUD básicas, y documentación del proceso de integración.

![Cronómetro](media/image10.svg){width="0.5625in" height="0.5625in"}

**CRONOGRAMA**

  -----------------------------------------------------------------------
       **Actividad**         **Tiempo**           **Aprendizaje**
  ----------------------- ---------------- ------------------------------
    Instalación y           2 horas         Comprensión de HTTP, setup
   configuración de NocoDB                 de NocoDB, creación de base
   con conceptos HTTP                      de datos "LessonPlans"

   Configuración de         2 horas        Variables de entorno, dotenv,
   variables de entorno                    seguridad en configuraciones
   y conexión API NocoDB                   y primeras conexiones HTTP

   Implementación CRUD      4 horas        Operaciones Create, Read,
   básico (Create, Read)                   integración React-NocoDB,
                                          manejo de fetch y estados

   Testing de integración   1 hora         Verificación de conexión,
   y documentación                         troubleshooting CORS,
                                          documentación para otros
                                          docentes

   Features opcionales      1 hora         Exploración breve de
   (demostración)                          react-to-print, export
                                          options, editores en vivo

                          Total: 10 horas  
  -----------------------------------------------------------------------

![Libros en estantería](media/image12.svg){width="0.4895833333333333in"
height="0.4895833333333333in"}

**RECURSOS DE APOYO**

**🗄️ NocoDB y Base de Datos:**

- **NocoDB Documentation**: <https://docs.nocodb.com/> - Guía completa
  de instalación y configuración

- **HTTP Methods Guide**: <https://developer.mozilla.org/es/docs/Web/HTTP/Methods> -
  Referencia de métodos HTTP con ejemplos

- **CORS Explained**: <https://developer.mozilla.org/es/docs/Web/HTTP/CORS> -
  Configuración de permisos entre aplicaciones

**🔐 Variables de Entorno y Seguridad:**

- **Vite Environment Variables**: <https://vitejs.dev/guide/env-and-mode.html> -
  Configuración específica para Vite

- **dotenv Documentation**: Gestión segura de configuraciones sensibles

- **Git Security**: Qué archivos excluir del control de versiones

**⚡ Integración Frontend-Backend:**

- **Fetch API**: <https://developer.mozilla.org/es/docs/Web/API/Fetch_API> -
  Realizar peticiones HTTP desde React

- **Axios Alternative**: Librería popular para peticiones HTTP

- **React State Management**: Manejo de datos desde APIs externas

**📋 Features Opcionales (Referencia breve):**

- **react-to-print**: Generación de PDFs desde componentes React
- **file-saver + xlsx**: Export a Excel y otros formatos
- **react-quill**: Editor de texto enriquecido para edición en vivo
