# Plan docente de alto nivel — Sesion 5 (Rutas y Controladores)

## 1. Perfil del grupo y diagnostico rapido
- Perfil: docentes en formacion TIC con base tecnica inicial.
- Diagnostico de entrada (5 min): 3 preguntas orales
  1) Que es una ruta en una app web.
  2) Donde vive un template en Spring Boot.
  3) Que hace un Controller.
- Ajuste: si menos del 50% responde con claridad, extender 10 min la seccion de mapa MVC y estructura de archivos.

## 2. Resultados de aprendizaje (alineados a comprension linea por linea)
- El estudiante **explica cada linea** del Controller basico (anotaciones, metodos, Model, redirect) con lenguaje propio.
- El estudiante **identifica la funcion de cada archivo** del flujo MVC (controller, model, repository, templates, properties).
- El estudiante **describe por que existen los imports** y que error aparece si falta una dependencia.
- El estudiante **ejecuta un flujo completo**: abrir listado, abrir formulario, guardar y ver el registro.

## 3. Metodologia de alto impacto
- Aprendizaje guiado + practica incremental + evaluacion formativa.
- Micro-demostraciones de 7–10 min seguidas de micro-ejercicios de 10–15 min.
- Feedback inmediato con checklist visible y correccion sobre el codigo linea por linea.

## 4. Secuencia de aprendizaje (120–140 min)
1) Activacion (10 min): analogia de ruta como "puerta".
2) Estructura de archivos (15 min): ubicar cada carpeta y explicar su proposito.
3) Imports y dependencias (20 min): relacionar cada import con su efecto.
4) Demo guiada (40 min): rutas + formulario + guardado, explicando cada linea.
5) Practica en equipos (30 min): replicar flujo y documentar decisiones.
6) Diagnostico guiado (10–15 min): lectura de logs.
7) Cierre (5 min): ticket de salida.

## 5. Estandares y criterios de calidad (industria)
- Claridad de rutas: nombres consistentes, sin duplicidad.
- Separacion de responsabilidades: Controller coordina, Repository guarda.
- Validacion basica: required, manejo de null en booleanos.
- Redireccion post-guardado: evita reenvio de formulario.
- Evidencia reproducible: comandos y capturas.

## 6. Evidencias esperadas (aprendizaje funcional)
- Captura de /recursos con datos.
- Captura de /recursos/new.
- Registro guardado en lista.
- Explicacion breve del flujo en palabras propias.
- Mini-glosario: 6 imports y 4 dependencias con su proposito.

## 7. Estrategias de diferenciacion
- Estudiantes que avanzan rapido: agregar edit/delete o pagina /recursos/ayuda.
- Estudiantes con dificultades: trabajar solo GET + vista list.html primero.
- Parejas: una persona explica y la otra implementa.

## 8. Errores frecuentes y abordaje
- 404: revisar ruta + @RequestMapping.
- TemplateInputException: ruta en templates.
- Null en checkbox: explicar comportamiento del HTML.
- Dependencia faltante: revisar pom.xml.

## 9. Instrumentos de evaluacion
- Rubrica por criterios (ver rubrica_evaluacion.md).
- Pauta de observacion en clase (ver pauta_observacion.md).
- Entregable con evidencias (entregable_equipo.html).

## 10. Cierre reflexivo
- Pregunta: "Si un alumno no ve su vista, que le pides revisar primero?"
- Micro-reflexion escrita: 4 pasos para crear una ruta.
