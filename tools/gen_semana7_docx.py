#!/usr/bin/env python3
"""Genera los documentos .docx para la Semana 7 — Deploy en Render."""

from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _add_heading(doc, text, level=1):
    h = doc.add_heading(text, level=level)
    for run in h.runs:
        run.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)
    return h


def _add_table(doc, headers, rows):
    t = doc.add_table(rows=1 + len(rows), cols=len(headers))
    t.style = "Light Grid Accent 1"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, h in enumerate(headers):
        cell = t.rows[0].cells[i]
        cell.text = h
        for p in cell.paragraphs:
            for r in p.runs:
                r.bold = True
    for ri, row in enumerate(rows):
        for ci, val in enumerate(row):
            t.rows[ri + 1].cells[ci].text = str(val)
    return t


# ──────────────────────────────────────────
# SESIÓN DE CLASE 7
# ──────────────────────────────────────────
def gen_sesion():
    doc = Document()
    style = doc.styles["Normal"]
    style.font.name = "Calibri"
    style.font.size = Pt(11)

    # Header
    doc.add_paragraph("Universidad Rafael Landívar").alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.add_paragraph("Facultad de Humanidades — Departamento de Educación").alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.add_paragraph("")

    _add_heading(doc, "Sesión de Clase 7 — Despliegue (deploy) de la aplicación web", 1)

    # Info table
    _add_table(doc,
        ["Campo", "Detalle"],
        [
            ["Carrera", "PEM en TIC"],
            ["Curso", "Introducción al Desarrollo Web con Java"],
            ["Unidad / Semana", "Unidad 7 — Semana 7"],
            ["Modalidad", "Híbrida (presencial + sincrónica)"],
            ["Duración estimada", "120–150 minutos"],
            ["Herramientas", "VS Code, Terminal, Git, GitHub, Render (render.com)"],
        ],
    )

    doc.add_paragraph("")

    # Resultados de aprendizaje
    _add_heading(doc, "Resultados de aprendizaje de la sesión", 2)
    _add_table(doc,
        ["#", "Resultado de aprendizaje", "Evidencia"],
        [
            ["1", "Prepara el proyecto Spring Boot para producción (system.properties, application.properties)", "Archivos configurados correctamente"],
            ["2", "Ejecuta el flujo Git completo: add → commit → push", "Captura de terminal con push exitoso"],
            ["3", "Configura un Web Service en Render paso a paso", "Captura del dashboard con status Live"],
            ["4", "Verifica que la app funcione con una URL pública", "URL accesible desde navegador y celular"],
            ["5", "Diagnostica errores comunes de deploy leyendo logs", "Bitácora de errores (si hubo)"],
        ],
    )

    doc.add_paragraph("")

    # Secuencia didáctica
    _add_heading(doc, "Secuencia didáctica", 2)

    steps = [
        ("1. Activación (10 min)", [
            "Pregunta detonadora: '¿Tu app solo existe en tu computadora? ¿Qué pasa si se apaga?'",
            "Analogía: tu PC es tu cuaderno personal; deploy es fotocopiar y poner en un tablón público.",
            "Mostrar el mapa del deploy: Código → Commit → Push → Render → URL pública.",
            "Meta del día: que cada equipo tenga su app con una URL pública funcional.",
        ]),
        ("2. Preparar el proyecto (20 min)", [
            "Verificar que la app funciona en localhost:8080 sin errores.",
            "Crear system.properties en la raíz del proyecto: java.runtime.version=17",
            "Ajustar application.properties: server.port=${PORT:8080}, H2 en memoria, consola H2 habilitada.",
            "Explicar ${PORT:8080}: usa el puerto de Render si existe, o 8080 como respaldo.",
            "Verificar .gitignore (no subir target/, *.class, *.jar).",
        ]),
        ("3. Git: add → commit → push (25 min) — Demo en vivo", [
            "Proyectar terminal y ejecutar: git status → git add . → git commit -m '...' → git push origin main.",
            "Enfatizar: mensajes de commit descriptivos ('Preparar para deploy' sí; 'cambios' no).",
            "Cada equipo replica los comandos en su terminal.",
            "Usar la terminal simulada del index.html para equipos que no pueden ejecutar en vivo.",
            "Errores comunes: 'nothing to commit' (falta git add), 'permission denied' (token de GitHub).",
        ]),
        ("4. Configurar Render (30 min) — Demo guiada", [
            "Hacer la configuración en vivo frente al grupo, proyectando la pantalla.",
            "Dashboard → New + → Web Service → Build and deploy from Git repository.",
            "Conectar repositorio de GitHub, verificar que detecta Java.",
            "Configurar: Name, Branch (main), Build (./mvnw clean install -DskipTests), Start (java -jar target/*.jar), Plan (Free).",
            "Agregar variable de entorno: JAVA_TOOL_OPTIONS=-Xmx256m.",
            "Click 'Create Web Service' → esperar build (3-8 min) → leer logs juntos.",
            "Momento de celebración cuando el status sea Live → abrir URL en celular.",
        ]),
        ("5. Práctica en equipos (30–40 min)", [
            "Cada equipo replica el proceso con su propio proyecto.",
            "Usar cheatsheet como referencia rápida.",
            "Si el build falla: primero leer el log, luego consultar la sección de errores.",
            "No hacer por ellos: preguntar '¿Qué dice el mensaje?' antes de intervenir.",
            "Registrar URL pública y capturas en el entregable.",
        ]),
        ("6. Re-deploy: cambio + push (10–15 min)", [
            "Hacer un cambio pequeño (ej: cambiar un título en una vista).",
            "git add . → git commit -m '...' → git push origin main.",
            "Abrir Render → ver que el build arranca automáticamente.",
            "Verificar el cambio en la URL pública.",
            "Mensaje: 'Cada push es un deploy. Así funciona el desarrollo web real.'",
        ]),
        ("7. Cierre y reflexión (10 min)", [
            "Ticket de salida: cada equipo comparte su URL pública.",
            "Cada equipo menciona un error que tuvieron y cómo lo resolvieron.",
            "Frase de cierre: 'Deployar es como ______ porque ______.'",
            "Adelanto: Semana 8 — Seguridad, QA y mantenimiento (redeploy seguro).",
        ]),
    ]

    for title, items in steps:
        _add_heading(doc, title, 3)
        for item in items:
            doc.add_paragraph(item, style="List Bullet")
        doc.add_paragraph("")

    # Errores comunes
    _add_heading(doc, "Errores comunes de deploy y soluciones", 2)
    _add_table(doc,
        ["Error", "Causa", "Solución"],
        [
            ["UnsupportedClassVersionError", "Java incorrecto", "Crear system.properties con java.runtime.version=17"],
            ["Port 8080 in use", "Puerto fijo", "server.port=${PORT:8080}"],
            ["Memory exceeded (OOM)", "Mucha RAM", "JAVA_TOOL_OPTIONS=-Xmx256m"],
            ["mvnw: Permission denied", "Sin permisos", "git update-index --chmod=+x mvnw"],
            ["H2 lock error", "H2 en archivo", "Cambiar a jdbc:h2:mem:proddb"],
            ["App tarda ~30s", "Plan free 'duerme'", "Normal, esperar al primer acceso"],
        ],
    )

    doc.add_paragraph("")

    # Recursos
    _add_heading(doc, "Recursos y enlaces", 2)
    resources = [
        "Render — https://render.com",
        "Documentación Render para Java — https://docs.render.com/deploy-java",
        "Git reference — https://git-scm.com/docs",
        "Material interactivo — Material_Sesion_Clase_7_DEPLOY/index.html",
    ]
    for r in resources:
        doc.add_paragraph(r, style="List Bullet")

    path = os.path.join(BASE, "PEM en TIC_Sesion de Clase 7 Programacion I.docx")
    doc.save(path)
    print(f"✅ Sesión de Clase 7 → {path}")


