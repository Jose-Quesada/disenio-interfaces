---
icon: lucide/pen-tool
---

# Unidad 5: Figma Profesional para Desarrolladores Frontend

## Objetivos de aprendizaje

Al finalizar esta unidad, el alumnado dominará Figma como herramienta profesional de diseño de interfaces, no desde la perspectiva del diseñador gráfico, sino desde el enfoque del desarrollador frontend que necesita interpretar especificaciones de diseño, extraer valores precisos (colores, tipografías, espaciados, dimensiones), comprender la arquitectura de componentes y colaborar eficazmente con equipos de diseño. El estudiante aprenderá a navegar con soltura por la interfaz de Figma, crear y manipular frames con constraints y auto layout, construir componentes reutilizables con variantes y propiedades, organizar bibliotecas de componentes compartidas entre proyectos, y crear prototipos interactivos que comuniquen la intención de diseño antes de escribir una sola línea de código. Un objetivo fundamental es que el alumno sea capaz de utilizar el Modo Desarrollo (Dev Mode) para extraer especificaciones técnicas precisas (código CSS, medidas, assets exportables) y comprender cómo se estructuran los design tokens en Figma para facilitar la traducción del diseño a código. Se espera que, al completar la unidad, el estudiante pueda diseñar de forma autónoma una interfaz web completa en Figma, desde los wireframes iniciales hasta un prototipo interactivo de alta fidelidad, aplicando buenas prácticas de naming, organización y atomic design.

## Relación con los Resultados de Aprendizaje

Esta unidad se vincula directamente con los Resultados de Aprendizaje oficiales del módulo 0615 *Diseño de interfaces web* (RD 405/2023, BOE; currículo andaluz):

- **RA1. Planifica la creación de una interfaz web valorando y aplicando especificaciones de diseño.** Figma es la herramienta de prototipado y wireframing más utilizada en la industria actual; el dominio de sus funcionalidades permite al alumnado materializar las especificaciones de diseño en prototipos validables antes de abordar la implementación técnica (CE 1.f).
- **RA2. Crea interfaces web homogéneos definiendo y aplicando estilos.** El alumno extrae desde Figma los valores de estilos (colores, tipografías, dimensiones) que aplicará posteriormente en HTML y CSS; las bibliotecas de componentes y los tokens de diseño son la manifestación práctica de un sistema visual coherente en la fase de diseño (CE 2.g).
- **RA5. Desarrolla interfaces web accesibles, analizando las pautas establecidas y aplicando técnicas de verificación.** El uso de plugins como Stark o A11y permite validar contrastes y simular condiciones de accesibilidad directamente sobre el diseño en Figma (CE 5.f).

## Conocimientos previos

Para el adecuado aprovechamiento de esta unidad, el alumnado debe poseer fundamentos sólidos de diseño de interfaces web, incluyendo comprensión de los principios de jerarquía visual, teoría del color aplicada a pantalla, tipografía digital, sistemas de rejilla y espaciado, y patrones de diseño de interacción comunes. Es necesario que el estudiante conozca los conceptos de diseño responsive y las diferencias de comportamiento entre dispositivos móviles, tabletas y escritorio, ya que en Figma se trabaja con frames que representan estas diferentes resoluciones. Resulta conveniente que el alumno haya tenido contacto previo con alguna herramienta de diseño vectorial (Illustrator, Sketch, Inkscape) para comprender conceptos como capas, grupos, formas vectoriales y operaciones booleanas. También es recomendable tener experiencia con CSS Flexbox, ya que Auto Layout en Figma se basa en los mismos principios y la correspondencia entre ambos es muy directa. No se requieren conocimientos previos de Figma específicamente, ya que la unidad comienza desde cero y cubre desde la creación de una cuenta gratuita hasta técnicas avanzadas de prototipado. Sin embargo, se espera del alumno una actitud exploratoria y proactiva hacia el aprendizaje de herramientas digitales complejas.

## Contenidos

1. Introducción a Figma: naturaleza colaborativa basada en navegador, comparativa con Sketch y Adobe XD, modelo freemium y planes de suscripción.
2. Interfaz de usuario: barra de herramientas principal, panel de capas y páginas, panel de propiedades, canvas y técnicas de navegación, panel de assets y componentes, modo prototipo y Dev Mode.
3. Frames y Constraints: el frame como unidad fundamental de diseño, diferencias con grupos, presets de dispositivos, comportamiento responsive mediante constraints, frames anidados y su correspondencia con HTML.
4. Auto Layout: fundamentos del layout automático en Figma, dirección horizontal y vertical, gap y padding, modos de resizing (fixed, hug contents, fill container), wrapping, aplicación práctica en componentes UI.
5. Sistema de Variables: variables de color, número, string y booleano, variables locales versus publicadas en bibliotecas, modos para theming claro/oscuro, scoping por tipo de propiedad, relación con tokens de diseño.
6. Componentes: creación desde cero, patrones de instanciación, overrides permitidos, propiedades de componente (variantes, texto, boolean, instance swap), slots de contenido.
7. Variantes: concepto y propósito, nomenclatura slash para jerarquías de propiedades, combinación de propiedades para matrices multidimensionales, ejemplos con botones, inputs y cards.
8. Bibliotecas de componentes: publicación en equipo, consumo entre archivos, flujo de actualizaciones, branching y control de versiones.
9. Prototipado interactivo: creación de conexiones entre frames, triggers y acciones, tipos de animación (instant, dissolve, smart animate, move in/out), overlays, scroll position, interactive components.
10. Exportación y especificaciones: formatos de exportación, configuración por capa, exportación masiva, Dev Mode para desarrolladores.
11. Plugins útiles para frontend: Iconify, Unsplash, Content Reel, Stark, A11y, Lorem Ipsum.
12. Proyecto guiado completo: aplicación Kanban de gestión de tareas.
13. Buenas prácticas: convenciones de nomenclatura, organización de páginas, atomic design en Figma, grid de 8 puntos.

## Desarrollo teórico

### Figma como herramienta colaborativa de diseño de interfaces

!!! info "Definición: Figma"
    **Figma** es la primera herramienta profesional de diseño de interfaces que funciona **completamente en el navegador**, sin necesidad de instalación ni de sincronización manual de archivos. Esta decisión arquitectónica, que en **2016** parecía arriesgada frente a competidores consolidados como **Sketch** (que requería macOS y plugins de sincronización como Abstract) o **Adobe XD** (con su modelo de aplicación nativa), se ha revelado como su ventaja competitiva más diferencial.

La naturaleza basada en navegador permite la **colaboración en tiempo real**: múltiples diseñadores y desarrolladores pueden trabajar simultáneamente sobre el mismo archivo, viendo los cambios de los demás en directo, de forma análoga a como **Google Docs** transformó la edición de documentos de texto.

Para el desarrollador frontend, esta característica elimina uno de los puntos de fricción más persistentes en los flujos de trabajo tradicionales: la **desincronización** entre el archivo de diseño y lo que ve el desarrollador. Con Figma, el desarrollador accede siempre a la versión más reciente del diseño simplemente abriendo el enlace del archivo, sin necesidad de descargar archivos, gestionar versiones ni preocuparse por tener la aplicación actualizada.

!!! tip "Modo Desarrollo (Dev Mode)"
    El **Modo Desarrollo (Dev Mode)**, introducido en **2023**, proporciona una vista específicamente diseñada para desarrolladores que muestra medidas, especificaciones **CSS**, *assets* exportables y anotaciones de diseño en un formato optimizado para la implementación técnica. El desarrollador puede seleccionar cualquier elemento en el canvas y obtener inmediatamente sus dimensiones, distancias a otros elementos, estilos de texto, colores en múltiples formatos y sugerencias de código **CSS**, **Tailwind** o **SwiftUI**.

Figma no es solo una herramienta de diseño de alta fidelidad; cubre el **espectro completo** del proceso de diseño de interfaces, desde los primeros *wireframes* de baja fidelidad hasta los prototipos interactivos completamente funcionales. El **modelo freemium** permite que cualquier persona pueda crear una cuenta gratuita y empezar a diseñar inmediatamente, con limitaciones razonables en el número de archivos y páginas que no impiden el aprendizaje ni la realización de proyectos de tamaño medio. Esto convierte a Figma en la herramienta ideal para el contexto educativo del módulo de Diseño de Interfaces Web.

### La interfaz de Figma: un recorrido por sus paneles fundamentales

Al abrir Figma, el usuario se encuentra con un lienzo infinito (el canvas) que constituye el espacio de trabajo principal. A diferencia de otras herramientas de diseño que imponen límites de página o mesa de trabajo, el canvas de Figma es ilimitado en todas las direcciones, lo que fomenta la exploración y el trabajo iterativo sin restricciones espaciales. Es común que los diseñadores coloquen exploraciones alternativas, versiones descartadas, moodboards y anotaciones en los márgenes del canvas, creando un espacio de trabajo orgánico donde el proceso de diseño es visible y trazable.

La barra de herramientas principal, situada en la parte superior de la ventana, contiene las herramientas de creación y manipulación organizadas de izquierda a derecha:

- **Selección** (tecla **V**) — herramienta por defecto y la más utilizada.
- **Marco o frame** (tecla **F**) — crea contenedores que representan pantallas, secciones o componentes.
- **Formas básicas** (tecla **R** rectángulo, **O** elipse, **L** línea) — además de polígono y estrella.
- **Pluma** (tecla **P**) — trazados vectoriales complejos; también el lápiz para dibujo libre.
- **Texto** (tecla **T**) — crea capas de texto.
- **Mano** (tecla **H**) — navega por el canvas arrastrando.
- **Comentarios** — revisión colaborativa; y el botón de **presentación** para previsualizar prototipos a pantalla completa.

El panel izquierdo alberga la jerarquía de capas, donde se muestran todas las páginas del documento y, dentro de cada página, todos los objetos organizados jerárquicamente. Una característica importante de Figma es que el orden de las capas en el panel es visual: las capas superiores en el panel aparecen por delante de las inferiores en el canvas. Esto contrasta con herramientas como Photoshop donde "capa superior" significa "más arriba en el panel pero más abajo visualmente". En Figma, lo que está más arriba en la lista de capas está al frente visualmente, lo cual es más intuitivo para quienes provienen del desarrollo web.

