import sys
import os
import openpyxl
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.formatting.rule import CellIsRule

sys.stdout.reconfigure(encoding='utf-8')

wb = openpyxl.Workbook()
wb.remove(wb.active)  # Remove default sheet

# -------------------------------------------------------------
# Color Palette & Visual System Tokens (Navy / Ocean Theme for Web Design)
# -------------------------------------------------------------
NAVY_HEADER = "0F172A"       # Slate 900
NAVY_SUBHEADER = "1E293B"    # Slate 800
BLUE_ACCENT = "1D4ED8"       # Blue 700
BLUE_LIGHT = "DBEAFE"        # Blue 100
BLUE_BORDER = "93C5FD"       # Blue 300
TEAL_HEADER = "0F766E"       # Teal 700
TEAL_LIGHT = "CCFBF1"        # Teal 100
GREEN_HEADER = "15803D"      # Green 700
GREEN_LIGHT = "DCFCE7"       # Green 100
PURPLE_HEADER = "6B21A8"     # Purple 700
PURPLE_LIGHT = "F3E8FF"      # Purple 100
ORANGE_HEADER = "C2410C"     # Orange 700
ORANGE_LIGHT = "FFEDD5"      # Orange 100
CYAN_HEADER = "0369A1"       # Sky 700
CYAN_LIGHT = "E0F2FE"        # Sky 100
ZEBRA_FILL = "F8FAFC"        # Slate 50
TOTAL_FILL = "FEF3C7"        # Amber 100
HIGHLIGHT_ROW = "FEF9C3"     # Yellow 100

FILL_NAVY = PatternFill(start_color=NAVY_HEADER, end_color=NAVY_HEADER, fill_type="solid")
FILL_SUBHEADER = PatternFill(start_color=NAVY_SUBHEADER, end_color=NAVY_SUBHEADER, fill_type="solid")
FILL_BLUE_HEADER = PatternFill(start_color=BLUE_ACCENT, end_color=BLUE_ACCENT, fill_type="solid")
FILL_BLUE_LIGHT = PatternFill(start_color=BLUE_LIGHT, end_color=BLUE_LIGHT, fill_type="solid")
FILL_TEAL_HEADER = PatternFill(start_color=TEAL_HEADER, end_color=TEAL_HEADER, fill_type="solid")
FILL_TEAL_LIGHT = PatternFill(start_color=TEAL_LIGHT, end_color=TEAL_LIGHT, fill_type="solid")
FILL_GREEN_HEADER = PatternFill(start_color=GREEN_HEADER, end_color=GREEN_HEADER, fill_type="solid")
FILL_GREEN_LIGHT = PatternFill(start_color=GREEN_LIGHT, end_color=GREEN_LIGHT, fill_type="solid")
FILL_PURPLE_HEADER = PatternFill(start_color=PURPLE_HEADER, end_color=PURPLE_HEADER, fill_type="solid")
FILL_PURPLE_LIGHT = PatternFill(start_color=PURPLE_LIGHT, end_color=PURPLE_LIGHT, fill_type="solid")
FILL_ORANGE_HEADER = PatternFill(start_color=ORANGE_HEADER, end_color=ORANGE_HEADER, fill_type="solid")
FILL_ORANGE_LIGHT = PatternFill(start_color=ORANGE_LIGHT, end_color=ORANGE_LIGHT, fill_type="solid")
FILL_CYAN_HEADER = PatternFill(start_color=CYAN_HEADER, end_color=CYAN_HEADER, fill_type="solid")
FILL_CYAN_LIGHT = PatternFill(start_color=CYAN_LIGHT, end_color=CYAN_LIGHT, fill_type="solid")
FILL_ZEBRA = PatternFill(start_color=ZEBRA_FILL, end_color=ZEBRA_FILL, fill_type="solid")
FILL_TOTAL = PatternFill(start_color=TOTAL_FILL, end_color=TOTAL_FILL, fill_type="solid")
FILL_HIGHLIGHT = PatternFill(start_color=HIGHLIGHT_ROW, end_color=HIGHLIGHT_ROW, fill_type="solid")

FONT_TITLE = Font(name="Segoe UI", size=14, bold=True, color="FFFFFF")
FONT_SUBTITLE = Font(name="Segoe UI", size=10, italic=True, color="E2E8F0")
FONT_HEADER = Font(name="Segoe UI", size=9, bold=True, color="FFFFFF")
FONT_HEADER_DARK = Font(name="Segoe UI", size=9, bold=True, color="0F172A")
FONT_BODY = Font(name="Segoe UI", size=9)
FONT_BODY_BOLD = Font(name="Segoe UI", size=9, bold=True)
FONT_KPI_VAL = Font(name="Segoe UI", size=16, bold=True, color="0F172A")
FONT_KPI_LBL = Font(name="Segoe UI", size=8, bold=True, color="64748B")

BORDER_THIN = Side(border_style="thin", color="CBD5E1")
BORDER_MEDIUM = Side(border_style="medium", color="64748B")
BORDER_DOUBLE = Side(border_style="double", color="0F172A")

CELL_BORDER = Border(left=BORDER_THIN, right=BORDER_THIN, top=BORDER_THIN, bottom=BORDER_THIN)
TOTAL_BORDER = Border(left=BORDER_THIN, right=BORDER_THIN, top=BORDER_THIN, bottom=BORDER_DOUBLE)
HEADER_BORDER = Border(left=BORDER_THIN, right=BORDER_THIN, top=BORDER_THIN, bottom=BORDER_MEDIUM)

ALIGN_CENTER = Alignment(horizontal="center", vertical="center", wrap_text=True)
ALIGN_LEFT = Alignment(horizontal="left", vertical="center")
ALIGN_RIGHT = Alignment(horizontal="right", vertical="center")

# 15 Students (Realistic for 2º DAW)
STUDENTS = [
    ("Álvarez Gómez", "Laura"),
    ("Benítez Romero", "Carlos"),
    ("Castillo Morales", "Elena"),
    ("Delgado Santos", "Alejandro"),
    ("Fernández Navarro", "Lucía"),
    ("García Serrano", "David"),
    ("Herrera Cruz", "Marta"),
    ("Jiménez Ortiz", "Pablo"),
    ("López Molina", "Sara"),
    ("Martín Vega", "Javier"),
    ("Navarro Gil", "Ana"),
    ("Pérez Rubio", "Álvaro"),
    ("Ramírez Soto", "Carmen"),
    ("Sánchez Vidal", "Daniel"),
    ("Torres Lozano", "Irene")
]

# 45 Official CEs for Diseño de Interfaces Web (2º DAW - Código 0615)
# Format: (RA_code, RA_weight, CE_code, CE_description, UDs, exact_ce_weight, default_tasks_x)
# Task indices: 0:T01, 1:T02, 2:T03, 3:T04, 4:T05, 5:T06(ExT1), 6:T07(GitT1),
#               7:T08, 8:T09, 9:T10, 10:T11, 11:T12, 12:T13(GesFlow/SPA), 13:T14(ExT2), 14:T15(GitT2)
CRITERIA_DATA = [
    # RA1: Planifica la creación de una interfaz web (12% total, 2% each)
    ("RA1", 0.12, "CE1.a", "Se ha reconocido la importancia de la comunicación visual y sus principios básicos.", "UD01, UD02", 0.02, [0, 5, 12]),
    ("RA1", 0.12, "CE1.b", "Se han analizado y seleccionado los colores y tipografías adecuados para pantalla.", "UD03", 0.02, [0, 5, 12]),
    ("RA1", 0.12, "CE1.c", "Se han analizado alternativas para la presentación de información web.", "UD01, UD06", 0.02, [0, 5, 12]),
    ("RA1", 0.12, "CE1.d", "Se ha valorado la importancia de definir y aplicar la guía de estilo.", "UD04", 0.02, [0, 5, 6, 12]),
    ("RA1", 0.12, "CE1.e", "Se han utilizado y valorado distintas tecnologías para el diseño web.", "UD01, UD05", 0.02, [0, 5, 12]),
    ("RA1", 0.12, "CE1.f", "Se han creado y utilizado plantillas y prototipos de diseño (Figma).", "UD05, UD06", 0.02, [0, 5, 6, 12]),

    # RA2: Crea interfaces web homogéneos definiendo y aplicando estilos (20% total, 2% each)
    ("RA2", 0.20, "CE2.a", "Se han reconocido las posibilidades de modificar las etiquetas HTML.", "UD07", 0.02, [1, 5]),
    ("RA2", 0.20, "CE2.b", "Se han definido estilos de forma directa.", "UD08", 0.02, [1, 5]),
    ("RA2", 0.20, "CE2.c", "Se han definido y asociado estilos globales en hojas externas.", "UD08", 0.02, [1, 5, 12]),
    ("RA2", 0.20, "CE2.d", "Se han definido hojas de estilos alternativas.", "UD08", 0.02, [1]),
    ("RA2", 0.20, "CE2.e", "Se han redefinido estilos (cascada, especificidad, @layer).", "UD08, UD09", 0.02, [1, 2, 5]),
    ("RA2", 0.20, "CE2.f", "Se han identificado las distintas propiedades de cada elemento.", "UD08, UD09, UD10", 0.02, [1, 2, 5]),
    ("RA2", 0.20, "CE2.g", "Se han creado clases y selectores de estilos (BEM).", "UD08, UD10", 0.02, [1, 2, 5, 12]),
    ("RA2", 0.20, "CE2.h", "Se han utilizado herramientas de validación de hojas de estilos (W3C).", "UD08", 0.02, [1, 3, 6, 14]),
    ("RA2", 0.20, "CE2.i", "Se han utilizado tecnologías y frameworks responsive (Grid, Tailwind 4).", "UD10, UD11, UD17", 0.02, [2, 3, 5, 12, 13]),
    ("RA2", 0.20, "CE2.j", "Se han analizado y utilizado preprocesadores de estilos (Sass/SCSS).", "UD18", 0.02, [3, 12]),

    # RA3: Prepara archivos multimedia para la web (16% total, 2% each)
    ("RA3", 0.16, "CE3.a", "Se han reconocido las implicaciones de licencias y derechos de autor (TRLPI/CC).", "UD19", 0.02, [4, 5]),
    ("RA3", 0.16, "CE3.b", "Se han identificado formatos de imagen, audio y vídeo (WebP, AVIF, SVG).", "UD12", 0.02, [4, 5, 12]),
    ("RA3", 0.16, "CE3.c", "Se han analizado herramientas para generar contenido multimedia.", "UD12", 0.02, [4]),
    ("RA3", 0.16, "CE3.d", "Se han empleado herramientas para el tratamiento digital de la imagen.", "UD12", 0.02, [4, 12]),
    ("RA3", 0.16, "CE3.e", "Se han utilizado herramientas para manipular audio y vídeo (HTML5 track).", "UD12", 0.02, [4, 12]),
    ("RA3", 0.16, "CE3.f", "Se han realizado animaciones a partir de imágenes fijas.", "UD12, UD13", 0.02, [4, 7, 12]),
    ("RA3", 0.16, "CE3.g", "Se han importado y exportado recursos multimedia en diversos formatos.", "UD12", 0.02, [4, 12]),
    ("RA3", 0.16, "CE3.h", "Se ha aplicado la guía de estilo al material multimedia.", "UD04, UD12", 0.02, [4, 6, 12]),

    # RA4: Integra contenido multimedia y elementos interactivos (24% total, ponderación diferenciada)
    ("RA4", 0.24, "CE4.a", "Se han reconocido tecnologías de inclusión de contenido interactivo.", "UD13", 0.02, [7, 12]),
    ("RA4", 0.24, "CE4.b", "Se han configurado navegadores para contenido multimedia e interactivo.", "UD13", 0.02, [7]),
    ("RA4", 0.24, "CE4.c", "Se han utilizado herramientas gráficas para contenido interactivo.", "UD13, UD21", 0.04, [7, 8, 12]),
    ("RA4", 0.24, "CE4.d", "Se ha analizado el código generado por herramientas interactivas.", "UD13, UD21, UD22", 0.04, [7, 8, 9, 12, 13]),
    ("RA4", 0.24, "CE4.e", "Se han agregado elementos multimedia a documentos web.", "UD12, UD13", 0.04, [7, 12]),
    ("RA4", 0.24, "CE4.f", "Se ha añadido interactividad a elementos web (Signals, Events, Forms).", "UD13, UD21, UD23", 0.04, [7, 8, 9, 12, 13]),
    ("RA4", 0.24, "CE4.g", "Se ha verificado el funcionamiento interactivo en múltiples dispositivos.", "UD11, UD13, UD23", 0.04, [7, 9, 12, 13, 14]),

    # RA5: Desarrolla interfaces web accesibles (16% total, 2% each)
    ("RA5", 0.16, "CE5.a", "Se ha reconocido la necesidad de diseñar webs accesibles (RD 1112/2018).", "UD14", 0.02, [10, 12]),
    ("RA5", 0.16, "CE5.b", "Se ha analizado la accesibilidad de diferentes documentos web.", "UD14", 0.02, [10, 12]),
    ("RA5", 0.16, "CE5.c", "Se han analizado los principios y pautas WCAG 2.2 y niveles de conformidad.", "UD14", 0.02, [10, 12, 13]),
    ("RA5", 0.16, "CE5.d", "Se han analizado los posibles errores según prioridades de verificación.", "UD14", 0.02, [10, 12]),
    ("RA5", 0.16, "CE5.e", "Se ha alcanzado el nivel de conformidad deseado (Nivel AA/AAA).", "UD14", 0.02, [10, 12]),
    ("RA5", 0.16, "CE5.f", "Se han verificado los niveles mediante tests automatizados (axe, Lighthouse).", "UD14", 0.02, [10, 12, 13]),
    ("RA5", 0.16, "CE5.g", "Se ha verificado la visualización con tecnologías asistivas (NVDA).", "UD14", 0.02, [10, 12]),
    ("RA5", 0.16, "CE5.h", "Se han utilizado herramientas que mejoren visibilidad y accesibilidad (WAI-ARIA).", "UD14", 0.02, [10, 12, 14]),

    # RA6: Desarrolla interfaces web amigables y usables (12% total, 2% each)
    ("RA6", 0.12, "CE6.a", "Se ha analizado la usabilidad de diferentes documentos web (Nielsen).", "UD15", 0.02, [11, 12]),
    ("RA6", 0.12, "CE6.b", "Se ha valorado la importancia de los estándares en la creación web.", "UD04, UD15", 0.02, [0, 11, 12]),
    ("RA6", 0.12, "CE6.c", "Se ha adecuado la interfaz web a los objetivos y usuarios (DCU/Personas).", "UD16", 0.02, [0, 11, 12]),
    ("RA6", 0.12, "CE6.d", "Se ha verificado la facilidad de navegación mediante diversos periféricos.", "UD15", 0.02, [11, 12]),
    ("RA6", 0.12, "CE6.e", "Se han analizado técnicas para verificar la usabilidad (SUS, métricas UX).", "UD15, UD16", 0.02, [11, 12, 14]),
    ("RA6", 0.12, "CE6.f", "Se ha verificado la usabilidad en diferentes navegadores y dispositivos.", "UD15", 0.02, [11, 12, 13])
]

