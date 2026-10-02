---
icon: lucide/rows-3
---

# Unidad 9: Flexbox - Maquetación Unidimensional Profesional

## Objetivos de aprendizaje

Al finalizar esta unidad, el alumnado dominará completamente el modelo de maquetación Flexbox, siendo capaz de construir cualquier layout unidimensional de forma profesional. Sabrá identificar y manipular los ejes principal y transversal según la dirección del flex, controlar el comportamiento de los ítems flex con las propiedades de crecimiento, reducción y base, y aplicar patrones de diseño profesionales como barras de navegación responsive, sistemas de tarjetas con contenido variable, formularios alineados, dashboards con sidebar flexible, sticky footers y centrado perfecto. El alumnado diferenciará claramente cuándo usar Flexbox frente a CSS Grid según las necesidades del layout. Será capaz de construir una barra de navegación completa con logo, menú, búsqueda e iconos, incluyendo una versión responsive con menú hamburguesa implementado con CSS puro (sin JavaScript). Dominará los patrones de alineación y distribución: centrado, espacio entre elementos, espacio alrededor, y alineación individual con `align-self` y `margin: auto`. Comprenderá el comportamiento de `flex-basis` frente a `width` y la interacción entre `flex-grow`, `flex-shrink` y `flex-basis` mediante el shorthand `flex`.

## Relación con los Resultados de Aprendizaje

Esta unidad se alinea directamente con el RA2 del módulo 0615: "Crear interfaces web utilizando hojas de estilos y lenguajes de marcas". Flexbox es, junto con CSS Grid, la herramienta fundamental de maquetación en el desarrollo web moderno. Los criterios de evaluación exigen que el alumnado "haya creado interfaces web utilizando hojas de estilos en cascada" y "haya aplicado técnicas de maquetación web", y Flexbox es la técnica principal para layouts unidimensionales. La unidad también conecta con el RA5 de accesibilidad, ya que un layout correctamente implementado con Flexbox respeta el orden natural del DOM y permite reordenar elementos visualmente sin afectar al orden de tabulación. Además, el componente de navegación responsive y los patrones de formulario se relacionan con el RA4 sobre integración de elementos interactivos.

## Conocimientos previos

El alumnado debe dominar los conceptos básicos de CSS: modelo de caja (`margin`, `border`, `padding`, `content`), diferencia entre elementos de bloque y en línea, selectores CSS (clase, ID, tipo), y las propiedades básicas de presentación (`width`, `height`, `color`, `background`). Debe comprender el concepto de `display` y haber usado al menos `block`, `inline` e `inline-block`. Es fundamental que entienda el flujo normal del documento y cómo los elementos se posicionan por defecto. Debe saber enlazar CSS externo y conocer la estructura básica de un documento HTML5. Experiencia previa con posicionamiento (`relative`, `absolute`) es recomendable pero no imprescindible.

## Contenidos

1. **Introducción a Flexbox.** Qué es, modelo unidimensional, soporte en navegadores. Comparación con otros métodos de maquetación (float, inline-block, table).
2. **Ejes del modelo Flexbox.** Eje principal (main axis) y eje transversal (cross axis). Cómo `flex-direction` cambia los ejes: `row`, `row-reverse`, `column`, `column-reverse`.
3. **Propiedades del contenedor flex.** `display: flex/inline-flex`. `flex-direction`. `flex-wrap: nowrap/wrap/wrap-reverse`. `flex-flow` (shorthand). `justify-content: flex-start/flex-end/center/space-between/space-around/space-evenly`. `align-items: stretch/flex-start/flex-end/center/baseline`. `align-content` (con wrap). `gap`, `row-gap`, `column-gap`.
4. **Propiedades de los ítems flex.** `order`. `flex-grow`. `flex-shrink`. `flex-basis`. `flex` (shorthand). `align-self`.
5. **Auto margins en Flexbox.** Trucos con `margin: auto` para distribución avanzada.
6. **Flex-basis vs width.** Diferencias, prioridad y cómo el navegador resuelve conflictos.
7. **Patrones de diseño con Flexbox.** Lista horizontal, centrado perfecto, sticky footer, holy grail simplificado, media objects, igual altura de columnas, formulario responsive, cards alineadas.
8. **Navbar profesional.** Paso a paso: logo, menú, búsqueda, iconos, responsive con hamburguesa CSS puro.
9. **Cards con Flexbox.** Grid de cards con `flex-wrap`, cards con altura variable y footer alineado, hover effects.
10. **Formularios con Flexbox.** Etiquetas e inputs alineados, botones, layout responsive.
11. **Dashboard con Flexbox.** Sidebar flexible + contenido principal. Sidebar colapsable CSS puro. Header, área principal, cards de estadísticas.
12. **Comparación Flexbox vs Grid.** Cuándo usar cada uno. Casos de uso óptimos.

## Desarrollo teórico

### 1. Introducción a Flexbox

!!! info "Definición"
    **Flexbox** (*Flexible Box Layout*) es un modelo de maquetación CSS **unidimensional** diseñado para distribuir espacio entre ítems y alinearlos dentro de un contenedor, incluso cuando su tamaño es desconocido o dinámico. La palabra "flex" se refiere a la capacidad de los elementos de **expandirse** (*grow*) para llenar el espacio disponible o **contraerse** (*shrink*) para evitar desbordamientos. Fue introducido como *Candidate Recommendation* del W3C en **2012** y hoy tiene soporte universal en todos los navegadores modernos, incluyendo versiones móviles.

Antes de Flexbox, los desarrolladores recurrían a otras técnicas para crear *layouts*, cada una con limitaciones significativas:

- **`float`** — requería *clearfix* y no permitía la alineación vertical.
- **`display: inline-block`** — dejaba espacios no deseados entre elementos.
- **Tablas HTML** — mezclaban presentación con contenido.

Flexbox resolvió estos problemas proporcionando un modelo de *layout* nativo y expresivo.

!!! tip "Una sola dimensión cada vez"
    La naturaleza **unidimensional** de Flexbox significa que trabaja en una sola dirección: o bien en fila (horizontal) o bien en columna (vertical). Para *layouts* **bidimensionales** (filas y columnas simultáneamente), **CSS Grid** es la herramienta complementaria adecuada. Ambos modelos coexisten y se complementan en el desarrollo web moderno.

### 2. Ejes del modelo Flexbox

El modelo Flexbox se articula en torno a dos ejes perpendiculares que cambian según la dirección definida por `flex-direction`:

| Eje | Definición | Propiedades que operan sobre él |
|-----|------------|---------------------------------|
| **Eje principal** (*main axis*) | Dirección primaria en la que se disponen los ítems flex. Con `row` (por defecto) es horizontal, de izquierda a derecha; con `column` es vertical, de arriba a abajo. | `justify-content`, `flex-grow`, `flex-shrink`, `flex-basis` |
| **Eje transversal** (*cross axis*) | Siempre es **perpendicular** al eje principal: vertical cuando el principal es horizontal, y horizontal cuando el principal es vertical. | `align-items`, `align-content` |

Los valores de `flex-direction` son:

| Valor | Eje principal | Eje transversal |
|-------|---------------|-----------------|
| **`row`** (por defecto) | Horizontal, de izquierda a derecha | Vertical, de arriba a abajo |
| **`row-reverse`** | Horizontal, de derecha a izquierda; útil para *layouts* RTL o efectos visuales | Vertical, de arriba a abajo |
| **`column`** | Vertical, de arriba a abajo | Horizontal, de izquierda a derecha |
| **`column-reverse`** | Vertical, de abajo a arriba | Horizontal, de izquierda a derecha |

!!! warning "Orden visual ≠ orden del DOM"
    `row-reverse` y `column-reverse` invierten el orden **VISUAL** pero **NO** el orden del DOM. El orden de tabulación y de lectura para lectores de pantalla sigue siendo el del DOM, por lo que estos valores deben usarse con precaución en contextos donde el orden semántico es importante.

### 3. Propiedades del contenedor flex

**`display: flex` vs `display: inline-flex`:** ambos convierten al elemento en un contenedor flex. La diferencia es cómo se comporta ese contenedor fuera del flujo de su padre:

| Valor | Comportamiento del contenedor |
|-------|-------------------------------|
| **`flex`** | Se comporta como **bloque**: ocupa todo el ancho disponible. |
| **`inline-flex`** | Se comporta como **inline**: solo ocupa el ancho de su contenido. |

**`flex-direction`:** define la dirección del eje principal. `row` (por defecto, horizontal izquierda a derecha), `row-reverse` (horizontal derecha a izquierda), `column` (vertical arriba a abajo), `column-reverse` (vertical abajo a arriba).

**`flex-wrap`:** controla si los ítems se envuelven a una nueva línea cuando no caben. `nowrap` (por defecto, todos en una línea aunque se desborden), `wrap` (envuelven a la siguiente línea), `wrap-reverse` (envuelven en dirección inversa).

**`flex-flow`:** *shorthand* de `flex-direction` + `flex-wrap`. Ejemplo: `flex-flow: row wrap;`.

**`justify-content`:** alinea los ítems a lo largo del **eje principal**. Valores:

| Valor | Comportamiento |
|-------|----------------|
| **`flex-start`** | Al inicio del eje principal. |
| **`flex-end`** | Al final del eje principal. |
| **`center`** | Centrados en el eje principal. |
| **`space-between`** | Primer ítem al inicio, último al final, espacio igual entre ellos. |
| **`space-around`** | Espacio igual alrededor de cada ítem (mitad en los extremos). |
| **`space-evenly`** | Espacio exactamente igual entre ítems y extremos. |

**`align-items`:** alinea los ítems a lo largo del **eje transversal**. Valores:

| Valor | Comportamiento |
|-------|----------------|
| **`stretch`** (por defecto) | Estira los ítems para llenar el contenedor en el *cross axis*. |
| **`flex-start`** | Al inicio del *cross axis*. |
| **`flex-end`** | Al final del *cross axis*. |
| **`center`** | Centrados en el *cross axis*. |
| **`baseline`** | Alineados por la línea base del texto. |

!!! tip "align-content solo funciona con varias líneas"
    `align-content` **solo tiene efecto cuando hay `flex-wrap: wrap` y, por tanto, múltiples líneas**. Controla la distribución de las líneas en el eje transversal y admite los mismos valores que `justify-content`. Con una única línea, la propiedad no hace nada.

**`gap`, `row-gap`, `column-gap`:** definen el espacio entre ítems flex, tanto en filas como en columnas. `gap` es el *shorthand*.

!!! tip "gap frente a margin"
    A diferencia de usar `margin`, el **`gap` solo se aplica ENTRE ítems**, nunca en los extremos del contenedor. Es la forma más limpia y predecible de separar elementos flex.

### 4. Propiedades de los ítems flex

**`order`:** Controla el orden visual de los ítems. Por defecto todos tienen `order: 0`. Valores negativos mueven el ítem al inicio; valores positivos al final. Solo afecta al orden visual, no al orden del DOM ni al de tabulación. Usar con moderación.

**`flex-grow`:** Factor de crecimiento. Define cuánto puede crecer un ítem respecto a los demás cuando hay espacio disponible. Valor por defecto: `0` (no crece). Si todos los ítems tienen `flex-grow: 1`, se reparten el espacio equitativamente. Si uno tiene `flex-grow: 2` y otro `1`, el primero recibe el doble de espacio extra.

**`flex-shrink`:** Factor de reducción. Define cuánto puede encogerse un ítem cuando falta espacio. Valor por defecto: `1` (puede encogerse). `flex-shrink: 0` impide que el ítem se encoja, manteniendo su tamaño mínimo. Útil para elementos que no deben deformarse.

**`flex-basis`:** Tamaño base del ítem antes de aplicar grow/shrink. Valor por defecto: `auto` (toma el width/height del elemento). Puede especificarse en cualquier unidad CSS. Es la propiedad más incomprendida de Flexbox.

**`flex` (shorthand):** forma recomendada de usar las tres propiedades anteriores. Sintaxis: `flex: <flex-grow> <flex-shrink> <flex-basis>`. Valores comunes:

| Valor | Equivalencia y efecto |
|-------|-----------------------|
| **`flex: 1`** | `flex: 1 1 0%` — crece y se encoge, base cero: distribución proporcional del espacio. |
| **`flex: auto`** | `flex: 1 1 auto` — crece y se encoge, base según el contenido. |
| **`flex: none`** | `flex: 0 0 auto` — no crece ni se encoge: tamaño fijo. |
| **`flex: 0 1 300px`** | No crece, puede encogerse, base de 300px. |

!!! tip "Prefiere el shorthand flex"
    Usa `flex` en lugar de escribir `flex-grow`, `flex-shrink` y `flex-basis` por separado: es más conciso y menos propenso a errores. Recuerda las equivalencias: `flex: 1` = `1 1 0%`, `flex: auto` = `1 1 auto` y `flex: none` = `0 0 auto`.

**`align-self`:** sobrescribe `align-items` para un ítem individual. Admite los mismos valores que `align-items`.

!!! tip "align-self para un ítem concreto"
    Usa `align-self` cuando **un solo ítem** necesita una alineación diferente al resto, por ejemplo una imagen que debe centrarse verticalmente en su celda mientras los demás ítems se estiran.

### 5. Auto margins en Flexbox

