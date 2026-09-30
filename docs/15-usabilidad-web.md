---
icon: lucide/user-check
---

# Unidad 15: Usabilidad Web

## Objetivos de aprendizaje

Al finalizar esta unidad, el alumnado será capaz de:

- Comprender el concepto de usabilidad según la norma ISO 9241-11, diferenciando claramente entre eficacia, eficiencia y satisfacción, y distinguiendo usabilidad de conceptos relacionados como UX y accesibilidad.
- Dominar las 10 heurísticas de Nielsen como herramienta fundamental de evaluación de interfaces, sabiendo identificar ejemplos concretos de cumplimiento y violación en cualquier sitio web o aplicación.
- Planificar y ejecutar una evaluación heurística completa siguiendo la metodología de Nielsen: preparación, evaluación individual, puesta en común, escala de severidad (0-4) e informe de resultados.
- Realizar un recorrido cognitivo (cognitive walkthrough) de una interfaz, analizando paso a paso si las decisiones de diseño facilitan que un usuario novel complete tareas sin ayuda externa.
- Diseñar, planificar y ejecutar tests de usuario en sus diferentes modalidades (presencial, remoto, moderado, no moderado), incluyendo la definición de objetivos, reclutamiento, guion de tareas y análisis de resultados.
- Calcular e interpretar las principales métricas de usabilidad: tasa de éxito, tiempo de tarea, tasa de errores, eficiencia, y satisfacción mediante cuestionarios estandarizados como SUS, NPS y SEQ.
- Comprender el eye tracking como técnica de investigación, interpretando mapas de calor y gaze plots, y conociendo sus aplicaciones prácticas y limitaciones.
- Analizar heat maps (de clic, scroll y movimiento) generados por herramientas como Hotjar y Microsoft Clarity para identificar patrones de comportamiento y problemas de usabilidad.
- Diseñar y ejecutar tests A/B para comparar objetivamente variantes de diseño, comprendiendo los fundamentos de significancia estadística y el tamaño de muestra necesario.
- Utilizar Google Analytics para identificar problemas de usabilidad a partir de datos cuantitativos: tasas de rebote, embudos de conversión, páginas de salida.
- Aplicar tests de guerrilla como método ágil y económico de validación temprana de diseños.
- Analizar críticamente la usabilidad de sitios web reales como Amazon, Renfe y portales de empleo público, identificando problemas y proponiendo soluciones.

## Relación con los Resultados de Aprendizaje

- **RA1: Planifica la creación de una interfaz web.** Los principios de usabilidad deben integrarse desde la fase de planificación, definiendo flujos de tareas eficientes, arquitectura de información intuitiva y patrones de interacción que minimicen la carga cognitiva.
- **RA2: Crea interfaces web homogéneas.** Las heurísticas de consistencia y estándares (heurística 4 de Nielsen) guían la creación de interfaces homogéneas donde patrones similares se comportan de manera predecible.
- **RA5: Evalúa la accesibilidad de la interfaz web.** La usabilidad y la accesibilidad comparten metodologías de evaluación complementarias; muchas barreras de accesibilidad son también problemas de usabilidad para todos los usuarios.
- **RA6: Verifica la usabilidad de la interfaz web.** Este RA es el núcleo de la unidad. El alumnado aprende a aplicar evaluación heurística, test de usuarios, métricas de usabilidad, analítica web y otras técnicas para verificar que una interfaz cumple con criterios de calidad de uso establecidos.

## Conocimientos previos

- **Diseño de interfaces básico:** Principios de diseño visual, teoría del color, tipografía, jerarquía visual, uso de espacio en blanco, responsive design.
- **HTML y CSS:** Capacidad para construir prototipos funcionales de interfaces web sobre los que realizar pruebas de usabilidad.
- **Metodologías ágiles:** Familiaridad con Scrum, sprints y el rol del diseño en entornos ágiles, donde la usabilidad debe validarse iterativamente.
- **Estadística básica:** Media, mediana, desviación estándar, concepto de muestra y población, interpretación de porcentajes. Sin estos fundamentos, las métricas de usabilidad no pueden interpretarse correctamente.
- **Observación y empatía:** Habilidad para observar el comportamiento de usuarios sin interferir ni sesgar sus acciones. Escucha activa y capacidad de hacer preguntas sin sugerir respuestas.

## Contenidos

### 1. Fundamentos de la usabilidad web
1.1. Definición de usabilidad según ISO 9241-11: eficacia, eficiencia y satisfacción.
1.2. Diferencias entre usabilidad, UX y accesibilidad: conceptos complementarios pero distintos.
1.3. Beneficios de la usabilidad: reducción de costes de soporte, aumento de conversión, satisfacción y retención de clientes.
1.4. Retorno de la inversión (ROI) en usabilidad: evidencia empírica y casos documentados.

### 2. Las 10 Heurísticas de Nielsen
2.1. Historia y vigencia de las heurísticas de Jakob Nielsen (1994-presente).
2.2. Desarrollo detallado de cada heurística con dos ejemplos de cumplimiento y dos de violación por cada una:
  1. Visibilidad del estado del sistema
  2. Coincidencia entre el sistema y el mundo real
  3. Control y libertad del usuario
  4. Consistencia y estándares
  5. Prevención de errores
  6. Reconocimiento antes que recuerdo
  7. Flexibilidad y eficiencia de uso
  8. Diseño estético y minimalista
  9. Ayudar a los usuarios a reconocer, diagnosticar y recuperarse de errores
  10. Ayuda y documentación

### 3. Evaluación heurística
3.1. Definición y propósito: inspección por expertos basada en principios.
3.2. Proceso completo: preparación, evaluación individual, puesta en común.
3.3. Número óptimo de evaluadores: 3-5 según la fórmula de Nielsen, curva de rendimiento decreciente.
3.4. Escala de severidad (0-4): cosmético, menor, mayor, catastrófico.
3.5. Estructura y formato del informe de resultados.

### 4. Otras técnicas de inspección
4.1. Inspección de estándares: checklists de usabilidad, guías de estilo corporativas, ISO 9241.
4.2. Recorrido cognitivo (Cognitive Walkthrough): definición, proceso paso a paso, cuándo usarlo (ideal para interfaces nuevas sin usuarios).
4.3. Inspección de consistencia.