# Task metadata: (TaskCode, ShortTitle, FullName, UDs, Trimestre)
TASKS_INFO = [
    # Trimestre 1 (Cols H to N in Matriz, Cols D to J in Registro)
    ("T01", "Figma & Estilos", "Act. 1: Prototipado Figma, Color, Tipografía y Guía de Estilo", "UD01-06", "T1"),
    ("T02", "HTML & CSS Pro", "Act. 2: Maquetación HTML5 Semántico y Selectores CSS Avanzados", "UD07-08", "T1"),
    ("T03", "Flexbox & Grid", "Act. 3: Maquetación Bidimensional con Flexbox y CSS Grid Layout", "UD09-10", "T1"),
    ("T04", "Responsive & TW4", "Act. 4: Responsive Web Design, Mobile-First, Sass y Tailwind CSS v4", "UD11, 17, 18", "T1"),
    ("T05", "Multimedia & Legal", "Act. 5: Multimedia Web (WebP, SVG, Audio/Vídeo) y Licencias TRLPI", "UD12, UD19", "T1"),
    ("T06", "Examen Práctico T1", "Examen Práctico 1er Trimestre (Maquetación Web Completa)", "UD01-12, 17-19", "T1"),
    ("T07", "Git & W3C T1", "Control de Versiones Git, Validación W3C y Buenas Prácticas T1", "Transversal", "T1"),

    # Trimestre 2 (Cols O to V in Matriz, Cols K to R in Registro)
    ("T08", "Interactividad CSS", "Act. 6: Interactividad, Microinteracciones y Animaciones Web", "UD13", "T2"),
    ("T09", "Angular Signals", "Act. 7: Componentes Standalone, Signals y Directivas de Control", "UD20-21", "T2"),
    ("T10", "Servicios & Forms", "Act. 8: Servicios, Inyección, HttpClient y Formularios Reactivos", "UD22-23", "T2"),
    ("T11", "Accesibilidad WCAG", "Act. 9: Auditoría de Accesibilidad WCAG 2.2, WAI-ARIA y axe", "UD14", "T2"),
    ("T12", "Usabilidad & SUS", "Act. 10: Evaluación Heurística de Nielsen, Métricas SUS y DCU", "UD15-16", "T2"),
    ("T13", "Proyecto Web SPA", "Proyecto Final Integrador: SPA Frontend Accesible en Angular", "UD01-23", "T2"),
    ("T14", "Examen Práctico T2", "Examen Práctico 2º Trimestre (Desarrollo Frontend SPA)", "UD13-16, 20-23", "T2"),
    ("T15", "Git & Despliegue T2", "Calidad Frontend, Despliegue Web, Git Flow y Actitud T2", "Transversal", "T2")
]

# Realistic grades for the 15 students across the 15 tasks
STUDENT_TASK_GRADES = [
    [8.5, 9.0, 8.5, 8.5, 9.0, 8.5, 9.0,   8.5, 9.0, 8.5, 9.0, 8.5, 9.0, 8.5, 9.5],
    [6.0, 6.0, 6.5, 7.0, 6.0, 6.0, 7.0,   6.5, 6.0, 7.0, 6.5, 6.0, 6.5, 6.0, 7.0],
    [9.5, 9.0, 10.0, 9.5, 10.0, 9.5, 10.0, 10.0, 9.5, 9.5, 10.0, 9.5, 10.0, 10.0, 10.0],
    [4.5, 5.0, 4.5, 5.5, 4.0, 4.5, 6.0,   5.0, 4.5, 5.0, 4.5, 5.0, 4.5, 4.0, 5.0],
    [7.5, 8.0, 7.0, 7.5, 8.0, 7.5, 8.5,   7.5, 8.0, 8.0, 7.5, 8.0, 7.5, 8.0, 8.5],
    [8.0, 7.5, 8.5, 8.0, 8.5, 8.0, 8.5,   8.0, 8.5, 8.0, 8.5, 8.0, 8.5, 8.0, 8.5],
    [9.0, 8.5, 9.5, 9.0, 9.0, 9.0, 9.5,   9.0, 9.5, 9.0, 9.5, 9.0, 9.5, 9.0, 9.5],
    [5.5, 6.0, 5.5, 5.0, 6.0, 5.5, 6.5,   5.5, 6.0, 5.5, 6.0, 5.5, 6.0, 5.5, 6.5],
    [10.0, 9.5, 9.5, 10.0, 9.5, 10.0, 10.0, 10.0, 9.5, 10.0, 10.0, 9.5, 10.0, 10.0, 10.0],
    [3.5, 4.0, 4.0, 4.5, 4.0, 3.5, 5.0,   4.0, 4.5, 4.0, 4.0, 4.5, 4.0, 4.0, 4.5],
    [8.0, 8.5, 8.0, 8.5, 8.0, 8.5, 9.0,   8.5, 8.0, 8.5, 8.5, 8.0, 8.5, 8.5, 9.0],
    [7.0, 6.5, 7.5, 7.0, 7.0, 7.0, 7.5,   7.5, 7.0, 7.5, 7.0, 7.5, 7.0, 7.5, 7.5],
    [6.5, 7.0, 6.0, 6.5, 7.0, 6.5, 7.0,   7.0, 6.5, 7.0, 6.5, 7.0, 6.5, 7.0, 7.0],
    [8.5, 9.0, 8.5, 9.0, 8.5, 9.0, 9.5,   9.0, 8.5, 9.0, 9.0, 8.5, 9.0, 9.0, 9.5],
    [9.0, 9.5, 9.0, 9.5, 9.0, 9.5, 9.5,   9.5, 9.0, 9.5, 10.0, 9.5, 9.5, 9.5, 10.0]
]


# =============================================================
# SHEET 1: MATRIZ DE CRITERIOS (SELECTOR AVANZADO DE TAREAS)
# =============================================================
ws_mat = wb.create_sheet(title="Matriz Criterios")
ws_mat.views.sheetView[0].showGridLines = True

# Title
ws_mat.merge_cells("A1:W1")
ws_mat["A1"] = "MATRIZ DE SELECCIÓN DE CRITERIOS DE EVALUACIÓN POR TAREA — DISEÑO DE INTERFACES WEB (2º DAW)"
ws_mat["A1"].font = FONT_TITLE
ws_mat["A1"].fill = FILL_NAVY
ws_mat["A1"].alignment = ALIGN_CENTER
ws_mat.row_dimensions[1].height = 36

ws_mat.merge_cells("A2:W2")
ws_mat["A2"] = "Marca con una 'X' en la casilla correspondiente para activar los criterios evaluados en cada tarea. Los porcentajes de las líneas 52 y 53 se calculan automáticamente."
ws_mat["A2"].font = FONT_SUBTITLE
ws_mat["A2"].fill = FILL_SUBHEADER
ws_mat["A2"].alignment = ALIGN_CENTER
ws_mat.row_dimensions[2].height = 20

# Header groups (Row 4)
ws_mat.merge_cells("A4:G4")
ws_mat["A4"] = "CRITERIOS OFICIALES DE EVALUACIÓN (ORDEN DE 16 DE JUNIO DE 2011 & DECRETO 104/2024)"
ws_mat["A4"].font = FONT_HEADER
ws_mat["A4"].alignment = ALIGN_CENTER
ws_mat["A4"].fill = FILL_NAVY

