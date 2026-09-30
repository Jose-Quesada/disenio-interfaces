---
icon: lucide/folder-tree
---

# Unidad 6: Arquitectura de la Información para Interfaces Web

## Objetivos de aprendizaje

Al finalizar esta unidad, el alumnado será capaz de diseñar la estructura informativa de sitios web y aplicaciones aplicando los principios, métodos y técnicas de la Arquitectura de la Información (AI). El estudiante aprenderá a organizar, etiquetar y estructurar los contenidos de una interfaz de forma que los usuarios puedan encontrar lo que buscan y comprender lo que encuentran con el mínimo esfuerzo cognitivo. Se persigue que el alumno domine las herramientas fundamentales de la AI: sea capaz de elaborar un sitemap completo que represente la estructura jerárquica de un sitio web, crear wireframes de diferentes niveles de fidelidad para comunicar la disposición espacial de los contenidos, diseñar user flows que modelen los recorridos de los usuarios a través de la interfaz, y construir mapas de navegación que visualicen las relaciones entre las diferentes secciones. Un objetivo transversal es que el estudiante comprenda la relación íntima entre la arquitectura de la información, la usabilidad y la experiencia de usuario, y sea capaz de justificar sus decisiones de diseño informativo con criterios objetivos basados en las necesidades de los usuarios y los objetivos del negocio.

## Relación con los Resultados de Aprendizaje

Esta unidad se vincula de manera directa y fundamental con los Resultados de Aprendizaje oficiales del módulo 0615 *Diseño de interfaces web* (RD 405/2023, BOE; currículo andaluz):

- **RA1. Planifica la creación de una interfaz web valorando y aplicando especificaciones de diseño.** La Arquitectura de la Información constituye precisamente la fase de planificación y estructuración previa a cualquier diseño visual o implementación técnica. Los sitemaps, wireframes y user flows que el alumno aprenderá a crear son los entregables fundamentales de esta fase de planificación (CE 1.c), y los diagramas y esquemas (sitemaps, flujos, mapas de navegación) constituyen la documentación estructural del proyecto.
- **RA2. Crea interfaces web homogéneos definiendo y aplicando estilos.** La estructura informativa debe ser coherente con el lenguaje visual definido en la guía de estilo; una AI consistente refuerza la homogeneidad percibida de la interfaz (CE 2.g).
- **RA5. Desarrolla interfaces web accesibles, analizando las pautas establecidas y aplicando técnicas de verificación.** Una arquitectura de la información bien diseñada es la base sobre la que se construye una experiencia accesible: navegación predecible, etiquetado claro y estructura lógica (CE 5.b).
- **RA6. Desarrolla interfaces web amigables analizando y aplicando las pautas de usabilidad establecidas.** La AI es el fundamento teórico de la usabilidad: facilita una navegación fácilmente recordada frente a redescubierta y adapta la estructura al objetivo y a los usuarios (CE 6.c).

## Conocimientos previos

Para el correcto aprovechamiento de esta unidad, el alumnado debe poseer conocimientos fundamentales sobre la web como medio de comunicación e interacción. Es necesario que el estudiante comprenda la diferencia entre un sitio web estático (orientado a la consulta de información) y una aplicación web dinámica (orientada a la realización de tareas), ya que la arquitectura de la información debe adaptarse a cada tipología. Se requieren nociones básicas de usabilidad y experiencia de usuario, incluyendo conceptos como affordance, feedback, carga cognitiva y modelos mentales, que serán constantemente referenciados al explicar el porqué de las decisiones de AI. El alumno debe estar familiarizado con la estructura básica de diferentes tipos de sitios web (ecommerce, corporativo, portal de noticias, aplicación SaaS, red social) para poder analizar críticamente sus arquitecturas de información. Es recomendable, aunque no imprescindible, que el estudiante haya navegado y utilizado herramientas de diagramación como Miro, Lucidchart o Draw.io, ya que muchas de las actividades prácticas requerirán la creación de diagramas. No se requieren conocimientos de programación para esta unidad, pero sí una mentalidad analítica y capacidad de abstracción para modelar estructuras de información complejas.

## Contenidos

1. Fundamentos de la Arquitectura de la Información: definición, orígenes históricos (Richard Saul Wurman), el modelo de las tres preguntas (¿dónde estoy?, ¿qué hay aquí?, ¿a dónde puedo ir?), relación con la UX y la usabilidad.
2. Componentes de la AI: sistemas de organización, sistemas de etiquetado, sistemas de navegación y sistemas de búsqueda. El modelo de los cuatro pilares de Rosenfeld y Morville.
3. Wireframes: definición y propósito, niveles de fidelidad (baja, media, alta), elementos que incluyen y elementos que excluyen, herramientas de wireframing, proceso de creación iterativo, wireframing responsive para múltiples breakpoints.
4. User Flows: definición, elementos constitutivos (pantallas, decisiones, acciones, conectores), tipos de flujos (task flow, wire flow, screen flow), notación y simbología, herramientas de diagramación, relación con los casos de uso y las historias de usuario.
5. Sitemap: definición, tipos de estructuras (jerárquica, lineal, radial, matricial), niveles de profundidad y amplitud, reglas de construcción (la regla de los 7±2, la regla de los 3 clics), herramientas de creación, diferencias entre sitemap visual y XML sitemap.
6. Mapa de navegación: diferencias conceptuales con el sitemap, representación de sistemas de navegación (global, local, contextual, breadcrumb, faceted, footer), patrones de navegación responsive.
7. Esquemas de organización de contenidos: organización alfabética, cronológica, geográfica, por tópico, por audiencia, por tarea. Criterios para seleccionar el esquema adecuado.
8. Estructuras de organización: modelo jerárquico (árbol), modelo secuencial (paso a paso), modelo matricial (rejilla), modelo de hipertexto (red). Ventajas e inconvenientes de cada estructura.
9. Card Sorting: definición y propósito, tipos (abierto, cerrado, híbrido), preparación y ejecución de una sesión, herramientas digitales (OptimalSort, Miro, FigJam), análisis de resultados (matriz de similaridad, dendrograma).
10. Tree Testing: definición, diferencias con card sorting, metodología de prueba, herramientas (Treejack, UserZoom), interpretación de métricas (success rate, directness, time taken).
11. Principios de etiquetado: características de una buena etiqueta (claridad, consistencia, predictibilidad, brevedad), tipos de etiquetas (navegación, contenido, iconos, indexación), pruebas de etiquetado con usuarios.
12. Sistemas de navegación: menú de navegación global, menú local, navegación contextual, breadcrumbs, tags y etiquetas, navegación facetada, búsqueda predictiva y autocompletado, navegación por footer.
13. Patrones de navegación responsive: menú hamburguesa, mega menú adaptable, off-canvas navigation, tab bar para móvil, bottom navigation, gestos de navegación.
14. Ejemplos prácticos detallados de creación de sitemaps, wireframes y user flows para diferentes tipos de proyectos web.
15. Análisis de la arquitectura de información de sitios web reales de referencia.

## Desarrollo teórico

### Fundamentos de la Arquitectura de la Información

!!! info "Definición: Arquitectura de la Información"
    La **Arquitectura de la Información (AI)** es la disciplina encargada de **organizar, estructurar y etiquetar** los contenidos de un entorno digital de manera que los usuarios puedan encontrar información y completar tareas de forma efectiva.

El término fue acuñado por **Richard Saul Wurman** en **1975**:

!!! quote "Richard Saul Wurman, 1975"
    «El estudio de la organización de la información para permitir que otros la encuentren.»

Sin embargo, fue la publicación en **1998** del libro *Information Architecture for the World Wide Web* de **Louis Rosenfeld** y **Peter Morville** —conocido cariñosamente como «el libro del oso polar» por la ilustración de su portada— lo que estableció la AI como una disciplina fundamental del diseño web.

!!! tip "Las tres preguntas de la AI"
    La AI se articula en torno a un modelo mental simple que todo usuario experimenta al llegar a un sitio web por primera vez. El usuario se formula, generalmente de forma inconsciente, tres preguntas fundamentales:

    - **¿Dónde estoy?** — necesita comprender en qué parte del sitio se encuentra.
    - **¿Qué hay aquí?** — necesita entender qué contenido o funcionalidad ofrece la página actual.
    - **¿A dónde puedo ir desde aquí?** — necesita identificar las opciones de navegación disponibles.

    Una buena arquitectura de la información responde a estas tres preguntas de forma **inmediata e intuitiva**, sin que el usuario tenga que pensar activamente en ellas. Cuando no encuentran respuesta, el usuario experimenta desorientación, frustración y, en muchos casos, **abandona el sitio**.

La AI guarda una relación **simbiótica** con la Experiencia de Usuario (UX). Mientras que la UX abarca la totalidad de la experiencia del usuario (incluyendo aspectos emocionales, estéticos y de interacción), la AI se centra específicamente en la **dimensión estructural**: cómo se organiza, nombra y conecta la información.

**Analogía arquitectónica.** Si una interfaz web fuera un edificio:

- La **AI** serían los **planos de planta** (dónde está cada habitación, cómo se conectan los pasillos, dónde están las escaleras).
- El **diseño de interacción** sería la **fontanería y la electricidad** (cómo funcionan los grifos y los interruptores).
- El **diseño visual** sería la **decoración interior** (colores, muebles, iluminación).

Sin unos buenos planos, el edificio será inhabitable por muy bonita que sea la decoración o por muy moderna que sea la instalación eléctrica.

### Los cuatro componentes fundamentales de la AI

Rosenfeld y Morville identificaron **cuatro sistemas interconectados** que componen la arquitectura de la información de cualquier entorno digital. Estos cuatro pilares proporcionan un marco de análisis que permite evaluar y diseñar la AI de forma sistemática:

| Pilar | Qué define |
|-------|------------|
| **Sistema de organización** | cómo se categoriza y estructura la información; responde a la pregunta «¿cómo agrupamos los contenidos?» |
| **Sistema de etiquetado** | cómo se nombran los contenidos y las opciones de navegación |
| **Sistema de navegación** | cómo los usuarios se desplazan entre los diferentes contenidos |
| **Sistema de búsqueda** | cómo los usuarios localizan información mediante consultas textuales |

**Sistema de organización.** Es, probablemente, la decisión de AI con mayor impacto en la experiencia del usuario. La organización puede basarse en dos familias de esquemas:

| Tipo de esquema | Ejemplos | Cuándo se usa |
|-----------------|----------|---------------|
| **Exacto** | alfabético, cronológico, geográfico | cuando los usuarios conocen el **nombre** o la **fecha** de lo que buscan |
| **Subjetivo** | por tópico, por audiencia, por tarea | cuando **exploran sin un objetivo concreto** |

La estructura de organización puede ser:

- **Jerárquica** — árbol de categorías y subcategorías, la más común en la web.
- **Secuencial** — paso a paso, típica en procesos de *checkout* o configuración.
- **Matricial** — rejilla que permite cruzar dos dimensiones, como filtros en un ecommerce.
- **De hipertexto** — red de enlaces contextuales entre contenidos relacionados.

**Sistema de etiquetado.** Define cómo se nombran los contenidos y las opciones de navegación. Cada etiqueta es una **promesa**: el usuario hace clic en «Contacto» esperando encontrar información de contacto, no un formulario de suscripción a la *newsletter*. Las etiquetas deben ser:

- **Claras** — el usuario entiende su significado sin ambigüedad.
- **Consistentes** — la misma etiqueta siempre lleva al mismo tipo de contenido.
- **Predictibles** — el usuario puede anticipar qué encontrará.
- **Breves** — idealmente, una o dos palabras.

El etiquetado es especialmente crítico porque constituye la **interfaz lingüística** entre el modelo mental del diseñador y el modelo mental del usuario; un desajuste entre ambos resulta en etiquetas que el diseñador considera obvias pero que el usuario no comprende.

**Sistema de navegación.** Incluye:

- **Navegación global** — presente en todas las páginas; da acceso a las secciones principales.
- **Navegación local** — específica de una sección; muestra sus subpáginas.
- **Navegación contextual** — enlaces insertados en el contenido que relacionan la página actual con otras relevantes.
- **Breadcrumbs** — ruta de migas que muestra la posición jerárquica de la página actual.
- **Navegación facetada** — filtros que permiten refinar resultados combinando múltiples criterios.
- **Navegación de utilidad** — enlaces a páginas funcionales como *login*, carrito o ayuda, normalmente en el *footer* o la cabecera secundaria.

**Sistema de búsqueda.** Aunque no todas las interfaces lo requieren (sitios pequeños o aplicaciones muy guiadas pueden funcionar exclusivamente con navegación), cuando el volumen de contenido supera cierto umbral la búsqueda se convierte en una necesidad. Un buen sistema de búsqueda incluye:

