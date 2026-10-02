---
icon: lucide/grid-3x3
---

# Unidad 10: CSS Grid Layout

## Objetivos de aprendizaje

Al finalizar esta unidad, el alumnado será capaz de diseñar layouts web complejos y bidimensionales utilizando CSS Grid Layout con total solvencia. Los objetivos concretos son: comprender el modelo de cuadrícula bidimensional y sus diferencias fundamentales con Flexbox, sabiendo identificar cuándo usar cada uno; configurar un contenedor grid mediante las propiedades `display: grid`, `grid-template-columns`, `grid-template-rows` y `grid-template-areas` para definir la estructura base del layout; utilizar las unidades específicas de Grid como `fr`, `minmax()`, `auto` y `repeat()` para crear diseños flexibles y adaptables; controlar la posición y tamaño de los ítems individuales con las propiedades `grid-column`, `grid-row` y `grid-area`; implementar patrones de alineación completos aplicando `justify-items`, `align-items`, `justify-content`, `align-content` y sus variantes de ítem individual; comprender la distinción entre grid explícito e implícito y dominar el uso de `grid-auto-rows` y `grid-auto-columns` para controlar las filas y columnas generadas automáticamente; diseñar layouts profesionales completos como páginas de aterrizaje, blogs, dashboards y galerías empleando exclusivamente CSS Grid; integrar Grid con media queries para conseguir diseños totalmente responsive; y evaluar el uso real de Grid en sitios web profesionales analizando su implementación en casos de estudio del mundo real.

## Relación con los Resultados de Aprendizaje

Esta unidad desarrolla el **Resultado de Aprendizaje 2 (RA2)** del módulo 0615 *Diseño de interfaces web* —"Crea interfaces web homogéneos definiendo y aplicando estilos"—, según el currículo oficial (RD 405/2023, BOE; currículo andaluz). En concreto, permite alcanzar los criterios relacionados con la aplicación de las propiedades y clases CSS para definir la estructura visual de la interfaz (CE 2.f y CE 2.g) y el empleo de técnicas de diseño responsive (CE 2.i), verificando la correcta visualización en diferentes navegadores y dispositivos. CSS Grid constituye la herramienta moderna por excelencia para la maquetación bidimensional en la web, superando las limitaciones de sistemas anteriores como tablas, floats o incluso Flexbox en determinados contextos. El dominio de Grid capacita al alumnado para implementar los diseños creados en herramientas como Figma (trabajados en unidades anteriores) de forma fiel y semántica. Además, esta unidad se conecta transversalmente con los módulos de Desarrollo Web en Entorno Cliente y Desarrollo Web en Entorno Servidor, donde el alumnado aplicará estos conocimientos para construir aplicaciones web completas. La competencia profesional asociada es la capacidad de desarrollar interfaces web que cumplan con los requisitos de diseño, usabilidad y accesibilidad establecidos en los proyectos.

## Conocimientos previos

Antes de abordar esta unidad, el alumnado debe dominar los fundamentos de HTML semántico, incluyendo el uso correcto de elementos estructurales como `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>` y `<footer>`, ya que Grid se aplica sobre estos contenedores semánticos. Debe conocer el modelo de cajas de CSS en profundidad: la diferencia entre `content-box` y `border-box`, cómo se calculan los tamaños, y las propiedades `margin`, `padding`, `border`, `width` y `height`. Es imprescindible tener soltura con las propiedades de posicionamiento CSS: `static`, `relative`, `absolute`, `fixed` y `sticky`, así como el contexto de apilamiento con `z-index`. El alumnado debe haber trabajado previamente con Flexbox (Unidad 9) y comprender su modelo unidimensional, sus propiedades de contenedor (`display: flex`, `flex-direction`, `flex-wrap`, `justify-content`, `align-items`, `align-content`, `gap`) y de ítem (`flex-grow`, `flex-shrink`, `flex-basis`, `align-self`, `order`). También debe manejar las unidades de medida CSS (`px`, `%`, `em`, `rem`, `vw`, `vh`, `vmin`, `vmax`), el uso de variables CSS (`--nombre-variable`), y la metodología de diseño responsive con media queries. Se asume conocimiento básico de las herramientas de desarrollo del navegador (Chrome DevTools o Firefox Developer Tools) para inspeccionar y depurar layouts. Por último, es recomendable haber practicado con la metodología Mobile First y los breakpoints comunes para entender cómo Grid se adapta a diferentes tamaños de pantalla.

## Contenidos

1. **Introducción a CSS Grid**: Historia y evolución de la maquetación web (tablas, floats, Flexbox, Grid). El modelo bidimensional. Filosofía de diseño: definir la cuadrícula primero, colocar los elementos después. Compatibilidad con navegadores y estrategia de adopción progresiva.

2. **El contenedor Grid**: Propiedades `display: grid` e `inline-grid`. Definición de columnas con `grid-template-columns`. Definición de filas con `grid-template-rows`. La función `repeat()`. Unidades disponibles: `px`, `%`, `fr`, `auto`, `min-content`, `max-content`. La función `minmax()`.

3. **Unidades y funciones avanzadas**: La unidad fracción (`fr`) explicada en detalle. Cálculo de espacio disponible. `auto-fill` vs `auto-fit` con `repeat()`. La función `minmax()` para límites flexibles. Uso combinado de diferentes unidades.

4. **Espaciado en Grid**: `column-gap`, `row-gap` y el shorthand `gap`. Diferencias con márgenes tradicionales. Espaciado responsivo con funciones CSS.

5. **Grid explícito vs implícito**: Concepto de grid explícito (definido por `grid-template-*`). Concepto de grid implícito (generado automáticamente). Control del grid implícito con `grid-auto-rows`, `grid-auto-columns` y `grid-auto-flow`.

6. **Posicionamiento de ítems**: `grid-column-start`, `grid-column-end`, `grid-row-start`, `grid-row-end`. Shorthands `grid-column` y `grid-row`. Uso de líneas numeradas, líneas con nombre, `span` y valores negativos. La propiedad `grid-area` como shorthand definitivo.

7. **Grid Areas**: Nombrado de áreas de cuadrícula. `grid-template-areas` para maquetación visual. Colocación de ítems mediante `grid-area`. Reorganización visual independiente del orden en el DOM.

8. **Alineación en Grid**: Propiedades de contenedor: `justify-items`, `align-items`, `place-items`, `justify-content`, `align-content`, `place-content`. Propiedades de ítem: `justify-self`, `align-self`, `place-self`. Valores: `start`, `end`, `center`, `stretch`.

9. **Subgrid**: Concepto y propósito. Herencia de la cuadrícula padre. Compatibilidad actual. Casos de uso prácticos con tarjetas alineadas.

10. **Patrones de layout con Grid**: Landing page completa, blog con grid de posts, ecommerce con filtros y productos, dashboard profesional, galería avanzada, layout de artículo editorial.

11. **Grid responsive**: Combinación con media queries. Cambios de `grid-template-areas` en breakpoints. Uso de `auto-fill`/`auto-fit` para layouts fluidos. Grid + Flexbox: cuándo y cómo combinar ambos modelos.

12. **Casos reales**: Análisis de implementaciones de Grid en sitios web profesionales (Airbnb, Spotify, The New York Times).

## Desarrollo teórico

### 1. Introducción a CSS Grid Layout

!!! info "Un poco de historia"
    **CSS Grid Layout** es el sistema de maquetación bidimensional más potente disponible en CSS. Fue diseñado específicamente para resolver los problemas de *layout* web que durante décadas se habían abordado con soluciones improvisadas: **tablas HTML** (uso no semántico), **floats** (diseñados para texto alrededor de imágenes), **posicionamiento absoluto** (difícil de mantener) y más recientemente **Flexbox** (excelente pero limitado a una dimensión). La especificación comenzó a gestarse en **2011**, cuando Microsoft implementó una versión temprana en Internet Explorer 10. Posteriormente, el W3C estandarizó la especificación oficial y en **marzo de 2017** los principales navegadores (Chrome, Firefox, Safari, Edge) lanzaron soporte completo casi simultáneamente, marcando un hito en la historia del desarrollo web.

La diferencia fundamental entre Grid y Flexbox radica en la **dimensionalidad** del *layout* que cada uno gestiona:

| | **Flexbox** | **CSS Grid** |
|---|---|---|
| **Modelo** | Unidimensional: trabaja en una sola dirección, ya sea fila o columna | Bidimensional: permite controlar simultáneamente filas y columnas |
| **Ideal para** | Distribuir elementos a lo largo de un eje: barras de navegación, listas de elementos, centrado de contenido | Maquetar páginas completas con cabeceras, barras laterales, áreas de contenido y pies de página |
| **Enfoque** | El contenido dicta el *layout* | El *layout* define dónde va el contenido |

Aunque ambos modelos pueden usarse en los mismos proyectos y a menudo se complementan, la **regla práctica** es: si necesitas control en **una sola dimensión**, usa Flexbox; si necesitas control en **dos dimensiones**, usa Grid.

!!! tip "Soporte y estrategia de adopción"
    El soporte actual de CSS Grid es universal: según datos de *Can I Use*, la cobertura global **supera el 97%** de los navegadores en uso, incluyendo todos los navegadores modernos en sus versiones actuales y la práctica totalidad de dispositivos móviles. Para navegadores antiguos como Internet Explorer 11 existe soporte parcial mediante la sintaxis prefijada (`-ms-grid`), aunque con limitaciones significativas. La estrategia recomendada es utilizar `@supports (display: grid)` para detectar soporte y proporcionar un *fallback* con Flexbox o *floats* cuando sea necesario.

### 2. El contenedor Grid

!!! info "El contenedor grid"
    El punto de partida para cualquier *layout* con Grid es declarar un elemento como contenedor grid mediante **`display: grid`** (o **`display: inline-grid`** si se desea que el contenedor se comporte como un elemento *inline*). A partir de ese momento, **todos los hijos directos** del contenedor se convierten automáticamente en ítems de la cuadrícula. A diferencia de Flexbox, el contenedor Grid requiere que se defina explícitamente la estructura de la cuadrícula: cuántas columnas tendrá, cuántas filas, y qué tamaños tendrán.

La propiedad **`grid-template-columns`** define el número y tamaño de las columnas: cada valor especificado crea una columna nueva. Análogamente, **`grid-template-rows`** define las filas. La función **`repeat()`** permite generar patrones repetitivos de forma concisa:

| Declaración | Equivalencia |
|-------------|--------------|
| `grid-template-columns: 200px 1fr 200px` | Tres columnas: dos laterales de 200 píxeles fijos y una central que ocupa el espacio restante. |
| `grid-template-columns: repeat(3, 1fr)` | `grid-template-columns: 1fr 1fr 1fr`: tres columnas de igual tamaño. |

Otras propiedades relevantes del contenedor:

- **`grid-template`** — *shorthand* que permite definir `grid-template-rows`, `grid-template-columns` y `grid-template-areas` en una sola declaración.
- **`grid-auto-rows`** y **`grid-auto-columns`** — definen el tamaño de las filas y columnas que se crean automáticamente cuando hay más ítems de los que caben en la cuadrícula explícita. Por ejemplo, en un grid de 12 columnas con `grid-auto-rows: 100px`, todas las filas creadas automáticamente tendrán 100 píxeles de alto.
- **`grid-auto-flow`** — controla el algoritmo de colocación automática: con valor `row` (por defecto) los ítems se colocan por filas, y con `column` se colocan por columnas. El valor `dense` activa un algoritmo que intenta llenar huecos en la cuadrícula, compactando visualmente los ítems aunque pueda alterar su orden.

!!! tip "Prefiere las propiedades individuales"
    La sintaxis del *shorthand* `grid-template` es compleja y se recomienda usarla con precaución. Para mantener la legibilidad del código, declara **`grid-template-columns`**, **`grid-template-rows`** y **`grid-template-areas`** por separado.

### 3. Unidades avanzadas de Grid

!!! info "La unidad fr"
    La unidad **`fr`** (fracción) es uno de los conceptos más potentes de CSS Grid y no existe en ningún otro contexto de CSS. Representa una fracción del **espacio disponible** dentro del contenedor grid, *después* de restar los espacios ocupados por elementos con tamaño fijo y los *gaps*. En `grid-template-columns: 1fr 2fr 1fr`, el espacio disponible se divide en **4 partes iguales**: la primera columna recibe 1 parte, la segunda 2 partes, y la tercera 1 parte. Esta unidad elimina la necesidad de calcular porcentajes y resulta especialmente útil en *layouts* responsivos.

La función **`minmax()`** permite establecer un rango de tamaño entre un valor **mínimo** y uno **máximo**. Es ideal para crear *layouts* flexibles que no colapsen más allá de un límite ni crezcan descontroladamente. Por ejemplo, `grid-template-columns: repeat(auto-fill, minmax(250px, 1fr))` crea tantas columnas como quepan, cada una con al menos **250px** y como máximo el espacio disponible. Los valores mínimo y máximo pueden ser cualquier unidad CSS, incluyendo `auto`, `min-content` o `max-content`.

Las palabras clave **`auto-fill`** y **`auto-fit`** se usan exclusivamente dentro de la función `repeat()` y controlan qué ocurre cuando hay espacio sobrante en la cuadrícula:

| Palabra clave | Comportamiento |
|---------------|----------------|
| **`auto-fill`** | Crea tantas pistas (columnas o filas) como quepan, **incluso si no hay suficientes ítems** para llenarlas, dejando espacio vacío al final. |
| **`auto-fit`** | También crea tantas pistas como quepan, pero **colapsa las pistas vacías**, permitiendo que los ítems existentes se expandan para ocupar el espacio sobrante. |

Esta diferencia es sutil pero crucial: **`auto-fit`** produce un *layout* que se ajusta al contenido, mientras que **`auto-fill`** mantiene la estructura de columnas aunque estén vacías.

!!! tip "Layouts fluidos sin media queries"
    El uso combinado de **`repeat()`**, **`auto-fit`/`auto-fill`** y **`minmax()`** permite crear *layouts* completamente responsivos **sin necesidad de media queries**: la combinación se adapta automáticamente a cualquier tamaño de pantalla.

### 4. Posicionamiento de ítems Grid

!!! info "Líneas de la cuadrícula"
    Cada ítem dentro de un contenedor grid puede posicionarse de forma **independiente de su orden en el DOM**. Las líneas de la cuadrícula se numeran automáticamente **empezando desde 1**, tanto para filas como para columnas. La numeración incluye también **valores negativos**: la línea **-1** es la última línea de la cuadrícula, **-2** la penúltima, y así sucesivamente. Esta doble numeración facilita enormemente el posicionamiento de ítems que deben ocupar hasta el final de la cuadrícula.

Las propiedades **`grid-column-start`** y **`grid-column-end`** definen sobre qué líneas de columna comienza y termina un ítem. Las mismas reglas se aplican a las filas con `grid-row-start`, `grid-row-end` y el *shorthand* `grid-row`.

| Declaración | Resultado |
|-------------|-----------|
| `grid-column-start: 1; grid-column-end: 3` | El ítem ocupa desde la línea 1 a la 3: **dos columnas**. |
| **`grid-column: 1 / 3`** | *Shorthand* equivalente a la declaración anterior. |
| **`grid-column: 1 / span 2`** | La palabra clave `span` indica cuántas celdas ocupa en lugar de la línea de fin: también **dos columnas**. |
| **`grid-row`** | *Shorthand* de `grid-row-start` y `grid-row-end`, con idéntico comportamiento. |

!!! info "grid-area, el shorthand definitivo"
    La propiedad **`grid-area`** agrupa las cuatro propiedades anteriores en el orden `grid-row-start / grid-column-start / grid-row-end / grid-column-end`. Por ejemplo, `grid-area: 1 / 1 / 3 / 3` posiciona un ítem desde la fila 1 columna 1 hasta la fila 3 columna 3, ocupando una caja de **2×2**. Esta propiedad también se utiliza para asignar ítems a **áreas nombradas** en `grid-template-areas`, lo que la convierte en una de las propiedades más versátiles de Grid.

### 5. Grid Areas: maquetación visual

!!! info "Grid areas: maquetación visual"
    Las áreas de cuadrícula constituyen la forma más intuitiva y visual de diseñar *layouts* con CSS Grid. Mediante **`grid-template-areas`** se define la estructura de la página como un **mapa ASCII** directamente en el CSS, asignando nombres significativos a cada región del *layout*. Esta técnica es especialmente poderosa porque **la disposición visual en el código coincide con la disposición visual en la página renderizada**, facilitando el mantenimiento y las modificaciones.

La propiedad `grid-template-areas` acepta una lista de cadenas de texto, donde:

- **Cada cadena** de texto representa una fila y **cada palabra** dentro de la cadena representa una celda.
- Las **celdas consecutivas con el mismo nombre** se fusionan en una sola área.
- Un punto (**`.`**) indica una **celda vacía**.
- Para asignar un ítem a un área nombrada se utiliza **`grid-area: nombre-area`** en el ítem correspondiente.

Por ejemplo, un *layout* clásico de cabecera-contenido-pie se define como: `grid-template-areas: "header header header" "sidebar content content" "footer footer footer"`.

!!! tip "Reorganizar el layout sin tocar el HTML"
    Una de las ventajas más significativas de las áreas de cuadrícula es la capacidad de **reorganizar completamente el *layout* en distintos *breakpoints*** simplemente redefiniendo `grid-template-areas` dentro de una media query, sin necesidad de modificar el HTML ni las propiedades individuales de cada ítem. Esta reordenación visual independiente del DOM es fundamental para el diseño *responsive* y la **accesibilidad**, ya que permite mantener un orden lógico en el HTML (para lectores de pantalla y SEO) mientras se presenta una disposición visual diferente.

### 6. Alineación en Grid

CSS Grid comparte con Flexbox el sistema de alineación del *Box Alignment Module*, lo que proporciona consistencia entre ambos modelos. Las propiedades de alineación se dividen en **dos grupos**: las que se aplican al **contenedor** grid (afectando a todos los ítems) y las que se aplican a **ítems individuales** (sobrescribiendo la alineación del contenedor para ítems específicos).

| Propiedad | Dónde se aplica | Función |
|-----------|-----------------|---------|
| **`justify-items`** / **`align-items`** | Contenedor | Alinean **todos los ítems** dentro de sus respectivas celdas, en los ejes horizontal (*inline*) y vertical (*block*). Valores: `stretch` (por defecto), `start`, `center`, `end`. |
| **`place-items`** | Contenedor | *Shorthand* que establece `align-items` y `justify-items` simultáneamente. |
| **`justify-content`** / **`align-content`** | Contenedor | Alinean **toda la cuadrícula** dentro del contenedor cuando sobra espacio. Valores: `start`, `end`, `center`, `space-between`, `space-around`, `space-evenly`. |
| **`place-content`** | Contenedor | *Shorthand* que establece `align-content` y `justify-content` simultáneamente. |
| **`justify-self`** / **`align-self`** | Ítem | Sobrescriben la alineación del contenedor para un ítem específico. |
| **`place-self`** | Ítem | *Shorthand* de `align-self` y `justify-self`. |

Las propiedades de contenedor **`justify-items`** y **`align-items`** controlan la alineación de todos los ítems dentro de sus respectivas celdas. El valor por defecto es **`stretch`**, que hace que los ítems se expandan para llenar completamente su celda; los valores `start`, `center` y `end` alinean los ítems al inicio, centro o final de la celda.

Cuando el tamaño total de la cuadrícula es menor que el del contenedor (por ejemplo, columnas con tamaños fijos en un contenedor más ancho), las propiedades **`justify-content`** y **`align-content`** controlan la alineación de toda la cuadrícula dentro del contenedor. Con `justify-content: center`, la cuadrícula se centra horizontalmente. Con `space-between` o `space-around`, el espacio sobrante se distribuye entre o alrededor de las columnas/filas. `space-evenly` distribuye el espacio equitativamente entre todas las columnas/filas y los bordes del contenedor.

Para ítems individuales, **`justify-self`** y **`align-self`** sobrescriben la alineación establecida por el contenedor para un ítem específico. Estas propiedades son útiles cuando se necesita que un ítem concreto tenga una alineación diferente al resto, como una imagen que debe estar centrada verticalmente dentro de su celda mientras otros ítems usan `stretch`.

!!! warning "justify-items frente a justify-content"
    Es habitual usar **`justify-content`** esperando centrar los ítems individualmente cuando en realidad se necesita **`justify-items`**: la primera propiedad alinea la **cuadrícula completa** dentro del contenedor, mientras que la segunda alinea los **ítems dentro de sus celdas**. Distinguir a qué grupo pertenece cada propiedad evita la mayoría de los errores de alineación en Grid.

### 7. Grid implícito vs explícito

!!! info "Grid explícito frente a grid implícito"
    La distinción entre grid explícito e implícito es crucial para manejar *layouts* con contenido dinámico donde el número de ítems no se conoce de antemano. El **grid explícito** es el definido por la persona desarrolladora mediante `grid-template-columns` y `grid-template-rows`. El **grid implícito** se genera automáticamente cuando hay más ítems de los que caben en el grid explícito o cuando un ítem se posiciona fuera de los límites definidos.

Por defecto, el grid implícito crea nuevas filas con altura **`auto`**, lo que significa que se ajustan al contenido. Para controlar este comportamiento se utilizan **`grid-auto-rows`** (por ejemplo, `grid-auto-rows: 150px` asegura que todas las filas creadas automáticamente tengan 150 píxeles de altura) y **`grid-auto-columns`**. La propiedad **`grid-auto-flow`** controla la dirección en la que se añaden nuevos ítems: **`row`** (por defecto, los ítems llenan filas) o **`column`** (los ítems llenan columnas).

!!! warning "grid-auto-flow dense altera el orden visual"
    El valor **`dense`** activa un algoritmo que intenta llenar huecos colocando ítems en espacios más pequeños si encajan, compactando visualmente la cuadrícula. **Esto puede alterar el orden visual de los ítems**: si el orden es importante para la semántica o la accesibilidad, `dense` puede causar problemas. Úsalo solo cuando el orden visual no sea significativo (como en galerías de imágenes).

Esta distinción es particularmente útil en contextos como listados de productos en un ecommerce (donde no se sabe cuántos productos habrá), galerías de imágenes generadas dinámicamente, o *feeds* de redes sociales que cargan contenido de forma asíncrona. Al definir el grid explícito para la estructura base y confiar en el grid implícito para el contenido variable, se logra un *layout* robusto que se adapta automáticamente al contenido.

### 8. Subgrid

!!! info "¿Qué es Subgrid?"
    **Subgrid** es una característica de CSS Grid **nivel 2** que permite a un ítem grid **heredar la definición de cuadrícula de su contenedor padre** para sus propios hijos. Esto significa que los elementos anidados dentro de un ítem grid pueden alinearse con la cuadrícula principal, resolviendo el problema histórico de que las cuadrículas anidadas no compartían las líneas de la cuadrícula contenedora.

Para activar subgrid, se usa el valor **`subgrid`** en `grid-template-columns` o `grid-template-rows` dentro de un contenedor que es a su vez ítem grid. Por ejemplo, si una tarjeta de producto es un ítem grid y necesita que su título, descripción y botón se alineen horizontalmente con los de otras tarjetas en la misma fila, se puede declarar `grid-template-rows: subgrid` en la tarjeta para que herede las líneas de fila de la cuadrícula padre.

!!! tip "Subgrid en la práctica"
    El soporte de Subgrid está disponible en **todos los navegadores modernos desde 2023**. Permite una **alineación perfecta entre componentes** sin necesidad de JavaScript ni soluciones complejas: es la respuesta estándar para alinear el contenido interno de tarjetas de altura variable.

### 9. Grid + Flexbox: estrategia combinada

!!! tip "Grid para la estructura, Flexbox para los componentes"
    CSS Grid y Flexbox **no son competidores sino aliados**: la combinación de ambos modelos produce *layouts* extremadamente flexibles y mantenibles. La estrategia recomendada es usar **Grid para la estructura principal** del *layout* (cabecera, *sidebar*, contenido, pie) y **Flexbox para los componentes internos** (alineación de elementos en una barra de navegación, distribución de tarjetas dentro de una sección, centrado de contenido en un héroe). Por ejemplo, un *layout* de página completa puede usar Grid para la disposición de las secciones principales y, dentro de cada sección, emplear Flexbox para alinear su contenido. También es común usar Grid para *layouts* que requieran control en ambos ejes (como una galería de imágenes con diferentes tamaños) y Flexbox para barras de navegación, listas horizontales o formularios.


## Ejemplos guiados

### Ejemplo Guiado 1: Primera cuadrícula básica con Grid

En este primer ejemplo construiremos una cuadrícula simple de 3 columnas con 5 elementos, demostrando cómo Grid distribuye automáticamente los ítems y cómo podemos hacer que ciertos elementos ocupen varias columnas o filas. La cuadrícula usa unidades mixtas: píxeles para las columnas laterales y fracciones para la columna central, un patrón muy común en layouts web.

=== "HTML"

    ``` html
    <!DOCTYPE html>
    <html lang="es">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Ejemplo 1 - Grid Básico</title>
      <link rel="stylesheet" href="./styles.css">
    </head>
    <body>
      <h2>Grid Básico: Cabecera, Sidebar, Contenido, Pie</h2>
      <div class="grid-contenedor">
        <div class="item">1 - Cabecera</div>
        <div class="item">2 - Sidebar izquierdo</div>
        <div class="item">3 - Contenido principal</div>
        <div class="item">4 - Sidebar derecho</div>
        <div class="item">5 - Pie de página</div>
      </div>
    </body>
    </html>
    ```

=== "CSS"

    ``` css
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      padding: 2rem;
      background: #f0f2f5;
    }

    h2 {
      text-align: center;
      margin-bottom: 1.5rem;
      color: #333;
    }

    /* ===== CONTENEDOR GRID ===== */
    /*
     * display: grid: activa el contexto de cuadrícula.
     * grid-template-columns define 3 columnas:
     *   Col 1: 200px fijos (sidebar)
     *   Col 2: 1fr (espacio restante)
     *   Col 3: 200px fijos (sidebar)
     * grid-template-rows: 3 filas con alturas definidas.
     * gap: 16px = espacio uniforme entre celdas.
     */
    .grid-contenedor {
      display: grid;
      grid-template-columns: 200px 1fr 200px;
      grid-template-rows: 80px 200px 80px;
      gap: 16px;
      background: #fff;
      padding: 16px;
      border-radius: 12px;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
      max-width: 1000px;
      margin: 0 auto;
    }

    /*
     * Cada ítem recibe estilos visuales para distinguirlo.
     * Los ítems se colocan automáticamente en el orden del DOM,
     * llenando las celdas disponibles fila por fila.
     */
    .item {
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      color: #fff;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 8px;
      font-weight: 600;
      font-size: 1.1rem;
    }

    /*
     * Los ítems 1 y 5 (cabecera y pie) ocupan TODAS las columnas.
     * grid-column: 1 / -1 significa:
     *   Empieza en la línea 1, termina en la línea -1 (la última).
     *   Los valores negativos cuentan desde el final.
     */
    .item:nth-child(1),
    .item:nth-child(5) {
      grid-column: 1 / -1;
    }

    /*
     * El ítem 3 (contenido principal) ocupa 2 filas.
     * grid-row: span 2 extiende el ítem 2 filas desde su posición.
     */
    .item:nth-child(3) {
      grid-row: span 2;
      background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    }
    ```

### Ejemplo Guiado 2: Grid con áreas nombradas

Las áreas nombradas son la forma más intuitiva de diseñar layouts con Grid. Consiste en dibujar literalmente la estructura de la página usando nombres significativos en una cuadrícula de texto. Este ejemplo muestra un layout completo con cabecera, navegación, héroe, sidebar, contenido principal y pie de página.

=== "HTML"

    ``` html
    <!DOCTYPE html>
    <html lang="es">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Ejemplo 2 - Grid Template Areas</title>
      <link rel="stylesheet" href="./styles.css">
    </head>
    <body>
      <!-- El HTML es lineal y semántico -->
      <!-- La disposición visual se define solo en CSS -->
      <div class="pagina">
        <header class="logo">LOGO</header>
        <nav class="navegacion">
          <a href="#">Inicio</a>
          <a href="#">Cursos</a>
          <a href="#">Blog</a>
          <a href="#">Contacto</a>
        </nav>
        <div class="usuario">Mi Cuenta</div>

        <section class="hero">Bienvenidos a la plataforma educativa</section>

        <aside class="lateral">
          <h3>Categorías</h3>
          <ul>
            <li>Desarrollo Web</li>
            <li>Diseño UX/UI</li>
            <li>Bases de Datos</li>
            <li>DevOps</li>
          </ul>
        </aside>

        <main class="contenido">
          <h2>Contenido Principal</h2>
          <p>Aquí se muestra el contenido principal de la página. CSS Grid permite
          definir este layout de forma visual y semántica, separando la estructura
          HTML de la presentación visual. Esto es clave para accesibilidad y SEO.</p>
        </main>

        <footer class="footer">2025 Plataforma Educativa - Todos los derechos reservados</footer>
      </div>
    </body>
    </html>
    ```

=== "CSS"

    ``` css
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      min-height: 100vh;
      padding: 1rem;
      background: #e8ecf1;
    }

    /*
     * grid-template-areas define el layout como mapa visual.
     * Cada cadena es una fila; cada palabra dentro, una celda.
     * Nombres repetidos en celdas adyacentes = áreas fusionadas.
     * El punto (.) indica celda vacía.
     */
    .pagina {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      grid-template-rows: 80px auto 1fr 60px;
      grid-template-areas:
        "logo     nav      nav      usuario"
        "hero     hero     hero     hero"
        "lateral  contenido contenido contenido"
        "footer   footer   footer   footer";
      gap: 12px;
      min-height: 100vh;
      max-width: 1200px;
      margin: 0 auto;
    }

    /* Asignación de cada elemento HTML a su área con grid-area */
    .logo {
      grid-area: logo;
      background: #1a1a2e;
      color: #fff;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 8px;
      font-weight: 700;
      font-size: 1.2rem;
    }

    .navegacion {
      grid-area: nav;
      background: #16213e;
      color: #fff;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 8px;
      gap: 2rem;
    }

    .navegacion a {
      color: #e2e2e2;
      text-decoration: none;
      padding: 0.5rem 1rem;
      border-radius: 4px;
      transition: background 0.3s;
    }

    .navegacion a:hover {
      background: rgba(255, 255, 255, 0.15);
    }

    .usuario {
      grid-area: usuario;
      background: #1a1a2e;
      color: #fff;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 8px;
    }

    .hero {
      grid-area: hero;
      background: linear-gradient(135deg, #0f3460, #533483);
      color: #fff;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 8px;
      font-size: 2rem;
      font-weight: 700;
      padding: 3rem;
      text-align: center;
    }

    .lateral {
      grid-area: lateral;
      background: #fff;
      padding: 1.5rem;
      border-radius: 8px;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
    }

    .contenido {
      grid-area: contenido;
      background: #fff;
      padding: 1.5rem;
      border-radius: 8px;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
    }

    .footer {
      grid-area: footer;
      background: #1a1a2e;
      color: #ccc;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 8px;
    }
    ```


### Ejemplo Guiado 3: Unidades fr, minmax() y repeat() con auto-fill/auto-fit

Las unidades de Grid son uno de sus mayores puntos fuertes. Este ejemplo demuestra el uso de la unidad fracción (fr), la función minmax() para establecer límites flexibles, y las diferencias cruciales entre auto-fill y auto-fit cuando se combinan con repeat().

=== "HTML"

    ``` html
    <!DOCTYPE html>
    <html lang="es">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Ejemplo 3 - Unidades Avanzadas de Grid</title>
      <link rel="stylesheet" href="./styles.css">
    </head>
    <body>
      <h2>Grid con minmax() - Altura mínima 100px, crece con contenido</h2>
      <div class="grid-minmax">
        <div class="tarjeta">Contenido corto</div>
        <div class="tarjeta">Contenido medio con algo más de información</div>
        <div class="tarjeta tarjeta-alta">
          <div>
            <p>Contenido extenso</p>
            <p>Esta tarjeta tiene más texto. minmax(100px, auto) hace que
            la fila crezca automáticamente. Las otras tarjetas en la misma
            fila también igualan la altura gracias a Grid.</p>
          </div>
        </div>
        <div class="tarjeta">Corto</div>
        <div class="tarjeta">Medio</div>
        <div class="tarjeta">Corto</div>
      </div>

      <h2>auto-fill: columnas vacías se mantienen</h2>
      <!-- 3 ítems en espacio para 5 columnas -> 2 columnas vacías visibles -->
      <div class="grid-auto-fill">
        <div class="tarjeta">Ítem 1</div>
        <div class="tarjeta">Ítem 2</div>
        <div class="tarjeta">Ítem 3</div>
      </div>

      <h2>auto-fit: ítems se expanden para llenar espacio</h2>
      <!-- 3 ítems, se expanden porque las columnas vacías se colapsan -->
      <div class="grid-auto-fit">
        <div class="tarjeta">Ítem 1</div>
        <div class="tarjeta">Ítem 2</div>
        <div class="tarjeta">Ítem 3</div>
      </div>
    </body>
    </html>
    ```

