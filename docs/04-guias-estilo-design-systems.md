---
icon: lucide/swatch-book
---

# Unidad 4: Guías de Estilo y Sistemas de Diseño

## Objetivos de aprendizaje

Al finalizar esta unidad, el alumnado será capaz de identificar y aplicar los principios fundamentales que rigen las guías de estilo y los sistemas de diseño en el desarrollo de interfaces web. Se persigue que el estudiante comprenda la diferencia conceptual entre una guía de estilo tradicional y un sistema de diseño moderno, así como su valor estratégico dentro del flujo de trabajo de un equipo de desarrollo frontend. El alumno aprenderá a analizar críticamente sistemas de diseño consolidados como Material Design, Human Interface Guidelines de Apple y Ant Design, extrayendo de cada uno sus principios rectores y aplicándolos en contextos reales. Un objetivo prioritario es que el estudiante adquiera la capacidad de construir su propio sistema de diseño desde cero, comenzando por la realización de un inventario de interfaz, pasando por la definición de tokens de diseño y culminando en la implementación técnica mediante variables CSS, SASS o Styled Components. Se espera que al terminar la unidad el alumno pueda documentar adecuadamente un sistema de diseño utilizando herramientas profesionales como Storybook o Zeroheight, y que sea capaz de justificar las decisiones de diseño adoptadas en base a criterios de consistencia, escalabilidad, accesibilidad y mantenibilidad del código.

## Relación con los Resultados de Aprendizaje

Esta unidad se vincula directamente con los Resultados de Aprendizaje oficiales del módulo 0615 *Diseño de interfaces web* (RD 405/2023, BOE; currículo andaluz):

- **RA1. Planifica la creación de una interfaz web valorando y aplicando especificaciones de diseño.** Los sistemas de diseño constituyen el puente entre la fase de planificación y la implementación técnica: definir y aplicar la guía de estilo (CE 1.d) es un requisito explícito de este resultado, y justificar el uso de cada herramienta y framework responde al CE 1.e.
- **RA2. Crea interfaces web homogéneos definiendo y aplicando estilos.** Los tokens de diseño y las variables CSS aportan la conexión metodológica directa con la creación de interfaces coherentes: un sistema de diseño garantiza que todos los componentes respondan a un mismo lenguaje visual (CE 2.g). La documentación del sistema con herramientas como Storybook o Zeroheight refuerza esa homogeneidad.
- **RA5. Desarrolla interfaces web accesibles, analizando las pautas establecidas y aplicando técnicas de verificación.** La incorporación de criterios de accesibilidad (WCAG) dentro del sistema de diseño garantiza que todos los componentes cumplan las pautas desde su concepción (CE 5.c).

## Conocimientos previos

Para abordar con éxito esta unidad, el alumnado debe dominar los fundamentos de HTML5 y CSS3, incluyendo el modelo de cajas, el posicionamiento mediante **Flexbox** y **Grid**, las *media queries* para diseño *responsive* y el uso de selectores avanzados. Es esencial que el estudiante conozca el concepto de **especificidad** en CSS y comprenda cómo funciona la **cascada de estilos**, ya que estos mecanismos son la base sobre la que se construye cualquier sistema de diseño. Se requiere también familiaridad con algún preprocesador CSS, preferiblemente **SASS/SCSS**, incluyendo el uso de variables, *mixins*, funciones y la directiva `@extend`. El alumno debe haber trabajado previamente con metodologías de organización de CSS como **BEM**, **SMACSS** u **OOCSS**, ya que los sistemas de diseño heredan y amplían estos principios de modularidad y reutilización. Es conveniente que el estudiante tenga nociones básicas de diseño gráfico aplicado a web: teoría del color, principios de tipografía digital, jerarquía visual, espaciado y proporción. También resulta beneficioso que conozca el funcionamiento de herramientas de diseño como **Figma**, aunque no es un requisito excluyente. Por último, se presupone una comprensión básica de los principios de usabilidad y accesibilidad web, incluyendo el conocimiento de las **WCAG 2.1** en su nivel **AA**.

## Contenidos

1. **Definición y objetivos de las guías de estilo:** elementos que las componen y su función dentro del ecosistema de diseño de un producto digital.
2. **Componentes de una guía de estilo:** desde el logotipo y la marca hasta el tono de voz, pasando por paletas cromáticas, tipografía, iconografía, botones, formularios, espaciado, sistemas de rejilla y tratamiento de imágenes.
3. **Tokens de diseño:** concepto, clasificación en tokens globales, de alias y específicos de componente, convenciones de nomenclatura estructurada e implementación práctica mediante CSS Custom Properties.
4. **Sistemas de diseño:** definición formal, diferencias fundamentales con las guías de estilo tradicionales, beneficios cuantificables en términos de consistencia, velocidad de desarrollo, escalabilidad y accesibilidad.
5. **Análisis de sistemas de diseño consolidados:** Material Design de Google y sus tres principios fundamentales, Human Interface Guidelines de Apple con su enfoque en claridad, deferencia y profundidad, y Ant Design como paradigma de sistema de diseño orientado al ámbito empresarial.
6. **Proceso de creación de un sistema de diseño propio:** desde el inventario de interfaz y la auditoría inicial hasta la documentación final, pasando por la definición de principios, la creación de tokens y la construcción de componentes.
7. **Implementación técnica de sistemas de diseño:** estrategias con variables CSS nativas, preprocesadores SASS/SCSS, CSS-in-JS mediante Styled Components y CSS Modules.
8. **Ejemplo práctico** de construcción de un mini design system completamente documentado y funcional.
9. **Herramientas profesionales:** Storybook para desarrollo aislado de componentes, Figma Tokens para sincronización diseño-código, Style Dictionary como gestor de tokens multiplataforma y Zeroheight para documentación colaborativa de sistemas de diseño.

## Desarrollo teórico

### Las guías de estilo como fundamento del diseño consistente

!!! info "Definición"
    Una **guía de estilo** es un documento vivo que establece las reglas, estándares y convenciones que rigen la identidad visual y la experiencia de usuario de un producto digital. Su objetivo primordial es garantizar la **coherencia visual y funcional** a lo largo de todas las pantallas, componentes e interacciones que conforman una aplicación o sitio web. La guía de estilo actúa como la **fuente única de verdad** a la que deben remitirse tanto diseñadores como desarrolladores cuando necesitan tomar decisiones sobre la apariencia o el comportamiento de cualquier elemento de la interfaz.

La guía de estilo contiene múltiples elementos interrelacionados:

- **Paleta de colores** - colores primarios, secundarios, de acento, semánticos (éxito, advertencia, error, información) y neutros, especificando para cada uno sus valores en diferentes espacios de color (**HEX**, **RGB**, **HSL**) y sus niveles de accesibilidad en cuanto a contraste.
- **Tipografía** - familias tipográficas, escala tipográfica con tamaños, pesos e interlineados para cada nivel jerárquico y reglas de uso para titulares, cuerpo de texto, etiquetas y texto auxiliar.
- **Iconografía** - estilo visual de los iconos (lineales, sólidos, *dual tone*), tamaños estandarizados, áreas de seguridad y reglas de alineación.
- **Sistema de espaciado** - escala matemática generalmente basada en una unidad base (**4px** u **8px**), aplicada de forma sistemática a márgenes, *paddings* y separaciones entre elementos.
- **Cuadrícula o *grid*** - estructura de columnas, calles y márgenes que organiza el contenido en los diferentes *breakpoints* responsive.
- **Elementos menos tangibles** - tono de voz de los textos de interfaz, estilo fotográfico y de ilustración, principios de animación y microinteracciones, y reglas de uso del logotipo y los elementos de marca.

Todos estos componentes conforman un ecosistema coherente que, correctamente implementado, garantiza que cualquier persona que interactúe con el producto perciba una experiencia unificada y profesional.

### Tokens de diseño: la unidad atómica de los sistemas de diseño

!!! info "Definición"
    Los **tokens de diseño** representan la evolución natural de las variables de estilo tradicionales hacia un sistema semántico, portable y mantenible. Un token de diseño es la **abstracción más pequeña y atómica** de una decisión de diseño, expresada como un par **nombre-valor** que puede ser consumida por cualquier plataforma o tecnología. A diferencia de las variables CSS o SASS tradicionales, que suelen estar ligadas a una implementación concreta, los tokens de diseño se definen en un formato **agnóstico** (generalmente JSON o YAML) y se transforman posteriormente para cada plataforma de destino: **CSS** para web, **XML** para Android, **Swift** para iOS, etc.

Los tokens de diseño se clasifican en **tres niveles jerárquicos**:

| Capa de tokens | Qué define | Ejemplo |
|----------------|------------|---------|
| **Global o primitivo** | Valores crudos sin ningún significado semántico asociado. | `blue-500: #1976D2`, `spacing-4: 16px` |
| **Alias o semántico** | Añade una capa de significado y vincula el valor con su función en el sistema. | `color-primary-500: {blue-500}` |
| **Específico de componente** | Aplica los tokens semánticos a contextos concretos. | `button-primary-background: {color-primary-500}`, `button-primary-text: {color-white}` |

Esta arquitectura en tres capas permite que un cambio en un token global se propague automáticamente a todos los componentes que lo referencian, facilitando el mantenimiento y la evolución del sistema.

La nomenclatura de los tokens sigue una convención estructurada que facilita su localización y comprensión.

!!! tip "Nomenclatura de tokens"
    Se recomienda utilizar el formato `categoría-propiedad-variante-estado`, como en `color-background-button-primary-hover` o `font-size-heading-h1-desktop`. Esta estructura jerárquica, combinada con el anidamiento que proporcionan formatos como JSON, permite organizar cientos o miles de tokens de forma navegable.

En el contexto del desarrollo web, los tokens de diseño se implementan típicamente mediante **CSS Custom Properties**, aprovechando su naturaleza dinámica y su capacidad de ser redefinidas en diferentes contextos. La especificación **CSS Houdini** y la API de **Properties and Values** prometen llevar esta integración aún más lejos, permitiendo registrar propiedades personalizadas con tipos, valores iniciales y comportamientos de herencia definidos explícitamente.

### Diferencias entre guía de estilo y sistema de diseño

!!! info "Definición"
    Aunque frecuentemente se utilizan como sinónimos, las guías de estilo y los sistemas de diseño representan conceptos diferentes tanto en su alcance como en su propósito. Una **guía de estilo** es fundamentalmente un documento de referencia estático que describe cómo deben verse y comportarse los elementos visuales de un producto: recoge principios, reglas y ejemplos, pero no proporciona los componentes implementados ni el código necesario para materializar esas reglas. En contraposición, un **sistema de diseño** es un ecosistema vivo que incluye tanto la documentación como los componentes funcionales, las librerías de código, los tokens de diseño, las herramientas de desarrollo y los procesos de gobernanza que garantizan su evolución controlada.

El sistema de diseño incorpora la guía de estilo como uno de sus componentes, pero va mucho más allá al proporcionar los bloques de construcción reales con los que se fabrican las interfaces:

| Aspecto | Guía de estilo | Sistema de diseño |
|---------|----------------|-------------------|
| **Qué prescribe** | Que «los botones primarios deben ser azules con bordes redondeados de **4px**». | El componente `<Button variant="primary" />` listo para usar en desarrollo. |
| **Qué lo acompaña** | Principios, reglas y ejemplos descritos en un documento. | Documentación en Storybook, tests unitarios, variantes de accesibilidad y directrices de uso. |

Esta diferencia fundamental tiene implicaciones profundas en la eficiencia del equipo.

!!! tip "Impacto en la eficiencia"
    Un sistema de diseño bien implementado y mantenido puede reducir el tiempo de desarrollo de nuevas funcionalidades entre un **25%** y un **50%**, eliminar inconsistencias visuales entre productos de una misma organización y facilitar la incorporación de nuevos miembros al equipo.

Los beneficios de adoptar un sistema de diseño son cuantificables:

- **Consistencia** - todos los equipos y productos de una organización comparten el mismo lenguaje visual, reduciendo drásticamente la deuda de diseño.
- **Velocidad** - los desarrolladores ensamblan interfaces componiendo piezas preexistentes en lugar de crearlas desde cero.
- **Escalabilidad** - el sistema crece de forma orgánica y controlada mediante un proceso de contribución y revisión.
- **Accesibilidad** - se integra desde la base: cada componente incorpora por defecto los atributos **ARIA**, los contrastes de color adecuados y el soporte para navegación por teclado, de modo que todas las interfaces construidas con el sistema heredan estas propiedades sin esfuerzo adicional.

### Material Design: el lenguaje visual de Google

Material Design nació en **2014** como la respuesta de Google a la fragmentación visual que sufrían sus productos. Su nombre proviene del concepto central que lo articula: la **metáfora del material**. Según este principio fundacional, la interfaz se comporta como si estuviera compuesta por capas de papel y tinta digitales que existen en un espacio tridimensional. Estas superficies proyectan sombras, se deslizan unas sobre otras y responden al tacto del usuario, pero nunca se atraviesan ni ocupan el mismo espacio simultáneamente. Esta metáfora proporciona un **modelo mental intuitivo** que los usuarios comprenden de forma casi instantánea, ya que se basa en su experiencia con los objetos físicos del mundo real.