- Un **motor de indexación** completo.
- Soporte para consultas con **errores tipográficos** (*fuzzy search*).
- **Búsqueda predictiva** con autocompletado.
- **Filtros post-búsqueda** (*faceted search*).
- **Ordenación** de resultados por relevancia y fecha.
- Una **página de resultados** bien diseñada que muestre la información suficiente para decidir qué resultado satisface la necesidad.

### Wireframes: el esqueleto de la interfaz

!!! info "Definición: wireframe"
    Un **wireframe** es una representación visual esquemática de una página o pantalla que muestra la **disposición espacial de los elementos de interfaz** (contenido, navegación, funcionalidades) **sin incluir el diseño visual final**. Si la interfaz fuera un cuerpo humano, el wireframe sería el **esqueleto**: define la estructura, las proporciones y las relaciones entre las partes, pero no muestra la piel, el color del pelo o la ropa. Esta abstracción es deliberada y valiosa, porque permite centrar la discusión en la **estructura y la funcionalidad** sin que los aspectos estéticos (colores, tipografías definitivas, imágenes finales) desvíen la atención.

Los wireframes se clasifican según su **nivel de fidelidad**:

| Nivel | Características | Uso principal |
|-------|-----------------|---------------|
| **Baja fidelidad (low-fi)** | esquemas muy básicos, a menudo dibujados a mano sobre papel o pizarra; rectángulos, líneas y texto *placeholder* | primeras fases de exploración y *brainstorming*: se crean, descartan y modifican en **minutos** |
| **Media fidelidad (mid-fi)** | herramientas digitales (Figma, Balsamiq, Sketch), escalas de grises, tipografías genéricas, proporciones y espaciados precisos | formato estándar para comunicar con *stakeholders* y pruebas tempranas de usabilidad |
| **Alta fidelidad (high-fi)** | contenidos reales, imágenes *placeholder* realistas y simulación precisa del *layout* final | difumina la frontera con los **mockups** visuales |

!!! tip "Qué incluye y qué excluye un wireframe"
    Un wireframe efectivo incluye, como mínimo:

    - La **estructura de la página** (cabecera, contenido principal, barra lateral, *footer*).
    - Los **bloques de contenido** con su jerarquía visual indicada (el tamaño relativo de cada bloque sugiere su importancia).
    - Los **elementos de navegación** (menús, *breadcrumbs*, enlaces).
    - Los **elementos funcionales** (botones, formularios, campos de búsqueda).
    - **Anotaciones** que expliquen comportamientos interactivos o decisiones de diseño que no son evidentes en el dibujo estático.

    Por el contrario, un buen wireframe **excluye deliberadamente**: los colores definitivos (se utilizan escalas de grises), las imágenes finales (se usan rectángulos con una X o *placeholders*), las tipografías decorativas (se usan genéricas como Arial o Inter) y los detalles ornamentales.

El proceso de *wireframing* es **iterativo** por naturaleza:

1. Creación de múltiples alternativas de baja fidelidad para cada pantalla principal, explorando diferentes disposiciones de los mismos elementos.
2. Discusión de las alternativas con el equipo y, en proyectos con presupuesto para investigación, **pruebas con usuarios** mediante prototipos de papel.
3. A partir del *feedback*, selección y refinado de las opciones más prometedoras, aumentando progresivamente la fidelidad.

Cuando se trabaja con diseño responsive, es necesario crear wireframes para cada *breakpoint* principal (**móvil**, **tablet**, **escritorio**), mostrando cómo los bloques de contenido se reorganizan, se apilan o se ocultan en función del espacio disponible.

### User Flows: modelando los recorridos del usuario

!!! info "Definición: user flow"
    Un **User Flow** (flujo de usuario) es un diagrama que representa el **recorrido completo** que un usuario realiza a través de una interfaz para completar una tarea u objetivo específico. Si el sitemap es el mapa de carreteras (todas las rutas posibles), el user flow es la **ruta concreta** que sigue un conductor para ir desde su casa hasta el trabajo. Son herramientas fundamentales porque obligan al equipo de diseño a pensar en la experiencia como una **secuencia de pasos interconectados**, no como pantallas aisladas.

Los elementos que componen un user flow:

- **Pantallas o estados de la interfaz** — representados típicamente como rectángulos.
- **Acciones del usuario** — líneas o flechas etiquetadas con el verbo de la acción («hace clic en…», «rellena el formulario…», «desliza hacia la izquierda…»).
- **Puntos de decisión** — rombos, donde el flujo se bifurca según la elección del usuario o el resultado de una validación.
- **Conectores** — flechas que indican la dirección del flujo entre pantallas.

También pueden incluir **anotaciones sobre el estado del sistema** («email enviado», «error de conexión», «sesión expirada») que contextualizan cada paso.

Existen diferentes tipos de user flows según el nivel de abstracción y el propósito:

- **Task flow** — describe el proceso a alto nivel, centrándose en las acciones del usuario **sin especificar pantallas concretas**; es útil para comprender la lógica del proceso antes de diseñar la interfaz.
- **Wire flow** — superpone el flujo sobre versiones simplificadas (*wireframes* en miniatura) de las pantallas reales, combinando la representación del proceso con la representación visual de cada paso.
- **Screen flow** (*flowchart* de pantallas) — el más detallado; muestra **cada pantalla como un nodo** del diagrama con todas las posibles conexiones entre ellas; es particularmente útil para documentar la navegación completa de una aplicación.

La creación de user flows debe seguir este recorrido:

1. **Identificar los objetivos principales** del usuario, redactados como historias de usuario («Como cliente, quiero comprar un producto para recibirlo en mi domicilio»).
2. Enumerar los pasos necesarios y dibujar el **flujo ideal** (*happy path*): el recorrido sin errores ni excepciones.
3. Añadir los **flujos alternativos y de error** que contemplan lo que ocurre cuando algo no sale según lo esperado: ¿qué pasa si el producto está agotado, si la tarjeta de crédito es rechazada, si el usuario quiere modificar la dirección de envío a mitad del proceso?

Estos escenarios alternativos suelen representar la **mayor parte de la complejidad** de la interfaz y son los que diferencian un diseño robusto de uno frágil.

### Sitemaps: la representación de la estructura del sitio

!!! info "Definición: sitemap"
    Un **sitemap** es un diagrama que representa la **estructura jerárquica** de un sitio web o aplicación, mostrando todas las páginas o pantallas y las **relaciones de contención** entre ellas. Responde a la pregunta «¿qué páginas tiene este sitio y cómo se organizan?» y constituye el entregable fundamental para documentar la arquitectura de la información de un proyecto web.

El formato más común es el **sitemap jerárquico**, que representa la estructura como un árbol donde el nodo raíz es la página de inicio (**Home**) y cada nivel sucesivo representa un nivel de profundidad en la navegación. Las páginas se representan como cajas etiquetadas con su nombre, y las líneas que las conectan indican la relación de pertenencia (la página inferior está contenida dentro de la sección representada por la página superior).

El sitemap debe mostrar toda la estructura de navegación principal del sitio, pero **no necesariamente cada una de las páginas de detalle** (sería inviable representar las **50.000 páginas** de producto de un ecommerce); para contenidos masivos, se suele indicar una **página tipo** (*template*) y una anotación que explique que se genera dinámicamente para cada elemento.

Los principios de construcción de sitemaps están gobernados por dos reglas empíricas derivadas de la psicología cognitiva:

| Regla | Origen | Aplicación al diseño de navegación |
|-------|--------|------------------------------------|
| **Regla de los 7±2** | número mágico de **Miller**: las personas mantienen aproximadamente siete elementos (más o menos dos) en su memoria de trabajo | cada nivel de navegación no debe superar **7±2 opciones** |
| **Regla de los 3 clics** | heurística de profundidad | cualquier contenido debería ser accesible en un máximo de **3 clics** desde la página de inicio |

!!! note "La regla de los 3 clics es controvertida"
    La investigación posterior ha demostrado que los usuarios **no abandonan por número de clics sino por desorientación**; aun así, sigue siendo una buena heurística para evaluar si la estructura es excesivamente profunda.

Es importante distinguir entre el sitemap visual y el XML sitemap:

| | **Sitemap visual** | **XML sitemap** |
|---|--------------------|-----------------|
| **Naturaleza** | el diagrama que creamos como herramienta de diseño | un archivo en formato **XML** |
| **Destinatario** | **humanos** (equipo de diseño) | **motores de búsqueda** (crawlers) |
| **Propósito** | herramienta de diseño | facilitar la **indexación** del sitio |

Aunque comparten nombre y ambos representan la estructura del sitio, sus propósitos y formatos son completamente diferentes. En el contexto de esta unidad, trabajaremos **exclusivamente con sitemaps visuales**.

### Card Sorting: investigación de la organización de contenidos con usuarios

!!! info "Definición: Card Sorting"
    El **Card Sorting** es una técnica de investigación de UX que permite descubrir **cómo los usuarios agrupan y categorizan mentalmente** los contenidos de un sitio web. Consiste en entregar a los participantes un conjunto de tarjetas (físicas o digitales), cada una con el nombre de un contenido o funcionalidad del sitio, y pedirles que las agrupen en categorías que tengan sentido para ellos y que pongan un nombre a cada categoría. El resultado es un **mapa del modelo mental colectivo** de los usuarios, que puede compararse con la estructura propuesta por el equipo de diseño para identificar desajustes.

Existen tres variantes principales:

- **Card Sorting abierto** — los participantes crean libremente tanto los grupos como los nombres de las categorías, sin ninguna restricción previa. Ideal para las **fases iniciales** de un proyecto, cuando se quiere descubrir cómo los usuarios conceptualizan un dominio sin influirles con categorías predefinidas.
- **Card Sorting cerrado** — se proporcionan las categorías predefinidas y los participantes solo deben asignar cada tarjeta a una de ellas. Útil para **validar una estructura de categorías ya propuesta**.
- **Card Sorting híbrido** — se proporcionan algunas categorías predefinidas pero se permite a los participantes crear otras nuevas si lo consideran necesario.

La preparación de una sesión requiere seleccionar cuidadosamente los contenidos a incluir en las tarjetas: deben ser **representativos del contenido real** del sitio, cubrir todos los tipos de información y funcionalidades, y estar redactados de forma clara y concisa.

!!! tip "Cuántas tarjetas preparar"
    Se recomienda utilizar entre **30 y 60 tarjetas**: menos de **30** puede no proporcionar suficiente riqueza de datos, y más de **60** puede fatigar al participante.

Las sesiones pueden realizarse de forma **presencial** (con tarjetas físicas de papel, lo que permite observar el proceso y el razonamiento en voz alta) o de forma **remota** mediante herramientas digitales como **OptimalSort**, **Miro**, **FigJam** o **UserZoom**, que permiten reclutar más participantes y recopilar datos cuantitativos de forma eficiente.

El análisis de resultados se apoya en dos herramientas principales:

- **Matriz de similaridad** — muestra, para cada par de tarjetas, el porcentaje de participantes que las colocaron en el mismo grupo. Un valor alto (por ejemplo, el **90%** de los participantes agruparon «Facturación» con «Historial de pagos») indica un **consenso fuerte** sobre la pertenencia de esos contenidos a una misma categoría.
- **Dendrograma** — representación visual en forma de árbol que agrupa jerárquicamente las tarjetas según su similaridad, revelando la estructura de categorías que emerge naturalmente de los datos. Analizándolo, el equipo de diseño puede decidir **cuántas categorías principales crear** (cortando el árbol a diferentes alturas) y qué contenidos incluir en cada una.

### Tree Testing: validación de la estructura de navegación

!!! info "Definición: Tree Testing"
    El **Tree Testing** es la técnica complementaria al Card Sorting. Mientras que el Card Sorting pregunta «¿cómo agruparías estos contenidos?», el Tree Testing pregunta «**¿dónde buscarías este contenido?**» y mide la efectividad de una estructura de categorías **ya definida**. Se presenta al participante únicamente la estructura de categorías en forma de árbol de texto (sin diseño visual, sin navegación, sin pistas contextuales) y se le pide que indique en qué categoría esperaría encontrar un contenido específico.

La prueba es sorprendentemente reveladora porque **elimina todas las muletas visuales y de navegación** que en una interfaz real pueden ayudar al usuario a encontrar información incluso cuando la estructura subyacente es deficiente. Si un participante no puede localizar un contenido en el árbol de texto, probablemente tampoco podrá hacerlo en la interfaz real, aunque en esta última pueda llegar a él por casualidad o mediante búsqueda. El Tree Testing, por tanto, evalúa la **calidad intrínseca** de la arquitectura de la información, aislándola de otros factores.