!!! tip "Auto margins en Flexbox"
    Una de las características más potentes y menos conocidas de Flexbox es el comportamiento de **`margin: auto`**: en un contenedor flex, un margen automático en un ítem **consume TODO el espacio disponible en esa dirección**, empujando al ítem hacia el extremo opuesto. Esto permite patrones como:
    - `margin-left: auto` en el último ítem de una barra de navegación para empujarlo a la derecha.
    - `margin: auto` en un único ítem para centrarlo perfectamente (alternativa a `justify-content: center`).
    - `margin-top: auto` en el *footer* de una card para empujarlo al fondo, manteniendo la alineación independientemente del contenido.

### 6. Flex-basis vs width

Cuando ambos están definidos, **`flex-basis` tiene prioridad sobre `width`** (o `height` en dirección *column*) para determinar el tamaño base del ítem. Sin embargo, si `flex-basis` es `auto` (valor por defecto), se usa `width`/`height`.

!!! note "Regla de resolución del navegador"
    1. Si `flex-basis` **no** es `auto`, se usa `flex-basis`.
    2. Si `flex-basis` es `auto` y `width`/`height` están definidos, se usa `width`/`height`.
    3. Si ninguno está definido, el tamaño se calcula a partir del contenido.

Por eso, usar `flex: 1` (que establece `flex-basis: 0%`) es diferente a usar `flex: auto` (que establece `flex-basis: auto`). Con `flex: 1`, todos los ítems parten de 0 y se reparten el espacio equitativamente. Con `flex: auto`, parten de su tamaño natural y luego se reparten el espacio restante, resultando en ítems de tamaños diferentes.

!!! warning "flex: 1 no es lo mismo que flex: auto"
    Con **`flex: 1`** (`flex-basis: 0%`) todos los ítems **parten de cero** y obtienen el mismo tamaño. Con **`flex: auto`** respetan el tamaño de su contenido y luego reparten el espacio extra, lo que puede producir **tamaños desiguales**. Confundirlos es una de las causas más habituales de resultados inesperados en Flexbox.

### 7. Patrones de diseño con Flexbox

- **Lista horizontal** — `display: flex; gap: 16px;` en una `<ul>`. Los `<li>` se alinean horizontalmente con espacio uniforme. Combinado con `flex-wrap: wrap` para *responsive*.
- **Centrado perfecto** — `display: flex; justify-content: center; align-items: center;` en el contenedor. Centra el contenido tanto horizontal como verticalmente: el método más simple y efectivo de centrado en CSS.
- **Sticky footer** — `body { display: flex; flex-direction: column; min-height: 100vh; }` y `main { flex: 1; }`. El `<main>` crece para ocupar todo el espacio disponible, empujando el `<footer>` al fondo de la página.
- **Media object** — patrón clásico con imagen a la izquierda y contenido a la derecha: `<div style="display:flex; gap:16px;"><img ...><div>...</div></div>`. La imagen mantiene su tamaño; el contenido ocupa el resto.
- **Igual altura de columnas** — por defecto, los ítems flex en una misma fila tienen la misma altura (`align-items: stretch`).
- **Formulario responsive** — campos en fila con `flex-wrap: wrap`. Etiquetas encima de los *inputs* en móvil (`flex-direction: column`), al lado en escritorio (`flex-direction: row`).
- **Cards alineadas** — contenedor con `display: flex; flex-wrap: wrap; gap: 24px;`. Cada card con `flex: 1 1 300px;` crece y se encoge, con ancho mínimo de 300px. Los *footers* se alinean con `margin-top: auto` dentro de cada card configurada como `display: flex; flex-direction: column;`.

!!! tip "Igual altura sin hacks"
    La **igual altura de columnas** resuelve un problema histórico de CSS: los ítems flex de una misma fila comparten altura gracias a `align-items: stretch`, que es además el valor por defecto. No hace falta JavaScript, *hacks* ni alturas fijas.

### 8. Navbar profesional con Flexbox

Una barra de navegación profesional construida con Flexbox contiene:

!!! tip "Navbar profesional con Flexbox"
    - **Contenedor:** `display: flex; align-items: center; justify-content: space-between; padding: 0 24px;` como base.
    - **Logo:** a la izquierda, con `flex-shrink: 0` para que no se comprima.
    - **Menú de navegación:** `<nav>` con `<ul>` flex, `gap` entre enlaces.
    - **Búsqueda e iconos:** agrupados a la derecha, posiblemente con `margin-left: auto` en el grupo de iconos.
    - **Responsive:** en pantallas pequeñas, el menú se oculta y se muestra un icono de hamburguesa. Implementación CSS pura usando un `<input type="checkbox">` oculto + `<label>` para el icono, y mostrando/ocultando el menú con `:checked`.

### 9. Cards con Flexbox

Las cards son uno de los patrones más comunes en la web. Con Flexbox conseguimos:

!!! tip "Cards con Flexbox"
    - Grid de cards *responsive* con `flex-wrap: wrap` y cada card con `flex: 1 1 300px`.
    - Cards con contenido de altura variable pero *footer* siempre alineado al fondo usando `display: flex; flex-direction: column;` en la card y `margin-top: auto;` en el *footer*.
    - Efectos *hover* con `transition` en `transform` y `box-shadow`.
    - Distribución uniforme del contenido interno con `justify-content: space-between`.

### 10. Formularios con Flexbox

Flexbox simplifica enormemente la alineación de etiquetas y campos en formularios:

!!! tip "Formularios con Flexbox"
    - Cada fila del formulario es un contenedor flex: `display: flex; align-items: center; gap: 12px;`.
    - La etiqueta ocupa un ancho fijo: `flex: 0 0 120px;` o `width: 120px;`.
    - El *input* ocupa el resto: `flex: 1;`.
    - En *responsive*, la dirección cambia a `flex-direction: column` para que la etiqueta quede encima del *input*.
    - Los botones se agrupan con `display: flex; gap: 12px; justify-content: flex-end;`.

### 11. Dashboard con Flexbox

Un dashboard típico tiene: *header* superior, *sidebar* lateral, área de contenido principal con cards. Con Flexbox:

!!! tip "Dashboard con Flexbox"
    - **Layout global:** `body { display: flex; min-height: 100vh; }` o un contenedor principal flex.
    - **Sidebar:** `flex: 0 0 250px;` (ancho fijo) o `flex: 0 0 60px;` (colapsada).
    - **Contenido principal:** `flex: 1;`, ocupa el resto.
    - **Área de cards:** `display: flex; flex-wrap: wrap; gap: 24px;`.
    - **Sidebar colapsable** con CSS puro usando el selector de hermanos `:checked` + `~` para cambiar `flex-basis`.

### 12. Flexbox vs Grid: cuándo usar cada uno

Cuándo conviene cada modelo:

| Criterio | **Flexbox** | **CSS Grid** |
|----------|-------------|--------------|
| **Dimensionalidad** | Unidimensional: una fila **O** una columna | Bidimensional: filas **Y** columnas simultáneamente |
| **Enfoque** | *Content-first*: cuando el **contenido** dicta el *layout* | *Layout-first*: cuando el **layout** dicta dónde va el contenido |
| **Ideales para** | Barras de navegación, listas de elementos, centrado de contenido, distribución de ítems en una dirección | *Layouts* de página completos, galerías con estructura de columnas fija, dashboards |

Ambos se complementan: **Grid para el *layout* macro de la página** y **Flexbox para los componentes** dentro de cada área del grid.

!!! tip "Regla práctica: combinar, no enfrentar"
    Si solo necesitas control en **una dimensión**, usa Flexbox. Si necesitas control en **dos dimensiones**, usa Grid. Grid gestiona la estructura (cabecera, sidebar, contenido, pie) y Flexbox resuelve la alineación interna de cada componente.

## Ejemplos guiados

### Ejemplo 1: Fundamentos de Flexbox - Contenedor e ítems

=== "HTML"

    ``` html
    <!DOCTYPE html>
    <html lang="es">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Fundamentos Flexbox | Ejemplo Didáctico</title>
      <link rel="stylesheet" href="./styles.css">
    </head>
    <body>
      <div class="contenedor">
        <h1>Fundamentos de Flexbox</h1>

        <!-- FLEX-DIRECTION -->
        <h2>1. flex-direction</h2>
        <p><strong>row (por defecto):</strong> Eje principal horizontal, izquierda a derecha.</p>
        <div class="flex-demo row">
          <div class="item">1</div><div class="item">2</div><div class="item">3</div>
        </div>
        <pre>.flex-demo { display: flex; flex-direction: row; gap: 8px; }</pre>

        <p><strong>row-reverse:</strong> Eje principal horizontal, derecha a izquierda. ¡El orden visual se invierte, el del DOM no!</p>
        <div class="flex-demo row-reverse">
          <div class="item">1 (DOM primero)</div><div class="item">2</div><div class="item">3 (DOM último)</div>
        </div>
        <pre>.flex-demo { display: flex; flex-direction: row-reverse; gap: 8px; }</pre>

        <p><strong>column:</strong> Eje principal vertical. Ideal para layouts de página completa.</p>
        <div class="flex-demo col">
          <div class="item">Header</div><div class="item">Content</div><div class="item">Footer</div>
        </div>
        <pre>.flex-demo { display: flex; flex-direction: column; gap: 8px; }</pre>

        <!-- JUSTIFY-CONTENT -->
        <h2>2. justify-content (eje principal)</h2>
        <p><strong>flex-start:</strong> Al inicio del eje principal.</p>
        <div class="flex-demo jc-start"><div class="item">A</div><div class="item">B</div><div class="item">C</div></div>
        <pre>justify-content: flex-start;</pre>

        <p><strong>center:</strong> Centrados horizontalmente.</p>
        <div class="flex-demo jc-center"><div class="item">A</div><div class="item">B</div><div class="item">C</div></div>
        <pre>justify-content: center;</pre>

        <p><strong>space-between:</strong> Espacio entre ítems, los extremos pegados a los bordes.</p>
        <div class="flex-demo jc-between"><div class="item">A</div><div class="item">B</div><div class="item">C</div></div>
        <pre>justify-content: space-between;</pre>

        <p><strong>space-around:</strong> Espacio alrededor de cada ítem (mitad en extremos).</p>
        <div class="flex-demo jc-around"><div class="item">A</div><div class="item">B</div><div class="item">C</div></div>
        <pre>justify-content: space-around;</pre>

        <p><strong>space-evenly:</strong> Espacio exactamente igual en todas partes.</p>
        <div class="flex-demo jc-evenly"><div class="item">A</div><div class="item">B</div><div class="item">C</div></div>
        <pre>justify-content: space-evenly;</pre>

        <p><strong>flex-end:</strong> Al final del eje principal.</p>
        <div class="flex-demo jc-end"><div class="item">A</div><div class="item">B</div><div class="item">C</div></div>
        <pre>justify-content: flex-end;</pre>

        <!-- ALIGN-ITEMS -->
        <h2>3. align-items (eje transversal)</h2>
        <p><strong>stretch (por defecto):</strong> Los ítems se estiran para llenar la altura del contenedor. Observa cómo el ítem bajo también alcanza la altura total.</p>
        <div class="flex-demo ai-stretch">
          <div class="item alto">Alto</div><div class="item bajo">Bajo</div><div class="item">Normal</div>
        </div>
        <pre>align-items: stretch; /* por defecto */</pre>

        <p><strong>center:</strong> Centrados verticalmente. ¡La forma más fácil de centrar en CSS!</p>
        <div class="flex-demo ai-center">
          <div class="item alto">Alto</div><div class="item bajo">Bajo</div><div class="item">Normal</div>
        </div>
        <pre>align-items: center;</pre>

        <p><strong>flex-start:</strong> Alineados al inicio del cross axis (arriba).</p>
        <div class="flex-demo ai-start">
          <div class="item alto">Alto</div><div class="item bajo">Bajo</div><div class="item">Normal</div>
        </div>
        <pre>align-items: flex-start;</pre>

        <p><strong>flex-end:</strong> Alineados al final del cross axis (abajo).</p>
        <div class="flex-demo ai-end">
          <div class="item alto">Alto</div><div class="item bajo">Bajo</div><div class="item">Normal</div>
        </div>
        <pre>align-items: flex-end;</pre>

        <!-- FLEX-WRAP -->
        <h2>4. flex-wrap</h2>
        <p><strong>wrap:</strong> Los ítems que no caben saltan a la siguiente línea. Redimensiona el navegador.</p>
        <div class="flex-demo wrap">
          <div class="item">Item 1</div><div class="item">Item 2</div>
          <div class="item">Item 3</div><div class="item">Item 4</div>
          <div class="item">Item 5</div><div class="item">Item 6</div>
        </div>

        <p><strong>nowrap:</strong> Los ítems se comprimen pero nunca saltan de línea. Pueden desbordarse.</p>
        <div class="flex-demo nowrap" style="overflow-x:auto;">
          <div class="item">Item 1</div><div class="item">Item 2</div>
          <div class="item">Item 3</div><div class="item">Item 4</div>
          <div class="item">Item 5</div><div class="item">Item 6</div>
        </div>

        <!-- GAP -->
        <h2>5. gap</h2>
        <p>gap: 24px entre todos los ítems. Más limpio que usar margin.</p>
        <div class="flex-demo gap-demo">
          <div class="item">A</div><div class="item">B</div><div class="item">C</div>
        </div>
        <pre>gap: 24px;</pre>
      </div>
    </body>
    </html>
    ```