=== "CSS"

    ``` css
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      padding: 2rem;
      background: #1a1a2e;
      color: #fff;
    }
    h2 { margin-bottom: 1.5rem; }

    /*
     * minmax() define un rango de tamaño: mínimo y máximo.
     * grid-auto-rows: minmax(100px, auto)
     * Cada fila tendrá al menos 100px pero crecerá si el contenido lo requiere.
     * Esto evita desbordamientos y mantiene una altura mínima consistente.
     */
    .grid-minmax {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      grid-auto-rows: minmax(100px, auto);
      gap: 20px;
      margin-bottom: 3rem;
    }

    /*
     * auto-fill: crea tantas columnas como quepan, incluso vacías.
     * Las columnas vacías ocupan espacio visible.
     * Ideal para mantener la estructura de rejilla aunque haya pocos ítems.
     */
    .grid-auto-fill {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
      gap: 16px;
      margin-bottom: 3rem;
    }

    /*
     * auto-fit: similar pero COLAPSA las columnas vacías.
     * Los ítems se expanden para llenar todo el ancho disponible.
     * Ideal cuando quieres que los ítems ocupen todo el espacio.
     */
    .grid-auto-fit {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 16px;
      margin-bottom: 3rem;
    }

    .tarjeta {
      background: linear-gradient(135deg, #667eea, #764ba2);
      padding: 1.5rem;
      border-radius: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 600;
      font-size: 1.1rem;
    }

    .tarjeta-alta { min-height: 200px; }
    .tarjeta:nth-child(3n+1) { background: linear-gradient(135deg, #f093fb, #f5576c); }
    .tarjeta:nth-child(3n+2) { background: linear-gradient(135deg, #4facfe, #00f2fe); }
    .tarjeta:nth-child(3n+3) { background: linear-gradient(135deg, #43e97b, #38f9d7); }
    ```

### Ejemplo Guiado 4: Grid implícito vs explícito y grid-auto-flow

Cuando el número de ítems supera las celdas definidas, el navegador genera automáticamente nuevas filas o columnas (grid implícito). Este ejemplo muestra cómo controlar este comportamiento con grid-auto-rows, grid-auto-columns y grid-auto-flow.

=== "HTML"

    ``` html
    <!DOCTYPE html>
    <html lang="es">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Ejemplo 4 - Grid Implícito vs Explícito</title>
      <link rel="stylesheet" href="./styles.css">
    </head>
    <body>
      <h2>Grid Explícito (azul) vs Implícito (oscuro)</h2>
      <p>4 celdas definidas explícitamente. Los 4 ítems extra generan nuevas filas.</p>
      <div class="grid-impl">
        <div class="item">1 - Explícito</div>
        <div class="item">2 - Explícito</div>
        <div class="item">3 - Explícito</div>
        <div class="item">4 - Explícito</div>
        <div class="item">5 - Implícito</div>
        <div class="item">6 - Implícito</div>
        <div class="item">7 - Implícito</div>
        <div class="item">8 - Implícito</div>
      </div>

      <h2>grid-auto-flow: column</h2>
      <p>Los ítems extra se colocan en nuevas COLUMNAS, no en nuevas filas.</p>
      <div class="grid-auto-flow-col">
        <div class="item">1</div><div class="item">2</div>
        <div class="item">3</div><div class="item">4</div>
        <div class="item">5</div><div class="item">6</div>
        <div class="item">7</div><div class="item">8</div>
      </div>

      <h2>grid-auto-flow: dense</h2>
      <p>Los huecos se rellenan automáticamente. Observa cómo los ítems pequeños
      ocupan los espacios libres dejados por los ítems grandes.</p>
      <div class="grid-dense">
        <div class="item">1 (2x2)</div><div class="item">2</div>
        <div class="item">3</div><div class="item">4</div>
        <div class="item">5 (2x2)</div><div class="item">6</div>
        <div class="item">7</div><div class="item">8</div>
        <div class="item">9</div><div class="item">10</div>
        <div class="item">11</div><div class="item">12</div>
      </div>
    </body>
    </html>
    ```

=== "CSS"

    ``` css
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      padding: 2rem;
      background: #0d1117;
      color: #c9d1d9;
    }
    h2 { margin-bottom: 1rem; color: #58a6ff; }
    p { margin-bottom: 1.5rem; color: #8b949e; }

    /*
     * Grid explícito: 2x2 = 4 celdas definidas.
     * Tenemos 8 ítems, los 4 extra van al grid implícito.
     * grid-auto-rows: 120px define altura para filas implícitas.
     */
    .grid-impl {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      grid-template-rows: repeat(2, 120px);
      grid-auto-rows: 120px;
      gap: 12px;
      margin-bottom: 2rem;
    }

    /*
     * grid-auto-flow: column
     * En lugar de añadir nuevas FILAS para ítems extra,
     * añade nuevas COLUMNAS. Ideal para layouts horizontales.
     */
    .grid-auto-flow-col {
      display: grid;
      grid-template-columns: repeat(2, 150px);
      grid-template-rows: repeat(2, 120px);
      grid-auto-flow: column;
      grid-auto-columns: 150px;
      gap: 12px;
      margin-bottom: 2rem;
    }

    /*
     * grid-auto-flow: dense
     * El algoritmo intenta llenar TODOS los huecos con ítems
     * que quepan, reorganizándolos visualmente si es necesario.
     * Perfecto para galerías de imágenes de diferentes tamaños.
     */
    .grid-dense {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      grid-auto-flow: dense;
      grid-auto-rows: 100px;
      gap: 10px;
    }

    .grid-dense .item:nth-child(1),
    .grid-dense .item:nth-child(5) {
      grid-column: span 2;
      grid-row: span 2;
      background: #238636;
    }

    .item {
      background: #21262d;
      border: 1px solid #30363d;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 600;
      color: #c9d1d9;
    }

    /* Ítems del grid explícito en azul para diferenciarlos */
    .grid-impl .item:nth-child(-n+4),
    .grid-auto-flow-col .item:nth-child(-n+4) {
      background: #1f6feb;
      color: #fff;
      border-color: #1f6feb;
    }
    ```

### Ejemplo Guiado 5: Sistema completo de alineación en Grid

La alineación es uno de los aspectos más potentes de Grid. Este ejemplo explora todas las propiedades: justify-items, align-items, place-items (alinear ítems en sus celdas), justify-content, align-content, place-content (alinear la cuadrícula en el contenedor), y justify-self, align-self, place-self (sobrescribir alineación para ítems específicos).

=== "HTML"

    ``` html
    <!DOCTYPE html>
    <html lang="es">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Ejemplo 5 - Alineación Completa en Grid</title>
      <link rel="stylesheet" href="./styles.css">
    </head>
    <body>
      <section>
        <h2>place-items: stretch (comportamiento por defecto)</h2>
        <p class="desc">Los ítems se estiran para llenar completamente su celda.</p>
        <div class="grid-items">
          <div class="item">1</div><div class="item">2</div>
          <div class="item">3</div><div class="item">4</div>
          <div class="item">5</div><div class="item">6</div>
          <div class="item">7</div><div class="item">8</div>
        </div>
      </section>

      <section>
        <h2>place-items: center</h2>
        <p class="desc">Ítems centrados en ambas direcciones. Se encogen al tamaño del contenido.</p>
        <div class="grid-items center">
          <div class="item item-ident">1</div><div class="item item-ident">2</div>
          <div class="item item-ident">3</div><div class="item item-ident">4</div>
          <div class="item item-ident">5</div><div class="item item-ident">6</div>
          <div class="item item-ident">7</div><div class="item item-ident">8</div>
        </div>
      </section>

      <section>
        <h2>place-items: start</h2>
        <p class="desc">Ítems alineados al inicio (arriba-izquierda) de sus celdas.</p>
        <div class="grid-items start">
          <div class="item item-ident">1</div><div class="item item-ident">2</div>
          <div class="item item-ident">3</div><div class="item item-ident">4</div>
          <div class="item item-ident">5</div><div class="item item-ident">6</div>
          <div class="item item-ident">7</div><div class="item item-ident">8</div>
        </div>
      </section>

      <section>
        <h2>place-content: center</h2>
        <p class="desc">La cuadrícula completa se centra en el contenedor (más grande que ella).</p>
        <div class="grid-content center">
          <div class="item">1</div><div class="item">2</div><div class="item">3</div>
          <div class="item">4</div><div class="item">5</div><div class="item">6</div>
        </div>
      </section>

      <section>
        <h2>place-content: space-between</h2>
        <p class="desc">El espacio sobrante se distribuye entre las filas y columnas.</p>
        <div class="grid-content between">
          <div class="item">1</div><div class="item">2</div><div class="item">3</div>
          <div class="item">4</div><div class="item">5</div><div class="item">6</div>
        </div>
      </section>

      <section>
        <h2>place-self: alineación individual por ítem</h2>
        <p class="desc">Ítems 1 (start), 5 (center) y 9 (end) sobrescriben la alineación del contenedor.</p>
        <div class="grid-items center grid-self">
          <div class="item item-ident">start</div><div class="item item-ident">2</div>
          <div class="item item-ident">3</div><div class="item item-ident">4</div>
          <div class="item item-ident">center</div><div class="item item-ident">6</div>
          <div class="item item-ident">7</div><div class="item item-ident">8</div>
          <div class="item item-ident">end</div><div class="item item-ident">10</div>
        </div>
      </section>
    </body>
    </html>
    ```

=== "CSS"

    ``` css
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      padding: 2rem;
      background: #f8f9fa;
    }
    section { margin-bottom: 3rem; }
    h2 { margin-bottom: 0.5rem; color: #212529; }
    .desc { color: #6c757d; margin-bottom: 1rem; }

    /*
     * place-items: alinea ítems dentro de sus celdas.
     * stretch (default): ítems se expanden al tamaño de la celda.
     * center: se centran y se encogen a su tamaño natural.
     * start/end: se alinean al borde de la celda.
     */
    .grid-items {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      grid-auto-rows: 150px;
      gap: 12px;
      background: #e9ecef;
      padding: 12px;
      border-radius: 8px;
    }

    .grid-items.start  { place-items: start; }
    .grid-items.center { place-items: center; }
    .grid-items.end    { place-items: end; }

    /*
     * place-content: posiciona la cuadrícula entera dentro
     * de un contenedor que es más grande que ella.
     * Valores: start, end, center, space-between, space-around, space-evenly.
     */
    .grid-content {
      display: grid;
      grid-template-columns: repeat(3, 150px);
      grid-template-rows: repeat(2, 100px);
      gap: 12px;
      background: #e9ecef;
      padding: 12px;
      border-radius: 8px;
      height: 300px;
    }

    .grid-content.center { place-content: center; }
    .grid-content.between { place-content: space-between; }

    /*
     * place-self: sobrescribe la alineación para un ítem concreto.
     * Muy útil cuando necesitas que un solo elemento se comporte
     * diferente al resto (por ejemplo, una imagen centrada en
     * un grid de tarjetas que usan stretch).
     */
    .grid-self .item:nth-child(1) { place-self: start; }
    .grid-self .item:nth-child(5) { place-self: center; }
    .grid-self .item:nth-child(9) { place-self: end; }

    .item {
      background: linear-gradient(135deg, #667eea, #764ba2);
      color: #fff;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 600;
      padding: 0.5rem;
    }

    .item-ident { width: 80px; height: 60px; }
    ```


### Ejemplo Guiado 6: Landing Page completa con Grid

Una landing page profesional construida íntegramente con CSS Grid. Incluye cabecera con navegación, héroe a dos columnas, sección de características con tarjetas responsivas, testimonios, llamada a la acción y pie de página. Todo el layout usa grid-template-areas para la estructura principal y repeat(auto-fit, minmax()) para las tarjetas.

=== "HTML"

    ``` html
    <!DOCTYPE html>
    <html lang="es">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Landing Page con CSS Grid</title>
      <link rel="stylesheet" href="./styles.css">
    </head>
    <body>
      <div class="landing">
        <header class="header">
          <div class="header__logo">TechFlow</div>
          <nav class="header__nav">
            <a href="#">Inicio</a>
            <a href="#">Servicios</a>
            <a href="#">Proyectos</a>
            <a href="#">Blog</a>
            <a href="#">Contacto</a>
          </nav>
          <button class="header__cta">Comenzar</button>
        </header>

        <section class="hero">
          <div class="hero__content">
            <h1>Transformamos ideas en experiencias digitales</h1>
            <p>Desarrollamos aplicaciones web modernas con las últimas tecnologías.</p>
            <div>
              <a href="#" class="btn btn--primario">Ver servicios</a>
              <a href="#" class="btn btn--secundario">Saber más</a>
            </div>
          </div>
          <div class="hero__image">Rocket</div>
        </section>

        <section class="features">
          <h2>Por que elegirnos?</h2>
          <p class="features__desc">Soluciones completas de desarrollo web adaptadas a tu negocio.</p>
          <div class="features__grid">
            <div class="feature-card">
              <span class="feature-card__icon">⚡</span>
              <h3>Rendimiento optimo</h3>
              <p>Aplicaciones ultrarrápidas optimizadas para buscadores y con carga instantánea.</p>
            </div>
            <div class="feature-card">
              <span class="feature-card__icon">🎨</span>
              <h3>Diseño personalizado</h3>
              <p>Interfaces únicas diseñadas a medida siguiendo tu identidad visual.</p>
            </div>
            <div class="feature-card">
              <span class="feature-card__icon">📱</span>
              <h3>100% responsive</h3>
              <p>Aplicaciones que se ven perfectas en cualquier dispositivo.</p>
            </div>
            <div class="feature-card">
              <span class="feature-card__icon">🔒</span>
              <h3>Seguridad garantizada</h3>
              <p>Implementamos las mejores prácticas de seguridad para proteger tus datos.</p>
            </div>
            <div class="feature-card">
              <span class="feature-card__icon">♿</span>
              <h3>Accesibilidad WCAG</h3>
              <p>Cumplimos estándares de accesibilidad para que tu web sea usable por todos.</p>
            </div>
            <div class="feature-card">
              <span class="feature-card__icon">🔄</span>
              <h3>Soporte continuo</h3>
              <p>Mantenimiento y actualizaciones periódicas para tu proyecto siempre al día.</p>
            </div>
          </div>
        </section>

        <section class="testimonials">
          <h2>Lo que dicen nuestros clientes</h2>
          <div class="testimonials__grid">
            <div class="testimonial">
              <p class="testimonial__text">"TechFlow transformó completamente nuestra presencia online. El diseño es espectacular."</p>
              <p class="testimonial__author">María García</p>
              <p class="testimonial__role">CEO de Innovatech</p>
            </div>
            <div class="testimonial">
              <p class="testimonial__text">"El equipo entendió nuestras necesidades desde el primer momento. Comunicación excelente."</p>
              <p class="testimonial__author">Carlos Ruiz</p>
              <p class="testimonial__role">Director de Marketing</p>
            </div>
            <div class="testimonial">
              <p class="testimonial__text">"Nuestra app se carga en milisegundos y la experiencia de usuario es inmejorable."</p>
              <p class="testimonial__author">Ana López</p>
              <p class="testimonial__role">CTO de DataCorp</p>
            </div>
          </div>
        </section>

        <section class="cta">
          <h2>Listo para empezar tu proyecto?</h2>
          <p>Contáctanos hoy y descubre cómo podemos ayudarte a alcanzar tus objetivos.</p>
          <a href="#" class="btn btn--primario" style="font-size:1.1rem; padding:1rem 2.5rem;">
            Solicitar presupuesto
          </a>
        </section>

        <footer class="footer">
          <div class="footer__col">
            <h4>TechFlow</h4>
            <p>Desarrollo web profesional desde 2018.</p>
            <p>Madrid, España</p>
          </div>
          <div class="footer__col">
            <h4>Servicios</h4>
            <a href="#">Desarrollo Web</a>
            <a href="#">Apps Móviles</a>
            <a href="#">Consultoría UX/UI</a>
            <a href="#">SEO Técnico</a>
          </div>
          <div class="footer__col">
            <h4>Empresa</h4>
            <a href="#">Sobre nosotros</a>
            <a href="#">Equipo</a>
            <a href="#">Blog</a>
            <a href="#">Contacto</a>
          </div>
          <div class="footer__col">
            <h4>Legal</h4>
            <a href="#">Aviso legal</a>
            <a href="#">Privacidad</a>
            <a href="#">Cookies</a>
          </div>
          <div class="footer__bottom">
            2025 TechFlow. Todos los derechos reservados.
          </div>
        </footer>
      </div>
    </body>
    </html>
    ```