Las métricas principales son:

- **Tasa de éxito** — porcentaje de tareas en las que el participante encontró el contenido en la categoría correcta.
- **Direccionalidad** — porcentaje de tareas en las que el participante fue **directamente** a la categoría correcta sin pasar por categorías incorrectas, lo que indica claridad de las etiquetas.
- **Tiempo empleado por tarea** — correlaciona con la facilidad de la decisión.

!!! warning "Tasa de éxito por debajo del 80%"
    Tasas de éxito **por debajo del 80%** indican **problemas serios** en la estructura de categorías que deben abordarse antes de implementar la navegación.

Las herramientas más utilizadas para Tree Testing son **Treejack** (de Optimal Workshop) y **UserZoom**.

### Sistemas de navegación: patrones y componentes

Los sistemas de navegación son los mecanismos que permiten al usuario desplazarse entre los diferentes contenidos de un sitio web:

- **Navegación global o principal** — el menú que aparece en todas las páginas (típicamente en la cabecera) y que da acceso a las secciones de primer nivel del sitio. Debe ser **visible, consistente y predecible**, y suele incluir entre **5 y 7 opciones**.
- **Navegación local** — aparece dentro de una sección y muestra las subpáginas de esa sección; se ubica habitualmente en una **barra lateral izquierda** o como un **submenú desplegable**.
- **Navegación contextual** — enlaces incrustados en el contenido que relacionan la página actual con otras relevantes, como «Artículos relacionados» al final de un *blog post*.

Los **breadcrumbs** o migas de pan muestran la ruta jerárquica desde la página de inicio hasta la página actual, permitiendo al usuario comprender dónde está y navegar hacia niveles superiores. Siguen el formato **Home > Categoría > Subcategoría > Página actual** y son especialmente útiles en sitios con estructuras profundas.

!!! warning "Ruta lógica, no historial"
    Las migas deben reflejar la ubicación jerárquica real (**la ruta lógica**), no el historial de navegación del usuario (**la ruta física**).

La **navegación facetada** es un patrón característico de los *ecommerce* y los buscadores que permite filtrar un conjunto de resultados aplicando simultáneamente múltiples criterios (*facetas*). Cada faceta representa una dimensión de filtrado (**precio, marca, talla, color, valoración**) y los valores de cada faceta se generan dinámicamente a partir de los resultados actuales. Es potente pero compleja de diseñar: debe ser evidente qué facetas están activas, permitir desactivar facetas individuales sin perder las demás, y gestionar el caso de que una combinación de facetas no produzca ningún resultado.

Para dispositivos móviles, el espacio limitado obliga a utilizar patrones específicos:

- **Menú hamburguesa** (tres líneas horizontales) — oculta la navegación detrás de un icono, liberando espacio para el contenido, pero **reduce la visibilidad** de las opciones de navegación.
- **Navegación por pestañas** (*tab bar*) — en la parte inferior de la pantalla, popularizada por iOS; ofrece acceso directo a **3-5 secciones** principales con un solo toque.
- **Navegación off-canvas** — desliza un panel lateral desde fuera de la pantalla, combinando la economía de espacio del menú hamburguesa con una experiencia de interacción más natural mediante gestos de *swipe*.

## Ejemplos guiados

### Ejemplo guiado 1: Creación de un sitemap para un ecommerce de ropa deportiva

En este ejemplo, crearemos el sitemap completo de una tienda online de ropa deportiva, utilizando notación estándar y aplicando los principios de jerarquía, equilibrio entre profundidad y amplitud, y etiquetado claro.

El sitemap se representa mediante un diagrama de árbol con cajas y líneas de conexión. La estructura se describe a continuación en formato textual preciso que puede trasladarse directamente a cualquier herramienta de diagramación.

La página de inicio (Home) ocupa el nivel 0 y constituye la raíz del árbol. Desde Home parten siete ramas principales que corresponden a las secciones de navegación global del sitio, representando el nivel 1:

```
Nivel 0:                        ┌─────────┐
                                │  HOME   │
                                └────┬────┘
                                     │
        ┌────────┬────────┬──────┬───┴───┬──────┬────────┐
        ▼        ▼        ▼      ▼       ▼      ▼        ▼
    ┌──────┐ ┌──────┐ ┌──────┐ ┌─────┐ ┌──────┐ ┌─────┐ ┌─────┐
    │Hombre│ │Mujer │ │ Niños│ │Equip│ │Outlet│ │Marc │ │Ayuda│
    └──┬───┘ └──┬───┘ └──┬───┘ │ os  │ └──┬───┘ │ as  │ │     │
       │        │        │     └──┬──┘    │     └──┬──┘ └──┬──┘
       │        │        │        │       │        │       │
```
Nivel 1: Hombre | Mujer | Niños | Equipos | Outlet | Marcas | Ayuda

Cada una de las secciones del nivel 1 se despliega en subcategorías de nivel 2. Desarrollamos la rama "Hombre" como ejemplo representativo:

```
┌──────┐
│Hombre│
└──┬───┘
   │
   ├──► Camisetas
   │    ├──► Manga corta
   │    ├──► Manga larga
   │    └──► Sin mangas
   │
   ├──► Pantalones
   │    ├──► Largos
   │    ├──► Cortos
   │    └──► Mallas
   │
   ├──► Sudaderas y chaquetas
   │    ├──► Sudaderas con capucha
   │    ├──► Sudaderas sin capucha
   │    └──► Chaquetas cortavientos
   │
   ├──► Calzado
   │    ├──► Zapatillas running
   │    ├──► Zapatillas training
   │    └──► Botas de montaña
   │
   ├──► Accesorios
   │    ├──► Gorras y viseras
   │    ├──► Calcetines
   │    ├──► Mochilas
   │    └──► Botellas y bidones
   │
   └──► Colecciones
        ├──► Nueva temporada
        ├──► Running
        ├──► Yoga
        └──► Gym
```

La rama "Mujer" replica una estructura similar adaptada a las categorías de producto femenino. La rama "Niños" se organiza por rangos de edad (0-2 años, 3-7 años, 8-14 años) y dentro de cada rango por tipo de producto. La rama "Equipos" se divide en Deportes de equipo, Deportes individuales, Fitness en casa y Tecnología deportiva (pulsómetros, relojes GPS). La rama "Outlet" se organiza por las mismas categorías que el catálogo principal pero con precios reducidos. La rama "Marcas" lista las marcas disponibles: Nike, Adidas, Puma, Under Armour, New Balance, Reebok, The North Face. La rama "Ayuda" contiene las páginas funcionales: Contacto, Envíos y devoluciones, Guía de tallas, Preguntas frecuentes, Seguimiento de pedido.

!!! note "Observaciones sobre el diseño del sitemap"
    - La **profundidad máxima es de 3 niveles** (Home > Hombre > Camisetas > Manga corta), lo que cumple con la regla de los 3 clics.
    - La **amplitud en el nivel 1 es de 7 opciones**, justo en el límite del número mágico de Miller.
    - Las categorías del nivel 2 tienen entre **3 y 6 subcategorías** cada una, manteniendo la carga cognitiva manejable.
    - Las etiquetas son **descriptivas y autoexplicativas**, evitando términos ambiguos o jerga interna.

### Ejemplo guiado 2: User flow para el proceso de checkout de un ecommerce

Diseñaremos el user flow completo del proceso de compra (checkout) en el ecommerce de ropa deportiva, contemplando tanto el flujo principal (happy path) como los flujos alternativos y de error.

**Flujo principal (Happy Path):**

El flujo comienza con el usuario en la página de producto, habiendo seleccionado talla y color, y presionando el botón "Añadir al carrito". Describimos cada paso:

```
[PÁGINA DE PRODUCTO]
    │ Usuario hace clic en "Añadir al carrito"
    ▼
[MINI CART / NOTIFICACIÓN]
    │ Se muestra una notificación: "Producto añadido al carrito"
    │ Opciones: "Seguir comprando" o "Ir al carrito"
    │ Usuario hace clic en "Ir al carrito"
    ▼
[CARRITO DE COMPRA]
    │ Muestra: lista de productos, cantidades, precios, total
    │ Usuario revisa cantidades (opcionalmente las modifica)
    │ Usuario hace clic en "Proceder al pago"
    ▼
[CHECKOUT - PASO 1: INFORMACIÓN DE ENVÍO]
    │ Formulario: nombre, apellidos, dirección, ciudad, CP, país, teléfono
    │ Checkbox: "Usar como dirección de facturación"
    │ Usuario rellena datos y hace clic en "Continuar"
    ▼
[CHECKOUT - PASO 2: MÉTODO DE ENVÍO]
    │ Opciones: Estándar (3-5 días, 3,99€), Express (24h, 7,99€)
    │ Usuario selecciona "Express" y hace clic en "Continuar"
    ▼
[CHECKOUT - PASO 3: MÉTODO DE PAGO]
    │ Opciones: Tarjeta, PayPal, Bizum, Transferencia
    │ Usuario selecciona "Tarjeta"
    │ Formulario: número de tarjeta, fecha caducidad, CVV
    │ Usuario rellena datos y hace clic en "Revisar pedido"
    ▼
[CHECKOUT - PASO 4: REVISIÓN Y CONFIRMACIÓN]
    │ Muestra resumen: productos, cantidades, dirección envío, método envío, pago, total
    │ Checkbox: "Acepto los términos y condiciones"
    │ Usuario marca el checkbox y hace clic en "Confirmar y pagar"
    ▼
[PANTALLA DE PROCESAMIENTO]
    │ Animación de carga: "Procesando tu pago..."
    │ (2 segundos de espera simulada)
    ▼
[PANTALLA DE CONFIRMACIÓN]
    │ Mensaje: "¡Pedido confirmado! Número de pedido: #28471"
    │ Resumen del pedido
    │ Botón: "Volver a la tienda"
    │ Email de confirmación enviado automáticamente al usuario
```

**Flujos alternativos y de error:**

Es crucial contemplar qué sucede cuando las cosas no van según lo esperado. Estos flujos se ramifican desde los puntos de decisión del flujo principal:

**Alternativa 1 - Carrito vacío:** Si el usuario intenta acceder a "Proceder al pago" con el carrito vacío (porque los productos expiraron o fueron eliminados), el sistema muestra la página de carrito con un mensaje "Tu carrito está vacío" y sugerencias de productos recomendados. El flujo se desvía a la exploración del catálogo.

**Alternativa 2 - Usuario no autenticado:** Si el usuario no ha iniciado sesión, en el paso 1 del checkout se le ofrece la opción de "Iniciar sesión para recuperar tus datos" o "Continuar como invitado". Si elige iniciar sesión, se abre un modal de login; al autenticarse, el formulario se rellena automáticamente con sus datos guardados.

**Alternativa 3 - Validación de dirección:** Si el código postal no coincide con la ciudad introducida, se muestra un mensaje de advertencia "El código postal no corresponde a la ciudad indicada" en color naranja. Si la dirección no es válida para el servicio de mensajería, se muestra un error "No realizamos envíos a esta ubicación" y se sugiere buscar un punto de recogida cercano.

**Alternativa 4 - Error de pago:** Si la tarjeta es rechazada (fondos insuficientes, fecha incorrecta, CVV erróneo), se muestra un mensaje de error en rojo bajo el campo correspondiente y el botón de confirmación se bloquea. El usuario puede reintroducir los datos o cambiar de método de pago.

**Alternativa 5 - Stock insuficiente:** Si entre que el usuario añadió el producto al carrito y confirma el pedido el stock se ha agotado, se muestra un mensaje en el paso de revisión: "Lo sentimos, el producto X ya no está disponible en la talla seleccionada" y se ofrecen alternativas (otras tallas, productos similares).

**Alternativa 6 - Timeout de sesión:** Si el usuario tarda más de 30 minutos en completar el checkout con la sesión iniciada, al siguiente paso se le pide que vuelva a autenticarse por seguridad. Los datos introducidos hasta el momento se conservan.

### Ejemplo guiado 3: Wireframes de baja y media fidelidad para una aplicación de recetas

Diseñaremos los wireframes para una aplicación móvil de recetas de cocina, mostrando la evolución desde baja fidelidad (boceto conceptual) hasta media fidelidad (wireframe digital con proporciones definidas).

**Wireframe de baja fidelidad - Pantalla de inicio de la app:**