El segundo principio de Material Design establece que el diseño debe ser **audaz, gráfico e intencional**. Esto se traduce en el uso deliberado de jerarquías tipográficas marcadas, espacios generosos, *grids* deliberadamente construidos y un uso del color con intención comunicativa clara. Material Design introdujo conceptos como la **superficie primaria** y la **superficie secundaria**, estableciendo elevaciones estandarizadas mediante sombras sutiles y capas de *scrim* que permiten al usuario comprender instantáneamente la jerarquía espacial de la interfaz. La paleta cromática de Material se organiza en una escala numérica que va desde el **50** (el tono más claro) hasta el **900** (el más oscuro), con variantes de acento etiquetadas como **A100**, **A200**, **A400** y **A700**.

El tercer principio afirma que el **movimiento proporciona significado**. En Material Design, las animaciones y transiciones no son meros adornos visuales sino herramientas comunicativas que revelan relaciones jerárquicas, guían la atención del usuario, proporcionan *feedback* sobre las acciones realizadas y dotan de personalidad a la experiencia. Material introdujo patrones como el ***ripple effect*** (una onda expansiva que se origina en el punto de contacto del dedo), las ***shared element transitions*** y las transformaciones de contenedor que comunican la relación entre dos estados de la interfaz de forma orgánica y comprensible. Con el tiempo, Material Design ha evolucionado hacia **Material You (Material 3)**, que incorpora la generación dinámica de paletas de color a partir del *wallpaper* del usuario y una nueva filosofía de personalización extrema.

### Human Interface Guidelines de Apple

Las Human Interface Guidelines (HIG) de Apple representan un enfoque radicalmente diferente al de Material Design, profundamente enraizado en la tradición del diseño industrial de la compañía y en sus valores fundamentales. Las HIG se articulan en torno a **tres principios rectores** que todo diseñador y desarrollador de plataformas Apple debe interiorizar. El primer principio, la **claridad**, establece que el texto debe ser legible a cualquier tamaño, los iconos deben ser precisos y sin ambigüedades, los adornos visuales deben ser sutiles y funcionales, y la interfaz debe comunicar su propósito de forma inmediata sin requerir interpretación por parte del usuario.

El segundo principio, la **deferencia**, es quizás el más característico de la filosofía de diseño de Apple. La deferencia significa que la interfaz debe **ceder el protagonismo al contenido**.

!!! info "Deferencia"
    La UI no compite con lo que el usuario quiere ver o hacer: **se desvanece, se vuelve translúcida, se oculta cuando no es necesaria**. Los elementos cromados se reducen al mínimo, los bordes y los contenedores se difuminan, y los espacios negativos se amplían para que el contenido respire.

Esta filosofía se materializa en patrones como las **barras de navegación translúcidas** que permiten ver el contenido al desplazarse, o el ***blur gaussiano*** que difumina el fondo cuando aparece un modal, manteniendo el contexto visual del usuario.

El tercer principio, la **profundidad**, se consigue mediante capas visuales sutiles y movimiento realista. A diferencia de Material Design, que utiliza sombras proyectadas para simular elevación, las HIG emplean translucidez, *parallax* y efectos de desenfoque para crear una sensación de profundidad más etérea y menos explícita. Las transiciones en iOS se basan en curvas de aceleración naturales que emulan la física del mundo real, y los gestos táctiles como el ***swipe back*** o el ***pull to refresh*** se integran de forma orgánica. Las HIG cubren exhaustivamente patrones de navegación como la **Tab Bar**, el **Navigation Controller**, las **Modales**, los **Action Sheets** y los **Menús Contextuales**, proporcionando directrices precisas sobre cuándo y cómo utilizar cada uno.

### Ant Design: un sistema de diseño orientado a producto empresarial

Ant Design surgió de la necesidad interna de Alibaba de unificar la experiencia de sus decenas de productos empresariales. A diferencia de Material Design (orientado al consumo) y las HIG (centradas en la excelencia estética), Ant Design se construyó desde cero pensando en las necesidades específicas de las aplicaciones empresariales:

- **Tablas de datos** complejas.
- **Formularios** extensos.
- **Flujos de trabajo** con múltiples pasos.
- ***Dashboards*** analíticos.
- **Sistemas de permisos** y roles.
- **Componentes para visualización** de datos masivos.

La filosofía de Ant Design se articula en torno a **cuatro valores de diseño**:

- **Natural** - persigue que la interacción del usuario con la interfaz sea tan fluida como su interacción con el mundo físico, minimizando la carga cognitiva y eliminando fricciones innecesarias.
- **Certain** - busca proporcionar certidumbre al usuario en todo momento: cada acción produce un resultado predecible, cada estado se comunica claramente y no existen ambigüedades en la interfaz.
- **Meaningful** - sostiene que cada elemento de la interfaz debe tener un propósito justificado y contribuir a los objetivos del usuario, eliminando lo superfluo.
- **Growing** - refleja la naturaleza viva del sistema de diseño: debe ser capaz de evolucionar, incorporar nuevos patrones y adaptarse a necesidades emergentes sin romper la consistencia.

Ant Design proporciona **más de 60 componentes React** listos para producción, incluyendo elementos tan especializados como:

- **ProTable** - tabla avanzada con búsqueda, filtrado, ordenación y paginación integradas.
- **ProForm** - formularios complejos con validación, *layouts* adaptativos y flujos multietapa.
- **ProLayout** - sistema de *layout* completo con menú lateral colapsable, *breadcrumbs* automáticos y soporte multiidioma.

La personalización se realiza mediante un sistema de **tokens de diseño** que utiliza **CSS-in-JS** (anteriormente Less, ahora basado en la biblioteca `@ant-design/cssinjs`) y que permite modificar cualquier aspecto visual del sistema sin perder la capacidad de recibir actualizaciones.

### Cómo crear un sistema de diseño propio

La creación de un sistema de diseño propio es un proceso metódico que comienza mucho antes de escribir una sola línea de código.

1. **Inventario de interfaz.** El primer paso consiste en realizar un inventario exhaustivo de la interfaz existente, capturando pantallas de cada vista y estado de la aplicación. Este inventario visual se imprime o se dispone en un lienzo digital colaborativo, y el equipo procede a identificar y etiquetar todos los elementos recurrentes: botones, campos de formulario, tarjetas, modales, pestañas, tablas, listas y cualquier otro patrón que se repita.

2. **Auditoría de consistencia.** Sobre el inventario visual se identifican las divergencias: botones que miden **36px** en una pantalla y **40px** en otra, mismos colores con diferentes valores hexadecimales, tipografías inconsistentes entre secciones, espaciados que no siguen ninguna escala reconocible. Esta auditoría suele revelar un nivel de deuda de diseño mucho mayor del que el equipo percibía, y constituye el argumento más poderoso para justificar la inversión en un sistema de diseño.

3. **Principios de diseño.** Estos principios, que deben ser **específicos, accionables y memorables**, guiarán todas las decisiones futuras sobre el sistema. Ejemplos de buenos principios son: «Primero móvil, luego escritorio», «Accesible por defecto, no como idea tardía», «Cada componente debe funcionar en modo oscuro», o «El rendimiento no es negociable: ningún componente debe añadir más de **2KB** al *bundle*».

4. **Tokens de diseño.** Comenzando por los tokens globales (la paleta de colores completa, la escala tipográfica, la escala de espaciado), se construye progresivamente la capa semántica que asigna significado a cada token, y finalmente los tokens de componente que aplican los valores a contextos concretos. Este proceso se documenta en una **tabla de decisiones** donde se registra el razonamiento detrás de cada elección.

5. **Componentes.** Se recomienda comenzar por los **átomos** (botones, *inputs*, etiquetas, iconos), continuar con las **moléculas** (campos de formulario con etiqueta y error, barras de búsqueda) y avanzar hacia los **organismos** (tablas, formularios completos, cabeceras). Cada componente se desarrolla de forma aislada, se documenta con sus variantes y estados, y se somete a revisión antes de ser incorporado al sistema.

6. **Documentación.** Un sistema de diseño no documentado es un sistema de diseño muerto. La documentación debe incluir para cada componente: su propósito y casos de uso, ejemplos visuales de todas sus variantes y estados, el código necesario para implementarlo, directrices de accesibilidad, consideraciones de rendimiento y notas sobre cuándo no usar ese componente. Herramientas como **Storybook** facilitan este proceso al generar documentación interactiva directamente desde el código.

### Implementación técnica de sistemas de diseño

La implementación técnica de un sistema de diseño en el frontend web puede abordarse mediante diferentes estrategias, cada una con sus ventajas e inconvenientes.

**CSS Custom Properties (variables CSS nativas).** El enfoque más sencillo y con menos dependencias externas. Permite definir los tokens de diseño en el selector `:root` y consumirlos desde cualquier hoja de estilo. Las Custom Properties ofrecen ventajas significativas sobre las variables de preprocesador: son **dinámicas** (pueden modificarse en tiempo de ejecución con JavaScript), **heredan en cascada** y pueden redefinirse dentro de contextos específicos o *media queries*. Esto las hace ideales para implementar temas (claro/oscuro), modos de alto contraste o adaptaciones *responsive* directamente desde los tokens.

**SASS/SCSS.** Como preprocesador añade capacidades que las CSS Custom Properties por sí solas no proporcionan, como **funciones**, **mixins**, **bucles** y **condicionales**. Un sistema de diseño implementado con SASS suele organizarse en una arquitectura de carpetas que separa los tokens (variables), las funciones y mixins, los estilos base (*reset* y tipografía) y los componentes. Los mixins permiten encapsular patrones repetitivos como la creación de variantes de botones o la generación de la escala tipográfica a partir de una función matemática.

No obstante, SASS compila a CSS estático, por lo que pierde la capacidad dinámica de las Custom Properties.

!!! tip "Estrategia híbrida"
    La combinación más efectiva utiliza **variables SASS** para la configuración en tiempo de compilación y **CSS Custom Properties** para los valores que necesitan cambiar en tiempo de ejecución (*runtime*).

**Styled Components (CSS-in-JS).** Ofrece un enfoque radicalmente diferente donde los estilos se escriben en JavaScript y se asocian directamente a componentes React. Esta aproximación permite utilizar todo el potencial del lenguaje (lógica condicional, *props*, contextos, *theming*) para construir componentes estilizados dinámicamente. Un sistema de diseño implementado con Styled Components define un **ThemeProvider** que inyecta los tokens de diseño a través del contexto de React, y cada componente estilizado accede a ellos mediante una función que recibe el *theme* como parámetro. Esta arquitectura facilita enormemente la implementación de temas dinámicos y la personalización por contexto, aunque introduce una dependencia de *runtime* y puede tener implicaciones de rendimiento si no se gestiona cuidadosamente la generación de clases CSS.

**CSS Modules.** Representa un punto intermedio que ofrece **encapsulación de estilos** sin renunciar a la semántica de CSS. Cada archivo de módulo define estilos con ámbito local mediante nombres de clase generados automáticamente con *hash*, eliminando las colisiones y los problemas de especificidad. Un sistema de diseño con CSS Modules puede combinar variables CSS para los tokens globales con la importación de módulos para los estilos específicos de cada componente, proporcionando un equilibrio entre aislamiento, rendimiento y mantenibilidad que muchos equipos encuentran óptimo.

## Ejemplos guiados

### Ejemplo guiado 1: Creación de una paleta de colores como tokens de diseño

!!! example "Contexto pedagógico"
    En este primer ejemplo guiado, construiremos la capa fundamental de cualquier sistema de diseño: la **paleta de colores estructurada como tokens de diseño**. Partiremos de una selección de colores base y la transformaremos en un sistema completo de tokens anidados utilizando CSS Custom Properties.

Comenzamos definiendo los colores primitivos o globales. Estos colores no tienen significado semántico aún, simplemente representan los valores cromáticos puros de nuestra paleta:

```css
:root {
  /* ===== COLORES GLOBALES (PRIMITIVOS) ===== */
  --color-blue-50:  #E3F2FD;
  --color-blue-100: #BBDEFB;
  --color-blue-200: #90CAF9;
  --color-blue-300: #64B5F6;
  --color-blue-400: #42A5F5;
  --color-blue-500: #2196F3;
  --color-blue-600: #1E88E5;
  --color-blue-700: #1976D2;
  --color-blue-800: #1565C0;
  --color-blue-900: #0D47A1;

  --color-gray-50:  #FAFAFA;
  --color-gray-100: #F5F5F5;
  --color-gray-200: #EEEEEE;
  --color-gray-300: #E0E0E0;
  --color-gray-400: #BDBDBD;
  --color-gray-500: #9E9E9E;
  --color-gray-600: #757575;
  --color-gray-700: #616161;
  --color-gray-800: #424242;
  --color-gray-900: #212121;

  --color-green-500: #4CAF50;
  --color-green-600: #43A047;
  --color-red-500:   #F44336;
  --color-red-600:   #E53935;
  --color-yellow-500: #FFEB3B;
  --color-orange-500: #FF9800;
  --color-white:      #FFFFFF;
  --color-black:      #000000;
}
```

A continuación, creamos la capa de tokens semánticos o de alias. Aquí asignamos significado funcional a los colores primitivos, estableciendo qué color será el primario de la marca, cuáles serán los colores de texto sobre diferentes fondos, y los colores que comunican estados al usuario:

```css
:root {
  /* ===== TOKENS SEMÁNTICOS (ALIAS) ===== */

  /* Marca - Color primario */
  --color-primary-50:  var(--color-blue-50);
  --color-primary-100: var(--color-blue-100);
  --color-primary-200: var(--color-blue-200);
  --color-primary-300: var(--color-blue-300);
  --color-primary-400: var(--color-blue-400);
  --color-primary-500: var(--color-blue-500);
  --color-primary-600: var(--color-blue-600);
  --color-primary-700: var(--color-blue-700);
  --color-primary-800: var(--color-blue-800);
  --color-primary-900: var(--color-blue-900);

  /* Marca - Color secundario */
  --color-secondary-500: var(--color-orange-500);

  /* Superficies y fondos */
  --color-surface-background:   var(--color-gray-50);
  --color-surface-paper:        var(--color-white);
  --color-surface-elevated:     var(--color-white);
  --color-surface-overlay:      rgba(0, 0, 0, 0.5);

  /* Texto */
  --color-text-primary:      var(--color-gray-900);
  --color-text-secondary:    var(--color-gray-600);
  --color-text-disabled:     var(--color-gray-400);
  --color-text-on-primary:   var(--color-white);
  --color-text-on-secondary: var(--color-white);

  /* Estados semánticos */
  --color-success-main:    var(--color-green-500);
  --color-success-hover:   var(--color-green-600);
  --color-error-main:      var(--color-red-500);
  --color-error-hover:     var(--color-red-600);
  --color-warning-main:    var(--color-yellow-500);
  --color-info-main:       var(--color-blue-500);

  /* Bordes */
  --color-border-default: var(--color-gray-300);
  --color-border-focus:   var(--color-blue-500);
  --color-border-error:   var(--color-red-500);
}
```

Finalmente, creamos la capa de tokens específicos de componente. Estos tokens aplican los colores semánticos a contextos muy concretos, como el fondo y el texto de un botón primario en sus diferentes estados:

```css
:root {
  /* ===== TOKENS DE COMPONENTE ===== */

  /* Botón primario */
  --button-primary-background:       var(--color-primary-500);
  --button-primary-background-hover: var(--color-primary-600);
  --button-primary-background-focus: var(--color-primary-700);
  --button-primary-text:             var(--color-text-on-primary);
  --button-primary-border:           var(--color-primary-500);
  --button-primary-shadow:           0 2px 4px rgba(33, 150, 243, 0.3);

  /* Botón secundario (outlined) */
  --button-secondary-background:       transparent;
  --button-secondary-background-hover: var(--color-primary-50);
  --button-secondary-text:             var(--color-primary-500);
  --button-secondary-border:           var(--color-primary-500);

  /* Input de formulario */
  --input-background:          var(--color-surface-paper);
  --input-border:              var(--color-border-default);
  --input-border-focus:        var(--color-border-focus);
  --input-border-error:        var(--color-border-error);
  --input-text:                var(--color-text-primary);
  --input-placeholder:         var(--color-text-disabled);
  --input-label:               var(--color-text-secondary);

  /* Card */
  --card-background:       var(--color-surface-paper);
  --card-shadow:           0 1px 3px rgba(0, 0, 0, 0.12), 0 1px 2px rgba(0, 0, 0, 0.08);
  --card-shadow-hover:     0 4px 6px rgba(0, 0, 0, 0.12), 0 2px 4px rgba(0, 0, 0, 0.08);
  --card-border-radius:    8px;
  --card-padding:          var(--spacing-6);

  /* Badge / Chip */
  --badge-success-background: var(--color-success-main);
  --badge-success-text:       var(--color-white);
  --badge-error-background:   var(--color-error-main);
  --badge-error-text:         var(--color-white);
}
```

!!! note "Explicación del resultado"
    Esta arquitectura en tres capas permite cambiar el color primario de toda la aplicación **modificando una única línea** en los tokens de alias, sin necesidad de tocar ningún componente individual. Por ejemplo, para cambiar el color primario de azul a verde, bastaría con modificar `--color-primary-500: var(--color-green-500)` en la capa semántica, y todos los botones, enlaces, *badges* y cualquier otro elemento que utilice el color primario se actualizarían automáticamente.

### Ejemplo guiado 2: Sistema tipográfico completo con escala modular

!!! example "Contexto pedagógico"
    En este ejemplo diseñaremos un sistema tipográfico completo basado en una **escala modular** (*perfect fourth*, factor **1.333**) que se adapta *responsive* mediante tokens de diseño y `clamp()` para fluidez:

```css
:root {
  /* ===== TOKENS TIPOGRÁFICOS ===== */

  /* Familias tipográficas */
  --font-family-primary:    'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --font-family-secondary:  'Merriweather', Georgia, 'Times New Roman', serif;
  --font-family-mono:       'JetBrains Mono', 'Fira Code', 'Cascadia Code', monospace;

  /* Pesos tipográficos */
  --font-weight-light:      300;
  --font-weight-regular:    400;
  --font-weight-medium:     500;
  --font-weight-semibold:   600;
  --font-weight-bold:       700;

  /* Escala tipográfica base móvil (factor 1.2 - minor third) */
  --font-size-xs:   0.75rem;    /* 12px */
  --font-size-sm:   0.875rem;   /* 14px */
  --font-size-base: 1rem;       /* 16px */
  --font-size-md:   1.125rem;   /* 18px */
  --font-size-lg:   1.25rem;    /* 20px */
  --font-size-xl:   1.5rem;     /* 24px */
  --font-size-2xl:  1.875rem;   /* 30px */
  --font-size-3xl:  2.25rem;    /* 36px */
  --font-size-4xl:  3rem;       /* 48px */

  /* Alturas de línea */
  --line-height-tight:   1.25;   /* Títulos */
  --line-height-normal:  1.5;    /* Cuerpo */
  --line-height-relaxed: 1.75;   /* Texto largo */

  /* Letter spacing */
  --letter-spacing-tight:   -0.02em;
  --letter-spacing-normal:   0;
  --letter-spacing-wide:     0.05em;
  --letter-spacing-wider:    0.1em;
}

/* Escala tipográfica responsive para escritorio */
@media (min-width: 768px) {
  :root {
    --font-size-xs:   0.75rem;    /* 12px */
    --font-size-sm:   0.875rem;   /* 14px */
    --font-size-base: 1rem;       /* 16px */
    --font-size-md:   1.25rem;    /* 20px */
    --font-size-lg:   1.5rem;     /* 24px */
    --font-size-xl:   2rem;       /* 32px */
    --font-size-2xl:  2.5rem;     /* 40px */
    --font-size-3xl:  3rem;       /* 48px */
    --font-size-4xl:  4rem;       /* 64px */
  }
}

/* Tokens de componente tipográfico */
:root {
  /* Heading 1 */
  --heading-1-font-size:       var(--font-size-4xl);
  --heading-1-font-weight:     var(--font-weight-bold);
  --heading-1-line-height:     var(--line-height-tight);
  --heading-1-letter-spacing:  var(--letter-spacing-tight);
  --heading-1-color:           var(--color-text-primary);
  --heading-1-margin-bottom:   var(--spacing-4);

  /* Heading 2 */
  --heading-2-font-size:       var(--font-size-3xl);
  --heading-2-font-weight:     var(--font-weight-semibold);
  --heading-2-line-height:     var(--line-height-tight);
  --heading-2-color:           var(--color-text-primary);
  --heading-2-margin-bottom:   var(--spacing-3);

  /* Heading 3 */
  --heading-3-font-size:       var(--font-size-2xl);
  --heading-3-font-weight:     var(--font-weight-semibold);
  --heading-3-line-height:     var(--line-height-tight);
  --heading-3-color:           var(--color-text-primary);
  --heading-3-margin-bottom:   var(--spacing-2);

  /* Body text */
  --body-font-size:            var(--font-size-base);
  --body-font-weight:          var(--font-weight-regular);
  --body-line-height:          var(--line-height-normal);
  --body-color:                var(--color-text-primary);

  /* Body small */
  --body-small-font-size:      var(--font-size-sm);
  --body-small-line-height:    var(--line-height-normal);
  --body-small-color:          var(--color-text-secondary);

  /* Caption / Label */
  --caption-font-size:         var(--font-size-xs);
  --caption-font-weight:       var(--font-weight-medium);
  --caption-line-height:       var(--line-height-normal);
  --caption-color:             var(--color-text-secondary);
  --caption-letter-spacing:    var(--letter-spacing-wide);
  --caption-text-transform:    uppercase;

  /* Overline */
  --overline-font-size:        var(--font-size-xs);
  --overline-font-weight:      var(--font-weight-semibold);
  --overline-letter-spacing:   var(--letter-spacing-wider);
  --overline-text-transform:   uppercase;

  /* Link */
  --link-color:                var(--color-primary-600);
  --link-color-hover:          var(--color-primary-700);
  --link-text-decoration:      underline;
}
```

A continuación implementamos las clases CSS que consumen estos tokens. Utilizamos una aproximación utility-first que nos permite aplicar la tipografía del sistema a cualquier elemento HTML mediante clases semánticas:

```css
/* ===== ESTILOS TIPOGRÁFICOS BASE ===== */

/* Reset y base tipográfica */
html {
  font-size: 16px;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-rendering: optimizeLegibility;
}

body {
  font-family: var(--font-family-primary);
  font-size: var(--body-font-size);
  font-weight: var(--body-font-weight);
  line-height: var(--body-line-height);
  color: var(--body-color);
}

/* Clases de utilidad tipográfica */
.heading-1 {
  font-size: var(--heading-1-font-size);
  font-weight: var(--heading-1-font-weight);
  line-height: var(--heading-1-line-height);
  letter-spacing: var(--heading-1-letter-spacing);
  color: var(--heading-1-color);
  margin-bottom: var(--heading-1-margin-bottom);
}

.heading-2 {
  font-size: var(--heading-2-font-size);
  font-weight: var(--heading-2-font-weight);
  line-height: var(--heading-2-line-height);
  color: var(--heading-2-color);
  margin-bottom: var(--heading-2-margin-bottom);
}

.heading-3 {
  font-size: var(--heading-3-font-size);
  font-weight: var(--heading-3-font-weight);
  line-height: var(--heading-3-line-height);
  color: var(--heading-3-color);
  margin-bottom: var(--heading-3-margin-bottom);
}

.body-text {
  font-size: var(--body-font-size);
  font-weight: var(--body-font-weight);
  line-height: var(--body-line-height);
  color: var(--body-color);
}

.body-small {
  font-size: var(--body-small-font-size);
  line-height: var(--body-small-line-height);
  color: var(--body-small-color);
}

.caption {
  font-size: var(--caption-font-size);
  font-weight: var(--caption-font-weight);
  line-height: var(--caption-line-height);
  color: var(--caption-color);
  letter-spacing: var(--caption-letter-spacing);
  text-transform: var(--caption-text-transform);
}

.overline {
  font-size: var(--overline-font-size);
  font-weight: var(--overline-font-weight);
  letter-spacing: var(--overline-letter-spacing);
  text-transform: var(--overline-text-transform);
}

.text-link {
  color: var(--link-color);
  text-decoration: var(--link-text-decoration);
  cursor: pointer;
  transition: color 0.2s ease;
}

.text-link:hover {
  color: var(--link-color-hover);
}
```

!!! note "Explicación del resultado"
    Este sistema tipográfico se beneficia de la arquitectura de tokens porque podemos ajustar cualquier aspecto de la tipografía **desde un único lugar**. Si el equipo de diseño decide cambiar la familia tipográfica o la escala, basta con modificar los tokens en `:root`. Además, al utilizar *rem* como unidad base, respetamos las preferencias de tamaño de fuente del usuario, cumpliendo con el criterio de accesibilidad **WCAG 1.4.4** sobre redimensionamiento de texto.

### Ejemplo guiado 3: Construcción de un sistema de botones completo

!!! example "Contexto pedagógico"
    En este tercer ejemplo guiado, construiremos un componente de botón completo con múltiples **variantes**, **tamaños** y **estados** que consume los tokens de diseño definidos anteriormente. Este componente ejemplifica cómo un sistema de diseño traslada las decisiones de diseño a código reutilizable:

```css
/* ===== SISTEMA DE BOTONES ===== */

/* Estilos base del botón (compartidos por todas las variantes) */
.btn {
  /* Layout */
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--spacing-2);
  vertical-align: middle;
  text-align: center;
  white-space: nowrap;
  text-decoration: none;

  /* Dimensiones */
  padding: var(--button-padding-y, var(--spacing-2))
           var(--button-padding-x, var(--spacing-4));
  height: var(--button-height, 40px);

  /* Tipografía */
  font-family: var(--font-family-primary);
  font-weight: var(--font-weight-medium);
  font-size: var(--button-font-size, var(--font-size-sm));
  line-height: 1;

  /* Visual */
  border: 2px solid transparent;
  border-radius: var(--button-border-radius, 6px);
  cursor: pointer;
  user-select: none;
  transition: all 0.2s ease-in-out;

  /* Estados */
  outline: none;
}

/* Foco visible solo para navegación por teclado */
.btn:focus-visible {
  box-shadow: 0 0 0 3px var(--color-border-focus);
}

/* Estado deshabilitado compartido */
.btn:disabled,
.btn[aria-disabled="true"] {
  opacity: 0.5;
  cursor: not-allowed;
  pointer-events: none;
}

/* ===== VARIANTES DE BOTÓN ===== */

/* Variante: Primary (filled) */
.btn--primary {
  background-color: var(--button-primary-background);
  color: var(--button-primary-text);
  border-color: var(--button-primary-border);
  box-shadow: var(--button-primary-shadow);
}

.btn--primary:hover:not(:disabled) {
  background-color: var(--button-primary-background-hover);
  box-shadow: 0 4px 8px rgba(33, 150, 243, 0.35);
  transform: translateY(-1px);
}

.btn--primary:active:not(:disabled) {
  background-color: var(--button-primary-background-focus);
  box-shadow: 0 1px 2px rgba(33, 150, 243, 0.2);
  transform: translateY(0);
}

/* Variante: Secondary (outlined) */
.btn--secondary {
  background-color: transparent;
  color: var(--color-primary-500);
  border-color: var(--color-primary-500);
}

.btn--secondary:hover:not(:disabled) {
  background-color: var(--color-primary-50);
  border-color: var(--color-primary-600);
  color: var(--color-primary-600);
}

.btn--secondary:active:not(:disabled) {
  background-color: var(--color-primary-100);
}

/* Variante: Ghost (text-only) */
.btn--ghost {
  background-color: transparent;
  color: var(--color-primary-500);
  border-color: transparent;
}

.btn--ghost:hover:not(:disabled) {
  background-color: var(--color-primary-50);
}

.btn--ghost:active:not(:disabled) {
  background-color: var(--color-primary-100);
}

/* Variante: Danger */
.btn--danger {
  background-color: var(--color-red-500);
  color: var(--color-white);
  border-color: var(--color-red-500);
}

.btn--danger:hover:not(:disabled) {
  background-color: var(--color-red-600);
  border-color: var(--color-red-600);
}

.btn--danger:active:not(:disabled) {
  background-color: #C62828;
}

/* ===== TAMAÑOS DE BOTÓN ===== */

/* Small: para espacios reducidos, tablas, barras de herramientas */
.btn--sm {
  --button-height: 32px;
  --button-padding-x: var(--spacing-3);
  --button-padding-y: var(--spacing-1);
  --button-font-size: var(--font-size-xs);
  --button-border-radius: 4px;
}

/* Medium: tamaño por defecto para la mayoría de casos de uso */
.btn--md {
  --button-height: 40px;
  --button-padding-x: var(--spacing-4);
  --button-padding-y: var(--spacing-2);
  --button-font-size: var(--font-size-sm);
  --button-border-radius: 6px;
}

/* Large: para CTAs principales, hero sections, landing pages */
.btn--lg {
  --button-height: 48px;
  --button-padding-x: var(--spacing-6);
  --button-padding-y: var(--spacing-3);
  --button-font-size: var(--font-size-base);
  --button-border-radius: 8px;
}

/* ===== BOTONES CON ICONO ===== */

/* Icono al inicio del texto del botón */
.btn__icon {
  width: 1.25em;
  height: 1.25em;
  flex-shrink: 0;
}

/* Botón solo icono (circular o cuadrado) */
.btn--icon-only {
  --button-padding-x: 0;
  --button-padding-y: 0;
  width: var(--button-height);
  padding: 0;
  border-radius: 50%;
}

.btn--icon-only.btn--sm { width: 32px; }
.btn--icon-only.btn--md { width: 40px; }
.btn--icon-only.btn--lg { width: 48px; }

/* Botón full-width */
.btn--block {
  display: flex;
  width: 100%;
}

/* Grupo de botones (botones unidos horizontalmente) */
.btn-group {
  display: inline-flex;
}

.btn-group .btn {
  border-radius: 0;
}

.btn-group .btn:first-child {
  border-radius: 6px 0 0 6px;
}

.btn-group .btn:last-child {
  border-radius: 0 6px 6px 0;
}

.btn-group .btn + .btn {
  margin-left: -2px;
}

.btn-group .btn:focus-visible {
  z-index: 1;
}
```

El HTML correspondiente para utilizar este sistema de botones es sencillo y semántico. Cada botón se compone de una clase base `.btn` más un modificador de variante y otro de tamaño, siguiendo la metodología BEM:

```html
<!-- Botón primario, tamaño por defecto -->
<button class="btn btn--primary btn--md" type="button">
  Guardar cambios
</button>

<!-- Botón secundario con icono -->
<button class="btn btn--secondary btn--md" type="button">
  <svg class="btn__icon" viewBox="0 0 24 24" aria-hidden="true">
    <path d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
    <path fill-rule="evenodd" d="M12 2C6.477 2 2 6.477 2 12s4.477 10 10 10 10-4.477 10-10S17.523 2 12 2z"/>
  </svg>
  Ver detalles
</button>

<!-- Botón de peligro, pequeño, deshabilitado -->
<button class="btn btn--danger btn--sm" type="button" disabled>
  Eliminar cuenta
</button>

<!-- Botón solo icono (ghost) -->
<button class="btn btn--ghost btn--icon-only btn--md" type="button"
        aria-label="Cerrar ventana">
  <svg class="btn__icon" viewBox="0 0 24 24" aria-hidden="true">
    <path d="M6 6l12 12M6 18L18 6"/>
  </svg>
</button>

<!-- Botón full-width para mobile -->
<button class="btn btn--primary btn--lg btn--block" type="submit">
  Completar pedido — 24,99€
</button>

<!-- Grupo de botones -->
<div class="btn-group" role="group" aria-label="Acciones del documento">
  <button class="btn btn--secondary btn--sm">Editar</button>
  <button class="btn btn--secondary btn--sm">Duplicar</button>
  <button class="btn btn--danger btn--sm">Eliminar</button>
</div>
```

### Ejemplo guiado 4: Sistema de espaciado y grid con tokens

!!! example "Contexto pedagógico"
    Construimos ahora el sistema de espaciado basado en una cuadrícula de **4px** y el sistema de *grid* *responsive* de **12 columnas**, ambos integrados mediante tokens de diseño:

```css
:root {
  /* ===== TOKENS DE ESPACIADO (escala basada en 4px) ===== */
  --spacing-0:  0;
  --spacing-1:  0.25rem;  /* 4px  - mínima separación */
  --spacing-2:  0.5rem;   /* 8px  - icono a texto, elementos compactos */
  --spacing-3:  0.75rem;  /* 12px - padding pequeño */
  --spacing-4:  1rem;     /* 16px - padding estándar, gutter de grid */
  --spacing-5:  1.25rem;  /* 20px */
  --spacing-6:  1.5rem;   /* 24px - padding de card, separación de secciones */
  --spacing-8:  2rem;     /* 32px - margen de layout */
  --spacing-10: 2.5rem;   /* 40px - separación entre secciones grandes */
  --spacing-12: 3rem;     /* 48px */
  --spacing-16: 4rem;     /* 64px - separación hero, footer */
  --spacing-20: 5rem;     /* 80px */

  /* ===== TOKENS DE GRID ===== */
  --grid-columns:            12;
  --grid-gutter:             var(--spacing-4);   /* Espacio entre columnas */
  --grid-margin-mobile:      var(--spacing-4);   /* Márgenes laterales en móvil */
  --grid-margin-tablet:      var(--spacing-8);   /* Márgenes laterales en tablet */
  --grid-margin-desktop:     auto;               /* Centrado en escritorio */

  --grid-max-width:          1200px;             /* Ancho máximo del contenedor */
  --grid-breakpoint-sm:      576px;
  --grid-breakpoint-md:      768px;
  --grid-breakpoint-lg:      992px;
  --grid-breakpoint-xl:      1200px;
  --grid-breakpoint-xxl:     1400px;
}

/* ===== SISTEMA DE GRID CSS ===== */

/* Contenedor principal */
.container {
  width: 100%;
  max-width: var(--grid-max-width);
  margin-left: auto;
  margin-right: auto;
  padding-left: var(--grid-margin-mobile);
  padding-right: var(--grid-margin-mobile);
}

@media (min-width: 768px) {
  .container {
    padding-left: var(--grid-margin-tablet);
    padding-right: var(--grid-margin-tablet);
  }
}

@media (min-width: 1200px) {
  .container {
    padding-left: 0;
    padding-right: 0;
  }
}

/* Fila del grid */
.row {
  display: flex;
  flex-wrap: wrap;
  margin-left: calc(-1 * var(--grid-gutter) / 2);
  margin-right: calc(-1 * var(--grid-gutter) / 2);
}

/* Columnas base */
[class*="col-"] {
  flex: 0 0 auto;
  width: 100%;
  padding-left: calc(var(--grid-gutter) / 2);
  padding-right: calc(var(--grid-gutter) / 2);
}

/* Sistema de columnas responsive para escritorio (≥992px) */
@media (min-width: 992px) {
  .col-1  { width: 8.333333%; }
  .col-2  { width: 16.666667%; }
  .col-3  { width: 25%; }
  .col-4  { width: 33.333333%; }
  .col-5  { width: 41.666667%; }
  .col-6  { width: 50%; }
  .col-7  { width: 58.333333%; }
  .col-8  { width: 66.666667%; }
  .col-9  { width: 75%; }
  .col-10 { width: 83.333333%; }
  .col-11 { width: 91.666667%; }
  .col-12 { width: 100%; }
}

/* Columnas para tablet (768px a 991px) */
@media (min-width: 768px) and (max-width: 991px) {
  .col-md-1  { width: 8.333333%; }
  .col-md-2  { width: 16.666667%; }
  .col-md-3  { width: 25%; }
  .col-md-4  { width: 33.333333%; }
  .col-md-5  { width: 41.666667%; }
  .col-md-6  { width: 50%; }
  .col-md-7  { width: 58.333333%; }
  .col-md-8  { width: 66.666667%; }
  .col-md-9  { width: 75%; }
  .col-md-10 { width: 83.333333%; }
  .col-md-11 { width: 91.666667%; }
  .col-md-12 { width: 100%; }
}

/* Columnas para móvil pequeño (<576px) */
@media (max-width: 575px) {
  .col-sm-1  { width: 8.333333%; }
  .col-sm-2  { width: 16.666667%; }
  .col-sm-3  { width: 25%; }
  .col-sm-4  { width: 33.333333%; }
  .col-sm-6  { width: 50%; }
  .col-sm-12 { width: 100%; }
}

/* Utilidades de espaciado */
.m-0  { margin: var(--spacing-0); }
.m-1  { margin: var(--spacing-1); }
.m-2  { margin: var(--spacing-2); }
.m-3  { margin: var(--spacing-3); }
.m-4  { margin: var(--spacing-4); }
.m-6  { margin: var(--spacing-6); }
.m-8  { margin: var(--spacing-8); }
.m-12 { margin: var(--spacing-12); }
.m-16 { margin: var(--spacing-16); }

.mt-4 { margin-top: var(--spacing-4); }
.mb-4 { margin-bottom: var(--spacing-4); }
.ml-4 { margin-left: var(--spacing-4); }
.mr-4 { margin-right: var(--spacing-4); }
.mx-auto { margin-left: auto; margin-right: auto; }

.p-0  { padding: var(--spacing-0); }
.p-1  { padding: var(--spacing-1); }
.p-2  { padding: var(--spacing-2); }
.p-3  { padding: var(--spacing-3); }
.p-4  { padding: var(--spacing-4); }
.p-6  { padding: var(--spacing-6); }
.p-8  { padding: var(--spacing-8); }
.p-12 { padding: var(--spacing-12); }

.pt-4 { padding-top: var(--spacing-4); }
.pb-4 { padding-bottom: var(--spacing-4); }
.pl-4 { padding-left: var(--spacing-4); }
.pr-4 { padding-right: var(--spacing-4); }
```

### Ejemplo guiado 5: Componente de tarjeta (Card) con todas las variantes

!!! example "Contexto pedagógico"
    Desarrollamos a continuación un componente **Card** que demuestra cómo los tokens de diseño se aplican a componentes compuestos, con soporte para diferentes variantes de *layout* y contenido:

```css
/* ===== SISTEMA DE TARJETAS (CARDS) ===== */

/* Estructura base de la card */
.card {
  display: flex;
  flex-direction: column;
  background-color: var(--card-background);
  border-radius: var(--card-border-radius);
  box-shadow: var(--card-shadow);
  overflow: hidden;
  transition: box-shadow 0.3s ease, transform 0.3s ease;
}

/* Elevación al hacer hover */
.card--hoverable:hover {
  box-shadow: var(--card-shadow-hover);
  transform: translateY(-2px);
}

/* Variante bordered: borde en lugar de sombra */
.card--bordered {
  box-shadow: none;
  border: 1px solid var(--color-border-default);
}

.card--bordered:hover {
  box-shadow: none;
  border-color: var(--color-primary-300);
}

/* Contenedor de imagen en la card */
.card__media {
  position: relative;
  width: 100%;
  overflow: hidden;
}

.card__media img {
  display: block;
  width: 100%;
  height: auto;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.card:hover .card__media img {
  transform: scale(1.05);
}

/* Relación de aspecto 16:9 para la imagen */
.card__media--16x9 {
  aspect-ratio: 16 / 9;
}

.card__media--16x9 img {
  height: 100%;
  object-fit: cover;
}

/* Relación de aspecto 4:3 */
.card__media--4x3 {
  aspect-ratio: 4 / 3;
}

.card__media--4x3 img {
  height: 100%;
  object-fit: cover;
}

/* Cuerpo de la card */
.card__body {
  flex: 1 1 auto;
  padding: var(--card-padding);
}

/* Título de la card */
.card__title {
  font-size: var(--font-size-lg);
  font-weight: var(--font-weight-semibold);
  line-height: var(--line-height-tight);
  color: var(--color-text-primary);
  margin-bottom: var(--spacing-2);
}

/* Subtítulo */
.card__subtitle {
  font-size: var(--font-size-sm);
  font-weight: var(--font-weight-regular);
  color: var(--color-text-secondary);
  margin-bottom: var(--spacing-3);
}

/* Texto descriptivo */
.card__text {
  font-size: var(--font-size-sm);
  line-height: var(--line-height-relaxed);
  color: var(--color-text-secondary);
  margin-bottom: var(--spacing-4);
}

/* Pie de la card (acciones) */
.card__footer {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: var(--spacing-2);
  padding: var(--spacing-3) var(--card-padding);
  border-top: 1px solid var(--color-border-default);
}

/* Card horizontal (imagen a la izquierda, contenido a la derecha) */
.card--horizontal {
  flex-direction: row;
}

.card--horizontal .card__media {
  width: 200px;
  flex-shrink: 0;
  height: auto;
}

.card--horizontal .card__media img {
  height: 100%;
  object-fit: cover;
}

.card--horizontal .card__body {
  display: flex;
  flex-direction: column;
  justify-content: center;
}

/* Card con overlay en la imagen */
.card__media-overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: var(--spacing-6) var(--spacing-4) var(--spacing-4);
  background: linear-gradient(to top, rgba(0,0,0,0.7), transparent);
  color: var(--color-white);
}

.card__media-overlay .card__title {
  color: var(--color-white);
  margin-bottom: var(--spacing-1);
}

.card__media-overlay .card__subtitle {
  color: rgba(255, 255, 255, 0.8);
}

/* Grid de cards */
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: var(--spacing-6);
}

@media (max-width: 575px) {
  .card-grid {
    grid-template-columns: 1fr;
  }
}
```

El HTML correspondiente para el componente Card:

```html
<!-- Card estándar con imagen, título, texto y acciones -->
<article class="card card--hoverable">
  <div class="card__media card__media--16x9">
    <img src="proyecto-dashboard.jpg" alt="Dashboard del proyecto con gráficos de rendimiento" loading="lazy">
  </div>
  <div class="card__body">
    <h3 class="card__title">Dashboard analytics</h3>
    <p class="card__subtitle">Actualizado hace 2 horas</p>
    <p class="card__text">
      Visualiza las métricas clave de tu negocio en tiempo real con nuestro nuevo panel de control. Incluye gráficos interactivos, filtros avanzados y exportación de datos.
    </p>
  </div>
  <div class="card__footer">
    <button class="btn btn--ghost btn--sm">Compartir</button>
    <button class="btn btn--primary btn--sm">Explorar</button>
  </div>
</article>

<!-- Card horizontal -->
<article class="card card--horizontal card--hoverable">
  <div class="card__media card__media--4x3">
    <img src="perfil-usuario.jpg" alt="Foto de perfil de María García" loading="lazy">
  </div>
  <div class="card__body">
    <h3 class="card__title">María García</h3>
    <p class="card__subtitle">Senior Frontend Developer</p>
    <p class="card__text">Especialista en React, TypeScript y sistemas de diseño. 8 años de experiencia en desarrollo de interfaces.</p>
  </div>
</article>
```

### Ejemplo guiado 6: Formularios con tokens de diseño

!!! example "Contexto pedagógico"
    Cerramos los ejemplos guiados con un sistema completo de formularios que integra todos los tokens definidos hasta ahora, incluyendo **validación visual**, **mensajes de ayuda** y **estados de error**:

```css
/* ===== SISTEMA DE FORMULARIOS ===== */

/* Grupo de campo (etiqueta + input + feedback) */
.form-group {
  margin-bottom: var(--spacing-6);
}

/* Etiqueta */
.form-label {
  display: block;
  font-size: var(--font-size-sm);
  font-weight: var(--font-weight-medium);
  color: var(--input-label);
  margin-bottom: var(--spacing-1);
}

/* Indicador de campo requerido */
.form-label--required::after {
  content: " *";
  color: var(--color-error-main);
  font-weight: var(--font-weight-bold);
}

/* Estilos base de inputs */
.form-input,
.form-select,
.form-textarea {
  display: block;
  width: 100%;
  padding: var(--spacing-2) var(--spacing-3);
  font-family: var(--font-family-primary);
  font-size: var(--font-size-base);
  line-height: var(--line-height-normal);
  color: var(--input-text);
  background-color: var(--input-background);
  border: 1px solid var(--input-border);
  border-radius: 6px;
  transition: border-color 0.2s ease, box-shadow 0.2s ease;
  appearance: none;
}

/* Placeholder */
.form-input::placeholder,
.form-textarea::placeholder {
  color: var(--input-placeholder);
  opacity: 1;
}

/* Foco */
.form-input:focus,
.form-select:focus,
.form-textarea:focus {
  outline: none;
  border-color: var(--input-border-focus);
  box-shadow: 0 0 0 3px rgba(33, 150, 243, 0.15);
}

/* Select personalizado */
.form-select {
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 12 12'%3E%3Cpath fill='%23757575' d='M6 8L1 3h10z'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 12px center;
  padding-right: 36px;
  cursor: pointer;
}

/* Textarea */
.form-textarea {
  min-height: 120px;
  resize: vertical;
}

/* Texto de ayuda */
.form-help {
  display: block;
  font-size: var(--font-size-xs);
  color: var(--color-text-secondary);
  margin-top: var(--spacing-1);
}

/* ===== ESTADOS DE VALIDACIÓN ===== */

/* Estado válido */
.form-input.is-valid,
.form-select.is-valid,
.form-textarea.is-valid {
  border-color: var(--color-success-main);
}

.form-input.is-valid:focus,
.form-select.is-valid:focus,
.form-textarea.is-valid:focus {
  box-shadow: 0 0 0 3px rgba(76, 175, 80, 0.15);
}

/* Estado inválido / error */
.form-input.is-invalid,
.form-select.is-invalid,
.form-textarea.is-invalid {
  border-color: var(--input-border-error);
}

.form-input.is-invalid:focus,
.form-select.is-invalid:focus,
.form-textarea.is-invalid:focus {
  box-shadow: 0 0 0 3px rgba(244, 67, 54, 0.15);
}

/* Mensaje de error */
.form-error {
  display: flex;
  align-items: center;
  gap: var(--spacing-1);
  font-size: var(--font-size-xs);
  color: var(--input-border-error);
  margin-top: var(--spacing-1);
}

.form-error::before {
  content: "";
  display: inline-block;
  width: 14px;
  height: 14px;
  flex-shrink: 0;
  background: currentColor;
  mask: url("data:image/svg+xml,%3Csvg viewBox='0 0 24 24' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z'/%3E%3C/svg%3E") center / contain no-repeat;
}

/* Mensaje de éxito */
.form-success {
  display: flex;
  align-items: center;
  gap: var(--spacing-1);
  font-size: var(--font-size-xs);
  color: var(--color-success-main);
  margin-top: var(--spacing-1);
}

/* ===== CHECKBOX Y RADIO PERSONALIZADOS ===== */

.form-check {
  display: flex;
  align-items: flex-start;
  gap: var(--spacing-2);
  cursor: pointer;
  font-size: var(--font-size-sm);
  color: var(--color-text-primary);
  line-height: var(--line-height-normal);
}

.form-check input[type="checkbox"],
.form-check input[type="radio"] {
  appearance: none;
  width: 20px;
  height: 20px;
  flex-shrink: 0;
  border: 2px solid var(--color-border-default);
  background-color: var(--input-background);
  cursor: pointer;
  transition: all 0.2s ease;
  position: relative;
  top: 1px;
}

.form-check input[type="checkbox"] {
  border-radius: 4px;
}

.form-check input[type="radio"] {
  border-radius: 50%;
}

.form-check input[type="checkbox"]:checked {
  background-color: var(--color-primary-500);
  border-color: var(--color-primary-500);
}

.form-check input[type="radio"]:checked {
  border-color: var(--color-primary-500);
  box-shadow: inset 0 0 0 4px var(--color-primary-500);
}

.form-check input[type="checkbox"]:checked::after {
  content: "";
  position: absolute;
  left: 5px;
  top: 2px;
  width: 6px;
  height: 10px;
  border: solid white;
  border-width: 0 2px 2px 0;
  transform: rotate(45deg);
}

.form-check input:focus-visible {
  outline: 2px solid var(--color-border-focus);
  outline-offset: 2px;
}

.form-check input:disabled,
.form-check input:disabled + * {
  opacity: 0.5;
  cursor: not-allowed;
}

/* ===== FORMULARIO INLINE Y HORIZONTAL ===== */

.form-inline {
  display: flex;
  align-items: flex-end;
  gap: var(--spacing-3);
  flex-wrap: wrap;
}

.form-inline .form-group {
  margin-bottom: 0;
  flex: 1;
  min-width: 200px;
}

/* Layout horizontal con etiqueta a la izquierda */
.form-horizontal .form-group {
  display: grid;
  grid-template-columns: 200px 1fr;
  gap: var(--spacing-4);
  align-items: start;
}

.form-horizontal .form-label {
  padding-top: var(--spacing-2);
  text-align: right;
}

.form-horizontal .form-help,
.form-horizontal .form-error {
  grid-column: 2;
}

@media (max-width: 767px) {
  .form-horizontal .form-group {
    grid-template-columns: 1fr;
  }

  .form-horizontal .form-label {
    text-align: left;
  }

  .form-horizontal .form-help,
  .form-horizontal .form-error {
    grid-column: 1;
  }
}
```

Ejemplo de formulario completo que integra todos los componentes:

```html
<form novalidate class="form-horizontal" aria-label="Formulario de registro">
  <!-- Campo de texto simple -->
  <div class="form-group">
    <label for="nombre" class="form-label form-label--required">Nombre completo</label>
    <input type="text" id="nombre" name="nombre" class="form-input"
           placeholder="Ej: María García López" required
           aria-describedby="nombre-help">
    <span id="nombre-help" class="form-help">Introduce tu nombre y apellidos tal como figuran en tu DNI.</span>
  </div>

  <!-- Campo de email con error -->
  <div class="form-group">
    <label for="email" class="form-label form-label--required">Correo electrónico</label>
    <input type="email" id="email" name="email"
           class="form-input is-invalid"
           placeholder="maria@ejemplo.com" required
           aria-describedby="email-error" aria-invalid="true">
    <span id="email-error" class="form-error" role="alert">El formato del correo electrónico no es válido.</span>
  </div>

  <!-- Campo de select -->
  <div class="form-group">
    <label for="rol" class="form-label form-label--required">Rol profesional</label>
    <select id="rol" name="rol" class="form-select" required>
      <option value="" disabled selected>Selecciona tu rol</option>
      <option value="frontend">Frontend Developer</option>
      <option value="backend">Backend Developer</option>
      <option value="fullstack">Full Stack Developer</option>
      <option value="design">UX/UI Designer</option>
    </select>
  </div>

  <!-- Campo textarea -->
  <div class="form-group">
    <label for="bio" class="form-label">Biografía profesional</label>
    <textarea id="bio" name="bio" class="form-textarea"
              placeholder="Cuéntanos brevemente tu experiencia y especialización..."
              maxlength="500"></textarea>
    <span class="form-help">Máximo 500 caracteres.</span>
  </div>

  <!-- Checkboxes agrupados -->
  <div class="form-group">
    <span class="form-label">Tecnologías que dominas</span>
    <div style="display: flex; flex-wrap: wrap; gap: var(--spacing-3);">
      <label class="form-check">
        <input type="checkbox" name="tech" value="react" checked>
        <span>React</span>
      </label>
      <label class="form-check">
        <input type="checkbox" name="tech" value="vue">
        <span>Vue.js</span>
      </label>
      <label class="form-check">
        <input type="checkbox" name="tech" value="angular">
        <span>Angular</span>
      </label>
      <label class="form-check">
        <input type="checkbox" name="tech" value="svelte">
        <span>Svelte</span>
      </label>
    </div>
  </div>

  <!-- Radio buttons -->
  <div class="form-group">
    <span class="form-label form-label--required">Modalidad de trabajo</span>
    <div style="display: flex; flex-wrap: wrap; gap: var(--spacing-4);">
      <label class="form-check">
        <input type="radio" name="modalidad" value="presencial" required>
        <span>Presencial</span>
      </label>
      <label class="form-check">
        <input type="radio" name="modalidad" value="remoto" checked>
        <span>Remoto</span>
      </label>
      <label class="form-check">
        <input type="radio" name="modalidad" value="hibrido">
        <span>Híbrido</span>
      </label>
    </div>
  </div>

  <!-- Checkbox de aceptación -->
  <div class="form-group">
    <label class="form-check">
      <input type="checkbox" name="terminos" required>
      <span>Acepto los <a href="/terminos" class="text-link">términos y condiciones</a> y la <a href="/privacidad" class="text-link">política de privacidad</a></span>
    </label>
  </div>

  <!-- Acciones del formulario -->
  <div style="display: flex; gap: var(--spacing-3); justify-content: flex-end; margin-top: var(--spacing-6);">
    <button type="reset" class="btn btn--secondary btn--md">Cancelar</button>
    <button type="submit" class="btn btn--primary btn--lg">Crear cuenta</button>
  </div>
</form>
```