=== "CSS"

    ``` css
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: 'Segoe UI', system-ui, sans-serif; background: #f8fafc; padding: 40px; color: #1e293b; }
    .contenedor { max-width: 900px; margin: 0 auto; }
    h1 { color: #2563eb; margin-bottom: 32px; }
    h2 { margin: 32px 0 16px; color: #334155; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px; }

    /* === ESTILOS DE DEMOSTRACIÓN === */

    /* Contenedor flex de demostración */
    .flex-demo {
      background: #e2e8f0; border-radius: 8px; padding: 16px;
      margin-bottom: 12px; min-height: 100px;
    }
    /* Items de demostración */
    .item {
      background: #2563eb; color: #fff; padding: 20px;
      border-radius: 6px; font-weight: 600; text-align: center;
      min-width: 60px; font-size: 0.9rem;
    }

    /* === 1. FLEX-DIRECTION === */
    .row { display: flex; flex-direction: row; gap: 8px; }
    .row-reverse { display: flex; flex-direction: row-reverse; gap: 8px; }
    .col { display: flex; flex-direction: column; gap: 8px; }

    /* === 2. JUSTIFY-CONTENT === */
    .jc-start { display: flex; justify-content: flex-start; gap: 8px; }
    .jc-end { display: flex; justify-content: flex-end; gap: 8px; }
    .jc-center { display: flex; justify-content: center; gap: 8px; }
    .jc-between { display: flex; justify-content: space-between; }
    .jc-around { display: flex; justify-content: space-around; }
    .jc-evenly { display: flex; justify-content: space-evenly; }

    /* === 3. ALIGN-ITEMS === */
    .ai-stretch { display: flex; align-items: stretch; gap: 8px; }
    .ai-start { display: flex; align-items: flex-start; gap: 8px; }
    .ai-end { display: flex; align-items: flex-end; gap: 8px; }
    .ai-center { display: flex; align-items: center; gap: 8px; }

    /* Items de diferentes alturas para demostrar align-items */
    .item.alto { padding: 40px 20px; }
    .item.bajo { padding: 12px 20px; }

    /* === 4. FLEX-WRAP === */
    .wrap { display: flex; flex-wrap: wrap; gap: 8px; }
    .wrap .item { flex: 0 0 calc(25% - 8px); }

    .nowrap { display: flex; flex-wrap: nowrap; gap: 8px; }
    .nowrap .item { flex: 0 0 calc(25% - 8px); }

    /* === 5. GAP === */
    .gap-demo { display: flex; gap: 24px; }
    .column-gap-demo { display: flex; column-gap: 32px; row-gap: 8px; flex-wrap: wrap; }

    /* === CONTROLES PARA PROBAR === */
    .controles { display: flex; gap: 12px; flex-wrap: wrap; margin: 24px 0; }
    .controles button {
      padding: 8px 16px; background: #fff; border: 1px solid #e2e8f0;
      border-radius: 4px; cursor: pointer; font-size: 0.85rem;
      transition: background 0.2s;
    }
    .controles button:hover { background: #f1f5f9; }
    .controles button.activo { background: #2563eb; color: #fff; border-color: #2563eb; }

    /* Código de ejemplo */
    pre { background: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 6px; overflow-x: auto; font-size: 0.85rem; margin: 8px 0; }
    ```

### Ejemplo 2: Propiedades de los ítems flex (grow, shrink, basis, order, align-self)

=== "HTML"

    ``` html
    <!DOCTYPE html>
    <html lang="es">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Propiedades de Items Flex | Ejemplo Didáctico</title>
      <link rel="stylesheet" href="./styles.css">
    </head>
    <body>
      <div class="contenedor">
        <h1>Propiedades de los Ítems Flex</h1>

        <!-- FLEX-GROW -->
        <h2>1. flex-grow (factor de crecimiento)</h2>
        <p>Todos <code>flex-grow: 0</code> (por defecto): no crecen. Ocupan solo su contenido.</p>
        <div class="flex-demo">
          <div class="item" style="flex-grow:0;">grow:0</div>
          <div class="item" style="flex-grow:0;">grow:0</div>
          <div class="item" style="flex-grow:0;">grow:0</div>
        </div>
        <pre>.item { flex-grow: 0; } /* no crecen */</pre>

        <p>Todos <code>flex-grow: 1</code>: se reparten el espacio equitativamente.</p>
        <div class="flex-demo">
          <div class="item" style="flex-grow:1;">grow:1</div>
          <div class="item" style="flex-grow:1;">grow:1</div>
          <div class="item" style="flex-grow:1;">grow:1</div>
        </div>
        <pre>.item { flex-grow: 1; } /* crecen equitativamente */</pre>

        <p>Mix: <code>grow:1</code>, <code>grow:2</code>, <code>grow:1</code>. El segundo recibe el doble de espacio extra.</p>
        <div class="flex-demo">
          <div class="item" style="flex-grow:1;">grow:1</div>
          <div class="item" style="flex-grow:2;">grow:2</div>
          <div class="item" style="flex-grow:1;">grow:1</div>
        </div>
        <pre>.item:nth-child(1) { flex-grow: 1; }
    .item:nth-child(2) { flex-grow: 2; }
    .item:nth-child(3) { flex-grow: 1; }</pre>

        <!-- FLEX-SHRINK -->
        <h2>2. flex-shrink (factor de reducción)</h2>
        <p><code>flex-shrink: 0</code> en el tercer ítem: no se encoge aunque falte espacio.</p>
        <div class="flex-demo" style="max-width:600px;">
          <div class="item" style="flex:0 1 200px;">shrink:1</div>
          <div class="item" style="flex:0 1 200px;">shrink:1</div>
          <div class="item" style="flex:0 0 200px;">shrink:0</div>
        </div>
        <pre>.item-especial { flex-shrink: 0; } /* este ítem no se encoge nunca */</pre>

        <!-- FLEX-BASIS -->
        <h2>3. flex-basis (tamaño base)</h2>
        <p>Ítems con <code>flex-basis</code> de 200px, 300px y 200px. Crecen/shrink desde su base.</p>
        <div class="flex-demo">
          <div class="item" style="flex:0 1 200px;">basis:200px</div>
          <div class="item" style="flex:0 1 300px;">basis:300px</div>
          <div class="item" style="flex:0 1 200px;">basis:200px</div>
        </div>
        <pre>.item { flex: 0 1 200px; } /* flex-grow:0 flex-shrink:1 flex-basis:200px */</pre>

        <!-- ORDER -->
        <h2>4. order (orden visual)</h2>
        <p>El ítem con <code>order: -1</code> aparece primero visualmente aunque sea el tercero en el DOM.</p>
        <div class="flex-demo">
          <div class="item" style="order:2;">DOM 1º, Order 2</div>
          <div class="item" style="order:3;">DOM 2º, Order 3</div>
          <div class="item" style="order:-1;">DOM 3º, Order -1</div>
        </div>
        <pre>.item-prioritario { order: -1; } /* Aparece primero visualmente */</pre>

        <!-- ALIGN-SELF -->
        <h2>5. align-self (alineación individual)</h2>
        <p>Contenedor con <code>align-items: center</code>, pero el segundo ítem se alinea al inicio.</p>
        <div class="flex-demo" style="align-items:center;min-height:120px;">
          <div class="item">Centrado</div>
          <div class="item" style="align-self:flex-start;">align-self: flex-start</div>
          <div class="item">Centrado</div>
        </div>
        <pre>.contenedor { align-items: center; }
    .item-especial { align-self: flex-start; }</pre>

        <!-- MARGIN AUTO -->
        <h2>6. Auto margins (magia flex)</h2>
        <p><code>margin-left: auto</code> en el último ítem lo empuja a la derecha.</p>
        <div class="flex-demo">
          <div class="item">Logo</div>
          <div class="item">Enlace 1</div>
          <div class="item">Enlace 2</div>
          <div class="item" style="margin-left:auto;">Perfil</div>
        </div>
        <pre>.item-ultimo { margin-left: auto; } /* Empuja a la derecha */</pre>

        <p><code>margin: auto</code> en un único ítem lo centra perfectamente (alternativa a justify-content).</p>
        <div class="flex-demo">
          <div class="item" style="margin:auto;">Centrado con margin:auto</div>
        </div>
        <pre>.item-unico { margin: auto; } /* Centrado perfecto */</pre>
      </div>
    </body>
    </html>
    ```

=== "CSS"

    ``` css
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: 'Segoe UI', system-ui, sans-serif; background: #f8fafc; padding: 40px; color: #1e293b; }
    .contenedor { max-width: 900px; margin: 0 auto; }
    h1 { color: #2563eb; margin-bottom: 32px; }
    h2 { margin: 32px 0 16px; color: #334155; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px; }
    .flex-demo { background: #e2e8f0; border-radius: 8px; padding: 16px; margin-bottom: 12px; display: flex; gap: 8px; }
    .item {
      background: #2563eb; color: #fff; padding: 16px; border-radius: 6px;
      font-weight: 600; text-align: center; font-size: 0.85rem; transition: all 0.3s ease;
    }
    pre { background: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 6px; overflow-x: auto; font-size: 0.85rem; margin: 8px 0; }
    ```

### Ejemplo 3: Navbar profesional responsive con hamburguesa CSS puro

=== "HTML"

    ``` html
    <!DOCTYPE html>
    <html lang="es">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Navbar Profesional Flexbox | Ejemplo Didáctico</title>
      <link rel="stylesheet" href="./styles.css">
    </head>
    <body>
      <header class="header">
        <div class="navbar">
          <!-- LOGO -->
          <a href="/" class="navbar__logo">Tech<span>Corp</span></a>

          <!-- CHECKBOX OCULTO que controla el toggle del menú en móvil -->
          <input type="checkbox" id="menu-toggle" class="navbar__toggle">
          <label for="menu-toggle" class="navbar__toggle-label" aria-label="Abrir menú de navegación">
            &#9776;
          </label>

          <!-- MENÚ DE NAVEGACIÓN -->
          <nav>
            <ul class="navbar__menu">
              <li><a href="/" class="activo">Inicio</a></li>
              <li><a href="/productos/">Productos</a></li>
              <li><a href="/servicios/">Servicios</a></li>
              <li><a href="/blog/">Blog</a></li>
              <li><a href="/contacto/">Contacto</a></li>
            </ul>
          </nav>

          <!-- ACCIONES: búsqueda + iconos -->
          <div class="navbar__acciones">
            <input type="search" class="navbar__busqueda" placeholder="Buscar..." aria-label="Buscar en el sitio">
            <button class="navbar__icono" aria-label="Notificaciones">&#128276;</button>
            <button class="navbar__icono" aria-label="Perfil de usuario">&#128100;</button>
          </div>
        </div>
      </header>

      <main>
        <h1>Navbar Profesional con Flexbox</h1>
        <p>
          Esta barra de navegación utiliza Flexbox para alinear logo, menú, búsqueda e iconos.
          En pantallas grandes (mayores de 768px), todos los elementos se muestran en una fila.
          En pantallas pequeñas, el menú se colapsa y se muestra mediante un icono hamburguesa implementado con CSS puro (checkbox + label + :checked).
        </p>
        <p>
          <strong>Características:</strong> menú con flex, icono hamburguesa CSS puro sin JavaScript, búsqueda integrada, diseño sticky (se queda fija al hacer scroll), responsive con dos breakpoints.
        </p>
        <p>
          <strong>Prueba:</strong> Redimensiona el navegador a menos de 768px de ancho. Verás desaparecer el menú y aparecer el icono ☰. Haz clic en él para desplegar el menú.
        </p>
      </main>
    </body>
    </html>
    ```