```
┌──────────────────────────────┐
│  [icono hamburguesa]  [logo] │  ← Header bar
├──────────────────────────────┤
│                              │
│  ┌──────────────────────┐    │
│  │  🔍 Buscar recetas   │    │  ← Barra de búsqueda
│  └──────────────────────┘    │
│                              │
│  [Categorías] [Ingredientes] │  ← Tabs de navegación
│  [Dificultad]  [Tiempo]      │     secundaria
│                              │
│  ┌── RECETAS DESTACADAS ───┐ │
│  │ ┌────────┐ ┌────────┐   │ │
│  │ │ Imagen │ │ Imagen │   │ │  ← Carrusel horizontal
│  │ │ Título │ │ Título │   │ │     de cards destacadas
│  │ └────────┘ └────────┘   │ │
│  └─────────────────────────┘ │
│                              │
│  ┌── ÚLTIMAS RECETAS ──────┐ │
│  │ ┌──────────────────────┐│ │
│  │ │ Imagen │ Título      ││ │
│  │ │        │ Dificultad   ││ │  ← Lista vertical de
│  │ │        │ Tiempo       ││ │     recetas recientes
│  │ ├──────────────────────┤│ │
│  │ │ Imagen │ Título      ││ │
│  │ │        │ Dificultad   ││ │
│  │ ├──────────────────────┤│ │
│  │ │ Imagen │ Título      ││ │
│  │ └──────────────────────┘│ │
│  └─────────────────────────┘ │
│                              │
│  [Inicio] [Explorar] [+] [Fav] [Perfil] │ ← Bottom nav
└──────────────────────────────┘
```

!!! note "Notas sobre el wireframe de baja fidelidad"
    - Se utilizan **rectángulos** para los bloques de contenido y **líneas** para los separadores.
    - El texto es descriptivo (no final) para identificar cada elemento.
    - Los **corchetes** indican elementos interactivos.
    - Las proporciones no son exactas: el objetivo es comunicar la **estructura general**.

**Evolución a wireframe de media fidelidad - Misma pantalla:**

Ahora refinamos el diseño con medidas, proporciones y una representación más cercana a lo que será la interfaz final:

```
Frame: 390 x 844px (iPhone 14)

┌──────────────────────────────────┐
│ 40px                             │  ← Status bar area
│ ☰               RecetasApp    ○  │  ← Header, h=56px, bg=#FFF
│ 16px                         16px│
├──────────────────────────────────┤
│ 16px                             │
│ ┌────────────────────────────────┐│
│ │ 🔍  Buscar por nombre o ingred. ││  ← Search bar, h=44px
│ └────────────────────────────────┘│     bg=#F5F5F5, radius=8
│ 16px                             │
│ [Categorías] [Ingredientes] ...  │  ← Tab pills, h=36px
│ 16px                             │
│ RECETAS DESTACADAS               │  ← Section title, 14px
│ 8px                              │
│ ┌───────────┐ ┌───────────┐     │
│ │           │ │           │ 16px │  ← Cards, 156x200px
│ │  Imagen   │ │  Imagen   │     │     radius=12, shadow
│ │  16:9     │ │  16:9     │     │
│ │           │ │           │     │
│ │ Título    │ │ Título    │     │
│ │ ⭐4.8 25m │ │ ⭐4.5 40m │     │
│ └───────────┘ └───────────┘     │
│ 16px                         16px│     Scroll horizontal
│ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ──│  ← más cards visibles
│ 24px                             │     parcialmente
│ ÚLTIMAS RECETAS                  │
│ 8px                              │
│ ┌────────────────────────────────┐│
│ │ ┌──────┐ Título de receta     ││  ← List item, h=88px
│ │ │ Img  │ ⭐⭐⭐⭐⭐ (128)       ││     imagen 72x72
│ │ │72x72 │ ⏱ 35 minutos        ││     texto a la derecha
│ │ └──────┘                      ││
│ ├────────────────────────────────┤│
│ │ ┌──────┐ Otro título largo..  ││
│ │ │ Img  │ ⭐⭐⭐⭐  (95)         ││
│ │ │72x72 │ ⏱ 20 minutos        ││
│ │ └──────┘                      ││
│ └────────────────────────────────┘│
│                                   │
├───────────────────────────────────┤
│  🏠      🔍      ➕      ❤️      👤 │  ← Bottom nav, h=56px
│ Inicio  Explor  Nueva  Favorit Perf│     bg=#FFF, border top
└───────────────────────────────────┘
```

!!! note "Observaciones sobre la evolución"
    Hemos añadido **medidas precisas** (en píxeles), definido alturas de elementos, espaciados exactos siguiendo una escala de **4 px**, y refinado la representación de cada componente para que sea más cercana a su aspecto final. Sin embargo, seguimos **sin utilizar colores reales** (escala de grises), imágenes reales (rectángulos con etiquetas) ni tipografías definitivas.

### Ejemplo guiado 4: Mapa de navegación para un sitio web institucional

Crearemos el mapa de navegación de la sede electrónica de un organismo público, identificando y representando los diferentes tipos de navegación que coexisten en la interfaz.

**Descripción textual del mapa de navegación:**

!!! warning "No confundas sitemap y mapa de navegación"
    Mientras el **sitemap** representa la estructura jerárquica de los contenidos (¿qué páginas hay?), el **mapa de navegación** representa los diferentes sistemas de navegación que permiten al usuario moverse entre esos contenidos (¿cómo se navega entre las páginas?).

Para la sede electrónica analizada, identificamos los siguientes sistemas de navegación:

**1. Navegación global (cabecera principal):**

Presente en todas las páginas del sitio. Las opciones de navegación global representan las grandes áreas funcionales de la sede electrónica.

```
┌──────────────────────────────────────────────────────────┐
│ [Logo organismo]  Inicio  Trámites  Servicios  Sede  Ayuda │
│                                       electrónica         │
│ [Buscador___________________________] [🔍]                 │
└──────────────────────────────────────────────────────────┘
```

Opciones de navegación global: Inicio, Trámites, Servicios, Sede electrónica, Ayuda. Esta navegación es persistente y visible desde cualquier página, proporcionando el marco de referencia constante que responde a la pregunta "¿dónde estoy?".

**2. Navegación local (barra lateral izquierda):**

Visible solo dentro de la sección activa. Cuando el usuario está en "Trámites", la barra lateral muestra las subcategorías de trámites.

```
┌─────────────────┐
│ TRÁMITES        │
│                 │
│ ► Ciudadanía   │
│   - DNI         │
│   - Pasaporte   │
│   - Certificados│
│                 │
│ ► Empresas     │
│   - Constitución│
│   - Licencias   │
│                 │
│ ► Vehículos    │
│   - Matriculación│
│   - ITV        │
│                 │
│ ► Vivienda     │
│   - Catastro    │
│   - Nota simple │
└─────────────────┘
```

**3. Breadcrumbs (migas de pan):**

Presentes debajo de la cabecera en todas las páginas excepto la de inicio. Muestran la ruta jerárquica completa.

```
Inicio > Trámites > Ciudadanía > DNI > Renovación del DNI
```

Cada elemento de la ruta es un enlace (excepto el último, que es la página actual y se muestra en texto sin enlace), permitiendo al usuario retroceder a cualquier nivel superior con un solo clic.

**4. Navegación contextual (enlaces en el contenido):**

Dentro de la página de cada trámite, el contenido incluye enlaces a trámites relacionados, normativa aplicable, preguntas frecuentes específicas y documentos descargables.

```
┌─────────────────────────────────────────────┐
│ RENOVACIÓN DEL DNI                          │
│                                             │
│ Descripción del trámite...                  │
│                                             │
│ Documentación necesaria:                    │
│   • Fotografía reciente (ver requisitos)    │
│                └── Enlace contextual        │
│   • Certificado de empadronamiento          │
│     (solicitar cita previa)                 │
│       └── Enlace contextual                 │
│                                             │
│ Trámites relacionados:                      │
│   • Renovación del pasaporte                │
│   • Cambio de domicilio en el DNI           │
│   • Denuncia por robo o extravío            │
│                                             │
│ Normativa: Ley Orgánica 4/2015...           │
│                                             │
│ [Iniciar trámite online]  [Descargar modelo]│
└─────────────────────────────────────────────┘
```

**5. Navegación de footer (pie de página):**

Presente en todas las páginas, contiene enlaces a información corporativa, legal y de contacto.

```
┌──────────────────────────────────────────────────────────┐
│ Aviso legal │ Política de privacidad │ Accesibilidad │ Mapa web │
│ Contacto │ RSS │ © Organismo 2026                           │
│ Redes sociales: [Twitter] [Facebook] [Instagram] [YouTube]  │
└──────────────────────────────────────────────────────────┘
```

**6. Navegación de utilidad (cabecera secundaria):**

En la esquina superior derecha, fuera de la navegación principal, se encuentran los enlaces de utilidad.

```
                                          [🔤 Tamaño texto] [🌐 ES ▼] [🔑 Acceder]
```

Estos enlaces permiten cambiar el tamaño del texto (accesibilidad), seleccionar el idioma de la interfaz (Castellano, Catalán, Gallego, Euskera, Inglés), y acceder al área personal mediante certificado digital, DNI electrónico o Cl@ve.

### Ejemplo guiado 5: Ejecución y análisis de un Card Sorting para un portal educativo

Simularemos una sesión de Card Sorting abierto para un portal educativo que ofrece cursos online, y analizaremos los resultados para definir la estructura de categorías.

**Preparación de las tarjetas:**

Se seleccionan 35 contenidos representativos del portal educativo, redactados como tarjetas concisas:

Tarjetas sobre cursos y contenido formativo:

1. Curso de Programación Web con HTML y CSS
2. Curso de JavaScript Avanzado
3. Curso de Python para Ciencia de Datos
4. Curso de Diseño UX/UI
5. Curso de Marketing Digital
6. Curso de Inglés B2
7. Curso de Contabilidad para PYMES
8. Curso de Fotografía Digital
9. Curso de Inteligencia Artificial
10. Curso de Ciberseguridad

Tarjetas sobre funcionalidades de la plataforma:

11. Mi perfil de estudiante
12. Certificados obtenidos
13. Historial de cursos
14. Progreso actual
15. Configuración de cuenta
16. Cambiar contraseña
17. Métodos de pago
18. Facturación e historial de compras
19. Cerrar sesión

Tarjetas sobre soporte y comunidad:

20. Preguntas frecuentes
21. Contactar con soporte técnico
22. Chat en vivo con tutor
23. Foros de discusión
24. Grupos de estudio
25. Mentorías personalizadas

Tarjetas sobre información institucional:

26. Sobre nosotros
27. Nuestros profesores
28. Metodología de enseñanza
29. Opiniones de estudiantes
30. Becas y financiación
31. Programa de afiliados
32. Bolsa de trabajo
33. Empresas colaboradoras
34. Blog educativo
35. Términos y condiciones

**Resultados de la sesión (simulados para 12 participantes):**

Tras ejecutar el Card Sorting con 12 participantes, analizamos la matriz de similaridad y el dendrograma. Los resultados muestran un consenso claro en la agrupación de la mayoría de tarjetas, con algunas discrepancias interesantes.

Agrupación con mayor consenso (más del 80% de participantes):

- Grupo A (etiquetado por participantes como "Cursos", "Catálogo", "Formación"): tarjetas 1-10. Todos los participantes agruparon todos los cursos juntos. Sin embargo, hubo divergencia en la subagrupación: 7 participantes subagruparon por temática (Tecnología, Negocios, Creatividad, Idiomas) y 5 participantes subagruparon por nivel (Básico, Intermedio, Avanzado). Esto sugiere que el portal debería ofrecer ambas formas de exploración (navegación por categorías temáticas y filtro por nivel).

- Grupo B (etiquetado como "Mi cuenta", "Perfil", "Área personal"): tarjetas 11-19. Consenso casi unánime, aunque las tarjetas 17-18 (Métodos de pago, Facturación) fueron colocadas por 3 participantes en un grupo separado llamado "Pagos". Esto sugiere que facturación podría ser una subcategoría de "Mi cuenta" o una categoría independiente si los usuarios le dan mucha importancia.

- Grupo C (etiquetado como "Ayuda", "Soporte"): tarjetas 20-22. Consistente.

- Tarjetas con discrepancia: las tarjetas 23-25 (Foros, Grupos de estudio, Mentorías) fueron etiquetadas como "Comunidad" por 8 participantes, pero como "Aprendizaje" por 4 participantes. Esta ambigüedad sugiere que estos contenidos son percibidos como parte integral del proceso de aprendizaje, no como un añadido social separado.

**Estructura de navegación propuesta basada en el Card Sorting:**

Nivel 1 (navegación global): Cursos, Comunidad, Mi Cuenta, Ayuda, Sobre Nosotros

Nivel 2 (subcategorías):

