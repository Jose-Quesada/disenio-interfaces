---
icon: lucide/accessibility
---

# Unidad 14: Accesibilidad Web

## Objetivos de aprendizaje

Al finalizar esta unidad, el alumnado será capaz de:

- Comprender el concepto de accesibilidad web en toda su amplitud, valorando su importancia desde las perspectivas legal, ética y de negocio, y reconociendo que la accesibilidad beneficia a todos los usuarios, no solo a aquellos con discapacidades permanentes.
- Identificar los diferentes tipos de discapacidad (visual, auditiva, motriz, cognitiva y neurológica) y comprender cómo cada una afecta a la interacción con contenidos web, desarrollando empatía hacia las diversas formas en que las personas acceden a la información digital.
- Conocer y aplicar la legislación vigente sobre accesibilidad web: el estándar europeo EN 301 549, el Real Decreto 1112/2018 sobre accesibilidad de sitios web del sector público en España, la Ley 11/2023 de trasposición de la Directiva Europea 2019/882 (European Accessibility Act), la ADA estadounidense y la Section 508.
- Dominar las Web Content Accessibility Guidelines (WCAG) en sus versiones 2.0, 2.1 y 2.2, comprendiendo la estructura jerárquica de Principios, Pautas y Criterios de Conformidad, y sabiendo diferenciar y aplicar los tres niveles de conformidad: A (mínimo), AA (estándar) y AAA (óptimo).
- Aplicar los cuatro principios POUR (Perceptible, Operable, Comprensible y Robusto) en el diseño y desarrollo de interfaces web, comprendiendo cada criterio de conformidad de nivel A y AA y sabiendo implementar las soluciones técnicas para satisfacerlos.
- Desarrollar interfaces plenamente navegables por teclado, comprendiendo el uso correcto de `tabindex`, los estilos de foco (`:focus`, `:focus-visible`, `:focus-within`), la implementación de enlaces de salto (skip links), y la gestión del orden de tabulación lógico.
- Entender el funcionamiento de los principales lectores de pantalla (NVDA, VoiceOver, JAWS, TalkBack), comprender cómo los usuarios ciegos o con baja visión navegan por la web (mediante headings, landmarks, enlaces y elementos de formulario), y saber verificar que una página es comprensible a través de estas herramientas.
- Utilizar correctamente el HTML semántico como primera y principal estrategia de accesibilidad: jerarquía de encabezados, landmarks HTML5, asociación de etiquetas, textos alternativos, y diferenciación entre enlaces y botones según su función.
- Aplicar WAI-ARIA de forma profesional, siguiendo las reglas de oro (priorizar HTML nativo), conociendo los roles (landmark, widget, document, abstract), las propiedades (`aria-label`, `aria-labelledby`, `aria-describedby`, `aria-required`, `aria-invalid`, `aria-current`, `aria-hidden`) y los estados (`aria-expanded`, `aria-selected`, `aria-checked`, `aria-disabled`, `aria-pressed`), e implementando correctamente las regiones live (`aria-live`, `aria-atomic`, `aria-relevant`).
- Realizar auditorías de accesibilidad utilizando herramientas automáticas (Lighthouse, WAVE, axe DevTools) y checklists de verificación manual, interpretando los resultados y priorizando las correcciones según su impacto en los usuarios.
- Construir componentes web complejos (formularios, modales, acordeones, tabs, tablas, menús, notificaciones) que cumplan los criterios de accesibilidad WCAG 2.1 nivel AA y sean utilizables por personas con diversas discapacidades.
- Auditar críticamente la accesibilidad de sitios web reales como la sede electrónica del gobierno español, portales bancarios y plataformas de comercio electrónico, identificando barreras y proponiendo soluciones concretas.

## Relación con los Resultados de Aprendizaje

Esta unidad constituye el núcleo de la competencia en accesibilidad del módulo 0615 Diseño de Interfaces Web y se relaciona directamente con los siguientes Resultados de Aprendizaje:

- **RA1: Planifica la creación de una interfaz web valorando y aplicando especificaciones de diseño.** En la fase de planificación se incorporan los requisitos de accesibilidad como criterios fundamentales de diseño: selección de patrones de interacción accesibles, definición de la jerarquía de encabezados y landmarks, planificación del orden de tabulación, y previsión de alternativas textuales para todo el contenido no textual.
- **RA2: Crea interfaces web homogéneos definiendo y aplicando estilos.** La homogeneidad incluye la consistencia en la implementación de características de accesibilidad: estilos de foco coherentes, etiquetado consistente de componentes similares y patrones de navegación predecibles en toda la aplicación (WCAG 3.2.3). Las hojas de estilo deben contemplar la accesibilidad visual: contraste de color suficiente (1.4.3), estilos de foco visibles (2.4.7), soporte para espaciado de texto personalizado (1.4.12) y adaptación a preferencias de usuario como `prefers-reduced-motion` y `prefers-contrast`.
- **RA4: Integra contenido multimedia en documentos web valorando su aportación y seleccionando adecuadamente los elementos interactivos.** La accesibilidad de los contenidos multimedia es crítica: subtítulos para vídeos, transcripciones para audio, audiodescripción para contenido visual, y alternativas textuales para imágenes, gráficos e infografías. Los componentes interactivos deben ser operables por teclado y comunicar su estado a tecnologías asistivas.
- **RA5: Desarrolla interfaces web accesibles, analizando las pautas establecidas y aplicando técnicas de verificación.** Este RA es el eje central de la unidad. El alumnado aprende a utilizar herramientas automáticas y manuales para verificar la conformidad con WCAG, interpretar informes de auditoría, realizar pruebas con lectores de pantalla, y elaborar informes de evaluación con recomendaciones priorizadas.
- **RA6: Desarrolla interfaces web amigables analizando y aplicando las pautas de usabilidad establecidas.** La accesibilidad y la usabilidad están íntimamente relacionadas: una interfaz accesible es inherentemente más usable para todos los usuarios. Las técnicas de evaluación de usabilidad aprendidas en otras unidades se aplican aquí con un enfoque específico en usuarios con discapacidad.

## Conocimientos previos

Para abordar con aprovechamiento esta unidad, el alumnado debe contar con los siguientes conocimientos:

- **HTML semántico sólido:** Comprensión profunda de la semántica de los elementos HTML5. Uso de etiquetas de seccionamiento (`header`, `nav`, `main`, `section`, `article`, `aside`, `footer`), etiquetas de texto (`h1`-`h6`, `p`, `ul`/`ol`/`li`, `dl`/`dt`/`dd`, `blockquote`, `cite`, `code`, `pre`), etiquetas de formulario (`form`, `fieldset`, `legend`, `label`, `input`, `select`, `textarea`, `button`, `datalist`, `output`), y atributos de accesibilidad nativos (`alt`, `title`, `lang`, `dir`). Es fundamental entender que un uso correcto del HTML semántico resuelve aproximadamente el **70% de los problemas de accesibilidad sin necesidad de ARIA**.

- **CSS intermedio:** Manejo de selectores, especificidad, cascada, modelo de cajas, Flexbox, Grid, media queries, pseudoclases y pseudoelementos. Específicamente, el alumno debe conocer las pseudoclases de foco (`:focus`, `:focus-visible`, `:focus-within`) y las propiedades relacionadas con la accesibilidad visual como `outline`, `color`, `background-color`, `font-size`, `line-height` y `letter-spacing`.

- **JavaScript básico:** Manipulación del DOM (seleccionar, crear, modificar y eliminar elementos), manejo de eventos (especialmente `keydown` para implementar navegación por teclado), modificación de atributos ARIA (`setAttribute`, `getAttribute`, `removeAttribute`), y gestión del foco programático (`element.focus()`, `document.activeElement`). Conocimiento de `localStorage` para persistencia de preferencias de accesibilidad.

- **Conocimientos básicos sobre discapacidad y tecnologia asistiva:** Nociones elementales sobre qué es un lector de pantalla, un magnificador de pantalla, un teclado adaptativo o un puntero de cabeza. No se requiere experiencia práctica, pero sí una comprensión conceptual de que existen diversas formas de interactuar con un ordenador más allá del binomio ratón+teclado estándar.

- **Herramientas de desarrollo:** Uso fluido de las DevTools del navegador, incluyendo la inspección del árbol de accesibilidad (pestaña Accessibility en Chrome), la auditoría Lighthouse, y la simulación de dispositivos.

## Contenidos

### 1. Fundamentos de la accesibilidad web
1.1. Definición de accesibilidad web. El poder de la Web como medio universal.
1.2. Importancia: perspectiva legal, ética y de negocio.
1.3. Estadísticas de discapacidad (OMS: 15% de la población mundial, más de 1.000 millones de personas).
1.4. Tipos de discapacidad: visual (ceguera, baja visión, daltonismo), auditiva (sordera, hipoacusia), motriz (limitaciones de movilidad, parálisis, temblores), cognitiva y neurológica (dislexia, TDAH, autismo, epilepsia).
1.5. Tecnologías de apoyo: lectores de pantalla, magnificadores, software de reconocimiento de voz, teclados adaptativos, conmutadores.

### 2. Marco legislativo y normativo
2.1. W3C Web Accessibility Initiative (WAI): historia, objetivos y recursos.
2.2. Norma europea EN 301 549: requisitos de accesibilidad para productos y servicios TIC.
2.3. Real Decreto 1112/2018 (España): accesibilidad de sitios web y apps del sector público.
2.4. Ley 11/2023 (España): trasposición de la Directiva Europea 2019/882 (European Accessibility Act).
2.5. Americans with Disabilities Act (ADA) - EEUU.
2.6. Section 508 of the Rehabilitation Act (EEUU).
2.7. Implicaciones para desarrolladores: obligaciones legales, plazos de cumplimiento, sanciones.

### 3. WCAG - Web Content Accessibility Guidelines
3.1. Historia y evolución: WCAG 2.0 (2008), WCAG 2.1 (2018), WCAG 2.2 (2023).
3.2. Niveles de conformidad: A (mínimo, 30 criterios), AA (estándar legal, 50 criterios incluyendo A), AAA (óptimo, 78 criterios).
3.3. Estructura jerárquica: 4 Principios > 13 Pautas > Criterios de Conformidad.
3.4. Técnicas: Suficientes (suficient techniques) y Recomendables (advisory techniques). Fallos comunes (common failures).

### 4. Los principios POUR en detalle
4.1. Perceptible (Perceivable): la información y los componentes de la interfaz deben presentarse de modo que los usuarios puedan percibirlos. Pautas: alternativas textuales (1.1), medios basados en el tiempo (1.2), adaptable (1.3), distinguible (1.4).
4.2. Operable (Operable): los componentes de la interfaz y la navegación deben ser operables. Pautas: accesible por teclado (2.1), tiempo suficiente (2.2), convulsiones y reacciones físicas (2.3), navegable (2.4), modalidades de entrada (2.5).
4.3. Comprensible (Understandable): la información y el manejo de la interfaz deben ser comprensibles. Pautas: legible (3.1), predecible (3.2), asistencia a la entrada (3.3).
4.4. Robusto (Robust): el contenido debe ser suficientemente robusto para ser interpretado por una amplia variedad de agentes de usuario, incluidas las tecnologías asistivas. Pauta: compatible (4.1).

### 5. Criterios de conformidad específicos
5.1. 1.1.1 Non-text Content (Nivel A): alternativas textuales para imágenes, gráficos, CAPTCHAs.
5.2. 1.4.1 Use of Color (Nivel A): el color no debe ser el único medio para transmitir información.
5.3. 1.4.3 Contrast Minimum (Nivel AA): ratio de contraste de 4.5:1 para texto normal, 3:1 para texto grande.
5.4. 1.4.11 Non-text Contrast (Nivel AA): contraste de 3:1 para componentes UI y objetos gráficos.
5.5. 1.4.12 Text Spacing (Nivel AA): el contenido debe soportar modificaciones de espaciado de texto sin pérdida.
5.6. 2.1.1 Keyboard (Nivel A): toda la funcionalidad debe ser operable mediante teclado.
5.7. 2.4.1 Bypass Blocks (Nivel A): mecanismo para saltar bloques de contenido repetitivo.
5.8. 2.4.3 Focus Order (Nivel A): orden de foco significativo que preserve la operabilidad.
5.9. 2.4.4 Link Purpose (Nivel A): el propósito de cada enlace debe poder determinarse.
5.10. 2.4.7 Focus Visible (Nivel AA): indicador de foco visible para elementos interactivos.
5.11. 3.2.3 Consistent Navigation (Nivel AA): navegación consistente entre páginas.
5.12. 4.1.2 Name, Role, Value (Nivel A): nombre, rol y valor accesibles para componentes UI.

### 6. Navegación por teclado
6.1. `tabindex`: valores 0 (incluye en el orden natural), -1 (foco programático), >0 (NO usar).
6.2. Estilos de foco: `:focus`, `:focus-visible`, `:focus-within`. Diseño de indicadores de foco visibles y estéticos.
6.3. Gestión del foco en SPAs y aplicaciones dinámicas.
6.4. Skip links: implementación y estilizado.
6.5. Teclas de acceso rápido (`accesskey`): uso, limitaciones y alternativas.
6.6. Orden de tabulación lógico: cómo garantizarlo, cómo evitar desórdenes con CSS Grid/Flexbox.

### 7. Lectores de pantalla y tecnologías asistivas
7.1. NVDA (Windows, gratuito): instalación, comandos básicos, funcionamiento del árbol de accesibilidad.
7.2. VoiceOver (macOS/iOS): activación, gestos, rotor.
7.3. JAWS (Windows, de pago): diferencias con NVDA.
7.4. TalkBack (Android): gestos y navegación.
7.5. Cómo navegan los usuarios: por headings, landmarks, enlaces, controles de formulario.
7.6. Ejemplo de cómo "lee" un lector de pantalla una página web.

### 8. HTML semántico como base de la accesibilidad
8.1. Jerarquía de encabezados (`h1`-`h6`): estructura, buenas prácticas, errores comunes.
8.2. Landmarks HTML5: `header`, `nav`, `main`, `footer`, `aside`, `section`, `form`, `search`.
8.3. Enlaces vs botones: cuándo usar cada uno, impacto en accesibilidad.
8.4. Etiquetas (`label`) asociadas a controles de formulario.
8.5. `fieldset` y `legend` para agrupar campos relacionados.
8.6. Texto alternativo (`alt`) para imágenes: cuándo usar texto descriptivo, cuándo usar `alt=""` (imagen decorativa).