### 5. Test de usuarios
5.1. Tipos: presencial vs remoto, moderado vs no moderado.
5.2. Planificación: objetivos de investigación, criterios de reclutamiento, guion de tareas.
5.3. Número de participantes: 5 para cualitativo (Nielsen), 20-30 para cuantitativo.
5.4. Think aloud: la técnica de pensamiento en voz alta.
5.5. Ejecución: bienvenida, consentimiento, tareas, cierre.
5.6. Análisis de resultados: de observaciones a hallazgos accionables.
5.7. Herramientas: UserTesting, Maze, Lookback, Loom, UserZoom, Optimal Workshop.

### 6. Métricas de usabilidad
6.1. Tasa de éxito, tiempo de tarea, tasa de errores, eficiencia.
6.2. Satisfacción: SUS (System Usability Scale), NPS (Net Promoter Score), SEQ (Single Ease Question), UMUX, SUS-Lite.
6.3. Métricas de comportamiento vs métricas de actitud.

### 7. Eye Tracking y Heat Maps
7.1. Eye Tracking: principios, hardware, métricas (fijaciones, sacadas, áreas de interés), mapas de calor de mirada, gaze plots.
7.2. Heat Maps de comportamiento: click maps, scroll maps, move maps. Herramientas: Hotjar, Microsoft Clarity, Crazy Egg, Mouseflow.
7.3. Interpretación y limitaciones: el dato no es autoevidente, necesita contexto.

### 8. A/B Testing
8.1. Definición y fundamentos: testeo experimental controlado.
8.2. Proceso: hipótesis, definición de variantes, métrica objetivo, cálculo de tamaño muestral, ejecución, análisis.
8.3. Significancia estadística, intervalos de confianza, errores tipo I y II.
8.4. Herramientas: Google Optimize, VWO, Optimizely.

### 9. Analítica web para usabilidad
9.1. Google Analytics 4: métricas relevantes (tasa de rebote, tiempo en página, páginas por sesión, flujo de usuarios, embudos de conversión).
9.2. Identificación de problemas de usabilidad a partir de datos analíticos.
9.3. Combinación de datos cuantitativos (analítica) y cualitativos (tests, heat maps).

### 10. Tests de guerrilla
10.1. Definición: tests rápidos, informales, con pocos recursos.
10.2. Ventajas: velocidad, bajo coste, iteración rápida.
10.3. Limitaciones: sesgo de muestra, menor rigor.

## Desarrollo teórico

### 1. ¿Qué es la usabilidad web y por qué es importante?

!!! info "Definición: usabilidad (ISO 9241-11)"
    La **usabilidad** se define formalmente en la norma **ISO 9241-11** como «el grado en que un producto puede ser utilizado por usuarios específicos para alcanzar objetivos específicos con **eficacia, eficiencia y satisfacción** en un contexto de uso específico».

Esta definición establece que la usabilidad **no es una propiedad absoluta** de un sistema, sino relativa a tres factores: los **usuarios concretos** que lo utilizan, los **objetivos** que persiguen, y el **contexto** (físico, social, organizativo) en el que lo hacen. Un mismo sitio web puede ser altamente usable para un adolescente experto en tecnología e inusable para una persona mayor con poca experiencia digital, aunque ambos quieran realizar la misma tarea. La usabilidad, por tanto, debe evaluarse y diseñarse teniendo en cuenta el **perfil de los usuarios reales**, no un usuario idealizado.

Los tres componentes de la norma:

- **Eficacia** — si los usuarios pueden alcanzar sus objetivos; se mide en términos de **completitud** (¿se completó la tarea?) y **precisión** (¿se completó correctamente?). Un sistema puede ser altamente eficiente pero ineficaz si los usuarios completan tareas rápidamente pero de forma incorrecta.
- **Eficiencia** — relaciona los **recursos gastados** (tiempo, esfuerzo mental, pasos) con los resultados obtenidos. Un sistema eficaz puede ser ineficiente si requiere demasiado tiempo o esfuerzo.
- **Satisfacción** — la respuesta **subjetiva** del usuario ante el uso del producto: ausencia de incomodidad y actitudes positivas. Un sistema puede ser eficaz y eficiente pero generar frustración (por ejemplo, si cumple su función pero tiene una estética descuidada o interrumpe constantemente con notificaciones).

Los beneficios empresariales de la usabilidad están ampliamente documentados:

- **Retorno de inversión (ROI)** — Jakob Nielsen estimó un ROI de **10:1 a 100:1**: cada euro invertido en mejorar la usabilidad retorna entre **10 y 100 euros** en beneficios.
- **Menos costes de soporte** — sitios web usables generan menos llamadas al servicio de atención al cliente, menos *emails* de consulta y menos devoluciones.
- **Mayor tasa de conversión** — simplificar un *checkout* puede aumentar las ventas entre un **10%** y un **35%**.
- **Satisfacción y retención** — un cliente satisfecho no solo repite, sino que recomienda.
- **Menos costes de desarrollo** — corregir problemas de usabilidad en etapas tempranas del diseño es mucho más barato que rediseñar tras el lanzamiento.

!!! info "Usabilidad frente a UX, accesibilidad y utilidad"
    - **UX** (*User Experience*) — concepto **más amplio** que engloba la usabilidad pero también la deseabilidad, el valor emocional, la confianza, la credibilidad y el significado personal. **Don Norman**, quien acuñó el término UX, lo define como «todos los aspectos de la interacción del usuario final con la empresa, sus servicios y sus productos».
    - **Accesibilidad** — **subconjunto** específico de la UX que se centra en garantizar que personas con discapacidad puedan percibir, operar y comprender el producto. Un producto puede ser usable pero inaccesible (fácil de usar con ratón, imposible con teclado), y accesible pero no usable (técnicamente operable con lector de pantalla pero confuso y mal organizado).
    - **Utilidad** — si el producto **hace lo que el usuario necesita**. Un producto puede ser muy usable pero inútil si no resuelve un problema real del usuario.

### 2. Las 10 Heurísticas de Nielsen en profundidad

!!! info "Origen de las heurísticas de Nielsen"
    En colaboración con **Rolf Molich**, Jakob Nielsen desarrolló en **1990** las primeras heurísticas de usabilidad, refinadas y publicadas en su forma canónica de **10 principios** en **1994**. No son directrices específicas de interfaz, sino **principios amplios y generalizables** que capturan aspectos fundamentales de la interacción humano-ordenador. Han demostrado una notable longevidad porque operan a un nivel de abstracción que las hace **independientes de tecnologías concretas**: aplican tanto a interfaces de línea de comandos como a aplicaciones móviles táctiles, pasando por sitios web, aplicaciones de escritorio, cajeros automáticos, electrodomésticos inteligentes y *dashboards* de vehículos.