ws_mat.merge_cells("H4:N4")
ws_mat["H4"] = "1er TRIMESTRE (T1) — TAREAS Y PRUEBAS"
ws_mat["H4"].font = FONT_HEADER
ws_mat["H4"].alignment = ALIGN_CENTER
ws_mat["H4"].fill = FILL_BLUE_HEADER

ws_mat.merge_cells("O4:V4")
ws_mat["O4"] = "2º TRIMESTRE (T2) — TAREAS, PRUEBAS Y PROYECTO"
ws_mat["O4"].font = FONT_HEADER
ws_mat["O4"].alignment = ALIGN_CENTER
ws_mat["O4"].fill = FILL_TEAL_HEADER

ws_mat.merge_cells("W4:W5")
ws_mat["W4"] = "Pond. CE\nOficial"
ws_mat["W4"].font = FONT_HEADER
ws_mat["W4"].alignment = ALIGN_CENTER
ws_mat["W4"].fill = FILL_PURPLE_HEADER

# Column subheaders (Row 5)
col_defs_mat = [
    ("RA", 8),
    ("Peso RA", 9),
    ("Código CE", 10),
    ("Descripción Oficial del Criterio de Evaluación", 44),
    ("UDs", 14),
    ("Total\nTareas", 8),
    ("Estado Cobertura", 14)
]

for col_idx, (name, width) in enumerate(col_defs_mat, start=1):
    col_let = get_column_letter(col_idx)
    ws_mat.column_dimensions[col_let].width = width
    cell = ws_mat.cell(row=5, column=col_idx, value=name)
    cell.font = FONT_HEADER
    cell.alignment = ALIGN_CENTER
    cell.fill = FILL_SUBHEADER
    cell.border = HEADER_BORDER

# Task headers (Cols H to V, idx 8 to 22)
for t_idx, t_info in enumerate(TASKS_INFO, start=8):
    col_let = get_column_letter(t_idx)
    ws_mat.column_dimensions[col_let].width = 12
    cell = ws_mat.cell(row=5, column=t_idx, value=f"{t_info[0]}\n{t_info[1]}")
    cell.font = FONT_HEADER
    cell.alignment = ALIGN_CENTER
    cell.fill = FILL_BLUE_HEADER if t_idx <= 14 else FILL_TEAL_HEADER
    cell.border = HEADER_BORDER

ws_mat.column_dimensions["W"].width = 12
ws_mat.row_dimensions[5].height = 36

# Fill 45 Criterios (Rows 6 to 50)
for c_idx, crit in enumerate(CRITERIA_DATA, start=6):
    ws_mat.row_dimensions[c_idx].height = 24
    ra_code, ra_weight, ce_code, ce_desc, uds, ce_w, tasks_x = crit
    is_zebra = (c_idx % 2 == 0)
    row_fill = FILL_ZEBRA if is_zebra else PatternFill(fill_type=None)
    
    # Col A: RA
    cA = ws_mat.cell(row=c_idx, column=1, value=ra_code)
    cA.font = FONT_BODY_BOLD
    cA.alignment = ALIGN_CENTER
    cA.fill = row_fill
    cA.border = CELL_BORDER
    
    # Col B: Peso RA
    cB = ws_mat.cell(row=c_idx, column=2, value=ra_weight)
    cB.font = FONT_BODY
    cB.alignment = ALIGN_CENTER
    cB.fill = row_fill
    cB.border = CELL_BORDER
    cB.number_format = "0.0%"
    
    # Col C: Codigo CE
    cC = ws_mat.cell(row=c_idx, column=3, value=ce_code)
    cC.font = FONT_BODY_BOLD
    cC.alignment = ALIGN_CENTER
    cC.fill = row_fill
    cC.border = CELL_BORDER
    
    # Col D: Descripcion
    cD = ws_mat.cell(row=c_idx, column=4, value=ce_desc)
    cD.font = FONT_BODY
    cD.alignment = ALIGN_LEFT
    cD.fill = row_fill
    cD.border = CELL_BORDER
    
    # Col E: UDs
    cE = ws_mat.cell(row=c_idx, column=5, value=uds)
    cE.font = FONT_BODY
    cE.alignment = ALIGN_CENTER
    cE.fill = row_fill
    cE.border = CELL_BORDER
    
    # Col F: Total Tareas que evaluan este criterio =COUNTIF(H{c_idx}:V{c_idx}, "X")
    cF = ws_mat.cell(row=c_idx, column=6)
    cF.value = f'=COUNTIF(H{c_idx}:V{c_idx}, "X")'
    cF.font = FONT_BODY_BOLD
    cF.alignment = ALIGN_CENTER
    cF.fill = FILL_TOTAL
    cF.border = CELL_BORDER
    
    # Col G: Estado Cobertura =IF(F{c_idx}>0, "EVALUADO", "SIN EVALUAR")
    cG = ws_mat.cell(row=c_idx, column=7)
    cG.value = f'=IF(F{c_idx}>0, "EVALUADO", "SIN EVALUAR")'
    cG.font = FONT_BODY_BOLD
    cG.alignment = ALIGN_CENTER
    cG.fill = row_fill
    cG.border = CELL_BORDER
    
    # Cols H to V: Tasks selection "X"
    for t_i in range(15):
        col_target = 8 + t_i
        cell_x = ws_mat.cell(row=c_idx, column=col_target)
        if t_i in tasks_x:
            cell_x.value = "X"
            cell_x.font = Font(name="Segoe UI", size=10, bold=True, color="1E3A8A")
            cell_x.fill = FILL_BLUE_LIGHT if col_target <= 14 else FILL_TEAL_LIGHT
        else:
            cell_x.value = ""
            cell_x.font = FONT_BODY
            cell_x.fill = row_fill
        cell_x.alignment = ALIGN_CENTER
        cell_x.border = CELL_BORDER
        
    # Col W: Ponderacion Oficial de este CE
    cW = ws_mat.cell(row=c_idx, column=23, value=ce_w)
    cW.font = FONT_BODY
    cW.alignment = ALIGN_CENTER
    cW.fill = row_fill
    cW.border = CELL_BORDER
    cW.number_format = "0.00%"

# Row 51: Total criterios evaluados por tarea
row_crit_count = 51
ws_mat.row_dimensions[row_crit_count].height = 24
ws_mat.merge_cells(f"A{row_crit_count}:G{row_crit_count}")
ws_mat[f"A{row_crit_count}"] = "TOTAL CRITERIOS EVALUADOS POR ESTA TAREA"
ws_mat[f"A{row_crit_count}"].font = FONT_HEADER_DARK
ws_mat[f"A{row_crit_count}"].alignment = ALIGN_RIGHT
ws_mat[f"A{row_crit_count}"].fill = FILL_TOTAL
ws_mat[f"A{row_crit_count}"].border = TOTAL_BORDER

for t_i in range(15):
    col_t = 8 + t_i
    col_let = get_column_letter(col_t)
    c_tot = ws_mat.cell(row=row_crit_count, column=col_t)
    c_tot.value = f'=COUNTIF({col_let}$6:{col_let}$50, "X")'
    c_tot.font = FONT_BODY_BOLD
    c_tot.alignment = ALIGN_CENTER
    c_tot.fill = FILL_TOTAL
    c_tot.border = TOTAL_BORDER

c_tot_w = ws_mat.cell(row=row_crit_count, column=23, value="100.0%")
c_tot_w.font = FONT_BODY_BOLD
c_tot_w.alignment = ALIGN_CENTER
c_tot_w.fill = FILL_GREEN_LIGHT
c_tot_w.border = TOTAL_BORDER

# Row 52: SUMA DE PESOS DE CRITERIOS EVALUADOS EN LA TAREA (Dinámico según las 'X')
row_weight = 52
ws_mat.row_dimensions[row_weight].height = 26
ws_mat.merge_cells(f"A{row_weight}:G{row_weight}")
ws_mat[f"A{row_weight}"] = "SUMA DE CRITERIOS EVALUADOS EN ESTA TAREA (Suma Directa con 'X')"
ws_mat[f"A{row_weight}"].font = FONT_HEADER_DARK
ws_mat[f"A{row_weight}"].alignment = ALIGN_RIGHT
ws_mat[f"A{row_weight}"].fill = FILL_HIGHLIGHT
ws_mat[f"A{row_weight}"].border = TOTAL_BORDER

for t_i in range(15):
    col_t = 8 + t_i
    col_let = get_column_letter(col_t)
    c_w = ws_mat.cell(row=row_weight, column=col_t)
    # SUMIF: Sum the CE global weights from col W where that task has an "X"
    c_w.value = f'=SUMIF({col_let}$6:{col_let}$50, "X", $W$6:$W$50)'
    c_w.font = Font(name="Segoe UI", size=9, bold=True, color="1E3A8A")
    c_w.alignment = ALIGN_CENTER
    c_w.fill = FILL_HIGHLIGHT
    c_w.border = TOTAL_BORDER
    c_w.number_format = "0.00%"

c_w_sum = ws_mat.cell(row=row_weight, column=23)
c_w_sum.value = f"=SUM(H{row_weight}:V{row_weight})"
c_w_sum.font = FONT_BODY_BOLD
c_w_sum.alignment = ALIGN_CENTER
c_w_sum.fill = FILL_HIGHLIGHT
c_w_sum.border = TOTAL_BORDER
c_w_sum.number_format = "0.00%"

# Row 53: % PONDERACIÓN EN EL TRIMESTRE (Normalizado a 100% de T1 / T2)
row_norm = 53
ws_mat.row_dimensions[row_norm].height = 26
ws_mat.merge_cells(f"A{row_norm}:G{row_norm}")
ws_mat[f"A{row_norm}"] = "% PONDERACIÓN EN EL TRIMESTRE (Normalizado a 100% para boletín de notas)"
ws_mat[f"A{row_norm}"].font = FONT_HEADER_DARK
ws_mat[f"A{row_norm}"].alignment = ALIGN_RIGHT
ws_mat[f"A{row_norm}"].fill = FILL_GREEN_LIGHT
ws_mat[f"A{row_norm}"].border = TOTAL_BORDER

for t_i in range(15):
    col_t = 8 + t_i
    col_let = get_column_letter(col_t)
    c_norm = ws_mat.cell(row=row_norm, column=col_t)
    if t_i < 7:  # T1: T01 to T07 (Cols H to N)
        c_norm.value = f'=IF(SUM($H${row_weight}:$N${row_weight})=0, 0, {col_let}${row_weight} / SUM($H${row_weight}:$N${row_weight}))'
    else:        # T2: T08 to T15 (Cols O to V)
        c_norm.value = f'=IF(SUM($O${row_weight}:$V${row_weight})=0, 0, {col_let}${row_weight} / SUM($O${row_weight}:$V${row_weight}))'
    c_norm.font = Font(name="Segoe UI", size=9, bold=True, color="15803D")
    c_norm.alignment = ALIGN_CENTER
    c_norm.fill = FILL_GREEN_LIGHT
    c_norm.border = TOTAL_BORDER
    c_norm.number_format = "0.00%"

c_norm_sum = ws_mat.cell(row=row_norm, column=23)
c_norm_sum.value = "100% T1 / 100% T2"
c_norm_sum.font = Font(name="Segoe UI", size=8, bold=True, color="15803D")
c_norm_sum.alignment = ALIGN_CENTER
c_norm_sum.fill = FILL_GREEN_LIGHT
c_norm_sum.border = TOTAL_BORDER