### 9. WAI-ARIA en profundidad
9.1. Las 5 reglas de ARIA: 1) Usa HTML nativo siempre que sea posible. 2) No cambies la semántica nativa a menos que sea absolutamente necesario. 3) Todos los controles interactivos deben ser operables por teclado. 4) No uses `role="presentation"` o `aria-hidden="true"` en elementos enfocables. 5) Todos los elementos interactivos deben tener un nombre accesible.
9.2. Categorías de roles: landmark, widget, document structure, abstract, window.
9.3. Propiedades ARIA: `aria-label`, `aria-labelledby`, `aria-describedby`, `aria-required`, `aria-invalid`, `aria-current`, `aria-hidden`, `aria-owns`, `aria-haspopup`.
9.4. Estados ARIA: `aria-expanded`, `aria-selected`, `aria-checked`, `aria-disabled`, `aria-pressed`, `aria-busy`.
9.5. Patrones de diseño ARIA: Accordion, Alert, Breadcrumb, Button, Carousel, Checkbox, Combobox, Dialog (Modal), Disclosure, Feed, Grid, Link, Listbox, Menu, Meter, Progressbar, Radio Group, Slider, Spinbutton, Switch, Table, Tabs, Toolbar, Tooltip, Tree, Window Splitter.
9.6. Live regions: `aria-live` (off, polite, assertive), `aria-atomic`, `aria-relevant`, roles live implícitos (`alert`, `status`, `log`, `marquee`, `timer`).

### 10. Auditorías de accesibilidad
10.1. Lighthouse (Chrome DevTools): ejecución, interpretación de resultados, limitaciones.
10.2. WAVE (WebAIM): instalación, análisis visual, informe detallado.
10.3. axe DevTools (Deque Systems): extensión de navegador, testing automático, integración CI.
10.4. Checklist de verificación manual: metodología, criterios a verificar, documentación de hallazgos.
10.5. Pruebas con lectores de pantalla: configuración de NVDA/VoiceOver, guion de pruebas.
10.6. Pruebas de teclado: verificar tabulación, foco visible, atajos, trampas de foco.
10.7. Informe de auditoría: estructura, severidad de hallazgos, recomendaciones priorizadas.

## Desarrollo teórico

### 1. ¿Qué es la accesibilidad web?

!!! info "Definición"
    La accesibilidad web es la práctica de diseñar y desarrollar sitios web, aplicaciones y contenidos digitales de manera que puedan ser utilizados por todas las personas, independientemente de sus capacidades físicas, sensoriales, cognitivas o técnicas. El objetivo es eliminar las barreras que impiden la interacción o el acceso a la información, garantizando la igualdad de oportunidades en el entorno digital.

Tim Berners-Lee, inventor de la World Wide Web, lo expresó con claridad:

!!! quote "Tim Berners-Lee"
    El poder de la Web está en su universalidad. El acceso para todos, independientemente de la discapacidad, es un aspecto esencial.

El concepto de accesibilidad web va mucho más allá de lo que comúnmente se piensa. No se trata únicamente de personas ciegas que utilizan lectores de pantalla. La accesibilidad beneficia a un espectro extraordinariamente amplio de situaciones y usuarios:

- **Ceguera total o parcial**.
- **Baja visión**.
- **Daltonismo** (aproximadamente el 8% de los hombres y el 0.5% de las mujeres).
- **Sordera o hipoacusia**.
- **Dificultades motrices** (que van desde la imposibilidad de usar un ratón hasta temblores que dificultan hacer clic en elementos pequeños).
- **Trastornos del espectro autista**.
- **Dislexia, TDAH o dificultades de aprendizaje**.
- **Epilepsia fotosensible**.
- **Personas mayores** cuyo oído, vista o movilidad se han deteriorado con la edad.
- **Lesiones temporales** (una fractura de brazo, por ejemplo).
- **Situaciones limitantes** (un entorno ruidoso o con mucho sol que dificulta ver la pantalla, o con las manos ocupadas).
- **Conexiones lentas o dispositivos antiguos** donde el contenido accesible y bien estructurado carga mejor.

En otras palabras, la accesibilidad nos beneficia a todos en algún momento de nuestras vidas.

!!! info "Cifras clave de la discapacidad"
    La Organización Mundial de la Salud estima que **más del 15% de la población mundial** —más de 1.000 millones de personas— vive con algún tipo de discapacidad. De ellas, aproximadamente **285 millones** tienen discapacidad visual (39 millones con ceguera y 246 millones con baja visión), **466 millones** tienen pérdida auditiva discapacitante, y alrededor de **200 millones** tienen dificultades significativas de movilidad. A estas cifras hay que añadir las personas con discapacidades cognitivas, neurológicas y del desarrollo, así como la población mayor de 65 años, que en muchos países supera ya el 20% del total.

    Todos estos colectivos representan, además, un enorme potencial económico: se estima que el poder adquisitivo global de las personas con discapacidad y sus familias supera los **8 billones de dólares anuales** (el *purple pound* o *disability market*).

Desde la perspectiva legal, la accesibilidad web ha dejado de ser opcional. En España, el **Real Decreto 1112/2018** sobre accesibilidad de los sitios web y aplicaciones para dispositivos móviles del sector público traspuso la Directiva (UE) 2016/2102, estableciendo la obligatoriedad de cumplir con la norma **UNE-EN 301 549**, que a su vez referencia las **WCAG 2.1 nivel AA** como requisito técnico. La **Ley 11/2023**, de trasposición de la Directiva Europea 2019/882 (*European Accessibility Act*), extiende estas obligaciones al sector privado para determinados productos y servicios —comercio electrónico, banca, transporte y servicios audiovisuales—, con plazos de cumplimiento que culminan en **junio de 2025**. En Estados Unidos, la **ADA** (*Americans with Disabilities Act*) y la **Section 508** han generado una avalancha de demandas por inaccesibilidad web, con miles de casos presentados cada año contra empresas cuyos sitios web no son accesibles.

Más allá de las obligaciones legales, existe un imperativo ético. La web fue concebida como un espacio universal, y la accesibilidad es la materialización técnica de ese principio fundacional. Excluir a personas con discapacidad del acceso a servicios esenciales (banca, salud, educación, empleo público, comercio) no solo es ilegal, sino profundamente injusto. Tim Berners-Lee lo resumió en una frase:

!!! quote "Tim Berners-Lee"
    Antes de que la web existiera, era bastante difícil acceder a la información. Ahora, si no se hace de forma accesible, estamos creando una brecha aún mayor.

### 2. Tipos de discapacidad y su impacto en el uso de la web

Para diseñar y desarrollar de forma accesible, es necesario comprender los diferentes tipos de discapacidad y cómo cada uno afecta a la experiencia de navegación web. Solo entendiendo las barreras concretas que enfrentan los usuarios podemos construir soluciones efectivas:

- **Discapacidad visual** — es probablemente la categoría más conocida en el contexto de la accesibilidad web, pero es importante entender su espectro completo. La ceguera total afecta a aproximadamente **39 millones de personas** en el mundo. Estas personas navegan por la web utilizando lectores de pantalla (software que convierte el contenido textual y la estructura del documento en voz sintetizada o braille) y dependen completamente de que los elementos estén correctamente etiquetados, que las imágenes tengan alternativas textuales, que los formularios estén correctamente asociados con sus etiquetas, y que la estructura del documento (encabezados, landmarks, listas) sea semánticamente correcta. Para un usuario ciego, un CAPTCHA visual sin alternativa de audio es una barrera insalvable; una imagen sin atributo `alt` simplemente no existe; un formulario sin etiquetas `<label>` correctamente asociadas es inutilizable porque el lector de pantalla no puede identificar qué información se espera en cada campo.

- **Baja visión** — afecta a una población mucho mayor (**246 millones de personas**). Estos usuarios no utilizan lectores de pantalla (generalmente), sino que dependen de magnificadores de pantalla, configuraciones de alto contraste, tamaños de fuente aumentados, y estilos personalizados. Para ellos, el contraste insuficiente entre texto y fondo es la barrera más común. También son críticos: la posibilidad de aumentar el texto sin que el diseño se rompa (zoom de hasta **200% sin pérdida de contenido**), los estilos de foco claramente visibles, y la no dependencia exclusiva del color para transmitir información. Un usuario con baja visión que utiliza un magnificador solo ve una pequeña porción de la pantalla a la vez, por lo que necesita pistas contextuales claras y una navegación predecible.

- **Daltonismo o discromatopsia** — afecta aproximadamente al **8% de los hombres**. Las formas más comunes son la deuteranopia (dificultad para distinguir verdes), protanopia (dificultad para distinguir rojos) y tritanopia (dificultad para distinguir azules). El criterio **1.4.1** (*Use of Color*) aborda específicamente esta necesidad: **el color nunca debe ser el único medio** para transmitir información, indicar una acción o distinguir un elemento. Un mensaje de error que solo se diferencia del mensaje de éxito por ser rojo en lugar de verde es invisible para una persona daltónica; es necesario añadir un icono, un texto o un patrón adicional.

- **Discapacidad auditiva** — afecta a aproximadamente **466 millones de personas** en el mundo. Para estos usuarios, cualquier contenido exclusivamente sonoro es inaccesible. Los vídeos sin subtítulos, los podcasts sin transcripción, las alertas sonoras sin equivalente visual, las llamadas telefónicas como único medio de verificación de identidad, todo ello constituye barreras. La solución es proporcionar alternativas textuales para todo contenido auditivo: subtítulos para vídeos (y mejor aún, closed captions que incluyen información contextual como "\[música suave\]" o "\[timbre de puerta\]"), transcripciones completas para contenido de audio, y alertas visuales para notificaciones que de otro modo serían solo sonoras. En el contexto de videoconferencias y contenido multimedia, es importante distinguir entre subtítulos (que transcriben el diálogo), closed captions (que incluyen sonidos ambientales e información contextual), y audiodescripción (una pista de audio adicional que describe lo que sucede en pantalla para personas ciegas).

- **Discapacidad motriz** — abarca un espectro muy amplio de condiciones: desde la imposibilidad total de usar las manos (usuarios que navegan con la voz, con punteros de cabeza, con sopladores, o con sistemas de seguimiento ocular) hasta dificultades más leves como temblores que dificultan hacer clic en objetivos pequeños, artritis que hace doloroso el uso prolongado del ratón, o parálisis parcial que impide combinaciones complejas de teclas. Para estos usuarios, la navegación por teclado es absolutamente crítica. Pero también lo son: los objetivos táctiles o clickables de tamaño suficiente (al menos **44×44 píxeles** según WCAG 2.5.5, nivel AAA; **24×24 píxeles** como mínimo exigible en 2.5.8, nivel AA), el tiempo suficiente para completar tareas (sin timeouts que expiren demasiado rápido), y la posibilidad de desactivar o extender límites de tiempo. Un usuario que controla el puntero con la cabeza necesita que los botones sean grandes y estén bien espaciados. Un usuario con temblor esencial necesita que haya margen de error al hacer clic.

- **Discapacidad cognitiva y neurológica** — es una categoría amplia que incluye: dislexia (dificultad para procesar texto escrito), TDAH (dificultad para mantener la atención), trastornos del espectro autista (sensibilidad a la sobrecarga sensorial), epilepsia fotosensible (el contenido con parpadeos o destellos puede desencadenar convulsiones), síndrome de Down, y discapacidad intelectual. Para estos usuarios, la claridad y simplicidad del contenido es fundamental: uso de lenguaje claro y sencillo, párrafos cortos, buena estructura visual, consistencia en la navegación, evitar animaciones innecesarias o parpadeantes (WCAG **2.3.1**: nada que parpadee más de **3 veces por segundo**), proporcionar instrucciones claras y ayuda contextual, y mantener una jerarquía visual que guíe la atención de forma lógica. Las WCAG 2.2 introdujeron criterios específicos para este colectivo, como **3.3.7** (*Accessible Authentication*), que requiere alternativas a pruebas cognitivas complejas.

### 3. Legislación sobre accesibilidad web

El marco legal de la accesibilidad web ha evolucionado significativamente en la última década, pasando de ser recomendaciones voluntarias a obligaciones legales con plazos de cumplimiento y, en algunos casos, sanciones económicas. Es esencial que el desarrollador web profesional conozca este marco, no solo para evitar riesgos legales, sino para comprender el contexto en el que se desarrolla su trabajo:

- **W3C y la Web Accessibility Initiative (WAI)** — El World Wide Web Consortium, el organismo internacional que desarrolla los estándares web, creó en **1997** la Web Accessibility Initiative con el objetivo de liderar la web hacia su máximo potencial de accesibilidad. La WAI desarrolla las **WCAG** (pautas de accesibilidad para el contenido), las **ATAG** (pautas de accesibilidad para herramientas de autor) y las **UAAG** (pautas de accesibilidad para agentes de usuario). También publica las técnicas suficientes y recomendables, tutoriales, y recursos educativos. El trabajo de la WAI es la base sobre la que se construyen todas las legislaciones nacionales e internacionales.

- **Norma europea EN 301 549** — Es el estándar europeo de requisitos de accesibilidad para productos y servicios de Tecnologías de la Información y la Comunicación (TIC). Desarrollada por los organismos europeos de normalización ETSI, CEN y CENELEC a petición de la Comisión Europea, esta norma armoniza los requisitos de accesibilidad en todos los estados miembros. En su versión más reciente, la **EN 301 549 V3.2.1** (**2021**), incorpora directamente las **WCAG 2.1 nivel AA** como requisitos técnicos para el contenido web, las herramientas de autor, y los agentes de usuario. La norma cubre también hardware (ordenadores, teléfonos, cajeros automáticos, máquinas expendedoras), software (sistemas operativos, aplicaciones), y servicios (comunicaciones electrónicas, transporte). Para un desarrollador web, lo relevante es saber que cumplir las WCAG 2.1 AA equivale a cumplir la EN 301 549 en lo que respecta al contenido web.

- **Real Decreto 1112/2018 (España)** — Este real decreto, publicado en el BOE el **19 de septiembre de 2018**, traspone al ordenamiento jurídico español la Directiva (UE) 2016/2102 sobre la accesibilidad de los sitios web y aplicaciones para dispositivos móviles de los organismos del sector público. Sus puntos clave son: obliga a todos los sitios web y apps del sector público (administración general del estado, comunidades autónomas, entidades locales, universidades públicas, organismos constitucionales, etc.) a cumplir con los requisitos de accesibilidad establecidos en la norma **EN 301 549** (es decir, **WCAG 2.1 AA**). Establece un **sistema de declaración de accesibilidad** que cada sitio debe publicar, incluyendo el estado de cumplimiento, las alternativas accesibles, y un mecanismo de comunicación para que los usuarios informen sobre incumplimientos. Crea un sistema de seguimiento y presentación de informes a la Comisión Europea **cada tres años**. Obliga a que los sitios web nuevos publicados después del **23 de septiembre de 2019** sean accesibles desde su lanzamiento. Este real decreto marcó un antes y un después en la accesibilidad del sector público español.