# ──────────────────────────────────────────
# GUÍA DE APRENDIZAJE 7
# ──────────────────────────────────────────
def gen_guia():
    doc = Document()
    style = doc.styles["Normal"]
    style.font.name = "Calibri"
    style.font.size = Pt(11)

    doc.add_paragraph("Universidad Rafael Landívar").alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.add_paragraph("Facultad de Humanidades — Departamento de Educación").alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.add_paragraph("")

    _add_heading(doc, "Guía de Aprendizaje 7 — Despliegue (deploy) de la aplicación web", 1)

    # Info
    _add_table(doc,
        ["Campo", "Detalle"],
        [
            ["Carrera", "PEM en TIC"],
            ["Curso", "Introducción al Desarrollo Web con Java"],
            ["Unidad / Semana", "Unidad 7 — Semana 7"],
            ["Modalidad", "Trabajo autónomo + sesión práctica"],
            ["Horas estimadas", "10 horas (4 clase + 6 autónomo)"],
        ],
    )
    doc.add_paragraph("")

    # Resultados
    _add_heading(doc, "Resultados de aprendizaje", 2)
    _add_table(doc,
        ["#", "Resultado", "Indicador de logro"],
        [
            ["1", "Prepara archivos de configuración para producción", "system.properties y application.properties correctos"],
            ["2", "Ejecuta flujo Git completo (add, commit, push)", "Push exitoso visible en GitHub"],
            ["3", "Crea y configura un Web Service en Render", "Dashboard muestra status Live"],
            ["4", "Verifica y prueba la URL pública", "App accesible desde navegador y celular"],
            ["5", "Realiza un re-deploy tras hacer cambios", "Cambio visible en producción"],
        ],
    )
    doc.add_paragraph("")

    # Parte 1: Comprensión
    _add_heading(doc, "Parte 1 — Comprensión (antes de la práctica)", 2)

    _add_heading(doc, "Actividad 1.1 — Lectura guiada: ¿Qué es deploy?", 3)
    items_1_1 = [
        "Lee la sección 'Mapa del deploy' en Material_Sesion_Clase_7_DEPLOY/index.html.",
        "Responde: ¿Cuáles son los 6 pasos del deploy? Escríbelos con tus palabras.",
        "Crea una analogía propia: 'Deployar es como ______ porque ______.'",
    ]
    for i in items_1_1:
        doc.add_paragraph(i, style="List Bullet")

    _add_heading(doc, "Actividad 1.2 — Mapa de archivos", 3)
    items_1_2 = [
        "Dibuja o describe la estructura de archivos que necesita tu proyecto para ser deployado.",
        "Identifica cuáles archivos SON necesarios para Render y cuáles NO deben subirse.",
        "Responde: ¿Para qué sirve system.properties? ¿Qué pasa si no existe?",
        "Responde: ¿Qué significa server.port=${PORT:8080}?",
    ]
    for i in items_1_2:
        doc.add_paragraph(i, style="List Bullet")

    _add_heading(doc, "Actividad 1.3 — Comandos Git esenciales", 3)
    items_1_3 = [
        "Revisa la sección 'Git: Commit y Push' en index.html.",
        "Escribe el flujo de 3 comandos (add, commit, push) y explica cada uno.",
        "Practica con la terminal simulada del index.html hasta completar los 4 pasos.",
        "Escribe un ejemplo de un BUEN mensaje de commit y uno MALO. Explica la diferencia.",
    ]
    for i in items_1_3:
        doc.add_paragraph(i, style="List Bullet")
    doc.add_paragraph("")

    # Parte 2: Implementación
    _add_heading(doc, "Parte 2 — Implementación (práctica guiada)", 2)

    impl_steps = [
        ("Paso 1: Verificar localhost", "Ejecutar la app localmente. Confirmar que el CRUD funciona sin errores. Si hay errores, resolverlos antes de continuar."),
        ("Paso 2: Crear system.properties", "En la raíz del proyecto, crear el archivo con: java.runtime.version=17"),
        ("Paso 3: Ajustar application.properties", "Agregar server.port=${PORT:8080}. Cambiar H2 a memoria: jdbc:h2:mem:proddb. Habilitar consola H2 con web-allow-others=true."),
        ("Paso 4: Verificar .gitignore", "Confirmar que target/, *.class, *.jar, .idea/ están en .gitignore. Estos archivos NO deben subirse a GitHub."),
        ("Paso 5: Git add, commit, push", "Ejecutar: git add . → git commit -m 'Preparar proyecto para deploy' → git push origin main. Verificar en GitHub que los archivos están actualizados."),
        ("Paso 6: Crear Web Service en Render", "Crear cuenta en render.com con GitHub. New + → Web Service → conectar repositorio. Configurar Build Command, Start Command, Plan Free. Agregar JAVA_TOOL_OPTIONS=-Xmx256m."),
        ("Paso 7: Verificar y celebrar", "Esperar build (3-8 min). Cuando status sea Live, copiar URL. Abrir en navegador y celular. Crear un registro para verificar que funciona."),
        ("Paso 8: Re-deploy", "Hacer un cambio pequeño en el código. git add . → commit → push. Verificar que Render re-deploya automáticamente. Confirmar el cambio en la URL pública."),
    ]

    for title, desc in impl_steps:
        _add_heading(doc, title, 3)
        doc.add_paragraph(desc)

    doc.add_paragraph("")

    # Rúbrica
    _add_heading(doc, "Rúbrica de evaluación", 2)
    _add_table(doc,
        ["Criterio", "Puntos", "Descripción"],
        [
            ["Archivos de configuración", "20", "system.properties y application.properties correctos y funcionales"],
            ["Flujo Git completo", "20", "add, commit (con mensaje descriptivo) y push exitosos"],
            ["Configuración de Render", "20", "Web Service creado con Build/Start/Variables correctos"],
            ["URL pública funcional", "20", "App accesible, CRUD funcionando, probada en celular"],
            ["Explicación y reflexión", "20", "Explicación clara del proceso (8-12 líneas) + analogía"],
        ],
    )

    doc.add_paragraph("")
    doc.add_paragraph("Total: 100 puntos")

    # Cronograma
    _add_heading(doc, "Cronograma sugerido", 2)
    _add_table(doc,
        ["Actividad", "Modalidad", "Horas"],
        [
            ["Lectura y comprensión (Parte 1)", "Autónomo", "2"],
            ["Terminal simulada + quiz", "Autónomo", "1"],
            ["Sesión práctica (Parte 2, pasos 1-7)", "Presencial/sincrónica", "4"],
            ["Re-deploy y entregable", "Autónomo", "2"],
            ["Reflexión y analogía", "Autónomo", "1"],
        ],
    )

    doc.add_paragraph("")

    # Recursos
    _add_heading(doc, "Recursos", 2)
    resources = [
        "Material interactivo: Material_Sesion_Clase_7_DEPLOY/index.html",
        "Cheatsheet: Material_Sesion_Clase_7_DEPLOY/cheatsheet.html",
        "Ejercicios: Material_Sesion_Clase_7_DEPLOY/ejercicios.html",
        "Render: https://render.com",
        "Documentación Render para Java: https://docs.render.com/deploy-java",
        "Git documentation: https://git-scm.com/docs",
    ]
    for r in resources:
        doc.add_paragraph(r, style="List Bullet")

    path = os.path.join(BASE, "PEM en TIC_Guia de Aprendizaje 7 Programacion 1.docx")
    doc.save(path)
    print(f"✅ Guía de Aprendizaje 7 → {path}")


if __name__ == "__main__":
    gen_sesion()
    gen_guia()
    print("\n🎉 Documentos Semana 7 generados correctamente.")