**H1: Visibilidad del estado del sistema.** "El diseño siempre debe mantener informados a los usuarios sobre lo que está sucediendo, mediante retroalimentación apropiada en un tiempo razonable." Esta heurística es probablemente la más fundamental y universalmente aplicable. La retroalimentación puede ser **visual** (un *spinner*, una barra de progreso, un cambio de color), **auditiva** (un sonido de notificación) o **táctil** (una vibración). El tiempo "razonable" depende del contexto: para una acción simple como marcar un *checkbox*, la respuesta debe ser **instantánea (<100 ms)**; para una carga de página, una barra de progreso con estimación de tiempo es aceptable; para una operación larga como procesar un vídeo, se necesita información sobre el estado, el progreso y el tiempo restante estimado.

**H2: Coincidencia entre el sistema y el mundo real.** "El sistema debe hablar el lenguaje de los usuarios, con palabras, frases y conceptos familiares, en lugar de términos orientados al sistema. Debe seguir las convenciones del mundo real, haciendo que la información aparezca en un orden natural y lógico." Ejemplos de cumplimiento incluyen el uso de metáforas del mundo físico (el carrito de compra, la papelera de reciclaje, el escritorio), iconos basados en objetos reales reconocibles, y lenguaje conversacional en lugar de jerga técnica. Ejemplos de violación incluyen mostrar IDs internos de base de datos al usuario ("Error: FK_Constraint_UserID_3"), usar terminología interna de la empresa que el cliente no conoce, u ordenar información alfabéticamente cuando el orden lógico para el usuario sería por relevancia o cronología.

**H3: Control y libertad del usuario.** "Los usuarios a menudo eligen funciones del sistema por error y necesitan una 'salida de emergencia' claramente marcada para abandonar el estado no deseado sin tener que pasar por un diálogo extendido. El sistema debe ofrecer deshacer y rehacer." Esta heurística aborda la libertad del usuario para explorar sin miedo a consecuencias irreversibles. Los botones "Atrás", "Cancelar", "Cerrar" y los comandos "Deshacer" son materializaciones de este principio. Una interfaz que no ofrece forma de deshacer una acción obliga al usuario a ser perfecto, lo cual genera ansiedad y ralentiza la exploración.

**H4: Consistencia y estándares.** "Los usuarios no deberían tener que preguntarse si diferentes palabras, situaciones o acciones significan lo mismo. Se deben seguir las convenciones de la plataforma y de la industria." La consistencia puede ser interna (dentro del mismo producto: todos los botones primarios tienen el mismo color, la misma acción se etiqueta igual en todas partes) o externa (con otros productos y plataformas: seguir las guías de estilo de iOS/Android/web, usar iconos estándar reconocibles). La consistencia reduce la curva de aprendizaje y la carga cognitiva porque el usuario transfiere conocimiento de una parte del sistema a otra.

**H5: Prevención de errores.** "Mejor que los buenos mensajes de error es un diseño cuidadoso que evite que ocurran errores en primer lugar." Esta heurística aboga por un diseño proactivo que elimine las condiciones propensas a errores. Ejemplos: deshabilitar opciones inválidas en lugar de permitir seleccionarlas y luego mostrar un error; usar selectores de fecha en lugar de campos de texto libre para fechas; mostrar confirmación antes de acciones destructivas; usar valores por defecto sensatos; aplicar máscaras de entrada en campos con formato fijo (DNI, teléfono, IBAN).

**H6: Reconocimiento antes que recuerdo.** "Minimizar la carga de memoria del usuario haciendo visibles los objetos, acciones y opciones. El usuario no debería tener que recordar información de una parte a otra del diálogo." La psicología cognitiva distingue entre recuerdo (generar información de la memoria sin ayudas) y reconocimiento (identificar información entre opciones presentadas). El reconocimiento es mucho más fácil y rápido. Ejemplos: menús visibles en lugar de comandos memorizados, autocompletado que sugiere opciones basadas en el historial, mostrar las opciones de filtro disponibles en lugar de esperar que el usuario sepa qué filtros existen.

**H7: Flexibilidad y eficiencia de uso.** "Los aceleradores —invisibles para el usuario novato— pueden acelerar la interacción del usuario experto, de modo que el sistema pueda adaptarse tanto a usuarios inexpertos como experimentados." Esta heurística reconoce que no todos los usuarios tienen el mismo nivel de experiencia, y que una interfaz debe servir tanto al principiante como al experto. Los atajos de teclado, las opciones de personalización, las plantillas y los flujos rápidos (como "comprar de nuevo" basado en pedidos anteriores) son ejemplos de aceleradores que no estorban al novato pero empoderan al experto.

**H8: Diseño estético y minimalista.** "Los diálogos no deben contener información irrelevante o raramente necesaria. Cada unidad extra de información en un diálogo compite con las unidades relevantes de información y disminuye su visibilidad relativa." Esta heurística se basa en el principio de que menos es más en el diseño de interfaces. El desorden visual, la sobrecarga informativa y la multiplicidad de opciones abruman al usuario y dificultan la toma de decisiones. La ley de Hick, que establece que el tiempo de decisión aumenta logarítmicamente con el número de opciones, proporciona la base científica para esta heurística.

**H9: Ayudar a los usuarios a reconocer, diagnosticar y recuperarse de errores.** "Los mensajes de error deben expresarse en lenguaje claro (no en códigos), indicar con precisión el problema y sugerir una solución de manera constructiva." Un buen mensaje de error tiene **tres componentes**:

1. **Qué salió mal**, en lenguaje del usuario.
2. **Por qué salió mal**, si es relevante.
3. **Qué puede hacer el usuario** para solucionarlo.

«Error 403 Forbidden» es un **mal mensaje**. «No tienes permiso para acceder a esta página. Si crees que deberías poder acceder, contacta con tu administrador o inicia sesión con una cuenta diferente» es un **buen mensaje**.

**H10: Ayuda y documentación.** "Aunque es mejor que el sistema pueda utilizarse sin documentación, puede ser necesario proporcionar ayuda y documentación. Esta debe ser fácil de buscar, estar enfocada en las tareas del usuario, listar pasos concretos a seguir, y no ser demasiado extensa." La ayuda debe ser contextual (relevante para lo que el usuario está haciendo), accionable (pasos concretos, no teoría), y concisa. La documentación exhaustiva en PDF rara vez se consulta; la ayuda integrada en la interfaz (tooltips, texto de ayuda junto al campo, preguntas frecuentes enlazadas) es mucho más efectiva.