=== "CSS"

    ``` css
    /* ===== RESET Y VARIABLES CSS ===== */
    * { margin: 0; padding: 0; box-sizing: border-box; }

    :root {
      --color-primario: #6c5ce7;
      --color-secundario: #a29bfe;
      --color-acento: #fd79a8;
      --color-oscuro: #2d3436;
      --color-claro: #dfe6e9;
      --color-blanco: #ffffff;
      --sombra: 0 4px 20px rgba(0, 0, 0, 0.08);
      --radio: 12px;
    }

    body {
      font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
      color: var(--color-oscuro);
      line-height: 1.6;
    }

    /*
     * ===== LAYOUT PRINCIPAL CON GRID =====
     * Usamos grid-template-areas para organizar las secciones.
     * Cada fila del layout es una sección:
     *   header, hero, features, testimonials, cta, footer.
     * Todas ocupan el ancho completo (1 columna).
     */
    .landing {
      display: grid;
      grid-template-columns: 1fr;
      grid-template-areas:
        "header"
        "hero"
        "features"
        "testimonials"
        "cta"
        "footer";
    }

    /* ===== CABECERA ===== */
    /*
     * La cabecera es a su vez un contenedor grid para alinear
     * logo, navegación y botón horizontalmente.
     */
    .header {
      grid-area: header;
      display: grid;
      grid-template-columns: auto 1fr auto;
      align-items: center;
      padding: 1rem 2rem;
      background: var(--color-blanco);
      box-shadow: var(--sombra);
      position: sticky;
      top: 0;
      z-index: 100;
    }

    .header__logo {
      font-size: 1.5rem;
      font-weight: 700;
      color: var(--color-primario);
    }

    .header__nav {
      display: flex;
      justify-content: center;
      gap: 2rem;
    }

    .header__nav a {
      text-decoration: none;
      color: var(--color-oscuro);
      font-weight: 500;
      transition: color 0.3s;
    }

    .header__nav a:hover { color: var(--color-primario); }

    .header__cta {
      background: var(--color-primario);
      color: var(--color-blanco);
      border: none;
      padding: 0.6rem 1.5rem;
      border-radius: 30px;
      font-weight: 600;
      cursor: pointer;
      transition: transform 0.2s, box-shadow 0.2s;
    }

    .header__cta:hover {
      transform: translateY(-2px);
      box-shadow: 0 4px 15px rgba(108, 92, 231, 0.4);
    }

    /* ===== HÉROE ===== */
    /*
     * El héroe usa un grid de 2 columnas:
     *   Col 1: texto (1fr) + Col 2: imagen decorativa (1fr)
     * En móvil (media query abajo) pasa a 1 sola columna.
     */
    .hero {
      grid-area: hero;
      display: grid;
      grid-template-columns: 1fr 1fr;
      align-items: center;
      gap: 3rem;
      padding: 5rem 2rem;
      background: linear-gradient(135deg, var(--color-primario), var(--color-secundario));
      color: var(--color-blanco);
      min-height: 500px;
    }

    .hero__content h1 {
      font-size: 3rem;
      line-height: 1.2;
      margin-bottom: 1.5rem;
    }

    .hero__content p {
      font-size: 1.2rem;
      opacity: 0.9;
      margin-bottom: 2rem;
    }

    .hero__image {
      background: rgba(255, 255, 255, 0.15);
      border-radius: var(--radio);
      height: 350px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 5rem;
    }

    .btn {
      display: inline-block;
      padding: 0.8rem 2rem;
      border-radius: 30px;
      font-weight: 600;
      text-decoration: none;
      cursor: pointer;
      transition: transform 0.2s;
    }

    .btn:hover { transform: translateY(-2px); }
    .btn--primario { background: var(--color-acento); color: var(--color-blanco); }
    .btn--secundario {
      background: transparent;
      color: var(--color-blanco);
      border: 2px solid var(--color-blanco);
      margin-left: 1rem;
    }

    /* ===== CARACTERÍSTICAS ===== */
    .features {
      grid-area: features;
      padding: 5rem 2rem;
      background: var(--color-blanco);
      text-align: center;
    }

    .features h2 { font-size: 2.2rem; margin-bottom: 1rem; }
    .features__desc {
      color: #636e72;
      max-width: 600px;
      margin: 0 auto 3rem;
    }

    /*
     * Grid de tarjetas responsivo sin media queries:
     * repeat(auto-fit, minmax(280px, 1fr))
     * Crea tantas columnas como quepan.
     * En desktop grande: 3 columnas.
     * En tablet: 2 columnas.
     * En móvil: 1 columna.
     * TODO automático gracias a auto-fit + minmax().
     */
    .features__grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 2rem;
      max-width: 1100px;
      margin: 0 auto;
    }

    .feature-card {
      padding: 2rem;
      border-radius: var(--radio);
      background: var(--color-blanco);
      box-shadow: var(--sombra);
      transition: transform 0.3s;
    }

    .feature-card:hover { transform: translateY(-5px); }
    .feature-card__icon { font-size: 2.5rem; margin-bottom: 1rem; display: block; }
    .feature-card h3 { margin-bottom: 0.8rem; }
    .feature-card p { color: #636e72; }

    /* ===== TESTIMONIOS ===== */
    .testimonials {
      grid-area: testimonials;
      padding: 5rem 2rem;
      background: #f8f9fa;
      text-align: center;
    }

    .testimonials h2 { font-size: 2.2rem; margin-bottom: 3rem; }

    .testimonials__grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 2rem;
      max-width: 1100px;
      margin: 0 auto;
    }

    .testimonial {
      background: var(--color-blanco);
      padding: 2rem;
      border-radius: var(--radio);
      box-shadow: var(--sombra);
    }

    .testimonial__text {
      font-style: italic;
      color: #636e72;
      margin-bottom: 1.5rem;
      font-size: 1.05rem;
    }

    .testimonial__author { font-weight: 600; color: var(--color-oscuro); }
    .testimonial__role { color: #b2bec3; font-size: 0.9rem; }

    /* ===== CTA (LLAMADA A LA ACCIÓN) ===== */
    .cta {
      grid-area: cta;
      display: grid;
      place-items: center;
      padding: 5rem 2rem;
      background: linear-gradient(135deg, var(--color-oscuro), #636e72);
      color: var(--color-blanco);
      text-align: center;
    }

    .cta h2 { font-size: 2.5rem; margin-bottom: 1rem; }
    .cta p { font-size: 1.2rem; opacity: 0.8; margin-bottom: 2rem; max-width: 500px; }

    /* ===== FOOTER ===== */
    .footer {
      grid-area: footer;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 3rem;
      padding: 4rem 2rem 2rem;
      background: var(--color-oscuro);
      color: var(--color-claro);
    }

    .footer__col h4 { color: var(--color-blanco); margin-bottom: 1rem; }
    .footer__col a {
      display: block;
      color: var(--color-claro);
      text-decoration: none;
      margin-bottom: 0.5rem;
      transition: color 0.3s;
    }

    .footer__col a:hover { color: var(--color-secundario); }

    .footer__bottom {
      grid-column: 1 / -1;
      text-align: center;
      padding-top: 2rem;
      border-top: 1px solid rgba(255, 255, 255, 0.1);
      font-size: 0.9rem;
      color: #636e72;
    }

    /* ===== RESPONSIVE ===== */
    @media (max-width: 768px) {
      .header {
        grid-template-columns: 1fr;
        gap: 0.5rem;
        text-align: center;
      }

      .header__nav { order: 3; gap: 1rem; flex-wrap: wrap; }

      .hero {
        grid-template-columns: 1fr;
        text-align: center;
        padding: 3rem 1.5rem;
      }

      .hero__image { height: 200px; }
      .hero__content h1 { font-size: 2rem; }
    }
    ```

### Ejemplo Guiado 7: Blog con Grid (posts destacados + sidebar + paginación)

Layout completo de un blog que combina post destacado a doble columna, grid de posts normales con auto-fill, sidebar con widgets, y paginación construida con grid. Demuestra cómo Grid puede gestionar layouts editoriales complejos.

=== "HTML"

    ``` html
    <!DOCTYPE html>
    <html lang="es">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Blog con CSS Grid</title>
      <link rel="stylesheet" href="./styles.css">
    </head>
    <body>
      <div class="blog">
        <header class="blog__header">
          <h1>TechBlog</h1>
          <p>Tecnología, desarrollo web y diseño de interfaces</p>
          <nav>
            <a href="#">Tecnología</a>
            <a href="#">Diseño</a>
            <a href="#">Desarrollo</a>
            <a href="#">Tutoriales</a>
            <a href="#">Podcast</a>
          </nav>
        </header>

        <main class="blog__main">
          <div class="posts">
            <!-- Post destacado: ocupa todo el ancho del área de posts -->
            <article class="post--featured">
              <div class="post__image">NEWS</div>
              <div class="post__content">
                <span class="post__category">Destacado</span>
                <h2 style="font-family:'Segoe UI',sans-serif; margin:0.5rem 0;">
                  CSS Grid: La guía definitiva para layouts modernos en 2025
                </h2>
                <p>Descubre cómo CSS Grid ha revolucionado la maquetación web.</p>
                <div class="post__meta">Por José Martínez · 15 min lectura · 12/05/2025</div>
              </div>
            </article>

            <!-- Grid de posts normales -->
            <div class="posts__grid">
              <article class="post">
                <div class="post__image">PC</div>
                <div class="post__content">
                  <span class="post__category">Desarrollo</span>
                  <h3>React 19: Novedades que debes conocer</h3>
                  <p>Exploramos las nuevas características de React 19.</p>
                  <div class="post__meta">10/05/2025 · 8 min</div>
                </div>
              </article>
              <article class="post">
                <div class="post__image">ART</div>
                <div class="post__content">
                  <span class="post__category">Diseño</span>
                  <h3>Design Tokens: Estandarizando tu sistema</h3>
                  <p>Aprende a implementar design tokens para consistencia visual.</p>
                  <div class="post__meta">08/05/2025 · 12 min</div>
                </div>
              </article>
              <article class="post">
                <div class="post__image">BOLT</div>
                <div class="post__content">
                  <span class="post__category">Rendimiento</span>
                  <h3>Optimización de Core Web Vitals</h3>
                  <p>Mejora la puntuación de tu web en los indicadores de Google.</p>
                  <div class="post__meta">05/05/2025 · 6 min</div>
                </div>
              </article>
              <article class="post">
                <div class="post__image">LOCK</div>
                <div class="post__content">
                  <span class="post__category">Seguridad</span>
                  <h3>Autenticación con Passkeys</h3>
                  <p>Implementa el nuevo estándar de autenticación biométrica.</p>
                  <div class="post__meta">01/05/2025 · 10 min</div>
                </div>
              </article>
            </div>

            <!-- Paginación con grid -->
            <nav class="pagination">
              <button class="pagination__btn pagination__btn--active">1</button>
              <button class="pagination__btn">2</button>
              <button class="pagination__btn">3</button>
              <button class="pagination__btn">4</button>
              <button class="pagination__btn">Siguiente →</button>
            </nav>
          </div>

          <aside class="sidebar">
            <div class="sidebar__widget">
              <h4>Sobre el autor</h4>
              <p>José Martínez, desarrollador web y profesor de FP en Andalucía.</p>
            </div>
            <div class="sidebar__widget">
              <h4>Categorías</h4>
              <ul>
                <li><a href="#">Desarrollo Web (24)</a></li>
                <li><a href="#">Diseño UX/UI (18)</a></li>
                <li><a href="#">CSS y Maquetación (15)</a></li>
                <li><a href="#">JavaScript (32)</a></li>
                <li><a href="#">Accesibilidad (8)</a></li>
              </ul>
            </div>
            <div class="sidebar__widget">
              <h4>Etiquetas</h4>
              <div class="sidebar__tag-cloud">
                <span class="tag">CSS Grid</span>
                <span class="tag">Flexbox</span>
                <span class="tag">React</span>
                <span class="tag">Node.js</span>
                <span class="tag">TypeScript</span>
                <span class="tag">Figma</span>
                <span class="tag">WCAG</span>
              </div>
            </div>
          </aside>
        </main>

        <footer class="blog__footer">
          2025 TechBlog. Desarrollado con CSS Grid.
        </footer>
      </div>
    </body>
    </html>
    ```

=== "CSS"

    ``` css
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: 'Georgia', 'Times New Roman', serif;
      background: #fafafa;
      color: #333;
      line-height: 1.7;
    }

    /*
     * Layout de 3 columnas con márgenes laterales.
     * La columna central (2/3) contiene contenido + sidebar.
     */
    .blog { display: grid; grid-template-columns: 1fr minmax(0, 1100px) 1fr; }

    .blog__header {
      grid-column: 1 / -1;
      background: #1a1a2e;
      color: #fff;
      padding: 2rem;
      text-align: center;
    }

    .blog__header h1 { font-family: 'Segoe UI', sans-serif; font-size: 2.5rem; }
    .blog__header nav {
      margin-top: 1.5rem;
      display: flex;
      justify-content: center;
      gap: 2rem;
    }
    .blog__header nav a { color: #ccc; text-decoration: none; transition: color 0.3s; }
    .blog__header nav a:hover { color: #fff; }

    /*
     * Contenedor principal: contenido (2fr) + sidebar (1fr)
     * 2fr + 1fr = 3 partes. Contenido ocupa 2/3, sidebar 1/3.
     */
    .blog__main {
      grid-column: 2 / 3;
      display: grid;
      grid-template-columns: 2fr 1fr;
      gap: 3rem;
      padding: 3rem 0;
    }

    .posts { display: grid; gap: 2rem; }

    /*
     * POST DESTACADO: ocupa 2 columnas (todo el ancho del área de posts)
     * Internamente usa otro grid: imagen a la izquierda + texto a la derecha.
     */
    .post--featured {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1.5rem;
      background: #fff;
      border-radius: 12px;
      overflow: hidden;
      box-shadow: 0 2px 12px rgba(0, 0, 0, 0.06);
      grid-column: 1 / -1;
    }

    .post--featured .post__image {
      background: linear-gradient(135deg, #667eea, #764ba2);
      min-height: 250px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #fff;
      font-size: 4rem;
    }

    .post--featured .post__content {
      padding: 1.5rem;
      display: flex;
      flex-direction: column;
      justify-content: center;
    }

    /* Grid de posts normales con auto-fill para responsividad automática */
    .posts__grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 1.5rem;
    }

    .post {
      background: #fff;
      border-radius: 12px;
      overflow: hidden;
      box-shadow: 0 2px 12px rgba(0, 0, 0, 0.06);
      transition: transform 0.3s;
    }

    .post:hover { transform: translateY(-4px); }
    .post__image {
      background: #dfe6e9;
      height: 180px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 3rem;
      color: #636e72;
    }

    .post__content { padding: 1.5rem; }
    .post__category {
      display: inline-block;
      background: #6c5ce7;
      color: #fff;
      padding: 0.25rem 0.75rem;
      border-radius: 20px;
      font-size: 0.75rem;
      font-family: 'Segoe UI', sans-serif;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 0.5rem;
    }

    .post h3 { margin: 0.5rem 0; font-size: 1.2rem; font-family: 'Segoe UI', sans-serif; }
    .post p { color: #636e72; font-size: 0.95rem; }
    .post__meta {
      margin-top: 1rem;
      font-size: 0.85rem;
      color: #b2bec3;
      font-family: 'Segoe UI', sans-serif;
    }

    /* Paginación: grid-auto-flow: column para botones en fila */
    .pagination {
      display: grid;
      grid-auto-flow: column;
      justify-content: center;
      gap: 0.5rem;
      margin-top: 2rem;
    }

    .pagination__btn {
      padding: 0.5rem 1rem;
      background: #fff;
      border: 1px solid #dfe6e9;
      border-radius: 6px;
      cursor: pointer;
      font-family: 'Segoe UI', sans-serif;
      transition: all 0.2s;
    }

    .pagination__btn:hover { background: #6c5ce7; color: #fff; border-color: #6c5ce7; }
    .pagination__btn--active { background: #6c5ce7; color: #fff; border-color: #6c5ce7; }

    /* Sidebar */
    .sidebar { display: grid; gap: 1.5rem; align-content: start; }
    .sidebar__widget {
      background: #fff;
      padding: 1.5rem;
      border-radius: 12px;
      box-shadow: 0 2px 12px rgba(0, 0, 0, 0.06);
    }

    .sidebar__widget h4 {
      font-family: 'Segoe UI', sans-serif;
      margin-bottom: 1rem;
      padding-bottom: 0.5rem;
      border-bottom: 2px solid #6c5ce7;
    }

    .sidebar__widget ul { list-style: none; }
    .sidebar__widget li { padding: 0.5rem 0; border-bottom: 1px solid #f0f0f0; }
    .sidebar__widget li a { color: #333; text-decoration: none; transition: color 0.3s; }
    .sidebar__widget li a:hover { color: #6c5ce7; }

    .sidebar__tag-cloud { display: flex; flex-wrap: wrap; gap: 0.5rem; }
    .tag {
      background: #f0f0f0;
      padding: 0.3rem 0.75rem;
      border-radius: 20px;
      font-size: 0.85rem;
      font-family: 'Segoe UI', sans-serif;
      transition: background 0.3s;
    }
    .tag:hover { background: #6c5ce7; color: #fff; }

    .blog__footer {
      grid-column: 1 / -1;
      background: #1a1a2e;
      color: #ccc;
      text-align: center;
      padding: 2rem;
      font-family: 'Segoe UI', sans-serif;
    }

    /* En móvil, contenido y sidebar se apilan en una columna */
    @media (max-width: 900px) {
      .blog__main { grid-template-columns: 1fr; padding: 2rem 1rem; }
      .post--featured { grid-template-columns: 1fr; }
      .blog__header h1 { font-size: 1.8rem; }
      .blog__header nav { flex-direction: column; gap: 0.5rem; }
    }
    ```