## Casos reales

### Caso real 1: Material Design en el ecosistema de aplicaciones de Google

Google representa el caso de estudio más ambicioso de implementación de un sistema de diseño a escala planetaria. Antes de Material Design, cada producto de Google poseía su propia identidad visual: Gmail utilizaba una paleta de rojos y grises con una tipografía serif en sus inicios, Google Calendar mostraba colores vibrantes sin una jerarquía clara, Google Drive empleaba un diseño minimalista de líneas finas y Google Maps priorizaba la información cartográfica sobre cualquier consideración estética. Esta fragmentación generaba una experiencia de usuario inconsistente que diluía la identidad de marca de Google como ecosistema integrado.

El lanzamiento de Material Design en **2014**, coincidiendo con **Android 5.0 Lollipop**, marcó un punto de inflexión. La implementación de Material Design en Gmail supuso una transformación radical: el buzón de entrada adoptó las superficies elevadas características del material, las sombras sutiles comenzaron a comunicar jerarquía entre los mensajes, el **FAB** (*Floating Action Button*) rojo de composición se convirtió en el elemento de acento principal, y las animaciones de *swipe* para archivar o eliminar correos incorporaron los principios de **movimiento significativo** que predica Material. La consistencia visual entre la versión web y las aplicaciones móviles de Gmail se multiplicó exponencialmente.

Google Drive experimentó una transformación similar pero adaptada a su naturaleza de gestor de archivos. Material Design se aplicó respetando la necesidad de mostrar grandes cantidades de información densa: las fichas de archivo adoptaron la elevación del material, los menús contextuales incorporaron las animaciones de ripple y reveal, y el cambio entre las vistas de lista y cuadrícula se animó con transiciones compartidas. Google Calendar, por su parte, integró las paletas de color adaptativas de **Material You**, permitiendo que los eventos del calendario heredaran colores extraídos del *wallpaper* del dispositivo del usuario en **Android 12** y posteriores, creando una experiencia personalizada sin precedentes.

El caso de Google Maps es particularmente instructivo porque demuestra cómo un sistema de diseño debe ser lo suficientemente flexible para adaptarse a productos con necesidades muy específicas. Google Maps no podía simplemente adoptar las superficies blancas y las sombras de Material Design porque su interfaz se superpone a un mapa que ya contiene su propia jerarquía visual. La solución fue una implementación selectiva: la barra de búsqueda y las fichas de lugar adoptaron la estética Material, pero la capa del mapa mantuvo su diseño cartográfico propio.

!!! tip "Lección del caso"
    Esta tensión entre **consistencia del sistema** y **especificidad del producto** es una de las lecciones más valiosas que ofrece el caso de Google.

### Caso real 2: Human Interface Guidelines en el ecosistema Apple

El ecosistema de aplicaciones de Apple constituye el ejemplo más coherente y longevo de aplicación de un sistema de diseño. A diferencia de Google, que tuvo que imponer Material Design sobre productos que ya tenían identidades visuales consolidadas, las HIG han guiado el diseño de las aplicaciones de Apple desde las primeras versiones de iOS y macOS, lo que ha resultado en un nivel de consistencia difícil de igualar.

La aplicación Notas de Apple es un caso paradigmático de aplicación de los principios de las HIG. Analizando su evolución desde **iOS 7** hasta **iOS 17**, podemos observar cómo la aplicación ha ido ganando funcionalidad (listas de verificación, escaneo de documentos, dibujo con Apple Pencil, etiquetas, carpetas inteligentes) sin que la interfaz haya perdido su esencia minimalista. La barra de herramientas se mantiene translúcida para no competir con el contenido, los iconos utilizan el lenguaje **SF Symbols** introducido en **iOS 13**, la tipografía **San Francisco** se aplica con la jerarquía precisa que dictan las HIG (**Title 1** para el nombre de la nota, **Body** para el contenido, **Caption** para las fechas), y las animaciones de transición entre la lista de notas y el editor utilizan la navegación *push* estándar de iOS.

La aplicación Salud demuestra cómo las HIG guían la visualización de datos complejos. Los anillos de actividad, las gráficas de tendencias y las tarjetas de métricas siguen estrictamente las directrices de color, tipografía y espaciado de Apple, pero lo más relevante es cómo la aplicación aplica el principio de deferencia: los datos de salud del usuario son los protagonistas absolutos, y la interfaz se reduce a contenedores translúcidos con bordes redondeados (el característico "glass effect" de Apple), tipografía limpia y espacios generosos que permiten que cada métrica respire visualmente.

El navegador Safari en iOS ofrece otra lección valiosa. La decisión de Apple en **iOS 15** de mover la barra de direcciones a la parte inferior de la pantalla fue una aplicación directa del principio de diseño centrado en el ser humano que subyace en las HIG: los estudios de usabilidad de Apple habían demostrado que, con pantallas cada vez más grandes, alcanzar la barra de direcciones en la parte superior resultaba incómodo.

!!! tip "Lección del caso"
    Esta decisión, inicialmente polémica, demuestra que las HIG **no son un documento dogmático** sino un marco que evoluciona en respuesta a la investigación de usabilidad y a las necesidades cambiantes de los usuarios.

### Caso real 3: Ant Design en aplicaciones empresariales de Alibaba

Ant Design ofrece el caso de estudio más relevante para el ámbito de las aplicaciones empresariales, un sector tradicionalmente descuidado por los grandes sistemas de diseño. Alibaba Group, el conglomerado de comercio electrónico más grande de China, se enfrentaba a un problema de escala sin precedentes: cientos de equipos de desarrollo mantenían decenas de aplicaciones empresariales internas para gestionar inventarios, logística, finanzas, atención al cliente y análisis de datos. Cada equipo había desarrollado sus propios componentes de interfaz, resultando en un ecosistema fragmentado donde un simple componente de tabla de datos podía tener quince implementaciones diferentes con comportamientos inconsistentes.

La decisión de crear Ant Design como sistema de diseño interno y posteriormente liberarlo como proyecto *open source* (en **2015**, y su versión React en **2017**) transformó radicalmente el panorama. Para los equipos de Alibaba, la adopción de Ant Design significó pasar de semanas de desarrollo para implementar una tabla de datos compleja a minutos de integración de un componente que ya incluía ordenación, filtrado, paginación, selección múltiple, columnas fijas, exportación de datos y modo oscuro. La consistencia visual entre aplicaciones eliminó la fricción que experimentaban los empleados al cambiar entre diferentes herramientas internas, reduciendo los tiempos de formación y los errores operativos.

El caso de Ant Design Pro es particularmente revelador. Se trata de un scaffold completo para aplicaciones empresariales que proporciona, además de los componentes de Ant Design, un sistema de layout con menú lateral y breadcrumbs automáticos, un sistema de enrutamiento, gestión de permisos y roles, internacionalización, temas claros y oscuros, y dashboards de ejemplo. Para una empresa que necesita lanzar rápidamente una aplicación de gestión interna, Ant Design Pro reduce el tiempo desde la decisión hasta el primer prototipo funcional de meses a días. Este enfoque de "solución completa" más allá de los componentes individuales es lo que diferencia a Ant Design de otros sistemas de diseño que se limitan a proporcionar una biblioteca de UI.

La evolución de Ant Design hacia la versión **5** también ofrece lecciones sobre gobernanza de sistemas de diseño. La migración de Less a **CSS-in-JS** (con la biblioteca `@ant-design/cssinjs`) fue una decisión técnica controvertida pero necesaria para soportar temas dinámicos sin duplicación de estilos, una necesidad creciente en aplicaciones que debían permitir personalización por cliente (*white-labeling*). El proceso de migración se gestionó con una estrategia de **compatibilidad hacia atrás** que permitió a los equipos adoptar la nueva versión gradualmente, y la documentación detallada del proceso de migración minimizó la fricción.

!!! tip "Lección del caso"
    Un sistema de diseño exitoso requiere **no solo buenos componentes sino también procesos de gobernanza** que gestionen su evolución sin alienar a los equipos que dependen de él.

## Actividades guiadas

### Actividad guiada 1: Auditoría de interfaz y extracción de tokens de diseño a partir de un diseño existente

**Objetivo:** Aprender a realizar una auditoría de interfaz para identificar los tokens de diseño implícitos en un diseño existente y formalizarlos en un sistema estructurado.

**Contexto:** Se proporciona al alumno una captura de pantalla de un dashboard de analítica web que contiene múltiples componentes (cabecera con navegación, sidebar, tarjetas de métricas, tabla de datos, gráficos, formulario de filtros). El diseño es consistente pero no está documentado.

**Pasos a seguir:**

1. Abrir la captura de pantalla en una herramienta de inspección visual (Figma, o cualquier visor de imágenes con capacidad de zoom y cuentagotas).
2. Identificar todos los colores presentes en la interfaz y agruparlos por función: colores de marca, colores de texto, colores de fondo, colores de borde, colores semánticos (éxito, error, advertencia).
3. Para cada color, extraer su valor hexadecimal utilizando el cuentagotas y documentarlo en una tabla con las columnas: Nombre del token, Valor HEX, Función, Componente(s) donde aparece.
4. Identificar la escala tipográfica: medir (o estimar) los tamaños de fuente de cada nivel jerárquico (título principal, títulos de sección, títulos de tarjeta, cuerpo de texto, texto secundario, etiquetas, valores numéricos destacados).
5. Documentar la familia o familias tipográficas identificadas, los pesos utilizados y las alturas de línea aparentes.
6. Medir los espaciados: padding de las tarjetas, márgenes entre secciones, gutter entre columnas del grid, separación entre elementos de formulario, padding de botones. Identificar si siguen una escala consistente (¿múltiplos de 4px? ¿de 8px?).
7. Observar los radios de borde: botones, tarjetas, inputs, modales. ¿Son consistentes en toda la interfaz?
8. Identificar las elevaciones: ¿se utilizan sombras? ¿Cuántos niveles de elevación diferentes se observan? Extraer los valores de box-shadow.
9. Redactar los tokens de diseño en las tres capas: globales, semánticos y de componente, siguiendo la convención de nomenclatura aprendida.
10. Crear un archivo `tokens.css` con las variables CSS correspondientes a todos los tokens identificados.

**Criterios de evaluación:**

- Se han identificado correctamente al menos el **80%** de los tokens de diseño presentes en la interfaz (2 puntos).
- La nomenclatura de los tokens sigue la convención estructurada `categoría-propiedad-variante-estado` (2 puntos).
- Se han organizado los tokens en las tres capas jerárquicas (global, alias, componente) correctamente (2 puntos).
- El archivo `tokens.css` es funcional y las variables están correctamente referenciadas (2 puntos).
- Se ha documentado cada decisión con un comentario breve que justifica la elección del token (2 puntos).

### Actividad guiada 2: Implementación de un sistema de temas claro/oscuro mediante CSS Custom Properties

**Objetivo:** Implementar un sistema de cambio de tema (claro y oscuro) utilizando exclusivamente CSS Custom Properties y sin dependencias externas, respetando la preferencia del sistema operativo del usuario.

**Contexto:** Partiendo del sistema de tokens de diseño creado en actividades anteriores, se debe implementar la capacidad de alternar entre un tema claro y un tema oscuro. El tema debe respetar la preferencia `prefers-color-scheme` del sistema operativo y ofrecer un toggle manual que persista en localStorage.

**Pasos a seguir:**

1. Duplicar el bloque de tokens semánticos en `:root`, creando una segunda versión con colores adaptados para modo oscuro (fondos oscuros, texto claro, contrastes ajustados).
2. Envolver los tokens del tema oscuro en una media query `@media (prefers-color-scheme: dark)` para que se apliquen automáticamente si el usuario tiene configurado el modo oscuro en su sistema operativo.
3. Crear una clase CSS `.theme-dark` que contenga los mismos tokens del tema oscuro y una clase `.theme-light` para forzar el tema claro, ambas con mayor especificidad que la media query para permitir la anulación manual.
4. Implementar un botón de toggle en HTML y el JavaScript necesario para: detectar el tema actual, alternarlo al hacer clic, añadir/quitar la clase correspondiente en `<html>`, y persistir la preferencia en `localStorage`.
5. Al cargar la página, el script debe verificar el localStorage: si existe una preferencia guardada, aplicarla; si no, respetar la configuración del sistema operativo.
6. Verificar que todos los componentes implementados anteriormente (botones, tarjetas, formularios) se visualizan correctamente en ambos temas.
7. Probar los niveles de contraste de texto en el tema oscuro utilizando la herramienta de desarrollador del navegador (Lighthouse o el inspector de accesibilidad) para garantizar que cumplen el ratio mínimo **4.5:1** para texto normal y **3:1** para texto grande (**WCAG AA**).

**Criterios de evaluación:**