# Conditional Formatting on Matrix
ws_mat.conditional_formatting.add("G6:G50", CellIsRule(operator="equal", formula=['"EVALUADO"'], stopIfTrue=True, fill=FILL_GREEN_LIGHT, font=Font(color="15803D", bold=True)))
ws_mat.conditional_formatting.add("G6:G50", CellIsRule(operator="equal", formula=['"SIN EVALUAR"'], stopIfTrue=True, fill=PatternFill(start_color="FEE2E2", end_color="FEE2E2", fill_type="solid"), font=Font(color="DC2626", bold=True)))
ws_mat.conditional_formatting.add("H6:V50", CellIsRule(operator="equal", formula=['"X"'], stopIfTrue=True, fill=FILL_BLUE_LIGHT, font=Font(color="1D4ED8", bold=True)))


# =============================================================
# SHEET 2: REGISTRO DE NOTAS (CALIFICADOR POR TAREAS)
# =============================================================
ws_reg = wb.create_sheet(title="Registro Notas")
ws_reg.views.sheetView[0].showGridLines = True

# Title
ws_reg.merge_cells("A1:T1")
ws_reg["A1"] = "REGISTRO DE CALIFICACIONES POR TAREA — DISEÑO DE INTERFACES WEB (2º DAW)"
ws_reg["A1"].font = FONT_TITLE
ws_reg["A1"].fill = FILL_NAVY
ws_reg["A1"].alignment = ALIGN_CENTER
ws_reg.row_dimensions[1].height = 36

ws_reg.merge_cells("A2:T2")
ws_reg["A2"] = "Introduce las notas obtenidas (0 a 10). Las cabeceras muestran el % dinámico calculado a partir de los criterios seleccionados en 'Matriz Criterios'."
ws_reg["A2"].font = FONT_SUBTITLE
ws_reg["A2"].fill = FILL_SUBHEADER
ws_reg["A2"].alignment = ALIGN_CENTER
ws_reg.row_dimensions[2].height = 20

# Subgroups headers (Row 4)
ws_reg.merge_cells("A4:C4")
ws_reg["A4"] = "DATOS DEL ALUMNADO"
ws_reg["A4"].font = FONT_HEADER
ws_reg["A4"].alignment = ALIGN_CENTER
ws_reg["A4"].fill = FILL_NAVY

ws_reg.merge_cells("D4:J4")
ws_reg["D4"] = "TAREAS 1er TRIMESTRE (T1) — PESOS DERIVADOS DE CRITERIOS"
ws_reg["D4"].font = FONT_HEADER
ws_reg["D4"].alignment = ALIGN_CENTER
ws_reg["D4"].fill = FILL_BLUE_HEADER

ws_reg.merge_cells("K4:R4")
ws_reg["K4"] = "TAREAS 2º TRIMESTRE (T2) — PESOS DERIVADOS DE CRITERIOS"
ws_reg["K4"].font = FONT_HEADER
ws_reg["K4"].alignment = ALIGN_CENTER
ws_reg["K4"].fill = FILL_TEAL_HEADER

ws_reg.merge_cells("S4:T4")
ws_reg["S4"] = "CALIFICACIONES TRIMESTRALES"
ws_reg["S4"].font = FONT_HEADER
ws_reg["S4"].alignment = ALIGN_CENTER
ws_reg["S4"].fill = FILL_PURPLE_HEADER

# Row 5: Column headers
reg_cols = [
    ("Nº", 5),
    ("Apellidos, Nombre", 25),
    ("Grupo", 8),
    # T01 to T07 (T1)
    ("T01\nFigma & Estilos", 12),
    ("T02\nHTML & CSS Pro", 12),
    ("T03\nFlex & Grid", 12),
    ("T04\nResp. & TW4", 12),
    ("T05\nMultimedia", 12),
    ("T06\nExamen T1", 12),
    ("T07\nGit & W3C T1", 11),
    # T08 to T15 (T2)
    ("T08\nInteractividad", 12),
    ("T09\nAngular Signals", 12),
    ("T10\nServicios & Forms", 12),
    ("T11\nAccesib. WCAG", 12),
    ("T12\nUsabilidad SUS", 12),
    ("T13\nProyecto SPA", 13),
    ("T14\nExamen T2", 12),
    ("T15\nGit & Despliegue", 11),
    # Trimester totals
    ("1º TRIMESTRE\n(100% Criterios)", 15),
    ("2º TRIMESTRE\n(100% Criterios)", 15)
]

ws_reg.row_dimensions[5].height = 36
for col_idx, (col_name, width) in enumerate(reg_cols, start=1):
    col_let = get_column_letter(col_idx)
    ws_reg.column_dimensions[col_let].width = width
    cell = ws_reg.cell(row=5, column=col_idx, value=col_name)
    cell.font = FONT_HEADER
    cell.alignment = ALIGN_CENTER
    cell.border = HEADER_BORDER
    if col_idx <= 3:
        cell.fill = FILL_NAVY
    elif col_idx <= 10:
        cell.fill = FILL_BLUE_HEADER
    elif col_idx <= 18:
        cell.fill = FILL_TEAL_HEADER
    else:
        cell.fill = FILL_PURPLE_HEADER

# Student rows (Rows 6 to 20)
for r_idx, (apell, nom) in enumerate(STUDENTS, start=6):
    ws_reg.row_dimensions[r_idx].height = 20
    is_zebra = (r_idx % 2 == 0)
    row_fill = FILL_ZEBRA if is_zebra else PatternFill(fill_type=None)
    
    # Nº
    c1 = ws_reg.cell(row=r_idx, column=1, value=r_idx-5)
    c1.alignment = ALIGN_CENTER
    c1.border = CELL_BORDER
    c1.fill = row_fill
    c1.font = FONT_BODY
    
    # Nombre
    c2 = ws_reg.cell(row=r_idx, column=2, value=f"{apell}, {nom}")
    c2.alignment = ALIGN_LEFT
    c2.border = CELL_BORDER
    c2.fill = row_fill
    c2.font = FONT_BODY_BOLD
    
    # Grupo
    c3 = ws_reg.cell(row=r_idx, column=3, value="2º DAW")
    c3.alignment = ALIGN_CENTER
    c3.border = CELL_BORDER
    c3.fill = row_fill
    c3.font = FONT_BODY
    
    # Grades for 15 tasks (Cols D to R, index 4 to 18)
    grades = STUDENT_TASK_GRADES[r_idx-6]
    for g_i, grade_val in enumerate(grades):
        c_task = ws_reg.cell(row=r_idx, column=4 + g_i, value=grade_val)
        c_task.alignment = ALIGN_CENTER
        c_task.border = CELL_BORDER
        c_task.fill = row_fill
        c_task.font = FONT_BODY
        c_task.number_format = "0.00"
        
    # Col S: NOTA 1º TRIMESTRE (T1) -> dynamically uses weights from 'Matriz Criterios'!H$53:N$53
    c_t1 = ws_reg.cell(row=r_idx, column=19)
    c_t1.value = f"=D{r_idx}*'Matriz Criterios'!H$53 + E{r_idx}*'Matriz Criterios'!I$53 + F{r_idx}*'Matriz Criterios'!J$53 + G{r_idx}*'Matriz Criterios'!K$53 + H{r_idx}*'Matriz Criterios'!L$53 + I{r_idx}*'Matriz Criterios'!M$53 + J{r_idx}*'Matriz Criterios'!N$53"
    c_t1.alignment = ALIGN_CENTER
    c_t1.border = CELL_BORDER
    c_t1.fill = FILL_BLUE_LIGHT
    c_t1.font = FONT_BODY_BOLD
    c_t1.number_format = "0.00"
    
    # Col T: NOTA 2º TRIMESTRE (T2) -> dynamically uses weights from 'Matriz Criterios'!O$53:V$53
    c_t2 = ws_reg.cell(row=r_idx, column=20)
    c_t2.value = f"=K{r_idx}*'Matriz Criterios'!O$53 + L{r_idx}*'Matriz Criterios'!P$53 + M{r_idx}*'Matriz Criterios'!Q$53 + N{r_idx}*'Matriz Criterios'!R$53 + O{r_idx}*'Matriz Criterios'!S$53 + P{r_idx}*'Matriz Criterios'!T$53 + Q{r_idx}*'Matriz Criterios'!U$53 + R{r_idx}*'Matriz Criterios'!V$53"
    c_t2.alignment = ALIGN_CENTER
    c_t2.border = CELL_BORDER
    c_t2.fill = FILL_TEAL_LIGHT
    c_t2.font = FONT_BODY_BOLD
    c_t2.number_format = "0.00"

# Average row for Tasks (Row 21)
row_reg_avg = 21
ws_reg.row_dimensions[row_reg_avg].height = 24
ws_reg.merge_cells(f"A{row_reg_avg}:C{row_reg_avg}")
c_avg_lbl = ws_reg.cell(row=row_reg_avg, column=1, value="PROMEDIO DEL GRUPO")
c_avg_lbl.font = FONT_HEADER_DARK
c_avg_lbl.alignment = ALIGN_CENTER
c_avg_lbl.fill = FILL_TOTAL
c_avg_lbl.border = TOTAL_BORDER
ws_reg.cell(row=row_reg_avg, column=2).border = TOTAL_BORDER
ws_reg.cell(row=row_reg_avg, column=3).border = TOTAL_BORDER

for col_idx in range(4, 21):
    col_let = get_column_letter(col_idx)
    c_avg = ws_reg.cell(row=row_reg_avg, column=col_idx)
    c_avg.value = f"=AVERAGE({col_let}6:{col_let}20)"
    c_avg.font = FONT_BODY_BOLD
    c_avg.alignment = ALIGN_CENTER
    c_avg.fill = FILL_TOTAL
    c_avg.border = TOTAL_BORDER
    c_avg.number_format = "0.00"

# Conditional formatting on Trimester notes
green_fill = PatternFill(start_color="DCFCE7", end_color="DCFCE7", fill_type="solid")
green_font = Font(color="15803D", bold=True)
red_fill = PatternFill(start_color="FEE2E2", end_color="FEE2E2", fill_type="solid")
red_font = Font(color="DC2626", bold=True)

ws_reg.conditional_formatting.add("S6:T20", CellIsRule(operator="greaterThanOrEqual", formula=["5.0"], stopIfTrue=True, fill=green_fill, font=green_font))
ws_reg.conditional_formatting.add("S6:T20", CellIsRule(operator="lessThan", formula=["5.0"], stopIfTrue=True, fill=red_fill, font=red_font))


# =============================================================
# SHEET 3: CÁLCULO POR CRITERIOS (CEs) — AUTOMATIZACIÓN TOTAL
# =============================================================
ws_ces = wb.create_sheet(title="Calculo CEs")
ws_ces.views.sheetView[0].showGridLines = True

# Title
ws_ces.merge_cells("A1:AW1")
ws_ces["A1"] = "CALIFICACIÓN DETALLADA POR CRITERIOS DE EVALUACIÓN (CE1.a a CE6.f) — DISEÑO DE INTERFACES WEB"
ws_ces["A1"].font = FONT_TITLE
ws_ces["A1"].fill = FILL_NAVY
ws_ces["A1"].alignment = ALIGN_CENTER
ws_ces.row_dimensions[1].height = 36