### 3. Evaluación heurística: metodología

!!! info "Definición: evaluación heurística"
    La **evaluación heurística** es un método de **inspección** donde un pequeño número de evaluadores examina una interfaz y juzga si cada elemento cumple con una lista de principios de usabilidad (las heurísticas). Su popularidad en la industria se debe a su excelente relación coste-beneficio: es **rápida** (se puede completar en días, no semanas), **económica** (no requiere laboratorio, equipamiento especial ni reclutamiento masivo) y **efectiva** (encuentra un alto porcentaje de problemas de usabilidad, especialmente los más graves).

Nielsen y Molich demostraron que el número óptimo de evaluadores es **entre 3 y 5**:

| Nº de evaluadores | Problemas de usabilidad detectados |
|-------------------|------------------------------------|
| **1** | aproximadamente el **35%** |
| **2** | alrededor del **50%** |
| **5** | aproximadamente el **75-80%** |

La curva tiene un claro **rendimiento decreciente**: añadir más evaluadores por encima de 5 encuentra proporcionalmente pocos problemas nuevos y aumenta el coste considerablemente. Esto se debe a que diferentes evaluadores tienden a encontrar diferentes tipos de problemas, y tras 5 evaluadores, la mayoría de los problemas significativos ya han sido identificados.

La **escala de severidad** permite priorizar los hallazgos para que el equipo de desarrollo sepa qué corregir primero. La escala propuesta por Nielsen tiene **5 niveles**:

| Nivel | Denominación | Criterio |
|-------|--------------|----------|
| **0** | No es un problema de usabilidad | falso positivo; no necesita acción |
| **1** | Problema cosmético | solo necesita arreglarse si hay tiempo extra; no afecta significativamente a la experiencia |
| **2** | Problema menor | baja prioridad; debería arreglarse pero no es urgente |
| **3** | Problema mayor | alta prioridad; importante arreglarlo; causa dificultades significativas a muchos usuarios |
| **4** | Problema catastrófico | imperativo arreglarlo **antes del lanzamiento**; impide a los usuarios completar tareas esenciales |

La severidad se determina combinando **tres factores**:

- La **frecuencia** con la que ocurre el problema.
- El **impacto** que tiene en el usuario cuando ocurre.
- La **persistencia** del problema (¿es algo que el usuario puede superar una vez que lo conoce, o le afectará cada vez?).

### 4. Test de usuarios: la evidencia empírica

El test de usuarios es la técnica de evaluación **más convincente y reveladora** porque permite observar directamente cómo personas reales interactúan con el producto. Mientras que la evaluación heurística nos dice **qué principios se violan**, el test de usuarios nos muestra **qué sucede realmente**: dónde se atascan los usuarios, qué malinterpretan, qué atajos descubren, y qué emociones experimentan durante el proceso.

!!! tip "Técnica think aloud"
    La técnica del ***think aloud*** (pensar en voz alta) es la práctica estándar en tests de usabilidad moderados. Consiste en pedir al participante que **verbalice continuamente** sus pensamientos, expectativas, confusiones y decisiones mientras realiza las tareas. Desarrollada originalmente en psicología cognitiva, permite al moderador acceder al **modelo mental del usuario en tiempo real**.

    No es natural (la mayoría de las personas no verbalizan sus pensamientos al usar un ordenador), por lo que el moderador debe recordar periódicamente al participante que siga hablando si se queda en silencio. Frases típicas para reactivarlo:

    - «¿Qué estás mirando ahora?»
    - «¿Qué esperas que pase si haces clic ahí?»
    - «¿Hay algo que te llame la atención?»

!!! tip "Número de participantes"
    El **número de participantes** para tests **cualitativos** (donde el objetivo es encontrar problemas, no medirlos) fue establecido por la investigación de Nielsen en **5 usuarios**. Con 5 usuarios se descubren aproximadamente el **85%** de los problemas de usabilidad de una interfaz.

    Testear con más usuarios en un estudio cualitativo tiene **rendimiento decreciente**: es más eficiente realizar **múltiples iteraciones** de test con 5 usuarios cada una (testear, rediseñar, volver a testear) que un único test masivo.

    Sin embargo, para estudios **cuantitativos** (donde se quiere medir con precisión tiempos, tasas de éxito o comparar diseños), se necesitan muestras más grandes, típicamente entre **20 y 40 participantes**, para alcanzar significancia estadística.

### 5. Métricas de usabilidad

**SUS (System Usability Scale):** Desarrollado por **John Brooke** en **1986**, es el cuestionario de usabilidad más utilizado en el mundo, con miles de estudios que lo referencian. Consta de **10 preguntas** con escala *Likert* de **1 a 5**. Su gran ventaja es que proporciona una puntuación única de **0 a 100** que resume la usabilidad percibida, permitiendo comparar cualquier sistema con cualquier otro.

| Puntuación SUS | Interpretación |
|----------------|----------------|
| **≈ 68** | media histórica a lo largo de décadas de estudios |
| **> 80** | excelentes (percentil **A**) |
| **< 50** | inaceptables |

El SUS **no mide dimensiones separadas** (no da una puntuación de "facilidad de aprendizaje" frente a "eficiencia"), sino que proporciona una medida **unidimensional** de usabilidad percibida que ha demostrado ser robusta y fiable.

**SEQ (Single Ease Question):** Es la métrica de satisfacción **más simple posible**: una única pregunta tras cada tarea —«En general, ¿cómo de fácil o difícil fue completar esta tarea?»— en una escala de **1 (muy difícil)** a **7 (muy fácil)**. Su simplicidad es su fortaleza: rápida de administrar, sensible a diferencias entre tareas, y mínimamente intrusiva.

**NPS (Net Promoter Score):** Mide la **lealtad del cliente** y su disposición a recomendar el producto. Una única pregunta —«¿Qué probabilidad hay de que recomiendes este producto a un amigo o colega?»— en escala de **0 a 10**. Los que responden **9-10** son «promotores», **7-8** «neutrales», **0-6** «detractores».

> **NPS = % promotores − % detractores**

### 6. Eye Tracking, Heat Maps y Analítica Web

El **eye tracking** registra los movimientos oculares mediante hardware especializado (cámaras infrarrojas de alta frecuencia, **60-1200 Hz**) para determinar exactamente hacia dónde mira el usuario en cada momento:

- **Mapas de calor de mirada** — visualizan las zonas más miradas (**rojo** = mucho, **azul** = poco).
- **Gaze plots** — muestran la secuencia de **fijaciones** (círculos numerados) conectadas por líneas (**sacadas**).

El eye tracking es muy valioso para estudios académicos y de investigación fundamental (dónde mira la gente en una página de resultados de Google, cómo escanea una *landing page*), pero tiene limitaciones prácticas: **alto coste** del hardware, necesidad de **calibración individual**, entorno de **laboratorio artificial**, y el hecho de que «mirar» no equivale a «ver» o «comprender».

!!! warning "Mirar no equivale a ver"
    Mirar fijamente un elemento **no significa** que el usuario lo haya procesado cognitivamente.

Los **heat maps de comportamiento** (Hotjar, Clarity) registran datos **pasivos** de usuarios reales en su entorno natural:

- **Click maps** — muestran dónde hacen clic los usuarios, revelando elementos que los usuarios **creen** que son *clickables* (aunque no lo sean), y qué elementos importantes están recibiendo **pocos clics**.
- **Scroll maps** — particulamente útiles para páginas de contenido largo: muestran que la mayoría de los usuarios abandonan antes de llegar al **50%** de la página, lo que implica que el contenido más importante debe estar **«above the fold»**.
- **Move maps** — registran la trayectoria del cursor, que correlaciona aproximadamente con la mirada.

!!! tip "Rigor en el A/B testing"
    El **A/B testing** es un experimento controlado donde se divide **aleatoriamente** el tráfico entre dos o más versiones de una página para medir cuál funciona mejor en una **métrica predefinida**. Es especialmente poderoso en comercio electrónico y marketing digital para optimizar conversiones.

    - La **significancia estadística** (**p < 0,05**) debe alcanzarse antes de declarar un ganador.
    - El test debe ejecutarse durante **ciclos completos de negocio** (mínimo **una semana**, idealmente **dos**) para evitar sesgos estacionales o de día de la semana.

## Ejemplos guiados

### Ejemplo Guiado 1: Evaluación Heurística de un Checkout

A continuación analizamos el proceso de checkout de una tienda online aplicando las 10 heurísticas de Nielsen.

**Checkout analizado:** 4 pasos (identificación, dirección, envío, pago).

**Hallazgos principales:**

1. **H1 - Visibilidad del estado:** El checkout no muestra el número de paso actual. El usuario no sabe si está en el paso 2 de 4 o en el 3 de 7. Solución: añadir barra de progreso: "Paso 2 de 4: Dirección de envío". Severidad: 3.

2. **H3 - Control y libertad:** No hay botón "Volver" entre pasos del checkout. Si el usuario se equivoca en la dirección, no puede volver a corregirla sin usar el botón Atrás del navegador (que puede perder datos). Solución: añadir botones de navegación visible entre pasos. Severidad: 4.

3. **H5 - Prevención de errores:** El campo de código postal acepta cualquier texto sin validar formato. El usuario puede escribir letras donde deberían ir números. Solución: aplicar máscara de entrada o validación en tiempo real. Severidad: 3.

4. **H6 - Reconocimiento vs recuerdo:** Los métodos de envío se muestran con nombres técnicos ("Envío estándar 48h", "Envío urgente 24h", "Punto de recogida SEUR") sin explicar qué significa cada uno. Solución: añadir descripciones breves con precio y plazo. Severidad: 2.

### Ejemplo Guiado 2: Diseño de un Test de Usuario para App de Banca Móvil

**Objetivo:** Evaluar si los usuarios pueden realizar transferencias bancarias desde la app móvil sin errores y en un tiempo razonable.

**Participantes:** 5 clientes del banco, 2 con baja experiencia tecnológica (mayores de 55), 3 con experiencia media. Reclutados mediante agencia de estudios de mercado. Incentivo: 50€.

**Tareas del test:**

1. Inicia sesión en la app con las credenciales proporcionadas. (Tarea de calentamiento)
2. Revisa el saldo de tu cuenta principal y dinos cuál es.
3. Realiza una transferencia de 150€ a la cuenta ES12 3456 7890 1234 5678 9012.
4. Programa una transferencia periódica de 50€ para el día 1 de cada mes.
5. Encuentra y activa la opción de notificaciones push para movimientos superiores a 500€.

**Métricas a medir:** Tasa de éxito por tarea, tiempo por tarea, número de errores, puntuación SEQ tras cada tarea, puntuación SUS al final.

### Ejemplo Guiado 3: Análisis de Scroll Map

Analizamos un scroll map de una página de producto:

```
|=====================| 100%  Hero: imagen + nombre + precio + CTA
|=====================|  98%  Valoraciones en estrellas
|==================== |  85%  Descripción corta
|================     |  62%  Características técnicas
|=========            |  41%  Opiniones de clientes
|======               |  28%  Productos relacionados
|===                  |  12%  Preguntas frecuentes
```

**Análisis:** Las opiniones de clientes (41% de visibilidad) y los productos relacionados (28%) están en una posición demasiado baja. Dado que las opiniones son un factor decisivo de compra, deberían estar más arriba. La sección de características técnicas retiene bien (62%), lo que indica que los usuarios la valoran pero quizás es demasiado extensa. Recomendación: mover la sección de opiniones justo después de la descripción, y resumir las características técnicas en bullets con opción de "Ver especificaciones completas".

### Ejemplo Guiado 4: Cálculo e Interpretación del SUS

5 usuarios evalúan una intranet corporativa. Sus respuestas:

| Preg | U1 | U2 | U3 | U4 | U5 |
|------|----|----|----|----|----|
| 1 (impar) | 3 | 4 | 2 | 3 | 4 |
| 2 (par)   | 2 | 1 | 3 | 2 | 1 |
| 3 (impar) | 4 | 3 | 3 | 4 | 3 |
| 4 (par)   | 1 | 2 | 2 | 1 | 2 |
| 5 (impar) | 3 | 3 | 2 | 3 | 4 |
| 6 (par)   | 2 | 1 | 3 | 2 | 1 |
| 7 (impar) | 4 | 4 | 3 | 4 | 4 |
| 8 (par)   | 1 | 1 | 2 | 1 | 2 |
| 9 (impar) | 3 | 3 | 2 | 3 | 3 |
| 10 (par)  | 2 | 1 | 3 | 2 | 1 |