- Cursos > Tecnología, Negocios, Creatividad, Idiomas
- Comunidad > Foros, Grupos de estudio, Mentorías, Blog
- Mi Cuenta > Perfil, Historial, Certificados, Pagos
- Ayuda > FAQ, Soporte, Chat con tutor
- Sobre Nosotros > Metodología, Profesores, Becas, Empresas, Bolsa de trabajo

### Ejemplo guiado 6: Diseño de navegación responsive para un portal de noticias

Diseñaremos la adaptación de la navegación de un portal de noticias a tres breakpoints diferentes (móvil, tablet y escritorio), mostrando cómo los patrones de navegación cambian en función del espacio disponible.

**Breakpoint escritorio (≥1024 px):**

En escritorio, disponemos de espacio suficiente para mostrar la navegación completa. La cabecera incluye el logo, la fecha, el tiempo, la navegación global completa, acceso al área de usuario y un botón de suscripción.

```
┌──────────────────────────────────────────────────────────────┐
│ [LOGO NOTICIAS24]  12 de junio de 2026  ☀ 24°C Madrid       │
│                                                              │
│ [🔍 Buscar...                                  ] [🔔] [👤 ▼] │
│                                                              │
│ Nacional | Internacional | Economía | Deportes | Cultura |   │ ← Nav global
│ Tecnología | Ciencia | Opinión | Vídeos | Podcasts [SUSCRIB] │
└──────────────────────────────────────────────────────────────┘
│                                                                  │
│ Breadcrumb: Inicio > Economía > Mercados                         │
│                                                                  │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│ [CONTENIDO PRINCIPAL DE LA PÁGINA ACTUAL]                       │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
│                                                                  │
│ Footer: Enlaces, Copyright, Redes sociales                       │
└──────────────────────────────────────────────────────────────────┘
```

**Breakpoint tablet (768 px - 1023 px):**

En tablet, el espacio se reduce. La navegación global se compacta mostrando solo las secciones principales. Las secciones secundarias se trasladan a un menú "Más" desplegable. El buscador se reduce a un icono.

```
┌────────────────────────────────────────────────┐
│ [LOGO]  ☀ 24°C  [🔍]  [🔔]  [👤]  [☰]       │
│                                                │
│ Nacional | Internacional | Economía | Deportes │ ← Solo 4 secciones
│ | Más ▼                                        │    principales, el resto
│                                                │    en "Más"
├────────────────────────────────────────────────┤
│ Breadcrumb: Inicio > Economía > Mercados       │
├────────────────────────────────────────────────┤
│ [CONTENIDO PRINCIPAL]                          │
└────────────────────────────────────────────────┘
```

**Breakpoint móvil (<768 px):**

En móvil, el espacio es crítico. La navegación se oculta tras un menú hamburguesa. Aparece una barra de navegación inferior fija con accesos rápidos a las secciones más utilizadas (bottom navigation, inspirada en patrones de apps móviles). El breadcrumb desaparece o se simplifica a un botón de retroceso.

```
┌──────────────────────────────────┐
│ [LOGO]            [🔍] [☰]      │ ← Header simplificado
├──────────────────────────────────┤
│                                  │
│ [CONTENIDO PRINCIPAL]            │
│                                  │
│                                  │
│                                  │
│                                  │
├──────────────────────────────────┤
│  🏠        📰        ▶️        ⚙ │ ← Bottom nav fija
│ Portada   Últimas   Vídeos  Más │    con 4 accesos
└──────────────────────────────────┘    principales
```

**Menú hamburguesa desplegado en móvil:**

Al hacer clic en el icono de hamburguesa (☰), se despliega un panel lateral (off-canvas) que cubre parcialmente la pantalla.

```
┌──────────────────┬─────────────┐
│                  │ ✕ Cerrar    │
│                  │             │
│ [Contenido       │ ► Portada   │
│  principal       │ ► Nacional  │
│  visible pero    │ ► Internac. │
│  atenuado por    │ ► Economía  │
│  overlay oscuro] │ ► Deportes  │
│                  │ ► Cultura   │
│                  │ ► Tecnología│
│                  │ ► Opinión   │
│                  │ ► Vídeos    │
│                  │             │
│                  │ ─────────   │
│                  │ 👤 Mi cuenta│
│                  │ ⭐ Favoritos│
│                  │ ⚙ Ajustes  │
│                  │ 🌐 Idioma   │
└──────────────────┴─────────────┘
```

Al hacer clic fuera del panel o en "Cerrar", el menú se desliza hacia la izquierda (animación de salida) y el contenido principal recupera su opacidad completa. Este patrón off-canvas proporciona acceso a la navegación completa sin abandonar la página actual ni perder el contexto de lectura.

## Casos reales

### Caso real 1: Arquitectura de la información de Amazon

Amazon representa, probablemente, el caso de estudio más complejo y sofisticado de arquitectura de la información en el comercio electrónico mundial. Con cientos de millones de productos, decenas de categorías de primer nivel y una base de usuarios que abarca todos los perfiles demográficos imaginables, la AI de Amazon debe satisfacer simultáneamente a quien busca un producto específico que ya conoce y a quien explora sin un objetivo definido.

La página de inicio de Amazon es un ejemplo magistral de equilibrio entre navegación global, navegación contextual y personalización. La cabecera contiene la navegación global principal con el mega menú "Todas las categorías" (una lista desplegable que da acceso a las aproximadamente 30 categorías de primer nivel del marketplace), la barra de búsqueda (el elemento más destacado visualmente, reflejando que la búsqueda es el modo principal de interacción para la mayoría de usuarios), y los enlaces de utilidad (cuenta, pedidos, lista de deseos, carrito).

El mega menú de Amazon es un caso de estudio por sí mismo. Al pasar el cursor sobre "Todas las categorías", se despliega un panel que muestra todas las categorías principales en una columna izquierda, y al pasar el cursor sobre cada una, un panel derecho muestra las subcategorías, categorías destacadas y ofertas especiales de esa sección. Este patrón permite acceder a cualquier categoría del sitio con un solo clic desde cualquier página, eliminando la necesidad de recordar rutas de navegación complejas.

La página de resultados de búsqueda de Amazon incorpora navegación facetada avanzada. Las facetas se generan dinámicamente a partir de los resultados: Departamento (categoría del producto), Valoración del cliente, Precio (con histograma de distribución), Marca, Características específicas de la categoría (talla para ropa, capacidad para dispositivos de almacenamiento, tipo de pantalla para televisores), Disponibilidad (Prime, envío gratis, entrega hoy) y Condición (nuevo, segunda mano). Las facetas activas se muestran como chips con un icono de cierre sobre los resultados, permitiendo al usuario ver y modificar sus criterios de filtrado sin perder el contexto.

La estructura de página de producto de Amazon sigue un patrón consistente que prioriza la información según su relevancia para la decisión de compra: imagen del producto (con galería y zoom), título, valoración y número de reseñas, precio y opciones de compra (con variantes de talla, color, configuración), información de envío y disponibilidad, sección "Comprados juntos habitualmente" (navegación contextual basada en datos de compra reales), descripción del producto, fichas técnicas, preguntas de clientes, reseñas de clientes (con navegación facetada dentro de las propias reseñas: por puntuación, por tema, con imágenes). Cada sección responde a una pregunta específica que el comprador se formula durante el proceso de decisión.

### Caso real 2: Arquitectura de la información de Airbnb

Airbnb ofrece un caso de estudio fascinante porque su AI debe manejar simultáneamente una estructura de contenidos masivos (millones de alojamientos en prácticamente todos los países del mundo) y un modelo de interacción basado en la exploración visual y aspiracional, no solo en la búsqueda funcional.

La página de inicio de Airbnb está dominada por un componente de búsqueda visualmente prominente que permite al usuario especificar el destino (con autocompletado predictivo que sugiere destinos populares, regiones y alojamientos flexibles), las fechas (con un selector de calendario de doble panel) y el número de huéspedes. Este componente de búsqueda refleja el modelo mental del usuario que llega a Airbnb: "Quiero encontrar un lugar donde alojarme en X destino durante Y fechas para Z personas". La simplicidad de esta entrada (tres campos) oculta una complejidad enorme en el backend.

Debajo del buscador, la página de inicio presenta una navegación basada en categorías visuales (iconos grandes con etiquetas) que permiten la exploración aspiracional: "Frente a la playa", "Cabañas", "Casas diminutas", "Islas", "Casas rurales", "Diseño", "Viñedos", "Fincas". Esta navegación representa un esquema de organización por tópico mezclado con atributos del alojamiento, y está diseñada para el usuario que no tiene un destino concreto sino un tipo de experiencia en mente. Es un ejemplo de cómo la AI debe adaptarse a diferentes modos de búsqueda (conocida vs. exploratoria) dentro del mismo sitio.

La página de resultados de búsqueda de Airbnb integra un mapa interactivo como elemento de navegación espacial. Los resultados se muestran simultáneamente como lista (panel izquierdo con tarjetas de alojamiento) y como puntos en el mapa (panel derecho). Esta dualidad permite al usuario alternar entre la evaluación detallada de alojamientos individuales y la navegación geográfica para explorar barrios o zonas. Los filtros (faceted navigation) incluyen facetas estándar (precio, tipo de alojamiento, número de habitaciones) y facetas específicas del dominio (idioma del anfitrión, servicios destacados como piscina o wifi, reglas de la casa como admite mascotas, tipo de propiedad). Airbnb introdujo recientemente facetas de "flexibilidad" que permiten buscar por tipo de viaje o estilo de alojamiento en lugar de por parámetros rígidos, reflejando una comprensión más matizada de los modelos mentales de los usuarios.

La página de detalle de alojamiento en Airbnb sigue una jerarquía informativa que prioriza: galería de fotos (el elemento más importante para la decisión), información resumida (tipo de alojamiento, título, ubicación, capacidades), valoraciones y reseñas, descripción del espacio, servicios ofrecidos (organizados en categorías colapsables), disponibilidad y precios (con calendario interactivo), evaluaciones detalladas, ubicación en el mapa, información sobre el anfitrión, normas de la casa, política de cancelación, y finalmente una sección de alojamientos similares (navegación contextual). La barra inferior fija (en móvil) o el panel lateral (en escritorio) muestra persistentemente el precio y un botón de reserva, eliminando la necesidad de volver al inicio de la página para completar la acción principal.

### Caso real 3: Arquitectura de la información de la Sede Electrónica del Gobierno de España

La Sede Electrónica (sede.administracion.gob.es) representa un caso de estudio en AI para servicios públicos digitales, donde las consideraciones de accesibilidad, claridad y universalidad son aún más críticas que en el sector privado, ya que el sitio debe ser utilizable por el 100% de la ciudadanía, incluyendo personas mayores, personas con discapacidad y personas con bajo nivel de alfabetización digital.

La página de inicio de la Sede Electrónica utiliza un esquema de organización híbrido que combina la organización por tópico (trámites agrupados por área temática: Trabajo y prestaciones, Vivienda y urbanismo, Educación y formación, Salud y servicios sociales, Transportes y vehículos) con la organización por audiencia (accesos rápidos para Ciudadanos, Empresas y Administraciones). Esta doble vía de acceso reconoce que diferentes usuarios conceptualizan los trámites de formas diferentes: algunos piensan en el área vital afectada (salud, educación, vivienda), mientras que otros se identifican primero como ciudadanos o empresarios.

La navegación global de la Sede Electrónica es deliberadamente reducida: solo cuatro o cinco opciones principales (Inicio, Trámites, Servicios, Ayuda) para no abrumar a usuarios con poca experiencia digital. La navegación local, sin embargo, es extensa y detallada, con menús laterales jerárquicos que muestran la estructura completa de la sección activa y permiten al usuario comprender la profundidad y amplitud de los contenidos disponibles. Los breadcrumbs son omnipresentes y muy visibles, reflejando la importancia de que el usuario sepa siempre dónde está en un sitio potencialmente muy profundo.

Un aspecto destacable de la Sede Electrónica es su sistema de búsqueda, que incorpora búsqueda predictiva con sugerencias de trámites frecuentes y un buscador avanzado facetado que permite filtrar por tipo de trámite, organismo responsable, nivel de administración (estatal, autonómico, local), perfil del solicitante (ciudadano, empresa, administración) y modo de tramitación (online, presencial, telefónico). La página de resultados de búsqueda muestra para cada trámite: nombre, organismo emisor, descripción breve, plazo de resolución, modo de tramitación, y etiquetas de clasificación, proporcionando la información necesaria para que el usuario decida cuál es el trámite correcto sin tener que hacer clic en cada resultado.

La accesibilidad en la Sede Electrónica es particularmente relevante. El sitio debe cumplir la normativa vigente:

!!! info "Normativa de accesibilidad del sector público"
    - **Real Decreto 1112/2018** — accesibilidad de los sitios web y aplicaciones del sector público.
    - **UNE-EN 301549** — norma técnica equiparable a **WCAG 2.1 nivel AA**.

La AI del sitio refleja este compromiso: las etiquetas son **claras y literales** (evitando metáforas o jerga), la profundidad de navegación se mantiene controlada, existen **múltiples formas de llegar al mismo contenido** (búsqueda, navegación por categorías, navegación por audiencia), y los elementos interactivos como menús desplegables y acordeones están diseñados para ser operables tanto con **ratón** como con **teclado y lectores de pantalla**.

## Actividades guiadas

### Actividad guiada 1: Creación de un sitemap completo para un portal de formación online

**Objetivo:** Diseñar y documentar el sitemap completo de un portal de formación online que ofrezca cursos, certificaciones, recursos y comunidad, aplicando principios de jerarquía, etiquetado y equilibrio profundidad-amplitud.

**Contexto:** La empresa "LearnHub" planea lanzar un portal de formación online con cursos en tecnología, negocio, creatividad y desarrollo personal. Necesitan un sitemap que organice lógicamente todos los contenidos y funcionalidades. El portal incluirá: catálogo de cursos con páginas de detalle, sistema de usuario con perfil y progreso, área de instructores, blog, foros de comunidad, página de precios y suscripciones, y páginas corporativas.

**Pasos a seguir:**

1. Realiza un inventario de todos los tipos de contenido y funcionalidades que debe albergar el portal. Enumera al menos 30 elementos diferentes. Clasifícalos en: contenidos principales (cursos, categorías), funcionalidades de usuario (perfil, progreso, certificados), contenidos de soporte (blog, FAQ, ayuda), y páginas institucionales (sobre nosotros, contacto, términos).
2. Define las categorías principales de primer nivel (navegación global). Justifica tu elección: ¿por qué esas categorías y no otras? Aplica la regla de 7±2 para mantener las opciones manejables.
3. Para cada categoría de primer nivel, desarrolla la estructura de subcategorías (segundo nivel). Asegúrate de que la profundidad no exceda 4 niveles en ningún caso.
4. Dibuja el sitemap utilizando una herramienta de diagramación (Figma, Miro, Lucidchart, Draw.io) o a mano sobre papel. Utiliza cajas para las páginas y líneas de conexión para las relaciones jerárquicas. Etiqueta cada caja con el nombre de la página.
5. Diferencia visualmente los diferentes tipos de páginas: usa un código de color o de forma para distinguir páginas de contenido, páginas funcionales, páginas de template (que se repiten para cada elemento, como la página de detalle de curso) y enlaces externos.
6. Identifica y anota en el diagrama al menos 3 puntos donde el usuario podría necesitar navegación contextual (enlaces entre páginas que no están directamente conectadas en la jerarquía pero que están relacionadas temáticamente).
7. Verifica el sitemap contra los principios aprendidos: ¿hay alguna página a más de 3 clics de la home? ¿Hay categorías con más de 9 subcategorías? ¿Hay etiquetas ambiguas? Corrige lo necesario.
8. Redacta un pequeño informe (500 palabras) justificando las decisiones principales de estructuración y comparando tu sitemap con al menos una alternativa que consideraste y descartaste.

**Criterios de evaluación:**

- El inventario de contenidos es exhaustivo y cubre todos los elementos relevantes (1.5 puntos).
- Las categorías de primer nivel son lógicas y respetan la regla de 7±2 (1.5 puntos).
- La profundidad máxima es de 4 niveles o menos (1 punto).
- El diagrama es claro, sigue una notación consistente y diferencia tipos de página (2 puntos).
- Las conexiones de navegación contextual están identificadas y justificadas (1 punto).
- El informe justifica las decisiones y menciona alternativas (1.5 puntos).
- La nomenclatura de las páginas es clara, consistente y sin ambigüedades (1.5 puntos).

### Actividad guiada 2: Wireframes responsive para una aplicación de gestión de tareas

**Objetivo:** Crear wireframes de media fidelidad para una aplicación web de gestión de tareas (estilo Kanban), cubriendo tres breakpoints (móvil, tablet, escritorio) y mostrando cómo se reorganiza la interfaz responsive.

**Contexto:** La aplicación "TaskBoard" permite a los usuarios gestionar proyectos mediante tableros Kanban con columnas (To Do, In Progress, Review, Done), tarjetas de tarea arrastrables, y funcionalidades de colaboración (comentarios, asignación, fechas límite). Debes wireframear las pantallas principales en los tres breakpoints.

**Pasos a seguir:**

1. Crea tres frames en Figma o en papel correspondientes a los tres breakpoints: móvil 375x812px, tablet 768x1024px, escritorio 1440x900px.
2. Identifica los bloques de contenido principales de la aplicación: barra de navegación superior, barra lateral de proyectos, tablero Kanban (con columnas y tarjetas), panel de detalle de tarea (modal o panel lateral), barra de búsqueda y filtros.
3. Wireframea la vista de tablero Kanban en escritorio. Incluye: sidebar izquierda con lista de proyectos, área principal con las 4 columnas del Kanban en horizontal (cada columna ocupando aproximadamente un 25% del ancho), cabecera con nombre del proyecto, botones de filtrar/compartir/configurar, y miniaturas de avatares de colaboradores.
4. Wireframea la misma vista en tablet. Decide qué cambia: ¿se mantienen las 4 columnas horizontales pero más estrechas? ¿Se colapsa la sidebar en un menú tipo drawer? ¿Se reducen a 2 columnas visibles con scroll horizontal? Justifica tu decisión con anotaciones.
5. Wireframea la vista en móvil. En este breakpoint, el Kanban horizontal de 4 columnas no es viable. Diseña una alternativa: columnas como tabs horizontales (cada tab muestra una columna completa en vertical), o vista de lista agrupada por estado, o scroll horizontal de columnas. Elige una opción y justifica.
6. Añade el wireframe del panel de detalle de tarea: en escritorio como panel lateral derecho que se abre sin salir del Kanban, en tablet como modal centrado, en móvil como pantalla completa.
7. Añade anotaciones a cada wireframe explicando: cómo se comportan los elementos interactivos (drag and drop de tarjetas, clic para abrir detalle), qué sucede en estados especiales (tablero vacío, carga de datos, error de conexión), y cómo se ha aplicado el principio de mobile-first (empezar diseñando para móvil y luego expandir).
8. Incluye al menos 5 anotaciones que relacionen decisiones de wireframe con su equivalente técnico en HTML/CSS (por ejemplo: "Esta sidebar será un elemento <aside> con position: fixed y transform: translateX para la animación off-canvas en móvil").

**Criterios de evaluación:**

- Los tres breakpoints están correctamente dimensionados y los wireframes son coherentes entre sí (1.5 puntos).
- La reorganización responsive está justificada con anotaciones para cada breakpoint (2 puntos).
- El panel de detalle de tarea se adapta correctamente en los tres breakpoints (1.5 puntos).
- Los estados especiales (vacío, carga, error) están contemplados (1 punto).
- Las anotaciones son claras e informativas (1.5 puntos).
- Las equivalencias con HTML/CSS están identificadas correctamente (1 punto).
- El diseño sigue los principios de mobile-first (1.5 puntos).

### Actividad guiada 3: Análisis y rediseño de la AI de un sitio web existente

**Objetivo:** Analizar críticamente la arquitectura de la información de un sitio web real, identificar problemas, proponer mejoras justificadas y documentarlas en un informe profesional.

**Contexto:** Cada alumno (o pareja) seleccionará un sitio web real de una PYME local, una asociación, un organismo público pequeño o un comercio electrónico de tamaño medio. El sitio debe tener al menos 15 páginas para que el análisis sea significativo.

**Pasos a seguir:**

1. Selecciona y documenta el sitio web elegido: URL, propósito del sitio, audiencia objetivo (estimada), tipo de contenido que alberga.
2. Realiza un inventario completo de páginas: navega sistemáticamente por el sitio comenzando desde la home, sigue todos los enlaces de navegación, y registra cada página única con su URL y su título.
3. Reconstruye el sitemap actual del sitio a partir de tu inventario: dibuja la estructura jerárquica tal como existe actualmente, no como crees que debería ser.
4. Identifica y documenta los sistemas de navegación presentes (global, local, contextual, breadcrumbs, búsqueda, footer) y evalúa cada uno: ¿funciona correctamente? ¿es consistente? ¿hay elementos rotos?
5. Realiza una prueba informal de Tree Testing: selecciona 5 contenidos del sitio y pide a 2-3 compañeros que intenten encontrarlos partiendo de la home. Registra: ¿lo encontraron? ¿cuántos clics necesitaron? ¿se desorientaron en algún momento? ¿qué ruta siguieron?
6. Identifica al menos 5 problemas de arquitectura de la información, clasificándolos según el componente de la AI afectado: organización (contenido mal categorizado), etiquetado (etiquetas ambiguas o inconsistentes), navegación (estructura de menús confusa, demasiada profundidad, enlaces rotos), búsqueda (resultados irrelevantes o inexistente).
7. Para cada problema identificado, propone una solución concreta y justifícala en base a los principios teóricos estudiados.
8. Dibuja el sitemap rediseñado que incorpore tus mejoras. Utiliza un color diferente o anotaciones para señalar los cambios respecto al sitemap original.
9. Redacta un informe de análisis y recomendaciones (mínimo 1500 palabras) estructurado en: resumen ejecutivo, metodología de análisis, hallazgos detallados (problemas encontrados), recomendaciones (mejoras propuestas), sitemap actual vs. sitemap propuesto, y conclusiones.

**Criterios de evaluación:**

- El inventario de páginas es exhaustivo y preciso (1.5 puntos).
- El sitemap reconstruido refleja fielmente la estructura actual del sitio (1.5 puntos).
- La evaluación de sistemas de navegación es detallada y crítica (1 punto).
- El Tree Testing informal se ha ejecutado y documentado correctamente (1 punto).
- Se han identificado al menos 5 problemas pertinentes y clasificados correctamente (2 puntos).
- Las soluciones propuestas son viables y están justificadas con teoría (1.5 puntos).
- El sitemap rediseñado mejora claramente el original (1 punto).
- El informe es profesional, está bien estructurado y es convincente (0.5 puntos).

### Actividad guiada 4: Card Sorting y propuesta de estructura para una intranet universitaria

**Objetivo:** Planificar, ejecutar (simuladamente) y analizar un estudio de Card Sorting para definir la estructura de navegación de una intranet universitaria.

**Contexto:** La Universidad Tecnológica del Sur va a renovar su intranet para estudiantes. Actualmente la intranet es un caos de enlaces acumulados durante años sin organización clara. Se te encarga realizar un Card Sorting para definir la nueva estructura. La intranet debe dar acceso a: matrícula, expediente académico, horarios, calendario de exámenes, becas, aula virtual (Moodle), biblioteca, correo universitario, servicios del campus (deporte, cultura, alojamiento), secretaría virtual, trámites administrativos, movilidad internacional, prácticas en empresa, orientación profesional, y más.

**Pasos a seguir:**

1. Prepara 40 tarjetas de contenido para el Card Sorting. Cada tarjeta debe representar un contenido o funcionalidad de la intranet, redactada de forma clara y concreta (por ejemplo: "Consultar notas del semestre actual", "Solicitar beca de comedor", "Reservar pista de tenis", "Descargar justificante de matrícula").
2. Define el protocolo de la sesión: ¿Card Sorting abierto, cerrado o híbrido? Justifica tu elección. ¿Cuántos participantes necesitas como mínimo? ¿Qué instrucciones les darás?
3. Ejecuta el Card Sorting tú mismo como participante (auto-card-sort) para tener una primera aproximación. Agrupa las 40 tarjetas en las categorías que consideres lógicas y nómbralas.
4. Simula los resultados de otros 8 participantes. Para cada participante, describe brevemente su perfil (estudiante de primero, de doctorado, de intercambio, etc.) y cómo agruparon las tarjetas (pueden ser variaciones sobre tu propia agrupación).
5. Analiza los resultados consolidados: identifica las agrupaciones con mayor consenso (tarjetas que al menos 7 de 9 participantes agruparon juntas) y los puntos de discrepancia (tarjetas que generaron agrupaciones divergentes). Para las discrepancias, formula hipótesis sobre por qué ocurren.
6. A partir del análisis, propón la estructura de categorías de primer y segundo nivel para la nueva intranet. La estructura debe tener entre 5 y 7 categorías de primer nivel y una profundidad máxima de 3 niveles.
7. Diseña un Tree Testing para validar tu propuesta: selecciona 10 tareas de búsqueda representativas (por ejemplo: "¿Dónde consultarías el horario de tutorías de tu profesor?"), define la estructura de árbol que presentarás a los participantes, y redacta las instrucciones que les darías.
8. Reflexiona sobre el proceso: ¿qué aprendiste sobre los modelos mentales de los estudiantes universitarios? ¿Qué harías diferente en un estudio real? ¿Qué limitaciones tiene un Card Sorting simulado frente a uno con participantes reales?