- **Ley 11/2023 (España)** — Publicada en el BOE el **9 de mayo de 2023**, esta ley traspone la Directiva (UE) 2019/882, conocida como **European Accessibility Act (EAA)**. Mientras que el RD 1112/2018 se centra en el sector público, esta ley extiende las obligaciones de accesibilidad a productos y servicios del **sector privado**. Los sectores afectados incluyen: comercio electrónico, servicios bancarios y financieros, servicios de transporte (incluyendo webs y apps de aerolíneas, autobuses, trenes), servicios audiovisuales (plataformas de streaming, libros electrónicos), servicios de comunicación electrónica (telefonía, mensajería), y terminales de autoservicio (cajeros, máquinas de billetes). La ley establece un plazo de cumplimiento: los productos y servicios nuevos deberán ser accesibles a partir del **28 de junio de 2025**. Para productos ya existentes, hay un período de transición hasta el **28 de junio de 2030**. Esta ley tiene un impacto directo en los desarrolladores web del sector privado, que por primera vez en España tienen obligaciones legales explícitas de accesibilidad.

### 4. WCAG - Web Content Accessibility Guidelines: estructura y principios

Las Web Content Accessibility Guidelines (WCAG) son el estándar internacional de facto para la accesibilidad del contenido web. Publicadas por el W3C, constituyen la referencia técnica que subyace a todas las legislaciones nacionales e internacionales. Su evolución refleja la maduración del campo de la accesibilidad digital:

| Versión | Año | Aportaciones |
|---------|-----|--------------|
| **WCAG 1.0** | 1999 | Un primer intento que rápidamente quedó obsoleto |
| **WCAG 2.0** | 2008 | Estableció la estructura fundamental de cuatro principios que se mantiene hasta hoy |
| **WCAG 2.1** | 2018 | Añadió criterios para abordar la accesibilidad en dispositivos móviles, personas con baja visión y discapacidades cognitivas |
| **WCAG 2.2** | 2023 | Añadió 9 nuevos criterios enfocados en mejorar la accesibilidad para personas con discapacidades cognitivas y para interacciones táctiles complejas |

Las WCAG se organizan en una estructura jerárquica de cuatro niveles:

!!! info "Estructura jerárquica de las WCAG"
    1. **Principios** — los **4 principios** conocidos por el acrónimo **POUR** (Perceptible, Operable, Comprensible, Robusto): los fundamentos conceptuales bajo los que se agrupan todas las pautas.
    2. **Pautas** (*Guidelines*) — **13 en total**; los objetivos básicos que los desarrolladores deben alcanzar.
    3. **Criterios de Conformidad** (*Success Criteria*) — enunciados **verificables y comprobables**; en WCAG 2.1 hay unos **78 criterios** (**50** de nivel A y AA, más **28** adicionales de nivel AAA).
    4. **Técnicas** (*Techniques*) — el nivel más granular: ejemplos concretos de cómo cumplir cada criterio, tanto **suficientes** (garantizan el cumplimiento) como **recomendables** (van más allá del mínimo).

Los tres niveles de conformidad (A, AA, AAA) reflejan grados crecientes de accesibilidad:

| Nivel | Descripción | Criterios | Ejemplos |
|-------|-------------|-----------|----------|
| **A** | Nivel mínimo de accesibilidad, sin el cual algunos grupos de usuarios encontrarían imposible o extremadamente difícil acceder al contenido | **30 criterios** | Texto alternativo en todas las imágenes (1.1.1), funcionalidad operable por teclado (2.1.1), contenido que no causa convulsiones (2.3.1) |
| **AA** | El nivel que la mayoría de las legislaciones exige como estándar; cumplirlo significa que la interfaz es usable para la gran mayoría de usuarios con discapacidad | **30 criterios A + 20 adicionales** | Contraste de color suficiente (1.4.3), foco visible (2.4.7), navegación consistente (3.2.3), etiquetas o instrucciones en formularios (3.3.2) |
| **AAA** | Nivel más alto de accesibilidad; no es realista ni exigible cumplirlo para sitios web completos, ya que algunos criterios son mutuamente excluyentes para ciertos tipos de contenido | **50 criterios A+AA + 28 adicionales** | Contraste mejorado de 7:1 (1.4.6), propósito de cada enlace solo con su texto (2.4.9), pronunciación de palabras ambiguas (3.1.6), interrupciones posponibles (2.2.4) |

**Los principios POUR en detalle:**

**Perceptible (Perceivable):** La información y los componentes de la interfaz de usuario deben presentarse a los usuarios de manera que puedan percibirlos. Este principio aborda la pregunta: ¿puede el usuario percibir el contenido a través de al menos uno de sus sentidos? Si el contenido es puramente visual (una imagen, un gráfico, un video sin sonido), un usuario ciego no puede percibirlo a menos que se proporcione una alternativa textual. Si el contenido es puramente auditivo (un podcast, una alerta sonora), un usuario sordo no puede percibirlo a menos que se proporcionen subtítulos o transcripción. El principio Perceptible se desarrolla en cuatro pautas:
- **1.1 Text Alternatives:** Proporcionar alternativas textuales para cualquier contenido no textual (imágenes, gráficos, iconos, botones de imagen, CAPTCHAs, contenido multimedia).
- **1.2 Time-based Media:** Proporcionar alternativas para contenido multimedia dependiente del tiempo: subtítulos para vídeo, transcripciones para audio, audiodescripción para contenido visual, lengua de signos.
- **1.3 Adaptable:** Crear contenido que pueda presentarse de diferentes maneras sin perder información o estructura. Esto implica usar HTML semántico para que el contenido mantenga su significado incluso si se modifica la presentación visual (secuencia correcta, orientación, identificación de campos de formulario).
- **1.4 Distinguishable:** Facilitar a los usuarios ver y oír el contenido, incluyendo la separación entre primer plano y fondo. Incluye criterios sobre contraste de color, redimensionamiento de texto, imágenes de texto, control de audio, y espaciado del texto.

**Operable (Operable):** Los componentes de la interfaz de usuario y la navegación deben ser operables. ¿Puede el usuario interactuar con la interfaz y navegar por el contenido? Este principio aborda una de las barreras más comunes: la dependencia exclusiva del ratón. Millones de personas no pueden usar un ratón por discapacidad motriz, visual o cognitiva. El principio Operable garantiza que la interfaz funcione mediante teclado, voz, punteros alternativos o cualquier otro método de entrada.
- **2.1 Keyboard Accessible:** Toda la funcionalidad debe ser operable mediante una interfaz de teclado, sin requerir sincronización temporal para pulsaciones individuales.
- **2.2 Enough Time:** Proporcionar a los usuarios tiempo suficiente para leer y usar el contenido. Incluye límites de tiempo ajustables, pausa/parada de movimiento, y prevención de interrupciones.
- **2.3 Seizures and Physical Reactions:** No diseñar contenido de manera que pueda causar convulsiones o reacciones físicas. El criterio más conocido (2.3.1) prohíbe contenido que parpadee más de tres veces por segundo.
- **2.4 Navigable:** Proporcionar formas de ayudar a los usuarios a navegar, encontrar contenido y determinar dónde se encuentran. Incluye skip links, títulos de página descriptivos, orden de foco lógico, propósito de enlaces claro, múltiples vías de navegación, y encabezados y etiquetas descriptivos.
- **2.5 Input Modalities:** Facilitar a los usuarios la operabilidad mediante diversas modalidades de entrada más allá del teclado. Añadido en WCAG 2.1, incluye gestos con puntero, cancelación de clic, etiquetas en nombres accesibles, actuación por movimiento, y tamaño mínimo de objetivo táctil.

**Comprensible (Understandable):** La información y el manejo de la interfaz de usuario deben ser comprensibles. ¿Puede el usuario entender el contenido y cómo funciona la interfaz? La accesibilidad no se trata solo de poder percibir y operar, sino también de poder comprender.
- **3.1 Readable:** Hacer que el contenido textual sea legible y comprensible. Incluye identificar el idioma principal de la página y los cambios de idioma en partes del contenido.
- **3.2 Predictable:** Hacer que las páginas web aparezcan y operen de manera predecible. Incluye consistencia en navegación e identificación de elementos, y cambios de contexto que solo ocurran a petición del usuario.
- **3.3 Input Assistance:** Ayudar a los usuarios a evitar y corregir errores. Incluye identificación de errores, etiquetas e instrucciones en formularios, sugerencias para corregir errores, y prevención de errores en contextos legales, financieros y de datos.

**Robusto (Robust):** El contenido debe ser lo suficientemente robusto para ser interpretado de manera fiable por una amplia variedad de agentes de usuario, incluidas las tecnologías asistivas. ¿Funciona el contenido en diferentes navegadores, dispositivos y con diferentes tecnologías asistivas, ahora y en el futuro? Este principio mira hacia adelante: garantiza que el contenido esté construido sobre estándares que maximicen la compatibilidad.
- **4.1 Compatible:** Maximizar la compatibilidad con agentes de usuario actuales y futuros, incluyendo tecnologías asistivas. El criterio 4.1.2 (Name, Role, Value) exige que todos los componentes de interfaz de usuario tengan su nombre, rol y valores correctamente expuestos a las APIs de accesibilidad. El criterio 4.1.3 (Status Messages, añadido en WCAG 2.1) exige que los mensajes de estado se comuniquen a través de roles o propiedades sin necesidad de recibir foco.

### 5. Navegación por teclado

La navegación por teclado es, junto con el contraste de color y las alternativas textuales, uno de los tres pilares más críticos de la accesibilidad web práctica. Si una interfaz no es operable mediante teclado, es completamente inaccesible para usuarios ciegos (que no pueden ver el cursor del ratón), usuarios con discapacidad motriz en miembros superiores, usuarios que utilizan software de reconocimiento de voz que emula eventos de teclado, y usuarios avanzados que simplemente prefieren la eficiencia del teclado.

El atributo **`tabindex`** controla si un elemento puede recibir foco mediante tabulación y en qué orden. Los valores posibles son tres, pero solo dos deberían utilizarse en la práctica:

- **`tabindex="0"`** — incluye el elemento en el **orden natural de tabulación** del documento, basado en su posición en el DOM. Es la forma correcta de hacer enfocable un elemento no interactivo por defecto (como un `<div>`, `<span>` o `<li>`) que actúa como control personalizado.
- **`tabindex="-1"`** — permite que el elemento reciba foco de forma **programática** mediante JavaScript (`element.focus()`) pero lo excluye del orden natural; no se alcanza presionando Tab. Es esencial para la gestión del foco en **SPAs** (por ejemplo, mover el foco a un `<h1>` tras una navegación) y para elementos que necesitan recibir foco temporalmente.
- **`tabindex` positivo (1, 2, 3…)** — **NUNCA debe usarse**: crea un orden de tabulación artificial que se desincroniza del DOM, produce experiencias de navegación confusas y es extremadamente difícil de mantener. Si se necesita un orden de tabulación específico, reorganiza la estructura del DOM.

Los **estilos de foco** son la manifestación visual de la navegación por teclado: sin un indicador de foco claramente visible, los usuarios de teclado no pueden saber dónde se encuentran en la página, lo que hace la navegación imposible. El criterio **2.4.7** (*Focus Visible*, nivel **AA**) exige que cualquier elemento interactivo operable por teclado tenga un indicador de foco visible.

!!! warning "Nunca elimines el outline sin reemplazo"
    Muchos desarrolladores eliminan el contorno de foco con `outline: none` por razones estéticas, convirtiendo la página en **inutilizable por teclado**. Nunca elimines el `outline` sin reemplazarlo por un estilo de foco alternativo **aún más visible**.

La pseudoclase **`:focus-visible`** (introducida en 2018) aplica estilos de foco **solo cuando el usuario navega con teclado** —no al hacer clic con el ratón—, resolviendo el dilema estético. **`:focus-within`** aplica estilos a un ancestro cuando alguno de sus descendientes tiene el foco, permitiendo resaltar el contenedor del elemento enfocado. Un buen indicador de foco debe cumplir el criterio **1.4.11** (*Non-text Contrast*, **AA**): un ratio de contraste de al menos **3:1** entre el indicador y los colores adyacentes.

Los **skip links** o enlaces de salto son enlaces ocultos que aparecen al recibir el foco (al presionar Tab al inicio de la página) y permiten **saltar directamente al contenido principal**, evitando tabular a través de docenas de enlaces de navegación. Son un requisito del criterio **2.4.1** (*Bypass Blocks*, **Nivel A**). El skip link es el **primer elemento enfocable** de la página y típicamente contiene el texto «Saltar al contenido principal». Su implementación correcta implica:

- El enlace tiene `href="#main-content"` y es lo **primer elemento** del `<body>`.
- El destino tiene `id="main-content"` y `tabindex="-1"` (para poder recibir foco programático).
- El enlace está oculto de forma normal, pero **se muestra al recibir el foco** con `:focus` (nunca `display: none` o `visibility: hidden`).

### 6. Lectores de pantalla

!!! info "Definición"
    Un **lector de pantalla** es un software que interpreta el contenido mostrado en la pantalla y lo presenta al usuario mediante **voz sintetizada o una línea braille**. No se limita a leer el texto visible: construye un modelo interno del documento (**el árbol de accesibilidad**) a partir de la información semántica proporcionada por el HTML y ARIA, y permite navegar por este modelo de formas que no son posibles con la vista: saltando entre encabezados, listando todos los enlaces, agrupando controles de formulario o explorando la estructura de landmarks.

Los principales lectores de pantalla son:

- **NVDA** (*NonVisual Desktop Access*) — gratuito y de código abierto para Windows; el más utilizado en pruebas de accesibilidad por su disponibilidad y calidad (Firefox y Chrome).
- **JAWS** (*Job Access With Speech*) — comercial, para Windows; el más utilizado en entornos corporativos y gubernamentales en países angloparlantes.
- **VoiceOver** — integrado gratuitamente en todos los dispositivos Apple (macOS, iOS, iPadOS); probablemente el lector de pantalla más usado del mundo si contamos móviles.
- **TalkBack** — integrado en Android; el equivalente de VoiceOver para el ecosistema Google.

Los usuarios de lectores de pantalla no «leen» la página de arriba a abajo: utilizan **atajos de teclado** para navegar eficientemente por la estructura del documento:

- **Por encabezados** (tecla **H** en NVDA) — saltan entre `h1`, `h2`, `h3` para hacerse una idea rápida de la estructura.
- **Por landmarks/regiones** (tecla **D**) — saltan entre `header`, `nav`, `main`, `footer`, `aside`.
- **Por enlaces** (tecla **K**) — navegan por todos los enlaces buscando el que les interesa.
- **Por controles de formulario** (tecla **F**) — saltan entre campos.
- **Por listas** (tecla **L**) — saltan entre listas.