### Ejemplo Guiado 8: Ecommerce con Grid de productos y filtros laterales

Tienda online completa con Grid que incluye cabecera con búsqueda, sidebar de filtros, grid de productos con tarjeta destacada (ocupa doble columna), y diseño totalmente responsive. Demuestra cómo Grid maneja layouts complejos de comercio electrónico con diferentes tamaños de tarjeta.

=== "HTML"

    ``` html
    <!DOCTYPE html>
    <html lang="es">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Ecommerce con Grid</title>
      <link rel="stylesheet" href="./styles.css">
    </head>
    <body>
      <header class="header">
        <div class="header__logo">ShopGrid</div>
        <div class="header__search">
          <input type="text" placeholder="Buscar productos...">
        </div>
        <div class="header__icons">
          <span>Usuario</span>
          <span>Fav</span>
          <span>Carrito (3)</span>
        </div>
      </header>

      <div class="shop">
        <!-- Filtros laterales -->
        <aside class="filters">
          <h3>Filtros</h3>
          <div class="filter-group">
            <h4>Categoría</h4>
            <label><input type="checkbox" checked> Electrónica</label>
            <label><input type="checkbox"> Ropa</label>
            <label><input type="checkbox"> Hogar</label>
            <label><input type="checkbox"> Deportes</label>
          </div>
          <div class="filter-group">
            <h4>Precio</h4>
            <div class="price-range">
              <input type="number" placeholder="Min" value="10">
              <span>-</span>
              <input type="number" placeholder="Max" value="500">
            </div>
          </div>
          <div class="filter-group">
            <h4>Valoración</h4>
            <label><input type="checkbox"> 4 estrellas o más</label>
            <label><input type="checkbox"> 3 estrellas o más</label>
            <label><input type="checkbox"> 2 estrellas o más</label>
          </div>
          <button class="btn-filtrar">Aplicar filtros</button>
        </aside>

        <!-- Grid de productos -->
        <main>
          <div class="products-header">
            <h2>Todos los productos (24)</h2>
            <select class="sort-select">
              <option>Más relevantes</option>
              <option>Precio: menor a mayor</option>
              <option>Precio: mayor a menor</option>
              <option>Mejor valorados</option>
            </select>
          </div>

          <div class="products-grid">
            <!-- Producto destacado (2 columnas) -->
            <article class="product-card product-card--featured">
              <div class="product-card__image">
                PHONE
                <span class="product-card__badge">-30%</span>
              </div>
              <div class="product-card__info">
                <span class="product-card__category">Electrónica</span>
                <h3 class="product-card__title">Smartphone Pro X5 - 256GB - Negro</h3>
                <div class="product-card__rating">4 estrellas (128)</div>
                <p style="color:#636e72; margin:0.5rem 0 1rem; font-size:0.9rem;">
                  Pantalla AMOLED 6.7", procesador 8 núcleos, cámara 108MP.
                </p>
                <div>
                  <span class="product-card__price">699 EUR</span>
                  <span class="product-card__price--old">999 EUR</span>
                </div>
                <button class="product-card__btn" style="margin-top:1rem; width:auto; border-radius:25px; padding:0.5rem 1.5rem;">
                  Añadir al carrito
                </button>
              </div>
            </article>

            <!-- Productos normales -->
            <article class="product-card">
              <div class="product-card__image">LAPTOP<span class="product-card__badge">Nuevo</span></div>
              <div class="product-card__info">
                <span class="product-card__category">Electrónica</span>
                <h3 class="product-card__title">Portátil UltraBook 15" i7 16GB</h3>
                <div class="product-card__rating">5 estrellas (56)</div>
              </div>
              <div class="product-card__footer">
                <span class="product-card__price">1199 EUR</span>
                <button class="product-card__btn">+</button>
              </div>
            </article>

            <article class="product-card">
              <div class="product-card__image">HEADPHONES</div>
              <div class="product-card__info">
                <span class="product-card__category">Audio</span>
                <h3 class="product-card__title">Auriculares BT ANC Premium</h3>
                <div class="product-card__rating">4 estrellas (342)</div>
              </div>
              <div class="product-card__footer">
                <span><span class="product-card__price">89 EUR</span><span class="product-card__price--old">129 EUR</span></span>
                <button class="product-card__btn">+</button>
              </div>
            </article>

            <article class="product-card">
              <div class="product-card__image">WATCH</div>
              <div class="product-card__info">
                <span class="product-card__category">Wearables</span>
                <h3 class="product-card__title">Smartwatch Deportivo GPS</h3>
                <div class="product-card__rating">4 estrellas (89)</div>
              </div>
              <div class="product-card__footer">
                <span class="product-card__price">199 EUR</span>
                <button class="product-card__btn">+</button>
              </div>
            </article>

            <article class="product-card">
              <div class="product-card__image">CAMERA</div>
              <div class="product-card__info">
                <span class="product-card__category">Fotografía</span>
                <h3 class="product-card__title">Cámara Mirrorless 24MP</h3>
                <div class="product-card__rating">5 estrellas (45)</div>
              </div>
              <div class="product-card__footer">
                <span class="product-card__price">849 EUR</span>
                <button class="product-card__btn">+</button>
              </div>
            </article>

            <article class="product-card">
              <div class="product-card__image">PRINTER</div>
              <div class="product-card__info">
                <span class="product-card__category">Oficina</span>
                <h3 class="product-card__title">Impresora Multifunción WiFi</h3>
                <div class="product-card__rating">3 estrellas (23)</div>
              </div>
              <div class="product-card__footer">
                <span><span class="product-card__price">149 EUR</span><span class="product-card__price--old">179 EUR</span></span>
                <button class="product-card__btn">+</button>
              </div>
            </article>

            <article class="product-card">
              <div class="product-card__image">KEYBOARD</div>
              <div class="product-card__info">
                <span class="product-card__category">Gaming</span>
                <h3 class="product-card__title">Teclado Mecánico RGB</h3>
                <div class="product-card__rating">5 estrellas (210)</div>
              </div>
              <div class="product-card__footer">
                <span class="product-card__price">79 EUR</span>
                <button class="product-card__btn">+</button>
              </div>
            </article>

            <article class="product-card">
              <div class="product-card__image">MONITOR</div>
              <div class="product-card__info">
                <span class="product-card__category">Monitores</span>
                <h3 class="product-card__title">Monitor 4K 27" IPS HDR10</h3>
                <div class="product-card__rating">4 estrellas (67)</div>
              </div>
              <div class="product-card__footer">
                <span class="product-card__price">449 EUR</span>
                <button class="product-card__btn">+</button>
              </div>
            </article>
          </div>
        </main>
      </div>
    </body>
    </html>
    ```

=== "CSS"

    ``` css
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      background: #f5f6fa;
      color: #2d3436;
    }

    /* Cabecera del ecommerce con grid: logo, búsqueda, iconos */
    .header {
      display: grid;
      grid-template-columns: auto 1fr auto auto;
      align-items: center;
      gap: 1.5rem;
      padding: 1rem 2rem;
      background: #fff;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
      position: sticky;
      top: 0;
      z-index: 100;
    }

    .header__logo { font-size: 1.5rem; font-weight: 700; color: #e17055; }
    .header__search { position: relative; max-width: 500px; }
    .header__search input {
      width: 100%;
      padding: 0.6rem 1rem 0.6rem 2.5rem;
      border: 1px solid #dfe6e9;
      border-radius: 25px;
      font-size: 0.95rem;
      outline: none;
      transition: border-color 0.3s;
    }
    .header__search input:focus { border-color: #e17055; }
    .header__icons { display: flex; gap: 1.5rem; font-size: 1.3rem; cursor: pointer; }

    /*
     * Layout principal: sidebar de filtros (250px fijos) + grid de productos (1fr).
     * 1fr permite que la zona de productos ocupe todo el espacio restante.
     */
    .shop {
      display: grid;
      grid-template-columns: 250px 1fr;
      gap: 2rem;
      padding: 2rem;
      max-width: 1300px;
      margin: 0 auto;
    }

    /* Sidebar de filtros con position sticky para seguir el scroll */
    .filters {
      background: #fff;
      padding: 1.5rem;
      border-radius: 12px;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
      height: fit-content;
      position: sticky;
      top: 90px;
    }

    .filters h3 { margin-bottom: 1.5rem; font-size: 1.1rem; }
    .filter-group {
      margin-bottom: 1.5rem;
      padding-bottom: 1.5rem;
      border-bottom: 1px solid #f0f0f0;
    }

    .filter-group h4 {
      margin-bottom: 0.75rem;
      font-size: 0.9rem;
      text-transform: uppercase;
      color: #636e72;
      letter-spacing: 0.5px;
    }

    .filter-group label {
      display: block;
      padding: 0.3rem 0;
      cursor: pointer;
      font-size: 0.95rem;
    }

    .filter-group input[type="checkbox"] { margin-right: 0.5rem; }

    .price-range {
      display: grid;
      grid-template-columns: 1fr auto 1fr;
      gap: 0.5rem;
      align-items: center;
    }

    .price-range input {
      width: 100%;
      padding: 0.4rem;
      border: 1px solid #dfe6e9;
      border-radius: 6px;
    }

    .btn-filtrar {
      width: 100%;
      padding: 0.7rem;
      background: #e17055;
      color: #fff;
      border: none;
      border-radius: 8px;
      font-weight: 600;
      cursor: pointer;
      transition: background 0.3s;
    }
    .btn-filtrar:hover { background: #d35400; }

    .products-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 1.5rem;
    }

    .sort-select {
      padding: 0.5rem 1rem;
      border: 1px solid #dfe6e9;
      border-radius: 8px;
      font-family: 'Segoe UI', sans-serif;
    }

    /*
     * Grid de productos con auto-fill:
     * Cada tarjeta mide mínimo 260px.
     * En desktop 1920px: caben ~5 columnas.
     * En desktop 1440px: caben ~4 columnas.
     * En tablet 768px: caben ~2 columnas.
     * En móvil: 1 columna.
     * TODO automático sin media queries.
     */
    .products-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
      gap: 1.5rem;
    }

    /* Tarjeta de producto con grid interno para estructura vertical */
    .product-card {
      background: #fff;
      border-radius: 12px;
      overflow: hidden;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
      transition: transform 0.3s, box-shadow 0.3s;
      display: grid;
      grid-template-rows: 220px auto auto auto;
    }

    .product-card:hover { transform: translateY(-4px); box-shadow: 0 8px 25px rgba(0,0,0,0.1); }

    .product-card__image {
      background: linear-gradient(135deg, #dfe6e9, #b2bec3);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 4rem;
      position: relative;
    }

    .product-card__badge {
      position: absolute;
      top: 10px;
      left: 10px;
      background: #e17055;
      color: #fff;
      padding: 0.25rem 0.75rem;
      border-radius: 20px;
      font-size: 0.75rem;
      font-weight: 600;
    }

    .product-card__info { padding: 1rem; }
    .product-card__category {
      color: #636e72;
      font-size: 0.8rem;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    .product-card__title { margin: 0.3rem 0; font-size: 1rem; font-weight: 600; }
    .product-card__rating { color: #f9ca24; font-size: 0.9rem; }

    .product-card__footer {
      display: grid;
      grid-template-columns: 1fr auto;
      align-items: center;
      padding: 0 1rem 1rem;
    }

    .product-card__price { font-size: 1.2rem; font-weight: 700; color: #2d3436; }
    .product-card__price--old {
      font-size: 0.85rem;
      color: #b2bec3;
      text-decoration: line-through;
      margin-left: 0.5rem;
    }

    .product-card__btn {
      background: #e17055;
      color: #fff;
      border: none;
      width: 40px;
      height: 40px;
      border-radius: 50%;
      font-size: 1.2rem;
      cursor: pointer;
      display: grid;
      place-items: center;
      transition: transform 0.2s;
    }
    .product-card__btn:hover { transform: scale(1.1); }

    /*
     * PRODUCTO DESTACADO: ocupa 2 columnas
     * Internamente usa grid horizontal (imagen | info).
     */
    .product-card--featured {
      grid-column: span 2;
      grid-template-columns: 1fr 1fr;
      grid-template-rows: auto;
    }

    .product-card--featured .product-card__image { height: 100%; }
    .product-card--featured .product-card__info { padding: 1.5rem; }
    .product-card--featured .product-card__title { font-size: 1.3rem; }
    .product-card--featured .product-card__price { font-size: 1.5rem; }

    /* Responsive: filtros encima de productos en tablet */
    @media (max-width: 900px) {
      .shop { grid-template-columns: 1fr; padding: 1rem; }
      .filters { position: static; }
      .product-card--featured { grid-column: span 1; grid-template-columns: 1fr; grid-template-rows: 200px auto; }
    }

    @media (max-width: 600px) {
      .header { grid-template-columns: 1fr auto; gap: 0.5rem; padding: 0.75rem 1rem; }
      .header__search { grid-column: 1 / -1; order: 3; }
    }
    ```

### Ejemplo Guiado 9: Dashboard profesional con Grid

Un dashboard de administración profesional que utiliza Grid tanto para el layout principal (sidebar + header + contenido) como para la disposición de widgets de diferentes tamaños. Incluye tarjetas de estadísticas, gráfico de barras, lista de actividad reciente y panel de tareas.