El panel derecho es contextual y muestra las propiedades del objeto seleccionado. Se divide en tres pestañas principales:

- **Design** — propiedades visuales: posición (**X**, **Y**), tamaño (**W**, **H**), rotación, opacidad, rellenos (*fills*), bordes (*strokes*), efectos (sombras, *blurs*) y tipografía.
- **Prototype** — configuración de conexiones interactivas entre frames.
- **Dev Mode** — especificaciones técnicas para desarrolladores.

Adicionalmente, en la parte inferior del panel izquierdo se encuentra el panel de **Assets**, que lista los componentes locales del archivo y las bibliotecas de componentes compartidos disponibles en el equipo, permitiendo arrastrarlos directamente al canvas.

### Frames y Constraints: la base del diseño responsive en Figma

!!! info "Definición: frame"
    El **frame** es el concepto fundamental sobre el que se construye cualquier diseño en Figma. Es un **contenedor que delimita un área de diseño** y puede comportarse como una pantalla completa cuando se le asigna un *preset* de dispositivo (por ejemplo, **iPhone 14: 390×844 px**, **iPad Pro 11: 834×1194 px**, **Desktop 1440: 1440×1024 px**) o como una sección dentro de una pantalla más grande.

Frente a un **grupo** (*Group*), que simplemente agrupa objetos visualmente sin afectar a su comportamiento, un frame ofrece capacidades reales de layout:

- **Sistema de coordenadas propio** para cada contenedor.
- **Recorte de contenido** (*clip content*).
- **Referencia para constraints y Auto Layout.**
- **Anidación** formando jerarquías complejas que reflejan la estructura de componentes de una interfaz real.

Cuando creamos un frame presionando la tecla **F** y seleccionando un *preset* de dispositivo, Figma establece automáticamente el tamaño del frame y nos permite añadir elementos hijos en su interior. Una práctica recomendada es comenzar siempre con frames que representen los *breakpoints* principales de nuestro diseño responsive: un frame de **375 px** de ancho para móvil, uno de **768 px** para tablet y uno de **1440 px** para escritorio. Esto nos obliga a pensar en cómo el diseño se adapta a diferentes tamaños de pantalla desde el inicio del proceso.

Los **constraints** (restricciones) son el mecanismo que Figma proporciona para simular el comportamiento responsive de los elementos dentro de un frame. Cuando un objeto hijo se posiciona dentro de un frame, se le pueden asignar constraints que definen cómo debe comportarse cuando el frame padre cambia de tamaño. Las opciones incluyen: fijado a la izquierda (**Left**), a la derecha (**Right**), centrado horizontalmente (**Center**), escalado horizontal (**Scale**), fijado arriba (**Top**), abajo (**Bottom**), centrado verticalmente, o combinaciones. Por ejemplo, un botón de *submit* en un formulario puede configurarse con constraints **Right + Bottom** para permanecer siempre en la esquina inferior derecha del formulario independientemente de cómo se redimensione.

Para un desarrollador frontend, comprender los constraints es esencial porque se traducen directamente a **CSS**:

| Constraint en Figma | Equivalente en CSS |
|---------------------|--------------------|
| **Left + Right** con ancho fijo | `margin: 0 auto;` + `width: Xpx;` |
| **Left + Right** con escalado (**Scale**) | `width: 100%;` |
| **Top + Bottom** | `height: 100%` con posicionamiento relativo |

Esta correspondencia directa permite al desarrollador extraer del diseño Figma no solo los valores estáticos sino la **intención responsive completa**, acelerando la implementación.

### Auto Layout: el motor de flexibilidad de Figma

!!! info "Definición: Auto Layout"
    **Auto Layout** es probablemente la funcionalidad de Figma que más impacto tiene en la productividad del diseño de interfaces y en la facilidad de traducción a código. Aplica automáticamente reglas de layout similares a **CSS Flexbox** a los objetos contenidos en un frame, permitiendo que se distribuyan horizontal o verticalmente, con espaciados consistentes, *paddings* uniformes y comportamientos de redimensionamiento dinámico. La activación se realiza mediante el atajo **Shift+A** o desde el botón correspondiente en el panel de propiedades.

La configuración de Auto Layout sigue cuatro parámetros:

- **Dirección** — horizontal (los elementos se disponen en fila, de izquierda a derecha) o vertical (en columna, de arriba a abajo).
- **Gap** (*spacing between items*) — el espaciado entre elementos, el equivalente exacto a la propiedad CSS **gap**.
- **Padding** — el interior del frame, configurable de forma independiente para cada uno de los cuatro lados o de forma uniforme.
- **Alineación** — en el eje principal (**justify-content** en CSS) al inicio, al centro o al final, y en el eje secundario (**align-items** en CSS) con las mismas opciones.

El comportamiento de redimensionamiento de cada elemento hijo dentro de un Auto Layout se controla mediante tres modos:

| Modo de resizing | Comportamiento | Equivalente en CSS |
|------------------|----------------|--------------------|
| **Fixed width/height** | el elemento mantiene un tamaño fijo definido en píxeles | `width` / `height` fijos |
| **Hug contents** | el elemento se ajusta al tamaño de su contenido | `width: fit-content` |
| **Fill container** | el elemento se expande para ocupar todo el espacio disponible | `flex: 1` |

Esta triple configuración permite crear componentes flexibles que se comportan correctamente cuando cambia su contenido o el tamaño de su contenedor, exactamente como ocurre en la web real.

La funcionalidad de ***wrapping*** (`wrap`), introducida a finales de **2023**, permite que los elementos fluyan a la siguiente línea cuando no caben en el ancho del contenedor, de forma análoga a **flex-wrap: wrap**. Esto es particularmente útil para diseñar listas de etiquetas (*chips*), *grids* de tarjetas adaptativos o colecciones de elementos que deben reorganizarse según el ancho disponible. Configurar *wrap* en un Auto Layout horizontal con *Fill container* en los elementos hijos crea automáticamente un layout de columnas flexibles similar a **auto-fill** en CSS Grid.

La correspondencia entre Auto Layout y CSS Flexbox es tan directa que Figma la aprovecha en Dev Mode para generar fragmentos de código CSS. Un frame con Auto Layout horizontal, *spacing* de **16 px**, *padding* uniforme de **24 px** y alineación centrada se traduce automáticamente a **display: flex; flex-direction: row; gap: 16px; padding: 24px; align-items: center**. Esta transparencia en la traducción diseño-código es una de las razones por las que los equipos de desarrollo valoran Figma como herramienta puente entre diseño e ingeniería.

### Sistema de variables en Figma

!!! info "Definición: variables de diseño"
    El **sistema de variables** de Figma, introducido en **junio de 2023** durante la conferencia **Config**, representa la incorporación nativa del concepto de **tokens de diseño** a la herramienta. Las variables permiten almacenar valores reutilizables que pueden aplicarse a propiedades de diseño como colores de relleno, colores de borde, tipografías, dimensiones, radios de borde y espaciados. El panel de variables, accesible desde el menú principal o desde el panel derecho en cualquier propiedad compatible, muestra todas las variables definidas en el archivo organizadas en **colecciones**.

Las variables pueden ser **locales** (definidas y utilizadas exclusivamente en el archivo actual) o **publicarse como biblioteca** para ser consumidas desde otros archivos del equipo. Esta distinción es fundamental: las variables locales son útiles para exploraciones, prototipos rápidos y trabajo individual, mientras que las variables publicadas constituyen la **fuente única de verdad** de los tokens de diseño de la organización. Cuando una variable publicada se modifica en el archivo origen, todos los archivos que la consumen reciben una notificación de actualización, exactamente igual que con los componentes compartidos.

Figma soporta **cuatro tipos de variables**:

| Tipo | Almacena | Uso típico |
|------|----------|------------|
| **Color** | valores en cualquier espacio de color, incluida la transparencia (*alpha*) | rellenos, bordes y efectos |
| **Número** | valores numéricos con o sin unidad (**px**, **rem**, **%**) | dimensiones, espaciados, radios, opacidades, grosores de borde |
| **String** | cadenas de texto | contenidos dinámicos, etiquetas y textos de interfaz consistentes |
| **Boolean** | valores verdadero/falso | visibilidad de capas o grupos: activar o desactivar secciones completas de la interfaz |

Una de las funcionalidades más potentes del sistema de variables es el soporte para **modos** (*modes*). Los modos permiten definir conjuntos alternativos de valores para una misma variable dentro de una colección. El caso de uso canónico es el **theming**: una colección de variables de color puede tener un modo **Light** donde la variable *surface/background* vale **#FFFFFF** y un modo **Dark** donde vale **#1A1A1A**. Al cambiar el modo aplicado a un frame o a un conjunto de frames, todos los elementos que utilizan variables cambian automáticamente al conjunto de valores correspondiente, permitiendo previsualizar instantáneamente el tema oscuro o cualquier otra variación temática.

Los modos no están limitados a temas de color. Pueden utilizarse para:

- **Densidad de información** — modo *Compact* con espaciados reducidos frente a *Comfortable* con espaciados generosos.
- **Múltiples idiomas** en los textos de interfaz (modos **ES**, **EN**, **FR** con variables de *string*).
- **Marcas blancas** (*white-label*), donde se cambia la paleta de colores corporativos.
- **Resoluciones de dispositivo**, ajustando tamaños de fuente y espaciados.

Esta flexibilidad convierte el sistema de variables de Figma en una herramienta no solo de consistencia sino de **exploración y validación de escenarios de diseño**.

### Componentes, variantes y bibliotecas