=== "CSS"

    ``` css
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: 'Segoe UI', system-ui, sans-serif; line-height: 1.6; color: #1e293b; }

    /* =============================================
       HEADER: Barra de navegación principal
       ============================================= */
    .header {
      background: #0f172a;
      color: #fff;
      padding: 0 24px;
      position: sticky;
      top: 0;
      z-index: 1000;
    }

    /* CONTENEDOR DE LA NAVBAR: flex con alineación centrada */
    .navbar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      max-width: 1200px;
      margin: 0 auto;
      min-height: 64px;
      flex-wrap: wrap;
    }

    /* LOGO: no se encoge nunca */
    .navbar__logo {
      font-size: 1.4rem;
      font-weight: 700;
      text-decoration: none;
      color: #fff;
      flex-shrink: 0;
    }
    .navbar__logo span { color: #60a5fa; }

    /* =============================================
       MENÚ DE NAVEGACIÓN
       ============================================= */
    .navbar__menu {
      display: flex;
      list-style: none;
      gap: 4px;
    }
    .navbar__menu a {
      color: #cbd5e1;
      text-decoration: none;
      padding: 8px 16px;
      border-radius: 6px;
      display: block;
      font-weight: 500;
      font-size: 0.95rem;
      transition: background 0.2s, color 0.2s;
    }
    .navbar__menu a:hover { background: rgba(255,255,255,0.1); color: #fff; }
    .navbar__menu a.activo { background: #2563eb; color: #fff; }

    /* =============================================
       ICONOS Y BÚSQUEDA (lado derecho)
       ============================================= */
    .navbar__acciones {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    /* Input de búsqueda */
    .navbar__busqueda {
      padding: 8px 14px;
      border: 1px solid #334155;
      border-radius: 20px;
      background: #1e293b;
      color: #e2e8f0;
      font-size: 0.9rem;
      width: 200px;
      transition: border-color 0.2s, background 0.2s;
    }
    .navbar__busqueda:focus {
      outline: none;
      border-color: #60a5fa;
      background: #0f172a;
    }

    /* Iconos */
    .navbar__icono {
      background: none;
      border: none;
      color: #cbd5e1;
      font-size: 1.2rem;
      cursor: pointer;
      padding: 8px;
      border-radius: 50%;
      transition: background 0.2s, color 0.2s;
    }
    .navbar__icono:hover { background: rgba(255,255,255,0.1); color: #fff; }

    /* =============================================
       HAMBURGUESA (CSS PURO: checkbox + label)
       El checkbox está oculto. El label muestra el icono ☰.
       Al marcar :checked, el menú se muestra.
       ============================================= */
    .navbar__toggle {
      display: none; /* Oculto en desktop */
    }
    .navbar__toggle-label {
      display: none; /* Oculto en desktop */
    }

    /* Contenido principal para demo */
    main { max-width: 800px; margin: 0 auto; padding: 40px 24px; }
    main h1 { color: #2563eb; margin-bottom: 16px; }
    main p { margin-bottom: 16px; color: #475569; }

    /* =============================================
       RESPONSIVE: Tablet y móvil (< 768px)
       ============================================= */
    @media (max-width: 768px) {
      .navbar { padding: 8px 0; }

      /* Mostrar el icono hamburguesa */
      .navbar__toggle-label {
        display: flex;
        align-items: center;
        cursor: pointer;
        font-size: 1.6rem;
        color: #cbd5e1;
        padding: 8px;
      }

      /* El menú se oculta por defecto en móvil */
      .navbar__menu {
        display: none;
        flex-direction: column;
        width: 100%;
        order: 3; /* Se coloca debajo del logo y el toggle */
        padding: 8px 0 16px 0;
      }

      /* MOSTRAR MENÚ cuando el checkbox está marcado (:checked) */
      .navbar__toggle:checked ~ .navbar__menu {
        display: flex;
      }

      /* Ajustar búsqueda en móvil */
      .navbar__busqueda { width: 140px; font-size: 0.8rem; }
    }

    @media (max-width: 480px) {
      .navbar__acciones { gap: 6px; }
      .navbar__busqueda { width: 100px; }
    }
    ```

### Ejemplo 4: Cards responsivas con footer alineado y altura variable

=== "HTML"

    ``` html
    <!DOCTYPE html>
    <html lang="es">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Cards Flexbox | Ejemplo Didáctico</title>
      <link rel="stylesheet" href="./styles.css">
    </head>
    <body>
      <div class="contenedor">
        <h1>Cursos Disponibles</h1>
        <p class="subtitulo">Las tarjetas tienen altura uniforme y el precio siempre está alineado al fondo, independientemente del contenido.</p>

        <div class="cards-grid">
          <!-- Card 1 -->
          <article class="card">
            <div class="card__imagen" style="background:linear-gradient(135deg,#667eea,#764ba2);"></div>
            <div class="card__body">
              <h3 class="card__title">Desarrollo Web Frontend</h3>
              <p class="card__text">Aprende HTML5, CSS3 y JavaScript moderno. Construye interfaces responsive y accesibles desde cero.</p>
            </div>
            <div class="card__footer">
              <span class="card__precio">€49.99</span>
              <button class="card__btn">Inscribirse</button>
            </div>
          </article>

          <!-- Card 2 (contenido más largo - el footer sigue alineado) -->
          <article class="card card--destacada">
            <div class="card__imagen" style="background:linear-gradient(135deg,#f093fb,#f5576c);"></div>
            <div class="card__body">
              <h3 class="card__title">React Avanzado</h3>
              <p class="card__text">Domina React con hooks, context API, gestión de estado con Redux y testing con Jest y React Testing Library. Este curso incluye un proyecto final completo de una aplicación de comercio electrónico con autenticación, carrito de compras y panel de administración.</p>
            </div>
            <div class="card__footer">
              <span class="card__precio">€79.99</span>
              <button class="card__btn">Inscribirse</button>
            </div>
          </article>

          <!-- Card 3 -->
          <article class="card">
            <div class="card__imagen" style="background:linear-gradient(135deg,#a18cd1,#fbc2eb);"></div>
            <div class="card__body">
              <h3 class="card__title">CSS Pro</h3>
              <p class="card__text">Flexbox, Grid, animaciones avanzadas, arquitectura CSS con metodologías ITCSS y BEM.</p>
            </div>
            <div class="card__footer">
              <span class="card__precio">€39.99</span>
              <button class="card__btn">Inscribirse</button>
            </div>
          </article>

          <!-- Card 4 -->
          <article class="card">
            <div class="card__imagen" style="background:linear-gradient(135deg,#89f7fe,#66a6ff);"></div>
            <div class="card__body">
              <h3 class="card__title">Node.js Backend</h3>
              <p class="card__text">APIs RESTful, Express, bases de datos SQL y NoSQL, autenticación JWT y despliegue en la nube.</p>
            </div>
            <div class="card__footer">
              <span class="card__precio">€59.99</span>
              <button class="card__btn">Inscribirse</button>
            </div>
          </article>

          <!-- Card 5 -->
          <article class="card">
            <div class="card__imagen" style="background:linear-gradient(135deg,#fddb92,#d1fdff);"></div>
            <div class="card__body">
              <h3 class="card__title">Python para Data Science</h3>
              <p class="card__text">Pandas, NumPy, visualización de datos, machine learning con scikit-learn y despliegue de modelos.</p>
            </div>
            <div class="card__footer">
              <span class="card__precio">€69.99</span>
              <button class="card__btn">Inscribirse</button>
            </div>
          </article>

          <!-- Card 6 -->
          <article class="card">
            <div class="card__imagen" style="background:linear-gradient(135deg,#cfd9df,#e2ebf0);"></div>
            <div class="card__body">
              <h3 class="card__title">Diseño UX/UI</h3>
              <p class="card__text">Investigación de usuarios, wireframes, prototipado con Figma, design systems y accesibilidad.</p>
            </div>
            <div class="card__footer">
              <span class="card__precio">€44.99</span>
              <button class="card__btn">Inscribirse</button>
            </div>
          </article>
        </div>
      </div>
    </body>
    </html>
    ```

=== "CSS"

    ``` css
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      background: #f1f5f9; color: #1e293b; line-height: 1.6;
      padding: 40px 20px;
    }
    .contenedor { max-width: 1100px; margin: 0 auto; }
    h1 { color: #2563eb; margin-bottom: 8px; text-align: center; }
    .subtitulo { text-align: center; color: #64748b; margin-bottom: 40px; }

    /* =============================================
       GRID DE CARDS con flex-wrap
       Cada card tiene flex: 1 1 300px:
       - flex-grow: 1 → crece para llenar espacio
       - flex-shrink: 1 → se encoge si es necesario
       - flex-basis: 300px → ancho base de 300px
       ============================================= */
    .cards-grid {
      display: flex;
      flex-wrap: wrap;
      gap: 24px;
    }

    .card {
      flex: 1 1 300px;
      background: #fff;
      border-radius: 12px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.06);
      overflow: hidden;
      transition: transform 0.2s ease, box-shadow 0.2s ease;

      /* CLAVE: la card también es flex en dirección columna
         para que el footer se alinee al fondo */
      display: flex;
      flex-direction: column;
    }
    .card:hover {
      transform: translateY(-4px);
      box-shadow: 0 8px 24px rgba(0,0,0,0.1);
    }

    /* Imagen de la card: tamaño fijo, no se deforma */
    .card__imagen {
      width: 100%;
      height: 180px;
      object-fit: cover;
      background: linear-gradient(135deg, #667eea, #764ba2);
    }

    /* Cuerpo de la card: ocupa el espacio disponible (crece) */
    .card__body {
      padding: 20px;
      flex: 1; /* CRECE para llenar el espacio entre header y footer */
    }
    .card__title {
      color: #1e293b;
      font-size: 1.1rem;
      margin-bottom: 8px;
    }
    .card__text {
      color: #64748b;
      font-size: 0.92rem;
    }

    /* Footer de la card: alineado al fondo gracias al flex column */
    .card__footer {
      padding: 16px 20px;
      border-top: 1px solid #e2e8f0;
      /* margin-top: auto también funciona, pero flex:1 en body ya lo empuja */
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .card__precio {
      font-weight: 700;
      font-size: 1.2rem;
      color: #2563eb;
    }
    .card__btn {
      padding: 8px 16px;
      background: #2563eb;
      color: #fff;
      border: none;
      border-radius: 6px;
      cursor: pointer;
      font-weight: 600;
      font-size: 0.85rem;
      transition: background 0.2s;
    }
    .card__btn:hover { background: #1d4ed8; }

    /* Variación: card destacada con borde superior de color */
    .card--destacada {
      border-top: 4px solid #2563eb;
    }

    @media (max-width: 600px) {
      .card { flex: 1 1 100%; }
    }
    ```

### Ejemplo 5: Dashboard con sidebar flexible y colapsable CSS puro

=== "HTML"

    ``` html
    <!DOCTYPE html>
    <html lang="es">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Dashboard Flexbox | Ejemplo Didáctico</title>
      <link rel="stylesheet" href="./styles.css">
    </head>
    <body>
      <!-- CHECKBOX OCULTO: controla el colapso de la sidebar -->
      <input type="checkbox" id="sidebar-toggle">

      <div class="dashboard">
        <!-- SIDEBAR -->
        <aside class="sidebar">
          <div class="sidebar__header">
            <span class="sidebar__texto">Admin Panel</span>
          </div>

          <!-- Botón de toggle del sidebar (label del checkbox) -->
          <label for="sidebar-toggle" class="sidebar__toggle-btn" aria-label="Colapsar barra lateral">
            &#9776; <span class="sidebar__texto">Colapsar</span>
          </label>

          <!-- Navegación -->
          <nav class="sidebar__nav">
            <a href="#" class="activo"><span class="icono">&#9632;</span> <span class="sidebar__texto">Dashboard</span></a>
            <a href="#"><span class="icono">&#9998;</span> <span class="sidebar__texto">Proyectos</span></a>
            <a href="#"><span class="icono">&#128100;</span> <span class="sidebar__texto">Usuarios</span></a>
            <a href="#"><span class="icono">&#128202;</span> <span class="sidebar__texto">Reportes</span></a>
            <a href="#"><span class="icono">&#9881;</span> <span class="sidebar__texto">Configuración</span></a>
          </nav>

          <div class="sidebar__footer">
            <span class="sidebar__texto">&copy; 2025 TechCorp</span>
          </div>
        </aside>

        <!-- CONTENIDO PRINCIPAL -->
        <main class="main-content">
          <header class="main-header">
            <h1>Dashboard</h1>
            <div class="usuario">
              <span>María López</span>
              <div class="avatar">ML</div>
            </div>
          </header>

          <div class="main-body">
            <!-- Cards de estadísticas -->
            <div class="stats-grid">
              <div class="stat-card">
                <div class="stat-card__label">Ingresos Totales</div>
                <div class="stat-card__value">€48,250</div>
                <div class="stat-card__change">+12.5% vs mes anterior</div>
              </div>
              <div class="stat-card">
                <div class="stat-card__label">Usuarios Activos</div>
                <div class="stat-card__value">2,847</div>
                <div class="stat-card__change">+8.3% vs mes anterior</div>
              </div>
              <div class="stat-card">
                <div class="stat-card__label">Tasa de Conversión</div>
                <div class="stat-card__value">3.24%</div>
                <div class="stat-card__change">+1.1% vs mes anterior</div>
              </div>
              <div class="stat-card">
                <div class="stat-card__label">Tickets Pendientes</div>
                <div class="stat-card__value">142</div>
                <div class="stat-card__change" style="color:#dc2626;">-5.2% vs ayer</div>
              </div>
            </div>

            <!-- Contenido secundario -->
            <div class="content-row">
              <div class="content-col">
                <h2>Actividad Reciente</h2>
                <p style="color:#64748b;">Los datos se actualizan en tiempo real. El dashboard está construido completamente con Flexbox.</p>
              </div>
              <div class="content-col">
                <h2>Próximas Tareas</h2>
                <p style="color:#64748b;">Prueba a colapsar la sidebar con el botón de la izquierda. Todo funciona con CSS puro.</p>
              </div>
            </div>
          </div>
        </main>
      </div>
    </body>
    </html>
    ```