!!! success "Responsabilidad del desarrollador"
    Esta forma de navegar solo funciona si la estructura semántica es correcta: jerarquía de encabezados **sin saltos de nivel**, landmarks identificados y no redundantes, cada enlace con un **texto descriptivo y único**, y cada campo de formulario con su **etiqueta correctamente asociada**.

!!! example "Cómo lee NVDA una página bien construida"
    Al cargar la página, NVDA anuncia: *«Documento web. Título de la página. La página tiene 3 landmarks: banner, navegación, contenido principal. 15 enlaces. 8 encabezados.»* El usuario presiona **H**: *«Encabezado nivel 1: Bienvenido a Nuestra Tienda»*; presiona **D** para saltar al contenido principal; presiona **F**: *«Buscar productos, edición, en blanco»*. Todo esto es posible porque el HTML está bien estructurado con etiquetas semánticas, atributos `alt` descriptivos y una jerarquía lógica de encabezados. Si la misma página estuviera construida con `<div>` genéricos y sin `alt`, el lector de pantalla solo podría decir *«Enlace… Enlace… Enlace…»* sin ninguna información útil.

### 7. WAI-ARIA en profundidad

WAI-ARIA (Web Accessibility Initiative - Accessible Rich Internet Applications) es una especificación técnica que define atributos HTML adicionales para mejorar la accesibilidad de aplicaciones web complejas y dinámicas, especialmente aquellas que utilizan componentes personalizados sin equivalentes en el HTML estándar. **ARIA complementa el HTML semántico; no lo sustituye.**

!!! tip "Primera regla de ARIA"
    Si puedes usar un elemento o atributo HTML nativo con la semántica y el comportamiento que necesitas **ya incorporados**, en lugar de reutilizar un elemento genérico y añadirle un rol, estado o propiedad ARIA para hacerlo accesible, **hazlo siempre así**. Un `<button>` nativo ya es enfocable y anuncia su rol; un `<div role="button">` necesita JavaScript para todo eso.

Los **roles ARIA** definen qué es un elemento. La categoría más importante para el desarrollo de interfaces es la de **widget roles**:

- **Widget roles** — `button`, `checkbox`, `radio`, `switch`, `tab`, `tabpanel`, `combobox`, `listbox`, `option`, `slider`, `progressbar`, `menu`, `menuitem`, `dialog`, `alertdialog`.
- **Landmark roles** — `banner`, `navigation`, `main`, `complementary`, `contentinfo`, `form`, `search`, `region`.

Los roles ARIA **no modifican el comportamiento** del elemento (no lo hacen clickable o enfocable si no lo era antes); solo modifican la semántica expuesta al árbol de accesibilidad.

Las **propiedades ARIA** añaden información adicional a los elementos:

- **`aria-label`** — etiqueta textual accesible directamente, útil para elementos sin texto visible (un botón que solo contiene un icono).
- **`aria-labelledby`** — referencia el ID de otro elemento cuyo texto se usará como etiqueta accesible, permitiendo **reutilizar texto visible**.
- **`aria-describedby`** — referencia elementos con descripciones adicionales (textos de ayuda, mensajes de error).
- **`aria-required="true"`** — indica que un campo es obligatorio.
- **`aria-invalid="true"`** — marca un campo con un error de validación.
- **`aria-current`** — indica el elemento actual en un conjunto (la página activa en una paginación).
- **`aria-hidden="true"`** — oculta el elemento del árbol de accesibilidad; útil para contenido **puramente decorativo o duplicado**.

Los **estados ARIA** representan configuraciones dinámicas que cambian en respuesta a las acciones del usuario. A diferencia de las propiedades (que tienden a ser estáticas), los estados se actualizan frecuentemente mediante JavaScript:

- **`aria-expanded="true|false"`** — en un botón que controla un panel desplegable.
- **`aria-selected="true|false"`** — en tabs, opciones de listbox o items de tree.
- **`aria-checked="true|false|mixed"`** — en checkboxes.
- **`aria-pressed="true|false|mixed"`** — en toggle buttons.
- **`aria-disabled="true"`** — en elementos deshabilitados.
- **`aria-busy="true"`** — en regiones que están siendo actualizadas.

Las **live regions** son quizás la característica más importante de ARIA para aplicaciones web dinámicas: permiten que los cambios en el contenido del DOM se comuniquen a los usuarios de lectores de pantalla **sin mover el foco**.

- **`aria-live="polite"`** — el anuncio espera a que termine la lectura actual. Es el valor correcto para la **mayoría de las notificaciones**.
- **`aria-live="assertive"`** — interrumpe la lectura actual para anunciar el cambio de inmediato. Reservar para **mensajes críticos**.
- **`aria-atomic="true|false"`** — controla si se anuncia toda la región o solo los cambios.
- **`aria-relevant`** — especifica qué tipos de cambios anunciar.
- **Roles live implícitos** — `role="alert"` (assertive + atomic), `role="status"` (polite + atomic), `role="log"` (polite, solo adiciones), `role="marquee"` (live off), `role="timer"` (polite, actualizaciones periódicas).

### 8. Auditorías de accesibilidad

Las auditorías de accesibilidad son el proceso sistemático de evaluar un sitio o aplicación web para identificar barreras de accesibilidad y verificar el cumplimiento de las WCAG. Una auditoría completa combina herramientas automáticas (rápidas pero limitadas en alcance) con pruebas manuales (más exhaustivas pero costosas en tiempo) y pruebas con usuarios reales con discapacidad (las más valiosas pero logísticamente complejas).

**Lighthouse** es una herramienta de auditoría integrada en Chrome DevTools que ejecuta una batería de comprobaciones automáticas. En su categoría *Accessibility*, evalúa aproximadamente **50 verificaciones** (en contraste con las **78** de WCAG 2.1), cubriendo aspectos como: contraste de color, atributos `alt` en imágenes, etiquetas en formularios, estructura de encabezados, nombres accesibles en enlaces, uso de roles ARIA, y tabindex. Lighthouse asigna una puntuación ponderada de **0 a 100**, pero es importante entender sus limitaciones: solo puede verificar el **25-35% de los criterios WCAG** de forma automática; el resto requiere revisión manual (por ejemplo, si el texto alternativo de una imagen es *correcto*, no solo si *existe*). **Un 100 en Lighthouse no garantiza que el sitio sea accesible.**

**WAVE** (Web Accessibility Evaluation Tool), desarrollado por WebAIM, es una extensión de navegador que inyecta iconos visuales en la página para señalar posibles problemas y características de accesibilidad. Usa iconos rojos para errores (como falta de texto alternativo, enlaces vacíos, errores de contraste), amarillos para alertas (posibles problemas que requieren revisión humana), verdes para características de accesibilidad presentes (como landmarks bien definidos), y azules para elementos estructurales. WAVE también proporciona una vista de "sin estilos" que muestra la página con todo el CSS desactivado, permitiendo verificar el orden del contenido. Es una herramienta excelente para inspecciones visuales rápidas.

**axe DevTools** de Deque Systems es posiblemente la herramienta de testing automático más completa y precisa del mercado. A diferencia de Lighthouse (que aplica una ponderación y da una puntuación), axe DevTools se centra en encontrar problemas concretos listando cada violación, su ubicación exacta en el DOM, el criterio WCAG infringido, la gravedad del impacto, y el código HTML responsable. Ofrece integración con flujos de CI/CD para automatizar el testing de accesibilidad en cada commit. Su extensión de navegador es gratuita y su API de JavaScript (`axe-core`) también es de código abierto.

La **verificación manual** es imprescindible para completar una auditoría. Un checklist de verificación manual debe incluir al menos:

1. **Navegar por toda la página usando solo el teclado** (Tab, Shift+Tab, Enter, Espacio, flechas, Escape), verificando que se puede acceder a todos los elementos interactivos, que el foco es siempre visible, que no hay trampas de teclado y que el orden de tabulación es lógico.
2. **Verificar que los enlaces de salto** (skip links) **funcionan**.
3. **Comprobar los textos alternativos** de las imágenes (no solo si existen, sino si describen adecuadamente el contenido).
4. **Verificar la jerarquía de encabezados** (no debe haber saltos de nivel).
5. **Revisar que los formularios** tengan etiquetas correctamente asociadas y mensajes de error claros y accesibles.
6. **Probar el zoom al 200%** comprobando que no se pierde contenido ni funcionalidad.
7. **Verificar que el contenido multimedia** tiene subtítulos y/o transcripciones.
8. **Comprobar que no hay información transmitida exclusivamente por color.**
9. **Verificar los ratios de contraste** de color manualmente con herramientas como el Colour Contrast Analyser.
10. **Probar la página con al menos un lector de pantalla** (NVDA en Windows, VoiceOver en Mac).

El **informe de auditoría** debe documentar cada hallazgo de forma estructurada con los siguientes campos:

- **Identificador único** del hallazgo.
- **Criterio WCAG infringido** y **nivel de conformidad** afectado.
- **Ubicación exacta** (URL y elemento).
- **Descripción del problema** y **impacto en usuarios** (qué tipo de discapacidad se ve afectada y con qué severidad).
- **Recomendación de solución**, con código de ejemplo si aplica.
- **Nivel de prioridad** basado en la combinación de **frecuencia, impacto y dificultad de corrección**:
    - **Crítico** — impide completamente el acceso a la funcionalidad (un formulario de pago no operable por teclado).
    - **Alto** — dificulta significativamente el acceso.
    - **Medio** — mejoras recomendables.
    - **Bajo** — incidencias cosméticas.



## Ejemplos guiados

### Ejemplo Guiado 1: Página Completa Accesible con Landmarks y Headings

Construimos una página web que ejemplifica todas las buenas prácticas de accesibilidad estructural: landmarks HTML5, jerarquía de encabezados correcta, skip links, y navegación accesible.

=== "HTML"

    ``` html
    <!DOCTYPE html>
    <html lang="es">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Tienda Online Accesible - Productos Ecológicos</title>
      <link rel="stylesheet" href="./styles.css">
    </head>
    <body>
      <!-- Skip link: primer elemento enfocable -->
      <a href="#main-content" class="skip-link">Saltar al contenido principal</a>

      <!-- Header: role banner implícito -->
      <header>
        <h1>EcoTienda - Productos Ecológicos</h1>
      </header>

      <!-- Navegación principal con aria-label para distinguirla de otras navegaciones -->
      <nav aria-label="Navegación principal">
        <ul>
          <li><a href="/" aria-current="page">Inicio</a></li>
          <li><a href="/productos">Productos</a></li>
          <li><a href="/blog">Blog</a></li>
          <li><a href="/contacto">Contacto</a></li>
        </ul>
      </nav>

      <!-- Contenido principal: destino del skip link -->
      <main id="main-content" tabindex="-1">
        <!-- Sección con encabezado descriptivo -->
        <section aria-labelledby="destacados-heading">
          <h2 id="destacados-heading">Productos Destacados</h2>
          <div class="card">
            <h3>Cesta de Frutas Ecológicas</h3>
            <p>Selección de frutas de temporada cultivadas sin pesticidas ni fertilizantes químicos. Directamente del agricultor a tu mesa.</p>
            <!-- Botón con texto descriptivo, no genérico -->
            <a href="/productos/cesta-frutas" class="btn">
              Ver detalles <span class="sr-only">de Cesta de Frutas Ecológicas</span>
            </a>
          </div>
          <div class="card">
            <h3>Pack de Verduras de Temporada</h3>
            <p>Verduras frescas recolectadas en su punto óptimo de maduración. Apoyamos a pequeños agricultores locales.</p>
            <a href="/productos/pack-verduras" class="btn">
              Ver detalles <span class="sr-only">de Pack de Verduras de Temporada</span>
            </a>
          </div>
        </section>

        <!-- Sección con contenido complementario -->
        <aside aria-labelledby="info-heading" role="complementary">
          <h3 id="info-heading">Envío gratuito en pedidos superiores a 50€</h3>
          <p>En península. Plazo de entrega: 24-48 horas laborables.</p>
        </aside>
      </main>

      <!-- Footer: role contentinfo implícito -->
      <footer>
        <p>&copy; 2025 EcoTienda. Todos los derechos reservados.</p>
        <nav aria-label="Enlaces legales">
          <a href="/privacidad">Política de Privacidad</a> |
          <a href="/cookies">Cookies</a> |
          <a href="/accesibilidad">Declaración de Accesibilidad</a>
        </nav>
      </footer>
    </body>
    </html>
    ```

=== "CSS"

    ``` css
    /* Skip link: oculto hasta que recibe el foco */
    .skip-link { position: absolute; top: -100px; left: 0; background: #4a90d9; color: #fff; padding: 0.5rem 1rem; z-index: 10000; text-decoration: none; border-radius: 0 0 0.25rem 0; }
    .skip-link:focus { top: 0; }
    /* Estilo de foco visible personalizado */
    *:focus-visible { outline: 3px solid #4a90d9; outline-offset: 2px; }
    body { font-family: system-ui, sans-serif; margin: 0; padding: 0; color: #333; line-height: 1.6; }
    header[role="banner"] { background: #2c3e50; color: #fff; padding: 1rem 2rem; }
    header h1 { margin: 0; font-size: 1.5rem; }
    nav[aria-label="Navegación principal"] { background: #34495e; padding: 0.5rem 2rem; }
    nav ul { list-style: none; margin: 0; padding: 0; display: flex; gap: 1.5rem; }
    nav a { color: #ecf0f1; text-decoration: none; padding: 0.5rem 0; }
    nav a:hover { text-decoration: underline; }
    nav a[aria-current="page"] { font-weight: bold; border-bottom: 2px solid #ecf0f1; }
    main { max-width: 900px; margin: 0 auto; padding: 2rem; }
    footer[role="contentinfo"] { background: #2c3e50; color: #bdc3c7; padding: 1.5rem 2rem; text-align: center; font-size: 0.9rem; }
    .card { border: 1px solid #ddd; border-radius: 0.5rem; padding: 1.5rem; margin-bottom: 1.5rem; }
    .card h2 { margin-top: 0; color: #2c3e50; }
    .btn { display: inline-block; padding: 0.6rem 1.2rem; background: #27ae60; color: #fff; text-decoration: none; border-radius: 0.25rem; font-weight: 500; }
    .btn:hover { background: #219a52; }
    /* Ocultar visualmente pero accesible para lectores de pantalla */
    .sr-only { position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip: rect(0,0,0,0); white-space: nowrap; border: 0; }
    ```

### Ejemplo Guiado 2: Formulario de Registro Completamente Accesible