!!! info "Definición: componente maestro e instancia"
    El **sistema de componentes** de Figma es el mecanismo que permite crear elementos reutilizables que mantienen coherencia en todo el diseño. Un componente se crea seleccionando uno o varios objetos y ejecutando el comando **Create component** (**Ctrl+Alt+K**). A partir de ese momento, el elemento original se convierte en el **componente maestro** (*main component*), identificado por un icono de **cuatro rombos rellenos**, y cualquier copia que se haga de él se convierte en una **instancia** (*instance*), identificada por un icono de **rombo vacío**.

La relación entre maestro e instancias es **unidireccional**: los cambios en el maestro se propagan a todas las instancias, pero las instancias pueden tener ***overrides*** (sobrescrituras) locales que no afectan al maestro.

Los *overrides* permiten personalizar aspectos específicos de una instancia sin romper el vínculo con el componente maestro. Por ejemplo, en un componente de tarjeta de producto, se puede sobrescribir la imagen, el título y el precio en cada instancia, pero el *layout*, la tipografía y los estilos se mantienen vinculados al maestro. Si posteriormente el equipo de diseño decide cambiar la tipografía de los títulos de tarjeta de **18 px** a **20 px**, basta con modificar el maestro para que todas las instancias que no tengan *override* de texto se actualicen automáticamente.

Las **propiedades de componente** son el mecanismo que permite exponer ciertos atributos del componente para que puedan modificarse desde el panel de propiedades sin necesidad de navegar por las capas internas. Existen **cuatro tipos**:

- **Variantes** — para seleccionar entre diferentes versiones del componente.
- **Texto** — para exponer capas de texto editables.
- **Boolean** — para mostrar u ocultar elementos, como un icono opcional.
- **Instance swap** — para permitir reemplazar un subcomponente por otro, por ejemplo cambiar el icono de un botón.

Las propiedades se definen en el componente maestro y aparecen como controles en el panel derecho cuando se selecciona cualquier instancia del componente.

Las **variantes** son un caso especial de propiedad de componente que permite agrupar múltiples componentes relacionados en un único conjunto con propiedades seleccionables.

!!! tip "Nomenclatura slash"
    Para crear variantes se utiliza la **nomenclatura slash** (barra diagonal): se nombra al componente con el formato **Propiedad=Valor**. Por ejemplo, un botón puede tener variantes nombradas como **Button/Size=Small**, **Button/Size=Medium**, **Button/Size=Large** y también **Button/Variant=Primary**, **Button/Variant=Secondary**, **Button/Variant=Danger**. Cuando se combinan múltiples propiedades (*slash* anidados), Figma genera automáticamente una **matriz de todas las combinaciones posibles**.

La transformación de componentes individuales en un conjunto de variantes se realiza seleccionando todos los componentes que se desea agrupar y ejecutando **Combine as variants**. Figma analiza los nombres de los componentes, extrae las propiedades y valores de la nomenclatura *slash*, y genera automáticamente tanto el conjunto de variantes como los controles de selección en el panel de propiedades. A partir de ese momento, cualquier instancia del conjunto de variantes puede cambiar entre todas las combinaciones disponibles simplemente usando los desplegables del panel de propiedades, sin necesidad de desconectar la instancia del componente maestro.

### Prototipado interactivo en Figma

!!! info "Definición: prototipo interactivo"
    El **prototipado** es la funcionalidad que transforma diseños estáticos en **experiencias interactivas simuladas**, permitiendo validar flujos de usuario, transiciones y microinteracciones antes de escribir código. Se configura en la pestaña **Prototype** del panel derecho y se basa en el establecimiento de **conexiones entre frames**. Cada conexión define un ***trigger*** (el evento que la activa), una **acción** (lo que ocurre) y una **animación** (cómo se transiciona visualmente).

Los *triggers* disponibles cubren la mayoría de interacciones web y móviles:

- **On click** — clic del ratón; **On hover** — el cursor se sitúa encima; **On press** — pulsación mantenida.
- **On drag** — arrastre; **Mouse enter** / **Mouse leave**.
- **After delay** — tras un tiempo configurable.
- **While hovering** y **While pressing** — comportamientos continuos mientras se mantiene la interacción.
- **On tap**, **On touch down** / **On touch up** — gestos táctiles para prototipado móvil.

Las acciones determinan qué sucede cuando se activa un *trigger*. La más común es **Navigate to**, que transiciona a otro frame del prototipo. El resto:

- **Open overlay** — abre un frame como capa superpuesta modal; **Swap overlay**, **Close overlay**.
- **Scroll to** — desplaza a una posición específica dentro de un frame con *scroll*.
- **Back** — retrocede al frame anterior.
- **Open link** — abre una URL externa.
- **Set variable** — modifica el valor de una variable de Figma en tiempo de prototipado, permitiendo crear **lógica condicional básica**.

Las animaciones entre frames pueden configurarse con diferentes comportamientos:

- **Instant** — transición sin animación: el frame de destino aparece inmediatamente.
- **Dissolve** — fundido cruzado entre ambos frames.
- **Smart Animate** — la animación más potente: Figma analiza los objetos con el **mismo nombre** en ambos frames y, si detecta cambios en sus propiedades (posición, tamaño, opacidad, color), genera automáticamente una transición animada entre los dos estados.
- **Move in / Move out** — desliza el frame entrante desde una dirección; **Slide in / Slide out** tiene un comportamiento similar.

Para cada animación se puede configurar la curva de aceleración (**ease in**, **ease out**, **ease in and out**, **linear**) y la duración en **milisegundos**.

!!! tip "Interactive components"
    Los **interactive components** (componentes interactivos) permiten encapsular comportamientos de prototipo dentro de variantes de un componente. Por ejemplo, un componente de botón puede tener variantes **Default**, **Hover**, **Pressed** y **Disabled**, con conexiones entre ellas que definan cómo transiciona entre estados al interactuar. Cuando este componente se utiliza como instancia en cualquier frame del prototipo, la interactividad ya está integrada **sin necesidad de configurar conexiones adicionales frame a frame**. Esto reduce drásticamente el trabajo de prototipado para componentes reutilizables y asegura consistencia en el comportamiento interactivo de toda la interfaz.

## Ejemplos guiados

### Ejemplo guiado 1: Creación de un frame para diseño de landing page responsive

En este primer ejercicio, configuraremos el espacio de trabajo para diseñar una landing page responsive utilizando frames que representan los tres breakpoints principales.

**Procedimiento paso a paso:**