- El tema oscuro se aplica correctamente en todos los componentes (3 puntos).
- La detección automática de `prefers-color-scheme` funciona correctamente (2 puntos).
- El toggle manual anula la preferencia del sistema y persiste en localStorage (2 puntos).
- Los contrastes en ambos temas cumplen con WCAG AA (2 puntos).
- El código JavaScript está correctamente comentado y no produce errores en consola (1 punto).

### Actividad guiada 3: Documentación de un componente en Storybook

**Objetivo:** Aprender a documentar componentes de un sistema de diseño utilizando Storybook, creando historias interactivas que muestren todas las variantes y estados del componente.

**Contexto:** Se trabajará con el componente Button desarrollado en los ejemplos guiados. El alumno debe instalar y configurar Storybook en un proyecto nuevo y crear las historias correspondientes para el componente Button.

**Pasos a seguir:**

1. Inicializar un nuevo proyecto con `npm init -y` e instalar React y ReactDOM como dependencias.
2. Instalar Storybook ejecutando `npx storybook@latest init` y seleccionar React como framework. Durante la instalación, Storybook detectará automáticamente el framework y configurará los archivos necesarios.
3. Crear el componente Button como un componente React funcional que acepte props: `variant` (primary, secondary, ghost, danger), `size` (sm, md, lg), `disabled`, `children`, `onClick`, e `icon`.
4. Implementar los estilos en un archivo CSS separado o utilizando CSS Modules, asegurándose de que todas las variantes y estados funcionen correctamente.
5. Crear el archivo de historia `Button.stories.jsx` en la misma carpeta que el componente, siguiendo el formato CSF (Component Story Format) de Storybook.
6. Escribir historias para cada variante: Primary, Secondary, Ghost, Danger.
7. Escribir historias para cada tamaño: Small, Medium, Large.
8. Escribir historias para estados: Disabled, With Icon, Icon Only, Loading (añadiendo un estado de carga con un spinner).
9. Configurar los controles (controls) de Storybook para que el usuario pueda cambiar las props desde el panel de addons y ver el resultado en tiempo real.
10. Añadir documentación escrita en formato Markdown mediante el bloque `<Description>` o mediante el parámetro `component.description`.
11. Ejecutar `npm run storybook` y verificar que todas las historias se renderizan correctamente y los controles funcionan.

**Criterios de evaluación:**

- Storybook se ha instalado y configurado correctamente (1 punto).
- El componente Button está correctamente implementado con todas las variantes y tamaños (2 puntos).
- Se han creado al menos 8 historias que cubren variantes, tamaños y estados (2 puntos).
- Los controles de Storybook permiten modificar props en tiempo real (2 puntos).
- Se ha incluido documentación descriptiva en al menos 3 historias (1 punto).
- El proyecto compila sin errores (2 puntos).

### Actividad guiada 4: Construcción de un mini sistema de diseño completo desde cero

**Objetivo:** Integrar todos los conocimientos de la unidad construyendo, paso a paso, un sistema de diseño completo y funcional que incluya tokens, componentes básicos y documentación.

**Contexto:** Se debe crear el sistema de diseño "Minimal DS" para una startup ficticia que construye una aplicación SaaS de gestión de proyectos. El sistema debe ser ligero, accesible y fácil de personalizar.

**Pasos a seguir:**

1. Definir los principios de diseño del sistema (máximo 5 principios, redactados de forma clara y accionable). Por ejemplo: "Mobile first", "Accesible WCAG AA por defecto", "Rendimiento primero", "Personalizable mediante tokens".
2. Crear la estructura de carpetas del proyecto: `/tokens/` para los tokens de diseño, `/components/` para los componentes CSS, `/docs/` para la documentación, y un `index.css` que importe todos los archivos.
3. Implementar los tokens globales en `tokens/globals.css`: paleta de colores (al menos 3 colores de marca con sus escalas, colores neutros, colores semánticos), escala tipográfica completa, escala de espaciado, border-radius, shadows.
4. Implementar los tokens semánticos en `tokens/semantic.css`: asignar significados a los colores (primary, secondary, surface, text), definir los tokens tipográficos por rol (heading-1, body, caption, etc.)
5. Implementar los tokens de componente en `tokens/components.css`: variables para botones, inputs, cards, badges.
6. Implementar los estilos base en `base/reset.css`: un reset CSS minimalista (box-sizing, márgenes) que no sea destructivo.
7. Implementar los estilos tipográficos en `base/typography.css`: clases de utilidad tipográfica que consuman los tokens.
8. Implementar el sistema de grid en `layout/grid.css`: contenedor, filas, columnas responsive.
9. Implementar el componente Button en `components/button.css`: siguiendo el ejemplo guiado 3 pero adaptándolo a la paleta de colores de Minimal DS.
10. Implementar el componente Card en `components/card.css`.
11. Implementar el componente Form en `components/form.css`.
12. Implementar el componente Badge en `components/badge.css`.
13. Crear un archivo `index.html` de demostración que muestre todos los componentes en acción, en un layout de ejemplo que simule una pantalla real de la aplicación.
14. Redactar un archivo `README.md` de documentación que explique: principios del sistema, cómo usar los tokens, ejemplos de cada componente con su código HTML, y guía de contribución.
15. Probar el sistema en al menos dos navegadores diferentes y en vista móvil (responsive).

**Criterios de evaluación:**

- La estructura de carpetas es lógica y los archivos están correctamente organizados (1 punto).
- Los tokens de diseño están completos en las tres capas (global, semántico, componente) (2 puntos).
- Los estilos base (reset y tipografía) son adecuados y no destructivos (1 punto).
- Los 4 componentes (button, card, form, badge) están implementados con al menos 2 variantes cada uno (2 puntos).
- El sistema de grid responsive funciona en al menos 3 breakpoints (1 punto).
- La página de demostración muestra todos los componentes correctamente (1 punto).
- La documentación README.md es clara y contiene ejemplos de uso (1 punto).
- El sistema funciona correctamente en vista móvil (1 punto).

## Actividades propuestas

### Actividad propuesta 1: Análisis comparativo de sistemas de diseño

Realiza un análisis comparativo detallado de tres sistemas de diseño públicos diferentes (por ejemplo: Material Design, Atlassian Design System, Shopify Polaris, Carbon de IBM, Fluent de Microsoft, Lightning de Salesforce). Para cada sistema, investiga y documenta: los principios de diseño que lo fundamentan, la arquitectura de tokens que utiliza, el catálogo de componentes que ofrece, la tecnología de implementación que emplea, el modelo de gobernanza y contribución que sigue, el tratamiento de la accesibilidad, y la estrategia de adopción de temas (claro/oscuro, multi-marca). Presenta los resultados en una tabla comparativa y redacta una conclusión argumentada sobre cuál de los tres sistemas elegirías para un proyecto de comercio electrónico, cuál para una aplicación empresarial interna y cuál para un producto SaaS B2C, justificando cada elección con criterios técnicos y de diseño.

### Actividad propuesta 2: Migración de una web existente a tokens de diseño

Selecciona una página web real que no utilice un sistema de diseño formal (puede ser una web local pequeña, el sitio web de un negocio cercano, o incluso un proyecto personal antiguo). Realiza una captura de todas las pantallas principales y efectúa una auditoría visual completa. Extrae todos los valores de diseño (colores, tipografías, espaciados, sombras, border-radius) y transfórmalos en un sistema de tokens de diseño estructurado en tres capas. A continuación, refactoriza el CSS de la web para que consuma exclusivamente estos tokens mediante CSS Custom Properties. Documenta el proceso de migración: qué decisiones de diseño tuviste que tomar al formalizar valores que antes eran inconsistentes, qué componentes eran redundantes y pudieron unificarse, y qué mejoras de mantenibilidad se consiguieron. Entrega tanto los archivos originales como los refactorizados, junto con un informe de la migración.

### Actividad propuesta 3: Diseño de la paleta cromática de un sistema de diseño mediante generación algorítmica

Investiga cómo funcionan los algoritmos de generación de paletas cromáticas (como el algoritmo de Material Design 3 para generar tonalidades a partir de un color semilla). Implementa, utilizando JavaScript o cualquier lenguaje de programación, una función que reciba un color base en formato HEX y genere automáticamente una escala de 10 tonalidades (desde el 50 al 900) siguiendo los principios de luminancia y saturación de Material Design. La función debe devolver los colores en formato HEX y garantizar que las tonalidades más claras (50-200) tengan suficiente contraste para texto oscuro y que las tonalidades más oscuras (700-900) tengan suficiente contraste para texto claro. Prueba tu función con al menos 5 colores semilla diferentes. Entrega el código fuente de la función, la paleta generada para cada color semilla y una validación de accesibilidad de los contrastes generados.

### Actividad propuesta 4: Propuesta de sistema de diseño para el proyecto integrado

Tomando como base el proyecto que estás desarrollando para el módulo de Proyecto Integrado (o un proyecto hipotético de envergadura similar), elabora una propuesta completa de sistema de diseño. La propuesta debe incluir: principios de diseño (mínimo 4, con justificación de cada uno), tokens de diseño completos (paleta de colores con escalas, tipografía con escala modular, espaciado, sombras, border-radius, duraciones de animación), bocetos o wireframes de los componentes principales (al menos 6 componentes: botones, formularios, tarjetas, navegación, tablas, modales), especificaciones de accesibilidad por componente, una estimación del esfuerzo necesario para implementar el sistema, y un plan de adopción en fases para integrarlo en el proyecto sin interrumpir el desarrollo. Entrega la propuesta en formato de documento de especificación de diseño, similar a los documentos que encontrarías en un entorno profesional real.

## Actividades de ampliación

### Actividad de ampliación 1: Implementación de un sistema de diseño con Styled Components y React

**Contexto:** Esta actividad está dirigida al alumnado que desea profundizar en la integración de sistemas de diseño con frameworks modernos de frontend. Se trabajará con React y Styled Components para recrear el sistema de diseño "Minimal DS" construido en la Actividad Guiada 4, pero esta vez como una biblioteca de componentes React completamente funcional y publicable en npm.

**Objetivos:**

- Configurar un proyecto React con soporte para Styled Components y ThemeProvider.
- Migrar los tokens CSS Custom Properties a un objeto de tema JavaScript consumible por ThemeProvider.
- Implementar cada componente (Button, Card, Form, Badge, Input, Select, Modal, Tabs) como un componente React estilizado con Styled Components.
- Cada componente debe aceptar props tipadas (con PropTypes o TypeScript) para sus variantes, tamaños y estados.
- Implementar una variante de tema oscuro como un segundo objeto de tema.
- Configurar Storybook para documentar todos los componentes React.
- Configurar tests unitarios con Jest y React Testing Library para al menos 3 componentes.
- Preparar el proyecto para publicación en npm (package.json, README, licencia, .npmignore).
- Publicar el paquete (aunque sea en un registro privado o local con `npm link`).
- Crear una aplicación de demostración que consuma la biblioteca publicada.

**Formato de entrega:** Repositorio Git con el código fuente completo de la biblioteca, la configuración de Storybook, los tests y la aplicación de demostración. Incluir README.md con instrucciones de instalación, uso y contribución.

**Rúbrica de evaluación:**

- Configuración correcta del proyecto con ThemeProvider (1 punto).
- Migración completa de tokens a objeto JavaScript (1 punto).
- Implementación correcta de 8 componentes React (4 puntos, 0.5 cada uno).
- Tipado de props (PropTypes o TypeScript) (1 punto).
- Tema oscuro funcional y toggle implementado (0.5 puntos).
- Documentación en Storybook con al menos 2 historias por componente (1 punto).
- Tests unitarios funcionales para 3 componentes (0.5 puntos).
- Aplicación de demostración funcional (0.5 puntos).
- README completo con instrucciones (0.5 puntos).

### Actividad de ampliación 2: Creación de tokens de diseño multiplataforma con Style Dictionary

**Contexto:** En equipos que desarrollan para múltiples plataformas (web, iOS, Android), mantener la consistencia de los tokens de diseño es un desafío. Style Dictionary es una herramienta de Amazon que permite definir tokens en un formato agnóstico (JSON) y transformarlos automáticamente a los formatos nativos de cada plataforma.

**Objetivos:**

- Configurar un proyecto con Style Dictionary desde cero.
- Definir un conjunto completo de tokens de diseño (colores, tipografía, espaciado, border-radius, sombras, tiempos de animación) en formato JSON siguiendo la especificación DTCG (Design Tokens Community Group).
- Configurar las transformaciones y plataformas de salida: CSS Custom Properties para web, variables SASS para web, XML para Android, y un objeto JavaScript/JSON para consumo en React Native.
- Implementar tokens condicionales para temas claro/oscuro.
- Generar una documentación HTML automática de los tokens utilizando las plantillas de Style Dictionary.
- Integrar el proceso de generación de tokens en el flujo de desarrollo (scripts npm: `build:tokens`, `watch:tokens`).
- Investigar y documentar cómo sincronizar estos tokens con Figma utilizando el plugin Figma Tokens.

**Formato de entrega:** Proyecto Style Dictionary completo con los archivos de configuración, los tokens en JSON, las salidas generadas para las 4 plataformas, la documentación HTML y un informe que explique el flujo de trabajo de tokens multiplataforma.

**Rúbrica de evaluación:**