=== "HTML"

    ``` html
    <div class="ejemplo-container">
      <h2>Formulario de Registro Accesible</h2>
      <form id="registroForm" novalidate aria-labelledby="form-heading">
        <p id="form-heading" class="form-desc">Todos los campos marcados con <span aria-hidden="true">*</span><span class="sr-only">asterisco</span> son obligatorios.</p>
        <!-- Resumen de errores (aria-live assertive + role alert) -->
        <div id="formErrors" class="form-errors" role="alert" aria-live="assertive" hidden></div>

        <fieldset>
          <legend>Datos personales</legend>

          <div class="form-group">
            <label for="nombre">Nombre completo <span aria-hidden="true">*</span></label>
            <input type="text" id="nombre" name="nombre" required aria-required="true" aria-describedby="nombreHelp nombreError" autocomplete="name">
            <span id="nombreHelp" class="help-text">Introduce tu nombre y apellidos tal como aparecen en tu documento de identidad.</span>
            <span id="nombreError" class="error-text" role="alert" aria-live="polite"></span>
          </div>

          <div class="form-group">
            <label for="email">Correo electrónico <span aria-hidden="true">*</span></label>
            <input type="email" id="email" name="email" required aria-required="true" aria-describedby="emailHelp emailError" autocomplete="email">
            <span id="emailHelp" class="help-text">Te enviaremos un correo de confirmación a esta dirección.</span>
            <span id="emailError" class="error-text" role="alert" aria-live="polite"></span>
          </div>

          <div class="form-group">
            <label for="password">Contraseña <span aria-hidden="true">*</span></label>
            <input type="password" id="password" name="password" required aria-required="true" aria-describedby="passHelp passError" autocomplete="new-password" minlength="8">
            <span id="passHelp" class="help-text">Mínimo 8 caracteres, una mayúscula, un número y un carácter especial.</span>
            <span id="passError" class="error-text" role="alert" aria-live="polite"></span>
          </div>
        </fieldset>

        <fieldset>
          <legend>Preferencias</legend>
          <div class="form-group">
            <input type="checkbox" id="newsletter" name="newsletter" aria-describedby="newsHelp">
            <label for="newsletter">Deseo recibir la newsletter semanal con ofertas y novedades</label>
            <span id="newsHelp" class="help-text">Puedes darte de baja en cualquier momento.</span>
          </div>
        </fieldset>

        <!-- Mensaje de estado del envío (aria-live polite) -->
        <div id="submitStatus" role="status" aria-live="polite" class="submit-status" hidden></div>
        <button type="submit" class="btn-submit">Crear cuenta</button>
      </form>
    </div>

    <link rel="stylesheet" href="./styles.css">

    <script src="./script.js"></script>
    ```

=== "CSS"

    ``` css
    .ejemplo-container { max-width: 600px; margin: 0 auto; padding: 2rem; font-family: system-ui, sans-serif; }
    .form-desc { color: #666; margin-bottom: 1.5rem; }
    .form-errors { background: #fde8e8; border: 1px solid #dc3545; border-radius: 0.5rem; padding: 1rem; margin-bottom: 1rem; color: #721c24; }
    .form-errors ul { margin: 0.5rem 0 0; padding-left: 1.2rem; }
    fieldset { border: 1px solid #ddd; border-radius: 0.5rem; padding: 1.2rem; margin-bottom: 1.5rem; }
    legend { font-weight: 600; color: #333; padding: 0 0.5rem; }
    .form-group { margin-bottom: 1.2rem; }
    .form-group label { display: block; margin-bottom: 0.3rem; font-weight: 500; }
    .form-group input[type="text"],
    .form-group input[type="email"],
    .form-group input[type="password"] {
      width: 100%; padding: 0.6rem 0.8rem; border: 2px solid #ddd; border-radius: 0.4rem; font-size: 1rem; transition: border-color 0.2s;
      box-sizing: border-box;
    }
    .form-group input:focus { border-color: #4a90d9; outline: none; box-shadow: 0 0 0 3px rgba(74,144,217,0.2); }
    .form-group input.invalid { border-color: #dc3545; box-shadow: 0 0 0 3px rgba(220,53,69,0.15); }
    .form-group input.valid { border-color: #28a745; }
    .help-text { font-size: 0.82rem; color: #888; display: block; margin-top: 0.25rem; }
    .error-text { font-size: 0.82rem; color: #dc3545; display: block; margin-top: 0.25rem; font-weight: 500; }
    .form-group input[type="checkbox"] { margin-right: 0.5rem; width: 18px; height: 18px; }
    .form-group input[type="checkbox"] + label { display: inline; font-weight: normal; }
    .btn-submit { padding: 0.75rem 2rem; background: #27ae60; color: #fff; border: none; border-radius: 0.4rem; font-size: 1rem; font-weight: 600; cursor: pointer; }
    .btn-submit:hover { background: #219a52; }
    .btn-submit:focus-visible { outline: 3px solid #333; outline-offset: 2px; }
    .submit-status { padding: 0.75rem; border-radius: 0.4rem; margin-bottom: 1rem; }
    .submit-status.success { background: #d4edda; color: #155724; }
    .submit-status.error { background: #fde8e8; color: #721c24; }
    .sr-only { position: absolute; width:1px; height:1px; padding:0; margin:-1px; overflow:hidden; clip:rect(0,0,0,0); white-space:nowrap; border:0; }
    ```

=== "JS"

    ``` js
    (function() {
      var form = document.getElementById('registroForm');
      var formErrors = document.getElementById('formErrors');
      var submitStatus = document.getElementById('submitStatus');

      // Validación en tiempo real con debounce
      var debounceTimer;
      form.addEventListener('input', function(e) {
        if (e.target.matches('input[required], input[type="email"], input[minlength]')) {
          clearTimeout(debounceTimer);
          debounceTimer = setTimeout(function() { validarCampo(e.target); }, 300);
        }
      });

      form.addEventListener('blur', function(e) {
        if (e.target.matches('input[required], input[type="email"], input[minlength]')) {
          validarCampo(e.target);
        }
      }, true);

      function validarCampo(input) {
        var errorEl = document.getElementById(input.id + 'Error');
        if (!errorEl) return;
        var errors = [];
        if (input.required && !input.value.trim()) errors.push('Este campo es obligatorio.');
        if (input.type === 'email' && input.value.trim() && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(input.value))
          errors.push('Introduce una dirección de correo válida.');
        if (input.id === 'password' && input.value && input.value.length < 8)
          errors.push('La contraseña debe tener al menos 8 caracteres.');
        if (input.id === 'password' && input.value && !/(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*])/.test(input.value))
          errors.push('La contraseña debe incluir mayúscula, número y carácter especial.');

        if (errors.length > 0) {
          input.classList.add('invalid'); input.classList.remove('valid');
          input.setAttribute('aria-invalid', 'true');
          errorEl.textContent = errors[0];
        } else if (input.value.trim()) {
          input.classList.remove('invalid'); input.classList.add('valid');
          input.setAttribute('aria-invalid', 'false');
          errorEl.textContent = '';
        } else {
          input.classList.remove('invalid', 'valid');
          input.removeAttribute('aria-invalid');
          errorEl.textContent = '';
        }
      }

      form.addEventListener('submit', function(e) {
        e.preventDefault();
        var allInputs = form.querySelectorAll('input[required], input[type="email"], input[minlength]');
        var globalErrors = [];
        allInputs.forEach(function(input) { validarCampo(input); if (input.getAttribute('aria-invalid') === 'true') globalErrors.push(input); });

        formErrors.innerHTML = '';
        formErrors.hidden = true;
        submitStatus.innerHTML = '';
        submitStatus.hidden = true;

        if (globalErrors.length > 0) {
          var list = '<ul>' + globalErrors.map(function(inp) {
            var label = form.querySelector('label[for="' + inp.id + '"]');
            return '<li><a href="#' + inp.id + '">' + (label ? label.textContent.replace(/\*/g,'').trim() : inp.name) + ': campo inválido</a></li>';
          }).join('') + '</ul>';
          formErrors.innerHTML = '<strong>Se encontraron ' + globalErrors.length + ' errores:</strong>' + list;
          formErrors.hidden = false;
          globalErrors[0].focus();
          return;
        }

        // Simular envío exitoso
        submitStatus.textContent = 'Registro completado con éxito. Revisa tu correo para confirmar la cuenta.';
        submitStatus.className = 'submit-status success';
        submitStatus.hidden = false;
        form.reset();
        allInputs.forEach(function(inp) { inp.classList.remove('valid', 'invalid'); inp.removeAttribute('aria-invalid'); });
        document.querySelector('label[for="nombre"]').focus();
      });
    })();
    ```

### Ejemplo Guiado 3: Modal Accesible con Focus Trapping Completo

=== "HTML"

    ``` html
    <div class="ejemplo-container">
      <h2>Modal Accesible (WCAG 2.1 AA)</h2>
      <button id="openModalBtn" aria-haspopup="dialog">Abrir diálogo de confirmación</button>
    </div>
    <div class="modal-backdrop" id="modalBackdrop" aria-hidden="true"></div>
    <div class="modal-wrapper" id="modalWrapper" role="dialog" aria-modal="true" aria-labelledby="modalTitle" aria-describedby="modalDesc" aria-hidden="true">
      <div class="modal-inner">
        <div class="modal-header">
          <h3 id="modalTitle">Confirmar eliminación</h3>
          <button id="modalCloseBtn" aria-label="Cerrar diálogo">&times;</button>
        </div>
        <div class="modal-body">
          <p id="modalDesc">¿Estás seguro? Esta acción es irreversible y eliminará todos los datos asociados permanentemente.</p>
        </div>
        <div class="modal-footer">
          <button id="modalCancelBtn">Cancelar</button>
          <button id="modalDeleteBtn" class="btn-danger">Eliminar definitivamente</button>
        </div>
      </div>
    </div>

    <link rel="stylesheet" href="./styles.css">

    <script src="./script.js"></script>
    ```

=== "CSS"

    ``` css
    .modal-backdrop { position: fixed; inset: 0; background: rgba(0,0,0,0.6); z-index: 1000; opacity: 0; visibility: hidden; transition: opacity 0.3s ease, visibility 0.3s ease; }
    .modal-backdrop.visible { opacity: 1; visibility: visible; }
    .modal-wrapper { position: fixed; inset: 0; z-index: 1001; display: flex; align-items: center; justify-content: center; opacity: 0; visibility: hidden; transition: opacity 0.3s ease; }
    .modal-wrapper.visible { opacity: 1; visibility: visible; }
    .modal-inner { background: #fff; border-radius: 0.75rem; box-shadow: 0 12px 40px rgba(0,0,0,0.3); width: 90%; max-width: 450px; transform: translateY(20px); transition: transform 0.3s cubic-bezier(0.34,1.56,0.64,1); }
    .modal-wrapper.visible .modal-inner { transform: translateY(0); }
    .modal-header { display: flex; justify-content: space-between; align-items: center; padding: 1.2rem 1.5rem; border-bottom: 1px solid #eee; }
    .modal-header h3 { margin: 0; font-size: 1.15rem; }
    .modal-body { padding: 1.5rem; color: #555; line-height: 1.6; }
    .modal-footer { display: flex; justify-content: flex-end; gap: 0.75rem; padding: 1rem 1.5rem; border-top: 1px solid #eee; }
    .modal-footer button { padding: 0.6rem 1.2rem; border: none; border-radius: 0.4rem; font-weight: 500; cursor: pointer; }
    .modal-footer button:first-child { background: #e9ecef; color: #333; }
    .btn-danger { background: #dc3545; color: #fff; }
    ```

=== "JS"

    ``` js
    (function() {
      var backdrop = document.getElementById('modalBackdrop');
      var wrapper = document.getElementById('modalWrapper');
      var openBtn = document.getElementById('openModalBtn');
      var closeBtn = document.getElementById('modalCloseBtn');
      var cancelBtn = document.getElementById('modalCancelBtn');
      var deleteBtn = document.getElementById('modalDeleteBtn');
      var lastFocus = null;

      function getFocusable() {
        return Array.from(wrapper.querySelectorAll('button:not([disabled]), [tabindex]:not([tabindex="-1"])'));
      }

      function trapFocus(e) {
        if (e.key !== 'Tab') return;
        var focusable = getFocusable();
        if (focusable.length === 0) { e.preventDefault(); return; }
        var first = focusable[0], last = focusable[focusable.length-1];
        if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
        else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
      }

      function open() {
        lastFocus = document.activeElement;
        backdrop.classList.add('visible'); wrapper.classList.add('visible');
        backdrop.setAttribute('aria-hidden','false'); wrapper.setAttribute('aria-hidden','false');
        document.body.style.overflow = 'hidden';
        setTimeout(function() { closeBtn.focus(); }, 100);
        wrapper.addEventListener('keydown', trapFocus);
      }

      function close() {
        backdrop.classList.remove('visible'); wrapper.classList.remove('visible');
        backdrop.setAttribute('aria-hidden','true'); wrapper.setAttribute('aria-hidden','true');
        document.body.style.overflow = '';
        wrapper.removeEventListener('keydown', trapFocus);
        if (lastFocus) { lastFocus.focus(); lastFocus = null; }
      }

      openBtn.addEventListener('click', open);
      [closeBtn, cancelBtn].forEach(function(b) { b.addEventListener('click', close); });
      backdrop.addEventListener('click', close);
      deleteBtn.addEventListener('click', function() { close(); });

      document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && wrapper.classList.contains('visible')) close();
      });

      // Prevenir que clics dentro del modal cierren
      document.querySelector('.modal-inner').addEventListener('click', function(e) { e.stopPropagation(); });
    })();
    ```

### Ejemplo Guiado 4: Accordion FAQ Completamente Accesible

=== "HTML"

    ``` html
    <div class="ejemplo-container">
      <h2>Preguntas Frecuentes Accesibles</h2>
      <div class="faq-accordion">
        <div class="faq-section">
          <button class="faq-trigger" id="faqBtn1" aria-expanded="false" aria-controls="faqPanel1">
            <span>¿Cuál es el plazo de envío?</span>
            <span class="faq-icon" aria-hidden="true">+</span>
          </button>
          <div class="faq-panel" id="faqPanel1" role="region" aria-labelledby="faqBtn1" hidden>
            <p>Envío estándar: 3-5 días laborables. Envío express: 24-48 horas. Envío internacional: 7-15 días según destino.</p>
          </div>
        </div>
        <div class="faq-section">
          <button class="faq-trigger" id="faqBtn2" aria-expanded="false" aria-controls="faqPanel2">
            <span>¿Cómo puedo realizar una devolución?</span>
            <span class="faq-icon" aria-hidden="true">+</span>
          </button>
          <div class="faq-panel" id="faqPanel2" role="region" aria-labelledby="faqBtn2" hidden>
            <p>Tienes 30 días desde la recepción. Accede a tu cuenta, selecciona el pedido y solicita la devolución. Te enviaremos una etiqueta de envío gratuita.</p>
          </div>
        </div>
      </div>
    </div>
    <link rel="stylesheet" href="./styles.css">
    <script src="./script.js"></script>
    ```