=== "HTML"

    ``` html
    <!DOCTYPE html>
    <html lang="es">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Dashboard Profesional con Grid</title>
      <link rel="stylesheet" href="./styles.css">
    </head>
    <body>
      <div class="dashboard">
        <aside class="sidebar">
          <div class="sidebar__logo">DashGrid</div>
          <nav class="sidebar__nav">
            <a href="#" class="sidebar__link sidebar__link--active">Dashboard</a>
            <a href="#" class="sidebar__link">Analiticas</a>
            <a href="#" class="sidebar__link">Usuarios</a>
            <a href="#" class="sidebar__link">Productos</a>
            <a href="#" class="sidebar__link">Pedidos</a>
            <span class="sidebar__section">Configuracion</span>
            <a href="#" class="sidebar__link">Ajustes</a>
            <a href="#" class="sidebar__link">Seguridad</a>
            <a href="#" class="sidebar__link">Ayuda</a>
          </nav>
        </aside>

        <header class="header">
          <div class="header__search">
            <input type="text" placeholder="Buscar en el dashboard...">
          </div>
          <div class="header__actions">
            <span>Notif</span>
            <span>Chat</span>
          </div>
          <div class="header__user">
            <span>María González</span>
            <div class="header__avatar">MG</div>
          </div>
        </header>

        <main class="main">
          <h1 class="main__title">Dashboard</h1>

          <div class="widgets">
            <!-- 4 widgets de estadísticas (1 columna cada uno) -->
            <div class="widget widget--stat">
              <div class="widget__header">
                <span class="widget__title">Ingresos Totales</span>
                <span>💰</span>
              </div>
              <div>
                <div class="widget__value">45231 EUR</div>
                <div class="widget__change widget__change--up">+12.5% vs mes anterior</div>
              </div>
            </div>

            <div class="widget widget--stat">
              <div class="widget__header">
                <span class="widget__title">Usuarios Activos</span>
                <span>👥</span>
              </div>
              <div>
                <div class="widget__value">2847</div>
                <div class="widget__change widget__change--up">+8.2% vs mes anterior</div>
              </div>
            </div>

            <div class="widget widget--stat">
              <div class="widget__header">
                <span class="widget__title">Ventas</span>
                <span>🛒</span>
              </div>
              <div>
                <div class="widget__value">1230</div>
                <div class="widget__change widget__change--down">-3.1% vs mes anterior</div>
              </div>
            </div>

            <div class="widget widget--stat">
              <div class="widget__header">
                <span class="widget__title">Conversion</span>
                <span>📈</span>
              </div>
              <div>
                <div class="widget__value">3.24%</div>
                <div class="widget__change widget__change--up">+0.8% vs mes anterior</div>
              </div>
            </div>

            <!-- Gráfico de barras (2 columnas) -->
            <div class="widget widget--wide">
              <div class="widget__header">
                <span class="widget__title">Ingresos Semanales</span>
                <span>📊</span>
              </div>
              <div class="chart-bars">
                <div class="chart-bar" style="height:60%"></div>
                <div class="chart-bar" style="height:80%"></div>
                <div class="chart-bar" style="height:45%"></div>
                <div class="chart-bar" style="height:90%"></div>
                <div class="chart-bar" style="height:70%"></div>
                <div class="chart-bar" style="height:55%"></div>
                <div class="chart-bar" style="height:95%"></div>
              </div>
              <div style="display:grid; grid-template-columns:repeat(7,1fr); gap:0.5rem; margin-top:0.5rem; color:var(--color-muted); font-size:0.75rem;">
                <span>L</span><span>M</span><span>X</span><span>J</span><span>V</span><span>S</span><span>D</span>
              </div>
            </div>

            <!-- Actividad reciente (2 columnas) -->
            <div class="widget widget--wide">
              <div class="widget__header">
                <span class="widget__title">Actividad Reciente</span>
                <span>📋</span>
              </div>
              <div class="activity-list">
                <div class="activity-item">
                  <div class="activity-dot"></div>
                  <div>
                    <strong>Nuevo pedido #45892</strong>
                    <div style="color:var(--color-muted);font-size:0.85rem;">Cliente: Juan Pérez - 2 productos</div>
                  </div>
                  <span class="activity-time">Hace 5 min</span>
                </div>
                <div class="activity-item">
                  <div class="activity-dot"></div>
                  <div>
                    <strong>Usuario registrado</strong>
                    <div style="color:var(--color-muted);font-size:0.85rem;">ana.lopez@email.com</div>
                  </div>
                  <span class="activity-time">Hace 12 min</span>
                </div>
                <div class="activity-item">
                  <div class="activity-dot"></div>
                  <div>
                    <strong>Pago confirmado #45890</strong>
                    <div style="color:var(--color-muted);font-size:0.85rem;">Importe: 156,50 EUR</div>
                  </div>
                  <span class="activity-time">Hace 28 min</span>
                </div>
                <div class="activity-item">
                  <div class="activity-dot"></div>
                  <div>
                    <strong>Soporte: ticket #1243 cerrado</strong>
                    <div style="color:var(--color-muted);font-size:0.85rem;">Técnico: Carlos Ruiz</div>
                  </div>
                  <span class="activity-time">Hace 1 hora</span>
                </div>
              </div>
            </div>

            <!-- Tareas (1 columna) -->
            <div class="widget">
              <div class="widget__header">
                <span class="widget__title">Tareas Pendientes</span>
                <span>✅</span>
              </div>
              <div class="task-list">
                <div class="task-item">
                  <div class="task-status task-status--done"></div>
                  <span style="text-decoration:line-through;color:var(--color-muted);">Revisar informe</span>
                  <span class="task-badge task-badge--done">Hecho</span>
                </div>
                <div class="task-item">
                  <div class="task-status task-status--pending"></div>
                  <span>Actualizar catálogo</span>
                  <span class="task-badge task-badge--pending">En curso</span>
                </div>
                <div class="task-item">
                  <div class="task-status task-status--urgent"></div>
                  <span>Corregir bug checkout</span>
                  <span class="task-badge task-badge--urgent">Urgente</span>
                </div>
                <div class="task-item">
                  <div class="task-status task-status--pending"></div>
                  <span>Preparar presentación Q3</span>
                  <span class="task-badge task-badge--pending">Pendiente</span>
                </div>
              </div>
            </div>

            <!-- Objetivos (1 columna) -->
            <div class="widget">
              <div class="widget__header">
                <span class="widget__title">Objetivos Mensuales</span>
                <span>🎯</span>
              </div>
              <div style="display:grid; gap:1rem; margin-top:0.5rem;">
                <div>
                  <div style="display:flex; justify-content:space-between; margin-bottom:0.25rem;">
                    <span style="font-size:0.85rem;">Ventas</span>
                    <span style="font-size:0.85rem;">85%</span>
                  </div>
                  <div style="background:var(--color-border); border-radius:4px; height:8px;">
                    <div style="background:var(--color-primary); width:85%; height:100%; border-radius:4px;"></div>
                  </div>
                </div>
                <div>
                  <div style="display:flex; justify-content:space-between; margin-bottom:0.25rem;">
                    <span style="font-size:0.85rem;">Usuarios nuevos</span>
                    <span style="font-size:0.85rem;">62%</span>
                  </div>
                  <div style="background:var(--color-border); border-radius:4px; height:8px;">
                    <div style="background:var(--color-success); width:62%; height:100%; border-radius:4px;"></div>
                  </div>
                </div>
                <div>
                  <div style="display:flex; justify-content:space-between; margin-bottom:0.25rem;">
                    <span style="font-size:0.85rem;">Soporte resuelto</span>
                    <span style="font-size:0.85rem;">94%</span>
                  </div>
                  <div style="background:var(--color-border); border-radius:4px; height:8px;">
                    <div style="background:var(--color-warning); width:94%; height:100%; border-radius:4px;"></div>
                  </div>
                </div>
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
    * { margin: 0; padding: 0; box-sizing: border-box; }

    :root {
      --sidebar-width: 240px;
      --header-height: 60px;
      --color-bg: #0f172a;
      --color-sidebar: #1e293b;
      --color-card: #1e293b;
      --color-primary: #3b82f6;
      --color-success: #10b981;
      --color-warning: #f59e0b;
      --color-danger: #ef4444;
      --color-text: #e2e8f0;
      --color-muted: #94a3b8;
      --color-border: #334155;
    }

    body {
      font-family: 'Inter', 'Segoe UI', system-ui, sans-serif;
      background: var(--color-bg);
      color: var(--color-text);
      min-height: 100vh;
    }

    /*
     * ===== LAYOUT PRINCIPAL =====
     * 2 columnas: sidebar fija (240px) + contenido flexible (1fr).
     * 2 filas: header (60px) + resto (1fr).
     * grid-template-areas define las zonas del dashboard.
     */
    .dashboard {
      display: grid;
      grid-template-columns: var(--sidebar-width) 1fr;
      grid-template-rows: var(--header-height) 1fr;
      grid-template-areas:
        "sidebar header"
        "sidebar main";
      min-height: 100vh;
    }

    /* ===== SIDEBAR ===== */
    .sidebar {
      grid-area: sidebar;
      background: var(--color-sidebar);
      border-right: 1px solid var(--color-border);
      display: flex;
      flex-direction: column;
      padding: 1.5rem 0;
    }

    .sidebar__logo {
      padding: 0 1.5rem 1.5rem;
      border-bottom: 1px solid var(--color-border);
      margin-bottom: 1.5rem;
      font-size: 1.3rem;
      font-weight: 700;
      color: var(--color-primary);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .sidebar__nav { display: flex; flex-direction: column; padding: 0 0.75rem; flex: 1; }

    .sidebar__link {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      padding: 0.6rem 0.75rem;
      border-radius: 8px;
      color: var(--color-muted);
      text-decoration: none;
      transition: all 0.2s;
      margin-bottom: 0.25rem;
    }

    .sidebar__link:hover,
    .sidebar__link--active {
      background: rgba(59, 130, 246, 0.1);
      color: var(--color-primary);
    }

    .sidebar__section {
      font-size: 0.7rem;
      text-transform: uppercase;
      letter-spacing: 1px;
      color: var(--color-muted);
      padding: 1rem 0.75rem 0.5rem;
    }

    /* ===== HEADER ===== */
    .header {
      grid-area: header;
      background: var(--color-sidebar);
      border-bottom: 1px solid var(--color-border);
      display: grid;
      grid-template-columns: 1fr auto auto;
      align-items: center;
      padding: 0 2rem;
      gap: 1rem;
    }

    .header__search input {
      background: var(--color-bg);
      border: 1px solid var(--color-border);
      padding: 0.5rem 1rem;
      border-radius: 8px;
      color: var(--color-text);
      width: 300px;
      outline: none;
    }

    .header__search input:focus { border-color: var(--color-primary); }
    .header__actions { display: flex; gap: 1rem; align-items: center; color: var(--color-muted); cursor: pointer; }
    .header__user { display: flex; align-items: center; gap: 0.5rem; cursor: pointer; }

    .header__avatar {
      width: 36px;
      height: 36px;
      background: var(--color-primary);
      border-radius: 50%;
      display: grid;
      place-items: center;
      font-weight: 600;
    }

    /* ===== CONTENIDO PRINCIPAL ===== */
    .main {
      grid-area: main;
      padding: 1.5rem 2rem;
      overflow-y: auto;
    }

    .main__title { font-size: 1.3rem; margin-bottom: 1.5rem; }

    /*
     * ===== GRID DE WIDGETS =====
     * 4 columnas iguales para los widgets.
     * Cada widget puede ocupar 1 o 2 columnas según su importancia.
     */
    .widgets {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      grid-auto-rows: minmax(150px, auto);
      gap: 1.25rem;
    }

    .widget {
      background: var(--color-card);
      border: 1px solid var(--color-border);
      border-radius: 12px;
      padding: 1.25rem;
    }

    .widget__header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 1rem;
    }

    .widget__title {
      font-size: 0.85rem;
      color: var(--color-muted);
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    /* Widgets de estadísticas (1 columna cada uno) */
    .widget--stat { display: flex; flex-direction: column; justify-content: space-between; }
    .widget--stat .widget__value { font-size: 2rem; font-weight: 700; }
    .widget--stat .widget__change { font-size: 0.85rem; margin-top: 0.25rem; }
    .widget__change--up { color: var(--color-success); }
    .widget__change--down { color: var(--color-danger); }

    /* Widget ancho: 2 columnas */
    .widget--wide { grid-column: span 2; }

    /* Gráfico de barras */
    .chart-bars {
      display: grid;
      grid-template-columns: repeat(7, 1fr);
      gap: 0.5rem;
      align-items: end;
      height: 150px;
    }

    .chart-bar {
      background: var(--color-primary);
      border-radius: 4px 4px 0 0;
      transition: height 0.5s;
    }

    /* Lista de actividad */
    .activity-list { display: grid; gap: 0.75rem; }
    .activity-item {
      display: grid;
      grid-template-columns: auto 1fr auto;
      gap: 0.75rem;
      align-items: center;
      padding-bottom: 0.75rem;
      border-bottom: 1px solid var(--color-border);
    }

    .activity-dot {
      width: 8px;
      height: 8px;
      background: var(--color-primary);
      border-radius: 50%;
    }

    .activity-time { color: var(--color-muted); font-size: 0.8rem; }

    /* Lista de tareas */
    .task-list { display: grid; gap: 0.5rem; }
    .task-item {
      display: grid;
      grid-template-columns: auto 1fr auto;
      gap: 0.75rem;
      align-items: center;
    }

    .task-status { width: 10px; height: 10px; border-radius: 50%; }
    .task-status--done { background: var(--color-success); }
    .task-status--pending { background: var(--color-warning); }
    .task-status--urgent { background: var(--color-danger); }

    .task-badge {
      font-size: 0.7rem;
      padding: 0.2rem 0.5rem;
      border-radius: 4px;
      text-transform: uppercase;
    }

    .task-badge--done { background: rgba(16,185,129,0.1); color: var(--color-success); }
    .task-badge--pending { background: rgba(245,158,11,0.1); color: var(--color-warning); }
    .task-badge--urgent { background: rgba(239,68,68,0.1); color: var(--color-danger); }

    /* Responsive: sidebar se oculta en tablet */
    @media (max-width: 1024px) {
      .dashboard {
        grid-template-columns: 1fr;
        grid-template-rows: var(--header-height) 1fr;
        grid-template-areas: "header" "main";
      }
      .sidebar { display: none; }
      .widgets { grid-template-columns: repeat(2, 1fr); }
      .widget--wide { grid-column: span 2; }
    }

    @media (max-width: 640px) {
      .widgets { grid-template-columns: 1fr; }
      .widget--wide { grid-column: span 1; }
      .header { grid-template-columns: 1fr auto; }
      .header__search { display: none; }
    }
    ```


### Ejemplo Guiado 10: Galería avanzada tipo masonry con Grid, overlays y filtros

Una galería de imágenes profesional que simula el efecto masonry (pared de ladrillos) usando diferentes tamaños de celda. Incluye overlays con información al hacer hover, filtros por categoría, y una segunda versión usando grid-auto-flow: dense para compactar automáticamente. Demuestra cómo Grid puede crear layouts visuales complejos típicos de portafolios y sitios de fotografía.

=== "HTML"

    ``` html
    <!DOCTYPE html>
    <html lang="es">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Galeria Avanzada con Grid</title>
      <link rel="stylesheet" href="./styles.css">
    </head>
    <body>
      <h1>Galeria de Fotografia</h1>

      <!-- Filtros de categorías -->
      <div class="gallery-filters">
        <button class="active">Todas</button>
        <button>Naturaleza</button>
        <button>Arquitectura</button>
        <button>Retratos</button>
        <button>Abstracto</button>
        <button>Viajes</button>
      </div>

      <!-- Galería principal -->
      <div class="gallery">
        <div class="gallery__item">
          <div class="gallery__img">SUNSET</div>
          <div class="gallery__overlay">
            <span class="icon">🔍</span>
            <h3>Atardecer en la playa</h3>
            <span>Naturaleza · 2025</span>
          </div>
        </div>
        <div class="gallery__item">
          <div class="gallery__img">BUILD</div>
          <div class="gallery__overlay">
            <span class="icon">🔍</span>
            <h3>Rascacielos</h3>
            <span>Arquitectura · 2025</span>
          </div>
        </div>
        <div class="gallery__item">
          <div class="gallery__img">FACE</div>
          <div class="gallery__overlay">
            <span class="icon">🔍</span>
            <h3>Retrato urbano</h3>
            <span>Retratos · 2025</span>
          </div>
        </div>
        <div class="gallery__item">
          <div class="gallery__img">FOREST</div>
          <div class="gallery__overlay">
            <span class="icon">🔍</span>
            <h3>Bosque místico</h3>
            <span>Naturaleza · 2024</span>
          </div>
        </div>
        <div class="gallery__item">
          <div class="gallery__img">BRIDGE</div>
          <div class="gallery__overlay">
            <span class="icon">🔍</span>
            <h3>Puente colgante</h3>
            <span>Arquitectura · 2025</span>
          </div>
        </div>
        <div class="gallery__item">
          <div class="gallery__img">ART</div>
          <div class="gallery__overlay">
            <span class="icon">🔍</span>
            <h3>Arte abstracto</h3>
            <span>Abstracto · 2025</span>
          </div>
        </div>
        <div class="gallery__item">
          <div class="gallery__img">MAP</div>
          <div class="gallery__overlay">
            <span class="icon">🔍</span>
            <h3>Mapa del mundo</h3>
            <span>Viajes · 2024</span>
          </div>
        </div>
        <div class="gallery__item">
          <div class="gallery__img">WAVE</div>
          <div class="gallery__overlay">
            <span class="icon">🔍</span>
            <h3>Olas del océano</h3>
            <span>Naturaleza · 2025</span>
          </div>
        </div>
        <div class="gallery__item">
          <div class="gallery__img">TOWER</div>
          <div class="gallery__overlay">
            <span class="icon">🔍</span>
            <h3>Torre de cristal</h3>
            <span>Arquitectura · 2025</span>
          </div>
        </div>
        <div class="gallery__item">
          <div class="gallery__img">SMILE</div>
          <div class="gallery__overlay">
            <span class="icon">🔍</span>
            <h3>Sonrisa sincera</h3>
            <span>Retratos · 2024</span>
          </div>
        </div>
        <div class="gallery__item">
          <div class="gallery__img">COLOR</div>
          <div class="gallery__overlay">
            <span class="icon">🔍</span>
            <h3>Explosión de color</h3>
            <span>Abstracto · 2025</span>
          </div>
        </div>
        <div class="gallery__item">
          <div class="gallery__img">ISLAND</div>
          <div class="gallery__overlay">
            <span class="icon">🔍</span>
            <h3>Isla paradisíaca</h3>
            <span>Viajes · 2025</span>
          </div>
        </div>
      </div>

      <h2>Versión con grid-auto-flow: dense</h2>
      <p style="text-align:center;color:#94a3b8;margin-bottom:2rem;">El algoritmo dense reorganiza los ítems para minimizar espacios vacíos.</p>

      <!-- Galería con dense -->
      <div class="gallery-dense">
        <div class="gallery__item"><div class="gallery__img">1</div><div class="gallery__overlay"><span class="icon">🔍</span><h3>Foto 1</h3></div></div>
        <div class="gallery__item"><div class="gallery__img">2</div><div class="gallery__overlay"><span class="icon">🔍</span><h3>Foto 2</h3></div></div>
        <div class="gallery__item"><div class="gallery__img">3</div><div class="gallery__overlay"><span class="icon">🔍</span><h3>Foto 3</h3></div></div>
        <div class="gallery__item"><div class="gallery__img">4</div><div class="gallery__overlay"><span class="icon">🔍</span><h3>Foto 4</h3></div></div>
        <div class="gallery__item"><div class="gallery__img">5</div><div class="gallery__overlay"><span class="icon">🔍</span><h3>Foto 5</h3></div></div>
        <div class="gallery__item"><div class="gallery__img">6</div><div class="gallery__overlay"><span class="icon">🔍</span><h3>Foto 6</h3></div></div>
        <div class="gallery__item"><div class="gallery__img">7</div><div class="gallery__overlay"><span class="icon">🔍</span><h3>Foto 7</h3></div></div>
        <div class="gallery__item"><div class="gallery__img">8</div><div class="gallery__overlay"><span class="icon">🔍</span><h3>Foto 8</h3></div></div>
        <div class="gallery__item"><div class="gallery__img">9</div><div class="gallery__overlay"><span class="icon">🔍</span><h3>Foto 9</h3></div></div>
        <div class="gallery__item"><div class="gallery__img">10</div><div class="gallery__overlay"><span class="icon">🔍</span><h3>Foto 10</h3></div></div>
      </div>
    </body>
    </html>
    ```