- Configuración correcta de Style Dictionary (1 punto).
- Tokens definidos siguiendo la especificación DTCG (2 puntos).
- Salidas generadas para 4 plataformas diferentes (2 puntos, 0.5 cada una).
- Tokens condicionales para temas claro/oscuro funcionales (1 punto).
- Documentación HTML automática generada (1 punto).
- Scripts npm configurados (1 punto).
- Informe sobre sincronización con Figma (1 punto).
- Organización y claridad del proyecto (1 punto).

### Actividad de ampliación 3: Desarrollo de un sistema de diseño con componentes web nativos (Web Components)

**Contexto:** Los Web Components representan un estándar de la plataforma web que permite crear componentes reutilizables sin depender de ningún framework. Esta actividad explora la implementación de un sistema de diseño utilizando exclusivamente tecnologías nativas del navegador: Custom Elements, Shadow DOM y HTML Templates.

**Objetivos:**

- Investigar la especificación de Web Components: Custom Elements v1, Shadow DOM v1, templates y slots.
- Diseñar e implementar un sistema de tokens de diseño como CSS Custom Properties que se inyecten en el Shadow DOM de cada componente mediante `adoptedStyleSheets` o etiquetas `<style>`.
- Implementar al menos 6 componentes como Custom Elements: `<ds-button>`, `<ds-input>`, `<ds-card>`, `<ds-badge>`, `<ds-modal>`, `<ds-tabs>`.
- Cada componente debe aceptar atributos HTML para configurar sus variantes (`<ds-button variant="primary" size="lg">`) y reflejar los cambios de atributo en el renderizado.
- Implementar la comunicación entre componentes mediante Custom Events.
- El sistema debe funcionar sin dependencias externas (sin frameworks, sin polyfills para navegadores modernos).
- Crear una página de demostración que utilice todos los componentes.
- Realizar pruebas de compatibilidad en Chrome, Firefox y Safari.
- Documentar las diferencias entre este enfoque nativo y los enfoques basados en frameworks como React o Vue, analizando ventajas e inconvenientes de cada uno para un sistema de diseño.

**Formato de entrega:** Código fuente de los Web Components, página de demostración, informe comparativo Web Components vs. Frameworks. Todo en un repositorio Git.

**Rúbrica de evaluación:**

- 6 componentes implementados correctamente como Custom Elements (3 puntos, 0.5 cada uno).
- Tokens de diseño correctamente aplicados mediante Shadow DOM (1.5 puntos).
- Comunicación entre componentes mediante eventos (1 punto).
- Funcionamiento sin dependencias externas en 3 navegadores (1.5 puntos).
- Página de demostración funcional (1 punto).
- Informe comparativo con análisis crítico (1.5 puntos).
- Organización del código y buenas prácticas (0.5 puntos).

## Buenas prácticas

La adopción de un sistema de diseño en un proyecto profesional requiere disciplina y adhesión a un conjunto de buenas prácticas que maximicen sus beneficios y minimicen los riesgos de fragmentación. La primera y más fundamental es el principio de **fuente única de verdad** (*single source of truth*).

!!! tip "Fuente única de verdad"
    Los tokens de diseño deben existir en un **único lugar canónico** desde el cual se propaguen a todas las plataformas y tecnologías. Un color como el primario de la marca **no debe estar definido simultáneamente** en una hoja de estilos CSS, en un archivo de configuración de React, en una paleta de Figma y en un documento de especificación: debe residir en un archivo de tokens (JSON, YAML) del cual se generen automáticamente todas las representaciones necesarias.

En cuanto a la nomenclatura, los tokens deben nombrarse siguiendo una convención **semántica** y no presentacional. Un token llamado `--color-blue-500` es menos mantenible que `--color-primary-500` porque si la marca cambia de azul a verde, el nombre `blue` se convierte en engañoso. La nomenclatura debe responder a la pregunta «¿para qué sirve este valor?» en lugar de «¿qué valor tiene?». Esta práctica, conocida como ***semantic naming***, es la que permite que un sistema de diseño sobreviva a cambios de identidad corporativa sin requerir una reescritura completa del código.

La documentación es tan importante como el código. Un componente sin documentación es un componente que no será utilizado por otros equipos, que será malinterpretado en su propósito, o que será duplicado innecesariamente. Cada componente del sistema debe documentar **su propósito, sus variantes visuales con ejemplos, su API de props o atributos, sus consideraciones de accesibilidad, ejemplos de código copiables y notas sobre cuándo no usar ese componente**. La documentación debe ser viva y mantenerse sincronizada con el código, preferiblemente mediante herramientas como **Storybook** que generan la documentación directamente desde el código fuente.

!!! warning "Accesibilidad desde el diseño"
    La accesibilidad no debe ser una ocurrencia tardía sino un requisito **desde la fase de diseño** de cada componente. Todos los componentes del sistema deben cumplir **WCAG 2.1 nivel AA** como mínimo: ratio de contraste de **4.5:1** para texto normal y **3:1** para texto grande, navegabilidad completa por teclado con estilos de foco visibles, atributos **ARIA** adecuados y contenido comprensible cuando se amplía al **200%**.

Incorporar tests automatizados de accesibilidad (con **axe-core** o similar) en el *pipeline* de **CI/CD** garantiza que las regresiones de accesibilidad se detecten antes de llegar a producción.

El **versionado semántico** (*SemVer*) debe aplicarse rigurosamente al sistema de diseño. Los cambios que rompen la API de un componente (**MAJOR**), las adiciones de nuevas funcionalidades compatibles hacia atrás (**MINOR**) y las correcciones de errores (**PATCH**) deben gestionarse con la misma disciplina que cualquier otra dependencia de software. Esto permite a los equipos consumidores actualizar con confianza sabiendo exactamente qué tipo de cambios incluye cada nueva versión.

Finalmente, establecer un proceso de **gobernanza y contribución** es esencial para la supervivencia a largo plazo del sistema de diseño. Debe existir un equipo responsable (*design system team*) que revise las contribuciones, mantenga la coherencia del sistema y tome las decisiones de diseño. El proceso de contribución debe estar documentado y ser accesible: cualquier desarrollador debe saber cómo proponer un nuevo componente, qué criterios se utilizarán para evaluarlo, y cuánto tiempo aproximadamente tomará el proceso de revisión e incorporación.

## Errores frecuentes

!!! warning "Cimientos antes que componentes"
    Uno de los errores más comunes y devastadores en la implementación de sistemas de diseño es **comenzar por el código antes de tener claros los principios y la arquitectura**. Equipos entusiastas saltan directamente a crear componentes React o Vue sin haber definido previamente los tokens de diseño, la escala tipográfica o el sistema de espaciado. El resultado es un conjunto de componentes que parecen coherentes individualmente pero que **no encajan entre sí**: una Card tiene un padding de **20px**, un Modal usa **24px**, y un Form usa **16px**. Esta inconsistencia subyacente se manifiesta en interfaces que se sienten visualmente descoordinadas y son difíciles de mantener.

La solución es definir primero los cimientos (tokens, escalas, principios) y construir los componentes sobre ellos.

Otro error frecuente es crear **componentes excesivamente específicos que no pueden reutilizarse** en contextos diferentes. Un `DashboardCard` que incluye por defecto un gráfico de barras y un selector de fecha será inutilizable en cualquier otro contexto que no sea exactamente ese *dashboard*. Los componentes del sistema de diseño deben ser **genéricos y componibles**, siguiendo principios como «haz una cosa y hazla bien». En lugar de `DashboardCard`, el sistema debería proporcionar `Card`, `Chart` y `DatePicker` como componentes independientes que puedan combinarse de múltiples formas.

La **falta de flexibilidad en los componentes** es el error simétrico al anterior. Un componente Button que solo existe en color azul y tamaño mediano es igualmente inútil. Los componentes del sistema deben exponer una API de personalización razonable mediante *props*, *slots* o tokens, permitiendo adaptarlos a diferentes contextos sin perder la coherencia del sistema. El arte del diseño de sistemas está en encontrar el equilibrio entre **estandarización** (que garantiza consistencia) y **flexibilidad** (que permite cubrir casos de uso diversos).

**Ignorar la accesibilidad durante el desarrollo de los componentes y pretender añadirla después** es uno de los errores más costosos. Un sistema de componentes construido sin pensar en la accesibilidad requerirá refactorizaciones profundas para incorporar atributos ARIA, gestión de foco, roles semánticos y soporte de teclado. Estos cambios tardíos suelen introducir regresiones visuales y de comportamiento que consumen tiempo y generan frustración. La accesibilidad debe ser un **criterio de aceptación** en la definición de cada componente.

**No documentar adecuadamente el sistema** es un error que lo condena al fracaso por abandono. Los desarrolladores no utilizarán componentes que no entienden, no sabrán qué *props* acepta un componente sin una referencia clara, y acabarán creando sus propias versiones alternativas que fragmentan la interfaz. La documentación debe ser exhaustiva pero navegable, con ejemplos visuales y de código, y debe mantenerse sincronizada automáticamente con el código mediante herramientas como Storybook.

Finalmente, **tratar el sistema de diseño como un proyecto con fecha de finalización en lugar de como un producto vivo y en evolución continua** es un error estratégico. Un sistema de diseño nunca está «terminado»; siempre habrá nuevos componentes que añadir, patrones que refinar, tokens que ajustar y tecnologías a las que adaptarse. Los equipos que asignan recursos para construir el sistema pero no para mantenerlo se encuentran, **seis meses después**, con un sistema obsoleto que los equipos han abandonado en favor de sus propias soluciones puntuales.

## Resumen

Las guías de estilo y los sistemas de diseño constituyen la columna vertebral metodológica del desarrollo de interfaces web moderno, estableciendo el puente entre las decisiones de diseño visual y su implementación técnica. Una guía de estilo documenta los elementos visuales y las reglas que rigen la apariencia de un producto, mientras que un sistema de diseño va más allá al proporcionar los componentes implementados, los tokens de diseño portables y los procesos de gobernanza que garantizan la consistencia a escala. Los **tokens de diseño**, organizados en capas **global**, **semántica** y de **componente**, representan la unidad atómica que permite que un cambio en la paleta de colores o la escala tipográfica se propague automáticamente a toda la interfaz sin necesidad de modificar manualmente cada componente.

Los grandes sistemas de diseño públicos —Material Design con su metáfora del material, Human Interface Guidelines con su deferencia al contenido, y Ant Design con su orientación al ámbito empresarial— ofrecen lecciones valiosas y patrones reutilizables, pero cada producto y cada equipo deben desarrollar su propio sistema adaptado a sus necesidades específicas. La implementación técnica puede abordarse mediante variables CSS nativas, preprocesadores SASS, CSS-in-JS con Styled Components o CSS Modules, y herramientas como Storybook, Figma Tokens y Style Dictionary facilitan la documentación y la sincronización entre diseño y código. El éxito a largo plazo de un sistema de diseño depende tanto de la calidad técnica de sus componentes como de los procesos de gobernanza, documentación y contribución que permitan su evolución controlada.

## Recursos complementarios

- **Material Design 3 (Material You):** La documentación oficial de la última versión de Material Design, que introduce la generación dinámica de paletas de color y el concepto de personalización. Disponible en https://m3.material.io
- **Human Interface Guidelines de Apple:** La referencia canónica para el diseño en plataformas Apple, actualizada anualmente con cada versión de los sistemas operativos. Disponible en https://developer.apple.com/design/human-interface-guidelines
- **Ant Design 5:** La documentación oficial incluye guías de diseño, componentes y recursos. Disponible en https://ant.design
- **Design Tokens Community Group (DTCG):** Grupo de trabajo del W3C que está estandarizando el formato de tokens de diseño. Su especificación es la referencia para herramientas como Style Dictionary. Disponible en https://www.designtokens.org
- **Style Dictionary:** Herramienta de Amazon para la gestión de tokens de diseño multiplataforma. Repositorio y documentación en https://amzn.github.io/style-dictionary
- **Storybook:** La herramienta de referencia para desarrollo aislado y documentación de componentes. Tutoriales completos en https://storybook.js.org/tutorials
- **Zeroheight:** Plataforma de documentación para sistemas de diseño utilizada por empresas como Uber, Adobe y Microsoft. Permite integrar componentes vivos de Storybook con documentación de diseño. Disponible en https://zeroheight.com
- **Figma Tokens:** Plugin de Figma que permite definir y gestionar tokens de diseño directamente en Figma y sincronizarlos con repositorios de código. Esencial para el flujo diseño-desarrollo. Buscar "Tokens Studio for Figma" en la comunidad de plugins de Figma.
- **Every Layout (Andy Bell y Hayden Pickering):** Libro que aborda los fundamentos del layout en CSS desde una perspectiva de sistemas de diseño, con énfasis en componentes intrínsecamente responsive. Disponible en https://every-layout.dev
- **Atomic Design (Brad Frost):** El libro y la metodología que introdujo el concepto de diseñar sistemas mediante átomos, moléculas y organismos. Disponible gratuitamente en https://atomicdesign.bradfrost.com
- **Inclusive Components (Heydon Pickering):** Recurso fundamental para la construcción de componentes accesibles por defecto, con ejemplos de código y patrones de diseño inclusivo. Disponible en https://inclusive-components.design
- **Design Systems Handbook (DesignBetter by InVision):** Guía completa sobre cómo crear, implementar y mantener sistemas de diseño, con casos de estudio de empresas como Airbnb, Uber y Shopify. Disponible en https://www.designbetter.co/design-systems-handbook