**Criterios de evaluación:**

- Las 40 tarjetas son representativas, claras y cubren el dominio adecuadamente (2 puntos).
- La elección del tipo de Card Sorting está justificada (0.5 puntos).
- El auto-card-sort está correctamente ejecutado y documentado (1 punto).
- Los 8 perfiles simulados son variados y verosímiles (1.5 puntos).
- El análisis identifica correctamente consensos y discrepancias con hipótesis razonables (1.5 puntos).
- La estructura propuesta es lógica, con 5-7 categorías de nivel 1 y profundidad máxima 3 (1.5 puntos).
- El Tree Testing está correctamente diseñado (1 punto).
- La reflexión sobre el proceso es honesta, crítica y revela aprendizaje (1 punto).

## Actividades propuestas

### Actividad propuesta 1: Diseño completo de AI para un marketplace de servicios profesionales

Imagina que trabajas como arquitecto de información para una startup que está creando un marketplace online donde profesionales freelance (diseñadores, desarrolladores, traductores, consultores, etc.) pueden ofrecer sus servicios y clientes pueden contratarlos. Tu tarea es diseñar la arquitectura de información completa del producto. Debes entregar: un sitemap exhaustivo de todo el sitio (mínimo 40 páginas), wireframes de media fidelidad de las 5 pantallas más críticas (home, búsqueda de profesionales, perfil de profesional, proceso de contratación, dashboard del profesional) en dos breakpoints, user flows detallados para 3 flujos principales (buscar y contratar a un profesional, publicar un servicio como profesional, gestionar un proyecto en curso), y un mapa de navegación que documento todos los sistemas de navegación. Todo debe ir acompañado de un documento de especificación que justifique, con base en principios de AI y UX, las decisiones estructurales principales.

### Actividad propuesta 2: Card Sorting y Tree Testing con usuarios reales

Organiza y ejecuta un estudio de Card Sorting real con un mínimo de 5 participantes para un proyecto de tu entorno (puede ser el proyecto integrado del ciclo, la web de un negocio familiar, una asociación a la que pertenezcas, o la página web que diseñaste en otra asignatura). Prepara entre 30 y 50 tarjetas, ejecuta las sesiones (pueden ser presenciales o remotas usando OptimalSort, Miro o FigJam), analiza los resultados con matriz de similaridad y dendrograma, y propón una estructura de categorías basada en los hallazgos. A continuación, valida tu propuesta con un Tree Testing utilizando al menos 3 participantes diferentes. Documenta todo el proceso en un informe de investigación de UX que incluya: objetivos del estudio, metodología detallada, participantes (perfiles anonimizados), resultados del Card Sorting (con visualizaciones), estructura propuesta, resultados del Tree Testing (con métricas de éxito, direccionalidad y tiempo), y conclusiones.

### Actividad propuesta 3: Análisis comparativo de la AI de tres sitios web del mismo sector

Selecciona tres sitios web que compitan en el mismo sector (por ejemplo: tres ecommerce de moda como Zara, Mango y Uniqlo; tres aerolíneas como Iberia, Vueling y Ryanair; tres bancos online como ING, BBVA y Revolut; tres plataformas de streaming como Netflix, HBO Max y Disney+). Para cada uno, realiza un análisis exhaustivo de su arquitectura de la información: reconstruye su sitemap (al menos las categorías principales y secundarias), documenta sus sistemas de navegación (global, local, contextual, breadcrumbs, búsqueda, facetada), analiza sus esquemas de organización (¿por tópico, por tarea, por audiencia, híbrido?), y evalúa la claridad y consistencia de su etiquetado. Presenta tus hallazgos en una tabla comparativa y redacta un análisis crítico (mínimo 2000 palabras) que compare las tres AI e identifique patrones comunes, diferencias notables, fortalezas y debilidades de cada una, y lecciones que podrían aplicarse a otros proyectos del sector.

### Actividad propuesta 4: Prototipo de AI para un proyecto de transformación digital de una PYME

Selecciona una PYME real de tu entorno (puede ser el negocio de un familiar, una tienda de barrio, un taller, una gestoría, una clínica) que actualmente no tenga presencia digital o la tenga muy limitada. Entrevista al propietario o responsable para entender el negocio, sus productos o servicios, sus clientes y sus necesidades digitales. A partir de esta investigación, diseña la arquitectura de la información completa para el sitio web o aplicación que esa PYME necesitaría para digitalizar sus servicios. Entrega: una propuesta de sitemap con justificación de las categorías principales (basada en las necesidades detectadas en la entrevista), wireframes de las pantallas principales en dos breakpoints, al menos dos user flows representativos de las tareas más importantes que los clientes realizarían, un mapa de navegación completo, y un breve plan de implementación que describa cómo se desarrollaría el proyecto y qué métricas de éxito se utilizarían para evaluar la efectividad de la AI una vez implementada.

## Actividades de ampliación

### Actividad de ampliación 1: Investigación y aplicación de estrategias de AI para SEO

**Contexto:** La Arquitectura de la Información y el SEO (Search Engine Optimization) están profundamente interrelacionados. La estructura del sitio, las URLs, el enlazado interno y los sitemaps XML son factores que los motores de búsqueda utilizan para entender y rankear un sitio web. Esta actividad explora la intersección entre AI y SEO.

**Objetivos:**

- Investigar cómo la arquitectura de la información impacta en el SEO: estructura de URLs amigables, importancia de la jerarquía plana (flat architecture), enlazado interno estratégico (internal linking), breadcrumbs con datos estructurados (schema.org), y sitemaps XML.
- Seleccionar un sitio web existente con una AI deficiente (o utilizar el analizado en la Actividad Propuesta 1).
- Realizar una auditoría SEO de la AI actual del sitio: analizar la estructura de URLs (¿son jerárquicas y descriptivas?), el enlazado interno (¿están las páginas importantes a pocos clics de la home?), la presencia de breadcrumbs, y la existencia y calidad del sitemap XML.
- Rediseñar la AI del sitio aplicando simultáneamente principios de AI centrada en el usuario y mejores prácticas de SEO.
- Crear un sitemap visual optimizado, un diagrama de enlazado interno (qué páginas enlazan a cuáles y con qué anchor text), y un ejemplo de archivo sitemap XML para el sitio rediseñado.
- Implementar datos estructurados (schema.org) para los breadcrumbs y la jerarquía del sitio en formato JSON-LD, con al menos 3 ejemplos de páginas diferentes.
- Redactar un informe que explique la relación bidireccional entre AI y SEO, documente las decisiones tomadas en el rediseño y estime el impacto potencial en el tráfico orgánico.

**Formato de entrega:** Informe de investigación (2000-3000 palabras), sitemap visual rediseñado, diagrama de enlazado interno, archivo sitemap.xml de ejemplo, ejemplos de datos estructurados JSON-LD, y presentación resumen en formato PDF.

**Rúbrica de evaluación:**

- La investigación sobre AI y SEO es rigurosa y cita fuentes relevantes (1.5 puntos).
- La auditoría SEO de la AI actual identifica problemas concretos (1.5 puntos).
- El rediseño aplica correctamente principios de AI y SEO (2 puntos).
- El sitemap visual y el diagrama de enlazado interno son claros y útiles (1.5 puntos).
- El sitemap XML está correctamente formado y es válido (1 punto).
- Los datos estructurados JSON-LD son correctos y variados (1 punto).
- El informe final está bien estructurado y es convincente (1.5 puntos).

### Actividad de ampliación 2: Diseño de una mega-navegación para un portal de contenidos masivos

**Contexto:** Los portales de contenidos masivos (grandes publishers de noticias, plataformas de streaming de vídeo, agregadores de contenido) enfrentan el desafío de organizar decenas de miles de piezas de contenido en estructuras navegables. Esta actividad aborda el diseño de sistemas de navegación avanzados para grandes volúmenes de información.

**Objetivos:**

- Investigar los patrones de navegación diseñados para grandes volúmenes de contenido: mega menús (tipos: dropdown simple, mega dropdown con columnas, mega dropdown con contenido destacado), navegación facetada avanzada (facetas dinámicas, facetas dependientes, rangos con histogramas), tag clouds y sistemas de etiquetado colaborativo (folksonomías), búsqueda predictiva con categorización de sugerencias, y sistemas de recomendación que actúan como navegación (recomendaciones basadas en historial, en similitud, en tendencias).
- Proponer un caso de estudio: un portal de streaming de cursos online con 10.000+ cursos organizados en 50+ categorías, con múltiples instructores, niveles de dificultad, idiomas, duraciones, valoraciones, y precios.
- Diseñar la AI del portal incluyendo: estructura jerárquica de categorías (con al menos 3 niveles de profundidad, 6-8 categorías de nivel 1), sistema de mega menú (dibujar su estructura: columnas, contenido destacado, acceso rápido), sistema de navegación facetada para la búsqueda/exploración de cursos (definir facetas, sus valores, y cómo se generan dinámicamente), y sistema de recomendaciones que aparecen en diferentes puntos del sitio (home, página de curso, carrito).
- Crear wireframes de las pantallas clave: mega menú desplegado, página de resultados de búsqueda con facetas aplicadas, página de detalle de curso con recomendaciones contextuales.
- Evaluar tu diseño aplicando los principios de AI estudiados: ¿respeta el equilibrio profundidad-amplitud? ¿las etiquetas son claras y consistentes? ¿están contempladas las 3 preguntas fundamentales (dónde estoy, qué hay aquí, a dónde puedo ir)?
- Redactar una reflexión sobre cómo el volumen de contenidos (10.000+ items) afecta a las decisiones de AI en comparación con un sitio de tamaño medio (100-500 páginas).

**Formato de entrega:** Documento de especificación de AI del portal (estructura de categorías, especificación del mega menú, especificación de facetas, diagrama del sistema de recomendaciones), wireframes de las pantallas clave, y ensayo reflexivo (1000-1500 palabras).

**Rúbrica de evaluación:**

- La investigación sobre patrones de navegación para grandes volúmenes es completa (1.5 puntos).
- La estructura de categorías es lógica, respeta la regla de 7±2 en cada nivel y tiene profundidad controlada (1.5 puntos).
- El mega menú está bien especificado y es navegable (1.5 puntos).
- La navegación facetada es completa, usable y contempla la generación dinámica de facetas (2 puntos).
- Los wireframes son claros e incluyen los elementos de navegación descritos (1.5 puntos).
- La evaluación contra los principios de AI es honesta y revela puntos de mejora (1 punto).
- La reflexión sobre el impacto del volumen de contenidos en las decisiones de AI es perspicaz (1 punto).

### Actividad de ampliación 3: Auditoría de accesibilidad de la navegación y propuesta de mejora

**Contexto:** La accesibilidad web es un requisito legal en la Unión Europea (Directiva 2016/2102 y Real Decreto 1112/2018 en España) para todos los sitios web del sector público y para muchos del sector privado. Los sistemas de navegación son componentes críticos para la accesibilidad, ya que si un usuario no puede navegar por el sitio, no puede acceder a ningún contenido, por muy accesible que este sea individualmente.

**Objetivos:**

- Investigar los requisitos de accesibilidad específicos para sistemas de navegación según WCAG 2.1 nivel AA: criterios relacionados con la navegación (2.4.1 Saltar bloques, 2.4.2 Titulado de páginas, 2.4.3 Orden del foco, 2.4.4 Propósito de los enlaces, 2.4.5 Múltiples vías, 2.4.6 Encabezados y etiquetas, 2.4.7 Foco visible, 2.4.8 Ubicación, 3.2.3 Navegación consistente, 3.2.4 Identificación consistente).
- Seleccionar 3 sitios web de diferentes categorías (uno institucional, uno ecommerce, uno de noticias) y realizar una auditoría de accesibilidad de sus sistemas de navegación centrada exclusivamente en los criterios de navegación de WCAG 2.1.
- Para cada sitio, evaluar sistemáticamente: ¿tiene un enlace para saltar al contenido principal (skip to content)? ¿los menús son operables con teclado (Tab, Enter, Escape para cerrar submenús)? ¿el orden de tabulación es lógico y sigue el orden visual? ¿las etiquetas de enlace describen claramente su destino? ¿existen múltiples formas de llegar al mismo contenido (búsqueda, navegación, sitemap, breadcrumbs)? ¿la navegación es consistente en todas las páginas? ¿los elementos con foco tienen un indicador visual claramente visible?
- Documentar los problemas encontrados con capturas de pantalla y referencias al criterio WCAG infringido.
- Para los problemas más graves, diseñar soluciones de rediseño: crear wireframes o mockups que muestren la navegación corregida y redactar el código HTML/CSS/ARIA necesario para implementar las correcciones.
- Implementar al menos un ejemplo de navegación accesible funcional (puede ser un menú principal, un breadcrumb, o una barra de búsqueda) en HTML, CSS y JavaScript vanilla, que cumpla con los criterios WCAG evaluados.
- Redactar un informe de auditoría profesional que pueda ser entregado a los responsables de cada sitio web.