=== "CSS"

    ``` css
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      background: #0a0a0a;
      color: #fff;
      padding: 2rem;
    }

    h1 {
      text-align: center;
      margin-bottom: 2rem;
      font-size: 2.5rem;
      background: linear-gradient(135deg, #667eea, #f5576c);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    /*
     * ===== GALERÍA MASONRY CON GRID =====
     * 4 columnas iguales, cada fila base de 200px.
     * Los ítems ocupan diferentes spans para crear efecto irregular.
     * No es masonry puro (eso requiere CSS Grid Level 3 experimental)
     * pero el resultado visual es muy similar y profesional.
     */
    .gallery {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      grid-auto-rows: 200px;
      gap: 12px;
      max-width: 1200px;
      margin: 0 auto;
    }

    /*
     * ===== DISTRIBUCIÓN DE TAMAÑOS =====
     * Asignamos manualmente diferentes spans para crear el efecto.
     * Algunos ítems ocupan 2 columnas, otros 2 filas, etc.
     * Esta técnica es ideal cuando tienes control sobre el contenido.
     */
    .gallery__item:nth-child(1)  { grid-row: span 2; grid-column: span 2; }
    .gallery__item:nth-child(2)  { grid-row: span 1; }
    .gallery__item:nth-child(3)  { grid-row: span 1; }
    .gallery__item:nth-child(4)  { grid-row: span 2; }
    .gallery__item:nth-child(5)  { grid-row: span 1; grid-column: span 2; }
    .gallery__item:nth-child(6)  { grid-row: span 1; }
    .gallery__item:nth-child(7)  { grid-row: span 1; }
    .gallery__item:nth-child(8)  { grid-row: span 2; }
    .gallery__item:nth-child(9)  { grid-row: span 1; }
    .gallery__item:nth-child(10) { grid-row: span 1; grid-column: span 2; }
    .gallery__item:nth-child(11) { grid-row: span 2; }
    .gallery__item:nth-child(12) { grid-row: span 1; }

    .gallery__item {
      position: relative;
      border-radius: 12px;
      overflow: hidden;
      cursor: pointer;
      transition: transform 0.3s, box-shadow 0.3s;
    }

    .gallery__item:hover {
      transform: scale(1.03);
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
      z-index: 10;
    }

    /* Gradientes simulando diferentes fotos */
    .gallery__img {
      width: 100%;
      height: 100%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 3rem;
    }

    .gallery__item:nth-child(1)  .gallery__img { background: linear-gradient(135deg, #667eea, #764ba2); }
    .gallery__item:nth-child(2)  .gallery__img { background: linear-gradient(135deg, #f093fb, #f5576c); }
    .gallery__item:nth-child(3)  .gallery__img { background: linear-gradient(135deg, #4facfe, #00f2fe); }
    .gallery__item:nth-child(4)  .gallery__img { background: linear-gradient(135deg, #43e97b, #38f9d7); }
    .gallery__item:nth-child(5)  .gallery__img { background: linear-gradient(135deg, #fa709a, #fee140); }
    .gallery__item:nth-child(6)  .gallery__img { background: linear-gradient(135deg, #a18cd1, #fbc2eb); }
    .gallery__item:nth-child(7)  .gallery__img { background: linear-gradient(135deg, #fccb90, #d57eeb); }
    .gallery__item:nth-child(8)  .gallery__img { background: linear-gradient(135deg, #e0c3fc, #8ec5fc); }
    .gallery__item:nth-child(9)  .gallery__img { background: linear-gradient(135deg, #f9d423, #ff4e50); }
    .gallery__item:nth-child(10) .gallery__img { background: linear-gradient(135deg, #667eea, #f5576c); }
    .gallery__item:nth-child(11) .gallery__img { background: linear-gradient(135deg, #00b09b, #96c93d); }
    .gallery__item:nth-child(12) .gallery__img { background: linear-gradient(135deg, #4facfe, #764ba2); }

    /*
     * ===== OVERLAY AL HACER HOVER =====
     * Capa semitransparente que aparece con transición suave.
     * Muestra título, categoría e icono de la foto.
     * inset: 0 equivale a top/right/bottom/left: 0
     */
    .gallery__overlay {
      position: absolute;
      inset: 0;
      background: rgba(0, 0, 0, 0.6);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      opacity: 0;
      transition: opacity 0.3s;
      padding: 1rem;
      text-align: center;
    }

    .gallery__item:hover .gallery__overlay { opacity: 1; }
    .gallery__overlay .icon { font-size: 2rem; margin-bottom: 0.5rem; }
    .gallery__overlay h3 { font-size: 1.2rem; margin-bottom: 0.25rem; }
    .gallery__overlay span { font-size: 0.85rem; color: #ccc; }

    /*
     * ===== GALERÍA CON DENSE (alternativa) =====
     * grid-auto-flow: dense hace que el navegador reorganice
     * los ítems para llenar huecos, ideal cuando no necesitas
     * controlar exactamente la posición de cada elemento.
     */
    .gallery-dense {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      grid-auto-rows: 200px;
      grid-auto-flow: dense;
      gap: 12px;
      max-width: 1200px;
      margin: 3rem auto 0;
    }

    /* Con dense podemos usar patrones más genéricos */
    .gallery-dense .gallery__item:nth-child(3n+1) {
      grid-column: span 2;
      grid-row: span 2;
    }

    .gallery-dense .gallery__item:nth-child(5n+2) {
      grid-row: span 2;
    }

    /* Filtros de la galería */
    .gallery-filters {
      display: grid;
      grid-auto-flow: column;
      justify-content: center;
      gap: 0.5rem;
      margin-bottom: 2rem;
    }

    .gallery-filters button {
      background: transparent;
      color: #fff;
      border: 1px solid #333;
      padding: 0.5rem 1.5rem;
      border-radius: 25px;
      cursor: pointer;
      font-family: 'Segoe UI', sans-serif;
      transition: all 0.3s;
    }

    .gallery-filters button:hover,
    .gallery-filters button.active {
      background: #667eea;
      border-color: #667eea;
    }

    h2 {
      text-align: center;
      margin: 3rem 0 1.5rem;
      color: #94a3b8;
      font-size: 1.2rem;
      text-transform: uppercase;
      letter-spacing: 2px;
    }

    /* ===== RESPONSIVE ===== */
    @media (max-width: 768px) {
      .gallery,
      .gallery-dense {
        grid-template-columns: repeat(2, 1fr);
        grid-auto-rows: 180px;
      }
      .gallery__item:nth-child(1),
      .gallery__item:nth-child(5),
      .gallery__item:nth-child(10) { grid-column: span 2; }
      h1 { font-size: 1.8rem; }
    }

    @media (max-width: 480px) {
      .gallery,
      .gallery-dense {
        grid-template-columns: 1fr;
        grid-auto-rows: 250px;
      }
      .gallery__item {
        grid-column: span 1 !important;
        grid-row: span 1 !important;
      }
    }
    ```

## Casos reales

### Caso 1: Airbnb - Búsqueda de alojamientos con Grid

!!! example "Caso 1: Airbnb"
    Airbnb utiliza CSS Grid de forma magistral en su página de resultados de búsqueda. El *layout* se compone de un grid de tarjetas de alojamiento que emplea `grid-template-columns: repeat(auto-fill, minmax(280px, 1fr))` para crear una cuadrícula fluida que se adapta automáticamente al ancho de pantalla. Cada tarjeta de alojamiento es un ítem grid que contiene internamente una imagen (con posición `relative` para los *badges* de "Superhost" o "Nuevo"), el nombre del alojamiento, la puntuación, y el precio. Lo más destacable de la implementación de Airbnb es cómo combinan Grid para la disposición general de tarjetas con Flexbox para los detalles internos de cada tarjeta (alineación de estrellas, precio, etc.). También es notable el uso de `gap` consistente para mantener el espaciado uniforme entre tarjetas, y cómo el *sidebar* de filtros se convierte en un modal en dispositivos móviles, momento en el cual el grid de resultados pasa a ocupar todo el ancho disponible. La sección de "Experiencias" en la página principal también utiliza un grid *scrollable* horizontal, demostrando que Grid no está limitado a *layouts* estáticos.

### Caso 2: Spotify - Biblioteca y playlists

!!! example "Caso 2: Spotify"
    Spotify emplea CSS Grid en múltiples niveles de su interfaz. El *layout* principal de la aplicación de escritorio usa Grid con una estructura de dos columnas (*sidebar* de navegación + contenido principal) donde el *sidebar* tiene un ancho fijo y el contenido usa `1fr`. Dentro del área de contenido, la sección "Buscar" presenta un grid de categorías musicales con tarjetas de diferentes colores usando `grid-template-columns: repeat(auto-fill, minmax(180px, 1fr))`. La biblioteca de *playlists* también utiliza Grid para mostrar las carátulas en filas de 4 o 5 columnas según el ancho disponible. Lo más interesante de la implementación de Spotify es cómo han resuelto la navegación: el reproductor inferior está fijo en la parte baja, y el contenido principal tiene su propio *scroll* interno, todo gestionado con alturas calculadas mediante `grid-template-rows: 1fr auto` y `calc()` para el reproductor. Las listas de reproducción muestran las canciones como filas de un grid donde la primera columna es el número, la segunda la carátula, la tercera el título/artista, y la cuarta la duración, todo perfectamente alineado.

### Caso 3: The New York Times - Layout editorial con Grid

!!! example "Caso 3: The New York Times"
    The New York Times fue uno de los primeros grandes medios en adoptar CSS Grid para su maquetación. Su página de inicio es un ejemplo magistral de cómo Grid puede manejar *layouts* editoriales complejos con diferentes jerarquías visuales. Utilizan un sistema de **12 columnas base** donde la noticia principal ocupa **8 columnas** y las secundarias se reparten en las **4 restantes**, creando un ritmo visual muy cuidado. Las secciones como "En profundidad" o "Análisis" utilizan `grid-template-areas` con nombres descriptivos para posicionar titulares, imágenes, sumarios y metadatos. Es particularmente notable cómo implementan los cambios de *layout* en diferentes *breakpoints*: en desktop, algunas noticias ocupan 2 o 3 columnas con imágenes grandes; en tablet, se reorganizan en 2 columnas; y en móvil, todas las noticias se apilan en una sola columna. Esta reorganización se logra principalmente redefiniendo `grid-template-areas` en cada media query, sin tocar el HTML. Además, utilizan Grid para las galerías de imágenes dentro de los artículos y para los widgets de "Más leídas" en la barra lateral.

## Actividades guiadas

### Actividad Guiada 1: Construir una página de portfolio personal con Grid

El alumnado construirá paso a paso una página de portfolio personal utilizando CSS Grid. La actividad comienza con la creación del HTML semántico con secciones de cabecera, presentación, proyectos, habilidades y contacto. A continuación, se define el contenedor grid principal con `display: grid` y se diseña la estructura usando `grid-template-areas`. Para la sección de proyectos, se implementa un subgrid con `repeat(auto-fill, minmax(300px, 1fr))` que muestra tarjetas de proyecto de forma adaptativa. Cada tarjeta de proyecto contiene una imagen de placeholder, título, descripción breve y tecnologías utilizadas. El alumnado deberá añadir alineación con `place-items` para centrar el contenido en las secciones de presentación y contacto, y usar `place-self` para posicionar elementos decorativos. Se comprobará el resultado en Chrome DevTools usando el inspector de Grid (que muestra las líneas de la cuadrícula con colores).

### Actividad Guiada 2: Rediseñar una tabla de precios con Grid

Partiendo de un diseño de tabla de precios clásica con 3 columnas (Básico, Profesional, Enterprise), el alumnado transformará el layout para que use CSS Grid. Cada plan se convertirá en una tarjeta dentro de un grid de 3 columnas con `grid-template-columns: repeat(3, 1fr)`. Las tarjetas usarán `grid-template-rows` para organizar internamente el nombre del plan, precio, características y botón de compra. La tarjeta del plan "Profesional" (central) se destacará visualmente haciéndola ligeramente más alta usando `grid-row: span 1` y aplicando una sombra más pronunciada. Se implementará la versión responsive con media queries: en tablet (menos de 900px), el grid pasará a 2 columnas; en móvil (menos de 600px), a 1 columna con las tarjetas apiladas verticalmente.

### Actividad Guiada 3: Crear un panel de control con widgets

El alumnado construirá un panel de control o dashboard con CSS Grid. El layout principal consistirá en una barra lateral fija de 220px y un área de contenido flexible usando `grid-template-columns: 220px 1fr`. Dentro del área de contenido, se creará un grid de widgets con `grid-template-columns: repeat(4, 1fr)` donde cada widget será una tarjeta con información (estadísticas, gráficos, listas). Los widgets de estadísticas ocuparán 1 columna (`grid-column: span 1`), mientras que los gráficos y la actividad reciente ocuparán 2 columnas (`grid-column: span 2`). El alumnado usará `grid-auto-rows: minmax(200px, auto)` para que las filas tengan altura flexible. Se añadirán media queries para que en pantallas medianas los widgets se organicen en 2 columnas y en móviles en 1 columna, ocultando la barra lateral mediante `display: none` en el breakpoint correspondiente.

### Actividad Guiada 4: Implementar una galería de imágenes responsiva

El alumnado creará una galería de imágenes tipo masonry usando CSS Grid. Se comenzará con un grid de 4 columnas (`grid-template-columns: repeat(4, 1fr)`) con `grid-auto-rows: 200px` para las filas base. Cada imagen de la galería ocupará diferentes spans de filas y columnas usando `grid-row: span 2` o `grid-column: span 2` en elementos específicos para crear el efecto de diferentes tamaños. Se añadirán overlays con CSS que aparezcan al hacer hover, mostrando el título y la categoría de cada imagen usando `position: absolute` y transiciones de opacidad. En la versión responsive, el grid pasará a 3 columnas en tablet y 2 columnas en móvil, ajustando los spans para mantener el efecto visual. Como extra, se implementará una versión alternativa usando `grid-auto-flow: dense` y se compararán ambos resultados.

### Actividad Guiada 5: Maquetar un artículo de blog con layout editorial

El alumnado maquetará un artículo de blog con un layout editorial profesional que incluya cabecera con título y metadatos, imagen destacada a Sangre (que ocupe todo el ancho), contenido principal con anchura de lectura óptima, barra lateral con artículos relacionados, y pie de página. El layout usará CSS Grid con la estructura `grid-template-columns: 1fr minmax(0, 65ch) 300px 1fr` donde la zona central (65ch) es el ancho óptimo de lectura, y las columnas laterales (`1fr`) permiten que las imágenes puedan expandirse a Sangre: `grid-column: 1 / -1` para la imagen destacada y `grid-column: 1 / 4` para imágenes que ocupen contenido + sidebar. Se usará `position: sticky` en la barra lateral para que siga al usuario durante el scroll.

## Actividades propuestas

### Actividad Propuesta 1: Página de inicio de un restaurante