**Cálculo:** Para impares: valor-1. Para pares: 5-valor. Suma × 2.5.

- U1: (3-1)+(5-2)+(4-1)+(5-1)+(3-1)+(5-2)+(4-1)+(5-1)+(3-1)+(5-2) = 2+3+3+4+2+3+3+4+2+3 = 29. SUS = 29*2.5 = 72.5
- U2: 3+4+2+3+2+4+3+4+2+4 = 31. SUS = 77.5
- U3: 1+2+2+3+1+2+2+3+1+2 = 19. SUS = 47.5
- U4: 2+3+3+4+2+3+3+4+2+3 = 29. SUS = 72.5
- U5: 3+4+2+3+3+4+3+3+2+4 = 31. SUS = 77.5

**SUS medio:** (72.5+77.5+47.5+72.5+77.5)/5 = 69.5

**Interpretación:** La puntuación media de 69.5 está ligeramente por encima de la media histórica de 68. Es un resultado aceptable pero no excelente. El usuario 3 encuentra el sistema claramente peor que los demás (47.5, por debajo de 50), lo que merece investigación: ¿qué perfil tiene? ¿qué tareas le resultaron frustrantes?


## Casos reales

### Caso Real 1: Análisis de Usabilidad de Amazon

Amazon es citado frecuentemente como referente de usabilidad en ecommerce, pero no es perfecto. Analicemos algunas decisiones de diseño:

**Acierto - One-Click Purchase:** La compra en un clic es un ejemplo magistral de la heurística 7 (Flexibilidad y eficiencia). Para usuarios recurrentes que ya tienen configurados sus datos de envío y pago, elimina todo el proceso de checkout. El usuario ve "Comprar ahora con 1-Clic" y, literalmente, con un clic ha comprado. Esto reduce la fricción al mínimo absoluto y es una ventaja competitiva tan importante que Amazon patentó el concepto durante años.

**Problema - Sobrecarga informativa en página de producto:** Las fichas de producto de Amazon acumulan una cantidad abrumadora de información: galería de imágenes, variantes (color, talla), precio, opciones de envío, "Comprados juntos habitualmente", "Quién compró esto también compró...", fichas técnicas, opiniones, preguntas, productos patrocinados... Viola la heurística 8 (Diseño minimalista). Amazon apuesta por saturar de opciones porque su algoritmo de recomendación y venta cruzada genera un porcentaje muy significativo de sus ingresos, pero desde el punto de vista de la usabilidad pura, es abrumador.

**Problema - Devoluciones y servicio al cliente ocultos:** Encontrar cómo devolver un producto o contactar con atención al cliente requiere navegar por múltiples niveles de menús, páginas de ayuda y preguntas frecuentes. Amazon prioriza que compres y no te vayas, no que resuelvas problemas. Esto es una violación deliberada de la heurística 6 (Reconocimiento antes que recuerdo) y la 3 (Control y libertad) por razones de negocio: hacen que devolver sea inconvenientemente difícil para reducir devoluciones.

### Caso Real 2: Análisis de Usabilidad de Renfe.com

La web de Renfe es un caso de estudio recurrente (y no precisamente por sus virtudes) en el ámbito de la usabilidad en España:

**Problema crítico - El buscador de trenes:** Durante años, el buscador de trenes de Renfe requería seleccionar estación de origen y destino de listas desplegables enormes sin búsqueda por texto, y no permitía escribir directamente el nombre de la estación. Esto violaba flagrantemente la heurística 7 (Flexibilidad y eficiencia) y la 6 (Reconocimiento). Un usuario que sabe que quiere viajar de "Madrid" a "Barcelona" se veía forzado a buscar en listas de cientos de estaciones, incluyendo apeaderos diminutos. Afortunadamente, esto ha mejorado en versiones recientes.

**Problema - Proceso de pago confuso:** El proceso de compra introduce múltiples pasos con opciones confusas (tarifas con nombres como "Promo", "Promo+", "Flexible", "Mesa" que no son autoexplicativas), selección de asiento en un mapa interactivo poco usable, y múltiples pantallas de confirmación. Un benchmark comparando el tiempo necesario para comprar un billete en Renfe vs Trainline muestra diferencias de 3-5 minutos a favor de la competencia.

**Acierto - Mejora continua:** Es justo reconocer que Renfe ha invertido significativamente en mejorar la usabilidad de su plataforma digital en los últimos años. La introducción de búsqueda con autocompletado, la simplificación del proceso de pago, y la app móvil (aunque mejorable) muestran una trayectoria positiva.

### Caso Real 3: Análisis de Portal de Empleo Público

Los portales de empleo público (como la plataforma de oposiciones de muchas comunidades autónomas) presentan problemas de usabilidad sistémicos:

**Problema - Lenguaje administrativo:** Utilizan terminología jurídico-administrativa que el ciudadano medio no entiende: "subsanación de solicitudes", "baremación de méritos", "lista provisional de personas aspirantes admitidas y excluidas". Viola la heurística 2 (Lenguaje del mundo real). Un ciudadano quiere saber simplemente "¿Me han admitido a la oposición?" o "¿Cuándo es el examen?".

**Problema - Arquitectura de información:** La información está dispersa en múltiples boletines, sedes electrónicas y portales con estructuras diferentes. Un opositor necesita consultar 3 o 4 sitios web diferentes para seguir un único proceso. Viola las heurísticas 6 (Reconocimiento) y 8 (Minimalismo). Solución: unificar en un único portal personalizado donde cada opositor vea solo sus procesos, sus plazos y sus estados.

**Problema - PDFs no accesibles:** Gran parte de la información se publica en PDFs escaneados, no en HTML. Esto es un problema de usabilidad (no se puede buscar texto, no se adapta a móvil) y de accesibilidad (los lectores de pantalla no pueden leer imágenes escaneadas).


## Actividades guiadas

### Actividad Guiada 1: Evaluación Heurística de un Sitio Web Real

**Objetivo:** Realizar una evaluación heurística completa de un sitio web elegido por el alumno, aplicando las 10 heurísticas de Nielsen, asignando severidad a cada hallazgo y elaborando un informe profesional.

**Material:** Plantilla de evaluación heurística, capturador de pantalla, editor de textos.

**Duración:** 90 minutos.

### Actividad Guiada 2: Diseño y Ejecución de un Mini Test de Usuario

**Objetivo:** Diseñar el guion de un test de usuario, reclutar a 3 compañeros como participantes, ejecutar el test (grabando la pantalla) y analizar los resultados.