ws_ces.merge_cells("A2:AW2")
ws_ces["A2"] = "Cálculo matemático automático: cada criterio se calcula promediando exclusivamente las tareas donde tiene marcada una 'X' en la 'Matriz Criterios'."
ws_ces["A2"].font = FONT_SUBTITLE
ws_ces["A2"].fill = FILL_SUBHEADER
ws_ces["A2"].alignment = ALIGN_CENTER
ws_ces.row_dimensions[2].height = 20

# Header groups (Row 4)
ws_ces.merge_cells("A4:B4")
ws_ces["A4"] = "ALUMNADO"
ws_ces["A4"].font = FONT_HEADER
ws_ces["A4"].alignment = ALIGN_CENTER
ws_ces["A4"].fill = FILL_NAVY

# 6 RA groups across the 45 CEs:
# RA1: cols C to H (6 CEs, idx 3 to 8)
ws_ces.merge_cells("C4:H4")
ws_ces["C4"] = "RA1 (12%) — Planificación, Prototipado, Color, Tipografía y Guía de Estilo"
ws_ces["C4"].font = FONT_HEADER
ws_ces["C4"].alignment = ALIGN_CENTER
ws_ces["C4"].fill = FILL_BLUE_HEADER

# RA2: cols I to R (10 CEs, idx 9 to 18)
ws_ces.merge_cells("I4:R4")
ws_ces["I4"] = "RA2 (20%) — HTML Semántico, CSS Moderno, Flexbox, Grid, Responsive y Preprocesadores"
ws_ces["I4"].font = FONT_HEADER
ws_ces["I4"].alignment = ALIGN_CENTER
ws_ces["I4"].fill = FILL_TEAL_HEADER

# RA3: cols S to Z (8 CEs, idx 19 to 26)
ws_ces.merge_cells("S4:Z4")
ws_ces["S4"] = "RA3 (16%) — Multimedia Web, Formatos (WebP, SVG), Audio/Vídeo y Marco Legal TRLPI"
ws_ces["S4"].font = FONT_HEADER
ws_ces["S4"].alignment = ALIGN_CENTER
ws_ces["S4"].fill = FILL_PURPLE_HEADER

# RA4: cols AA to AG (7 CEs, idx 27 to 33)
ws_ces.merge_cells("AA4:AG4")
ws_ces["AA4"] = "RA4 (24%) — Interactividad, Animaciones, Framework Frontend Angular y Formularios"
ws_ces["AA4"].font = FONT_HEADER
ws_ces["AA4"].alignment = ALIGN_CENTER
ws_ces["AA4"].fill = FILL_ORANGE_HEADER

# RA5: cols AH to AO (8 CEs, idx 34 to 41)
ws_ces.merge_cells("AH4:AO4")
ws_ces["AH4"] = "RA5 (16%) — Accesibilidad Web Universal (WCAG 2.2, WAI-ARIA) y Auditorías"
ws_ces["AH4"].font = FONT_HEADER
ws_ces["AH4"].alignment = ALIGN_CENTER
ws_ces["AH4"].fill = FILL_GREEN_HEADER

# RA6: cols AP to AU (6 CEs, idx 42 to 47)
ws_ces.merge_cells("AP4:AU4")
ws_ces["AP4"] = "RA6 (12%) — Usabilidad Web, Heurísticas de Nielsen, Métricas SUS y DCU"
ws_ces["AP4"].font = FONT_HEADER
ws_ces["AP4"].alignment = ALIGN_CENTER
ws_ces["AP4"].fill = FILL_CYAN_HEADER

# Summary of CEs
ws_ces.merge_cells("AV4:AW4")
ws_ces["AV4"] = "RESUMEN DE CRITERIOS"
ws_ces["AV4"].font = FONT_HEADER
ws_ces["AV4"].alignment = ALIGN_CENTER
ws_ces["AV4"].fill = FILL_NAVY

# Row 5: Column headers with CE codes
ws_ces.column_dimensions["A"].width = 5
ws_ces.cell(row=5, column=1, value="Nº").font = FONT_HEADER
ws_ces.cell(row=5, column=1).alignment = ALIGN_CENTER
ws_ces.cell(row=5, column=1).fill = FILL_NAVY
ws_ces.cell(row=5, column=1).border = HEADER_BORDER

ws_ces.column_dimensions["B"].width = 24
ws_ces.cell(row=5, column=2, value="Apellidos, Nombre").font = FONT_HEADER
ws_ces.cell(row=5, column=2).alignment = ALIGN_LEFT
ws_ces.cell(row=5, column=2).fill = FILL_NAVY
ws_ces.cell(row=5, column=2).border = HEADER_BORDER

ws_ces.row_dimensions[5].height = 30
for c_i, crit in enumerate(CRITERIA_DATA, start=3):
    col_let = get_column_letter(c_i)
    ws_ces.column_dimensions[col_let].width = 9
    cell = ws_ces.cell(row=5, column=c_i, value=crit[2])
    cell.font = FONT_HEADER
    cell.alignment = ALIGN_CENTER
    cell.border = HEADER_BORDER
    ra_code = crit[0]
    if ra_code == "RA1":
        cell.fill = FILL_BLUE_HEADER
    elif ra_code == "RA2":
        cell.fill = FILL_TEAL_HEADER
    elif ra_code == "RA3":
        cell.fill = FILL_PURPLE_HEADER
    elif ra_code == "RA4":
        cell.fill = FILL_ORANGE_HEADER
    elif ra_code == "RA5":
        cell.fill = FILL_GREEN_HEADER
    else:
        cell.fill = FILL_CYAN_HEADER

ws_ces.column_dimensions["AV"].width = 12
ws_ces.cell(row=5, column=48, value="Media CEs\nSuperados").font = FONT_HEADER
ws_ces.cell(row=5, column=48).alignment = ALIGN_CENTER
ws_ces.cell(row=5, column=48).fill = FILL_NAVY
ws_ces.cell(row=5, column=48).border = HEADER_BORDER

ws_ces.column_dimensions["AW"].width = 12
ws_ces.cell(row=5, column=49, value="Nº CEs >= 5\n(de 45)").font = FONT_HEADER
ws_ces.cell(row=5, column=49).alignment = ALIGN_CENTER
ws_ces.cell(row=5, column=49).fill = FILL_NAVY
ws_ces.cell(row=5, column=49).border = HEADER_BORDER

# Student rows (Rows 6 to 20 in Calculo CEs)
for r_idx, (apell, nom) in enumerate(STUDENTS, start=6):
    ws_ces.row_dimensions[r_idx].height = 20
    is_zebra = (r_idx % 2 == 0)
    row_fill = FILL_ZEBRA if is_zebra else PatternFill(fill_type=None)
    
    # Nº & Nombre
    c1 = ws_ces.cell(row=r_idx, column=1, value=r_idx-5)
    c1.alignment = ALIGN_CENTER
    c1.border = CELL_BORDER
    c1.fill = row_fill
    c1.font = FONT_BODY
    
    c2 = ws_ces.cell(row=r_idx, column=2, value=f"{apell}, {nom}")
    c2.alignment = ALIGN_LEFT
    c2.border = CELL_BORDER
    c2.fill = row_fill
    c2.font = FONT_BODY_BOLD
    
    for c_i in range(45):
        target_col = 3 + c_i
        mat_row = 6 + c_i
        cell_ce = ws_ces.cell(row=r_idx, column=target_col)
        
        # Dynamic formula averaging tasks where 'Matriz Criterios' has "X"
        formula = f'=IF(SUMPRODUCT((\'Matriz Criterios\'!$H${mat_row}:$V${mat_row}="X")*ISNUMBER(\'Registro Notas\'!$D{r_idx}:$R{r_idx}))=0, "-", SUMPRODUCT((\'Matriz Criterios\'!$H${mat_row}:$V${mat_row}="X")*ISNUMBER(\'Registro Notas\'!$D{r_idx}:$R{r_idx})*\'Registro Notas\'!$D{r_idx}:$R{r_idx})/SUMPRODUCT((\'Matriz Criterios\'!$H${mat_row}:$V${mat_row}="X")*ISNUMBER(\'Registro Notas\'!$D{r_idx}:$R{r_idx})))'
        cell_ce.value = formula
        cell_ce.alignment = ALIGN_CENTER
        cell_ce.border = CELL_BORDER
        cell_ce.fill = row_fill
        cell_ce.font = FONT_BODY
        cell_ce.number_format = "0.00"
        
    # Col AV: Media CEs Superados
    cAV = ws_ces.cell(row=r_idx, column=48)
    cAV.value = f"=AVERAGE(C{r_idx}:AU{r_idx})"
    cAV.alignment = ALIGN_CENTER
    cAV.border = CELL_BORDER
    cAV.fill = FILL_TOTAL
    cAV.font = FONT_BODY_BOLD
    cAV.number_format = "0.00"
    
    # Col AW: Nº CEs >= 5
    cAW = ws_ces.cell(row=r_idx, column=49)
    cAW.value = f'=COUNTIF(C{r_idx}:AU{r_idx}, ">=5")'
    cAW.alignment = ALIGN_CENTER
    cAW.border = CELL_BORDER
    cAW.fill = FILL_GREEN_LIGHT
    cAW.font = FONT_BODY_BOLD

# Group Average Row
row_ce_avg = 21
ws_ces.row_dimensions[row_ce_avg].height = 24
ws_ces.merge_cells(f"A{row_ce_avg}:B{row_ce_avg}")
c_avg_lbl_ce = ws_ces.cell(row=row_ce_avg, column=1, value="PROMEDIO DEL GRUPO")
c_avg_lbl_ce.font = FONT_HEADER_DARK
c_avg_lbl_ce.alignment = ALIGN_CENTER
c_avg_lbl_ce.fill = FILL_TOTAL
c_avg_lbl_ce.border = TOTAL_BORDER
ws_ces.cell(row=row_ce_avg, column=2).border = TOTAL_BORDER

for col_idx in range(3, 50):
    col_let = get_column_letter(col_idx)
    c_avg = ws_ces.cell(row=row_ce_avg, column=col_idx)
    c_avg.value = f"=AVERAGE({col_let}6:{col_let}20)"
    c_avg.font = FONT_BODY_BOLD
    c_avg.alignment = ALIGN_CENTER
    c_avg.fill = FILL_TOTAL
    c_avg.border = TOTAL_BORDER
    c_avg.number_format = "0.00"

ws_ces.conditional_formatting.add("C6:AU20", CellIsRule(operator="greaterThanOrEqual", formula=["5.0"], stopIfTrue=True, fill=green_fill, font=green_font))
ws_ces.conditional_formatting.add("C6:AU20", CellIsRule(operator="lessThan", formula=["5.0"], stopIfTrue=True, fill=red_fill, font=red_font))


# =============================================================
# SHEET 4: CÁLCULO POR RESULTADOS DE APRENDIZAJE (RAs)
# =============================================================
ws_ras = wb.create_sheet(title="Calculo RAs")
ws_ras.views.sheetView[0].showGridLines = True

ws_ras.merge_cells("A1:I1")
ws_ras["A1"] = "CALIFICACIÓN POR RESULTADOS DE APRENDIZAJE (RA1 a RA6) — PONDERACIÓN OFICIAL DIW"
ws_ras["A1"].font = FONT_TITLE
ws_ras["A1"].fill = FILL_NAVY
ws_ras["A1"].alignment = ALIGN_CENTER
ws_ras.row_dimensions[1].height = 36