Diseña y maqueta la página de inicio de un restaurante utilizando CSS Grid. Debe incluir: cabecera con logo y menú de navegación, sección héroe con imagen de fondo e introducción, sección "Nuestra carta" con grid de platos (3 columnas en desktop, 2 en tablet, 1 en móvil), sección de testimonios con 3 citas, y pie de página con información de contacto y horarios. Utiliza `grid-template-areas` para la estructura principal y `repeat(auto-fill, minmax())` para la carta. Implementa al menos un cambio de layout con media queries. Entrega los archivos HTML y CSS con comentarios explicativos en cada propiedad Grid.

### Actividad Propuesta 2: Panel de administración de una tienda online

Crea un panel de administración para una tienda online usando CSS Grid. El layout debe tener: sidebar de navegación (220px, fijo), cabecera superior con búsqueda y avatar de usuario, y área de contenido con widgets. Los widgets deben incluir: 4 tarjetas de métricas (ventas, pedidos, clientes, ingresos) en la primera fila, un gráfico de ventas que ocupe 2/3 del ancho, y una lista de últimos pedidos en el 1/3 restante. Usa `grid-template-areas` para el layout principal y `grid-column: span 2` para widgets destacados. Implementa un menú responsive que se convierta en hamburguesa en móviles (usando checkbox hack o JavaScript mínimo). Entrega el código completo con comentarios.

### Actividad Propuesta 3: Portafolio de diseño gráfico tipo masonry

Implementa un portafolio de diseño gráfico con efecto masonry usando CSS Grid. La galería debe contener al menos 15 trabajos con diferentes proporciones (horizontal, vertical, cuadrado). Usa `grid-template-columns: repeat(4, 1fr)` y `grid-auto-rows` con diferentes spans para crear el efecto irregular. Cada trabajo debe tener un overlay con título, categoría y año que aparezca al hacer hover. Añade filtros por categoría en la parte superior usando botones. Implementa la versión responsive (3 columnas en tablet, 2 en móvil). Investiga y compara tu solución con una implementación que use `grid-auto-flow: dense`. Documenta las diferencias observadas.

### Actividad Propuesta 4: Red social de fotografía (feed)

Diseña el feed de una red social de fotografía (estilo Instagram/Pinterest) usando CSS Grid. El layout debe incluir: cabecera con logo y búsqueda, grid de publicaciones con imágenes de diferentes alturas, y barra lateral con sugerencias de usuarios. Las publicaciones deben mostrarse en un grid de 3 columnas donde cada publicación contiene la imagen, los botones de interacción (me gusta, comentar, compartir) y la descripción. Usa `grid-template-rows` dentro de cada publicación para estructurar internamente los elementos. Implementa al menos dos breakpoints donde cambie el número de columnas del feed. Añade la funcionalidad de que la barra lateral desaparezca en dispositivos móviles usando media queries.

### Actividad Propuesta 5: Sitio web de una conferencia tech

Maqueta el sitio web completo de una conferencia de tecnología usando exclusivamente CSS Grid. Secciones requeridas: cabecera con menú y botón de registro (sticky), héroe con cuenta atrás y formulario de inscripción, sección de ponentes con grid de tarjetas (foto, nombre, charla, bio breve), agenda/horario con grid de sesiones mostrando hora, título y sala, sección de patrocinadores con grid de logos, y pie de página con enlaces y mapa de ubicación. Cada sección debe usar una estrategia Grid diferente según el contenido. Implementa diseño responsive con al menos 3 breakpoints (móvil, tablet, desktop). El héroe debe reorganizarse completamente: en desktop, texto a la izquierda y formulario a la derecha; en móvil, formulario debajo del texto.

## Actividades de ampliación

### Actividad de Ampliación 1: Framework CSS propio basado en Grid

Desarrolla un mini-framework CSS personal basado en CSS Grid. El framework debe proporcionar clases utilitarias para crear layouts comunes sin escribir CSS personalizado. Implementa: un sistema de grid de 12 columnas mediante clases `.grid` y `.col-{n}`, clases para áreas de layout predefinidas (`.layout-header`, `.layout-sidebar`, `.layout-content`, `.layout-footer`), generación de layouts responsivos mediante clases como `.grid--2col`, `.grid--3col`, `.grid--4col` que internamente usen `repeat(auto-fit, minmax())`, y utilidades de alineación (`.items-center`, `.items-start`, `.content-between`). Escribe los estilos CSS del framework y una página de demostración que muestre todas las funcionalidades. Compara tu solución con frameworks existentes como Bootstrap o Tailwind y documenta las ventajas de un enfoque nativo con Grid.

### Actividad de Ampliación 2: Comparativa exhaustiva Grid vs Flexbox

Realiza una investigación práctica comparando CSS Grid y Flexbox en diferentes escenarios. Para cada uno de los siguientes casos de uso, implementa dos versiones (una con Grid y otra con Flexbox) y analiza: número de líneas de CSS necesarias, legibilidad del código, facilidad de mantenimiento, comportamiento responsive, y rendimiento. Los escenarios a comparar son: barra de navegación horizontal con logo y enlaces, galería de tarjetas con altura variable, centrado perfecto de un elemento, layout de página completa con sidebar, y formulario con etiquetas alineadas. Documenta tus hallazgos en un informe con las implementaciones de código y conclusiones sobre cuándo usar cada tecnología.

### Actividad de Ampliación 3: Implementar Subgrid para cards alineadas

Investiga y experimenta con la característica Subgrid de CSS Grid Level 2. Crea un layout de tarjetas de producto donde el contenido interno de cada tarjeta (título, descripción, precio, botón) se alinee perfectamente entre todas las tarjetas de la misma fila, independientemente de la longitud del contenido. Implementa dos versiones: una usando Subgrid (`grid-template-rows: subgrid`) y otra sin Subgrid (usando técnicas alternativas como altura fija o `display: contents`). Compara ambas soluciones en términos de complejidad de código, mantenibilidad y soporte de navegadores. Prueba el resultado en diferentes navegadores y documenta el nivel de soporte actual. Incluye capturas de pantalla de ambas versiones.

## Buenas prácticas

1. **Usa Grid para el layout principal y Flexbox para componentes internos**: La combinación de ambos modelos produce el código más limpio y mantenible. Grid gestiona la estructura bidimensional de la página (cabecera, sidebar, contenido, pie) mientras Flexbox se encarga de la alineación unidimensional dentro de cada sección (menús, listas, centrado de contenido).

2. **Nombra las líneas y áreas del grid con nombres semánticos**: En lugar de confiar solo en números de línea, asigna nombres descriptivos usando la sintaxis `[nombre-linea]` en `grid-template-columns` o mediante `grid-template-areas`. Esto hace que el código sea autodocumentado y más fácil de modificar. Por ejemplo, `grid-template-columns: [inicio-sidebar] 250px [fin-sidebar inicio-contenido] 1fr [fin-contenido]`.

3. **Prefiere `grid-template-areas` sobre posicionamiento por líneas para layouts estáticos**: El enfoque de áreas es visual e intuitivo. Cuando el layout es conocido y no cambia dinámicamente, definir la estructura como un mapa ASCII en CSS facilita que cualquier desarrollador entienda la disposición de un vistazo.

4. **Utiliza `minmax()` y `auto-fill`/`auto-fit` en lugar de media queries cuando sea posible**: La combinación `repeat(auto-fit, minmax(250px, 1fr))` produce layouts fluidos que se adaptan automáticamente sin necesidad de breakpoints explícitos. Esto reduce el código CSS, elimina puntos de ruptura arbitrarios y crea una experiencia más fluida en todos los tamaños de pantalla.

5. **Define el grid explícito para la estructura base y confía en el grid implícito para contenido dinámico**: Establece las columnas y filas principales con `grid-template-*` y usa `grid-auto-rows` y `grid-auto-flow` para controlar cómo se comporta el layout cuando hay más contenido del previsto.

6. **Usa las herramientas de desarrollo del navegador para depurar**: Tanto Firefox como Chrome incluyen inspectores visuales de Grid que muestran las líneas de la cuadrícula, las áreas nombradas y los gaps. En Firefox, el panel "CSS Grid" del inspector es especialmente potente y permite visualizar los números de línea y nombres de área directamente sobre la página.

7. **Proporciona fallbacks con `@supports` para navegadores antiguos**: Si el proyecto requiere soporte para IE11 u otros navegadores sin Grid, envuelve el código Grid en `@supports (display: grid)` y proporciona un layout alternativo con Flexbox o floats fuera del bloque `@supports`.

8. **Evita el uso excesivo de `grid-template` shorthand**: Aunque es potente, la sintaxis del shorthand es compleja y propensa a errores. Es preferible usar las propiedades individuales (`grid-template-columns`, `grid-template-rows`, `grid-template-areas`) para mantener la claridad.

9. **Establece `box-sizing: border-box` globalmente**: Esta práctica, ya recomendada en general, es especialmente importante con Grid porque el cálculo de anchos de columna con `fr` y porcentajes es más predecible cuando padding y border están incluidos en el tamaño total.

10. **Documenta la estructura del grid con comentarios**: Dado que los layouts con Grid pueden ser complejos, incluye comentarios que expliquen la intención de cada definición de grid, especialmente cuando uses posicionamiento por líneas o spans que no son evidentes a simple vista.

## Errores frecuentes

Los errores siguientes aparecen una y otra vez en los primeros proyectos con CSS Grid:

!!! warning "Errores frecuentes de CSS Grid"
    1. **Confundir `auto-fill` con `auto-fit`**: es uno de los errores más comunes al empezar con Grid. `auto-fill` mantiene las columnas vacías (dejando espacio en blanco), mientras que `auto-fit` las colapsa (los ítems se expanden). La diferencia es sutil pero tiene un impacto visual enorme. Si al reducir el número de ítems tu *layout* muestra espacios vacíos inexplicables, probablemente estás usando `auto-fill` cuando necesitas `auto-fit`.

    2. **Olvidar que los ítems grid son solo los hijos directos**: solo los elementos que son hijos inmediatos del contenedor con `display: grid` se convierten en ítems de la cuadrícula. Los nietos y descendientes más profundos no participan en el grid a menos que también se declaren como contenedores grid. Este error es frecuente al anidar estructuras HTML.

    3. **No definir `grid-auto-rows` para el grid implícito**: cuando hay más ítems de los que caben en el grid explícito, las nuevas filas se crean con `height: auto` por defecto. Esto puede provocar alturas inconsistentes si no se define explícitamente `grid-auto-rows`. Es buena práctica establecer siempre un valor para esta propiedad cuando el número de ítems es variable.

    4. **Usar porcentajes en lugar de `fr` para columnas flexibles**: aunque `grid-template-columns: 33.33% 33.33% 33.33%` puede funcionar, es más frágil que `grid-template-columns: repeat(3, 1fr)`. Los porcentajes no descuentan automáticamente el espacio de los *gaps* y son más difíciles de mantener cuando cambia el número de columnas.

    5. **Posicionar ítems fuera de los límites del grid sin definir el grid implícito**: si un ítem se posiciona en `grid-column: 5 / 6` pero el grid solo tiene 3 columnas definidas, el navegador creará columnas implícitas. Sin `grid-auto-columns`, estas tendrán ancho 0 o `auto`, lo que puede causar comportamientos inesperados.

    6. **Confundir `justify-items`/`align-items` con `justify-content`/`align-content`**: las primeras alinean los ítems dentro de sus celdas; las segundas alinean la cuadrícula completa dentro del contenedor. Es habitual usar `justify-content` esperando centrar los ítems individualmente cuando en realidad se necesita `justify-items`.

    7. **No considerar el orden de los elementos en el DOM al usar `dense`**: el valor `dense` en `grid-auto-flow` puede alterar el orden visual de los ítems para llenar huecos. Si el orden de los elementos es importante para la semántica o accesibilidad, `dense` puede causar problemas. Úsalo solo cuando el orden visual no sea significativo (como en galerías de imágenes).

    8. **Ignorar el soporte de Subgrid**: aunque Subgrid ya está disponible en navegadores modernos, muchos desarrolladores no lo aprovechan. Antes de implementar soluciones complejas con JavaScript o `display: contents` para alinear tarjetas, verifica si Subgrid puede resolver el problema de forma más elegante.

    9. **Abusar de `grid-column: 1 / -1` sin entender los límites**: esta técnica es muy útil para hacer que un elemento ocupe todo el ancho, pero puede causar problemas cuando se combina con `grid-auto-flow: column` o cuando el grid implícito genera más columnas de las esperadas.

    10. **Sobrecargar las media queries con cambios de grid**: en lugar de redefinir completamente el grid en cada *breakpoint*, aprovecha las capacidades fluidas de Grid (`auto-fit`, `minmax()`) para minimizar la cantidad de código *responsive* necesario. Reserva las *media queries* solo para cambios estructurales mayores.

## Resumen

CSS Grid Layout representa la culminación de décadas de evolución en maquetación web, ofreciendo por primera vez un sistema nativo y bidimensional para diseñar layouts. A lo largo de esta unidad hemos explorado desde los fundamentos (contendor grid, definición de columnas y filas) hasta patrones avanzados (landing pages, dashboards, galerías masonry) pasando por todas las propiedades que hacen de Grid una herramienta indispensable en el desarrollo web moderno.

Los conceptos clave que el alumnado debe retener son: la diferencia entre grid explícito (definido manualmente) e implícito (generado automáticamente), el uso de la unidad `fr` para distribuir espacio proporcionalmente, la potencia de `minmax()` combinada con `auto-fill`/`auto-fit` para crear layouts fluidos sin media queries, el posicionamiento de ítems mediante líneas numeradas y spans, y la maquetación visual con `grid-template-areas` que permite diseñar la estructura de la página como un mapa ASCII directamente en CSS.

Grid no reemplaza a Flexbox sino que lo complementa. Mientras Grid brilla en la maquetación bidimensional de páginas completas, Flexbox sigue siendo la mejor opción para alinear elementos en una sola dimensión (barras de navegación, listas, centrado de contenido). La combinación de ambos, junto con media queries para ajustes responsive, proporciona un conjunto de herramientas completo para cualquier desafío de maquetación web.

El soporte universal de Grid en navegadores modernos permite su uso sin restricciones en proyectos actuales. Para proyectos que requieran compatibilidad con navegadores antiguos, `@supports` ofrece una vía de mejora progresiva limpia y estándar.

## Recursos complementarios

- **CSS Grid Garden (https://cssgridgarden.com/)**: Juego interactivo que enseña Grid mediante desafíos de posicionamiento con zanahorias. Ideal para practicar las propiedades de forma lúdica. Recomendado como primer contacto práctico con Grid.

- **Guía completa de CSS Grid en CSS-Tricks (https://css-tricks.com/snippets/css/complete-guide-grid/)**: La referencia visual más completa y actualizada sobre CSS Grid. Excelente chuleta de consulta rápida con todas las propiedades explicadas visualmente.

- **MDN Web Docs - CSS Grid Layout (https://developer.mozilla.org/es/docs/Web/CSS/CSS_Grid_Layout)**: La documentación oficial de Mozilla, traducida al español. Incluye tutoriales detallados, ejemplos interactivos y guías de referencia para cada propiedad.

- **Grid by Example (https://gridbyexample.com/)**: Sitio creado por Rachel Andrew, una de las principales expertas en CSS Grid. Contiene ejemplos prácticos clasificados por patrones de uso, vídeos explicativos y código descargable.

- **Layout Land (https://www.youtube.com/c/LayoutLand)**: Canal de YouTube de Jen Simmons donde explora las posibilidades creativas de CSS Grid con ejemplos innovadores y demostraciones prácticas.

- **Can I Use - CSS Grid (https://caniuse.com/css-grid)**: Datos actualizados de soporte de navegadores para CSS Grid, incluyendo subgrid y funcionalidades específicas. Imprescindible para tomar decisiones sobre adopción.

- **W3C CSS Grid Layout Module Level 1 (https://www.w3.org/TR/css-grid-1/)**: La especificación oficial del W3C. Documento de referencia técnica para comprender el comportamiento exacto de cada propiedad según el estándar.

- **Firefox DevTools - Inspector de Grid**: Firefox incluye el inspector de Grid más potente del mercado. Accesible desde las herramientas de desarrollo, permite visualizar líneas, áreas y gaps sobreimpresionados en la página. Imprescindible para depurar layouts complejos.

- **Libro "CSS: The Definitive Guide - 5th Edition" de Eric Meyer y Estelle Weyl (O'Reilly, 2023)**: Cubre CSS Grid en profundidad junto con todas las demás tecnologías CSS. Recurso de referencia para profundizar en los fundamentos teóricos.

- **Autoprefixer (https://github.com/postcss/autoprefixer)**: Herramienta PostCSS que añade automáticamente prefijos de navegador. Incluye soporte para la sintaxis antigua de Grid de IE11, facilitando la compatibilidad con navegadores legacy.