1. Crea un nuevo archivo en Figma (Ctrl+N) y renómbralo como "Landing Page - Proyecto DAW" haciendo doble clic sobre "Untitled" en la barra superior.
2. Presiona la tecla F para activar la herramienta Frame. En el panel derecho, observa que aparecen presets de dispositivos a la derecha.
3. Selecciona el preset "Desktop - 1440 x 1024". Haz clic en el canvas para crear el frame. Renómbralo como "Desktop / Home" en el panel izquierdo haciendo doble clic sobre su nombre.
4. Presiona F de nuevo y selecciona "iPad Pro 11\" - 834 x 1194". Coloca este frame a la derecha del frame Desktop, dejando aproximadamente 200px de separación. Renómbralo como "Tablet / Home".
5. Presiona F una tercera vez y selecciona "iPhone 14 - 390 x 844". Colócalo a la derecha del frame Tablet. Renómbralo como "Mobile / Home".
6. Ajusta la altura de los frames Desktop y Tablet: selecciona el frame Desktop y en el panel derecho cambia su altura (H) a 4000px. Haz lo mismo con Tablet. El frame Mobile déjalo en 3000px.
7. Para cada uno de los tres frames, en el panel derecho, en la sección "Fill", añade un color de fondo blanco (#FFFFFF). Esto hará visible el área de diseño.
8. Organiza visualmente los frames en el canvas de forma que estén alineados horizontalmente. Selecciona los tres frames (shift+clic en cada uno) y utiliza las guías de alineación que aparecen automáticamente.
9. Guarda el archivo (Ctrl+S). Figma guarda automáticamente en la nube, pero este comando fuerza un guardado explícito.

Ahora tienes tres lienzos de diseño que representan los tres contextos de visualización principales. A medida que diseñes, debes ir completando los tres frames en paralelo para garantizar que el diseño funciona en todos los tamaños de pantalla.

### Ejemplo guiado 2: Diseño de un botón con Auto Layout y creación de componente con variantes

Aprenderemos a diseñar un sistema de botones completo utilizando Auto Layout para crear un componente flexible con múltiples variantes de tamaño, color y estado.

**Procedimiento paso a paso:**

1. En el canvas, presiona F para crear un frame pequeño (aproximadamente 300x300px) que nos servirá como área de trabajo para componentes. Renómbralo como "Componentes / Button".
2. Presiona T para la herramienta de texto y escribe "Button". Selecciona el texto y en el panel derecho configura: Inter, Medium, 14px, color blanco (#FFFFFF), alineación centrada.
3. Con el texto seleccionado, presiona Shift+A para convertir el texto en un Auto Layout frame. Observa que el texto ahora tiene un padding automático.
4. En el panel derecho, verifica que la dirección del Auto Layout está en Horizontal y la alineación en Center.
5. En la sección de Auto Layout, establece: Horizontal padding = 24px, Vertical padding = 12px. El gap déjalo en 0 (solo tenemos un elemento).
6. Ahora dale estilo al botón: en la sección Fill, selecciona un color azul (#2563EB). En la sección Stroke, no añadas borde. En la sección Effects, añade una sombra (Drop shadow) con los valores: X=0, Y=2, Blur=4, Spread=0, Color=#2563EB al 30% de opacidad.
7. En la sección de propiedades del frame, establece el Corner radius en 8px para las cuatro esquinas.
8. Verifica el comportamiento responsive del botón: selecciona el frame del botón y en Auto Layout, en la sección de resizing, cambia Width de "Fixed" a "Hug contents" y Height también a "Hug contents". Ahora el botón se ajustará automáticamente al tamaño del texto.
9. Con el botón seleccionado, presiona Ctrl+Alt+K para crear un Componente. El frame cambiará de color (borde púrpura) y aparecerá un icono de cuatro rombos rellenos indicando que es un componente maestro.
10. Renombra el componente maestro a "Button/Size=Medium/Variant=Primary/State=Default" utilizando la nomenclatura slash. Este nombre creará automáticamente tres propiedades de variante: Size, Variant y State.
11. Crea una instancia del componente: mantén pulsado Alt y arrastra el componente maestro a una posición vacía dentro del mismo frame de trabajo. Verás que la instancia tiene un icono de rombo vacío y al seleccionarla no puedes editar sus capas internas.
12. Vuelve al componente maestro (doble clic sobre él o búscalo en el panel Assets). Modifica el texto a "Button Large", cambia el Vertical padding a 16px y el Horizontal padding a 32px.
13. Renombra este nuevo componente como "Button/Size=Large/Variant=Primary/State=Default". Ahora tienes dos componentes que comparten las mismas propiedades pero con diferente valor de Size.
14. Repite el proceso para crear "Button/Size=Small/Variant=Primary/State=Default" con Vertical padding=8px, Horizontal padding=16px y font-size=12px.
15. Ahora crea la variante Secondary: duplica el Medium, cambia el Fill a transparente, añade un Stroke de 2px color #2563EB y cambia el color del texto a #2563EB. Renombra a "Button/Size=Medium/Variant=Secondary/State=Default".
16. Crea la variante Danger: duplica el Medium, cambia el Fill a #DC2626. Renombra a "Button/Size=Medium/Variant=Danger/State=Default".
17. Selecciona todos los componentes de botón que has creado y haz clic derecho > "Combine as variants". Figma analizará los nombres slash, extraerá las propiedades Size, Variant y State, y creará un conjunto de variantes unificado.
18. Verifica que en el panel derecho, al seleccionar el conjunto de variantes, aparecen controles desplegables para Size, Variant y State.
19. Prueba el conjunto: crea una instancia arrastrando Alt+clic sobre cualquiera de los botones del conjunto. En el panel derecho, usa los desplegables para cambiar entre tamaños, variantes y estados.

### Ejemplo guiado 3: Creación de un input de formulario con estados de validación

En este ejemplo crearemos un componente de campo de formulario con etiqueta, input, texto de ayuda y estados de error y éxito.

**Procedimiento paso a paso:**

1. Crea un nuevo frame de trabajo de aproximadamente 400x400px. Renómbralo como "Componentes / Input".
2. Presiona T y escribe "Email address". Configura la tipografía: Inter, Medium, 14px, color #374151. Este será el label.
3. Crea un rectángulo (R) de 320px de ancho por 44px de alto. Configura: Fill #FFFFFF, Stroke 1px color #D1D5DB, Corner radius 6px.
4. Coloca el rectángulo debajo del label. Selecciona ambos (label y rectángulo) y presiona Shift+A para crear un Auto Layout vertical.
5. Configura el Auto Layout: dirección Vertical, gap=6px, padding=0, alineación=Start. Renombra este frame como "Input Field / Base".
6. Añade texto de ayuda: dentro del Auto Layout, debajo del rectángulo, presiona T y escribe "We will never share your email with anyone else." Configura: Inter, Regular, 12px, color #6B7280.
7. El Auto Layout se expandirá automáticamente para incluir el nuevo texto gracias a la configuración Hug contents.
8. Ahora crea la variante con error. Duplica el frame completo (Ctrl+D). Cambia el color del borde del rectángulo a #DC2626 (rojo). Cambia el color del texto de ayuda a #DC2626 y el texto a "Please enter a valid email address."
9. Añade un icono de error: dentro del rectángulo del input, añade un pequeño círculo rojo de 16x16px con un signo de exclamación blanco. Colócalo a la derecha dentro del input, con padding derecho. Para esto necesitarás crear un Auto Layout horizontal dentro del rectángulo.
10. Renombra el primer componente maestro como "InputField/State=Default" y el segundo como "InputField/State=Error".
11. Crea una tercera variante para estado Success: duplica la Default, cambia el borde a #16A34A (verde), el texto de ayuda a "Email verified successfully" en color #16A34A.
12. Crea una cuarta variante para estado Disabled: duplica Default, baja la opacidad del rectángulo al 50%, cambia el Fill a #F3F4F6 y el texto de la etiqueta a color #9CA3AF.
13. Selecciona los cuatro componentes y haz "Combine as variants" para crear un conjunto de variantes unificado con la propiedad State.

### Ejemplo guiado 4: Diseño de una card de producto con Auto Layout y componentes anidados

Diseñaremos una card de producto completa utilizando Auto Layout, componentes anidados e intercambio de instancias.

**Procedimiento paso a paso:**

1. Crea un frame de trabajo de 500x600px. Renómbralo como "Componentes / Card".
2. Dentro, crea un rectángulo de 320x180px. Configura Fill con una imagen placeholder (en la sección Fill, selecciona "Image" y elige "Unsplash" si tienes el plugin, o usa un color gris claro #E5E7EB). Corner radius: 8px (solo esquinas superiores).
3. Debajo de la imagen, añade el contenido de la card: título del producto (T, 18px, Semibold, #111827), categoría (T, 12px, Medium, #6B7280, mayúsculas), descripción (T, 14px, Regular, #4B5563, dos líneas), precio (T, 24px, Bold, #2563EB) y botón de añadir al carrito (usa una instancia del componente Button creado en el ejemplo 2).
4. Selecciona todos los elementos de contenido (sin la imagen) y crea un Auto Layout vertical (Shift+A). Configura: gap=12px, padding=20px en los cuatro lados, alineación Start.
5. Ahora selecciona la imagen y el frame de contenido, y crea un Auto Layout vertical que los contenga a ambos. Configura: gap=0, padding=0. Este es el frame principal de la card.
6. Establece el Corner radius de este frame principal en 8px. Añade un Stroke de 1px color #E5E7EB y una sombra sutil (Drop shadow: X=0, Y=2, Blur=8, color negro al 8%).
7. Convierte este frame en un componente maestro (Ctrl+Alt+K). Renómbralo como "Card/Product".
8. Ahora configura las propiedades del componente: selecciona el componente maestro y en el panel derecho, en la sección "Component properties", haz clic en el icono +.
9. Añade una propiedad de texto para el título: selecciona "Text", nómbrala "Title", y en "Value" selecciona la capa de texto del título.
10. Añade propiedades de texto para categoría, descripción y precio.
11. Añade una propiedad de intercambio de instancia (Instance swap) para el botón: selecciona la instancia del botón en el componente y asígnale la propiedad "Button". Ahora cualquier instancia de Card podrá elegir qué variante de botón mostrar.
12. Crea una variante horizontal de la card: duplica el componente maestro, cambia el Auto Layout principal a dirección Horizontal, ajusta la imagen a 200px de ancho con Height 100% (Fill container) y el contenido a Fill container.
13. Renombra el primer componente como "Card/Layout=Vertical" y el nuevo como "Card/Layout=Horizontal".
14. Combina como variantes y verifica que puedes cambiar entre layout vertical y horizontal desde el panel de propiedades.

### Ejemplo guiado 5: Prototipo interactivo de navegación entre pantallas

Crearemos un prototipo funcional que muestre la navegación entre una pantalla de lista de productos y una pantalla de detalle de producto.

**Procedimiento paso a paso:**

1. Crea dos frames: uno de 390x844px (iPhone 14) para "Product List" y otro idéntico para "Product Detail". Colócalos uno al lado del otro.
2. En "Product List", diseña una cabecera con título "Products" y una barra de búsqueda. Debajo, crea una lista de 4-5 cards de producto utilizando instancias del componente Card creado en el ejemplo anterior.
3. En "Product Detail", diseña la pantalla de detalle: imagen grande del producto, nombre, descripción extensa, precio destacado y botón de compra.
4. Cambia a la pestaña Prototype en el panel derecho (o presiona Shift+E).
5. Selecciona la primera card de producto en el frame "Product List". Verás que aparece un círculo blanco (nodo de conexión) en su borde derecho.
6. Arrastra desde ese nodo hasta el frame "Product Detail" para crear una conexión.
7. En el panel derecho de Prototype, configura la interacción: Trigger = On Click, Action = Navigate to, Destination = Product Detail, Animation = Smart Animate, Duration = 300ms, Easing = Ease Out.
8. Ahora crea la navegación de vuelta: en el frame "Product Detail", diseña un botón de "Back" (una flecha hacia la izquierda) en la esquina superior izquierda.
9. En la pestaña Prototype, conecta el botón Back al frame "Product List": Trigger = On Click, Action = Navigate to, Destination = Product List, Animation = Smart Animate, Direction = From Left (o configura Move In desde la izquierda).
10. Para la interacción del botón "Buy Now" en la pantalla de detalle, crea un tercer frame de 390x844px llamado "Checkout". Diseña un formulario simple de checkout.
11. Conecta el botón "Buy Now" al frame Checkout con Smart Animate, duración 400ms.
12. Añade una interacción más: en el frame "Product List", selecciona cada una de las cards (excepto la primera) y conéctalas al frame "Product Detail" con el mismo trigger On Click. Así todas las cards navegan al detalle.
13. Haz clic en el botón Play (triángulo) en la esquina superior derecha de la barra de herramientas para abrir el prototipo en una ventana de presentación.
14. Prueba todas las interacciones: clic en cualquier card debe navegar al detalle, clic en Back debe volver a la lista, clic en Buy Now debe navegar al checkout.

### Ejemplo guiado 6: Uso de Dev Mode para extraer especificaciones CSS

Aprenderemos a utilizar el Modo Desarrollo para extraer medidas, estilos y código de un diseño en Figma.

**Procedimiento paso a paso:**

1. Cambia al Dev Mode haciendo clic en el icono </> en la barra de herramientas superior o presionando Shift+D.
2. Observa que la interfaz cambia: el panel derecho ahora muestra información técnica en lugar de propiedades de diseño.
3. Selecciona la card de producto que diseñaste en ejemplos anteriores. En el panel de Dev Mode, observa que Figma muestra: dimensiones totales (ancho x alto), posición dentro del frame padre, y distancias a otros elementos cercanos.
4. Desplázate por el panel de Dev Mode: verás una sección de "Code" que muestra sugerencias de código. Figma puede generar CSS, Tailwind CSS y SwiftUI por defecto. Selecciona CSS del desplegable si no está seleccionado.
5. Haz clic en diferentes elementos dentro de la card (el título, la descripción, el botón) y observa cómo cambian las especificaciones en Dev Mode para cada elemento seleccionado.
6. Selecciona un texto de título. En Dev Mode verás: font-family, font-size, font-weight, line-height, letter-spacing y color. Anota estos valores: son exactamente los que necesitas para tu CSS.
7. Mide distancias: mantén pulsada la tecla Alt (Option en Mac) y sitúa el cursor sobre un elemento. Figma mostrará líneas rojas con las distancias en píxeles hasta los elementos cercanos, tanto horizontal como verticalmente.
8. Selecciona el Auto Layout principal de la card. En Dev Mode verás una representación visual del layout: dirección del flex, gap, padding en cada lado, y modo de resizing. Debajo, el código CSS generado incluirá display: flex; flex-direction: column; gap: 0px; y los paddings.
9. En la sección "Assets" del panel de Dev Mode, verás todos los elementos exportables. Haz clic en el icono de exportación junto a la imagen de la card para descargarla en PNG, SVG o el formato que necesites.
10. En la parte inferior del panel de Dev Mode, verás una sección de "Properties" que muestra las variables de Figma aplicadas al elemento seleccionado. Si estás utilizando variables de color, aquí verás los nombres de las variables (tokens) en lugar de los valores crudos, facilitando la correspondencia con tus tokens CSS.

## Casos reales

### Caso real 1: El rediseño de Microsoft Teams utilizando Figma

Microsoft Teams experimentó un rediseño completo en 2023 que fue ejecutado íntegramente en Figma por un equipo distribuido globalmente. Este caso es particularmente instructivo porque demuestra cómo Figma escala para manejar proyectos de diseño de enorme complejidad con cientos de pantallas, miles de componentes y decenas de diseñadores trabajando simultáneamente.

El equipo de diseño de Teams organizó el proyecto en Figma utilizando páginas separadas para cada área funcional de la aplicación: Chat, Canales, Calendario, Llamadas, Archivos y Configuración. Cada página contenía los frames de todas las pantallas y estados de esa área, organizados en filas y columnas según el flujo de usuario. Utilizaron un sistema de bibliotecas compartidas con tres niveles: una biblioteca "Core" con los tokens de diseño y componentes atómicos (botones, inputs, iconos, tipografías, colores), una biblioteca "Teams Components" con los componentes compuestos específicos de Teams (tarjetas de mensaje, barras de herramientas, paneles laterales), y una biblioteca de "Templates" con layouts predefinidos para los tipos de pantalla más comunes.

El uso de Auto Layout fue intensivo en este proyecto. Cada componente, desde el más simple (un badge de notificación) hasta el más complejo (un panel de configuración de reunión con docenas de campos), se construyó con Auto Layout y modos de resizing apropiados para garantizar que se comportaran correctamente en diferentes tamaños de ventana. Los diseñadores podían cambiar el ancho de un frame de 1920px a 1024px y ver cómo todos los componentes se reajustaban automáticamente gracias a los constraints y al Auto Layout, permitiendo validar el comportamiento responsive sin diseñar manualmente cada breakpoint.

El proceso de handoff a desarrollo se realizó completamente a través de Dev Mode. Los desarrolladores accedían a los archivos de Figma, cambiaban a Dev Mode y obtenían especificaciones precisas de cada componente: dimensiones, espaciados, tipografías, colores (referenciados como tokens de diseño), y fragmentos de código CSS. El equipo de diseño mantenía además un archivo de "Redlines" con anotaciones detalladas sobre comportamientos interactivos, estados de error, casos edge y consideraciones de accesibilidad que no podían comunicarse solo con el diseño visual.

### Caso real 2: Sistema de diseño de una startup fintech española en Figma

Una startup fintech española especializada en gestión de gastos empresariales construyó su sistema de diseño completo en Figma siguiendo la metodología de Atomic Design. Este caso es relevante porque ilustra cómo un equipo pequeño (dos diseñadores y cuatro desarrolladores) puede implementar un sistema de diseño profesional en Figma y mantener la sincronización diseño-código.

El sistema se organizó en Figma en páginas que correspondían a los niveles de Atomic Design. La página "Tokens" contenía frames con muestras de todos los colores de la paleta (con sus nombres de variable), la escala tipográfica completa (con todas las combinaciones de tamaño, peso y altura de línea), la escala de espaciado (múltiplos de 4px desde 4 hasta 128) y los efectos (sombras, blurs, overlay). Cada elemento de esta página estaba vinculado a una variable de Figma, creando la fuente única de verdad para los tokens de diseño.

La página "Átomos" contenía los componentes más básicos: botones en todas sus variantes y tamaños, inputs de texto, selects, checkboxes, radio buttons, toggles, badges, avatares, iconos y etiquetas. Todos construidos con Auto Layout y convertidos en conjuntos de variantes con propiedades completas. La página "Moléculas" contenía combinaciones de átomos: campos de formulario (label + input + mensaje de error), barras de búsqueda, chips con icono de cierre, tooltips, dropdowns. La página "Organismos" contenía componentes complejos: formularios completos, tablas de datos, modales, cards de producto, barras de navegación, sidebars.

Para mantener la sincronización con el código, el equipo utilizó el plugin Tokens Studio (anteriormente Figma Tokens) para exportar todos los tokens de diseño a un repositorio Git en formato JSON compatible con Style Dictionary. Un pipeline de CI/CD transformaba automáticamente estos JSON en variables CSS y en objetos JavaScript de tema para la aplicación React. Cuando los diseñadores modificaban un token en Figma, el plugin sincronizaba el cambio con el repositorio, y el pipeline generaba las nuevas variables que se publicaban como una nueva versión del paquete npm de tokens del sistema de diseño.

### Caso real 3: Prototipado de una aplicación bancaria para test de usabilidad

Un importante banco español utilizó Figma para prototipar su nueva aplicación de banca móvil antes de escribir una sola línea de código. El objetivo era validar los flujos principales mediante tests de usabilidad con usuarios reales, iterando rápidamente sobre el diseño en función del feedback.

El equipo de UX creó en Figma un prototipo de alta fidelidad que simulaba la aplicación completa. Utilizaron más de 80 frames para cubrir todos los flujos principales: onboarding, login (con varios estados: vacío, completado, error de credenciales, bloqueo por intentos), dashboard principal, movimientos de cuenta, transferencias (nacionales, internacionales, periódicas, con varios estados de formulario), bizum, tarjetas (consulta, bloqueo, configuración de límites) y perfil de usuario.

La clave del prototipo fue el uso intensivo de interactive components. El teclado numérico para introducir el PIN se diseñó como un componente interactivo con variantes para cada tecla pulsada y para los estados del PIN (0 dígitos, 1 dígito, 2 dígitos, 3 dígitos, 4 dígitos y error). Los formularios de transferencia incluían estados de validación en tiempo real simulados mediante variantes: campos vacíos, válidos, con error, y botón de envío deshabilitado/habilitado. Las listas de movimientos utilizaban variantes para simular los diferentes estados: loading (skeleton), vacío (ilustración + mensaje), con datos y error de conexión.

El prototipo se probó con 15 usuarios en sesiones de usabilidad moderadas. Los participantes realizaban tareas guiadas ("transfiere 50 euros a tu contacto María", "bloquea temporalmente tu tarjeta de débito", "encuentra el gasto del supermercado de la semana pasada") mientras el moderador observaba. Los problemas detectados se anotaban directamente sobre el archivo de Figma mediante comentarios, y el equipo de diseño iteraba sobre los frames afectados en cuestión de horas. Este ciclo de prototipado-test-iteración se repitió tres veces antes de que el diseño se considerara validado y se iniciara el desarrollo, resultando en una reducción drástica de cambios de última hora durante la fase de implementación.

## Actividades guiadas

### Actividad guiada 1: Diseño de una landing page completa con Auto Layout y sistema de grid

**Objetivo:** Diseñar en Figma una landing page completa para un producto SaaS imaginario, utilizando Auto Layout en todos los componentes y aplicando un sistema de grid de 12 columnas.

**Contexto:** La empresa ficticia "TaskFlow" necesita una landing page para promocionar su software de gestión de tareas. Debes diseñar la página en tres breakpoints (móvil 390px, tablet 834px, escritorio 1440px).

**Pasos a seguir:**

1. Crea un nuevo archivo en Figma y organiza el espacio con tres frames de los tamaños indicados para los tres breakpoints.
2. Investiga y documenta (en texto, dentro del archivo Figma) los elementos que debe contener una landing page SaaS: hero section, sección de características, sección de precios, sección de testimonios, CTA final, footer.
3. Configura un sistema de grid en cada frame: selecciona el frame, en el panel derecho activa "Layout grid", selecciona "Columns", establece 12 columnas, gutter 24px, margin: 80px (escritorio), 40px (tablet), 16px (móvil).
4. Diseña la sección Hero utilizando Auto Layout vertical. Debe contener: un titular principal, un subtítulo, un campo de email con botón de registro y una imagen o ilustración del producto.
5. Diseña la sección de características con 3 columnas en escritorio, 2 en tablet y 1 en móvil. Cada característica debe ser una card con icono, título y descripción.
6. Aplica constraints a cada elemento dentro de los frames para que se comporten responsive cuando cambie el tamaño.
7. Convierte los elementos repetidos en componentes: las cards de características, los botones, los iconos.
8. Verifica el comportamiento responsive: selecciona el frame Desktop y arrastra su borde derecho hacia la izquierda. Los elementos con constraints deberían reaccionar.
9. Aplica los mismos principios para diseñar las secciones de precios, testimonios y CTA.
10. Documenta al menos 5 correspondencias entre decisiones de diseño en Figma y su equivalente en CSS.

**Criterios de evaluación:**

- Los tres breakpoints están correctamente configurados con sus grids (1.5 puntos).
- Todas las secciones utilizan Auto Layout y se comportan correctamente (2 puntos).
- Los elementos repetidos están convertidos en componentes reutilizables (1.5 puntos).
- Las constraints están correctamente aplicadas y el comportamiento responsive es verificable (2 puntos).
- La documentación de equivalencias Figma-CSS es correcta (1.5 puntos).
- La landing page es visualmente coherente y profesional (1.5 puntos).

### Actividad guiada 2: Construcción de un design system de componentes UI en Figma

**Objetivo:** Construir en Figma un design system completo de componentes de interfaz de usuario siguiendo Atomic Design, con tokens de diseño mediante variables de Figma.

**Contexto:** Se debe crear un design system llamado "EduDS" que incluya tokens, átomos, moléculas y organismos. El sistema debe estar organizado en páginas separadas y todos los componentes deben ser reutilizables.

**Pasos a seguir:**

1. Crea un nuevo archivo Figma. En la página 1, renómbrala a "🎨 Tokens". En esta página, crea:
    - Una tabla visual de la paleta de colores: al menos 3 colores de marca con 10 tonalidades cada uno, colores neutros (grises), colores semánticos (success, warning, error, info).
    - Una tabla de escala tipográfica con todos los niveles (h1-h6, body, caption, overline) mostrando fuente, tamaño, peso, altura de línea.
    - Una tabla de escala de espaciado (múltiplos de 4px).
    - Una tabla de radios de borde y sombras.
2. Crea variables de Figma para todos los tokens: abre el panel de variables (clic derecho en el canvas > Variables), crea colecciones para color, spacing, border-radius, typography. Define cada token como variable.
3. Aplica las variables a los elementos visuales de la página de tokens para verificar que funcionan. Modifica una variable y comprueba que sus usos se actualizan.
4. Crea una colección adicional de variables con modo "Light" y "Dark" para los colores semánticos. Verifica que puedes cambiar entre modos.
5. En la página 2 "⚛️ Átomos", crea componentes para: Button (variantes primary, secondary, ghost, danger; tamaños sm, md, lg; estados default, hover, active, disabled, loading), Input (tipos text, email, password, number, textarea; estados default, focus, error, disabled), Checkbox, Radio, Toggle, Badge, Avatar.
6. Cada átomo debe utilizar variables de Figma en lugar de valores hardcodeados para colores, tipografías y espaciados.
7. En la página 3 "🧬 Moléculas", crea componentes compuestos: FormField (label + input + help text + error message), SearchBar, Chip con icono de cierre, Tooltip, Dropdown.
8. En la página 4 "🦠 Organismos", crea: NavigationBar, Sidebar, Card (con todas sus variantes: simple, con imagen, horizontal), Modal, DataTable simple.
9. Configura propiedades de componente en todos los átomos y moléculas (text properties, boolean properties, instance swap).
10. Publica los componentes como biblioteca de equipo (si tienes plan de equipo) o asegúrate de que todos son accesibles desde el panel Assets.

**Criterios de evaluación:**

- La página de tokens es completa y utiliza variables de Figma correctamente (2 puntos).
- Los modos Light/Dark funcionan en las variables de color (1 punto).
- Se han creado al menos 6 átomos como componentes con variantes (2 puntos).
- Se han creado al menos 4 moléculas (1 punto).
- Se han creado al menos 3 organismos (1 punto).
- Los componentes tienen propiedades configuradas (1 punto).
- El sistema es consistente visualmente (1 punto).
- La organización por páginas y nomenclatura es clara (1 punto).

### Actividad guiada 3: Prototipo interactivo de un flujo de onboarding

**Objetivo:** Crear un prototipo interactivo completo de un flujo de onboarding para una aplicación móvil, con transiciones animadas, overlays y componentes interactivos.

**Contexto:** Una app de meditación y bienestar necesita un flujo de onboarding de 5 pantallas que guíe al usuario nuevo a través de las funcionalidades principales.

**Pasos a seguir:**

1. Crea 5 frames de 390x844px para las pantallas del onboarding. Nómbralos: "Onboarding 1 - Welcome", "Onboarding 2 - Features", "Onboarding 3 - Personalize", "Onboarding 4 - Notifications", "Onboarding 5 - Sign Up".
2. Diseña cada pantalla con: una ilustración o icono grande en la parte superior, un titular, un texto descriptivo, un indicador de progreso (dots) y un botón de "Next" o "Get Started" (en la última pantalla).
3. Diseña el indicador de progreso como un componente con 5 variantes (5 dots donde uno está activo). Utiliza este componente en cada pantalla con la variante correspondiente.
4. Configura las conexiones de prototipo entre todas las pantallas: cada botón "Next" navega a la siguiente pantalla con Smart Animate, duración 300ms.
5. Añade una animación de transición especial entre pantallas: selecciona un elemento común (por ejemplo, la ilustración) en dos pantallas consecutivas y asegúrate de que tengan el mismo nombre de capa para que Smart Animate los detecte.
6. En la pantalla 5 (Sign Up), diseña un formulario de registro (nombre, email, contraseña). Convierte el botón "Get Started" en un estado disabled (gris, no clickable) hasta que el formulario esté completo (simúlalo con una variante diferente).
7. Crea un frame adicional de 390x844px para la pantalla "Home" (la pantalla principal post-onboarding). Diseña mínimamente esta pantalla.
8. Conecta el botón "Get Started" de la pantalla 5 al frame Home con Smart Animate.
9. Añade un botón "Skip" en todas las pantallas de onboarding que navegue directamente a Home con una animación más rápida (200ms, Ease In).
10. Prueba el prototipo completo en la ventana de presentación. Verifica que todas las transiciones son suaves y que el flujo es coherente.
11. Simula un test de usabilidad: pide a un compañero que realice el flujo y anota al menos 3 observaciones de mejora directamente como comentarios en Figma.

**Criterios de evaluación:**

- Las 5 pantallas de onboarding están diseñadas de forma coherente (2 puntos).
- Las conexiones de prototipo funcionan correctamente (2 puntos).
- Smart Animate se ha configurado adecuadamente con elementos con nombre consistente (1.5 puntos).
- El flujo alternativo (Skip) funciona (1 punto).
- La pantalla Home existe y es accesible desde el prototipo (1 punto).
- Se han documentado 3 observaciones de mejora como comentarios en Figma (1.5 puntos).
- El diseño es visualmente atractivo y profesional (1 punto).

### Actividad guiada 4: Extracción de especificaciones técnicas desde Dev Mode para implementación

**Objetivo:** Practicar la extracción sistemática de toda la información técnica necesaria para implementar un diseño en código, utilizando Dev Mode de Figma.

**Contexto:** Se proporciona un diseño de Figma (puede ser el creado en actividades anteriores) que contiene una página de dashboard con múltiples componentes. El alumno debe documentar todas las especificaciones necesarias para que un desarrollador frontend pueda implementar la página sin tener que consultar el diseño constantemente.

**Pasos a seguir:**

1. Abre el archivo de Figma que contiene el dashboard diseñado (o utiliza el creado en tu proyecto de landing page).
2. Cambia a Dev Mode (Shift+D).
3. Crea un documento de especificaciones (puede ser un Google Doc, un Notion, o un archivo Markdown) con las siguientes secciones.
4. Sección "Paleta de colores": para cada color utilizado en el diseño, anota su valor HEX, su nombre de variable Figma (si existe) y dónde se utiliza.
5. Sección "Tipografía": para cada estilo de texto encontrado, documenta: nombre del estilo, familia, tamaño, peso, altura de línea, letter-spacing, color y uso en la interfaz.
6. Sección "Espaciado y layout": utilizando la herramienta de medición de Dev Mode (Alt + hover), documenta: márgenes del contenedor principal, paddings de cada sección, gaps entre elementos en Auto Layouts, gutter del grid.
7. Sección "Componentes": para cada tipo de componente, documenta: nombre del componente, dimensiones, variantes existentes, propiedades configurables, tokens de diseño que utiliza.
8. Sección "Breakpoints y responsive": si el diseño tiene versiones responsive, documenta para cada breakpoint: ancho del contenedor, cambios en el grid (número de columnas), cambios en el layout (stack vs row), elementos que se ocultan o muestran.
9. Sección "Assets": lista todos los elementos exportables (iconos, imágenes, ilustraciones) con su formato recomendado (SVG, PNG, WebP) y dimensiones de exportación (@1x, @2x, @3x).
10. Sección "Consideraciones de implementación": notas sobre animaciones y transiciones (duraciones, easings), estados de componentes (hover, active, disabled, loading, error), y cualquier comportamiento interactivo descrito en el prototipo.
11. Descarga al menos 3 assets del diseño utilizando Dev Mode (un icono SVG, una imagen placeholder en PNG @2x y un componente como SVG).
12. Revisa el documento de especificaciones con un compañero o con el profesor para verificar que no falta información relevante.

**Criterios de evaluación:**

- El documento de especificaciones cubre las 7 secciones requeridas (3.5 puntos, 0.5 cada una).
- Los valores extraídos (colores, tamaños, espaciados) son precisos y coinciden con el diseño (2 puntos).
- Las correspondencias con tokens y variables están documentadas (1 punto).
- Se han descargado 3 assets correctamente (1.5 puntos).
- El documento está organizado y es comprensible para un desarrollador que no vea el diseño (1 punto).
- Las consideraciones de implementación son útiles y accionables (1 punto).

## Actividades propuestas

### Actividad propuesta 1: Diseño responsive de una aplicación de gestión de biblioteca

Diseña en Figma la interfaz completa de una aplicación web de gestión de biblioteca que permita buscar libros, ver detalles, reservar ejemplares y gestionar el perfil de usuario. El diseño debe cubrir tres breakpoints (móvil, tablet, escritorio) e incluir al menos las siguientes pantallas: página principal con buscador y resultados, ficha de detalle de libro, formulario de reserva (multipaso), perfil de usuario con historial de préstamos, y dashboard de administrador con estadísticas básicas. Todos los elementos repetidos deben ser componentes reutilizables con variantes. Utiliza Auto Layout en todas las pantallas y documenta, mediante comentarios en Figma, al menos 10 decisiones de diseño justificadas.

### Actividad propuesta 2: Sistema de temas claro/oscuro con variables de Figma

Partiendo del design system "EduDS" creado en las actividades guiadas (o creando uno nuevo si no se realizó), implementa un sistema completo de temas claro y oscuro utilizando las variables y modos de Figma. Debes definir todas las variables de color necesarias en ambos modos, aplicarlas a todos los componentes del sistema, y crear dos frames de demostración (uno en cada tema) que muestren los mismos componentes para verificar la consistencia. Adicionalmente, investiga cómo exportar estas variables de Figma a un archivo JSON que pueda ser consumido por Style Dictionary o directamente por CSS Custom Properties, y documenta el proceso en un breve tutorial paso a paso.

### Actividad propuesta 3: Auditoría de accesibilidad de un diseño en Figma

Selecciona un diseño de Figma existente (puede ser uno de los creados en clase, un template de la comunidad de Figma, o un diseño propio de un proyecto anterior). Utilizando el plugin Stark, realiza una auditoría completa de accesibilidad que incluya: análisis de contraste de color de todos los textos contra sus fondos (con informe de cumplimiento WCAG AA y AAA), simulación de daltonismo (protanopia, deuteranopia, tritanopia) sobre las pantallas principales para verificar que la información no depende exclusivamente del color, verificación de los tamaños de toque (al menos 44x44px para elementos interactivos en móvil), y comprobación de jerarquía de encabezados. Genera un informe documentando los problemas encontrados y proponiendo soluciones concretas de rediseño en Figma. Implementa al menos 5 de las correcciones propuestas.

### Actividad propuesta 4: Prototipo de alta fidelidad para un proceso de compra ecommerce

Diseña y prototipa en Figma el flujo completo de compra de un ecommerce de productos tecnológicos. El prototipo debe incluir: navegación por categorías (con mega menú en escritorio y menú hamburguesa en móvil), listado de productos con filtros (precio, marca, valoración) aplicables, ficha de producto con galería de imágenes, carrito de compra con gestión de cantidades, proceso de checkout multipaso (dirección, envío, pago, confirmación), y pantalla de confirmación de pedido. Utiliza componentes interactivos para los elementos que cambian de estado (botones de añadir al carrito, toggle de favoritos, selectores de cantidad). Implementa Smart Animate en todas las transiciones. El prototipo debe ser navegable y permitir completar una compra de principio a fin.

## Actividades de ampliación

### Actividad de ampliación 1: Sincronización bidireccional Figma-Código

**Contexto:** En entornos profesionales avanzados, los equipos buscan mantener sincronizados los tokens de diseño entre Figma y el código para que un cambio en cualquiera de los dos entornos se refleje en el otro. Esta actividad explora el ecosistema de herramientas que permiten esta sincronización.

**Objetivos:**

- Instalar y configurar el plugin Tokens Studio for Figma (anteriormente Figma Tokens).
- Definir un conjunto completo de tokens de diseño (colores, tipografías, espaciados, sombras, border-radius) utilizando el plugin.
- Sincronizar los tokens con un repositorio GitHub (utilizando el proveedor de almacenamiento del plugin).
- Configurar un proyecto con Style Dictionary que consuma los tokens desde el repositorio y genere CSS Custom Properties y variables SASS.
- Realizar un cambio en un token desde Figma, sincronizarlo, regenerar los archivos de código y verificar que el cambio se refleja.
- Realizar el proceso inverso: modificar un token desde el repositorio (simulando un cambio hecho por un desarrollador) y comprobar cómo se reflejaría en Figma.
- Documentar todo el flujo de trabajo en un diagrama y un tutorial.
- Investigar las limitaciones actuales de la sincronización bidireccional y proponer soluciones o workarounds.

**Formato de entrega:** Repositorio Git con los archivos de tokens (JSON de Figma, configuración de Style Dictionary, salidas CSS/SCSS), diagrama del flujo de sincronización en formato imagen o Figma, y tutorial en README.md.

**Rúbrica de evaluación:**

- Tokens Studio configurado correctamente y tokens definidos (2 puntos).
- Sincronización con GitHub funcionando (2 puntos).
- Style Dictionary generando CSS y SCSS correctamente (2 puntos).
- Prueba de cambio Figma -> Código realizada y documentada (1.5 puntos).
- Prueba de cambio Código -> Figma simulada y documentada (1 punto).
- Diagrama del flujo completo (0.5 puntos).
- Análisis de limitaciones y propuestas (1 punto).

### Actividad de ampliación 2: Plugin de Figma para automatización de tareas de diseño

**Contexto:** Figma permite la creación de plugins personalizados que automatizan tareas repetitivas. Esta actividad introduce al alumnado en el desarrollo de plugins para Figma utilizando TypeScript y la Figma Plugin API.

**Objetivos:**

- Configurar un entorno de desarrollo para plugins de Figma (Node.js, TypeScript, Figma Plugin API typings).
- Desarrollar un plugin que automatice una tarea útil. Opciones sugeridas: generador automático de paletas de color a partir de un color semilla, generador de grids responsive (crea automáticamente filas y columnas con constraints configuradas), conversor de textos a componentes tipográficos, validador de naming conventions (verifica que los componentes sigan la convención slash), o generador de variantes de componente (crea automáticamente todas las combinaciones de propiedades a partir de unos parámetros base).
- El plugin debe tener una UI (interfaz de usuario) que permita configurar los parámetros de la automatización.
- El plugin debe funcionar correctamente en la versión de escritorio de Figma (no es necesario publicarlo en la comunidad).
- Documentar el proceso de desarrollo, las decisiones técnicas tomadas, y cómo probar y depurar un plugin de Figma.
- Investigar y documentar las diferencias entre la API de plugins (sandbox) y la API de widgets de Figma, así como los casos de uso apropiados para cada una.

**Formato de entrega:** Carpeta del plugin con código fuente TypeScript, manifest.json, UI HTML, README con instrucciones de instalación y desarrollo. Documento de investigación sobre Figma Plugin API vs Widget API.

**Rúbrica de evaluación:**

- Entorno de desarrollo configurado correctamente (1 punto).
- Plugin funcional que realiza la tarea descrita (3 puntos).
- UI del plugin funcional y usable (2 puntos).
- Documentación del proceso de desarrollo (1.5 puntos).
- Análisis comparativo Plugin API vs Widget API (1.5 puntos).
- Código limpio y bien comentado (1 punto).

### Actividad de ampliación 3: Proyecto final evaluable - Diseño completo de aplicación web en Figma

**Contexto:** Esta actividad constituye el proyecto final evaluable de la unidad. El alumno debe integrar todos los conocimientos adquiridos para diseñar una aplicación web completa en Figma, desde la investigación inicial hasta un prototipo interactivo de alta fidelidad listo para handoff a desarrollo.

**Objetivos:**

- Seleccionar un proyecto de aplicación web de entre las opciones propuestas por el profesor o proponer uno propio (debe ser aprobado). Ejemplos: una plataforma de cursos online, una app de recetas compartidas, un gestor de finanzas personales, un marketplace de segunda mano, una red social para profesionales de un sector específico.
- Realizar una fase de investigación y definición: identificar usuarios objetivo, definir funcionalidades principales, crear user personas básicos.
- Diseñar wireframes de baja fidelidad de al menos 6 pantallas principales, utilizando solo formas básicas (rectángulos grises, líneas, texto placeholder). Validar los flujos principales con un test informal (compañero de clase).
- Crear un design system en Figma para el proyecto: tokens de diseño (colores, tipografía, espaciado, etc.) definidos como variables, componentes atómicos (botones, inputs, iconos, etc.) con variantes y propiedades, y componentes moleculares/organismos específicos del proyecto.
- Diseñar las pantallas en alta fidelidad para al menos 3 breakpoints (móvil, tablet, escritorio) o, si el proyecto es mobile-first, al menos 10 pantallas móviles diferentes.
- Crear un prototipo interactivo con al menos 3 flujos de usuario completos, utilizando Smart Animate, overlays e interactive components.
- Realizar una auditoría de accesibilidad básica con Stark y documentar las correcciones aplicadas.
- Preparar la documentación de handoff: especificaciones en Dev Mode, assets exportables organizados, anotaciones de comportamiento interactivo.
- Grabar un vídeo de 3-5 minutos demostrando el prototipo interactivo y explicando las decisiones de diseño principales.

**Formato de entrega:** Enlace al archivo Figma (con permisos de visualización), documento PDF de especificaciones de diseño (exportado desde Figma o redactado aparte), y vídeo de demostración.

**Rúbrica de evaluación:**

- Investigación y definición del proyecto (1 punto).
- Wireframes de baja fidelidad (1 punto).
- Design system completo con variables y componentes (3 puntos).
- Pantallas de alta fidelidad (3 puntos).
- Prototipo interactivo con 3 flujos completos (2 puntos).
- Auditoría de accesibilidad y correcciones (1 punto).
- Documentación de handoff (1 punto).
- Vídeo de demostración (1 punto).
- Calidad visual y consistencia del diseño (2 puntos).

## Buenas prácticas

**Organización de páginas y frames.** La organización del archivo de Figma es el primer indicador de profesionalidad en el diseño de interfaces. Un archivo bien organizado utiliza páginas (Page 1, Page 2, etc.) renombradas con nombres descriptivos y, preferiblemente, emojis como prefijos visuales para facilitar la navegación: "🎨 Design System", "📱 Mobile Screens", "💻 Desktop Screens", "🔬 Components Lab", "📋 Archive / Explorations". Dentro de cada página, los frames deben estar organizados en filas y columnas con espaciados uniformes (típicamente **80-100 px** entre frames), y deben estar agrupados por funcionalidad o flujo. Un colaborador que abra el archivo por primera vez debe poder orientarse en **menos de 30 segundos**.

**Nomenclatura de capas y componentes.** Debe ser descriptiva y seguir una convención consistente. Para componentes, la **nomenclatura slash (/)** es el estándar de Figma porque genera automáticamente propiedades de variante: "Button/Size=Medium/Variant=Primary/State=Default". Para capas dentro de componentes, se recomienda usar nombres semánticos en inglés (o en el idioma acordado por el equipo): "icon-left", "label", "badge-count", "chevron-right". **Evitar nombres genéricos** como "Rectangle 47" o "Group 12". Cuando un elemento tenga el mismo nombre en dos frames diferentes, **Smart Animate** lo detectará automáticamente y aplicará una transición, por lo que los nombres consistentes son cruciales para el prototipado.

!!! tip "Sistema de 8 puntos"
    El **sistema de grid de 8 puntos** (*8pt grid system*) es un estándar de la industria que debe aplicarse tanto en diseño como en desarrollo: todos los espaciados, *paddings*, tamaños y dimensiones deben ser **múltiplos de 8 px** (o de **4 px** para ajustes muy finos). Esto garantiza que los diseños se alineen con el sistema de píxeles de las pantallas y facilita la implementación. En Figma se configura la grilla de *layout* del frame con columnas de 8 px y el **nudge amount** (cantidad de desplazamiento con flechas) a 8 px en **Preferences > Nudge Amount**.

**Atomic Design en Figma.** La metodología organiza los componentes en niveles de complejidad creciente. La página de "Átomos" contiene los elementos más básicos e indivisibles (botones, inputs, iconos, etiquetas). La página de "Moléculas" contiene combinaciones simples de átomos (campo de formulario = *label* + *input* + *error message*). La página de "Organismos" contiene secciones completas de interfaz (*header*, *footer*, card compleja, formulario completo). Esta organización facilita la localización de componentes, evita la duplicación y permite construir nuevas pantallas por composición de organismos existentes en lugar de diseñar desde cero.

**Auto Layout como norma, no como excepción.** Cualquier grupo de elementos que tenga una relación espacial (horizontal, vertical, *grid*) debe estar contenido en un frame con Auto Layout. Esto garantiza que el diseño se comporte correctamente cuando cambie el contenido (texto más largo, más elementos en una lista) y facilita la traducción a **CSS Flexbox**. La resistencia a usar Auto Layout ("es más rápido diseñar con posiciones absolutas") es un error común que genera **deuda de diseño** y ralentiza el *handoff* a desarrollo.

**Documentación dentro de Figma.** Mediante comentarios y anotaciones, es especialmente valiosa para comunicar decisiones de diseño, *casos edge* y comportamientos interactivos que no son evidentes en el diseño estático. Los comentarios pueden anotarse directamente sobre elementos específicos del *canvas* y son visibles para todos los colaboradores. Para documentación más estructurada, se puede utilizar la funcionalidad de **Annotations** en Dev Mode o crear frames específicos de documentación con textos explicativos, flechas y referencias visuales.

## Errores frecuentes

!!! warning "Usa frames, no grupos"
    Uno de los errores más comunes entre principiantes en Figma es utilizar **grupos (Groups)** en lugar de **frames (Frames)**. Los grupos son meras agrupaciones visuales que **no proporcionan constraints, auto layout, clipping ni capacidades de layout responsive**. Un diseño construido con grupos se comporta de forma impredecible cuando se redimensiona y no puede traducirse limpiamente a HTML/CSS. **Regla de oro:** si un elemento contiene a otros elementos, debe ser un frame, no un grupo. Los grupos solo deben utilizarse para agrupaciones temporales o para organizar capas que no tienen relación de *layout*.

**No utilizar Auto Layout** es otro error generalizado que produce diseños frágiles. Cuando un botón se diseña con posiciones absolutas (texto posicionado manualmente dentro de un rectángulo), cualquier cambio en el texto (por ejemplo, traducir "Submit" a "Enviar formulario") rompe el diseño y requiere ajustes manuales. Con Auto Layout, el botón se ajusta automáticamente al tamaño del texto manteniendo los *paddings* configurados. La resistencia inicial a Auto Layout (porque requiere una forma diferente de pensar el *layout*) debe superarse cuanto antes, ya que es la funcionalidad que más productividad y calidad aporta al diseño de interfaces.

**Crear múltiples componentes separados** para variantes que deberían estar unificadas es un error organizativo muy frecuente. Por ejemplo, crear "Button Primary", "Button Secondary" y "Button Danger" como componentes independientes en lugar de como variantes de un mismo componente "Button". Esto duplica el mantenimiento (cualquier cambio en la estructura del botón debe hacerse tres veces), impide el intercambio de variantes desde el panel de propiedades y complica la consistencia. **Siempre que varios componentes compartan estructura pero difieran en propiedades visuales, deben combinarse como variantes.**

**Ignorar el comportamiento responsive** durante el diseño es un error con consecuencias costosas. Diseñar exclusivamente para escritorio (**1440 px**) y asumir que "ya se adaptará en desarrollo" transfiere al desarrollador decisiones de diseño que deberían haberse tomado en la fase de diseño. Cada pantalla debe diseñarse en al menos **dos breakpoints** (móvil y escritorio), y los constraints deben configurarse para que los elementos se comporten correctamente en tamaños intermedios. Dedicar tiempo a configurar constraints durante el diseño ahorra horas de idas y venidas entre diseño y desarrollo.

**No utilizar variables de Figma** y *hardcodear* valores es un error que dificulta el mantenimiento y la consistencia. Si el color primario de la marca está definido manualmente como **#2563EB** en **40 componentes** diferentes, cambiarlo a **#1D4ED8** requerirá modificar manualmente esos 40 componentes. Con variables, basta con cambiar el valor de la variable una vez y todos los componentes se actualizan automáticamente. Las variables deben definirse **al inicio del proyecto**, antes de empezar a diseñar componentes.

Finalmente, **diseñar prototipos excesivamente complejos que no pueden implementarse** es un error frecuente cuando el diseñador desconoce las capacidades y limitaciones de la plataforma de destino. Animaciones imposibles en CSS, transiciones entre pantallas que no tienen correspondencia en el framework utilizado (React, Vue, etc.), o microinteracciones que requerirían bibliotecas de animación pesadas son ejemplos de diseños que generan frustración en el equipo de desarrollo. La comunicación constante entre diseño y desarrollo y el conocimiento técnico del medio (web, iOS, Android) son esenciales para mantener los prototipos dentro del ámbito de lo realizable.

## Resumen

Figma se ha consolidado como la herramienta de diseño de interfaces dominante en la industria del desarrollo web y de aplicaciones, desplazando a competidores como Sketch y Adobe XD gracias a su naturaleza colaborativa basada en navegador, su modelo freemium accesible y su ecosistema de plugins y funcionalidades que cubren el ciclo completo desde la ideación hasta el handoff técnico. Para el desarrollador frontend, el dominio de Figma es una competencia cada vez más demandada, no para reemplazar al diseñador sino para colaborar eficazmente con él, comprender las decisiones de diseño, extraer especificaciones técnicas precisas y participar en la construcción y mantenimiento del sistema de diseño compartido.

Los fundamentos técnicos de Figma —frames, constraints, Auto Layout, variables, componentes y variantes— tienen correspondencias directas con los conceptos del desarrollo web (HTML elements, CSS positioning, Flexbox, CSS Custom Properties, Web Components), lo que facilita que un desarrollador frontend aprenda Figma y que un diseñador comprenda mejor las implicaciones técnicas de sus decisiones. El prototipado interactivo permite validar flujos de usuario, transiciones y microinteracciones antes de escribir código, reduciendo los costosos cambios de última hora y alineando las expectativas de todos los stakeholders del proyecto.

El Modo Desarrollo (Dev Mode) cierra el círculo proporcionando un puente directo entre el diseño y el código: medidas precisas, especificaciones CSS, tokens de diseño referenciados por nombre y assets exportables en los formatos adecuados. Las buenas prácticas de organización, nomenclatura y uso sistemático de Auto Layout y variables son las que diferencian un archivo de Figma profesional y mantenible de uno caótico que genera más problemas de los que resuelve.

## Recursos complementarios

- **Figma Learn Center:** La plataforma oficial de aprendizaje de Figma, con tutoriales interactivos, guías paso a paso y cursos por nivel. Disponible en https://help.figma.com/hc/en-us/categories/360002051613-Get-started
- **Figma YouTube Channel:** Canal oficial con tutoriales, webinars, novedades de producto y casos de estudio. Especialmente recomendada la serie "Figma for Developers". Disponible en https://www.youtube.com/c/Figmadesign
- **Figma Community:** Repositorio de archivos, componentes y plugins compartidos por la comunidad. Recurso valiosísimo para estudiar cómo otros diseñadores estructuran sus proyectos. Disponible en https://www.figma.com/community
- **Auto Layout Playground (Figma Community):** Archivo interactivo para practicar y dominar Auto Layout, creado por el equipo de Figma. Buscar "Auto layout playground" en la Comunidad de Figma.
- **Design Systems Figma Community Files:** Colecciones de archivos de sistemas de diseño completos compartidos por empresas como Uber, Shopify y Microsoft. Buscar "design system" o "UI kit" en la Comunidad de Figma.
- **Stark Plugin:** Plugin de accesibilidad para Figma que permite verificar contrastes, simular daltonismo y generar informes de cumplimiento WCAG. Instalable desde la Comunidad de Figma.
- **Tokens Studio for Figma (anteriormente Figma Tokens):** Plugin para gestionar tokens de diseño en Figma y sincronizarlos con repositorios Git. Disponible en la Comunidad de Figma.
- **Figma Plugin API Documentation:** Documentación oficial para el desarrollo de plugins y widgets de Figma. Disponible en https://www.figma.com/plugin-docs
- **Figma for Developers (Blog Post de Figma):** Artículo oficial que explica cómo los desarrolladores pueden aprovechar Figma. Buscar en https://www.figma.com/blog
- **Figma to Code (varios recursos):** Herramientas y plugins que convierten diseños de Figma en código (HTML/CSS, React, Vue, Flutter). Investigar: Anima, Figma to React, Locofy, Quest AI.