ws_ras.merge_cells("A2:I2")
ws_ras["A2"] = "Cada Resultado de Aprendizaje se obtiene de sus Criterios oficiales. La Nota Final aplica los coeficientes del Decreto 104/2024 y la Orden de 16/06/2011."
ws_ras["A2"].font = FONT_SUBTITLE
ws_ras["A2"].fill = FILL_SUBHEADER
ws_ras["A2"].alignment = ALIGN_CENTER
ws_ras.row_dimensions[2].height = 20

headers_ras = [
    ("Nº", 5),
    ("Apellidos, Nombre", 25),
    ("RA1 (12%)\nPlanificación UI\nFigma & Estilos", 16),
    ("RA2 (20%)\nMaquetación Web\nCSS, Grid, Flex, TW4", 17),
    ("RA3 (16%)\nMultimedia Web\nSVG, Vídeo & TRLPI", 16),
    ("RA4 (24%)\nInteractividad Web\nAngular & Forms", 16),
    ("RA5 (16%)\nAccesibilidad Web\nWCAG 2.2 / WAI-ARIA", 16),
    ("RA6 (12%)\nUsabilidad Web\nHeurísticas & DCU", 16),
    ("CALIFICACIÓN FINAL\nORDINARIA (100%)", 18)
]

ws_ras.row_dimensions[4].height = 42
for col_idx, (h_text, width) in enumerate(headers_ras, start=1):
    col_let = get_column_letter(col_idx)
    ws_ras.column_dimensions[col_let].width = width
    cell = ws_ras.cell(row=4, column=col_idx, value=h_text)
    cell.font = FONT_HEADER
    cell.alignment = ALIGN_CENTER
    cell.border = HEADER_BORDER
    if col_idx <= 2:
        cell.fill = FILL_NAVY
    elif col_idx <= 8:
        cell.fill = FILL_BLUE_HEADER
    else:
        cell.fill = FILL_GREEN_HEADER

# Fill Student Rows for RAs
for r_idx, (apell, nom) in enumerate(STUDENTS, start=6):
    ws_ras.row_dimensions[r_idx].height = 20
    is_zebra = (r_idx % 2 == 0)
    row_fill = FILL_ZEBRA if is_zebra else PatternFill(fill_type=None)
    
    # Nº & Nombre
    c1 = ws_ras.cell(row=r_idx, column=1, value=r_idx-5)
    c1.alignment = ALIGN_CENTER
    c1.border = CELL_BORDER
    c1.fill = row_fill
    c1.font = FONT_BODY
    
    c2 = ws_ras.cell(row=r_idx, column=2, value=f"{apell}, {nom}")
    c2.alignment = ALIGN_LEFT
    c2.border = CELL_BORDER
    c2.fill = row_fill
    c2.font = FONT_BODY_BOLD
    
    # RA1 (12%): CE1.a to CE1.f -> 'Calculo CEs'!C{r_idx}:H{r_idx} (cols 3 to 8)
    c_ra1 = ws_ras.cell(row=r_idx, column=3)
    c_ra1.value = f"=AVERAGE('Calculo CEs'!C{r_idx}:H{r_idx})"
    c_ra1.alignment = ALIGN_CENTER
    c_ra1.border = CELL_BORDER
    c_ra1.fill = row_fill
    c_ra1.font = FONT_BODY
    c_ra1.number_format = "0.00"
    
    # RA2 (20%): CE2.a to CE2.j -> 'Calculo CEs'!I{r_idx}:R{r_idx} (cols 9 to 18)
    c_ra2 = ws_ras.cell(row=r_idx, column=4)
    c_ra2.value = f"=AVERAGE('Calculo CEs'!I{r_idx}:R{r_idx})"
    c_ra2.alignment = ALIGN_CENTER
    c_ra2.border = CELL_BORDER
    c_ra2.fill = row_fill
    c_ra2.font = FONT_BODY
    c_ra2.number_format = "0.00"
    
    # RA3 (16%): CE3.a to CE3.h -> 'Calculo CEs'!S{r_idx}:Z{r_idx} (cols 19 to 26)
    c_ra3 = ws_ras.cell(row=r_idx, column=5)
    c_ra3.value = f"=AVERAGE('Calculo CEs'!S{r_idx}:Z{r_idx})"
    c_ra3.alignment = ALIGN_CENTER
    c_ra3.border = CELL_BORDER
    c_ra3.fill = row_fill
    c_ra3.font = FONT_BODY
    c_ra3.number_format = "0.00"
    
    # RA4 (24%): CE4.a (2%), CE4.b (2%), CE4.c-g (4% each) -> 'Calculo CEs'!AA{r_idx}:AG{r_idx}
    # Weighted average according to Andalusian official regulation
    c_ra4 = ws_ras.cell(row=r_idx, column=6)
    c_ra4.value = f"=('Calculo CEs'!AA{r_idx}*0.02 + 'Calculo CEs'!AB{r_idx}*0.02 + 'Calculo CEs'!AC{r_idx}*0.04 + 'Calculo CEs'!AD{r_idx}*0.04 + 'Calculo CEs'!AE{r_idx}*0.04 + 'Calculo CEs'!AF{r_idx}*0.04 + 'Calculo CEs'!AG{r_idx}*0.04) / 0.24"
    c_ra4.alignment = ALIGN_CENTER
    c_ra4.border = CELL_BORDER
    c_ra4.fill = row_fill
    c_ra4.font = FONT_BODY
    c_ra4.number_format = "0.00"
    
    # RA5 (16%): CE5.a to CE5.h -> 'Calculo CEs'!AH{r_idx}:AO{r_idx} (cols 34 to 41)
    c_ra5 = ws_ras.cell(row=r_idx, column=7)
    c_ra5.value = f"=AVERAGE('Calculo CEs'!AH{r_idx}:AO{r_idx})"
    c_ra5.alignment = ALIGN_CENTER
    c_ra5.border = CELL_BORDER
    c_ra5.fill = row_fill
    c_ra5.font = FONT_BODY
    c_ra5.number_format = "0.00"
    
    # RA6 (12%): CE6.a to CE6.f -> 'Calculo CEs'!AP{r_idx}:AU{r_idx} (cols 42 to 47)
    c_ra6 = ws_ras.cell(row=r_idx, column=8)
    c_ra6.value = f"=AVERAGE('Calculo CEs'!AP{r_idx}:AU{r_idx})"
    c_ra6.alignment = ALIGN_CENTER
    c_ra6.border = CELL_BORDER
    c_ra6.fill = row_fill
    c_ra6.font = FONT_BODY
    c_ra6.number_format = "0.00"
    
    # Calificacion Final Ordinaria Oficial DIW (12% + 20% + 16% + 24% + 16% + 12% = 100%)
    c_tot = ws_ras.cell(row=r_idx, column=9)
    c_tot.value = f"=C{r_idx}*0.12 + D{r_idx}*0.20 + E{r_idx}*0.16 + F{r_idx}*0.24 + G{r_idx}*0.16 + H{r_idx}*0.12"
    c_tot.alignment = ALIGN_CENTER
    c_tot.border = CELL_BORDER
    c_tot.fill = FILL_TOTAL
    c_tot.font = Font(name="Segoe UI", size=10, bold=True, color="0F172A")
    c_tot.number_format = "0.00"

# Average Row
row_ras_avg = 21
ws_ras.row_dimensions[row_ras_avg].height = 24
ws_ras.merge_cells(f"A{row_ras_avg}:B{row_ras_avg}")
c_avg_lbl_ras = ws_ras.cell(row=row_ras_avg, column=1, value="PROMEDIO DEL GRUPO")
c_avg_lbl_ras.font = FONT_HEADER_DARK
c_avg_lbl_ras.alignment = ALIGN_CENTER
c_avg_lbl_ras.fill = FILL_TOTAL
c_avg_lbl_ras.border = TOTAL_BORDER
ws_ras.cell(row=row_ras_avg, column=2).border = TOTAL_BORDER

for col_idx in range(3, 10):
    col_let = get_column_letter(col_idx)
    c_avg = ws_ras.cell(row=row_ras_avg, column=col_idx)
    c_avg.value = f"=AVERAGE({col_let}6:{col_let}20)"
    c_avg.font = FONT_BODY_BOLD
    c_avg.alignment = ALIGN_CENTER
    c_avg.fill = FILL_TOTAL
    c_avg.border = TOTAL_BORDER
    c_avg.number_format = "0.00"

ws_ras.conditional_formatting.add("I6:I20", CellIsRule(operator="greaterThanOrEqual", formula=["5.0"], stopIfTrue=True, fill=green_fill, font=green_font))
ws_ras.conditional_formatting.add("I6:I20", CellIsRule(operator="lessThan", formula=["5.0"], stopIfTrue=True, fill=red_fill, font=red_font))


# =============================================================
# SHEET 5: PANEL DE CONTROL Y RESUMEN EJECUTIVO
# =============================================================
ws_dash = wb.create_sheet(title="Panel de Control")
ws_dash.views.sheetView[0].showGridLines = True

# Title Header
ws_dash.merge_cells("A1:N1")
ws_dash["A1"] = "PANEL DE CONTROL GENERAL — DISEÑO DE INTERFACES WEB (2º DAW)"
ws_dash["A1"].font = FONT_TITLE
ws_dash["A1"].fill = FILL_NAVY
ws_dash["A1"].alignment = ALIGN_CENTER
ws_dash.row_dimensions[1].height = 36

ws_dash.merge_cells("A2:N2")
ws_dash["A2"] = "Síntesis Integral: Trimestres, Resultados de Aprendizaje Oficiales (RA1-RA6), Calificación Ordinaria y Acceso a Dual (71 h)"
ws_dash["A2"].font = FONT_SUBTITLE
ws_dash["A2"].fill = FILL_SUBHEADER
ws_dash["A2"].alignment = ALIGN_CENTER
ws_dash.row_dimensions[2].height = 20

# Top KPI Cards (Rows 4 to 6)
ws_dash.merge_cells("B4:C4")
ws_dash["B4"] = "ALUMNADO MATRICULADO"
ws_dash["B4"].font = FONT_KPI_LBL
ws_dash["B4"].alignment = ALIGN_CENTER
ws_dash.merge_cells("B5:C6")
ws_dash["B5"] = '=COUNTA(A9:A23)'
ws_dash["B5"].font = FONT_KPI_VAL
ws_dash["B5"].alignment = ALIGN_CENTER
ws_dash["B5"].fill = FILL_BLUE_LIGHT

ws_dash.merge_cells("E4:F4")
ws_dash["E4"] = "APROBADOS EVAL. ORDINARIA"
ws_dash["E4"].font = FONT_KPI_LBL
ws_dash["E4"].alignment = ALIGN_CENTER
ws_dash.merge_cells("E5:F6")
ws_dash["E5"] = '=COUNTIF(L9:L23, ">=5")'
ws_dash["E5"].font = Font(name="Segoe UI", size=16, bold=True, color="15803D")
ws_dash["E5"].alignment = ALIGN_CENTER
ws_dash["E5"].fill = FILL_GREEN_LIGHT