=== "CSS"

    ``` css
    .faq-accordion { max-width: 650px; }
    .faq-section { border: 1px solid #e0e0e0; border-radius: 0.5rem; margin-bottom: 0.5rem; overflow: hidden; }
    .faq-trigger { display: flex; justify-content: space-between; align-items: center; width: 100%; padding: 0.9rem 1.2rem; background: none; border: none; font-size: 1rem; font-weight: 500; color: #333; cursor: pointer; text-align: left; transition: background 0.2s; }
    .faq-trigger:hover { background: #f8f9fa; }
    .faq-trigger:focus-visible { outline: 3px solid #4a90d9; outline-offset: -2px; border-radius: 0.5rem; }
    .faq-trigger[aria-expanded="true"] { color: #4a90d9; background: #f0f5ff; }
    .faq-icon { font-size: 1.4rem; transition: transform 0.3s ease; color: #999; }
    .faq-trigger[aria-expanded="true"] .faq-icon { transform: rotate(45deg); color: #4a90d9; }
    .faq-panel { max-height: 0; overflow: hidden; transition: max-height 0.4s ease, opacity 0.3s ease; opacity: 0; }
    .faq-panel:not([hidden]) { max-height: 300px; opacity: 1; }
    .faq-panel p { padding: 0 1.2rem 1.2rem; color: #555; line-height: 1.7; margin: 0; }
    ```

=== "JS"

    ``` js
    (function() {
      var btns = Array.from(document.querySelectorAll('.faq-trigger'));
      function toggle(btn) {
        var panel = document.getElementById(btn.getAttribute('aria-controls'));
        var expanded = btn.getAttribute('aria-expanded') === 'true';
        btn.setAttribute('aria-expanded', !expanded);
        if (expanded) panel.setAttribute('hidden',''); else panel.removeAttribute('hidden');
      }
      btns.forEach(function(btn, i) {
        btn.addEventListener('click', function() { toggle(btn); });
        btn.addEventListener('keydown', function(e) {
          var target = null;
          if (e.key === 'ArrowDown') { e.preventDefault(); target = btns[(i+1) % btns.length]; }
          else if (e.key === 'ArrowUp') { e.preventDefault(); target = btns[(i-1+btns.length) % btns.length]; }
          else if (e.key === 'Home') { e.preventDefault(); target = btns[0]; }
          else if (e.key === 'End') { e.preventDefault(); target = btns[btns.length-1]; }
          else if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); toggle(btn); }
          if (target) target.focus();
        });
      });
    })();
    ```

### Ejemplo Guiado 5: Tabs Accesibles con Navegación por Flechas

=== "HTML"

    ``` html
    <div class="ejemplo-container">
      <h2>Panel de Configuración (Tabs Accesibles)</h2>
      <div role="tablist" aria-label="Configuración" class="tabs-bar">
        <button role="tab" aria-selected="true" aria-controls="panel1" id="tab1" tabindex="0" class="tab-btn active">General</button>
        <button role="tab" aria-selected="false" aria-controls="panel2" id="tab2" tabindex="-1" class="tab-btn">Seguridad</button>
        <button role="tab" aria-selected="false" aria-controls="panel3" id="tab3" tabindex="-1" class="tab-btn">Notificaciones</button>
      </div>
      <div role="tabpanel" id="panel1" aria-labelledby="tab1" class="tab-panel-content"><p>Ajustes generales de la cuenta: idioma, zona horaria y formato de fecha.</p></div>
      <div role="tabpanel" id="panel2" aria-labelledby="tab2" class="tab-panel-content" hidden><p>Configuración de seguridad: autenticación en dos factores, cambio de contraseña y revisión de dispositivos.</p></div>
      <div role="tabpanel" id="panel3" aria-labelledby="tab3" class="tab-panel-content" hidden><p>Preferencias de notificaciones por email, push y dentro de la aplicación.</p></div>
    </div>
    <link rel="stylesheet" href="./styles.css">
    <script src="./script.js"></script>
    ```

=== "CSS"

    ``` css
    .tabs-bar { display: flex; border-bottom: 2px solid #e0e0e0; }
    .tab-btn { padding: 0.7rem 1.2rem; background: none; border: none; font-size: 0.95rem; color: #666; cursor: pointer; font-weight: 500; transition: color 0.2s; }
    .tab-btn:hover { color: #333; }
    .tab-btn.active, .tab-btn[aria-selected="true"] { color: #4a90d9; border-bottom: 3px solid #4a90d9; margin-bottom: -2px; }
    .tab-btn:focus-visible { outline: 3px solid #4a90d9; outline-offset: -2px; border-radius: 2px 2px 0 0; }
    .tab-panel-content { padding: 1.2rem; background: #fff; border: 1px solid #e0e0e0; border-top: none; border-radius: 0 0 0.5rem 0.5rem; color: #555; line-height: 1.6; }
    ```

=== "JS"

    ``` js
    (function() {
      var tabs = Array.from(document.querySelectorAll('[role="tab"]'));
      var panels = Array.from(document.querySelectorAll('[role="tabpanel"]'));
      function activate(tab) {
        tabs.forEach(function(t) { t.setAttribute('aria-selected','false'); t.setAttribute('tabindex','-1'); t.classList.remove('active'); });
        panels.forEach(function(p) { p.setAttribute('hidden',''); });
        tab.setAttribute('aria-selected','true'); tab.setAttribute('tabindex','0'); tab.classList.add('active');
        var panel = document.getElementById(tab.getAttribute('aria-controls'));
        if (panel) panel.removeAttribute('hidden');
      }
      tabs.forEach(function(tab, i) {
        tab.addEventListener('click', function() { activate(tab); });
        tab.addEventListener('keydown', function(e) {
          var target = null;
          if (e.key === 'ArrowRight') { e.preventDefault(); target = tabs[(i+1)%tabs.length]; }
          else if (e.key === 'ArrowLeft') { e.preventDefault(); target = tabs[(i-1+tabs.length)%tabs.length]; }
          else if (e.key === 'Home') { e.preventDefault(); target = tabs[0]; }
          else if (e.key === 'End') { e.preventDefault(); target = tabs[tabs.length-1]; }
          else if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); activate(tab); }
          if (target) target.focus();
        });
      });
    })();
    ```

### Ejemplo Guiado 6: Tabla de Datos Accesible

=== "HTML"

    ``` html
    <div class="ejemplo-container">
      <h2>Informe de Ventas (Tabla Accesible)</h2>
      <div class="table-wrapper" role="region" aria-labelledby="tablaTitulo" tabindex="0">
        <table aria-describedby="tablaDesc">
          <caption id="tablaTitulo">Ventas mensuales por producto - Primer trimestre 2025</caption>
          <p id="tablaDesc" class="sr-only">La tabla muestra las ventas de enero a marzo. Haga clic en los encabezados para ordenar.</p>
          <thead>
            <tr>
              <th scope="col">Producto</th>
              <th scope="col" aria-sort="descending">Enero <span aria-hidden="true">&#9660;</span></th>
              <th scope="col">Febrero</th>
              <th scope="col">Marzo</th>
              <th scope="col">Total</th>
            </tr>
          </thead>
          <tbody>
            <tr><th scope="row">Zapatillas Running</th><td>1.250 €</td><td>1.480 €</td><td>1.620 €</td><td>4.350 €</td></tr>
            <tr><th scope="row">Camiseta Técnica</th><td>890 €</td><td>920 €</td><td>1.100 €</td><td>2.910 €</td></tr>
            <tr><th scope="row">Mochila Senderismo</th><td>2.100 €</td><td>1.950 €</td><td>2.300 €</td><td>6.350 €</td></tr>
          </tbody>
        </table>
      </div>
    </div>
    <link rel="stylesheet" href="./styles.css">
    ```

=== "CSS"

    ``` css
    .table-wrapper { overflow-x: auto; }
    table { border-collapse: collapse; width: 100%; font-size: 0.95rem; }
    caption { font-weight: 600; font-size: 1.1rem; margin-bottom: 0.75rem; text-align: left; }
    thead th { background: #f0f0f0; padding: 0.7rem; text-align: left; border-bottom: 2px solid #ccc; font-weight: 600; }
    tbody td, tbody th { padding: 0.6rem 0.7rem; border-bottom: 1px solid #eee; }
    tbody th { font-weight: 500; text-align: left; }
    .sr-only { position:absolute; width:1px; height:1px; padding:0; margin:-1px; overflow:hidden; clip:rect(0,0,0,0); white-space:nowrap; border:0; }
    ```

### Ejemplo Guiado 7: Skip Links Implementación Completa

=== "HTML"

    ``` html
    <div class="ejemplo-container">
      <h2>Demo de Skip Links</h2>
      <p class="instrucciones">Presiona Tab al cargar la página. Aparecerá un enlace "Saltar al contenido".</p>
      <div class="demo-skip">
        <a href="#demo-main" class="demo-skip-link">Saltar al contenido principal</a>
        <header class="demo-header-bar" role="banner">
          <nav aria-label="Principal"><a href="#">Inicio</a> <a href="#">Productos</a> <a href="#">Contacto</a></nav>
        </header>
        <main id="demo-main" tabindex="-1">
          <h1>Contenido Principal</h1>
          <p>El foco llegó aquí directamente gracias al skip link, sin tener que tabular por todos los enlaces de navegación.</p>
        </main>
      </div>
    </div>
    <link rel="stylesheet" href="./styles.css">
    ```

=== "CSS"

    ``` css
    .demo-skip-link { position: absolute; top: -100px; left: 10px; background: #2c3e50; color: #fff; padding: 0.6rem 1.2rem; z-index: 1000; border-radius: 0 0 0.3rem 0.3rem; text-decoration: none; font-weight: 500; }
    .demo-skip-link:focus { top: 0; }
    .demo-header-bar { background: #34495e; padding: 0.8rem; }
    .demo-header-bar a { color: #ecf0f1; margin-right: 1.5rem; }
    .instrucciones { background: #e8f4f8; padding: 0.8rem; border-radius: 0.5rem; color: #2c3e50; }
    ```

### Ejemplo Guiado 8: Menú Desplegable Accesible

=== "HTML"

    ``` html
    <div class="ejemplo-container">
      <h2>Menú Desplegable Accesible</h2>
      <div class="dropdown">
        <button class="dropdown-btn" aria-haspopup="true" aria-expanded="false" id="dropdownBtn">
          Opciones <span aria-hidden="true">&#9660;</span>
        </button>
        <ul class="dropdown-menu" id="dropdownMenu" role="menu" aria-labelledby="dropdownBtn" hidden>
          <li role="none"><button role="menuitem" tabindex="-1">Editar</button></li>
          <li role="none"><button role="menuitem" tabindex="-1">Duplicar</button></li>
          <li role="none"><hr role="separator"></li>
          <li role="none"><button role="menuitem" tabindex="-1" class="danger-item">Eliminar</button></li>
        </ul>
      </div>
    </div>
    <link rel="stylesheet" href="./styles.css">
    <script src="./script.js"></script>
    ```

=== "CSS"

    ``` css
    .dropdown { position: relative; display: inline-block; }
    .dropdown-btn { padding: 0.6rem 1.2rem; background: #f0f0f0; border: 1px solid #ccc; border-radius: 0.4rem; cursor: pointer; font-size: 0.95rem; }
    .dropdown-btn:focus-visible { outline: 3px solid #4a90d9; outline-offset: 2px; }
    .dropdown-menu { position: absolute; top: 100%; left: 0; background: #fff; border: 1px solid #ddd; border-radius: 0.4rem; box-shadow: 0 4px 12px rgba(0,0,0,0.1); list-style: none; padding: 0.3rem 0; margin: 0.25rem 0 0; min-width: 180px; z-index: 100; }
    .dropdown-menu[hidden] { display: none; }
    .dropdown-menu button { display: block; width: 100%; padding: 0.6rem 1rem; background: none; border: none; text-align: left; cursor: pointer; font-size: 0.9rem; }
    .dropdown-menu button:hover { background: #f5f5f5; }
    .dropdown-menu button:focus-visible { background: #e8f0fe; outline: none; }
    .danger-item { color: #dc3545; }
    hr[role="separator"] { border: none; border-top: 1px solid #eee; margin: 0.3rem 0; }
    ```

=== "JS"

    ``` js
    (function() {
      var btn = document.getElementById('dropdownBtn');
      var menu = document.getElementById('dropdownMenu');
      var items = Array.from(menu.querySelectorAll('[role="menuitem"]'));

      btn.addEventListener('click', function() {
        var open = btn.getAttribute('aria-expanded') === 'true';
        btn.setAttribute('aria-expanded', !open);
        menu.hidden = open;
        if (!open) { items[0].focus(); }
      });

      btn.addEventListener('keydown', function(e) {
        if (e.key === 'ArrowDown') { e.preventDefault(); btn.setAttribute('aria-expanded','true'); menu.hidden = false; items[0].focus(); }
      });

      menu.addEventListener('keydown', function(e) {
        var idx = items.indexOf(document.activeElement);
        if (e.key === 'ArrowDown') { e.preventDefault(); items[(idx+1) % items.length].focus(); }
        else if (e.key === 'ArrowUp') { e.preventDefault(); items[(idx-1+items.length) % items.length].focus(); }
        else if (e.key === 'Escape') { e.preventDefault(); closeMenu(); }
        else if (e.key === 'Tab') { closeMenu(); }
      });

      function closeMenu() { btn.setAttribute('aria-expanded','false'); menu.hidden = true; btn.focus(); }
      document.addEventListener('click', function(e) { if (!btn.contains(e.target) && !menu.contains(e.target)) closeMenu(); });
    })();
    ```

### Ejemplo Guiado 9: Toast Notifications con aria-live

=== "HTML"

    ``` html
    <div class="ejemplo-container">
      <h2>Notificaciones Accesibles con aria-live</h2>
      <button onclick="accesibleToast('exito','Cambios guardados correctamente.')" class="toast-btn exito">Guardar (Éxito)</button>
      <button onclick="accesibleToast('error','No se pudo conectar con el servidor. Revisa tu conexión.')" class="toast-btn error">Error de red</button>
      <div id="accesibleToastContainer" aria-label="Notificaciones" class="toast-acc-container"></div>
    </div>
    <link rel="stylesheet" href="./styles.css">
    <script src="./script.js"></script>
    ```

=== "CSS"

    ``` css
    .toast-btn { padding: 0.5rem 1rem; border: none; border-radius: 0.4rem; color: #fff; cursor: pointer; margin-right: 0.5rem; font-weight: 500; }
    .toast-btn.exito { background: #28a745; } .toast-btn.error { background: #dc3545; }
    .toast-acc-container { position: fixed; bottom: 1rem; right: 1rem; z-index: 9999; display: flex; flex-direction: column-reverse; gap: 0.5rem; max-width: 380px; }
    .toast-acc { background: #fff; padding: 0.8rem 1rem; border-radius: 0.5rem; box-shadow: 0 4px 12px rgba(0,0,0,0.15); border-left: 4px solid #6c757d; font-size: 0.9rem; animation: slideIn 0.35s ease; }
    .toast-acc.exito { border-left-color: #28a745; } .toast-acc.error { border-left-color: #dc3545; }
    @keyframes slideIn { from {transform: translateX(120%); opacity: 0;} to {transform: translateX(0); opacity: 1;} }
    ```