**Duración:** 120 minutos.

### Actividad Guiada 3: Cálculo e Interpretación de Métricas SUS

**Objetivo:** Administrar el cuestionario SUS a 5 usuarios de un sitio web, calcular las puntuaciones individuales y la media, e interpretar los resultados contrastándolos con los benchmarks de la industria.

### Actividad Guiada 4: Análisis de Heat Maps con Datos Reales de Hotjar

**Objetivo:** Utilizar datos de heat maps proporcionados por el profesor para identificar problemas de usabilidad en una página web y proponer soluciones de rediseño.

### Actividad Guiada 5: Diseño de un Test A/B

**Objetivo:** Diseñar un experimento A/B completo: formular hipótesis, definir variantes, calcular tamaño de muestra necesario, y especificar el plan de análisis estadístico.


## Actividades propuestas

### Actividad Propuesta 1: Evaluación Heurística Comparativa

Realiza una evaluación heurística de dos sitios web competidores del mismo sector (por ejemplo, dos aerolíneas, dos supermercados online, dos plataformas de streaming). Compara los resultados identificando fortalezas y debilidades de cada uno. Elabora un informe con tabla comparativa y recomendaciones para cada competidor.

**Criterios de evaluación:** Aplicación correcta de las 10 heurísticas (3 puntos), severidad justificada (2 puntos), calidad del análisis comparativo (3 puntos), formato profesional del informe (2 puntos).

### Actividad Propuesta 2: Test de Usuario Completo Documentado

Planifica, ejecuta y documenta un test de usuario con 5 participantes para una tarea concreta (por ejemplo, "comprar un billete de avión", "reservar una cita médica online"). Incluye: guion de test, fichas de consentimiento informado, transcripción de hallazgos, métricas calculadas (tasa de éxito, tiempos, errores), cuestionario SUS, y recomendaciones priorizadas de mejora.

**Criterios de evaluación:** Calidad del guion y las tareas (2 puntos), ejecución profesional y grabación (2 puntos), análisis de resultados y métricas (3 puntos), informe con recomendaciones accionables (3 puntos).

### Actividad Propuesta 3: Propuesta de Rediseño Basada en Analítica Web

Accede a los datos de Google Analytics de un sitio web (proporcionados por el profesor o de un proyecto personal). Identifica al menos 5 problemas de usabilidad inferidos de los datos (alta tasa de rebote en ciertas páginas, abandono en pasos del embudo de conversión, bajo tiempo en página). Propón soluciones de rediseño para cada problema y estima el impacto esperado.

### Actividad Propuesta 4: Análisis Heurístico de una Aplicación Móvil

Instala una aplicación móvil de banca, transporte público o administración. Realiza una evaluación heurística adaptada a móvil (existen conjuntos de heurísticas específicas para dispositivos táctiles, como las de Inostroza o las de Joyce). Identifica problemas relacionados con el tamaño de los targets táctiles, la navegación por gestos, y la legibilidad en pantallas pequeñas.

### Actividad Propuesta 5: Creación de un Panel de Métricas de Usabilidad

Diseña un dashboard (en Excel, Google Sheets o herramienta BI) que consolide y visualice las métricas de usabilidad de un producto digital. Debe incluir: evolución temporal del SUS, tasas de éxito por tarea en los últimos tests, comparativa con benchmarks, y funnel de conversión con tasas de abandono por paso. Explica cómo usarías este panel para tomar decisiones de diseño.


## Actividades de ampliación

### Actividad de Ampliación 1: Investigación sobre ROI de Usabilidad

Investiga y documenta al menos 10 casos reales documentados donde la inversión en usabilidad produjo un retorno medible. Busca en fuentes como Nielsen Norman Group, MeasuringU, estudios de caso de empresas como Amazon, IBM, Apple, o casos publicados en conferencias como UXPA. Elabora un informe que incluya: empresa, sector, inversión realizada, mejora implementada, resultado medible (en % de conversión, reducción de costes, aumento de ingresos), y fuente de la información.

**Criterios de evaluación:** Variedad de casos y sectores (3 puntos), rigor en la documentación de fuentes (3 puntos), análisis del ROI y lecciones aprendidas (4 puntos).

### Actividad de Ampliación 2: Implementación de un Proceso de UX Continua

Diseña un proceso completo de usabilidad y UX para integrar en un equipo de desarrollo ágil (Scrum). Define: ceremonias (cuándo se testea, cuándo se evalúa), roles (quién modera, quién observa, quién analiza), métricas (qué se mide y con qué frecuencia), herramientas (stack tecnológico para tests, analítica, heat maps), y entregables por sprint. El proceso debe ser realista para un equipo de 5-7 desarrolladores con 1 diseñador UX.

### Actividad de Ampliación 3: Benchmarking de Usabilidad Sectorial

Selecciona un sector (banca online, ecommerce de moda, reserva de viajes, administración electrónica) y realiza un estudio de benchmarking de usabilidad con al menos 5 competidores. Evalúa cada uno con: las 10 heurísticas de Nielsen, métricas de rendimiento (tiempo para tareas clave), un análisis SUS mediante 3 usuarios por sitio, y un heat map de scroll de las páginas principales. Elabora un informe de posicionamiento competitivo con rankings, fortalezas y debilidades, y recomendaciones para un hipotético nuevo entrante en el sector.


## Buenas prácticas

1. **Testea pronto y a menudo.** No esperes a tener el producto "terminado" para hacer tests de usuario. Testea wireframes en papel, prototipos de baja fidelidad, y versiones intermedias. Los problemas encontrados temprano son infinitamente más baratos de arreglar.

2. **No testes con familiares, amigos o compañeros de trabajo.** Su conocimiento previo del proyecto y su deseo de no herir sentimientos sesgan completamente los resultados. Recluta participantes que no tengan relación con el equipo.

3. **Mide antes y después.** Siempre establece una línea base (métricas del diseño actual) antes de implementar cambios. Sin línea base, no puedes demostrar que tu rediseño mejoró algo.

4. **Triangula métodos.** No confíes en un solo método de evaluación. Combina evaluación heurística (rápida y barata), tests de usuario (evidencia directa) y analítica web (datos a gran escala) para obtener una imagen completa.

5. **No hagas preguntas que sugieran la respuesta.** En un test de usuario, nunca digas "¿No crees que sería mejor si el botón estuviera aquí?". Pregunta en su lugar: "¿Hay algo que te llame la atención en esta pantalla?".