=== "CSS"

    ``` css
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: 'Segoe UI', system-ui, sans-serif; color: #1e293b; }

    /* =============================================
       LAYOUT PRINCIPAL DEL DASHBOARD
       body como contenedor flex en fila
       ============================================= */
    .dashboard {
      display: flex;
      min-height: 100vh;
    }

    /* =============================================
       SIDEBAR (barra lateral)
       flex: 0 0 250px → ancho fijo, no crece ni se encoge
       display: flex + flex-direction: column para el contenido interno
       ============================================= */
    .sidebar {
      flex: 0 0 250px;
      background: #0f172a;
      color: #cbd5e1;
      display: flex;
      flex-direction: column;
      transition: flex-basis 0.3s ease;
      overflow: hidden;
    }

    .sidebar__header {
      padding: 24px 20px;
      font-weight: 700;
      font-size: 1.2rem;
      color: #fff;
      border-bottom: 1px solid #1e293b;
    }

    /* Navegación de la sidebar */
    .sidebar__nav {
      flex: 1;
      padding: 16px 0;
      overflow-y: auto;
    }
    .sidebar__nav a {
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 12px 20px;
      color: #94a3b8;
      text-decoration: none;
      transition: background 0.15s, color 0.15s;
      font-size: 0.92rem;
      white-space: nowrap;
    }
    .sidebar__nav a:hover { background: #1e293b; color: #e2e8f0; }
    .sidebar__nav a.activo { background: #2563eb; color: #fff; }

    .sidebar__nav .icono { font-size: 1.1rem; width: 24px; text-align: center; }

    /* Footer de la sidebar */
    .sidebar__footer {
      padding: 16px 20px;
      border-top: 1px solid #1e293b;
      font-size: 0.8rem;
      color: #64748b;
    }

    /* =============================================
       CHECKBOX PARA COLAPSAR LA SIDEBAR (CSS puro)
       El checkbox está oculto. Al marcarse, la sidebar cambia
       su flex-basis a 60px y oculta los textos
       ============================================= */
    #sidebar-toggle { display: none; }

    /* BOTÓN DE TOGGLE (label del checkbox) */
    .sidebar__toggle-btn {
      display: block;
      padding: 12px 20px;
      cursor: pointer;
      text-align: right;
      color: #94a3b8;
      font-size: 0.9rem;
      user-select: none;
    }
    .sidebar__toggle-btn:hover { color: #fff; }

    /* CUANDO EL CHECKBOX ESTÁ MARCADO:
       La sidebar se colapsa a 60px de ancho y oculta los textos */
    #sidebar-toggle:checked ~ .sidebar {
      flex: 0 0 60px;
    }
    #sidebar-toggle:checked ~ .sidebar .sidebar__texto {
      display: none;
    }
    #sidebar-toggle:checked ~ .sidebar .sidebar__header {
      font-size: 0;
    }
    #sidebar-toggle:checked ~ .sidebar .sidebar__footer {
      display: none;
    }

    /* =============================================
       CONTENIDO PRINCIPAL
       flex: 1 → ocupa todo el espacio restante
       display: flex + flex-direction: column
       ============================================= */
    .main-content {
      flex: 1;
      display: flex;
      flex-direction: column;
      min-width: 0;
      background: #f1f5f9;
    }

    /* HEADER del contenido */
    .main-header {
      background: #fff;
      padding: 16px 24px;
      border-bottom: 1px solid #e2e8f0;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .main-header h1 { font-size: 1.3rem; color: #1e293b; }
    .main-header .usuario {
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .main-header .avatar {
      width: 36px; height: 36px;
      background: #2563eb; border-radius: 50%;
      display: flex; align-items: center; justify-content: center;
      color: #fff; font-weight: 700; font-size: 0.9rem;
    }

    /* ÁREA DE CONTENIDO (scrollable) */
    .main-body {
      flex: 1;
      padding: 24px;
      overflow-y: auto;
    }

    /* GRID DE CARDS DE ESTADÍSTICAS con flex-wrap */
    .stats-grid {
      display: flex;
      flex-wrap: wrap;
      gap: 24px;
      margin-bottom: 32px;
    }
    .stat-card {
      flex: 1 1 200px;
      background: #fff;
      padding: 24px;
      border-radius: 12px;
      box-shadow: 0 1px 4px rgba(0,0,0,0.04);
    }
    .stat-card__label { font-size: 0.85rem; color: #64748b; margin-bottom: 4px; }
    .stat-card__value { font-size: 1.8rem; font-weight: 700; color: #1e293b; }
    .stat-card__change { font-size: 0.8rem; color: #16a34a; }

    /* Layout para el resto de contenido */
    .content-row {
      display: flex;
      flex-wrap: wrap;
      gap: 24px;
    }
    .content-col {
      flex: 1 1 400px;
      background: #fff;
      border-radius: 12px;
      padding: 24px;
      box-shadow: 0 1px 4px rgba(0,0,0,0.04);
    }
    .content-col h2 { margin-bottom: 16px; color: #334155; font-size: 1.1rem; }

    /* RESPONSIVE */
    @media (max-width: 768px) {
      .sidebar { flex: 0 0 200px; }
      #sidebar-toggle:checked ~ .sidebar { flex: 0 0 50px; }
      .stats-grid { gap: 12px; }
      .stat-card { flex: 1 1 140px; padding: 16px; }
    }
    @media (max-width: 480px) {
      .dashboard { flex-direction: column; }
      .sidebar { flex: 0 0 auto; }
      .sidebar__nav { display: flex; overflow-x: auto; }
      .sidebar__nav a { padding: 12px; }
      #sidebar-toggle, .sidebar__toggle-btn { display: none; }
    }
    ```

### Ejemplo 6: Formulario responsive con Flexbox

=== "HTML"

    ``` html
    <!DOCTYPE html>
    <html lang="es">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Formulario Flexbox | Ejemplo Didáctico</title>
      <link rel="stylesheet" href="./styles.css">
    </head>
    <body>
      <div class="form-container">
        <h1>Formulario de Contacto</h1>

        <form>
          <!-- FILA 1: Nombre y Apellidos (2 campos en la misma fila) -->
          <div style="display:flex;gap:16px;flex-wrap:wrap;">
            <div class="form-row" style="flex:1 1 250px;">
              <label for="nombre">Nombre</label>
              <input type="text" id="nombre" name="nombre" required placeholder="Tu nombre">
            </div>
            <div class="form-row" style="flex:1 1 250px;">
              <label for="apellidos">Apellidos</label>
              <input type="text" id="apellidos" name="apellidos" required placeholder="Tus apellidos">
            </div>
          </div>

          <!-- FILA 2: Email -->
          <div class="form-row">
            <label for="email">Email</label>
            <input type="email" id="email" name="email" required placeholder="tu@email.com">
          </div>

          <!-- FILA 3: Teléfono -->
          <div class="form-row">
            <label for="telefono">Teléfono</label>
            <input type="tel" id="telefono" name="telefono" placeholder="+34 600 000 000">
          </div>

          <!-- BLOQUE: Mensaje (label arriba porque ocupa más espacio) -->
          <div class="form-block">
            <label for="mensaje">Mensaje</label>
            <textarea id="mensaje" name="mensaje" rows="4" placeholder="Escribe tu mensaje aquí..."></textarea>
          </div>

          <!-- BOTONES -->
          <div class="form-actions">
            <button type="button" class="btn-secondary">Cancelar</button>
            <button type="submit" class="btn-primary">Enviar Mensaje</button>
          </div>
        </form>
      </div>
    </body>
    </html>
    ```

=== "CSS"

    ``` css
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      background: #f1f5f9; color: #1e293b; line-height: 1.6;
      padding: 40px 20px; display: flex; justify-content: center;
    }
    .form-container {
      background: #fff; border-radius: 12px;
      box-shadow: 0 4px 24px rgba(0,0,0,0.06);
      padding: 40px; max-width: 700px; width: 100%;
    }
    h1 { color: #2563eb; margin-bottom: 32px; }
    h2 { color: #334155; margin: 32px 0 16px; font-size: 1.1rem; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px; }

    /* === FILA DE FORMULARIO CON FLEXBOX ===
       Cada .form-row es un contenedor flex.
       En desktop: label a la izquierda (120px), input a la derecha (flex:1).
       En mobile: dirección column, label encima del input. */
    .form-row {
      display: flex;
      align-items: center;
      gap: 16px;
      margin-bottom: 20px;
    }
    .form-row label {
      flex: 0 0 130px;
      font-weight: 600;
      font-size: 0.9rem;
      color: #334155;
    }
    .form-row input,
    .form-row select,
    .form-row textarea {
      flex: 1;
      padding: 10px 14px;
      border: 1px solid #e2e8f0;
      border-radius: 6px;
      font-size: 0.95rem;
      font-family: inherit;
      transition: border-color 0.2s, box-shadow 0.2s;
    }
    .form-row input:focus,
    .form-row select:focus,
    .form-row textarea:focus {
      outline: none;
      border-color: #2563eb;
      box-shadow: 0 0 0 3px rgba(37,99,235,0.1);
    }

    /* Variante: label arriba del input (para campos más complejos) */
    .form-block {
      display: flex;
      flex-direction: column;
      gap: 6px;
      margin-bottom: 20px;
    }
    .form-block label { font-weight: 600; font-size: 0.9rem; color: #334155; }
    .form-block input,
    .form-block select,
    .form-block textarea {
      padding: 10px 14px;
      border: 1px solid #e2e8f0;
      border-radius: 6px;
      font-size: 0.95rem;
      font-family: inherit;
    }

    /* Botones alineados a la derecha */
    .form-actions {
      display: flex;
      gap: 12px;
      justify-content: flex-end;
      margin-top: 32px;
    }
    .btn-primary {
      padding: 12px 28px;
      background: #2563eb; color: #fff;
      border: none; border-radius: 6px;
      font-weight: 600; cursor: pointer;
    }
    .btn-primary:hover { background: #1d4ed8; }
    .btn-secondary {
      padding: 12px 28px;
      background: #e2e8f0; color: #475569;
      border: none; border-radius: 6px;
      font-weight: 600; cursor: pointer;
    }
    .btn-secondary:hover { background: #cbd5e1; }

    /* RESPONSIVE: en móvil, label encima del input */
    @media (max-width: 600px) {
      .form-container { padding: 24px 16px; }
      .form-row { flex-direction: column; align-items: stretch; gap: 6px; }
      .form-row label { flex: none; }
      .form-actions { flex-direction: column; }
      .form-actions button { width: 100%; }
    }
    ```

### Ejemplo 7: Sticky Footer + Holy Grail simplificado

=== "HTML"

    ``` html
    <!DOCTYPE html>
    <html lang="es">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Sticky Footer + Layout Flexbox | Ejemplo Didáctico</title>
      <link rel="stylesheet" href="./styles.css">
    </head>
    <body>
      <div class="page">
        <header class="page__header">Sticky Footer + Holy Grail con Flexbox</header>

        <main class="page__main">
          <h1>Layouts Clásicos con Flexbox</h1>

          <h2>1. Sticky Footer</h2>
          <p>
            El body usa <code>display: flex; flex-direction: column; min-height: 100vh;</code>.
            El <code>&lt;main&gt;</code> tiene <code>flex: 1;</code>, lo que lo hace crecer para
            ocupar todo el espacio entre el header y el footer. Si el contenido es corto, el footer
            queda al fondo de la ventana. Si el contenido es largo, el footer se desplaza
            naturalmente tras el contenido.
          </p>
          <pre>.page { display: flex; flex-direction: column; min-height: 100vh; }
    .page__main { flex: 1; }</pre>

          <h2>2. Holy Grail (3 columnas)</h2>
          <p>
            Layout clásico con barra lateral izquierda, contenido central y barra lateral derecha.
            Las barras laterales tienen ancho fijo (<code>flex: 0 0 200px</code>), y el contenido
            central ocupa el resto (<code>flex: 1</code>).
          </p>
          <div class="holy-grail">
            <aside class="holy-grail__left">
              <strong>Sidebar Izquierda</strong><br>
              Navegación secundaria, filtros, categorías...
              <div class="sticky-box" style="margin-top:16px;">
                Contenido sticky al hacer scroll
              </div>
            </aside>
            <section class="holy-grail__center">
              <strong>Contenido Principal</strong>
              <p>Esta es el área central del layout Holy Grail. Ocupa todo el espacio disponible entre las dos barras laterales. En pantallas pequeñas (menos de 768px), el layout cambia a dirección columna y las barras laterales se apilan encima y debajo del contenido.</p>
            </section>
            <aside class="holy-grail__right">
              <strong>Sidebar Derecha</strong><br>
              Contenido relacionado, publicidad, widgets...
            </aside>
          </div>
        </main>

        <footer class="page__footer">
          &copy; 2025 - Ejemplo didáctico de Flexbox. El footer siempre está al fondo gracias a <code>flex: 1</code> en el main.
        </footer>
      </div>
    </body>
    </html>
    ```

=== "CSS"

    ``` css
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      color: #1e293b; line-height: 1.6;
    }

    /* =============================================
       STICKY FOOTER con Flexbox
       body como columna flex con min-height: 100vh
       main con flex: 1 crece para ocupar el espacio
       El footer queda siempre al fondo.
       ============================================= */
    .page {
      display: flex;
      flex-direction: column;
      min-height: 100vh;
    }
    .page__header {
      background: #0f172a; color: #fff;
      padding: 16px 24px; font-weight: 700; font-size: 1.2rem;
    }
    .page__main {
      flex: 1; /* OCUPA TODO EL ESPACIO DISPONIBLE, empujando el footer abajo */
      max-width: 1000px; margin: 0 auto; width: 100%;
      padding: 40px 24px;
    }
    .page__footer {
      background: #0f172a; color: #94a3b8;
      text-align: center; padding: 24px; font-size: 0.9rem;
    }

    h1 { color: #2563eb; margin-bottom: 16px; }
    p { margin-bottom: 16px; color: #475569; }

    /* =============================================
       HOLY GRAIL simplificado con Flexbox
       Tres columnas: aside izquierda, contenido principal, aside derecha
       ============================================= */
    .holy-grail {
      display: flex;
      gap: 24px;
      margin-top: 32px;
    }
    .holy-grail__left,
    .holy-grail__right {
      flex: 0 0 200px;
      background: #f1f5f9;
      padding: 20px;
      border-radius: 8px;
      font-size: 0.9rem;
      color: #64748b;
    }
    .holy-grail__center {
      flex: 1; /* Ocupa el espacio restante */
      background: #fff;
      padding: 20px;
      border-radius: 8px;
      border: 1px solid #e2e8f0;
    }

    /* Sticky dentro del layout */
    .sticky-box {
      position: sticky;
      top: 16px;
      background: #eff6ff;
      padding: 16px;
      border-radius: 6px;
      border: 1px solid #bfdbfe;
    }

    /* Responsive */
    @media (max-width: 768px) {
      .holy-grail { flex-direction: column; }
      .holy-grail__left,
      .holy-grail__right { flex: none; }
    }

    pre {
      background: #1e293b; color: #e2e8f0; padding: 12px;
      border-radius: 6px; font-size: 0.82rem; overflow-x: auto;
      margin: 8px 0;
    }
    ```