=== "JS"

    ``` js
    function accesibleToast(tipo, mensaje, duracion) {
      duracion = duracion || 5000;
      var container = document.getElementById('accesibleToastContainer');
      var toast = document.createElement('div');
      toast.className = 'toast-acc ' + tipo;
      toast.setAttribute('role', 'status'); /* aria-live polite implícito */
      toast.textContent = mensaje;
      container.insertBefore(toast, container.firstChild);
      setTimeout(function() { toast.style.opacity = '0'; toast.style.transition = 'opacity 0.3s'; setTimeout(function() { if (toast.parentNode) toast.remove(); }, 300); }, duracion);
    }
    ```

### Ejemplo Guiado 10: Dark Mode Toggle Accesible

=== "HTML"

    ``` html
    <div class="ejemplo-container">
      <h2>Toggle de Modo Oscuro Accesible</h2>
      <button id="a11yDarkToggle" aria-pressed="false" aria-label="Activar modo oscuro" class="a11y-toggle">
        <span class="a11y-toggle-sun" aria-hidden="true">&#9728;&#65039;</span>
        <span class="a11y-toggle-moon" aria-hidden="true">&#127769;</span>
      </button>
      <div class="a11y-card">Este contenido cambiará de tema respetando la accesibilidad visual. El estado se anuncia a lectores de pantalla mediante aria-pressed.</div>
    </div>
    <link rel="stylesheet" href="./styles.css">
    <script src="./script.js"></script>
    ```

=== "CSS"

    ``` css
    :root { --bg: #fff; --text: #333; --card: #f8f9fa; --border: #e0e0e0; transition: background-color 0.4s ease, color 0.3s ease; }
    html.a11y-dark { --bg: #1a1a2e; --text: #e0e0e0; --card: #16213e; --border: #333355; }
    body { background: var(--bg); color: var(--text); }
    .a11y-toggle { width: 44px; height: 44px; border-radius: 50%; border: 2px solid var(--border); background: var(--card); cursor: pointer; display: flex; align-items: center; justify-content: center; font-size: 1.3rem; color: var(--text); transition: background 0.3s, border-color 0.3s; }
    .a11y-toggle:focus-visible { outline: 3px solid #4a90d9; outline-offset: 3px; }
    html:not(.a11y-dark) .a11y-toggle-moon { display: none; }
    html.a11y-dark .a11y-toggle-sun { display: none; }
    .a11y-card { background: var(--card); border: 1px solid var(--border); border-radius: 0.5rem; padding: 1.2rem; margin-top: 1rem; transition: background 0.3s, border-color 0.3s; }
    ```

=== "JS"

    ``` js
    (function() {
      var btn = document.getElementById('a11yDarkToggle');
      function apply(dark) {
        document.documentElement.classList.toggle('a11y-dark', dark);
        btn.setAttribute('aria-pressed', dark ? 'true' : 'false');
        btn.setAttribute('aria-label', dark ? 'Activar modo claro' : 'Activar modo oscuro');
        try { localStorage.setItem('a11y-theme', dark ? 'dark' : 'light'); } catch(e) {}
      }
      btn.addEventListener('click', function() { apply(!document.documentElement.classList.contains('a11y-dark')); });
      var saved = localStorage.getItem('a11y-theme');
      if (saved === 'dark') apply(true);
      else if (saved === 'light') apply(false);
      else if (window.matchMedia('(prefers-color-scheme: dark)').matches) apply(true);
    })();
    ```


## Casos reales

### Caso Real 1: Auditoría de Accesibilidad de la Sede Electrónica (sede.administracion.gob.es)

La Sede Electrónica del Gobierno de España es un caso de estudio paradigmático porque, como organismo del sector público, está legalmente obligada a cumplir con el RD 1112/2018 y la EN 301 549 (WCAG 2.1 AA). Realicemos una auditoría de accesibilidad analizando las barreras más comunes y sus soluciones:

**Problemas de contraste:** Analizando la página principal con la herramienta Colour Contrast Analyser, encontramos que varios elementos de texto secundario (fechas, metadatos, breadcrumbs) presentan un ratio de contraste de aproximadamente 3.8:1, por debajo del mínimo 4.5:1 exigido por el criterio 1.4.3 para texto normal. La solución pasa por oscurecer estos textos secundarios a un color como #595959 sobre fondo blanco, que proporciona un ratio de 7:1.

**Navegación por teclado:** La navegación por teclado es mayoritariamente correcta, con un indicador de foco visible (aunque débil) y un orden de tabulación lógico. Sin embargo, el menú principal de navegación no implementa correctamente el patrón ARIA para menús: los submenús no se expanden con Enter o Espacio, sino solo con hover, dejándolos inaccesibles para usuarios de teclado. La solución técnica es implementar `aria-expanded` en los botones padre y mostrar los submenús también con eventos `keydown` (Enter/Espacio) y `focusin`, no solo con `mouseenter`.

**Formularios:** Los formularios de búsqueda utilizan correctamente `<label>` asociadas a los inputs mediante `for`/`id` y mensajes de error con `role="alert"`. Sin embargo, no se proporciona un resumen de errores al enviar un formulario con múltiples campos incorrectos. El usuario de lector de pantalla debe navegar campo por campo para encontrar los errores. La solución es añadir un contenedor `aria-live="assertive"` al inicio del formulario que liste todos los errores tras el envío, con enlaces internos a cada campo erróneo.

**Estructura de encabezados:** La jerarquía de encabezados presenta saltos de nivel (de `h1` a `h3` sin `h2` intermedio en algunas secciones), lo que viola las buenas prácticas de estructura (criterio 1.3.1 de forma implícita). La solución es revisar la jerarquía para que sea estrictamente secuencial.

### Caso Real 2: Auditoría de un Portal Bancario (ejemplo: banca online de una entidad española)

Los portales bancarios presentan desafíos de accesibilidad particularmente críticos porque manejan información financiera sensible y transacciones económicas. Analicemos los problemas más graves encontrados típicamente:

**Sesiones con timeout no configurable:** La mayoría de portales bancarios cierran la sesión automáticamente tras 5-10 minutos de inactividad por motivos de seguridad, pero no proporcionan un mecanismo para que el usuario sea advertido con antelación y pueda extender la sesión. Esto viola el criterio 2.2.1 (Timing Adjustable, Nivel A). La solución es mostrar un diálogo modal 2 minutos antes del cierre que pregunte "¿Desea continuar con la sesión?" con un contador regresivo visible, permitiendo al usuario extenderla sin perder datos.

**CAPTCHAs inaccesibles:** Muchos portales bancarios utilizan CAPTCHAs visuales sin alternativa de audio accesible, bloqueando completamente el acceso a usuarios ciegos. El criterio 1.1.1 (Non-text Content, Nivel A) exige alternativas textuales, y las WCAG recomiendan utilizar métodos de verificación que no dependan exclusivamente de una capacidad sensorial. Soluciones modernas incluyen reCAPTCHA v3 (invisible, basado en comportamiento) o hCaptcha con opción de accesibilidad por cookie.

**Gráficos financieros sin alternativa:** Los dashboards con gráficos de evolución de inversiones, gastos o ahorros suelen implementarse con `<canvas>` o SVG sin atributos ARIA, siendo completamente invisibles para lectores de pantalla. El criterio 1.1.1 exige alternativas textuales. La solución es proporcionar una tabla de datos equivalente oculta visualmente pero accesible (`sr-only`) que describa los mismos datos en formato tabular, o añadir `role="img"` y `aria-label` al SVG con una descripción significativa.

### Caso Real 3: Auditoría de un Ecommerce (ejemplo: tienda online de moda)

Las tiendas online son el sector donde la accesibilidad tiene un impacto más directo en el negocio: un carrito de compra inaccesible significa ventas perdidas.

**Filtros de producto solo con ratón:** Los filtros laterales (por talla, color, precio) suelen implementarse con sliders, checkboxes estilizados y selects sin las correspondientes contrapartidas de teclado. Un usuario que navega con teclado no puede seleccionar un rango de precios en un slider que solo responde a `mousedown`/`mousemove`. La solución es implementar controles alternativos de entrada numérica (dos campos de texto para precio mínimo y máximo) junto al slider visual, asegurando que ambos estén sincronizados.

**Imágenes de producto sin texto alternativo descriptivo:** Es muy común encontrar `alt="producto"` o `alt="imagen"` en las fichas de producto. Un usuario ciego no puede saber el color, el estampado, el corte o el material de la prenda. El texto alternativo debe describir la imagen de forma útil: `alt="Vestido midi azul marino con estampado floral blanco, manga larga, tejido de algodón orgánico"`.

**Proceso de checkout no operable por teclado:** Los selectores de dirección de envío, métodos de pago y confirmación de pedido a veces utilizan componentes personalizados que no son focusables ni responden a eventos de teclado. Un usuario que ha llenado su carrito no puede completar la compra. La solución es asegurar que cada paso del checkout use controles nativos o, si son personalizados, implemente los roles y la navegación por teclado correspondientes según los patrones ARIA.

**Notificaciones dinámicas sin aria-live:** Cuando se añade un producto al carrito, aparece una notificación (tipo toast o mini ventana). Si no tiene `role="status"`, un lector de pantalla no anunciará que el producto se ha añadido, dejando al usuario sin confirmación de su acción. La solución es simple: añadir `role="status"` al contenedor de la notificación.


## Actividades guiadas

### Actividad Guiada 1: Auditoría de Accesibilidad de una Página Web Real

**Objetivo:** Realizar una auditoría de accesibilidad completa de una página web real (elegida por el alumno) utilizando herramientas automáticas y verificación manual, documentando los hallazgos en un informe estructurado con recomendaciones de corrección.

**Material necesario:** Navegador Chrome con Lighthouse y axe DevTools instalados, extensión WAVE, Colour Contrast Analyser, NVDA (Windows) o VoiceOver (Mac), plantilla de informe.

**Duración estimada:** 120 minutos.

**Desarrollo:** (1) Selecciona una página web de un servicio público o comercio electrónico. (2) Ejecuta Lighthouse y anota la puntuación de accesibilidad y cada violación encontrada. (3) Ejecuta axe DevTools y documenta todos los issues con su severidad y ubicación. (4) Realiza una inspección visual con WAVE, anotando todos los errores (rojos) y alertas (amarillos). (5) Verifica manualmente: navegación por teclado, orden de tabulación, estilos de foco, estructura de encabezados, etiquetas de formulario, atributos alt, skip links. (6) Prueba la página con NVDA/VoiceOver y documenta la experiencia (¿se entiende la estructura? ¿los enlaces tienen sentido? ¿los formularios son usables?). (7) Elabora un informe con: resumen ejecutivo, tabla de hallazgos (criterio WCAG, nivel, severidad, ubicación, descripción, solución), y recomendaciones priorizadas.

**Entregable:** Informe de auditoría en formato PDF con todos los hallazgos documentados.

### Actividad Guiada 2: Transformación de una Página No Accesible a Accesible

**Objetivo:** Partiendo de una página HTML proporcionada por el profesor que contiene múltiples barreras de accesibilidad (imágenes sin alt, formularios sin labels, contraste insuficiente, falta de landmarks, etc.), corregir todas las barreras hasta alcanzar el nivel AA de WCAG 2.1.

**Duración estimada:** 90 minutos.

**Desarrollo:** Se proporciona una página HTML "enferma" con al menos 15 barreras de accesibilidad. El alumno debe: añadir landmarks HTML5, corregir la jerarquía de encabezados, añadir atributos alt descriptivos, asociar labels a todos los campos de formulario, mejorar el contraste de color, añadir estilos de foco visibles, implementar un skip link, y añadir atributos ARIA donde sea necesario. Al finalizar, debe ejecutar Lighthouse y verificar que la puntuación es 100.

### Actividad Guiada 3: Construcción de un Componente Accordion según Patrón ARIA

**Objetivo:** Construir desde cero un componente de acordeón que cumpla estrictamente con el patrón ARIA Disclosure, incluyendo toda la navegación por teclado, estados aria, animaciones y testing con lector de pantalla.

**Duración estimada:** 60 minutos.

### Actividad Guiada 4: Testing con Lector de Pantalla

**Objetivo:** Aprender a utilizar NVDA o VoiceOver para evaluar la accesibilidad de una página web, practicando las técnicas de navegación más comunes que utilizan los usuarios reales.

**Duración estimada:** 60 minutos.

### Actividad Guiada 5: Implementación de un Buscador Accesible con ARIA Combobox

**Objetivo:** Construir un campo de búsqueda con autocompletado que implemente el patrón ARIA Combobox (List Autocomplete), con todos los atributos aria, navegación por teclado y anuncio del número de resultados.

**Duración estimada:** 75 minutos.


## Actividades propuestas

### Actividad Propuesta 1: Auditoría Completa de un Portal de Empleo Público

Realiza una auditoría de accesibilidad WCAG 2.1 AA del portal de empleo público de tu comunidad autónoma. Documenta al menos 15 hallazgos con su criterio WCAG, severidad, y solución técnica propuesta. Presta especial atención a los formularios de inscripción (¿son operables por teclado? ¿las etiquetas están correctamente asociadas? ¿los errores se anuncian con aria-live?). Verifica también los PDFs descargables (¿son accesibles o son imágenes escaneadas sin OCR?).

### Actividad Propuesta 2: Página Web Municipal Totalmente Accesible

Diseña y desarrolla la página de inicio de un ayuntamiento ficticio que cumpla WCAG 2.1 AA. Debe incluir: skip links, landmarks semánticos, jerarquía de encabezados correcta, carrusel de noticias accesible (con pausa, navegación por teclado y aria-live), formulario de contacto accesible (con validación, resumen de errores y confirmación aria-live), tabla de eventos con `scope` y `caption`, y declaración de accesibilidad. Verifica con Lighthouse (puntuación 100) y prueba con NVDA.

### Actividad Propuesta 3: Sistema de Navegación Multinivel Accesible

Implementa un menú de navegación con tres niveles de profundidad que cumpla el patrón ARIA Menu/Menubar. Debe funcionar completamente con teclado (Enter/Espacio para expandir, Escape para cerrar, flechas para navegar), anunciar correctamente los estados con aria-expanded, y ser responsive (en móvil se transforma en un menú hamburguesa accesible).

### Actividad Propuesta 4: Formulario de Compra Accesible Paso a Paso