6. **Prioriza los hallazgos.** No todos los problemas de usabilidad son igual de graves. Usa la combinación de frecuencia × impacto × persistencia para priorizar y enfoca los recursos limitados en los problemas catastróficos y mayores.

7. **Graba las sesiones (con consentimiento).** Las grabaciones de tests de usuario son evidencia convincente para stakeholders escépticos. Un vídeo de 30 segundos de un usuario frustrado vale más que 30 páginas de informe.

8. **Itera.** Un solo test no resuelve todos los problemas. El mantra de la usabilidad es "diseñar, testear, rediseñar, volver a testear". La mejora es iterativa e incremental.

## Errores frecuentes

### Error 1: Testear con el número equivocado de participantes

Testear con 1 o 2 usuarios y pensar que es suficiente, o testear con 30 usuarios en un estudio cualitativo derrochando recursos. **Solución:** 5 usuarios para tests cualitativos, 20-40 para cuantitativos.

### Error 2: Creer que el diseñador puede evaluar su propio diseño

El sesgo del creador es inevitable. El diseñador sabe cómo se supone que debe funcionar y no puede experimentar la confusión de un usuario novel. **Solución:** Siempre usa evaluadores o usuarios externos.

### Error 3: Usar métricas sin contexto

Decir "el tiempo medio de tarea fue de 120 segundos" sin compararlo con una línea base, un benchmark de la competencia o el tiempo mínimo teórico. **Solución:** Siempre contextualiza las métricas.

### Error 4: Detener un test A/B antes de tiempo

Ver resultados provisionales prometedores y detener el test para implementar la variante ganadora, sin alcanzar el tamaño de muestra necesario. Esto produce falsos positivos. **Solución:** Precalcula el tamaño de muestra necesario y no mires los resultados hasta alcanzarlo.

### Error 5: Ayudar al participante durante el test

Cuando un participante se atasca, el moderador novato tiende a dar pistas o ayudar. Esto invalida el test porque no vemos lo que el usuario habría hecho por sí mismo. **Solución:** Resiste la tentación de ayudar. Si el usuario está completamente bloqueado, pregúntale qué haría en una situación real, pero no le des la solución.

### Error 6: Usar jerga técnica con los participantes

Decir "Haz clic en el CTA del hero" en lugar de "Busca un botón para empezar". **Solución:** Usa el lenguaje del usuario, no el del diseñador o desarrollador.

### Error 7: Interpretar los mapas de calor sin contexto cualitativo

Ver que una zona es roja (muy mirada o muy cliqueada) y asumir que es buena, cuando podría indicar confusión (los usuarios hacen clic repetidamente en algo que no es un botón). **Solución:** Los heat maps generan hipótesis, no conclusiones. Valídalas con tests cualitativos.

### Error 8: Calcular la media cuando los datos tienen valores atípicos extremos

Si un participante tardó 50 segundos y otro 500 segundos, la media (275 s) no representa a ninguno de los dos. **Solución:** Usa la mediana o la media geométrica para tiempos de tarea, que son menos sensibles a valores atípicos.


## Resumen

La usabilidad es una disciplina central en el desarrollo de productos digitales que va mucho más allá del "sentido común" o la "intuición del diseñador". Se fundamenta en principios de psicología cognitiva, en metodologías de investigación empírica y en métricas rigurosas que permiten evaluar y mejorar objetivamente las interfaces.

Las 10 heurísticas de Nielsen constituyen la herramienta de inspección más utilizada y accesible, proporcionando un marco sistemático para identificar problemas sin necesidad de usuarios reales. La evaluación heurística, realizada por 3-5 evaluadores independientes, detecta la mayoría de problemas significativos en días, no en semanas, y con costes mínimos.

El test de usuarios sigue siendo el patrón oro de la evaluación de usabilidad: observar a personas reales intentando completar tareas reales proporciona evidencia que ninguna inspección puede sustituir. La combinación de métodos cualitativos (observación, think aloud) y cuantitativos (tiempos, tasas de éxito, errores) ofrece una imagen completa de la experiencia del usuario.

Las métricas estandarizadas (SUS, SEQ, NPS) permiten cuantificar la usabilidad percibida y comparar objetivamente diferentes diseños, versiones y productos. Los heat maps y la analítica web aportan datos de comportamiento a gran escala que complementan los hallazgos cualitativos de tests y evaluaciones.

La práctica de la usabilidad es inherentemente iterativa: diseñar, prototipar, evaluar, aprender, rediseñar. Cada ciclo produce un producto más cercano a las necesidades y capacidades reales de sus usuarios.

## Recursos complementarios

### Libros
- **"Don't Make Me Think" de Steve Krug** (New Riders). El libro de usabilidad más accesible y práctico. Lectura obligatoria para cualquier persona que diseñe o desarrolle interfaces.
- **"Rocket Surgery Made Easy" de Steve Krug** (New Riders). Guía práctica para realizar tests de usabilidad con pocos recursos.
- **"Usability Engineering" de Jakob Nielsen** (Morgan Kaufmann). El texto académico fundacional de la ingeniería de usabilidad.
- **"Measuring the User Experience" de Tom Tullis y Bill Albert** (Morgan Kaufmann). La referencia definitiva sobre métricas de usabilidad y UX.
- **"Quantifying the User Experience" de Jeff Sauro y James R. Lewis** (Morgan Kaufmann). Estadística aplicada a UX.

### Herramientas
- **Hotjar:** https://www.hotjar.com - Heat maps, grabaciones de sesión, encuestas.
- **Microsoft Clarity:** https://clarity.microsoft.com - Heat maps gratuitos ilimitados.
- **Maze:** https://maze.co - Tests de usuario no moderados.
- **UserTesting:** https://www.usertesting.com - Plataforma de tests de usuario remotos.
- **Optimal Workshop:** https://www.optimalworkshop.com - Card sorting, tree testing, first click testing.
- **MeasuringU:** https://measuringu.com - Calculadoras de tamaño muestral, benchmarks SUS.

### Referencias online
- **Nielsen Norman Group:** https://www.nngroup.com - Artículos, investigaciones y formación de referencia en usabilidad.
- **UX Collective:** https://uxdesign.cc - Publicación en Medium con artículos de calidad sobre UX y usabilidad.
- **Laws of UX:** https://lawsofux.com - Colección visual de principios psicológicos aplicados al diseño de interfaces.