### Ejemplo 8: Media Object y centrado con auto margins

=== "HTML"

    ``` html
    <!DOCTYPE html>
    <html lang="es">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Auto Margins y Media Object | Ejemplo Didáctico</title>
      <link rel="stylesheet" href="./styles.css">
    </head>
    <body>
      <div class="contenedor">
        <h1>Media Object y Auto Margins</h1>

        <h2>1. Media Object (imagen + texto)</h2>
        <div class="media">
          <div class="media__img">JD</div>
          <div class="media__body">
            <div class="media__title">Juan Domínguez</div>
            <div class="media__text">Ha comentado en tu publicación: "Excelente artículo sobre Flexbox. Los ejemplos son muy claros y me han ayudado a entender flex-grow vs flex-basis."</div>
          </div>
        </div>
        <div class="media">
          <div class="media__img" style="background:linear-gradient(135deg,#f093fb,#f5576c);">ML</div>
          <div class="media__body">
            <div class="media__title">María López</div>
            <div class="media__text">Ha compartido tu proyecto en LinkedIn. ¡Felicidades!</div>
          </div>
        </div>
        <pre>.media { display: flex; gap: 16px; align-items: flex-start; }
    .media__img { flex-shrink: 0; }
    .media__body { flex: 1; }</pre>

        <h2>2. Auto Margins (margin-left: auto)</h2>
        <p>El grupo de botones de la derecha se empuja automáticamente.</p>
        <div class="toolbar">
          <span class="toolbar__item">Archivo</span>
          <span class="toolbar__item">Editar</span>
          <span class="toolbar__item">Ver</span>
          <!-- margin-left: auto empuja todo lo que sigue a la derecha -->
          <span class="toolbar__item toolbar__item--push-right">Ayuda</span>
          <span class="toolbar__item toolbar__item--danger">Salir</span>
        </div>
        <pre>.toolbar__item--push-right { margin-left: auto; }</pre>

        <h2>3. Card con footer al fondo (margin-top: auto)</h2>
        <div class="card-flex">
          <div class="card-flex__body">
            <strong>Título de la Card</strong>
            <p style="margin-top:8px;color:#64748b;">El contenido de esta card puede ser de cualquier longitud. El footer siempre queda al fondo gracias a margin-top: auto en combinación con el flex column de la card.</p>
          </div>
          <div class="card-flex__footer">
            <span>3 comentarios</span>
            <span>Hace 2 horas</span>
          </div>
        </div>
        <pre>.card-flex { display: flex; flex-direction: column; }
    .card-flex__footer { margin-top: auto; }</pre>
      </div>
    </body>
    </html>
    ```

=== "CSS"

    ``` css
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: 'Segoe UI', system-ui, sans-serif; background: #f8fafc; padding: 40px; color: #1e293b; }
    .contenedor { max-width: 800px; margin: 0 auto; }
    h1 { color: #2563eb; margin-bottom: 32px; }
    h2 { margin: 32px 0 16px; color: #334155; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px; }

    /* ==========================================
       MEDIA OBJECT
       Patrón clásico: imagen a la izquierda,
       contenido a la derecha. Flexbox lo resuelve
       de forma nativa y elegante.
       ========================================== */
    .media {
      display: flex;
      gap: 16px;
      background: #fff;
      padding: 20px;
      border-radius: 8px;
      margin-bottom: 12px;
      box-shadow: 0 1px 3px rgba(0,0,0,0.06);
      align-items: flex-start;
    }
    .media__img {
      flex-shrink: 0; /* La imagen no se encoge */
      width: 64px;
      height: 64px;
      border-radius: 50%;
      background: linear-gradient(135deg, #667eea, #764ba2);
      display: flex; align-items: center; justify-content: center;
      color: #fff; font-weight: 700; font-size: 1.2rem;
    }
    .media__body { flex: 1; }
    .media__title { font-weight: 700; margin-bottom: 4px; }
    .media__text { color: #64748b; font-size: 0.92rem; }

    /* ==========================================
       AUTO MARGINS: Distribución avanzada
       margin-left: auto empuja elementos a la derecha
       margin-right: auto empuja a la izquierda
       margin: auto centra en ambas direcciones
       ========================================== */

    /* Barra de herramientas con separación automática */
    .toolbar {
      display: flex;
      align-items: center;
      gap: 8px;
      background: #fff;
      padding: 16px;
      border-radius: 8px;
      margin-bottom: 12px;
      box-shadow: 0 1px 3px rgba(0,0,0,0.06);
    }
    .toolbar__item {
      padding: 8px 16px;
      background: #f1f5f9;
      border-radius: 6px;
      font-size: 0.9rem;
      font-weight: 500;
    }
    .toolbar__item--push-right { margin-left: auto; }
    .toolbar__item--danger { background: #fef2f2; color: #dc2626; }

    /* Footer de card alineado con margin-top: auto */
    .card-flex {
      display: flex;
      flex-direction: column;
      background: #fff;
      border-radius: 8px;
      box-shadow: 0 1px 3px rgba(0,0,0,0.06);
      min-height: 200px;
      padding: 20px;
    }
    .card-flex__body { flex: 1; }
    .card-flex__footer {
      margin-top: auto;
      padding-top: 12px;
      border-top: 1px solid #e2e8f0;
      display: flex;
      justify-content: space-between;
      font-size: 0.9rem;
    }

    pre { background: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 6px; overflow-x: auto; font-size: 0.82rem; margin: 8px 0; }
    ```

### Ejemplo 9: Patrones prácticos - Centrado, igual altura, lista horizontal

=== "HTML"

    ``` html
    <!DOCTYPE html>
    <html lang="es">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Patrones Flexbox | Ejemplo Didáctico</title>
      <link rel="stylesheet" href="./styles.css">
    </head>
    <body>
      <div class="contenedor">
        <h1>Patrones Prácticos con Flexbox</h1>

        <h2>1. Centrado Perfecto</h2>
        <div class="centro-demo">
          <div class="contenido">Contenido centrado en ambas direcciones</div>
        </div>
        <pre>.padre { display: flex; justify-content: center; align-items: center; }</pre>

        <h2>2. Igual Altura de Columnas</h2>
        <div class="columnas-iguales">
          <div class="col">
            <h3>Columna 1</h3>
            <p>Contenido breve.</p>
          </div>
          <div class="col">
            <h3>Columna 2</h3>
            <p>Mucho más contenido aquí. Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quos. Este texto hace que la columna sea más alta.</p>
          </div>
          <div class="col">
            <h3>Columna 3</h3>
            <p>Contenido medio. Todas las columnas tienen la misma altura automáticamente.</p>
          </div>
        </div>
        <pre>.columnas { display: flex; gap: 16px; }
    .col { flex: 1; } /* stretch alinea alturas automáticamente */</pre>

        <h2>3. Lista Horizontal Responsive</h2>
        <ul class="lista-horizontal">
          <li>HTML5</li><li>CSS3</li><li>JavaScript</li>
          <li>React</li><li>Node.js</li><li>Python</li>
          <li>Docker</li><li>Git</li>
        </ul>
        <pre>.lista { display: flex; gap: 12px; flex-wrap: wrap; }</pre>

        <h2>4. Header con Logo Izquierda + Menú Derecha</h2>
        <div class="header-demo">
          <div class="logo">Mi Sitio Web</div>
          <div class="links">
            <a href="#">Inicio</a><a href="#">Acerca de</a>
            <a href="#">Servicios</a><a href="#">Contacto</a>
          </div>
        </div>
        <pre>.header { display: flex; justify-content: space-between; align-items: center; }</pre>
      </div>
    </body>
    </html>
    ```

=== "CSS"

    ``` css
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: 'Segoe UI', system-ui, sans-serif; background: #f1f5f9; padding: 40px 20px; color: #1e293b; }
    .contenedor { max-width: 900px; margin: 0 auto; }
    h1 { color: #2563eb; margin-bottom: 32px; text-align: center; }
    h2 { margin: 32px 0 16px; color: #334155; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px; }
    pre { background: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 6px; font-size: 0.82rem; margin: 8px 0; overflow-x: auto; }

    /* 1. CENTRADO PERFECTO */
    .centro-demo {
      display: flex; justify-content: center; align-items: center;
      height: 200px; background: #fff; border-radius: 8px;
      box-shadow: 0 1px 3px rgba(0,0,0,0.06); margin-bottom: 12px;
    }
    .centro-demo .contenido {
      background: #2563eb; color: #fff; padding: 24px 40px;
      border-radius: 8px; font-weight: 700; text-align: center;
    }

    /* 2. IGUAL ALTURA DE COLUMNAS (automático con stretch) */
    .columnas-iguales {
      display: flex; gap: 16px; margin-bottom: 12px;
    }
    .col {
      flex: 1; background: #fff; padding: 24px; border-radius: 8px;
      box-shadow: 0 1px 3px rgba(0,0,0,0.06);
    }
    .col h3 { color: #2563eb; margin-bottom: 8px; }

    /* 3. LISTA HORIZONTAL RESPONSIVE */
    .lista-horizontal {
      display: flex; gap: 12px; list-style: none;
      flex-wrap: wrap; margin-bottom: 12px;
    }
    .lista-horizontal li {
      padding: 8px 16px; background: #fff; border-radius: 20px;
      box-shadow: 0 1px 2px rgba(0,0,0,0.06); font-size: 0.9rem;
      font-weight: 500;
    }

    /* 4. ELEMENTOS DISTRIBUIDOS CON LOGO A IZQ + MENÚ DERECHA */
    .header-demo {
      display: flex; justify-content: space-between; align-items: center;
      background: #0f172a; padding: 16px 24px; border-radius: 8px;
      margin-bottom: 12px; flex-wrap: wrap; gap: 12px;
    }
    .header-demo .logo { color: #fff; font-weight: 700; font-size: 1.2rem; }
    .header-demo .links { display: flex; gap: 16px; flex-wrap: wrap; }
    .header-demo .links a { color: #94a3b8; text-decoration: none; font-size: 0.9rem; }
    .header-demo .links a:hover { color: #fff; }

    @media (max-width: 600px) {
      .columnas-iguales { flex-direction: column; }
    }
    ```

### Ejemplo 10: Comparación flex-basis vs width + Galería con flex-wrap

=== "HTML"

    ``` html
    <!DOCTYPE html>
    <html lang="es">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Flex-basis vs Width | Ejemplo Didáctico</title>
      <link rel="stylesheet" href="./styles.css">
    </head>
    <body>
      <div class="contenedor">
        <h1>Flex-basis vs Width</h1>

        <h2>1. flex: 0 1 200px (basis: 200px)</h2>
        <p>Ítems parten de 200px. Pueden encogerse si falta espacio. <strong>flex-basis: 200px tiene prioridad sobre width.</strong></p>
        <div class="flex-demo">
          <div class="item" style="flex:0 1 200px; width:300px;">base:200px<br>width:300px ign</div>
          <div class="item" style="flex:0 1 200px;">base:200px</div>
          <div class="item" style="flex:0 1 200px;">base:200px</div>
        </div>
        <pre>.item { flex: 0 1 200px; width: 300px; }
    /* flex-basis:200px gana sobre width:300px */</pre>

        <h2>2. flex: 1 (equivale a flex: 1 1 0%)</h2>
        <p><strong>flex-basis: 0%</strong>: todos parten de 0 y se reparten el espacio equitativamente. El contenido no influye.</p>
        <div class="flex-demo">
          <div class="item" style="flex:1;">Corto</div>
          <div class="item" style="flex:1;">Medio</div>
          <div class="item" style="flex:1;">Texto mucho más largo que los demás</div>
        </div>
        <pre>.item { flex: 1; } /* flex: 1 1 0% */</pre>

        <h2>3. flex: auto (equivale a flex: 1 1 auto)</h2>
        <p><strong>flex-basis: auto</strong>: cada ítem parte de su tamaño natural (determinado por contenido o width). El espacio extra se reparte proporcionalmente DESPUÉS.</p>
        <div class="flex-demo">
          <div class="item" style="flex:auto;">Corto</div>
          <div class="item" style="flex:auto;">Medio</div>
          <div class="item" style="flex:auto;">Texto mucho más largo que los demás y ocupa más</div>
        </div>
        <pre>.item { flex: auto; } /* flex: 1 1 auto */</pre>

        <h2>4. Galería Responsive con flex-wrap</h2>
        <p>Cada item: <code>flex: 1 1 200px</code>. Mínimo 200px, crecen para llenar, envuelven con wrap.</p>
        <div class="galeria">
          <div class="galeria-item"><img src="" alt=""><div class="info">Proyecto Alpha - Web App</div></div>
          <div class="galeria-item"><img src="" alt=""><div class="info">Proyecto Beta - Mobile</div></div>
          <div class="galeria-item"><img src="" alt=""><div class="info">Dashboard Analytics</div></div>
          <div class="galeria-item"><img src="" alt=""><div class="info">E-commerce Platform</div></div>
          <div class="galeria-item"><img src="" alt=""><div class="info">Portfolio Personal</div></div>
        </div>
        <pre>.galeria { display: flex; flex-wrap: wrap; gap: 16px; }
    .galeria-item { flex: 1 1 200px; }</pre>
      </div>
    </body>
    </html>
    ```