Desarrolla un checkout de varios pasos (dirección, envío, pago, confirmación) completamente accesible. Cada paso debe anunciarse al cargar (con foco en el encabezado), los errores deben mostrarse en un resumen aria-live assertive con enlaces a los campos erróneos, el progreso debe indicarse con un stepper accesible (con aria-current="step"), y los cambios de paso deben ser suaves y mantener el foco.

### Actividad Propuesta 5: Tabla de Datos Compleja con Ordenación y Filtros Accesibles

Crea una tabla de datos con al menos 50 filas que permita ordenación por columnas (anunciando el estado con aria-sort) y filtrado. Los filtros deben ser accesibles por teclado, los cambios en la tabla deben anunciarse con aria-live, y la paginación debe ser completamente operable sin ratón.


## Actividades de ampliación

### Actividad de Ampliación 1: Kit de Componentes Accesibles

Desarrolla una librería de componentes UI que implemente al menos 10 patrones ARIA Authoring Practices: Accordion, Alert Dialog, Breadcrumb, Carousel, Combobox, Dialog (Modal), Disclosure, Menu, Tabs, y Tooltip. Cada componente debe ser autocontenido (HTML/CSS/JS), completamente accesible, y documentado con su comportamiento de teclado esperado, atributos ARIA utilizados y casos de prueba. La librería debe incluir tests automáticos de accesibilidad con axe-core.

### Actividad de Ampliación 2: Aplicación Web Completa con Accesibilidad Verificada

Desarrolla una aplicación web completa (por ejemplo, un gestor de tareas, un blog o un portfolio) verificando la accesibilidad en cada etapa: usa ESLint con plugin de accesibilidad (eslint-plugin-jsx-a11y si usas React, o similares), integra axe-core en tus tests, realiza pruebas manuales con teclado y lector de pantalla, y documenta el cumplimiento WCAG 2.1 AA en una declaración de accesibilidad. Implementa un sistema de preferencias de accesibilidad (tema oscuro/claro, reducción de movimiento, alto contraste, tamaño de fuente) que se persista en localStorage.

### Actividad de Ampliación 3: Investigación sobre Accesibilidad en Frameworks Modernos

Investiga y documenta el estado de la accesibilidad en los principales frameworks y librerías JavaScript (React, Vue, Angular, Svelte). Analiza qué herramientas proporciona cada uno para garantizar la accesibilidad, qué trampas comunes existen, y qué componentes de terceros ofrecen las mejores garantías de accesibilidad. Compara React ARIA (Adobe), Radix UI, Headless UI, Angular CDK, y Vuetify desde la perspectiva de la accesibilidad. Elabora un informe con recomendaciones para elegir la stack tecnológica más accesible.


## Buenas prácticas

1. **Empieza con HTML semántico siempre.** Antes de pensar en ARIA, asegúrate de usar los elementos HTML nativos correctos para cada función. Un `<button>` nativo ya es focusable, clickable, responde a Enter y Espacio, y anuncia su rol sin necesidad de una sola línea de JavaScript. No reemplaces un `<button>` por un `<div>` con `role="button"` a menos que sea absolutamente inevitable.

2. **No elimines el outline sin reemplazo.** Si quitas el `outline` por razones estéticas, debes proporcionar un indicador de foco alternativo igual o más visible. Usa `:focus-visible` para aplicar el foco solo cuando el usuario navega con teclado.

3. **Prueba con teclado real.** Dedica al menos 15 minutos en cada sprint a navegar por tu aplicación usando exclusivamente el teclado. Si no puedes completar una tarea, un usuario con discapacidad motriz tampoco podrá.

4. **Usa un lector de pantalla al menos una vez al mes.** Configura NVDA (gratuito) y navega por tu aplicación. Escuchar cómo "lee" tu interfaz un lector de pantalla es la forma más reveladora de entender los problemas de accesibilidad.

5. **Verifica el contraste de color en todo el texto.** Usa herramientas como Colour Contrast Analyser (gratuito, de The Paciello Group) para verificar cada combinación de color texto/fondo. No confíes en tu ojo: un gris que te parece legible puede tener un ratio de **2.5:1**, muy por debajo del **4.5:1** exigido.

6. **Proporciona alternativas textuales descriptivas y útiles.** Un `alt="foto"` no ayuda a nadie. Describe la imagen como lo harías por teléfono a alguien que no puede verla. Si la imagen es puramente decorativa, usa `alt=""` para que el lector de pantalla la ignore.

7. **No hagas trampa con el contraste usando texto grande.** El criterio **1.4.3** exige **4.5:1** para texto normal y **3:1** para texto grande (más de 18px o 14px en negrita). No uses tamaños de fuente grandes solo para eludir los requisitos de contraste.

8. **Todos los formularios deben tener etiquetas visibles y asociadas.** Usa `<label for="id">` SIEMPRE. No uses placeholder como sustituto de label (desaparece al escribir, tiene bajo contraste y no es leído por todos los lectores de pantalla). Si el diseño no permite label visible, usa `aria-label` o `aria-labelledby`.

9. **Los mensajes de error deben ser claros y accesibles.** No uses solo color rojo para indicar errores (criterio 1.4.1). Añade texto descriptivo, iconos, y asegúrate de que los errores se anuncian con `aria-live` o `role="alert"`.

10. **Automatiza las auditorías de accesibilidad.** Integra axe-core o Lighthouse CI en tu pipeline de CI/CD. Configura un umbral mínimo de puntuación de accesibilidad (por ejemplo, 90 en Lighthouse) para que el build falle si se introducen regresiones.


## Errores frecuentes

### Error 1: Usar `tabindex` positivo (1, 2, 3...)

El uso de `tabindex` con valores mayores que 0 es uno de los errores más persistentes y dañinos. Crea un orden de tabulación artificial que se desincroniza del DOM visual, confunde a los usuarios y es una pesadilla de mantenimiento.

**Solución:** Usa exclusivamente `tabindex="0"` (incluye en orden natural) o `tabindex="-1"` (foco programático). Si necesitas un orden específico, reorganiza los elementos en el DOM.

### Error 2: Eliminar el outline sin alternativa

`* { outline: none; }` es una de las líneas de CSS más dañinas que existen. Elimina el indicador de foco para todos los elementos, haciendo la página inutilizable por teclado.

**Solución:** Nunca uses `outline: none` globalmente. Si necesitas eliminar el outline en un elemento específico, proporciona un estilo de foco alternativo visible. Mejor aún, usa `:focus-visible` para un control más granular.

### Error 3: Imágenes con `alt` vacío en imágenes informativas

Usar `alt=""` en imágenes que transmiten información importante (fotos de producto, gráficos, iconos funcionales) hace que sean invisibles para lectores de pantalla.

**Solución:** Diferencia entre imágenes decorativas (`alt=""`) e informativas (`alt="descripción útil"`). Si un icono actúa como botón, el texto accesible debe ir en el botón, no en el alt.

### Error 4: Formularios sin etiquetas asociadas

Confiar en `placeholder` o en el texto adyacente al input sin usar `<label for="...">` provoca que los lectores de pantalla no puedan identificar el propósito del campo.

**Solución:** Usa siempre `<label for="id">`. Si el diseño no permite una label visible, usa una label visualmente oculta (`sr-only`) o `aria-label` en el input.

### Error 5: Contenido dinámico sin anunciar

Añadir, eliminar o modificar contenido del DOM mediante JavaScript sin usar aria-live. El lector de pantalla no se entera de los cambios porque no tiene mecanismo para detectarlos.

**Solución:** Para cada cambio dinámico significativo, evalúa si debe ser anunciado. Si es una notificación, usa `role="status"`. Si es un error, usa `role="alert"`. Si es un resultado de búsqueda, usa `aria-live="polite"` en el contenedor.

### Error 6: Enlaces sin texto descriptivo o con texto genérico

"Leer más", "Haz clic aquí", "Aquí", "Ver más"... Estos textos de enlace no proporcionan ninguna información sobre el destino cuando se sacan de contexto (que es exactamente como los leen los usuarios de lectores de pantalla cuando listan todos los enlaces de la página).

**Solución:** El texto del enlace debe describir su propósito de forma autónoma. Usa "Ver detalles del producto X" en lugar de "Ver más". Para enlaces repetidos, usa `aria-label` para diferenciarlos.

### Error 7: Usar ARIA incorrectamente o innecesariamente

"No ARIA is better than bad ARIA" (Ningún ARIA es mejor que ARIA incorrecto). Añadir roles y atributos ARIA incorrectos puede empeorar la accesibilidad en lugar de mejorarla. Por ejemplo, añadir `role="button"` a un `<button>` nativo, o usar `aria-selected` en elementos que no son seleccionables.

**Solución:** Sigue estrictamente las 5 reglas de ARIA. Si un elemento HTML nativo ya proporciona la semántica necesaria, no añadas ARIA. Verifica siempre el árbol de accesibilidad en DevTools para confirmar que el nombre, rol y valor son los esperados.

### Error 8: Omitir la verificación manual confiando solo en herramientas automáticas

Obtener un 100 en Lighthouse y asumir que la página es completamente accesible. Las herramientas automáticas solo detectan entre el 25% y el 35% de los problemas de accesibilidad.

**Solución:** Siempre complementa las herramientas automáticas con verificación manual: navegación por teclado, prueba con lector de pantalla, verificación de alternativas textuales (¿son correctas, no solo existentes?), y comprobación de contraste con herramienta dedicada.

### Error 9: No gestionar el foco en modales y diálogos

Abrir un modal y dejar el foco en el body o en el botón que lo abrió, permitiendo que el usuario tabule por la página oculta detrás del modal.

**Solución:** Al abrir un modal, mueve el foco al primer elemento interactivo dentro del modal (normalmente el botón de cierre). Implementa focus trapping para que Tab/Shift+Tab ciclen dentro del modal. Al cerrar, devuelve el foco al elemento que lo abrió.

### Error 10: No declarar el idioma de la página

Omitir el atributo `lang` en el elemento `<html>`. Los lectores de pantalla necesitan conocer el idioma para seleccionar el sintetizador de voz correcto y pronunciar adecuadamente.

**Solución:** Siempre incluye `<html lang="es">` en la etiqueta raíz. Si hay partes del documento en otro idioma, marca esos fragmentos con `lang="en"` o el código correspondiente.

### Error 11: Uso excesivo de `aria-hidden` en elementos interactivos

Ocultar elementos del árbol de accesibilidad con `aria-hidden="true"` mientras siguen siendo focusables, creando una "trampa de foco invisible": el foco llega a un elemento que el lector de pantalla no puede leer.

**Solución:** Nunca apliques `aria-hidden="true"` a un elemento que pueda recibir foco. Si necesitas ocultar contenido de lectores de pantalla temporalmente, asegúrate de que ningún elemento dentro sea focusable, o gestiona el foco para evitarlo.


## Resumen

La accesibilidad web no es una característica opcional ni un lujo; es un derecho fundamental, una obligación legal y una necesidad de negocio. Esta unidad ha proporcionado al alumnado una formación integral que abarca desde los fundamentos conceptuales (los cuatro principios POUR, los tipos de discapacidad y su impacto en la navegación) hasta la implementación técnica detallada (WCAG, WAI-ARIA, patrones de diseño accesibles) y las metodologías de verificación (auditorías automáticas y manuales).

Hemos establecido que la accesibilidad comienza con el HTML semántico. Un uso correcto de landmarks, encabezados, etiquetas de formulario y textos alternativos resuelve aproximadamente el 70% de los problemas de accesibilidad sin necesidad de ARIA. WAI-ARIA debe reservarse para aquellos componentes y patrones de interacción que el HTML nativo no puede expresar por sí mismo: pestañas, acordeones, menús desplegables, modales, sliders y otros widgets complejos.

La navegación por teclado ha sido identificada como uno de los pilares más críticos, con un énfasis especial en la gestión del foco, los estilos de foco visibles, la implementación de skip links, y la necesidad de probar toda la aplicación exclusivamente con teclado. El conocimiento práctico de los lectores de pantalla (NVDA, VoiceOver, JAWS) capacita al alumnado para verificar sus propias implementaciones desde la perspectiva de un usuario con discapacidad visual.

El bloque de legislación ha contextualizado la accesibilidad en el marco normativo actual: RD 1112/2018 para el sector público, Ley 11/2023 (European Accessibility Act) para el sector privado, con plazos de cumplimiento que culminan en junio de 2025. El alumnado sale de esta unidad sabiendo que la accesibilidad no es una recomendación, sino una exigencia legal concreta.

Los diez ejemplos guiados han cubierto los componentes más relevantes (página completa con landmarks, formulario, modal, acordeón, tabs, tabla, skip links, menú desplegable, toast y dark mode) proporcionando implementaciones de referencia. Los tres casos reales han mostrado cómo aplicar los conocimientos adquiridos al análisis crítico de sitios web reales del gobierno, la banca y el comercio electrónico.

Finalmente, las buenas prácticas y los errores frecuentes han sintetizado la sabiduría práctica acumulada en el campo de la accesibilidad web, proporcionando al alumnado una guía clara de qué hacer y qué evitar en su práctica profesional diaria.

## Recursos complementarios

### Documentación oficial

- **WCAG 2.1 (traducción autorizada al español):** https://www.w3.org/Translations/WCAG21-es/
- **WCAG 2.2 (W3C Recommendation):** https://www.w3.org/TR/WCAG22/
- **ARIA Authoring Practices Guide:** https://www.w3.org/WAI/ARIA/apg/
- **WAI-ARIA 1.2 Specification:** https://www.w3.org/TR/wai-aria-1.2/
- **EN 301 549 V3.2.1:** https://www.etsi.org/deliver/etsi_en/301500_301599/301549/03.02.01_60/en_301549v030201p.pdf
- **Real Decreto 1112/2018 (BOE):** https://www.boe.es/buscar/doc.php?id=BOE-A-2018-12699
- **Ley 11/2023 (BOE):** https://www.boe.es/buscar/act.php?id=BOE-A-2023-1102

### Herramientas

- **axe DevTools:** https://www.deque.com/axe/devtools/
- **WAVE:** https://wave.webaim.org/
- **Lighthouse (Chrome DevTools):** integrado en Chrome
- **NVDA (lector de pantalla gratuito):** https://www.nvaccess.org/download/
- **Colour Contrast Analyser (TPGi):** https://www.tpgi.com/color-contrast-checker/
- **Accessibility Insights (Microsoft):** https://accessibilityinsights.io/

### Libros recomendados

- **"Inclusive Design Patterns"** de Heydon Pickering (Smashing Magazine)
- **"A Web for Everyone"** de Sarah Horton y Whitney Quesenbery
- **"Practical Web Inclusion and Accessibility"** de Ashley Firth
- **"Accessibility for Everyone"** de Laura Kalbag
