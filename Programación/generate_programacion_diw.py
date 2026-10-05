# -*- coding: utf-8 -*-
"""
Script generador de la Programación Didáctica actualizada y completa
del módulo profesional 'Diseño de Interfaces Web' (Código 0615) - 2º DAW
Comunidad Autónoma de Andalucía.

Genera:
1. Programación/Diseño_de_interfaces_web_2DAW_2025-2026.docx (Actualización directa)
2. Programación/Programacion_Didactica_DIW_2DAW_Andalucia.docx (Copia formal)
3. Programación/Programacion_Didactica_DIW_2DAW.md (Versión Markdown en Programación)
4. docs/programacion-didactica.md (Integración en portal de apuntes web)
"""

import os
import sys
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def build_diw_programacion():
    doc = docx.Document()
    
    # Page setup - Margins (Normal 2.5 cm = ~0.98 inches)
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(0.9)
        section.bottom_margin = Inches(0.9)
        section.left_margin = Inches(0.9)
        section.right_margin = Inches(0.9)
        
    # Styles config
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Calibri'
    normal_style.font.size = Pt(10)
    normal_style.font.color.rgb = RGBColor(0x1F, 0x29, 0x37)
    
    # Helper functions
    def set_cell_background(cell, fill_hex):
        tcPr = cell._element.get_or_add_tcPr()
        shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
        tcPr.append(shd)

    def set_cell_margins(cell, top=120, bottom=120, left=150, right=150):
        tcPr = cell._element.get_or_add_tcPr()
        tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
        tcPr.append(tcMar)

    def set_table_borders(table, color="D1D5DB", sz="4", val="single"):
        tblPr = table._element.xpath('w:tblPr')
        if tblPr:
            borders = parse_xml(
                f'<w:tblBorders {nsdecls("w")}>'
                f'<w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
                f'<w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
                f'<w:left w:val="none"/>'
                f'<w:right w:val="none"/>'
                f'<w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
                f'<w:insideV w:val="none"/>'
                f'</w:tblBorders>'
            )
            tblPr[0].append(borders)

    def add_callout(text_list, title="MARCO DESTACADO", bg_hex="F0FDF4", border_hex="16A34A", text_color=(0x16, 0x65, 0x34)):
        table = doc.add_table(rows=1, cols=1)
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        table.autofit = False
        table.columns[0].width = Inches(6.7)
        
        cell = table.cell(0, 0)
        set_cell_background(cell, bg_hex)
        set_cell_margins(cell, top=140, bottom=140, left=200, right=200)
        
        tcPr = cell._element.get_or_add_tcPr()
        borders = parse_xml(
            f'<w:tcBorders {nsdecls("w")}>'
            f'<w:top w:val="none"/>'
            f'<w:left w:val="single" w:sz="24" w:space="0" w:color="{border_hex}"/>'
            f'<w:bottom w:val="none"/>'
            f'<w:right w:val="none"/>'
            f'</w:tcBorders>'
        )
        tcPr.append(borders)
        
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.15
        run_title = p.add_run(f"📌 {title}\n")
        run_title.bold = True
        run_title.font.name = "Calibri"
        run_title.font.size = Pt(10)
        run_title.font.color.rgb = RGBColor(*text_color)
        
        for idx, line in enumerate(text_list):
            if idx > 0:
                p = cell.add_paragraph()
                p.paragraph_format.space_before = Pt(2)
                p.paragraph_format.space_after = Pt(2)
                p.paragraph_format.line_spacing = 1.15
            r = p.add_run(line)
            r.font.name = "Calibri"
            r.font.size = Pt(9.5)
            r.font.color.rgb = RGBColor(0x1F, 0x29, 0x37)
        
        p_after = doc.add_paragraph()
        p_after.paragraph_format.space_before = Pt(2)
        p_after.paragraph_format.space_after = Pt(4)

    def heading_1(text):
        p = doc.add_paragraph()
        p.paragraph_format.keep_with_next = True
        p.paragraph_format.space_before = Pt(18)
        p.paragraph_format.space_after = Pt(6)
        r = p.add_run(text)
        r.font.name = "Calibri"
        r.font.size = Pt(14.5)
        r.bold = True
        r.font.color.rgb = RGBColor(0x0F, 0x4C, 0x81) # Deep Indigo/Blue
        return p

    def heading_2(text):
        p = doc.add_paragraph()
        p.paragraph_format.keep_with_next = True
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(4)
        r = p.add_run(text)
        r.font.name = "Calibri"
        r.font.size = Pt(12)
        r.bold = True
        r.font.color.rgb = RGBColor(0x02, 0x84, 0xC7) # Sky Blue / Ocean
        return p

    def heading_3(text):
        p = doc.add_paragraph()
        p.paragraph_format.keep_with_next = True
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(2)
        r = p.add_run(text)
        r.font.name = "Calibri"
        r.font.size = Pt(10.5)
        r.bold = True
        r.font.color.rgb = RGBColor(0x37, 0x41, 0x51) # Slate Gray
        return p

    def body_p(text, bold_prefix=None, space_after=4):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            r_pre = p.add_run(bold_prefix)
            r_pre.bold = True
            r_pre.font.name = "Calibri"
            r_pre.font.size = Pt(10)
            r_pre.font.color.rgb = RGBColor(0x1F, 0x29, 0x37)
        r = p.add_run(text)
        r.font.name = "Calibri"
        r.font.size = Pt(10)
        r.font.color.rgb = RGBColor(0x1F, 0x29, 0x37)
        return p

    def bullet_p(text, bold_prefix=None):
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            r_pre = p.add_run(bold_prefix)
            r_pre.bold = True
            r_pre.font.name = "Calibri"
            r_pre.font.size = Pt(10)
            r_pre.font.color.rgb = RGBColor(0x1F, 0x29, 0x37)
        r = p.add_run(text)
        r.font.name = "Calibri"
        r.font.size = Pt(10)
        r.font.color.rgb = RGBColor(0x1F, 0x29, 0x37)
        return p

    def styled_table(headers, data, col_widths=None, header_bg="0F4C81", header_fg=(0xFF, 0xFF, 0xFF)):
        table = doc.add_table(rows=len(data) + 1, cols=len(headers))
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        table.autofit = False
        
        # Header
        hdr_cells = table.rows[0].cells
        for i, title in enumerate(headers):
            hdr_cells[i].text = title
            set_cell_background(hdr_cells[i], header_bg)
            set_cell_margins(hdr_cells[i], top=120, bottom=120, left=140, right=140)
            p = hdr_cells[i].paragraphs[0]
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            for run in p.runs:
                run.font.name = "Calibri"
                run.font.size = Pt(9.5)
                run.font.bold = True
                run.font.color.rgb = RGBColor(*header_fg)
                
        # Data rows
        for row_idx, row_data in enumerate(data):
            row_cells = table.rows[row_idx + 1].cells
            bg_color = "F9FAFB" if row_idx % 2 == 1 else "FFFFFF"
            for col_idx, cell_value in enumerate(row_data):
                row_cells[col_idx].text = str(cell_value)
                set_cell_background(row_cells[col_idx], bg_color)
                set_cell_margins(row_cells[col_idx], top=100, bottom=100, left=140, right=140)
                p = row_cells[col_idx].paragraphs[0]
                p.paragraph_format.space_before = Pt(0)
                p.paragraph_format.space_after = Pt(0)
                p.paragraph_format.line_spacing = 1.1
                for run in p.runs:
                    run.font.name = "Calibri"
                    run.font.size = Pt(9)
                    run.font.color.rgb = RGBColor(0x1F, 0x29, 0x37)
                    
        # Column widths
        if col_widths:
            for i, col in enumerate(table.columns):
                w = Inches(col_widths[i])
                for cell in col.cells:
                    cell.width = w
                    
        set_table_borders(table)
        
        p_after = doc.add_paragraph()
        p_after.paragraph_format.space_before = Pt(2)
        p_after.paragraph_format.space_after = Pt(4)
        return table

    # -------------------------------------------------------------
    # PORTADA Y ENCABEZADO
    # -------------------------------------------------------------
    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_before = Pt(24)
    p_title.paragraph_format.space_after = Pt(4)
    p_title.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p_title.add_run("PROGRAMACIÓN DIDÁCTICA")
    r.bold = True
    r.font.size = Pt(22)
    r.font.color.rgb = RGBColor(0x0F, 0x4C, 0x81)

    p_sub = doc.add_paragraph()
    p_sub.paragraph_format.space_before = Pt(0)
    p_sub.paragraph_format.space_after = Pt(8)
    p_sub.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = p_sub.add_run("Módulo Profesional: Diseño de Interfaces Web (Código 0615)")
    r_sub.bold = True
    r_sub.font.size = Pt(13)
    r_sub.font.color.rgb = RGBColor(0x02, 0x84, 0xC7)

    p_cycles = doc.add_paragraph()
    p_cycles.paragraph_format.space_before = Pt(0)
    p_cycles.paragraph_format.space_after = Pt(16)
    p_cycles.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_c = p_cycles.add_run("Ciclo Formativo de Grado Superior: Desarrollo de Aplicaciones Web (DAW)\nSegundo Curso · Familia Profesional: Informática y Comunicaciones\nComunidad Autónoma de Andalucía · Curso Académico 2025 / 2026")
    r_c.font.size = Pt(11)
    r_c.font.color.rgb = RGBColor(0x4B, 0x55, 0x63)

    # Tabla Ficha Técnica del Módulo
    info_headers = ["Elemento", "Especificación y Datos del Módulo"]
    info_data = [
        ["Denominación oficial", "Diseño de Interfaces Web"],
        ["Código oficial del módulo", "0615 (Real Decreto 687/2010 y Orden de 16 de junio de 2011)"],
        ["Ciclo formativo y curso", "2º curso de Técnico Superior en Desarrollo de Aplicaciones Web (DAW)"],
        ["Carga horaria total", "175 horas totales (5 horas semanales durante el periodo lectivo en centro + fase dual en empresa)"],
        ["Equivalencia crediticia", "9 créditos ECTS (Grado Superior)"],
        ["Régimen de impartición", "Formación Profesional Grado D - Régimen Dual General (400 horas totales de empresa en 2º curso)"],
        ["Departamento didáctico", "Departamento de Informática y Comunicaciones"],
        ["Repositorio y Materiales de aula", "Carpeta digital del módulo: apuntes estructurados en 23 unidades en docs/"]
    ]
    styled_table(info_headers, info_data, col_widths=[2.3, 4.4], header_bg="0F4C81")

    # -------------------------------------------------------------
    # 1. INTRODUCCIÓN Y JUSTIFICACIÓN PEDAGÓGICA
    # -------------------------------------------------------------
    heading_1("1. INTRODUCCIÓN Y JUSTIFICACIÓN PEDAGÓGICA DEL MÓDULO")
    body_p("El módulo profesional de Diseño de Interfaces Web (Código 0615) se imparte en el segundo curso del Ciclo Formativo de Grado Superior de Desarrollo de Aplicaciones Web (DAW), perteneciente a la familia profesional de Informática y Comunicaciones, con una carga lectiva de 175 horas totales (a razón de 5 horas semanales durante el periodo lectivo en el centro educativo complementado con la fase de formación en empresa).")
    body_p("En el desarrollo de aplicaciones web actual, la interfaz de usuario (UI) y la experiencia de usuario (UX) constituyen el punto de convergencia crítico entre la lógica del negocio y el usuario final. Un desarrollo técnicamente sólido en backend carece de impacto si la interfaz resulta confusa, inaccesible, lenta o visualmente deficiente.")
    
    add_callout([
        "El módulo capacita al futuro Técnico Superior en DAW para:",
        "1. Dominar los principios de psicología cognitiva y comunicación visual (Leyes de Gestalt, jerarquía visual, teoría del color y tipografía adaptativa).",
        "2. Diseñar prototipos profesionales e interactivos mediante Figma y construir Sistemas de Diseño (Design Systems y Design Tokens) escalables.",
        "3. Maquetar con HTML5 semántico y CSS moderno avanzado (Flexbox, CSS Grid Layout, Container Queries, variables CSS, metodologías BEM/ITCSS, preprocesadores Sass y frameworks utility-first como Tailwind CSS 4).",
        "4. Integrar y optimizar contenido multimedia de última generación (WebP, AVIF, SVG interactivo, audio/vídeo HTML5) respetando la legislación sobre derechos de autor y licencias.",
        "5. Desarrollar Single Page Applications (SPA) dinámicas y reactivas empleando frameworks frontend modernos basados en componentes (Angular).",
        "6. Garantizar la accesibilidad web universal conforme a las directivas WCAG 2.1 / 2.2 (niveles A, AA y AAA) y WAI-ARIA (RD 1112/2018), así como aplicar auditorías heurísticas de usabilidad (Nielsen, métricas SUS y Core Web Vitals)."
    ], title="Propósito Formativo y Competencial de Diseño de Interfaces Web")

    body_p("La programación didáctica está compaginada de forma exhaustiva con el banco de apuntes, prácticas y código disponible en las 23 unidades temáticas de la carpeta docs/ del módulo.")

    # -------------------------------------------------------------
    # 2. MARCO NORMATIVO VIGENTE
    # -------------------------------------------------------------
    heading_1("2. MARCO NORMATIVO VIGENTE")
    body_p("La programación didáctica se fundamenta y ajusta estrictamente a la siguiente jerarquía normativa estatal, autonómica andaluza y sectorial:")

    heading_2("2.1 Normativa General del Sistema Educativo y Formación Profesional")
    bullet_p("Garantiza el derecho fundamental a la educación y el libre desarrollo de la personalidad.", "Constitución Española de 1978 (Artículo 27): ")
    bullet_p("Marco regulador de las enseñanzas no universitarias, con las modificaciones introducidas por la Ley Orgánica 3/2020 (LOMLOE) en materia de digitalización, diseño universal y equidad educativa.", "Ley Orgánica 2/2006, de 3 de mayo, de Educación (LOE / LOMLOE): ")
    bullet_p("Establece el marco legal unificado del Sistema de FP y el carácter dual de las ofertas formativas de Grado D.", "Ley Orgánica 3/2022, de 31 de marzo, de ordenación e integración de la FP: ")
    bullet_p("Desarrolla la ordenación del Sistema de Formación Profesional (estructura de Grados D, régimen dual y resultados de aprendizaje).", "Real Decreto 659/2023, de 18 de julio: ")
    bullet_p("Establece el título de Técnico Superior en Desarrollo de Aplicaciones Web y fija sus enseñanzas mínimas.", "Real Decreto 687/2010, de 20 de mayo: ")
    bullet_p("Por los que se actualizan determinados reales decretos de títulos de FP, consolidando las adaptaciones tecnológicas y curriculares en DAW.", "Real Decreto 405/2023 y Real Decreto 500/2024: ")

    heading_2("2.2 Normativa Autonómica de la Comunidad Autónoma de Andalucía")
    bullet_p("Garantizan el derecho a la educación permanente y la adecuación de la FP a las necesidades del tejido productivo andaluz.", "Estatuto de Autonomía para Andalucía (Ley Orgánica 2/2007) - Artículos 21 y 52: ")
    bullet_p("Marco legal educativo propio de Andalucía.", "Ley 17/2007, de 10 de diciembre, de Educación de Andalucía (LEA): ")
    bullet_p("Regula la ordenación de las enseñanzas del Sistema de FP en Andalucía, estableciendo el régimen dual y la autonomía pedagógica de los centros educativos (deroga el Decreto 436/2008).", "Decreto 104/2024, de 28 de mayo: ")
    bullet_p("Regula con carácter preceptivo la evaluación criterial, continua, formativa y colegiada, así como las convocatorias y titulación en Grados D y E en Andalucía (deroga la Orden de 29 de septiembre de 2010).", "Orden de 18 de septiembre de 2025: ")
    bullet_p("Regula la organización y desarrollo de la fase de formación en empresa u organismo equiparado en los centros docentes andaluces.", "Orden de 26 de septiembre de 2025: ")
    bullet_p("Desarrolla el currículo del título de Técnico Superior en DAW en la Comunidad Autónoma de Andalucía.", "Orden de 16 de junio de 2011: ")
    bullet_p("Reglamento Orgánico de los IES y normas de organización y funcionamiento de centros docentes en Andalucía.", "Decreto 327/2010, de 13 de julio, y Orden de 20 de agosto de 2010: ")

    heading_2("2.3 Normativa Específica de Accesibilidad, Propiedad Intelectual y Protección de Datos")
    bullet_p("Exige la accesibilidad de sitios web y aplicaciones móviles del sector público y servicios de interés general (trasposición de la Directiva UE 2016/2102).", "Real Decreto 1112/2018, de 7 de septiembre (Accesibilidad Web): ")
    bullet_p("Trasposición de directivas europeas en materia de accesibilidad de determinados productos y servicios (Acta Europea de Accesibilidad).", "Ley 11/2023, de 8 de mayo: ")
    bullet_p("Regula los derechos de autor, explotación de software, contenidos multimedia y licencias de distribución (Creative Commons, GPL, MIT, Apache).", "Real Decreto Legislativo 1/1996 (Ley de Propiedad Intelectual - TRLPI): ")
    bullet_p("Regulan la privacidad por diseño, el tratamiento lícito de datos y la garantía de derechos digitales en interfaces web y formularios.", "Reglamento (UE) 2016/679 (RGPD) y Ley Orgánica 3/2018 (LOPDGDD): ")

    # -------------------------------------------------------------
    # 3. CONTEXTO DEL GRUPO DE ALUMNADO
    # -------------------------------------------------------------
    heading_1("3. CONTEXTO DEL GRUPO DE ALUMNADO (2º DAW)")
    body_p("El grupo de 2º curso de Desarrollo de Aplicaciones Web está compuesto por 9 alumnos/as procedentes de Martos y localidades adyacentes de la comarca (Torredelcampo, Fuensanta de Martos, Jaén capital):")
    bullet_p("Edades comprendidas entre 18 y 31 años, con perfiles motivados y orientados a la inserción laboral inmediata o a la especialización técnica.", "Distribución etaria: ")
    bullet_p("La mayor parte del grupo promocionó directamente desde 1º DAW con todos los módulos superados. Existen 2 alumnos repetidores: uno con dedicación exclusiva al módulo de proyecto y asignaturas pendientes con seguimiento individualizado; y otro en proceso de reincorporación.", "Trayectoria académica previa: ")
    bullet_p("Dos alumnos cuentan con convalidación oficial del módulo de Itinerario Personal para la Empleabilidad II (IPE II).", "Convalidaciones: ")
    bullet_p("El grupo presenta un nivel competencial sólido pero heterogéneo en frontend. No se registran informes formales de NEAE en el expediente de orientación, si bien se aplican medidas preventivas de refuerzo y ampliación basadas en el Diseño Universal para el Aprendizaje (DUA).", "Atención a la diversidad: ")

    # -------------------------------------------------------------
    # 4. OBJETIVOS GENERALES Y COMPETENCIAS
    # -------------------------------------------------------------
    heading_1("4. OBJETIVOS GENERALES Y COMPETENCIAS DEL TÍTULO")
    body_p("De acuerdo con la Orden de 16 de junio de 2011 y el Real Decreto 687/2010, el módulo de Diseño de Interfaces Web contribuye directamente a los siguientes objetivos generales y competencias profesionales:")

    heading_2("4.1 Objetivos Generales del Ciclo Vinculados al Módulo")
    bullet_p("Utilizar lenguajes de marcas y estándares web, asumiendo el manual de estilo, para desarrollar interfaces en aplicaciones web.", "i) Estándares y estilos: ")
    bullet_p("Emplear herramientas y lenguajes específicos, siguiendo las especificaciones, para desarrollar componentes multimedia.", "j) Componentes multimedia: ")
    bullet_p("Evaluar la interactividad, accesibilidad y usabilidad de una interfaz, verificando los criterios preestablecidos, para integrar componentes multimedia en la interfaz de una aplicación.", "k) Evaluación UX/UI: ")
    bullet_p("Utilizar herramientas y lenguajes específicos para desarrollar e integrar componentes software en el entorno del servidor y cliente web.", "l) Integración de componentes: ")
    bullet_p("Verificar los componentes software desarrollados, analizando las especificaciones, para completar el plan de pruebas de la interfaz.", "ñ) Verificación y testing: ")
    bullet_p("Utilizar herramientas específicas para elaborar y mantener la documentación técnica y guías de estilo.", "o) Documentación: ")
    bullet_p("Identificar y proponer las acciones profesionales necesarias para dar respuesta a la accesibilidad universal y al diseño para todos.", "y) Accesibilidad universal: ")

    heading_2("4.2 Competencias Profesionales, Personales y Sociales")
    bullet_p("Desarrollar interfaces en aplicaciones web de acuerdo con un manual de estilo, utilizando lenguajes de marcas y estándares web (g).", "Competencia en maquetación y estilos: ")
    bullet_p("Desarrollar e integrar componentes multimedia en la interfaz de una aplicación web, realizando el análisis de interactividad, accesibilidad y usabilidad (h, i).", "Competencia multimedia e interactiva: ")
    bullet_p("Desarrollar aplicaciones web estructuradas por componentes reutilizables, reactivas y orientadas al consumo de servicios y APIs (e, f, j, k, l).", "Desarrollo frontend por componentes: ")
    bullet_p("Completar planes de pruebas de usabilidad, contraste y accesibilidad, y documentar técnicamente los sistemas de diseño (m, n).", "Calidad y verificación técnica: ")

    # -------------------------------------------------------------
    # 5. RESULTADOS DE APRENDIZAJE Y CRITERIOS DE EVALUACIÓN
    # -------------------------------------------------------------
    heading_1("5. RESULTADOS DE APRENDIZAJE Y CRITERIOS DE EVALUACIÓN")
    body_p("A continuación se detallan los 6 Resultados de Aprendizaje oficiales fijados por la Orden de 16 de junio de 2011 para el módulo de Diseño de Interfaces Web, junto con sus Criterios de Evaluación y el peso porcentual asignado a cada uno:")

    ra_headers = ["RA", "Resultado de Aprendizaje Oficial", "Criterios de Evaluación Oficiales (CE)", "Pond. Total"]
    ra_data = [
        [
            "RA1",
            "Planifica la creación de una interfaz web valorando y aplicando especificaciones de diseño.",
            "a) Se ha reconocido la importancia de la comunicación visual y sus principios básicos.\nb) Se han analizado y seleccionado los colores y tipografías adecuados para pantalla.\nc) Se han analizado alternativas para la presentación de información web.\nd) Se ha valorado la importancia de definir y aplicar la guía de estilo.\ne) Se han utilizado y valorado distintas tecnologías para el diseño web.\nf) Se han creado y utilizado plantillas y prototipos de diseño.",
            "12 %\n(2% / CE)"
        ],
        [
            "RA2",
            "Crea interfaces web homogéneos definiendo y aplicando estilos.",
            "a) Se han reconocido las posibilidades de modificar las etiquetas HTML.\nb) Se han definido estilos de forma directa.\nc) Se han definido y asociado estilos globales en hojas externas.\nd) Se han definido hojas de estilos alternativas.\ne) Se han redefinido estilos.\nf) Se han identificado las distintas propiedades de cada elemento.\ng) Se han creado clases y selectores de estilos.\nh) Se han utilizado herramientas de validación de hojas de estilos.\ni) Se han analizado y utilizado tecnologías y frameworks para diseño responsive.\nj) Se han analizado y utilizado preprocesadores de estilos (Sass/SCSS).",
            "20 %\n(2% / CE)"
        ],
        [
            "RA3",
            "Prepara archivos multimedia para la web, analizando sus características y manejando herramientas específicas.",
            "a) Se han reconocido las implicaciones de licencias y derechos de autor.\nb) Se han identificado formatos de imagen, audio y vídeo a utilizar (WebP, AVIF, SVG).\nc) Se han analizado herramientas para generar contenido multimedia.\nd) Se han empleado herramientas para el tratamiento digital de la imagen.\ne) Se han utilizado herramientas para manipular audio y vídeo.\nf) Se han realizado animaciones a partir de imágenes fijas.\ng) Se han importado y exportado recursos multimedia en diversos formatos.\nh) Se ha aplicado la guía de estilo al material multimedia.",
            "16 %\n(2% / CE)"
        ],
        [
            "RA4",
            "Integra contenido multimedia en documentos web valorando su aportación y seleccionando adecuadamente los elementos interactivos.",
            "a) Se han reconocido tecnologías de inclusión de contenido interactivo (2%).\nb) Se han configurado navegadores para contenido multimedia e interactivo (2%).\nc) Se han utilizado herramientas gráficas para contenido interactivo (4%).\nd) Se ha analizado el código generado por herramientas interactivas (4%).\ne) Se han agregado elementos multimedia a documentos web (4%).\nf) Se ha añadido interactividad a elementos web (4%).\ng) Se ha verificado el funcionamiento interactivo en múltiples dispositivos (4%).",
            "24 %\n(Pond. diferenciada)"
        ],
        [
            "RA5",
            "Desarrolla interfaces web accesibles, analizando las pautas establecidas y aplicando técnicas de verificación.",
            "a) Se ha reconocido la necesidad de diseñar webs accesibles.\nb) Se ha analizado la accesibilidad de diferentes documentos web.\nc) Se han analizado los principios y pautas WCAG y niveles de conformidad.\nd) Se han analizado los posibles errores según prioridades de verificación.\ne) Se ha alcanzado el nivel de conformidad deseado (Nivel AA/AAA).\nf) Se han verificado los niveles mediante tests automatizados.\ng) Se ha verificado la visualización en múltiples navegadores y tecnologías asistivas.\nh) Se han utilizado herramientas que mejoren la visibilidad y accesibilidad (SEO/ARIA).",
            "16 %\n(2% / CE)"
        ],
        [
            "RA6",
            "Desarrolla interfaces web amigables analizando y aplicando las pautas de usabilidad establecidas.",
            "a) Se ha analizado la usabilidad de diferentes documentos web.\nb) Se ha valorado la importancia de los estándares en la creación web.\nc) Se ha adecuado la interfaz web a los objetivos y usuarios destinatarios.\nd) Se ha verificado la facilidad de navegación mediante diversos periféricos.\ne) Se han analizado técnicas para verificar la usabilidad de un documento web.\nf) Se ha verificado la usabilidad en diferentes navegadores y dispositivos.",
            "12 %\n(2% / CE)"
        ]
    ]
    styled_table(ra_headers, ra_data, col_widths=[0.6, 2.2, 3.2, 0.7], header_bg="0F4C81")

    # -------------------------------------------------------------
    # 6. ORGANIZACIÓN Y SECUENCIACIÓN DE UNIDADES DIDÁCTICAS
    # (COMPAGINADAS CON LOS MATERIALES DE DOCS/)
    # -------------------------------------------------------------
    heading_1("6. SECUENCIACIÓN DIDÁCTICA Y COMPAGINACIÓN CON LOS APUNTES DEL MÓDULO")
    body_p("Para dar una respuesta coherente y estructurada a los 6 Resultados de Aprendizaje y aprovechar al máximo los 23 documentos de apuntes preparados en la carpeta docs/, los contenidos se secuencian en 6 Unidades de Trabajo (UT) agrupadas temporalmente en los dos trimestres lectivos en centro educativo (previos a la fase intensiva de formación en empresa):")

    # UT 1
    heading_2("6.1 TRIMESTRE 1 · UT 1: Fundamentos de UI/UX, Psicología del Diseño, Color, Tipografía, Sistemas de Diseño y Prototipado en Figma (30 horas)")
    body_p("Esta unidad aborda las bases de la comunicación visual, los modelos mentales del usuario, la arquitectura de la información y la creación de prototipos profesionales de alta fidelidad.")
    bullet_p("Percepción visual y psicología cognitiva: Leyes de Gestalt (proximidad, semejanza, continuidad, cierre, figura-fondo). Leyes de UX: Ley de Fitts, Ley de Hick, Ley de Miller, Ley de Jakob y Efecto de Estética-Usabilidad. Carga cognitiva y modelos mentales.", "Contenidos Teóricos: ")
    bullet_p("Teoría del color en pantallas: Espacios de color (RGB, HSL, HWB, Oklch), psicología del color, armonías, ratios de contraste WCAG (4.5:1 para texto normal, 3:1 para texto grande/componentes). Tipografía web: anatomía, familias tipográficas, escalas modulares (Type Scale), jerarquía visual, legibilidad (leading, tracking, line-length) y fuentes variables (Variable Fonts).", "Color y Tipografía: ")
    bullet_p("Guías de estilo y Design Systems: Metodología Atomic Design (átomos, moléculas, organismos, plantillas, páginas). Design Tokens (colores, espaciados, tipografías, elevaciones) y documentación en Storybook/Zeroheight.", "Design Systems: ")
    bullet_p("Figma profesional: Creación de Frames, Layout Grids, Auto Layout avanzado con flexión y wrap, componentes reutilizables, variantes (Variants y Component Properties), constraints responsivos, variables de diseño, prototipado interactivo con animaciones Smart Animate y exportación de assets para desarrollo.", "Herramientas de Prototipado: ")
    bullet_p("Arquitectura de la Información (AI): Jerarquía de contenidos, árboles de navegación, flujos de usuario (User Flows), técnicas de Card Sorting (abierto/cerrado) y diseño de Wireframes (baja, media y alta fidelidad).", "Arquitectura de Información: ")
    
    bullet_p("docs/index.md (Unidad 1: Introducción al Diseño de Interfaces Web).", "Materiales vinculados en docs/: ")
    bullet_p("docs/02-psicologia-diseno.md (Psicología Cognitiva y Leyes UX).", " ")
    bullet_p("docs/03-color-tipografia.md (Teoría del Color, Contraste y Tipografía Web).", " ")
    bullet_p("docs/04-guias-estilo-design-systems.md (Design Systems y Atomic Design).", " ")
    bullet_p("docs/05-figma-profesional.md (Figma Avanzado, Auto Layout y Prototipado).", " ")
    bullet_p("docs/06-arquitectura-informacion.md (Arquitectura de Información y Wireframes).", " ")

    add_callout([
        "• Tarea Integradora UT1: Creación completa del Sistema de Diseño y Prototipo Interactivo de Alta Fidelidad en Figma para una aplicación web (incluyendo Design Tokens, componentes con variantes, Auto Layout y flujo de navegación navegable).",
        "• RAs y Criterios Evaluados: RA1 (a, b, c, d, e, f) y RA6 (b, c)."
    ], title="Proyecto / Tarea Práctica Bloque 1")

    # UT 2
    heading_2("6.2 TRIMESTRE 1 · UT 2: Maquetación Web Profesional: HTML5 Semántico, CSS Avanzado, Flexbox, Grid y Responsive Design (35 horas)")
    body_p("Esta unidad transforma las especificaciones de diseño en código web robusto, modular, semántico y perfectamente adaptado a cualquier dispositivo y resolución.")
    bullet_p("HTML5 Semántico: Estructura de documentos (<header>, <nav>, <main>, <article>, <section>, <aside>, <footer>), elementos de texto, formularios accesibles, metadatos, Open Graph y microdatos Schema.org para SEO técnico.", "HTML5 Semántico: ")
    bullet_p("CSS Profesional: Modelo de caja (Box Model, box-sizing), flujo normal, posicionamiento, cascada, especificidad, herencia y capas de cascada (@layer). Variables CSS nativas (Custom Properties) para temas dinámicos (Dark/Light mode). Metodologías de arquitectura CSS (BEM - Block Element Modifier, ITCSS).", "CSS Moderno: ")
    bullet_p("Maquetación Unidimensional con Flexbox: Flex container, flex items, ejes principal y cruzado (justify-content, align-items, align-content), flex-grow, flex-shrink, flex-basis y alineaciones dinámicas.", "Flexbox: ")
    bullet_p("Maquetación Bidimensional con CSS Grid Layout: Grid container, pistas explícitas e implícitas, grid-template-columns/rows, fr units, minmax(), repeat(), auto-fill vs auto-fit, grid-template-areas y alineación de áreas complejas.", "CSS Grid: ")
    bullet_p("Responsive Web Design: Estrategia Mobile-First, Viewport meta tag, Media Queries modernas (range syntax), Container Queries (@container) para componentes intrínsecamente adaptables, e imágenes responsivas (<picture>, srcset, sizes).", "Responsive Design: ")
    bullet_p("Preprocesadores y Frameworks CSS: Preprocesadores Sass/SCSS (variables, nesting, mixins, funciones, modularización con @use y @forward). Frameworks CSS Utility-First: Tailwind CSS 4 (configuración moderna, directivas @theme, utilidades de espaciado, tipografía y responsive design).", "Sass y Tailwind CSS: ")

    bullet_p("docs/07-html-semantico.md (HTML5 Semántico, Accesibilidad y SEO).", "Materiales vinculados en docs/: ")
    bullet_p("docs/08-css-profesional.md (CSS Profesional, Cascada y Metodología BEM).", " ")
    bullet_p("docs/09-flexbox.md (Flexbox - Maquetación Unidimensional).", " ")
    bullet_p("docs/10-css-grid-layout.md (CSS Grid Layout y Áreas).", " ")
    bullet_p("docs/11-responsive-design.md (Diseño Responsive, Mobile First y Container Queries).", " ")
    bullet_p("docs/17-tailwindcss4.md (Tailwind CSS 4 - Fundamentos y Práctica).", " ")
    bullet_p("docs/18-preprocesadores-css.md (Preprocesadores CSS - SASS/SCSS y LESS).", " ")

    add_callout([
        "• Tarea Integradora UT2: Maquetación web completa y responsive de una interfaz web compleja a partir de un diseño en Figma, utilizando HTML5 semántico, CSS Grid + Flexbox, Custom Properties, preprocesador Sass y maquetación alternativa con Tailwind CSS 4.",
        "• RAs y Criterios Evaluados: RA2 (a, b, c, d, e, f, g, h, i, j)."
    ], title="Proyecto / Tarea Práctica Bloque 2")

    # UT 3
    heading_2("6.3 TRIMESTRE 1 / 2 · UT 3: Multimedia Web, Optimización de Activos, Derechos de Autor y Licencias (20 horas)")
    body_p("Esta unidad capacita para la preparación, procesamiento, compresión e integración técnica de recursos multimedia en la web, así como para la gestión ética y legal de contenidos digitales.")
    bullet_p("Formatos de imagen para la web: Mapas de bits (JPEG, PNG, WebP, AVIF) vs gráficos vectoriales (SVG). Estructura del SVG: viewBox, paths, optimización con SVGO y manipulación con CSS/JS. Técnicas de compresión con y sin pérdidas. Lazy loading nativo (loading='lazy').", "Formatos y Optimización de Imagen: ")
    bullet_p("Audio y Vídeo HTML5: Contenedores y códecs (MP4/H.264, WebM/VP9, AV1, MP3, AAC, Ogg). Etiquetas <audio> y <video>, atributos (controls, autoplay, muted, loop, playsinline). Pistas de texto y subtítulos sincronizados con formato WebVTT (<track> kind='subtitles/captions') para accesibilidad.", "Audio y Vídeo: ")
    bullet_p("Marco Legal y Propiedad Intelectual: Real Decreto Legislativo 1/1996 (TRLPI), derechos morales y patrimoniales. Licencias Creative Commons (CC BY, SA, NC, ND, CC0/Dominio Público). Licencias de software libre y código abierto (MIT, Apache 2.0, GPL, BSD). Banco de recursos multimedia libres (Unsplash, Freepik, Google Fonts). Privacidad y derechos de imagen en la web.", "Marco Legal y Licencias: ")

    bullet_p("docs/12-multimedia-web.md (Integración de Contenido Multimedia en la Web).", "Materiales vinculados en docs/: ")
    bullet_p("docs/19-marco-legal-multimedia.md (Marco Legal Multimedia, Derechos de Autor y Licencias).", " ")

    add_callout([
        "• Tarea Integradora UT3: Creación de un catálogo multimedia optimizado con imágenes responsivas en formato AVIF/WebP, iconos SVG interactivos accesibles y reproductor de vídeo accesible con subtítulos WebVTT y auditoría de licencias legales.",
        "• RAs y Criterios Evaluados: RA3 (a, b, c, d, e, f, g, h)."
    ], title="Proyecto / Tarea Práctica Bloque 3")

    # UT 4
    heading_2("6.4 TRIMESTRE 2 · UT 4: Interactividad, Animaciones y Desarrollo Frontend por Componentes con Framework (Angular) (55 horas)")
    body_p("Esta unidad profundiza en la interactividad web avanzada y en la arquitectura de aplicaciones SPA (Single Page Applications) construidas mediante el framework Angular.")
    bullet_p("Interactividad y Microinteracciones CSS/JS: Transiciones CSS (timing functions, bezier curves), animaciones con @keyframes, transformaciones 2D/3D. Manipulación del DOM mediante JavaScript moderno, eventos de ratón, teclado, touch y scroll. Web Animations API.", "Animaciones e Interactividad: ")
    bullet_p("Introducción a Angular y Componentes Standalone: Arquitectura del framework, Angular CLI, TypeScript para frontend, estructura de componentes Standalone (imports, selector, templateUrl, styleUrl), ciclo de vida del componente (ngOnInit, ngOnDestroy).", "Angular - Componentes: ")
    bullet_p("Data Binding y Control de Flujo: Interpolación {{ }}, Property Binding [ ], Event Binding ( ), Two-way Binding [(ngModel)]. Nuevas directivas de control de flujo en templates (@if, @else, @for con track, @switch). Signals de Angular para reactividad moderna. Pipes nativos y personalizados.", "Data Binding y Signals: ")
    bullet_p("Servicios, Inyección de Dependencias y Consumo de APIs: Inyección de dependencias (@Injectable, providedIn: 'root'), HttpClientModule / provideHttpClient(), programación reactiva con RxJS (Observables, operadores map, filter, catchError), consumo de APIs REST y manejo de estados de carga/error en UI.", "Servicios y HttpClient: ")
    bullet_p("Enrutamiento y Formularios Reactivos: Angular Router (RouterModule, rutas, parámetros, rutas hijas, Lazy Loading de componentes, Guards). Formularios Reactivos (ReactiveFormsModule, FormGroup, FormControl, FormBuilder), validaciones sincrónicas y asincrónicas, y retroalimentación visual de errores en UI.", "Routing y Formularios: ")

    bullet_p("docs/13-interactividad-web.md (Interactividad Web, Transiciones y Animaciones).", "Materiales vinculados en docs/: ")
    bullet_p("docs/20-angular-introduccion.md (Angular - Introducción y Primeros Componentes).", " ")
    bullet_p("docs/21-angular-componentes-datos.md (Angular - Data Binding, Directivas y Signals).", " ")
    bullet_p("docs/22-angular-servicios-httpclient.md (Angular - Servicios, HttpClient y RxJS).", " ")
    bullet_p("docs/23-angular-routing-formularios.md (Angular - Enrutamiento y Formularios Reactivos).", " ")

    add_callout([
        "• Proyecto Integrador Frontend (Angular): Desarrollo de una Single Page Application (SPA) completa en Angular compuesta por múltiples componentes Standalone, navegación mediante Angular Router, consumo de servicios API REST remotos con HttpClient, microinteracciones visuales y formularios reactivos con validación en tiempo real.",
        "• RAs y Criterios Evaluados: RA4 (a, b, c, d, e, f, g) y RA2 (i)."
    ], title="Proyecto / Tarea Práctica Bloque 4")

    # UT 5
    heading_2("6.5 TRIMESTRE 2 · UT 5: Accesibilidad Web Universal (WCAG 2.1/2.2, WAI-ARIA) y Validación Técnica (20 horas)")
    body_p("Esta unidad capacita para asegurar que las aplicaciones web sean plenamente utilizables por todas las personas, incluidas aquellas con discapacidades visuales, auditivas, motrices o cognitivas.")
    bullet_p("Fundamentos y Principios de Accesibilidad: Consorcio W3C, Iniciativa de Accesibilidad Web (WAI). Principios WCAG (POUR: Perceptible, Operable, Comprensible, Robusto). Niveles de conformidad: A, AA y AAA.", "Principios WCAG: ")
    bullet_p("Criterios de Éxito y Puntos de Verificación: Texto alternativo (alt), contraste de color, redimensionamiento de texto, navegación por teclado completa sin trampas de foco, indicadores de foco visibles, tiempo suficiente, encabezados lógicos, etiquetas de formulario y gestión de errores.", "Pautas de Verificación: ")
    bullet_p("WAI-ARIA (Accessible Rich Internet Applications): Roles (role='banner', 'navigation', 'alert', 'dialog'), estados y propiedades (aria-expanded, aria-hidden, aria-live, aria-describedby, aria-label) para enriquecer componentes dinámicos de Angular/JS.", "WAI-ARIA: ")
    bullet_p("Técnicas y Herramientas de Verificación: Auditorías automatizadas (axe DevTools, Lighthouse Accessibility, WAVE, Colour Contrast Analyser). Pruebas manuales con lectores de pantalla (NVDA en Windows, VoiceOver en macOS/iOS). Marco legal: Real Decreto 1112/2018 y Ley 11/2023.", "Auditoría de Accesibilidad: ")

    bullet_p("docs/14-accesibilidad-web.md (Accesibilidad Web, WCAG 2.2, WAI-ARIA y Auditorías).", "Materiales vinculados en docs/: ")
    bullet_p("docs/07-html-semantico.md (Landmarks semánticos y accesibilidad).", " ")

    add_callout([
        "• Tarea Integradora UT5: Auditoría técnica y remediación de accesibilidad de una aplicación web real, alcanzando la conformidad WCAG 2.2 Nivel AA, aplicando WAI-ARIA en componentes interactivos y redactando un informe de conformidad formal según el RD 1112/2018.",
        "• RAs y Criterios Evaluados: RA5 (a, b, c, d, e, f, g, h)."
    ], title="Proyecto / Tarea Práctica Bloque 5")

    # UT 6
    heading_2("6.6 TRIMESTRE 2 · UT 6: Usabilidad Web, Métricas UX, Heurísticas y Diseño Centrado en el Usuario (DCU) (15 horas)")
    body_p("Esta unidad analiza la eficacia, eficiencia y satisfacción del usuario final con la interfaz mediante metodologías formales de evaluación y pruebas de usuario.")
    bullet_p("Principios de Usabilidad y Evaluación Heurística: Las 10 Heurísticas de Usabilidad de Jakob Nielsen (visibilidad del estado del sistema, correspondencia con el mundo real, control y libertad del usuario, consistencia y estándares, prevención de errores, reconocimiento antes que recuerdo, flexibilidad, estética minimalista, diagnóstico de errores y ayuda).", "Heurísticas de Nielsen: ")
    bullet_p("Métricas de Rendimiento y Experiencia de Usuario: System Usability Scale (SUS), Net Promoter Score (NPS), tasa de éxito de tareas, tiempo en tarea y Core Web Vitals de Google (LCP - Largest Contentful Paint, INP - Interaction to Next Paint, CLS - Cumulative Layout Shift).", "Métricas UX y Rendimiento: ")
    bullet_p("Metodología de Diseño Centrado en el Usuario (DCU / Design Thinking): Etapas de Empatizar (User Personas, Empathy Maps), Definir (User Journey Maps), Idear, Prototipar y Testear. Conducción de pruebas de usabilidad con usuarios reales, protocolos 'Think Aloud' y matrices de hallazgos.", "Diseño Centrado en Usuario: ")

    bullet_p("docs/15-usabilidad-web.md (Usabilidad Web, Heurísticas de Nielsen y Pruebas).", "Materiales vinculados en docs/: ")
    bullet_p("docs/16-diseno-centrado-usuario.md (Diseño Centrado en el Usuario y Design Thinking).", " ")

    add_callout([
        "• Tarea Integradora UT6: Evaluación heurística y test de usabilidad con usuarios de una aplicación web, medición de puntuación SUS y Core Web Vitals, y propuesta justificada de rediseño de interfaz.",
        "• RAs y Criterios Evaluados: RA6 (a, b, c, d, e, f)."
    ], title="Proyecto / Tarea Práctica Bloque 6")

    # -------------------------------------------------------------
    # 7. METODOLOGÍA DIDÁCTICA Y PRINCIPIOS PEDAGÓGICOS
    # -------------------------------------------------------------
    heading_1("7. METODOLOGÍA DIDÁCTICA Y PRINCIPIOS PEDAGÓGICOS")
    body_p("La metodología de enseñanza-aprendizaje en el aula de 2º DAW se basa en los principios de aprendizaje significativo, aprendizaje constructivista y desarrollo orientado a proyectos reales:")
    bullet_p("Se simulan dinámicas de trabajo reales de agencias frontend: desde la fase de ideación y prototipado en Figma, pasando por el maquetado CSS profesional, hasta el desarrollo de componentes SPA en Angular y la auditoría final de accesibilidad.", "Aprendizaje Basado en Proyectos (ABP): ")
    bullet_p("Todas las sesiones en el aula de informática combinan explicaciones conceptuales breves con la inmediata codificación práctica en el editor de código (Visual Studio Code, Figma, navegadores con DevTools).", "Enfoque Práctico (Learning by Doing): ")
    bullet_p("Se promueve el uso de control de versiones con Git/GitHub, la modularidad mediante componentes y la aplicación de buenas prácticas (código limpio, semántico, accesible y performante).", "Cultura de Desarrollo Profesional: ")
    bullet_p("Plataforma Moodle Centros / Google Classroom como entorno de gestión de contenidos, entrega de prácticas, cuestionarios técnicos y comunicación telemática continua.", "Entorno Virtual de Aprendizaje: ")

    # -------------------------------------------------------------
    # 8. EVALUACIÓN Y CALIFICACIÓN
    # -------------------------------------------------------------
    heading_1("8. EVALUACIÓN, INSTRUMENTOS Y CRITERIOS DE CALIFICACIÓN")
    body_p("De acuerdo con el Decreto 104/2024, de 28 de mayo, y la Orden de 18 de septiembre de 2025 de la Junta de Andalucía, la evaluación en Formación Profesional es continua, formativa, criterial e integradora.")

    heading_2("8.1 Instrumentos y Procedimientos de Evaluación")
    bullet_p("Prácticas de maquetación, ejercicios de Figma, componentes interactivos y auditorías realizadas durante las sesiones de aula (40% de la calificación del periodo).", "1. Prácticas y Tareas de Laboratorio de cada Unidad (40%): ")
    bullet_p("Desarrollo de un proyecto web completo que aglutina el diseño en Figma, maquetación responsive, integración multimedia, desarrollo de componentes Angular y verificación de accesibilidad, incluyendo defensa oral individual (40% de la calificación).", "2. Proyecto Web Frontend Integrador y Defensa Oral (40%): ")
    bullet_p("Pruebas escritas y ejercicios prácticos de desarrollo en tiempo limitado para comprobar la adquisición autónoma y rigurosa de los criterios de evaluación (20% de la calificación).", "3. Pruebas Objetivas y Supuestos Prácticos (20%): ")

    heading_2("8.2 Criterios de Calificación y Superación del Módulo")
    bullet_p("La calificación de cada evaluación parcial reflejará el grado de consecución ponderado de los Criterios de Evaluación trabajados hasta esa fecha.", "Evaluaciones Parciales: ")
    bullet_p("Para superar el módulo profesional, es imprescindible que la media ponderada de los Criterios de Evaluación de cada uno de los 6 Resultados de Aprendizaje (RA1 a RA6) sea igual o superior a 5,0 puntos sobre 10.", "Superación Criterial Obligatoria: ")
    bullet_p("La nota final del módulo en la evaluación final ordinaria será la media aritmética ponderada de todos los criterios evaluados, redondeada a número entero de 1 a 10.", "Calificación Final Ordinaria: ")

    heading_2("8.3 Procedimientos de Recuperación Continua y Extraordinaria")
    bullet_p("El alumnado que no alcance la calificación mínima en las prácticas o proyectos dispondrá de actividades de refuerzo y reentrega corregida con defensa individual antes de la sesión de evaluación ordinaria.", "Recuperación Continua: ")
    bullet_p("En caso de no superar el módulo en la convocatoria ordinaria de mayo, el alumnado realizará una prueba práctica extraordinaria en junio centrada exclusivamente en los Resultados de Aprendizaje no superados.", "Convocatoria Extraordinaria: ")

    # -------------------------------------------------------------
    # 9. FORMACIÓN EN EMPRESA U ORGANISMO EQUIPARADO (RÉGIMEN DUAL EN 2º DAW)
    # -------------------------------------------------------------
    heading_1("9. FORMACIÓN EN EMPRESA U ORGANISMO EQUIPARADO (RÉGIMEN DUAL EN 2º DAW)")
    body_p("En cumplimiento de la Ley Orgánica 3/2022, el Real Decreto 659/2023, el Decreto 104/2024 y la Orden de 26 de septiembre de 2025 de la Junta de Andalucía, el ciclo de DAW se imparte en modalidad dual general:")
    body_p("En el segundo curso, el alumnado realiza un total de 400 horas de formación en empresas tecnológicas colaboradoras (50 jornadas laborales de 8 horas), distribuidas entre los módulos formativos de segundo curso según el plan de formación del centro:")

    dual_headers = ["Módulo Profesional", "Horas Totales", "Horas en Centro", "Horas en Empresa (Dual)"]
    dual_data = [
        ["Desarrollo Web en Entorno Servidor (DWES)", "245 h", "145 h", "100 h"],
        ["Desarrollo Web en Entorno Cliente (DWEC)", "210 h", "124 h", "86 h"],
        ["Diseño de Interfaces Web (DIW)", "175 h", "104 h", "71 h"],
        ["Despliegue de Aplicaciones Web (DAW)", "70 h", "41 h", "29 h"],
        ["Módulo Optativo", "105 h", "62 h", "43 h"],
        ["Inglés Profesional", "70 h", "41 h", "29 h"],
        ["Itinerario Personal para la Empleabilidad II (IPE II)", "105 h", "62 h", "43 h"],
        ["TOTAL HORAS 2º CURSO (+70h Proyecto)", "1.050 h", "579 h", "400 h (50 jornadas)"]
    ]
    styled_table(dual_headers, dual_data, col_widths=[2.7, 1.2, 1.3, 1.5], header_bg="0F4C81")

    heading_2("9.1 Resultados de Aprendizaje y Criterios Desarrollados en Empresa")
    body_p("Durante la estancia dual en la empresa colaboradora, el módulo de Diseño de Interfaces Web desarrollará y consolidará especialmente los siguientes Resultados de Aprendizaje y Criterios de Evaluación en proyectos reales:")
    bullet_p("b) Selección de colores y tipografías corporativas; c) Presentación de información en interfaces reales; e) Utilización de tecnologías de diseño web de la empresa; f) Creación y mantenimiento de plantillas y componentes.", "RA1 (Planificación y diseño de interfaces): ")
    bullet_p("a) Modificación y optimización de HTML; b) Aplicación de estilos; e) Redefinición y refactorización de estilos CSS; f) Propiedades avanzadas de maquetación; h) Validación y linters de estilos; i) Uso de frameworks CSS y diseño responsive en producción.", "RA2 (Creación de interfaces homogéneos y estilos): ")
    bullet_p("Integración de componentes frontend en frameworks (Angular/React/Vue) y verificación de accesibilidad y usabilidad con clientes y usuarios finales.", "RA4, RA5 y RA6 (Interactividad y calidad): ")

    # -------------------------------------------------------------
    # 10. ATENCIÓN A LA DIVERSIDAD Y DISEÑO UNIVERSAL PARA EL APRENDIZAJE (DUA)
    # -------------------------------------------------------------
    heading_1("10. ATENCIÓN A LA DIVERSIDAD Y DISEÑO UNIVERSAL PARA EL APRENDIZAJE (DUA)")
    body_p("Se aplican los principios del Diseño Universal para el Aprendizaje (DUA) para garantizar el éxito educativo de todo el alumnado:")
    bullet_p("Proporcionar código fuente de ejemplo, vídeos explicativos, documentación técnica oficial (MDN, Angular docs), diagramas de arquitectura y resúmenes conceptuales.", "Múltiples formas de representación: ")
    bullet_p("Permitir entregas con diferentes niveles de complejidad, proyectos personalizados según intereses del alumno (e-commerce, portales educativos, dashboards) y opciones de frameworks.", "Múltiples formas de acción y expresión: ")
    bullet_p("Conectar los contenidos con las demandas reales del mercado laboral, trabajo cooperativo y aprendizaje basado en retos.", "Múltiples formas de implicación: ")

    heading_2("10.1 Medidas Concretas para el Grupo")
    bullet_p("Guías paso a paso, descomposiciones de tareas complejas en micro-hitos y sesiones de apoyo guiado en el laboratorio.", "Alumnado con ritmos más lentos o dificultades: ")
    bullet_p("Retos avanzados de programación frontend (creación de directivas y pipes personalizados en Angular, optimización de renderizado con OnPush y Signals, arquitecturas CSS avanzadas y micro-frontends).", "Alumnado aventajado / Altas capacidades: ")
    bullet_p("Seguimiento a través de la plataforma virtual (Moodle), material online 100% disponible (`docs/`), flexibilidad justificada en plazos de entrega y tutorías telemáticas.", "Alumnado trabajador o con régimen modular: ")
    bullet_p("Atención individualizada para la coordinación del proyecto y asignaturas pendientes, adaptando el calendario de entregas.", "Alumnado repetidor: ")

    # -------------------------------------------------------------
    # 11. ELEMENTOS TRANSVERSALES Y PROYECTO LINGÜÍSTICO DE CENTRO
    # -------------------------------------------------------------
    heading_1("11. ELEMENTOS TRANSVERSALES Y PROYECTO LINGÜÍSTICO DE CENTRO")
    body_p("En cumplimiento de los artículos 39 y 40 de la Ley 17/2007 (LEA) y del Real Decreto 659/2023:")
    bullet_p("El módulo sitúa el Diseño para Todos y la Accesibilidad Web Universal (WCAG / WAI-ARIA) en el centro de la práctica profesional, garantizando que el software no excluya a personas con discapacidades.", "Accesibilidad Universal y No Discriminación: ")
    bullet_p("Fomento de la presencia de mujeres en el desarrollo frontend y visibilización de referentes femeninos en diseño UX/UI y programación web.", "Igualdad de Género: ")
    bullet_p("Sensibilización en el respeto a los derechos de autor, licencias abiertas y cumplimiento de normativas de privacidad y cookies (RGPD/LOPDGDD).", "Propiedad Intelectual y Privacidad: ")
    bullet_p("Optimización de transferencias de red, compresión de activos multimedia y reducción de la huella de carbono digital en servidores web (Green Web Design).", "Sostenibilidad y Transición Ecológica: ")
    bullet_p("Lectura y redacción de documentación técnica en español e inglés (especificaciones W3C, MDN, Angular.io). Se exigirá corrección ortográfica y gramatical en memorias y proyectos (descuento formativo de 0,2 por falta hasta un máximo de 2 puntos con opción de corrección).", "Proyecto Lingüístico de Centro (PLC): ")

    # -------------------------------------------------------------
    # 12. ACTIVIDADES COMPLEMENTARIAS Y EXTRAESCOLARES
    # -------------------------------------------------------------
    heading_1("12. ACTIVIDADES COMPLEMENTARIAS Y EXTRAESCOLARES")
    body_p("Se prevén las siguientes actividades complementarias y extraescolares:")
    bullet_p("Visitas a empresas de desarrollo de software, estudios de diseño UX/UI y consultoras tecnológicas del entorno andaluz (Parque Tecnológico Geolit en Jaén, PTA Málaga, Cartuja en Sevilla).", "Visitas a Empresas Tecnológicas: ")
    bullet_p("Participación en conferencias, eventos de desarrolladores (Google Developer Groups, jornadas de software libre) y webinars con expertos en frontend y accesibilidad web.", "Jornadas Técnicas y Encuentros Frontend: ")
    bullet_p("Encuentros con antiguos alumnos/as de DAW que trabajan actualmente como desarrolladores frontend o ingenieros de interfaz.", "Mesa Redonda con Egresados: ")

    # -------------------------------------------------------------
    # 13. RECURSOS DIDÁCTICOS, BIBLIOGRAFÍA Y MATERIALES DEL MÓDULO
    # -------------------------------------------------------------
    heading_1("13. RECURSOS DIDÁCTICOS, BIBLIOGRAFÍA Y MATERIALES DEL MÓDULO")
    body_p("El desarrollo formativo se fundamenta en los 23 documentos de apuntes y prácticas alojados en la carpeta docs/ del módulo:")

    docs_headers = ["Unidad / Doc", "Título del Recurso en docs/", "Contenido y Enfoque Profesional"]
    docs_data = [
        ["01 (index.md)", "01. Introducción al Diseño de Interfaces Web", "Fundamentos de UI/UX, ergonomía digital, herramientas y flujo de trabajo frontend."],
        ["02", "02-psicologia-diseno.md", "Psicología cognitiva, Leyes de Gestalt, Leyes de UX (Fitts, Hick, Miller, Jakob) y modelos mentales."],
        ["03", "03-color-tipografia.md", "Teoría del color, espacios de color modernos (Oklch), ratios WCAG, jerarquía tipográfica y fuentes variables."],
        ["04", "04-guias-estilo-design-systems.md", "Sistemas de diseño, Atomic Design, Design Tokens y documentación de componentes."],
        ["05", "05-figma-profesional.md", "Figma avanzado: Frames, Auto Layout, Componentes, Variantes, Variables y prototipado Smart Animate."],
        ["06", "06-arquitectura-informacion.md", "Arquitectura de información, árboles de contenido, User Flows, Card Sorting y Wireframes."],
        ["07", "07-html-semantico.md", "HTML5 semántico, landmarks accesibles, microdatos Schema.org y SEO técnico."],
        ["08", "08-css-profesional.md", "CSS profesional, Box Model, cascada, especificidad, Custom Properties y metodología BEM."],
        ["09", "09-flexbox.md", "Maquetación unidimensional con Flexbox, propiedades del contenedor y de los items."],
        ["10", "10-css-grid-layout.md", "Maquetación bidimensional con CSS Grid, pistas, áreas, auto-fit/auto-fill y alineaciones."],
        ["11", "11-responsive-design.md", "Diseño responsive Mobile-First, Media Queries, Container Queries e imágenes responsivas (<picture>)."],
        ["12", "12-multimedia-web.md", "Integración de multimedia: WebP, AVIF, SVG interactivo, audio/vídeo HTML5 y subtítulos WebVTT."],
        ["13", "13-interactividad-web.md", "Interactividad web, transiciones CSS, keyframes, eventos DOM y animaciones JavaScript."],
        ["14", "14-accesibilidad-web.md", "Accesibilidad web universal, pautas WCAG 2.1/2.2 (A/AA/AAA), WAI-ARIA, tests automáticos y lectores."],
        ["15", "15-usabilidad-web.md", "Usabilidad web, las 10 heurísticas de Nielsen, métricas SUS, Core Web Vitals y pruebas de usuario."],
        ["16", "16-diseno-centrado-usuario.md", "Metodología DCU y Design Thinking: User Personas, Empathy Maps y Customer Journey Maps."],
        ["17", "17-tailwindcss4.md", "Tailwind CSS 4: Enfoque Utility-First, configuración moderna, directivas @theme y responsive design."],
        ["18", "18-preprocesadores-css.md", "Preprocesadores CSS: Sass/SCSS y LESS, variables, anidamiento, mixins, funciones y @use/@forward."],
        ["19", "19-marco-legal-multimedia.md", "Marco legal multimedia: TRLPI, licencias Creative Commons, licencias de software, RGPD y privacidad."],
        ["20", "20-angular-introduccion.md", "Angular: Arquitectura por componentes Standalone, TypeScript, Angular CLI y ciclo de vida."],
        ["21", "21-angular-componentes-datos.md", "Angular: Data Binding, directivas de control (@if, @for, @switch), Signals y Pipes."],
        ["22", "22-angular-servicios-httpclient.md", "Angular: Inyección de dependencias, Servicios, HttpClient, RxJS (Observables) y consumo de APIs REST."],
        ["23", "23-angular-routing-formularios.md", "Angular: Enrutamiento con Angular Router, Lazy Loading, Formularios Reactivos y validación UI."]
    ]
    styled_table(docs_headers, docs_data, col_widths=[1.1, 2.4, 3.2], header_bg="0F4C81")

    # Enlaces oficiales
    body_p("Portales y documentación técnica de referencia:")
    bullet_p("W3C / Web Accessibility Initiative (WAI): w3.org/WAI (Pautas WCAG 2.2 y especificación WAI-ARIA).", "• ")
    bullet_p("MDN Web Docs (Mozilla): developer.mozilla.org (Referencia estándar de HTML, CSS, JavaScript y APIs Web).", "• ")
    bullet_p("Angular Official Documentation: angular.dev (Guías oficiales, tutoriales y API reference de Angular).", "• ")
    bullet_p("Figma Learn: help.figma.com (Documentación de Auto Layout, componentes y prototipado).", "• ")
    bullet_p("Tailwind CSS Docs: tailwindcss.com (Documentación técnica de Tailwind CSS v4).", "• ")

    # Guardar archivos docx
    out_docx_1 = r"e:\00. Clases\Apuntes\Diseño interfaces\Programación\Diseño_de_interfaces_web_2DAW_2025-2026.docx"
    out_docx_2 = r"e:\00. Clases\Apuntes\Diseño interfaces\Programación\Programacion_Didactica_DIW_2DAW_Andalucia.docx"
    
    doc.save(out_docx_1)
    doc.save(out_docx_2)
    print(f"Documentos Word DIW guardados con éxito:\n1. {out_docx_1}\n2. {out_docx_2}")

if __name__ == "__main__":
    build_diw_programacion()