ws_dash.merge_cells("H4:I4")
ws_dash["H4"] = "SUSPENSOS EVAL. ORDINARIA"
ws_dash["H4"].font = FONT_KPI_LBL
ws_dash["H4"].alignment = ALIGN_CENTER
ws_dash.merge_cells("H5:I6")
ws_dash["H5"] = '=COUNTIF(L9:L23, "<5")'
ws_dash["H5"].font = Font(name="Segoe UI", size=16, bold=True, color="DC2626")
ws_dash["H5"].alignment = ALIGN_CENTER
ws_dash["H5"].fill = PatternFill(start_color="FEE2E2", end_color="FEE2E2", fill_type="solid")

ws_dash.merge_cells("K4:L4")
ws_dash["K4"] = "NOTA MEDIA DEL GRUPO"
ws_dash["K4"].font = FONT_KPI_LBL
ws_dash["K4"].alignment = ALIGN_CENTER
ws_dash.merge_cells("K5:L6")
ws_dash["K5"] = '=AVERAGE(L9:L23)'
ws_dash["K5"].font = FONT_KPI_VAL
ws_dash["K5"].alignment = ALIGN_CENTER
ws_dash["K5"].fill = FILL_TOTAL
ws_dash["K5"].number_format = "0.00"

ws_dash.merge_cells("M4:N4")
ws_dash["M4"] = "TASA DE ÉXITO ACADÉMICO"
ws_dash["M4"].font = FONT_KPI_LBL
ws_dash["M4"].alignment = ALIGN_CENTER
ws_dash.merge_cells("M5:N6")
ws_dash["M5"] = '=E5/B5'
ws_dash["M5"].font = Font(name="Segoe UI", size=16, bold=True, color="1E3A8A")
ws_dash["M5"].alignment = ALIGN_CENTER
ws_dash["M5"].fill = FILL_PURPLE_LIGHT
ws_dash["M5"].number_format = "0.0%"

# Table Headers (Row 8)
headers_dash = [
    ("Nº", 5),
    ("Apellidos, Nombre", 24),
    ("1º Trim\n(T1)", 10),
    ("2º Trim\n(T2)", 10),
    ("RA1\n(12%)", 8),
    ("RA2\n(20%)", 8),
    ("RA3\n(16%)", 8),
    ("RA4\n(24%)", 8),
    ("RA5\n(16%)", 8),
    ("RA6\n(12%)", 8),
    ("Media\nT1-T2", 9),
    ("Nota Final\nOrdinaria (Marzo)", 16),
    ("Calificación Cualitativa", 18),
    ("Acceso a Dual en Empresa", 22)
]

ws_dash.row_dimensions[8].height = 40
for col_idx, (h_text, width) in enumerate(headers_dash, start=1):
    col_let = get_column_letter(col_idx)
    ws_dash.column_dimensions[col_let].width = width
    cell = ws_dash.cell(row=8, column=col_idx, value=h_text)
    cell.font = FONT_HEADER
    cell.alignment = ALIGN_CENTER
    cell.border = HEADER_BORDER
    if col_idx <= 2:
        cell.fill = FILL_NAVY
    elif col_idx <= 4:
        cell.fill = FILL_TEAL_HEADER
    elif col_idx <= 10:
        cell.fill = FILL_BLUE_HEADER
    elif col_idx <= 12:
        cell.fill = FILL_GREEN_HEADER
    else:
        cell.fill = FILL_PURPLE_HEADER

# Student rows (Rows 9 to 23 in Panel de Control)
for r_idx, (apell, nom) in enumerate(STUDENTS, start=9):
    ws_dash.row_dimensions[r_idx].height = 20
    is_zebra = (r_idx % 2 == 0)
    row_fill = FILL_ZEBRA if is_zebra else PatternFill(fill_type=None)
    src_row = r_idx - 3  # Maps row 9 to row 6 in other sheets
    
    # Nº & Nombre
    c1 = ws_dash.cell(row=r_idx, column=1, value=r_idx-8)
    c1.alignment = ALIGN_CENTER
    c1.border = CELL_BORDER
    c1.fill = row_fill
    c1.font = FONT_BODY
    
    c2 = ws_dash.cell(row=r_idx, column=2, value=f"{apell}, {nom}")
    c2.alignment = ALIGN_LEFT
    c2.border = CELL_BORDER
    c2.fill = row_fill
    c2.font = FONT_BODY_BOLD
    
    # 1º Trimestre (from 'Registro Notas'!S{src_row})
    c3 = ws_dash.cell(row=r_idx, column=3)
    c3.value = f"='Registro Notas'!S{src_row}"
    c3.alignment = ALIGN_CENTER
    c3.border = CELL_BORDER
    c3.fill = FILL_BLUE_LIGHT if is_zebra else PatternFill(start_color="EFF6FF", end_color="EFF6FF", fill_type="solid")
    c3.font = FONT_BODY_BOLD
    c3.number_format = "0.00"
    
    # 2º Trimestre (from 'Registro Notas'!T{src_row})
    c4 = ws_dash.cell(row=r_idx, column=4)
    c4.value = f"='Registro Notas'!T{src_row}"
    c4.alignment = ALIGN_CENTER
    c4.border = CELL_BORDER
    c4.fill = FILL_TEAL_LIGHT if is_zebra else PatternFill(start_color="F0FDFA", end_color="F0FDFA", fill_type="solid")
    c4.font = FONT_BODY_BOLD
    c4.number_format = "0.00"
    
    # RA1 to RA6 (from 'Calculo RAs'!C{src_row}:H{src_row})
    for ra_i in range(6):
        c_target = 5 + ra_i
        ra_col_let = get_column_letter(3 + ra_i)
        c_ra = ws_dash.cell(row=r_idx, column=c_target)
        c_ra.value = f"='Calculo RAs'!{ra_col_let}{src_row}"
        c_ra.alignment = ALIGN_CENTER
        c_ra.border = CELL_BORDER
        c_ra.fill = row_fill
        c_ra.font = FONT_BODY
        c_ra.number_format = "0.00"
        
    # Media T1-T2 (Col K, 11)
    c_med = ws_dash.cell(row=r_idx, column=11)
    c_med.value = f"=AVERAGE(C{r_idx}, D{r_idx})"
    c_med.alignment = ALIGN_CENTER
    c_med.border = CELL_BORDER
    c_med.fill = row_fill
    c_med.font = FONT_BODY
    c_med.number_format = "0.00"
    
    # Nota Final Ordinaria (from 'Calculo RAs'!I{src_row})
    c_fin = ws_dash.cell(row=r_idx, column=12)
    c_fin.value = f"='Calculo RAs'!I{src_row}"
    c_fin.alignment = ALIGN_CENTER
    c_fin.border = CELL_BORDER
    c_fin.fill = FILL_TOTAL
    c_fin.font = Font(name="Segoe UI", size=10, bold=True, color="0F172A")
    c_fin.number_format = "0.00"
    
    # Calificacion Cualitativa (Col M, 13)
    c_cual = ws_dash.cell(row=r_idx, column=13)
    c_cual.value = f'=IF(L{r_idx}>=9, "SOBRESALIENTE", IF(L{r_idx}>=7, "NOTABLE", IF(L{r_idx}>=6, "BIEN", IF(L{r_idx}>=5, "SUFICIENTE", "INSUFICIENTE"))))'
    c_cual.alignment = ALIGN_CENTER
    c_cual.border = CELL_BORDER
    c_cual.fill = row_fill
    c_cual.font = FONT_BODY_BOLD
    
    # Acceso a Dual (Col N, 14)
    c_dual = ws_dash.cell(row=r_idx, column=14)
    c_dual.value = f'=IF(L{r_idx}>=5, "AUTORIZADO (DUAL)", "PENDIENTE RECUP.")'
    c_dual.alignment = ALIGN_CENTER
    c_dual.border = CELL_BORDER
    c_dual.fill = row_fill
    c_dual.font = FONT_BODY_BOLD

# Group Average Row
row_dash_avg = 24
ws_dash.row_dimensions[row_dash_avg].height = 24
ws_dash.merge_cells(f"A{row_dash_avg}:B{row_dash_avg}")
c_avg_lbl_d = ws_dash.cell(row=row_dash_avg, column=1, value="PROMEDIO DEL GRUPO")
c_avg_lbl_d.font = FONT_HEADER_DARK
c_avg_lbl_d.alignment = ALIGN_CENTER
c_avg_lbl_d.fill = FILL_TOTAL
c_avg_lbl_d.border = TOTAL_BORDER
ws_dash.cell(row=row_dash_avg, column=2).border = TOTAL_BORDER

for col_idx in range(3, 13):
    col_let = get_column_letter(col_idx)
    c_avg = ws_dash.cell(row=row_dash_avg, column=col_idx)
    c_avg.value = f"=AVERAGE({col_let}9:{col_let}23)"
    c_avg.font = FONT_BODY_BOLD
    c_avg.alignment = ALIGN_CENTER
    c_avg.fill = FILL_TOTAL
    c_avg.border = TOTAL_BORDER
    c_avg.number_format = "0.00"

ws_dash.cell(row=row_dash_avg, column=13, value="").fill = FILL_TOTAL
ws_dash.cell(row=row_dash_avg, column=13).border = TOTAL_BORDER
ws_dash.cell(row=row_dash_avg, column=14, value="").fill = FILL_TOTAL
ws_dash.cell(row=row_dash_avg, column=14).border = TOTAL_BORDER

ws_dash.conditional_formatting.add("L9:L23", CellIsRule(operator="greaterThanOrEqual", formula=["5.0"], stopIfTrue=True, fill=green_fill, font=green_font))
ws_dash.conditional_formatting.add("L9:L23", CellIsRule(operator="lessThan", formula=["5.0"], stopIfTrue=True, fill=red_fill, font=red_font))
ws_dash.conditional_formatting.add("N9:N23", CellIsRule(operator="equal", formula=['"AUTORIZADO (DUAL)"'], stopIfTrue=True, fill=green_fill, font=green_font))
ws_dash.conditional_formatting.add("N9:N23", CellIsRule(operator="equal", formula=['"PENDIENTE RECUP."'], stopIfTrue=True, fill=red_fill, font=red_font))


# =============================================================
# SHEET 6: SEGUIMIENTO DUAL Y EXTRAORDINARIA
# =============================================================
ws_dual = wb.create_sheet(title="Seguimiento Dual y Extraord")
ws_dual.views.sheetView[0].showGridLines = True

ws_dual.merge_cells("A1:J1")
ws_dual["A1"] = "FASE DE FORMACIÓN DUAL EN EMPRESA (T3 - 71 h) Y CONVOCATORIA EXTRAORDINARIA"
ws_dual["A1"].font = FONT_TITLE
ws_dual["A1"].fill = FILL_NAVY
ws_dual["A1"].alignment = ALIGN_CENTER
ws_dual.row_dimensions[1].height = 36

ws_dual.merge_cells("A2:J2")
ws_dual["A2"] = "Orden de 26 de septiembre de 2025 (Dual Andalucía) | Periodo en Empresa: Marzo a Junio 2026 (71 h vinculadas a DIW)"
ws_dual["A2"].font = FONT_SUBTITLE
ws_dual["A2"].fill = FILL_SUBHEADER
ws_dual["A2"].alignment = ALIGN_CENTER
ws_dual.row_dimensions[2].height = 20