=== "CSS"

    ``` css
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: 'Segoe UI', system-ui, sans-serif; background: #f8fafc; padding: 40px; color: #1e293b; }
    .contenedor { max-width: 900px; margin: 0 auto; }
    h1 { color: #2563eb; margin-bottom: 32px; }
    h2 { margin: 32px 0 16px; color: #334155; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px; }
    .flex-demo { background: #e2e8f0; border-radius: 8px; padding: 16px; margin-bottom: 12px; display: flex; gap: 8px; }
    .item {
      background: #2563eb; color: #fff; padding: 16px; border-radius: 6px;
      font-weight: 600; text-align: center; font-size: 0.85rem;
    }
    pre { background: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 6px; overflow-x: auto; font-size: 0.82rem; margin: 8px 0; }

    /* GALERÍA */
    .galeria {
      display: flex; flex-wrap: wrap; gap: 16px;
    }
    .galeria-item {
      flex: 1 1 200px;
      background: #fff; border-radius: 8px; overflow: hidden;
      box-shadow: 0 1px 4px rgba(0,0,0,0.06);
      transition: transform 0.2s;
    }
    .galeria-item:hover { transform: scale(1.03); }
    .galeria-item img {
      width: 100%; height: 150px; object-fit: cover; display: block;
      background: linear-gradient(135deg, #667eea, #764ba2);
    }
    .galeria-item .info { padding: 16px; font-size: 0.9rem; }
    ```

## Casos reales

### Caso Real 1: GitHub - Navegación y layout con Flexbox

!!! example "Caso real: GitHub"
    GitHub utiliza Flexbox extensivamente en toda su interfaz. La barra de navegación superior es un contenedor flex con `justify-content: space-between` para separar el logo y la búsqueda (izquierda) de los iconos de notificaciones y perfil (derecha). La *sidebar* de repositorios usa `display: flex; flex-direction: column;` para alinear los elementos de navegación verticalmente. El área principal de código emplea Flexbox para la cabecera del archivo (nombre, botones de acción) y para alinear elementos en las barras de herramientas. En la vista de *Issues* y *Pull Requests*, cada ítem de la lista es un contenedor flex que alinea el *checkbox*, título, etiquetas y metadatos en una fila. GitHub demuestra cómo Flexbox es la herramienta ideal para componentes de interfaz y barras de herramientas, mientras que CSS Grid se reserva para el *layout* global de algunas páginas.

### Caso Real 2: Twitter/X - Timeline y composición de tweets

!!! example "Caso real: Twitter/X"
    Twitter/X utiliza Flexbox como núcleo de su interfaz. La *timeline* está construida con un *layout* flex de dos columnas (*sidebar* izquierda, contenido central, tendencias derecha). Cada tweet individual es un contenedor flex horizontal (avatar + contenido) que sigue el patrón *media object* estudiado. El avatar tiene `flex-shrink: 0` para mantener su tamaño, y el cuerpo del tweet tiene `flex: 1` para ocupar el espacio restante. Las acciones del tweet (comentar, retweet, *like*, compartir) están en un contenedor flex con `justify-content: space-between`. La barra de navegación inferior en móvil usa `justify-content: space-around`. Twitter es un ejemplo perfecto de Flexbox usado para componentes de interfaz de usuario repetitivos y alineados.

### Caso Real 3: Stripe - Landing page y componentes de pago

!!! example "Caso real: Stripe"
    Stripe utiliza Flexbox para construir *layouts* complejos en su *landing page* y documentación. Las secciones de la *landing page* son contenedores flex que alternan dirección de fila/columna para imagen + texto. Los componentes de pago (Stripe Elements) usan Flexbox para alinear campos de formulario (número de tarjeta, fecha, CVC) en una sola fila *responsive*. La documentación de Stripe emplea un *layout* de dos columnas con Flexbox: navegación lateral y contenido principal. En móvil, la dirección cambia a columna. Los botones y CTAs usan Flexbox para centrar iconos y texto. Stripe demuestra el uso de Flexbox tanto para macro-*layouts* como para micro-componentes de interfaz.

## Actividades guiadas

### Actividad Guiada 1: Construir una navbar completa paso a paso

**RA:** RA2. **Objetivo:** Construir una barra de navegación profesional completamente funcional con Flexbox, incluyendo logo, menú, búsqueda, iconos y versión responsive con hamburguesa CSS puro.

**Enunciado:** Construye una navbar para un sitio web corporativo que incluya: (1) logo a la izquierda, (2) menú de navegación central con 5 enlaces, (3) campo de búsqueda y 2 iconos a la derecha, (4) menú hamburguesa funcional en móvil (<768px) usando solo CSS (checkbox + label + :checked), (5) header sticky, (6) transiciones suaves en el despliegue del menú, (7) indicador de página activa en el enlace correspondiente. Todo el HTML debe ser semántico y accesible.

**Criterios de evaluación:**

- Uso correcto de Flexbox para alinear todos los elementos en la navbar (logo, menú, búsqueda, iconos) (3 puntos).
- Menú hamburguesa funcional con CSS puro (checkbox + label + :checked + ~) (3 puntos).
- Diseño responsive con al menos 2 breakpoints (2 puntos).
- Header sticky funcional (1 punto).
- Transiciones y estética profesional (1 punto).

**Rúbrica:**

| Criterio | Insuficiente (0-4) | Satisfactorio (5-7) | Excelente (8-10) |
|----------|-------------------|---------------------|------------------|
| Flexbox | Elementos desalineados o no usa Flexbox | Flexbox usado pero con errores de alineación | Flexbox perfecto: space-between, align-items, gap correctos |
| Hamburguesa CSS | No funciona o usa JS | Funciona pero con bugs | Checkbox+label+:checked funcional y accesible |
| Responsive | Sin responsive | Un solo breakpoint | 2+ breakpoints, adaptación fluida |
| Estética | Diseño básico sin estilos | Estilos correctos pero sin detalles | Diseño profesional con transiciones y atención al detalle |

### Actividad Guiada 2: Galería de productos con cards de altura variable

**RA:** RA2. **Objetivo:** Crear una galería de productos con Flexbox donde las cards tengan altura uniforme y el precio siempre esté alineado al fondo, independientemente de la longitud del contenido.

**Enunciado:** Crea una galería de 8 productos tecnológicos con: (1) grid responsive con `flex-wrap: wrap`, (2) cada card debe ser un contenedor flex column para alinear el footer al fondo, (3) imágenes con `object-fit: cover` de altura fija, (4) footer con precio y botón "Comprar" siempre alineado al fondo, (5) efectos hover (elevación y sombra) con transiciones, (6) 2-3 cards por fila en desktop, 1 en móvil. Usa `flex: 1 1 280px` para las cards.

**Criterios de evaluación:**

- Grid responsive con flex-wrap correcto (2 puntos).
- Cards como flex column con footer alineado al fondo (3 puntos).
- Efectos hover con transiciones (1 punto).
- Imágenes con object-fit (1 punto).
- Diseño responsive (2 puntos).
- Código limpio y comentado (1 punto).

### Actividad Guiada 3: Dashboard con sidebar colapsable

**RA:** RA2. **Objetivo:** Construir un dashboard administrativo con sidebar flexible y colapsable usando CSS puro y Flexbox.

**Enunciado:** Crea un dashboard que incluya: (1) sidebar izquierda con navegación (250px de ancho), (2) header superior con título y avatar, (3) área de contenido principal con scroll, (4) 4 cards de estadísticas usando flex-wrap, (5) sidebar colapsable a 60px con CSS puro (checkbox), (6) ocultación de textos al colapsar. El layout completo debe usar Flexbox.

**Criterios de evaluación:**

- Layout principal con Flexbox correcto (sidebar + contenido) (3 puntos).
- Sidebar colapsable con CSS puro (checkbox) (3 puntos).
- Cards de estadísticas con flex-wrap (2 puntos).
- Diseño responsive (2 puntos).

### Actividad Guiada 4: Formulario de checkout con Flexbox

**RA:** RA2. **Objetivo:** Construir un formulario de checkout de comercio electrónico donde etiquetas e inputs estén perfectamente alineados usando Flexbox, con diseño responsive.

**Enunciado:** Crea un formulario de pago que incluya: campos personales (nombre, email, teléfono), dirección de envío, y datos de tarjeta. Usa Flexbox para: (1) alinear label (130px) e input (flex:1) en cada fila en desktop, (2) cambiar a dirección column en móvil, (3) agrupar campos relacionados horizontalmente (ej: ciudad + CP + país en una fila), (4) alinear botones a la derecha con gap, (5) campos con anchos proporcionales usando flex-grow.

**Criterios de evaluación:**

- Alineación label-input con Flexbox (3 puntos).
- Agrupación de campos en filas horizontales (2 puntos).
- Diseño responsive (column en móvil) (2 puntos).
- Botones alineados correctamente (1 punto).
- Validación HTML5 implementada (2 puntos).

### Actividad Guiada 5: Página de inicio completa con Flexbox

**RA:** RA2. **Objetivo:** Construir una landing page completa usando exclusivamente Flexbox para todos los layouts (sin Grid), demostrando el dominio total del modelo unidimensional.

**Enunciado:** Diseña una landing page para una startup que contenga: (1) header con navbar (sticky), (2) sección hero centrada vertical/horizontalmente, (3) sección de 3 características en fila (flex-wrap responsive), (4) sección de precios con 3 planes alineados, (5) sección de testimonios con media objects, (6) footer con múltiples columnas usando flex-wrap. Todo con Flexbox, sin usar CSS Grid.

**Criterios de evaluación:**

- Todos los layouts implementados correctamente con Flexbox (4 puntos).
- Diseño responsive completo (2 puntos).
- Media objects en testimonios (2 puntos).
- Footer multicolumna con flex-wrap (1 punto).
- Estética profesional y cohesión visual (1 punto).

## Actividades propuestas

### Actividad Propuesta 1: Replica de la interfaz de Gmail con Flexbox

**RA:** RA2. **Objetivo:** Reproducir el layout principal de Gmail (bandeja de entrada) usando exclusivamente Flexbox, demostrando comprensión de layouts complejos unidimensionales anidados.

**Enunciado:** Reproduce la interfaz de Gmail con: sidebar izquierda (carpetas/etiquetas), lista de correos central (cada email es un media object con checkbox, remitente, asunto, fecha), y panel de vista previa. Usa Flexbox para todos los alineamientos internos. Implementa diseño responsive.

**Criterios:** Layout principal correcto (3 puntos), lista de correos como media objects (3 puntos), sidebar con scroll (2 puntos), responsive (2 puntos).

### Actividad Propuesta 2: Timeline de red social con Flexbox

**RA:** RA2. **Objetivo:** Crear una timeline de red social al estilo Twitter/LinkedIn, donde cada post sea un media object construido con Flexbox.

**Enunciado:** Crea una timeline con al menos 6 posts. Cada post debe usar el patrón media object (avatar + contenido). El contenido debe incluir: nombre, handle, texto del post (longitud variable), imagen opcional, y barra de acciones (like, comentar, compartir) con `justify-content: space-between`. Implementa posts anidados (comentarios) con indentación.

**Criterios:** Media objects correctos (4 puntos), barra de acciones alineada (2 puntos), posts anidados (2 puntos), diseño responsive (2 puntos).

### Actividad Propuesta 3: Comparativa visual Flexbox vs Grid

**RA:** RA2. **Objetivo:** Crear una página didáctica que muestre visualmente la diferencia entre Flexbox y CSS Grid, implementando el mismo layout con ambas técnicas y explicando cuándo usar cada una.

**Enunciado:** Crea una página con dos secciones lado a lado que muestren el mismo layout (una galería de 6 elementos) implementado con Flexbox en la izquierda y con Grid en la derecha. Añade controles para modificar propiedades (gap, dirección, wrap) y ver cómo reacciona cada modelo. Incluye una sección de conclusiones sobre cuándo usar cada técnica.

**Criterios:** Implementaciones correctas en ambos modelos (4 puntos), controles interactivos (2 puntos), explicaciones claras (2 puntos), diseño didáctico (2 puntos).

### Actividad Propuesta 4: Calculadora de Flexbox interactiva

**RA:** RA2. **Objetivo:** Crear una herramienta interactiva que permita modificar propiedades Flexbox y ver los cambios en tiempo real.