**Formato de entrega:** Informe de auditoría de accesibilidad de navegación (los 3 sitios analizados con hallazgos WCAG y soluciones propuestas), wireframes o mockups de las soluciones de rediseño, implementación funcional de un componente de navegación accesible (HTML/CSS/JS), y ensayo reflexivo sobre la relación entre AI y accesibilidad.

**Rúbrica de evaluación:**

- La investigación sobre WCAG para navegación es correcta y completa (1.5 puntos).
- La auditoría de los 3 sitios es sistemática y documenta hallazgos específicos con referencias WCAG (2 puntos).
- Los problemas identificados son reales y relevantes (1.5 puntos).
- Las soluciones de rediseño son viables y resuelven los problemas detectados (1.5 puntos).
- La implementación del componente de navegación accesible es funcional y cumple WCAG (2 puntos).
- El informe de auditoría es profesional y accionable (1 punto).
- La reflexión sobre AI y accesibilidad demuestra comprensión de la interdependencia entre ambas disciplinas (0.5 puntos).

## Buenas prácticas

**Diseña a partir del usuario, no del organigrama.** La arquitectura de la información debe diseñarse a partir de las necesidades y modelos mentales de los usuarios, no de la estructura interna de la organización. Un error clásico es organizar la web de una universidad según su organigrama (Vicerrectorado de Ordenación Académica, Vicerrectorado de Estudiantes, Vicerrectorado de Investigación) en lugar de según las tareas que los usuarios quieren realizar (Matricularse, Consultar notas, Solicitar beca, Buscar máster). La técnica de **Card Sorting** es la herramienta principal para descubrir los modelos mentales de los usuarios y evitar imponer estructuras organizativas internas que solo tienen sentido para quienes trabajan dentro de la institución.

**La consistencia en la navegación es un principio no negociable.** La navegación global debe aparecer en el **mismo lugar, con el mismo orden y con las mismas etiquetas** en todas las páginas del sitio. Cualquier variación (un menú que cambia de posición, una etiqueta que se modifica al cambiar de sección, un orden de opciones que se altera) desorienta al usuario y le obliga a reaprender la interfaz en cada página. La navegación local debe ser consistente dentro de cada sección, aunque puede variar entre secciones diferentes (la navegación local de "Productos" es diferente de la de "Soporte", y eso es esperable y correcto).

**El etiquetado debe probarse con usuarios.** Lo que para el equipo de diseño es obvio puede no serlo para los usuarios. Etiquetas como "Soluciones", "Recursos", "Área personal" o "Dashboard" son ambiguas y significan cosas diferentes para diferentes personas. Las pruebas de etiquetado (presentar una etiqueta y preguntar «¿qué esperarías encontrar si haces clic aquí?») son **rápidas, baratas y revelan discrepancias** entre el lenguaje del emisor y el del receptor. El etiquetado también debe considerar el **SEO**: las etiquetas de navegación son señales potentes para los motores de búsqueda sobre el contenido del sitio.

!!! tip "Equilibra profundidad y amplitud"
    - **Estructuras muy profundas** (muchos niveles con pocas opciones en cada uno) obligan al usuario a hacer muchos clics, aumentando la probabilidad de abandono.
    - **Estructuras muy anchas** (muchas opciones en el primer nivel) abruman al usuario con demasiadas alternativas simultáneas, dificultando la decisión.
    - La **regla de los 7±2** gobierna la amplitud y la **regla de los 3 clics** la profundidad: no son leyes físicas sino **heurísticas** que deben aplicarse con criterio, considerando el contexto específico del sitio y las capacidades de sus usuarios.

**Diseña para la peor condición de uso, no para la mejor.** Hay que asumir que algunos usuarios tendrán conexiones lentas, pantallas pequeñas, poca experiencia digital, o discapacidades que afecten a su interacción con la interfaz. La navegación debe funcionar **sin JavaScript** (o con un *fallback* razonable), **sin CSS** (el orden del contenido en el HTML debe ser lógico), **sin ratón** (solo con teclado), y con **lectores de pantalla** (atributos ARIA correctos). Diseñar para los casos extremos produce una navegación más robusta que funciona para todos.

**Documenta y mantén la AI como entregable vivo.** El sitemap, los *wireframes* y los *user flows* no son documentos que se crean al inicio del proyecto y se archivan; deben actualizarse a medida que el proyecto evoluciona, reflejando los cambios en la estructura de contenidos y en la navegación. **Un sitemap desactualizado es peor que no tener sitemap**, porque induce a error a los nuevos miembros del equipo que lo consulten confiando en su vigencia.

## Errores frecuentes

!!! warning "El error más común: el «espejo de la organización»"
    Diseñar la estructura del sitio basándose en la **organización interna** de la empresa o institución en lugar de en las tareas y modelos mentales de los usuarios. Este error, conocido como ***org-chart mirroring***, produce categorías como «Departamento Comercial», «División de Operaciones» y «Recursos Corporativos» que tienen sentido para los empleados pero no para los clientes. El resultado es que **los usuarios no encuentran lo que buscan** porque no saben qué departamento gestiona cada cosa. **Solución:** invertir tiempo en investigación de usuarios (Card Sorting, entrevistas, análisis de *logs* de búsqueda) para construir la estructura desde la perspectiva del usuario.

**Etiquetas ambiguas, creativas o excesivamente marketinianas.** Etiquetas como «Descubre», «Inspírate», «Vive la experiencia» o «Soluciones innovadoras» no comunican qué contenido se encontrará al hacer clic. Las etiquetas deben ser **informativas y descriptivas**, priorizando la claridad sobre la creatividad. Si existe una palabra que el **95%** de los usuarios entiende (por ejemplo, «Ayuda»), no debe reemplazarse por una alternativa más creativa pero menos clara (por ejemplo, «Centro de conocimiento»).

**Estructuras de navegación excesivamente profundas.** Es un error que penaliza tanto la usabilidad como el **SEO**. Cuando un contenido está a **5, 6 o 7 clics** de la página de inicio, es prácticamente invisible tanto para los usuarios como para los motores de búsqueda (que interpretan la profundidad como una señal de baja importancia). La solución suele pasar por **aplanar la jerarquía**: reducir el número de niveles reorganizando los contenidos, utilizando *mega menús* que expongan la estructura hasta el nivel 3 desde cualquier página, y complementando con navegación contextual y búsqueda.

**Ignorar la navegación en dispositivos móviles.** Es un error con consecuencias graves en la actualidad, cuando **más del 50% del tráfico web** proviene de dispositivos móviles. Diseñar una navegación compleja pensando solo en el escritorio (donde hay espacio de sobra) y luego intentar «adaptarla» al móvil suele resultar en menús inutilizables. El enfoque correcto es **mobile-first**: diseñar primero la navegación para la pantalla más restrictiva, asegurándose de que es usable en ese contexto, y luego expandirla para pantallas más grandes aprovechando el espacio adicional.

**No proporcionar múltiples vías de acceso al mismo contenido.** Penaliza a usuarios con diferentes estrategias de navegación: unos prefieren explorar mediante menús jerárquicos; otros van directamente a la barra de búsqueda; otros utilizan los *breadcrumbs*; otros siguen enlaces contextuales. Limitar el acceso a una única vía (por ejemplo, solo mediante el menú) excluye a los usuarios que operan con estrategias diferentes. Una buena AI proporciona **redundancia funcional**: el mismo contenido debe ser accesible mediante **navegación, búsqueda y enlaces contextuales**.

**Diseñar *wireframes* sin anotaciones.** Genera malentendidos entre diseño y desarrollo. Un *wireframe* que muestra un formulario con todos los campos correctamente rellenados no comunica cómo debe verse ese formulario cuando hay errores de validación, cuando está cargando, o cuando se ha enviado correctamente. Las anotaciones son el **canal de comunicación** entre quien diseña la estructura y quien la implementa, y su ausencia es fuente de iteraciones innecesarias y resultados inconsistentes.

## Resumen

La Arquitectura de la Información es la disciplina que da sentido y estructura a los contenidos digitales, garantizando que los usuarios puedan encontrar lo que buscan y comprender lo que encuentran. Sus cuatro pilares fundamentales —sistemas de organización, etiquetado, navegación y búsqueda— proporcionan un marco sistemático para analizar y diseñar la dimensión estructural de cualquier interfaz web. Las herramientas principales para el diseño de la AI incluyen: los sitemaps para representar la estructura jerárquica del sitio, los wireframes para visualizar la disposición espacial de los contenidos en cada página, los user flows para modelar los recorridos del usuario a través de la interfaz, y los mapas de navegación para documentar los diferentes sistemas de navegación que coexisten en el sitio.

Las técnicas de investigación con usuarios, especialmente el Card Sorting y el Tree Testing, permiten fundamentar las decisiones de AI en evidencia empírica sobre los modelos mentales de los usuarios, en lugar de en suposiciones del equipo de diseño. La aplicación de principios como la regla de 7±2, la regla de los 3 clics, el equilibrio entre profundidad y amplitud, y la consistencia de etiquetas y navegaciones, contribuye a crear estructuras intuitivas que reducen la carga cognitiva del usuario. La AI no es una fase inicial del proyecto que se supera, sino una disciplina continua que debe acompañar la evolución del producto digital, adaptándose a nuevos contenidos, nuevas funcionalidades y nuevas necesidades de los usuarios.

## Recursos complementarios

- **Information Architecture for the World Wide Web (4th Edition) - Louis Rosenfeld, Peter Morville, Jorge Arango:** El libro de referencia canónico sobre arquitectura de la información, conocido como "el libro del oso polar". Cubre en profundidad todos los conceptos de la unidad. O'Reilly Media, 2015.
- **How to Make Sense of Any Mess - Abby Covert:** Un libro breve y práctico sobre cómo aplicar el pensamiento de la arquitectura de la información a cualquier problema de organización de información. Disponible en http://www.howtomakesenseofanymess.com
- **Optimal Workshop:** Plataforma de herramientas de investigación de UX que incluye OptimalSort (Card Sorting), Treejack (Tree Testing) y Chalkmark (pruebas de primer clic). Versiones gratuitas limitadas disponibles para uso educativo. https://www.optimalworkshop.com
- **Miro:** Pizarra colaborativa online con plantillas específicas para sitemaps, user flows, wireframes y card sorting. Plan gratuito para educación disponible. https://miro.com/templates
- **Figma / FigJam:** FigJam, la pizarra colaborativa de Figma, incluye plantillas y herramientas para sitemaps, user flows, wireframes de baja fidelidad y sesiones de card sorting colaborativas. Plan gratuito educativo disponible. https://www.figma.com/figjam
- **Lucidchart:** Herramienta de diagramación profesional con plantillas para sitemaps, user flows, diagramas de navegación y wireframes. Capa gratuita con limitaciones. https://www.lucidchart.com
- **Balsamiq Wireframes:** Herramienta especializada en wireframes de baja fidelidad con un estilo deliberadamente "sketchy" que comunica que se trata de un trabajo en progreso. Ideal para primeras fases. Versión de prueba disponible. https://balsamiq.com
- **XML Sitemaps Generator:** Herramienta gratuita para generar sitemaps XML para motores de búsqueda. Útil para entender la diferencia entre sitemaps visuales y XML. https://www.xml-sitemaps.com
- **NNGroup (Nielsen Norman Group) - Articles on Information Architecture:** La consultora de UX más prestigiosa del mundo ofrece artículos gratuitos de alta calidad sobre todos los temas de AI. Buscar "information architecture" en https://www.nngroup.com/articles
- **MeasuringU - Tree Testing Articles:** Artículos técnicos sobre metodología y análisis de Tree Testing, incluyendo interpretación de métricas. Buscar "tree testing" en https://measuringu.com
- **A11Y Project - Navigation Patterns:** Recursos sobre patrones de navegación accesibles, con ejemplos de código HTML/CSS/JS que cumplen WCAG. https://www.a11yproject.com/patterns