headers_dual = [
    ("Nº", 5),
    ("Apellidos, Nombre", 25),
    ("Nota Ordinaria\n(Marzo)", 15),
    ("Empresa Asignada", 22),
    ("Tutor/a Laboral", 20),
    ("Horas Dual\n(Módulo 71 h)", 14),
    ("Valoración Empresa\n(Apto / No Apto)", 18),
    ("RAs Pendientes\n(Extraordinaria)", 18),
    ("Nota Convocatoria\nExtraordinaria (Junio)", 20),
    ("Calificación Definitiva\nCurso Académico", 20)
]

ws_dual.row_dimensions[4].height = 38
for col_idx, (h_text, width) in enumerate(headers_dual, start=1):
    col_let = get_column_letter(col_idx)
    ws_dual.column_dimensions[col_let].width = width
    cell = ws_dual.cell(row=4, column=col_idx, value=h_text)
    cell.font = FONT_HEADER
    cell.alignment = ALIGN_CENTER
    cell.border = HEADER_BORDER
    if col_idx <= 2:
        cell.fill = FILL_NAVY
    elif col_idx <= 7:
        cell.fill = FILL_TEAL_HEADER
    else:
        cell.fill = FILL_PURPLE_HEADER

for r_idx, (apell, nom) in enumerate(STUDENTS, start=5):
    ws_dual.row_dimensions[r_idx].height = 20
    is_zebra = (r_idx % 2 == 0)
    row_fill = FILL_ZEBRA if is_zebra else PatternFill(fill_type=None)
    dash_row = r_idx + 4  # Maps row 5 to row 9 in Dashboard
    
    # Nº & Nombre
    c1 = ws_dual.cell(row=r_idx, column=1, value=r_idx-4)
    c1.alignment = ALIGN_CENTER
    c1.border = CELL_BORDER
    c1.fill = row_fill
    c1.font = FONT_BODY
    
    c2 = ws_dual.cell(row=r_idx, column=2, value=f"{apell}, {nom}")
    c2.alignment = ALIGN_LEFT
    c2.border = CELL_BORDER
    c2.fill = row_fill
    c2.font = FONT_BODY_BOLD
    
    # Nota Ordinaria (Pulled from Dashboard)
    c3 = ws_dual.cell(row=r_idx, column=3)
    c3.value = f"='Panel de Control'!L{dash_row}"
    c3.alignment = ALIGN_CENTER
    c3.border = CELL_BORDER
    c3.fill = FILL_TOTAL
    c3.font = FONT_BODY_BOLD
    c3.number_format = "0.00"
    
    # Empresa
    c4 = ws_dual.cell(row=r_idx, column=4, value="WebCraft Studio S.L." if r_idx % 2 == 0 else "Frontend Solutions Andalucía")
    c4.alignment = ALIGN_LEFT
    c4.border = CELL_BORDER
    c4.fill = row_fill
    c4.font = FONT_BODY
    
    # Tutor
    c5 = ws_dual.cell(row=r_idx, column=5, value="D. Alejandro Montes" if r_idx % 2 == 0 else "Dña. Silvia Valenzuela")
    c5.alignment = ALIGN_LEFT
    c5.border = CELL_BORDER
    c5.fill = row_fill
    c5.font = FONT_BODY
    
    # Horas Dual (71 h para DIW en 2º DAW)
    c6 = ws_dual.cell(row=r_idx, column=6, value=71)
    c6.alignment = ALIGN_CENTER
    c6.border = CELL_BORDER
    c6.fill = row_fill
    c6.font = FONT_BODY
    
    # Valoración
    c7 = ws_dual.cell(row=r_idx, column=7)
    c7.value = f'=IF(C{r_idx}>=5, "APTO", "PENDIENTE")'
    c7.alignment = ALIGN_CENTER
    c7.border = CELL_BORDER
    c7.fill = row_fill
    c7.font = FONT_BODY_BOLD
    
    # RAs Pendientes
    c8 = ws_dual.cell(row=r_idx, column=8, value=f'=IF(C{r_idx}<5, "RA2, RA4", "Ninguno")')
    c8.alignment = ALIGN_CENTER
    c8.border = CELL_BORDER
    c8.fill = row_fill
    c8.font = FONT_BODY
    
    # Nota Extraordinaria
    c9 = ws_dual.cell(row=r_idx, column=9, value="")
    c9.alignment = ALIGN_CENTER
    c9.border = CELL_BORDER
    c9.fill = row_fill
    c9.font = FONT_BODY
    c9.number_format = "0.00"
    
    # Calificación Definitiva
    c10 = ws_dual.cell(row=r_idx, column=10)
    c10.value = f'=IF(ISBLANK(I{r_idx}), C{r_idx}, MAX(C{r_idx}, I{r_idx}))'
    c10.alignment = ALIGN_CENTER
    c10.border = CELL_BORDER
    c10.fill = FILL_GREEN_LIGHT
    c10.font = FONT_BODY_BOLD
    c10.number_format = "0.00"

ws_dual.conditional_formatting.add("J5:J19", CellIsRule(operator="greaterThanOrEqual", formula=["5.0"], stopIfTrue=True, fill=green_fill, font=green_font))
ws_dual.conditional_formatting.add("J5:J19", CellIsRule(operator="lessThan", formula=["5.0"], stopIfTrue=True, fill=red_fill, font=red_font))


# =============================================================
# SHEET 7: GUÍA DE FUNCIONAMIENTO INTERACTIVA
# =============================================================
ws_guide = wb.create_sheet(title="Guía de Funcionamiento")
ws_guide.views.sheetView[0].showGridLines = True

ws_guide.merge_cells("A1:G1")
ws_guide["A1"] = "GUÍA DE USO Y ARQUITECTURA DEL SISTEMA DE EVALUACIÓN — DIW (2º DAW)"
ws_guide["A1"].font = FONT_TITLE
ws_guide["A1"].fill = FILL_NAVY
ws_guide["A1"].alignment = ALIGN_CENTER
ws_guide.row_dimensions[1].height = 36

guide_sections = [
    ("1. Filosofía y Funcionamiento Dinámico",
     "Esta hoja de cálculo implementa un motor de evaluación competencial bidireccional completamente automatizado para DIW:\n"
     "• La 'Matriz Criterios' contiene los 45 Criterios de Evaluación oficiales agrupados en los 6 Resultados de Aprendizaje.\n"
     "• En cualquier momento del curso puedes marcar o desmarcar con una 'X' qué criterios evalúa cada tarea o examen.\n"
     "• En la FILA 52 se calcula automáticamente la SUMA EXACTA DE LOS PESOS de los criterios marcados con 'X' para esa tarea.\n"
     "• En la FILA 53 se calcula el % DE PONDERACIÓN EN EL TRIMESTRE, normalizado a 100% (para que el boletín de notas trimestral sume 100%).\n"
     "• El motor recalcula en tiempo real las notas individuales de cada criterio, el avance de cada RA y las notas trimestrales y finales."),
    
    ("2. Flujo de Trabajo para el Docente",
     "PASO 1: Configurar la Matriz Criterios\n"
     "Revisa las columnas H a V (tareas T01 a T15). Coloca una 'X' en la fila del criterio que evalúe dicha tarea.\n"
     "La fila 51 te indica cuántos criterios evalúa cada tarea.\n"
     "La fila 52 calcula dinámicamente la suma directa de los pesos de dichos criterios sobre el total del módulo.\n"
     "La fila 53 rebalancea automáticamente los porcentajes dentro de cada trimestre sumando exactamente el 100%.\n\n"
     "PASO 2: Introducir Calificaciones en 'Registro Notas'\n"
     "Introduce las notas (0.00 a 10.00) obtenidas por los alumnos en cada tarea (columnas D a R).\n"
     "Las notas de 1º y 2º Trimestre se calculan automáticamente en las columnas S y T a partir de los pesos derivados de los criterios.\n\n"
     "PASO 3: Supervisar el 'Panel de Control'\n"
     "Observa las tarjetas de KPIs (Alumnos, Aprobados, Suspensos, Nota Media, Tasa de Éxito) y la tabla consolidada\n"
     "con la calificación oficial en marzo y la autorización automática para la estancia Dual en empresa (71 h)."),
    
    ("3. Robustez Matemática (Sin Ceros Prematuros)",
     "La fórmula implementada en cada criterio utiliza la función ISNUMBER combinada con SUMPRODUCT:\n"
     "Solo se promedian aquellas tareas que tienen una 'X' Y QUE ADEMÁS TIENEN NOTA INTRODUCIDA.\n"
     "Esto evita que un alumno aparezca con una nota suspensa en un criterio a principio de curso simplemente\n"
     "porque las tareas del segundo trimestre todavía no se han impartido o calificado."),
    
    ("4. Marco Normativo Integrado",
     "• Ley Orgánica 3/2022 y Real Decreto 659/2023 (Ordenación del Sistema de Formación Profesional).\n"
     "• Real Decreto 687/2010 y Real Decreto 405/2023 / RD 500/2024 (Currículo oficial y competencias de DAW).\n"
     "• Decreto 104/2024 (Ordenación de FP en Andalucía, derogando el Decreto 436/2008).\n"
     "• Orden de 18 de septiembre de 2025 (Evaluación y acreditación del alumnado de FP en Andalucía).\n"
     "• Orden de 26 de septiembre de 2025 (Regulación de la formación dual y estancias en empresa en Andalucía: 71 h DIW).")
]

ws_guide.column_dimensions["A"].width = 6
ws_guide.column_dimensions["B"].width = 85
for c in ["C", "D", "E", "F", "G"]:
    ws_guide.column_dimensions[c].width = 12

curr_row = 3
for title, text in guide_sections:
    ws_guide.row_dimensions[curr_row].height = 26
    ws_guide.merge_cells(f"B{curr_row}:G{curr_row}")
    cell_sec = ws_guide[f"B{curr_row}"]
    cell_sec.value = title
    cell_sec.font = Font(name="Segoe UI", size=11, bold=True, color="1E3A8A")
    cell_sec.fill = FILL_BLUE_LIGHT
    cell_sec.alignment = ALIGN_LEFT
    cell_sec.border = HEADER_BORDER
    curr_row += 1
    
    num_lines = text.count("\n") + 1
    ws_guide.row_dimensions[curr_row].height = max(50, num_lines * 18)
    ws_guide.merge_cells(f"B{curr_row}:G{curr_row}")
    cell_body = ws_guide[f"B{curr_row}"]
    cell_body.value = text
    cell_body.font = FONT_BODY
    cell_body.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
    cell_body.fill = FILL_ZEBRA
    cell_body.border = CELL_BORDER
    curr_row += 2


# -------------------------------------------------------------
# Save Workbook
# -------------------------------------------------------------
output_dir = r"e:\00. Clases\Apuntes\Diseño interfaces\Programación"
os.makedirs(output_dir, exist_ok=True)

excel_path = os.path.join(output_dir, "Hoja_Evaluacion_Avanzada_DIW_2DAW_2025_2026.xlsx")
excel_path_v2 = os.path.join(output_dir, "Hoja_Evaluacion_Avanzada_DIW_2DAW_2025_2026_v2.xlsx")

try:
    wb.save(excel_path)
    print(f"Hoja de evaluación avanzada para DIW guardada con éxito en:\n{excel_path}")
except PermissionError:
    wb.save(excel_path_v2)
    print(f"AVISO: El archivo principal está abierto en Excel. Se ha guardado en:\n{excel_path_v2}")