**Enunciado:** Construye una página con: (1) un contenedor flex con 5 ítems de demostración, (2) controles deslizantes (range inputs) para modificar `flex-grow`, `flex-shrink`, `flex-basis` de cada ítem individualmente, (3) selectores para `flex-direction`, `justify-content`, `align-items`, `flex-wrap`, `gap`, (4) visualización en tiempo real de los cambios, (5) display del código CSS generado. Usa JavaScript para actualizar los estilos dinámicamente.

**Criterios:** Controles range funcionales (3 puntos), selectores de propiedades (3 puntos), visualización en tiempo real (2 puntos), display del CSS generado (2 puntos).

### Actividad Propuesta 5: Kit de componentes UI con Flexbox

**RA:** RA2. **Objetivo:** Crear una librería de componentes de interfaz reutilizables construidos con Flexbox.

**Enunciado:** Desarrolla un kit que incluya: (1) botones con iconos alineados, (2) cards de producto, (3) listas de características con icono + texto, (4) barras de progreso con etiquetas, (5) tabs/pestañas de navegación, (6) breadcrumbs, (7) badges y etiquetas, (8) avatares con estado online. Todos los componentes deben usar Flexbox para su alineación interna y ser responsive.

**Criterios:** 8 componentes funcionales (4 puntos), alineación interna con Flexbox (3 puntos), responsive (2 puntos), documentación (1 punto).

## Actividades de ampliación

### Actividad de Ampliación 1: Clon responsive de la interfaz de Spotify Web Player

**RA:** RA1, RA2. **Objetivo:** Reproducir la interfaz del reproductor web de Spotify usando exclusivamente Flexbox para todos los layouts.

**Enunciado:** Clona la interfaz de Spotify con: (1) sidebar izquierda con playlists (scrollable), (2) área principal con grid de álbumes/playlists destacadas, (3) barra de reproducción inferior fija con controles de playback, progreso y volumen, (4) header superior con navegación y perfil. Cada sección debe usar Flexbox para sus alineamientos. Implementa 3 breakpoints (desktop, tablet, mobile). En mobile, la barra de reproducción se simplifica y la sidebar se oculta.

**Criterios:**

- Layout principal con Flexbox correcto en todas las secciones (3 puntos).
- Barra de reproducción con controles perfectamente alineados (3 puntos).
- Diseño responsive con 3 breakpoints funcionales (3 puntos).
- Fidelidad visual al diseño original (1 punto).

**Rúbrica:**

| Criterio | Insuficiente (0-4) | Satisfactorio (5-7) | Excelente (8-10) |
|----------|-------------------|---------------------|------------------|
| Layout Flexbox | No usa Flexbox o lo usa incorrectamente | Flexbox usado en la mayoría de secciones | Flexbox aplicado correctamente en TODAS las secciones |
| Reproductor | Controles desalineados | Controles alineados pero con fallos en responsive | Controles perfectamente alineados y funcionales en todos los breakpoints |
| Responsive | Solo desktop | Desktop + tablet o mobile | 3 breakpoints totalmente funcionales |
| Fidelidad visual | Parecido lejano | Similar pero con diferencias notables | Muy cercano al original en estructura y estilos |

### Actividad de Ampliación 2: Juego de Tres en Raya (Tic-Tac-Toe) con Flexbox

**RA:** RA2 y RA4. **Objetivo:** Crear un juego completo de tres en raya usando HTML, CSS (Flexbox para el tablero) y JavaScript para la lógica.

**Enunciado:** Desarrolla un juego de tres en raya para dos jugadores con: (1) tablero 3x3 construido con Flexbox (flex-wrap en el contenedor, cada celda con flex: 1 1 33.33%), (2) celdas centradas con Flexbox, (3) animaciones al colocar fichas, (4) detección de victoria con línea ganadora resaltada, (5) marcador de puntuación alineado con Flexbox, (6) botón de reinicio, (7) diseño responsive que funcione en móvil. Usa Flexbox para TODOS los alineamientos.

**Criterios:**

- Tablero 3x3 con Flexbox (3 puntos).
- Celdas con contenido centrado usando Flexbox (2 puntos).
- Lógica del juego funcional en JS (3 puntos).
- Animaciones y diseño visual (1 punto).
- Diseño responsive (1 punto).

### Actividad de Ampliación 3: Sistema de diseño de componentes con Flexbox y documentación

**RA:** RA1, RA2. **Objetivo:** Crear un design system completo documentado, donde todos los componentes usen Flexbox para su alineación interna.

**Enunciado:** Desarrolla un design system documentado que incluya: (1) tokens de diseño como variables CSS, (2) al menos 12 componentes diferentes (botones, cards, inputs, modales, tabs, badges, alerts, tooltips, dropdowns, avatares, breadcrumbs, paginación), (3) cada componente debe usar Flexbox para su alineación interna, (4) página de documentación que muestre cada componente con su variante y código, (5) modo claro/oscuro mediante variables CSS, (6) diseño responsive de la propia página de documentación.

**Criterios:**

- 12+ componentes funcionales (4 puntos).
- Flexbox correcto en la alineación interna de cada componente (3 puntos).
- Documentación clara y completa (2 puntos).
- Modo claro/oscuro funcional (1 punto).

**Rúbrica:**

| Criterio | Insuficiente (0-4) | Satisfactorio (5-7) | Excelente (8-10) |
|----------|-------------------|---------------------|------------------|
| Componentes | Menos de 6 componentes | 6-11 componentes funcionales | 12+ componentes bien diseñados |
| Uso de Flexbox | Flexbox ausente en varios componentes | Flexbox presente pero no en todos | Flexbox correcto en la alineación interna de TODOS los componentes |
| Documentación | Sin documentación | Documentación parcial o incompleta | Documentación completa con ejemplos y código de cada componente |
| Temas | Sin modo oscuro | Modo oscuro implementado con errores | Modo claro/oscuro completo y funcional |

## Buenas prácticas

1. **Usa `display: flex` en el contenedor padre, no en los hijos.** Flexbox se activa en el contenedor; los hijos se convierten automáticamente en ítems flex.

2. **Usa el shorthand `flex` en lugar de `flex-grow`, `flex-shrink` y `flex-basis` por separado.** Es más conciso y menos propenso a errores. Recuerda: `flex: 1` = `flex: 1 1 0%`, `flex: auto` = `flex: 1 1 auto`, `flex: none` = `flex: 0 0 auto`.

3. **Usa `gap` en lugar de `margin` para separar ítems flex.** `gap` solo aplica entre ítems, no en los extremos. Es más limpio y predecible.

4. **Prefiere `flex-basis` sobre `width`/`height` en ítems flex.** `flex-basis` tiene prioridad y define el tamaño en el eje principal correctamente, independientemente de la dirección del flex.

5. **Usa `margin: auto` para distribución avanzada.** `margin-left: auto` empuja un ítem a la derecha. `margin-top: auto` empuja al fondo. Es más semántico y mantenible que usar elementos espaciadores.

6. **Aplica `min-width: 0` en ítems flex que contengan texto largo.** Por defecto, un ítem flex no se encoge por debajo del tamaño de su contenido. `min-width: 0` permite que el texto se trunque con `overflow: hidden` y `text-overflow: ellipsis`.

7. **No uses `order` para cambiar el orden semántico del contenido.** `order` solo afecta a la presentación visual. El orden del DOM determina el orden de tabulación y lectura para lectores de pantalla. Si necesitas cambiar el orden, cambia el HTML.

8. **Combina Flexbox con CSS Grid, no los enfrentes.** Usa Grid para el layout macro de la página (filas y columnas) y Flexbox para los componentes dentro de cada celda (alineación de contenido, barras de herramientas, listas).

9. **Diseña mobile-first con `flex-wrap: wrap`.** Define el comportamiento base para móvil (normalmente columna o wrap) y usa media queries `min-width` para layouts más complejos en desktop.

10. **No abuses de `flex-wrap: wrap` para crear grids.** Si necesitas un grid bidimensional con control preciso de filas y columnas, usa CSS Grid. Flexbox con wrap es adecuado para colecciones de items de tamaño similar pero no para layouts de cuadrícula estrictos.

## Errores frecuentes

Los errores siguientes aparecen una y otra vez en los primeros proyectos con Flexbox:

!!! warning "Errores frecuentes de Flexbox"
    1. **Olvidar que Flexbox es UNIDIMENSIONAL.** Intentar crear *layouts* de filas y columnas simultáneas con Flexbox (en lugar de Grid) resulta en código innecesariamente complejo.

    2. **Usar `flex: 1` cuando se necesita `flex: auto`.** Con `flex: 1` (`flex-basis: 0%`), todos los ítems parten de cero y obtienen el mismo tamaño. Con `flex: auto`, respetan el tamaño de su contenido y luego reparten el espacio extra, lo que puede dar tamaños desiguales.

    3. **Aplicar propiedades flex al elemento equivocado.** `justify-content`, `align-items` y `flex-wrap` van en el CONTENEDOR. `flex-grow`, `flex-shrink`, `flex-basis` y `align-self` van en los ÍTEMS.

    4. **No establecer `flex-shrink: 0` en elementos que no deben deformarse.** Logos, iconos, avatares. Si no se especifica, pueden encogerse y deformarse cuando falta espacio.

    5. **Usar `float` o `inline-block` junto con Flexbox.** Las propiedades *float*, *clear* y *vertical-align* no tienen efecto en ítems flex. Si necesitas posicionamiento específico, usa las propiedades de Flexbox.

    6. **Olvidar que `align-content` solo funciona con `flex-wrap: wrap`.** Sin *wrap*, `align-content` no tiene efecto (solo hay una línea).

    7. **No probar con contenido de longitud variable.** Un *layout* flex puede verse perfecto con contenido de prueba breve y romperse con contenido real más largo. Prueba siempre con textos de diferentes longitudes.

    8. **Creer que `order` cambia el orden en el DOM.** Solo cambia la presentación visual. El orden de tabulación y accesibilidad sigue siendo el del DOM.

## Resumen

Esta unidad ha proporcionado un dominio completo de Flexbox, el modelo de maquetación unidimensional que ha revolucionado el desarrollo web moderno. El alumnado ha aprendido que Flexbox opera sobre dos ejes perpendiculares —principal y transversal— cuya orientación depende de `flex-direction`. Ha dominado las propiedades del contenedor (`justify-content`, `align-items`, `align-content`, `flex-wrap`, `gap`) que controlan la distribución colectiva de los ítems, y las propiedades de los ítems (`flex-grow`, `flex-shrink`, `flex-basis`, `align-self`, `order`) que controlan el comportamiento individual.

La unidad ha enfatizado la importancia del shorthand `flex` como forma preferida de controlar el crecimiento, reducción y tamaño base. Se ha explicado la diferencia crucial entre `flex: 1` (distribución proporcional desde cero) y `flex: auto` (distribución del espacio extra respetando tamaños de contenido), ya que confundirlos es fuente de errores comunes.

Los patrones de diseño estudiados cubren los casos de uso más frecuentes en el desarrollo profesional: barras de navegación responsive con hamburguesa CSS puro, grids de tarjetas con altura uniforme y footer alineado, dashboards con sidebar colapsable, formularios con etiquetas e inputs alineados, sticky footers, centrado perfecto, media objects y distribución avanzada con auto margins.

Se ha proporcionado una comparación clara entre Flexbox y CSS Grid: Flexbox para layouts unidimensionales (componentes, barras, listas), Grid para layouts bidimensionales (estructura de página, galerías con control de filas y columnas). Ambos se complementan y deben ser dominados por igual.

El alumnado ha completado 10 ejemplos guiados completos con código HTML y CSS extensamente comentado, ha analizado 3 casos reales de sitios web de primer nivel, y dispone de actividades para practicar desde lo más básico hasta proyectos completos de ampliación. Con esta base, está preparado para afrontar cualquier desafío de maquetación unidimensional que se presente en el desarrollo web profesional.

## Recursos complementarios

- **MDN Web Docs - Flexbox:** https://developer.mozilla.org/es/docs/Web/CSS/CSS_Flexible_Box_Layout - Referencia completa con ejemplos interactivos.
- **CSS-Tricks - A Complete Guide to Flexbox:** https://css-tricks.com/snippets/css/a-guide-to-flexbox/ - La guía visual más consultada, con diagramas de cada propiedad.
- **Flexbox Froggy:** https://flexboxfroggy.com/ - Juego interactivo para aprender Flexbox moviendo ranas. Ideal para practicar de forma lúdica.
- **Flexbox Defense:** http://www.flexboxdefense.com/ - Juego de tower defense donde se usan propiedades Flexbox para posicionar torres.
- **Flexbox Zombies:** https://mastery.games/flexboxzombies/ - Curso gamificado con narrativa de zombies.
- **Flexbox Patterns:** https://www.flexboxpatterns.com/ - Colección de patrones de diseño con Flexbox explicados paso a paso.
- **What The Flexbox?!** - Curso en video gratuito de Wes Bos con 20 lecciones prácticas.
- **Can I Use - Flexbox:** https://caniuse.com/flexbox - Tabla de compatibilidad de Flexbox por navegador.
- **Flexulator:** https://www.flexulator.com/ - Calculadora visual de crecimiento y reducción de ítems flex.
- **Solved by Flexbox:** https://philipwalton.github.io/solved-by-flexbox/ - Demostración de problemas clásicos de CSS resueltos con Flexbox.
