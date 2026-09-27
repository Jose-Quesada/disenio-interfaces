# Unidad 8: CSS Profesional y Técnicas Avanzadas

## Objetivos de aprendizaje

Al finalizar esta unidad, el alumnado dominará el uso de CSS moderno para crear interfaces web profesionales, responsivas y mantenibles. Será capaz de utilizar selectores avanzados (combinadores, pseudoclases como `:has()`, `:is()`, `:where()`, `:not()`, pseudoelementos `::before`, `::after`, `::marker`), comprender y controlar la especificidad y la cascada mediante `@layer`, dominar el modelo de caja con `box-sizing`, aplicar diferentes modos de display y posicionamiento, utilizar variables CSS (Custom Properties) para crear temas dinámicos con cambio claro/oscuro mediante JavaScript, emplear correctamente todas las unidades CSS (`px`, `em`, `rem`, `vw`, `vh`, `%`, `fr`, `dvh`), organizar el código con metodologías profesionales (BEM, ITCSS), crear animaciones y transiciones fluidas respetando `prefers-reduced-motion`, y dominar todas las técnicas de centrado de elementos. El alumnado aplicará estos conocimientos para construir layouts profesionales completos combinando técnicas modernas de CSS.

## Relación con los Resultados de Aprendizaje

Esta unidad se alinea con el RA2 del módulo 0615: "Crear interfaces web utilizando hojas de estilos y lenguajes de marcas". Los contenidos sobre selectores avanzados, especificidad, modelo de caja, display, posicionamiento, variables CSS y animaciones permiten al alumnado implementar cualquier diseño de interfaz requerido por las especificaciones. También se relaciona con el RA1 en cuanto a la planificación de la interfaz valorando especificaciones de diseño, pues la organización del código CSS mediante metodologías es parte fundamental de la planificación técnica. La unidad conecta con el RA5 de accesibilidad mediante las secciones sobre `prefers-reduced-motion`, contraste y técnicas de diseño inclusivo.

## Conocimientos previos

El alumnado debe conocer los fundamentos de CSS: sintaxis de reglas (selector, propiedad, valor), selectores básicos (tipo, clase `.`, ID `#`), modelo de caja elemental (margin, border, padding, content), propiedades básicas de color (`color`, `background-color`) y tipografía (`font-family`, `font-size`, `font-weight`, `text-align`), y el concepto de herencia en CSS. Debe saber enlazar hojas de estilo externas mediante `<link>` y estilos internos con `<style>`. Es recomendable tener experiencia previa maquetando páginas sencillas y haberse encontrado con problemas comunes de especificidad y colapso de márgenes.

## Contenidos

1. **Evolución y estado actual de CSS.** De CSS1 a CSS3. Módulos CSS4. Novedades: `@layer`, `@container`, CSS Nesting, `:has()`.
2. **Selectores avanzados.** Combinadores: descendiente, hijo `>`, hermano adyacente `+`, hermano general `~`. Pseudoclases funcionales: `:is()`, `:where()`, `:not()`, `:has()`. Pseudoclases de formulario: `:valid`, `:invalid`, `:disabled`, `:checked`. Pseudoelementos: `::before`, `::after`, `::marker`, `::selection`, `::placeholder`.
3. **Especificidad y cascada.** Cálculo (a,b,c). `!important`. `@layer` para control de especificidad. Estrategias de ordenación.
4. **Modelo de caja.** `box-sizing: border-box` vs `content-box`. Colapso de márgenes. `padding`, `border`, `margin`, `outline`.
5. **Display y Position.** `block`, `inline`, `inline-block`, `none`, `flex`, `grid`, `contents`. Position: `static`, `relative`, `absolute`, `fixed`, `sticky`. Z-index y contexto de apilamiento.
6. **Variables CSS (Custom Properties).** Definición con `--nombre`. Uso con `var()`. Fallback. Scope (`:root` vs local). Herencia. Temas dinámicos claro/oscuro con JavaScript.
7. **Unidades CSS.** Absolutas: `px`. Relativas: `%`, `em`, `rem`, `vw`, `vh`, `vmin`, `vmax`, `dvh`, `svh`, `lvh`, `ch`, `ex`. `fr` en Grid. Cuándo usar cada una.
8. **Organización del código CSS.** Metodologías: BEM, SMACSS, OOCSS, ITCSS, Cube CSS. Utility-first (Tailwind). CSS Modules. Naming conventions.
9. **Funciones CSS.** `calc()`, `min()`, `max()`, `clamp()`, `color-mix()`, `hsl()`, `rgb()`.
10. **Pseudoelementos decorativos.** `::before`/`::after`. Contadores CSS. Tooltips CSS puro.
11. **Transiciones y animaciones.** `transition`, `@keyframes`, `animation`. Propiedades animables. `prefers-reduced-motion`.
12. **Técnicas de centrado.** Flexbox, Grid, absolute + transform, text-align + line-height.

## Desarrollo teórico

### 1. Evolución y estado actual de CSS

!!! info "Evolución de CSS"
    CSS ha evolucionado desde su primera especificación en 1996 (**CSS1**, propiedades básicas de fuente, color y alineación) hasta el ecosistema actual de módulos independientes. **CSS3**, lanzado a partir de 1999, fragmentó la especificación en módulos temáticos (Selectores, Color, Fondos, Transformaciones, Animaciones, Flexbox, Grid) que evolucionan a ritmos independientes. Actualmente se habla de **"CSS4"** como término informal para referirse a los módulos más recientes que añaden funcionalidades significativas.

Entre las novedades más importantes destacan:

!!! info "Novedades de CSS moderno"
    - **`@layer`** — organiza capas de cascada y controla la especificidad sin recurrir a `!important`.
    - **`@container`** (Container Queries) — permite aplicar estilos basados en el tamaño de un contenedor padre, no solo del viewport.
    - **CSS Nesting** — permite anidar selectores dentro de otros (similar a Sass/LESS) de forma nativa.
    - **`:has()`** — la pseudoclase conocida como "el selector padre": selecciona elementos basándose en sus descendientes, resolviendo una limitación histórica de CSS.

### 2. Selectores avanzados

**Combinadores:**

- **Descendiente (`A B`)** — selecciona B que es descendiente de A a cualquier nivel.
- **Hijo (`A > B`)** — selecciona B solo si es hijo directo de A.
- **Hermano adyacente (`A + B`)** — selecciona B inmediatamente después de A.
- **Hermano general (`A ~ B`)** — selecciona todos los B que son hermanos de A, no necesariamente adyacentes.

**Pseudoclases funcionales modernas:**

- **`:is()`** — permite agrupar selectores simplificando código repetitivo: `:is(header, main, footer) p` aplica a párrafos dentro de header, main o footer. Su especificidad es la del argumento más específico.
- **`:where()`** — funciona igual pero con especificidad **0** (ideal para estilos base fácilmente sobrescribibles).
- **`:not()`** — excluye elementos que coinciden con el selector: `p:not(.destacado)` selecciona párrafos sin la clase destacado.
- **`:has()`** — el "selector padre": `article:has(img)` selecciona articles que contienen imágenes; `form:has(:invalid)` selecciona formularios con campos inválidos.

**Pseudoclases de formulario:**

- **`:valid` / `:invalid`** — aplican estilos según el estado de validación HTML5.
- **`:disabled` / `:enabled`** — para campos deshabilitados.
- **`:checked`** — para checkboxes y radios marcados.
- **`:focus-visible`** — muestra foco solo cuando se navega con teclado (no con ratón).
- **`:focus-within`** — aplica cuando cualquier descendiente tiene foco.

**Pseudoelementos:**

- **`::before` y `::after`** — crean contenido generado antes/después del contenido real del elemento (requieren `content`).
- **`::marker`** — estiliza los marcadores de listas.
- **`::selection`** — estiliza el texto seleccionado.
- **`::placeholder`** — estiliza el texto placeholder de inputs.
- **`::first-letter` / `::first-line`** — estilizan la primera letra/línea de un bloque de texto.

### 3. Especificidad y cascada

!!! info "Definición"
    La especificidad determina qué regla CSS se aplica cuando múltiples reglas compiten por el mismo elemento. Se calcula como **(a,b,c)**: **a** = IDs, **b** = clases/atributos/pseudoclases, **c** = elementos/pseudoelementos. Los estilos **inline** tienen máxima especificidad. La cascada resuelve empates por orden de aparición.

!!! warning "Evita abusar de !important"
    `!important` fuerza la aplicación de una declaración saltándose la especificidad. Su uso debe ser excepcional y está considerado una mala práctica cuando se abusa.

Para controlar la cascada sin `!important`, CSS introdujo `@layer`, que permite definir capas con orden explícito: **las capas declaradas después tienen prioridad**, independientemente de la especificidad de los selectores dentro de cada capa.

!!! tip "Capas lógicas con @layer"
    Esto permite organizar el CSS en capas lógicas: **reset**, **base**, **componentes**, **utilidades**, donde las utilidades siempre ganan por estar en la última capa.

### 4. Modelo de caja

!!! info "Modelo de caja"
    El modelo de caja define cómo se calcula el tamaño total de un elemento. Por defecto (`box-sizing: content-box`), `width` y `height` definen solo el área de contenido; padding y border se añaden al total. Con `box-sizing: border-box`, `width` y `height` incluyen **content**, **padding** y **border**, simplificando enormemente los cálculos de layout.

Es práctica estándar aplicarlo universalmente: `*, *::before, *::after { box-sizing: border-box; }`.

!!! warning "Colapso de márgenes"
    El colapso de márgenes ocurre cuando márgenes verticales adyacentes se solapan: **el mayor prevalece**. Solo afecta a márgenes verticales de elementos en flujo normal. Padding, border y contenido no colapsan.

    Se evita con alguna de estas técnicas:

    - usar `display: flex` o `display: grid` en el contenedor;
    - añadir `padding` en el padre;
    - aplicar `overflow: auto` en el contenedor.

### 5. Display y Position

!!! info "Display"
    - **`block`** — ocupa todo el ancho y fuerza salto de línea.
    - **`inline`** — fluye en línea sin forzar saltos.
    - **`inline-block`** — combina flujo inline con capacidad de definir dimensiones.
    - **`none`** — oculta el elemento (no ocupa espacio).
    - **`flex` y `grid`** — activan contextos de formato flex y grid.
    - **`contents`** — hace que el elemento desaparezca visualmente pero sus hijos se comporten como hijos directos del ancestro (útil para layouts).

**Position:**

| Valor | Comportamiento |
|-------|----------------|
| **`static`** | Flujo normal. |
| **`relative`** | Desplaza desde su posición normal sin afectar a otros. |
| **`absolute`** | Posiciona respecto al ancestro posicionado más cercano; sale del flujo. |
| **`fixed`** | Posiciona respecto al viewport; sale del flujo. |
| **`sticky`** | Combina relative y fixed: se comporta como relative hasta que alcanza un umbral de scroll, luego se fija. |

!!! note "Z-index y contexto de apilamiento"
    **Z-index** controla el apilamiento en el eje Z; solo funciona en elementos posicionados o flex/grid items. Crea contexto de apilamiento cuando se combina con `position` distinto de `static`.

### 6. Variables CSS (Custom Properties)

!!! info "Variables CSS (Custom Properties)"
    Las variables CSS se definen con `--nombre: valor;` y se usan con `var(--nombre, fallback)`. Se heredan de padres a hijos. Normalmente se definen en `:root` para ámbito global: `:root { --color-primario: #2563eb; }`. El **fallback** es opcional y se usa si la variable no está definida.

    La gran ventaja sobre preprocesadores es que las variables CSS son **dinámicas**: pueden cambiar en tiempo de ejecución mediante JavaScript (`element.style.setProperty('--color', 'red')`), responder a media queries y actualizarse en cascada. Esto permite implementar **temas (claro/oscuro)** con un simple cambio de variables en `:root` o `html` cuando el usuario pulsa un botón o el sistema cambia de modo.

```css
:root { --bg: #fff; --text: #1a1a2e; }
[data-theme="dark"] { --bg: #1a1a2e; --text: #f1f5f9; }
body { background: var(--bg); color: var(--text); }
```

### 7. Unidades CSS

| Unidad | Referencia | Uso típico |
|--------|------------|------------|
| **`px`** | Píxeles (unidad absoluta) | Bordes, sombras y valores pequeños precisos. |
| **`%`** | Porcentaje relativo al padre | Anchos y altos responsivos. |
| **`em`** | `font-size` del elemento actual | Márgenes y paddings que escalan con el texto. |
| **`rem`** | `font-size` del `<html>` | Tipografía y espaciados globales consistentes (preferible). |
| **`vw` / `vh`** | Porcentaje del viewport | `100vw` = ancho completo, `100vh` = alto completo. |
| **`dvh` / `svh` / `lvh`** | Viewport dinámicas | Consideran las barras de navegación móviles. |
| **`ch`** | Ancho del carácter "0" | Limitar anchos de línea de texto (60-70ch óptimo). |
| **`fr`** | Fracción en CSS Grid | Distribuye espacio disponible proporcionalmente. |
| **`clamp(min, ideal, max)`** | Función CSS | Limita un valor entre un mínimo y un máximo. |

### 8. Organización del código CSS

!!! info "Metodologías de organización"
    - **BEM (Block-Element-Modifier)** — metodología de nomenclatura. Bloque: `.card`, Elemento: `.card__title`, Modificador: `.card--featured`. Evita anidamiento excesivo, produce selectores planos de baja especificidad y es auto-documentado.
    - **ITCSS (Inverted Triangle CSS)** — arquitectura por capas de especificidad creciente: Settings → Tools → Generic → Elements → Objects → Components → Utilities. Las utilidades (`.hidden`, `.text-center`) tienen máxima especificidad por posición.
    - **Utility-first (Tailwind CSS)** — enfoque donde cada clase aplica una propiedad CSS específica: `class="flex items-center gap-4 p-6 bg-white rounded-lg shadow-md"`. Ventajas: sin nombrar cosas, sin especificidad, cambios locales, CSS final más pequeño en producción.

### 9. Funciones CSS

- `calc()`: operaciones matemáticas con unidades mixtas: `width: calc(100% - 2rem)`.
- `min()`: elige el valor más pequeño: `width: min(100%, 800px)`.
- `max()`: elige el valor más grande: `width: max(50%, 300px)`.
- `clamp(min, ideal, max)`: tipografía fluida: `font-size: clamp(1rem, 2.5vw, 2rem)`.
- `color-mix()`: mezcla colores: `color-mix(in srgb, blue 70%, white)`.
- `hsl()`/`hsla()`: color por matiz, saturación, luminosidad.

### 10. Pseudoelementos decorativos

`::before` y `::after` requieren la propiedad **`content`** (puede ser texto, `url()` o vacío para decoración pura). Son hijos del elemento y se comportan como `inline` por defecto. Útiles para **iconos**, **decoraciones**, **tooltips CSS puro**, **limpieza de floats** y **animaciones decorativas** sin HTML adicional.

!!! info "Contadores CSS"
    Los contadores CSS (`counter-reset`, `counter-increment`, `counter()`) permiten numerar elementos automáticamente, muy útil para listas numeradas personalizadas o numeración de figuras:

    - **`counter-reset`** — inicializa un contador.
    - **`counter-increment`** — incrementa el contador.
    - **`counter()`** — muestra el valor del contador.

### 11. Transiciones y animaciones

**Transiciones:** `transition: propiedad duración timing-function retardo`. Suavizan cambios de estado: `transition: background 0.3s ease`. Solo funcionan con propiedades animables (colores, dimensiones, transform, opacity, etc.).

**Animaciones:** `@keyframes nombre { 0% {...} 100% {...} }` define fotogramas. `animation: nombre duración timing-function retardo iteraciones dirección fill-mode`. Permiten secuencias complejas y repetición.

!!! warning "Obligatorio: prefers-reduced-motion"
    **`prefers-reduced-motion`** es una media query que respeta la preferencia del sistema operativo del usuario para reducir animaciones. Es obligatorio para accesibilidad:

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; }
}
```

### 12. Técnicas de centrado

| Técnica | Aplicación |
|---------|------------|
| **Flexbox** | `display: flex; justify-content: center; align-items: center;` en el contenedor. Centrado bidimensional más simple y moderno. |
| **Grid** | `display: grid; place-items: center;` (shorthand de `align-items` + `justify-items`). Para un solo elemento: `place-content: center`. |
| **Absolute + transform** | `position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);` sobre el elemento a centrar, con `position: relative` en el padre. |
| **Text-align + line-height** | Para centrado horizontal de texto inline: `text-align: center`. Para centrado vertical de una línea: `line-height` igual a la altura del contenedor. |

## Ejemplos guiados

### Ejemplo 1: Selectores avanzados en acción

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Selectores CSS Avanzados | Ejemplo Didáctico</title>
  <style>
    /* RESET BÁSICO */
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      background: #f8fafc; padding: 40px;
      color: #1e293b; line-height: 1.7;
    }
    .contenedor { max-width: 800px; margin: 0 auto; }

    /* === SELECTORES EN ACCIÓN === */

    /* 1. COMBINADOR HIJO (>) : solo los li hijos DIRECTOS de .menu */
    .menu > li { display: inline-block; margin-right: 16px; }

    /* 2. COMBINADOR HERMANO ADYACENTE (+) : párrafo que sigue INMEDIATAMENTE a h2 */
    h2 + p { font-style: italic; color: #64748b; margin-bottom: 16px; }

    /* 3. COMBINADOR HERMANO GENERAL (~) : todos los botones hermanos de h3 */
    h3 ~ button { margin-right: 8px; }

    /* 4. :is() : estilos compartidos para múltiples elementos sin repetir */
    :is(h2, h3, h4) { color: #2563eb; margin-top: 24px; margin-bottom: 8px; }

    /* 5. :where() : igual que :is() pero con especificidad 0 (fácil de sobrescribir) */
    :where(nav a) { color: #475569; text-decoration: none; }

    /* 6. :not() : todos los párrafos EXCEPTO los que tienen clase .destacado */
    p:not(.destacado) { opacity: 0.85; }

    /* 7. :has() : tarjeta que CONTIENE una imagen */
    .card:has(img) { border: 2px solid #2563eb; }

    /* 8. :has() : formulario que CONTIENE campos inválidos */
    form:has(:invalid) { border-left: 4px solid #dc2626; padding-left: 16px; }

    /* 9. ::before : decoración antes del contenido de h2 */
    h2::before {
      content: "◆"; color: #2563eb; margin-right: 8px; font-size: 0.8em;
    }

    /* 10. ::after : contenido generado después */
    a[href^="http"]::after {
      content: " ↗"; font-size: 0.7em; color: #94a3b8;
    }

    /* 11. ::marker : personalizar marcadores de lista */
    ul.personalizada li::marker { color: #2563eb; content: "→ "; }

    /* 12. ::selection : texto seleccionado */
    ::selection { background: #2563eb; color: #fff; }

    /* 13. :nth-child / :nth-of-type : filas alternas en tabla o lista */
    li:nth-child(odd) { background: #f1f5f9; }
    li:nth-child(even) { background: #e2e8f0; }

    /* 14. :focus-visible : foco solo con teclado (no con ratón) */
    :focus-visible { outline: 3px solid #2563eb; outline-offset: 2px; }

    /* 15. :focus-within : cuando cualquier descendiente del form tiene foco */
    form:focus-within { box-shadow: 0 0 0 3px rgba(37,99,235,0.2); }

    /* Tarjetas de ejemplo */
    .card {
      padding: 16px; border-radius: 8px; background: #fff;
      margin-bottom: 12px; box-shadow: 0 1px 4px rgba(0,0,0,0.06);
    }
    .card img { max-width: 100%; border-radius: 4px; }
    .destacado { background: #eff6ff; padding: 12px; border-radius: 6px; }
    li { padding: 8px 12px; border-radius: 4px; }
    form { max-width: 400px; padding: 20px; background: #fff; border-radius: 8px; }
    input { padding: 8px; border: 1px solid #e2e8f0; border-radius: 4px; width: 100%; margin-bottom: 8px; }
    button { padding: 8px 16px; background: #2563eb; color: #fff; border: none; border-radius: 4px; cursor: pointer; }
    button:hover { background: #1d4ed8; }
  </style>
</head>
<body>
  <div class="contenedor">
    <h1>Demostración de Selectores CSS Avanzados</h1>

    <!-- Combinador hijo > -->
    <h2>Combinador Hijo (&gt;)</h2>
    <ul class="menu">
      <li>Elemento 1</li>
      <li>Elemento 2</li>
      <li>Elemento 3</li>
    </ul>

    <!-- Hermanos adyacentes + -->
    <h2>Hermano Adyacente (+)</h2>
    <p>Este párrafo está inmediatamente después de un h2: se muestra en cursiva y gris.</p>

    <!-- :is() y ::before -->
    <h2>Selector :is() con H3 y H4</h2>
    <h3>Subtítulo h3 con color azul (gracias a :is)</h3>
    <h4>Subtítulo h4 también azul (gracias a :is)</h4>

    <!-- :has() con img -->
    <h2>Selector :has() - Tarjeta con imagen</h2>
    <div class="card">
      <p>Tarjeta con imagen (borde azul):</p>
      <img src="https://via.placeholder.com/400x150" alt="Placeholder" width="400" height="150">
    </div>
    <div class="card" style="margin-top:12px;">
      <p>Tarjeta sin imagen (sin borde azul).</p>
    </div>

    <!-- :has() con formulario -->
    <h2>:has() en formulario</h2>
    <form>
      <p>Formulario con campo email (requerido, por tanto :invalid al estar vacío):</p>
      <input type="email" required placeholder="Email (requerido)">
      <p style="font-size:0.85rem;color:#64748b;">Observa el borde rojo izquierdo del formulario mientras el campo está vacío.</p>
      <button type="submit">Enviar</button>
    </form>

    <!-- ::marker -->
    <h2>Pseudoelemento ::marker</h2>
    <ul class="personalizada">
      <li>Elemento con flecha personalizada</li>
      <li>Segundo elemento</li>
      <li>Tercer elemento</li>
    </ul>

    <!-- :nth-child y ::selection -->
    <h2>:nth-child y ::selection</h2>
    <p>Selecciona cualquier texto de esta página para ver el color de selección azul.</p>
    <ul>
      <li>Fila 1 (odd - fondo gris claro)</li>
      <li>Fila 2 (even - fondo gris medio)</li>
      <li>Fila 3 (odd)</li>
      <li>Fila 4 (even)</li>
    </ul>

    <!-- :not() -->
    <h2>:not()</h2>
    <p>Párrafo normal (opacidad reducida).</p>
    <p class="destacado">Párrafo destacado (opacidad completa, fondo azul claro).</p>

    <!-- Enlaces externos con ::after -->
    <h2>Enlaces externos con ::after</h2>
    <p>Enlace interno: <a href="/pagina">Ir a página</a></p>
    <p>Enlace externo: <a href="https://developer.mozilla.org">MDN Web Docs</a></p>
  </div>
</body>
</html>
```

### Ejemplo 2: Sistema de temas claro/oscuro con variables CSS y JavaScript

```html
<!DOCTYPE html>
<html lang="es" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="theme-color" content="#ffffff" media="(prefers-color-scheme: light)">
  <meta name="theme-color" content="#0f172a" media="(prefers-color-scheme: dark)">
  <title>Toggle Tema Claro/Oscuro | Ejemplo Didáctico</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    /* ===============================================
       DEFINICIÓN DE VARIABLES CSS POR TEMA
       Las variables se heredan desde html a todo el documento
       =============================================== */
    :root, [data-theme="light"] {
      --color-bg: #ffffff;
      --color-bg-secondary: #f8fafc;
      --color-text: #1e293b;
      --color-text-secondary: #64748b;
      --color-primary: #2563eb;
      --color-primary-hover: #1d4ed8;
      --color-border: #e2e8f0;
      --color-card: #ffffff;
      --shadow-sm: 0 1px 3px rgba(0,0,0,0.08);
      --shadow-md: 0 4px 12px rgba(0,0,0,0.1);
      --radius: 8px;
    }

    [data-theme="dark"] {
      --color-bg: #0f172a;
      --color-bg-secondary: #1e293b;
      --color-text: #f1f5f9;
      --color-text-secondary: #94a3b8;
      --color-primary: #60a5fa;
      --color-primary-hover: #93bbfd;
      --color-border: #334155;
      --color-card: #1e293b;
      --shadow-sm: 0 1px 3px rgba(0,0,0,0.3);
      --shadow-md: 0 4px 12px rgba(0,0,0,0.4);
    }

    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      background: var(--color-bg);
      color: var(--color-text);
      line-height: 1.6;
      transition: background 0.3s ease, color 0.3s ease;
    }

    /* HEADER */
    .header {
      background: var(--color-bg-secondary);
      border-bottom: 1px solid var(--color-border);
      padding: 16px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .logo { font-size: 1.3rem; font-weight: 700; color: var(--color-primary); }

    /* BOTÓN DE TOGGLE DE TEMA */
    .theme-toggle {
      background: var(--color-bg);
      border: 1px solid var(--color-border);
      color: var(--color-text);
      padding: 8px 16px;
      border-radius: var(--radius);
      cursor: pointer;
      font-weight: 600;
      font-size: 0.9rem;
      display: flex;
      align-items: center;
      gap: 8px;
      transition: background 0.2s, transform 0.15s;
    }
    .theme-toggle:hover { transform: scale(1.05); }
    .theme-toggle:focus-visible { outline: 3px solid var(--color-primary); outline-offset: 2px; }
    .theme-toggle .icono { font-size: 1.2rem; }

    /* CONTENIDO PRINCIPAL */
    main { max-width: 900px; margin: 0 auto; padding: 40px 24px; }
    h1 { color: var(--color-primary); margin-bottom: 8px; }
    h2 { margin-top: 32px; margin-bottom: 16px; }
    p { margin-bottom: 16px; color: var(--color-text); }

    /* CARDS */
    .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 24px; margin-top: 32px; }
    .card {
      background: var(--color-card);
      border: 1px solid var(--color-border);
      border-radius: var(--radius);
      padding: 24px;
      box-shadow: var(--shadow-sm);
      transition: box-shadow 0.2s;
    }
    .card:hover { box-shadow: var(--shadow-md); }
    .card h3 { color: var(--color-primary); margin-bottom: 8px; }
    .card p { color: var(--color-text-secondary); font-size: 0.92rem; }

    /* FOOTER */
    footer {
      text-align: center; padding: 24px; color: var(--color-text-secondary);
      border-top: 1px solid var(--color-border);
    }
  </style>
</head>
<body>
  <header class="header">
    <span class="logo">CSS Variables Demo</span>
    <!-- BOTÓN DE CAMBIO DE TEMA: ejecuta toggleTheme() al hacer clic -->
    <button class="theme-toggle" onclick="toggleTheme()" aria-label="Cambiar tema claro/oscuro">
      <span class="icono" id="icono-tema">☀️</span>
      <span id="texto-tema">Modo Oscuro</span>
    </button>
  </header>

  <main>
    <h1>Sistema de Temas con Variables CSS</h1>
    <p>
      Esta página demuestra un sistema completo de temas claro/oscuro implementado
      exclusivamente con variables CSS (Custom Properties) y unas pocas líneas de
      JavaScript. El cambio entre temas es instantáneo porque solo se modifican
      los valores de las variables, no se recargan hojas de estilo completas.
    </p>

    <h2>Características del Sistema</h2>
    <div class="grid">
      <div class="card">
        <h3>Variables Dinámicas</h3>
        <p>Las Custom Properties se actualizan en tiempo real al cambiar el atributo <code>data-theme</code> en el elemento <code>&lt;html&gt;</code>. Todos los elementos que usan <code>var()</code> se actualizan automáticamente.</p>
      </div>
      <div class="card">
        <h3>Transiciones Suaves</h3>
        <p>El body tiene <code>transition: background 0.3s, color 0.3s</code> para una transición visual agradable entre temas.</p>
      </div>
      <div class="card">
        <h3>Persistencia Opcional</h3>
        <p>Se puede guardar la preferencia del usuario en <code>localStorage</code> para mantener el tema elegido entre visitas.</p>
      </div>
    </div>
  </main>

  <footer>
    <p>Variables CSS (Custom Properties) - Ejemplo didáctico del módulo DIW</p>
  </footer>

  <script>
    /*
     * SISTEMA DE CAMBIO DE TEMA CLARO/OSCURO
     * Cambia el atributo data-theme en <html> entre "light" y "dark"
     * Las variables CSS en :root y [data-theme] hacen el resto
     */
    function toggleTheme() {
      const html = document.documentElement;
      const temaActual = html.getAttribute('data-theme');
      const nuevoTema = temaActual === 'dark' ? 'light' : 'dark';

      // Cambiar el atributo data-theme en <html>
      // Esto activa las variables del tema correspondiente
      html.setAttribute('data-theme', nuevoTema);

      // Actualizar los iconos y texto del botón
      const icono = document.getElementById('icono-tema');
      const texto = document.getElementById('texto-tema');

      if (nuevoTema === 'dark') {
        icono.textContent = '🌙';
        texto.textContent = 'Modo Claro';
        // Actualizar meta theme-color para la barra del navegador
        document.querySelector('meta[name="theme-color"]').content = '#0f172a';
      } else {
        icono.textContent = '☀️';
        texto.textContent = 'Modo Oscuro';
        document.querySelector('meta[name="theme-color"]').content = '#ffffff';
      }

      // OPCIONAL: Guardar preferencia en localStorage
      localStorage.setItem('tema', nuevoTema);
    }

    // Al cargar la página, aplicar el tema guardado (si existe)
    document.addEventListener('DOMContentLoaded', function() {
      const temaGuardado = localStorage.getItem('tema');
      if (temaGuardado) {
        document.documentElement.setAttribute('data-theme', temaGuardado);
        const icono = document.getElementById('icono-tema');
        const texto = document.getElementById('texto-tema');
        if (temaGuardado === 'dark') {
          icono.textContent = '🌙';
          texto.textContent = 'Modo Claro';
          document.querySelector('meta[name="theme-color"]').content = '#0f172a';
        }
      }

      // Detectar preferencia del sistema operativo
      const prefiereOscuro = window.matchMedia('(prefers-color-scheme: dark)').matches;
      if (!temaGuardado && prefiereOscuro) {
        document.documentElement.setAttribute('data-theme', 'dark');
        document.getElementById('icono-tema').textContent = '🌙';
        document.getElementById('texto-tema').textContent = 'Modo Claro';
      }
    });
  </script>
</body>
</html>
```

### Ejemplo 3: Layout responsivo con clamp(), min(), max()

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Clamp, Min, Max | Ejemplo Didáctico</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      background: #f8fafc; color: #1e293b; line-height: 1.6;
    }

    /* TIPOGRAFÍA FLUIDA CON clamp() */
    h1 { font-size: clamp(1.5rem, 5vw, 3rem); }
    h2 { font-size: clamp(1.2rem, 3vw, 2rem); }
    p  { font-size: clamp(0.9rem, 1.5vw, 1.1rem); }

    /* ANCHO MÁXIMO CON min() */
    .contenedor {
      /* El ancho será 100% o 900px, lo que sea menor */
      width: min(100%, 900px);
      margin: 0 auto;
      padding: 40px 20px;
    }

    /* ESPACIADO FLUIDO CON clamp() */
    section {
      /* El padding crece con el viewport entre 20px y 60px */
      padding: clamp(20px, 5vw, 60px) 0;
    }

    /* TARJETAS CON TAMAÑO MÍNIMO USANDO max() */
    .tarjeta {
      /* El ancho mínimo es 250px, pero puede crecer */
      width: max(250px, 30%);
      background: #fff;
      padding: 24px;
      border-radius: 8px;
      box-shadow: 0 1px 4px rgba(0,0,0,0.06);
    }

    /* CALC() PARA SIDEBAR + CONTENIDO */
    .layout-sidebar {
      display: flex;
      gap: 24px;
      flex-wrap: wrap;
    }
    .sidebar {
      /* Sidebar: ancho fijo de 250px */
      flex: 0 0 250px;
    }
    .contenido-sidebar {
      /* Contenido: resto del espacio menos el gap */
      flex: 1 1 calc(100% - 274px);
      min-width: 300px;
    }

    h1 { color: #2563eb; text-align: center; margin-bottom: 32px; }
    h2 { color: #334155; margin-bottom: 16px; margin-top: 32px; }
    pre {
      background: #1e293b; color: #e2e8f0; padding: 16px;
      border-radius: 8px; overflow-x: auto; font-size: 0.85rem;
      margin: 16px 0;
    }
  </style>
</head>
<body>
  <div class="contenedor">
    <h1>Funciones CSS Modernas: clamp(), min(), max(), calc()</h1>
    <p>
      Este texto usa tipografía fluida con <code>clamp()</code>. Redimensiona la
      ventana del navegador y verás cómo el tamaño de fuente se ajusta automáticamente
      entre un mínimo y un máximo, escalando suavemente con el viewport.
    </p>

    <section>
      <h2>Tipografía Fluida</h2>
      <pre>h1 { font-size: clamp(1.5rem, 5vw, 3rem); }
h2 { font-size: clamp(1.2rem, 3vw, 2rem); }
p  { font-size: clamp(0.9rem, 1.5vw, 1.1rem); }</pre>
      <p>La función <code>clamp(min, ideal, max)</code> es perfecta para tipografía responsive sin media queries. El texto nunca será menor que <code>min</code> ni mayor que <code>max</code>.</p>
    </section>

    <section>
      <h2>Ancho del Contenedor con min()</h2>
      <pre>.contenedor { width: min(100%, 900px); }</pre>
      <p><code>min()</code> elige el valor más pequeño. En pantallas grandes, el contenedor mide 900px. En pantallas pequeñas, mide el 100% del ancho disponible.</p>
    </section>

    <section>
      <h2>Layout con calc()</h2>
      <pre>.sidebar { flex: 0 0 250px; }
.contenido-sidebar { flex: 1 1 calc(100% - 274px); }</pre>
      <p><code>calc()</code> permite mezclar unidades. Aquí calculamos el espacio restante restando el sidebar (250px) + gap (24px) del ancho total.</p>
    </section>
  </div>
</body>
</html>
```

### Ejemplo 4: Organización con BEM y @layer

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>BEM y @layer | Ejemplo Didáctico</title>
  <style>
    /* =============================================
       ORGANIZACIÓN CON @LAYER
       El orden de las capas define la prioridad.
       La última capa declarada tiene mayor prioridad,
       independientemente de la especificidad.
       ============================================= */

    /* Capa 1: Reset (menor prioridad) */
    @layer reset {
      *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
      img { max-width: 100%; height: auto; display: block; }
    }

    /* Capa 2: Base - estilos de elementos HTML */
    @layer base {
      body {
        font-family: 'Segoe UI', system-ui, sans-serif;
        line-height: 1.6; color: #1e293b; background: #f8fafc;
      }
      a { color: #2563eb; }
      h2 { font-size: 1.4rem; margin-bottom: 12px; }
    }

    /* Capa 3: Componentes - bloques BEM */
    @layer components {
      /* BLOQUE: card */
      .card {
        background: #fff; border-radius: 8px;
        box-shadow: 0 1px 4px rgba(0,0,0,0.06); padding: 24px;
      }

      /* ELEMENTO: card__title */
      .card__title { color: #1e293b; font-size: 1.1rem; margin-bottom: 8px; }

      /* ELEMENTO: card__body */
      .card__body { color: #64748b; font-size: 0.92rem; }

      /* MODIFICADOR: card--featured */
      .card--featured {
        border-left: 4px solid #2563eb;
        background: #eff6ff;
      }

      /* BLOQUE: btn */
      .btn {
        display: inline-block; padding: 10px 20px; border-radius: 6px;
        font-weight: 600; text-decoration: none; border: none; cursor: pointer;
        font-size: 0.9rem; transition: background 0.2s, transform 0.1s;
      }
      /* ELEMENTO: btn__icon */
      .btn__icon { margin-right: 6px; }
      /* MODIFICADOR: btn--primary */
      .btn--primary { background: #2563eb; color: #fff; }
      .btn--primary:hover { background: #1d4ed8; }
      /* MODIFICADOR: btn--outline */
      .btn--outline { background: transparent; border: 2px solid #2563eb; color: #2563eb; }
      .btn--outline:hover { background: #2563eb; color: #fff; }
    }

    /* Capa 4: Utilidades (máxima prioridad) */
    @layer utilities {
      .text-center { text-align: center !important; }
      .mt-1 { margin-top: 8px; }
      .mt-2 { margin-top: 16px; }
      .mt-3 { margin-top: 24px; }
    }

    /* Layout de la demo */
    .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px; max-width: 900px; margin: 0 auto; padding: 40px 20px; }
    h1 { text-align: center; margin: 32px 0; color: #2563eb; }
  </style>
</head>
<body>
  <h1>Metodología BEM + Capas @layer</h1>

  <div class="grid">
    <!-- Tarjeta normal con BEM -->
    <article class="card">
      <h3 class="card__title">Tarjeta Normal</h3>
      <p class="card__body">Esta tarjeta usa la metodología BEM: bloque <code>.card</code>, elemento <code>.card__title</code>, elemento <code>.card__body</code>. Los selectores son planos y de baja especificidad.</p>
      <a href="#" class="btn btn--primary mt-2">
        <span class="btn__icon">→</span> Acción Principal
      </a>
    </article>

    <!-- Tarjeta destacada (modificador BEM) -->
    <article class="card card--featured">
      <h3 class="card__title">Tarjeta Destacada</h3>
      <p class="card__body">Modificador <code>.card--featured</code>: añade borde izquierdo azul y fondo azul claro. Los modificadores BEM extienden bloques sin crear nuevos bloques.</p>
      <a href="#" class="btn btn--outline mt-2">
        <span class="btn__icon">☆</span> Acción Secundaria
      </a>
    </article>

    <!-- Tarjeta con utilidades -->
    <article class="card text-center">
      <h3 class="card__title">Utilidades @layer</h3>
      <p class="card__body">La clase <code>.text-center</code> está en la capa <code>utilities</code>, la última declarada. Por tanto, gana a cualquier otro estilo, incluso sin <code>!important</code> en los componentes.</p>
      <p class="card__body mt-2">Las capas <code>@layer</code> permiten controlar la cascada sin abusar de <code>!important</code>.</p>
    </article>
  </div>
</body>
</html>
```

### Ejemplo 5: Transiciones y animaciones con prefers-reduced-motion

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Transiciones y Animaciones | Ejemplo Didáctico</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      background: #f8fafc; color: #1e293b; line-height: 1.6;
      padding: 40px 20px;
    }
    .contenedor { max-width: 800px; margin: 0 auto; }
    h1 { color: #2563eb; margin-bottom: 32px; text-align: center; }
    h2 { color: #334155; margin: 32px 0 16px; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px; }

    /* ==========================================
       EJEMPLO 1: TRANSICIONES CON HOVER
       ========================================== */
    .btn-transicion {
      display: inline-block; padding: 12px 28px;
      background: #2563eb; color: #fff; border: none; border-radius: 6px;
      font-weight: 600; font-size: 1rem; cursor: pointer;
      /* Transición: propiedad duración función-de-tiempo */
      transition: background 0.3s ease, transform 0.2s ease, box-shadow 0.3s ease;
    }
    .btn-transicion:hover {
      background: #1d4ed8;
      transform: translateY(-2px);
      box-shadow: 0 4px 12px rgba(37,99,235,0.3);
    }
    .btn-transicion:active {
      transform: translateY(0);
    }

    /* ==========================================
       EJEMPLO 2: ANIMACIÓN CON @KEYFRAMES
       ========================================== */
    @keyframes entradaDesdeArriba {
      from {
        opacity: 0;
        transform: translateY(-30px);
      }
      to {
        opacity: 1;
        transform: translateY(0);
      }
    }

    @keyframes pulso {
      0%, 100% { transform: scale(1); }
      50% { transform: scale(1.05); }
    }

    @keyframes giro {
      from { transform: rotate(0deg); }
      to { transform: rotate(360deg); }
    }

    .animada-entrada {
      animation: entradaDesdeArriba 0.6s ease-out both;
    }
    .animada-pulso {
      animation: pulso 2s ease-in-out infinite;
      display: inline-block;
      padding: 8px 16px; background: #dbeafe; border-radius: 20px;
      font-weight: 600; color: #2563eb;
    }
    .animada-giro {
      animation: giro 3s linear infinite;
      display: inline-block; font-size: 2rem;
    }

    /* Retrasos escalonados para animación de tarjetas */
    .tarjeta:nth-child(1) { animation-delay: 0s; }
    .tarjeta:nth-child(2) { animation-delay: 0.15s; }
    .tarjeta:nth-child(3) { animation-delay: 0.3s; }

    .tarjeta {
      background: #fff; padding: 20px; border-radius: 8px;
      box-shadow: 0 1px 4px rgba(0,0,0,0.06); margin-bottom: 12px;
    }

    /* ==========================================
       ACCESIBILIDAD: PREFERS-REDUCED-MOTION
       Respeta la preferencia del sistema operativo
       para reducir animaciones y movimientos.
       ========================================== */
    @media (prefers-reduced-motion: reduce) {
      *, *::before, *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
      }
    }

    /* Toggle de animación */
    .toggle-anim {
      display: flex; align-items: center; gap: 12px; margin: 24px 0;
      padding: 16px; background: #fff; border-radius: 8px;
      box-shadow: 0 1px 3px rgba(0,0,0,0.06);
    }
    .toggle-anim button {
      padding: 8px 16px; background: #2563eb; color: #fff;
      border: none; border-radius: 4px; cursor: pointer;
    }
  </style>
</head>
<body>
  <div class="contenedor">
    <h1>Transiciones y Animaciones CSS</h1>

    <h2>1. Transición en Botón (hover)</h2>
    <button class="btn-transicion">Pasa el ratón sobre mí</button>
    <p style="margin-top:8px;color:#64748b;font-size:0.9rem;">
      El botón cambia de color, se eleva 2px y gana sombra. Todo suavizado con <code>transition</code>.
    </p>

    <h2>2. Animaciones con @keyframes</h2>
    <p>
      <span class="animada-giro">⚙️</span>
      Giro continuo con <code>animation: giro 3s linear infinite</code>.
    </p>
    <p style="margin-top:12px;">
      <span class="animada-pulso">🔔 Nueva oferta</span>
      Pulso con <code>animation: pulso 2s ease-in-out infinite</code>.
    </p>

    <h2>3. Entrada Escalonada (Stagger)</h2>
    <div class="tarjeta animada-entrada">
      <strong>Tarjeta 1:</strong> Entra con animación, delay 0s.
    </div>
    <div class="tarjeta animada-entrada">
      <strong>Tarjeta 2:</strong> Entra con animación, delay 0.15s.
    </div>
    <div class="tarjeta animada-entrada">
      <strong>Tarjeta 3:</strong> Entra con animación, delay 0.3s. Efecto de cascada visual.
    </div>

    <h2>4. Accesibilidad: prefers-reduced-motion</h2>
    <p>
      Si tu sistema operativo tiene activada la opción "Reducir movimientos",
      todas las animaciones de esta página se detendrán automáticamente. Esto
      es un requisito de accesibilidad WCAG 2.2 (Criterio 2.3.3).
    </p>
    <p style="font-size:0.85rem;color:#64748b;">
      Para probarlo en Windows: Configuración → Accesibilidad → Efectos visuales → Mostrar animaciones.
      En macOS: Preferencias del Sistema → Accesibilidad → Reducir movimiento.
    </p>
  </div>
</body>
</html>
```

### Ejemplo 6: Técnicas de centrado

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Técnicas de Centrado CSS | Ejemplo Didáctico</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      background: #f8fafc; color: #1e293b; line-height: 1.6;
      padding: 40px 20px;
    }
    .contenedor { max-width: 800px; margin: 0 auto; }
    h1 { color: #2563eb; margin-bottom: 32px; text-align: center; }
    h2 { margin: 32px 0 16px; color: #334155; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px; }

    /* CAJA DEMOSTRATIVA */
    .demo-box {
      border: 2px dashed #94a3b8; border-radius: 8px;
      margin-bottom: 16px; min-height: 150px; position: relative;
      background: #fff;
    }
    .demo-box .hijo {
      background: #2563eb; color: #fff; padding: 16px 24px;
      border-radius: 4px; font-weight: 600; text-align: center;
    }

    /* 1. FLEXBOX: centrado perfecto */
    .centro-flex {
      display: flex;
      justify-content: center;
      align-items: center;
    }

    /* 2. GRID: place-items (shorthand para align-items + justify-items) */
    .centro-grid {
      display: grid;
      place-items: center;
    }

    /* 3. ABSOLUTE + TRANSFORM: centrado sobre padre relative */
    .centro-absolute .hijo {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
    }

    /* 4. MARGIN AUTO: centrado horizontal (elemento de bloque con ancho definido) */
    .centro-margin .hijo {
      width: fit-content;
      margin: 0 auto;
      margin-top: 50px; /* Solo para esta demo visual */
    }

    /* 5. TEXT-ALIGN + LINE-HEIGHT: centrado texto inline */
    .centro-texto {
      text-align: center;
      line-height: 150px; /* Igual a la altura del contenedor */
    }

    pre {
      background: #1e293b; color: #e2e8f0; padding: 12px;
      border-radius: 6px; font-size: 0.85rem; margin-top: 8px;
      overflow-x: auto;
    }
    code { font-family: 'Fira Code', 'Cascadia Code', monospace; }
  </style>
</head>
<body>
  <div class="contenedor">
    <h1>6 Técnicas de Centrado en CSS</h1>

    <h2>1. Flexbox</h2>
    <div class="demo-box centro-flex">
      <div class="hijo">Centrado con Flexbox</div>
    </div>
    <pre>.padre { display: flex; justify-content: center; align-items: center; }</pre>
    <p>La técnica más versátil y recomendada actualmente. Funciona con uno o múltiples hijos y en ambas direcciones.</p>

    <h2>2. CSS Grid</h2>
    <div class="demo-box centro-grid">
      <div class="hijo">Centrado con Grid</div>
    </div>
    <pre>.padre { display: grid; place-items: center; }</pre>
    <p><code>place-items</code> es el shorthand de <code>align-items</code> + <code>justify-items</code>. Ideal para centrar contenido en una celda grid.</p>

    <h2>3. Absolute + Transform</h2>
    <div class="demo-box centro-absolute">
      <div class="hijo">Centrado con Absolute</div>
    </div>
    <pre>.hijo { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); }
.padre { position: relative; } /* Necesario como referencia */</pre>
    <p>Técnica clásica pre-flexbox. El 50% posiciona la esquina superior izquierda en el centro del padre; <code>translate(-50%, -50%)</code> retrocede la mitad del ancho y alto del propio elemento.</p>

    <h2>4. Margin Auto (solo horizontal)</h2>
    <div class="demo-box centro-margin">
      <div class="hijo">Centrado horizontal</div>
    </div>
    <pre>.hijo { width: fit-content; margin: 0 auto; }</pre>
    <p>La técnica más antigua. Solo centra horizontalmente. Requiere que el elemento tenga un ancho definido.</p>

    <h2>5. Text-Align + Line-Height (texto inline)</h2>
    <div class="demo-box centro-texto">
      Texto centrado en ambas direcciones
    </div>
    <pre>.padre { text-align: center; line-height: 150px; } /* line-height = altura del contenedor */</pre>
    <p>Solo válido para contenido de texto inline. <code>line-height</code> igual a la altura centra verticalmente una sola línea de texto.</p>
  </div>
</body>
</html>
```

### Ejemplo 7: Tooltips CSS puro con ::before/::after

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Tooltips CSS Puro | Ejemplo Didáctico</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      background: #f8fafc; color: #1e293b; line-height: 1.6;
      padding: 60px 20px; display: flex; justify-content: center;
      gap: 40px; flex-wrap: wrap;
    }
    h1 { width: 100%; text-align: center; color: #2563eb; margin-bottom: 32px; }
    h2 { width: 100%; text-align: center; color: #64748b; font-weight: 400; margin-bottom: 24px; }

    /* =============================================
       TOOLTIP CSS PURO
       Usa ::after para el contenido del tooltip
       y ::before para la flecha triangular
       ============================================= */

    /* Botón base que activa el tooltip */
    .tooltip-trigger {
      position: relative; /* Necesario para posicionar el tooltip respecto a este elemento */
      padding: 12px 24px; background: #2563eb; color: #fff;
      border: none; border-radius: 6px; cursor: pointer;
      font-weight: 600; font-size: 0.95rem;
    }

    /* Tooltip (::after): se muestra al hacer hover/focus en el trigger */
    .tooltip-trigger::after {
      /* Contenido del tooltip definido mediante un atributo data-tooltip */
      content: attr(data-tooltip);

      /* Posicionamiento: centrado encima del trigger */
      position: absolute;
      bottom: calc(100% + 10px); /* Encima del trigger + 10px de separación */
      left: 50%;
      transform: translateX(-50%);

      /* Estilos visuales */
      background: #1e293b; color: #fff; padding: 8px 14px;
      border-radius: 6px; font-size: 0.82rem; white-space: nowrap;
      font-weight: 400;

      /* Oculto por defecto */
      opacity: 0; visibility: hidden;
      transition: opacity 0.2s ease, visibility 0.2s ease;

      /* Puntero: se asegura de que el tooltip no interfiera con clicks */
      pointer-events: none;
    }

    /* Flecha triangular (::before) del tooltip */
    .tooltip-trigger::before {
      content: "";
      position: absolute;
      bottom: calc(100% + 4px); /* Justo encima del trigger */
      left: 50%;
      transform: translateX(-50%);

      /* Triángulo CSS: bordes transparentes excepto el inferior */
      border: 6px solid transparent;
      border-top-color: #1e293b;

      opacity: 0; visibility: hidden;
      transition: opacity 0.2s ease, visibility 0.2s ease;
    }

    /* Mostrar tooltip y flecha al hacer hover O focus */
    .tooltip-trigger:hover::after,
    .tooltip-trigger:hover::before,
    .tooltip-trigger:focus-visible::after,
    .tooltip-trigger:focus-visible::before {
      opacity: 1; visibility: visible;
    }

    /* Tooltip desde abajo (variante) */
    .tooltip-abajo::after {
      bottom: auto; top: calc(100% + 10px);
    }
    .tooltip-abajo::before {
      bottom: auto; top: calc(100% + 4px);
      border-top-color: transparent; border-bottom-color: #1e293b;
    }

    /* Tooltip desde la derecha (variante) */
    .tooltip-derecha::after {
      bottom: auto; left: calc(100% + 10px); top: 50%;
      transform: translateY(-50%);
    }
    .tooltip-derecha::before {
      bottom: auto; left: calc(100% + 4px); top: 50%;
      transform: translateY(-50%);
      border-top-color: transparent; border-left-color: #1e293b;
    }
  </style>
</head>
<body>
  <h1>Tooltips CSS Puro</h1>
  <h2>Sin JavaScript, usando ::before, ::after y data attributes</h2>

  <!-- Tooltip superior (por defecto) -->
  <button class="tooltip-trigger" data-tooltip="Este es un tooltip superior" aria-label="Botón con tooltip superior">
    Tooltip Superior
  </button>

  <!-- Tooltip inferior -->
  <button class="tooltip-trigger tooltip-abajo" data-tooltip="Tooltip que aparece debajo" aria-label="Botón con tooltip inferior">
    Tooltip Inferior
  </button>

  <!-- Tooltip lateral derecho -->
  <button class="tooltip-trigger tooltip-derecha" data-tooltip="Tooltip a la derecha" aria-label="Botón con tooltip derecho">
    Tooltip Derecha
  </button>
</body>
</html>
```

### Ejemplo 8: Contadores CSS para numeración automática

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Contadores CSS | Ejemplo Didáctico</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      background: #f8fafc; color: #1e293b; line-height: 1.7;
      padding: 40px 20px;
    }
    .contenedor { max-width: 800px; margin: 0 auto; }
    h1 { color: #2563eb; margin-bottom: 8px; }
    .intro { color: #64748b; margin-bottom: 32px; }
    h2 { margin: 32px 0 16px; color: #334155; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px; }

    /* ==========================================
       CONTADORES CSS
       counter-reset: inicializa un contador
       counter-increment: incrementa el contador
       counter(): muestra el valor del contador
       ========================================== */

    /* EJEMPLO 1: Lista numerada personalizada */
    .lista-numerada {
      counter-reset: item;
      list-style: none;
    }
    .lista-numerada li {
      counter-increment: item;
      padding: 12px 16px;
      background: #fff;
      border-radius: 6px;
      margin-bottom: 8px;
      box-shadow: 0 1px 3px rgba(0,0,0,0.06);
    }
    .lista-numerada li::before {
      content: counter(item);
      display: inline-block;
      width: 28px; height: 28px;
      background: #2563eb; color: #fff; border-radius: 50%;
      text-align: center; line-height: 28px;
      font-weight: 700; font-size: 0.85rem;
      margin-right: 12px;
    }

    /* EJEMPLO 2: Numeración de figuras con prefijo "Figura X:" */
    .seccion-figuras {
      counter-reset: figura;
    }
    .seccion-figuras figure {
      counter-increment: figura;
      margin-bottom: 16px;
      background: #fff;
      padding: 16px;
      border-radius: 8px;
    }
    .seccion-figuras figcaption::before {
      content: "Figura " counter(figura) ": ";
      font-weight: 700;
      color: #2563eb;
    }

    /* EJEMPLO 3: Contador jerárquico (sección.subsección) */
    .contenido-jerarquico {
      counter-reset: seccion;
    }
    .contenido-jerarquico h2 {
      counter-reset: subseccion;
      counter-increment: seccion;
    }
    .contenido-jerarquico h2::before {
      content: counter(seccion) ". ";
      color: #2563eb;
    }
    .contenido-jerarquico h3 {
      counter-increment: subseccion;
    }
    .contenido-jerarquico h3::before {
      content: counter(seccion) "." counter(subseccion) " ";
      color: #64748b;
    }

    pre {
      background: #1e293b; color: #e2e8f0; padding: 12px;
      border-radius: 6px; font-size: 0.85rem; margin: 8px 0;
      overflow-x: auto;
    }
  </style>
</head>
<body>
  <div class="contenedor">
    <h1>Contadores CSS</h1>
    <p class="intro">
      Los contadores CSS permiten numerar elementos automáticamente sin modificar
      el HTML. Son ideales para listas numeradas personalizadas, numeración de
      figuras, secciones jerárquicas y cualquier contenido que requiera numeración
      dinámica que se actualice automáticamente.
    </p>

    <h2>Lista Numerada Personalizada</h2>
    <ol class="lista-numerada">
      <li>Primer elemento de la lista con número circular azul</li>
      <li>Segundo elemento: los números se generan con <code>counter-increment</code></li>
      <li>Tercer elemento: si añades o quitas elementos, la numeración se recalcula automáticamente</li>
      <li>Cuarto elemento: los estilos del número se controlan completamente con CSS</li>
    </ol>
    <pre>counter-reset: item;           /* Inicializa el contador */
counter-increment: item;       /* Incrementa en cada li */
content: counter(item);       /* Muestra el valor actual */</pre>

    <h2>Numeración de Figuras</h2>
    <div class="seccion-figuras">
      <figure>
        <figcaption>Diagrama de arquitectura del sistema</figcaption>
      </figure>
      <figure>
        <figcaption>Mockup de la interfaz de usuario</figcaption>
      </figure>
      <figure>
        <figcaption>Flujo de navegación entre pantallas</figcaption>
      </figure>
    </div>

    <h2>Numeración Jerárquica (sección.subsección)</h2>
    <div class="contenido-jerarquico">
      <h2>Introducción</h2>
      <h3>Objetivos</h3>
      <h3>Alcance</h3>
      <h2>Desarrollo</h2>
      <h3>Metodología</h3>
      <h3>Implementación</h3>
      <h2>Conclusiones</h2>
    </div>
  </div>
</body>
</html>
```

## Casos reales

### Caso Real 1: Sistema de diseño de Stripe (stripe.com)

!!! example "Caso real: Stripe"
    Stripe utiliza un enfoque sofisticado de variables CSS para su sistema de diseño.

    - Definen cientos de **custom properties** en `:root` que controlan colores, espaciados, tipografía, sombras y bordes.
    - Su sistema de temas es particularmente avanzado: utilizan variables para cada token de diseño y cambian entre temas claro/oscuro modificando las variables a nivel de `:root`.
    - Emplean `@layer` para organizar su CSS en capas lógicas (reset, base, componentes, utilidades), y sus componentes siguen una metodología similar a **BEM** con nombres descriptivos.
    - Hacen uso extensivo de `:focus-visible` para accesibilidad con teclado y `prefers-reduced-motion` para respetar preferencias de animación del usuario.
    - Sus animaciones son sutiles y funcionales, utilizando `transition` para micro-interacciones en botones y formularios.

### Caso Real 2: Tailwind CSS en Vercel (vercel.com)

!!! example "Caso real: Vercel con Tailwind CSS"
    Vercel utiliza **Tailwind CSS**, el framework utility-first más popular.

    - Su HTML está lleno de clases utilitarias como `flex`, `items-center`, `gap-4`, `p-6`.
    - Este enfoque elimina completamente los problemas de especificidad y naming, pero requiere disciplina en la organización del HTML.
    - Vercel combina Tailwind con variables CSS para temas y utiliza `dark:` prefix para modo oscuro.
    - Las animaciones y transiciones se manejan con clases de Tailwind (`transition-all`, `duration-200`, `hover:scale-105`).
    - El CSS final en producción es notablemente pequeño gracias al purgado de clases no utilizadas.

### Caso Real 3: GitHub - CSS a escala masiva con Primer Design System

!!! example "Caso real: GitHub Primer"
    GitHub mantiene **Primer**, su sistema de diseño open source.

    - Utilizan **CSS Modules** para encapsular estilos por componente, complementado con variables CSS globales para tokens de diseño.
    - Su arquitectura CSS incluye capas de utilidades, componentes y temas.
    - Hacen uso intensivo de `:focus-visible` y `prefers-reduced-motion`.
    - Las animaciones son mínimas y funcionales.
    - Su sistema de color soporta múltiples temas (light, dark, high contrast, daltonismo) implementados mediante variables CSS intercambiables.
    - Es un ejemplo de CSS a escala empresarial con cientos de componentes mantenidos por equipos distribuidos globalmente.

## Actividades guiadas

### Actividad Guiada 1: Sistema de temas claro/oscuro con variables CSS

- **RA:** RA2
- **Objetivo:** Implementar un sistema completo de temas intercambiables usando variables CSS y JavaScript, incluyendo persistencia en localStorage y detección de preferencia del sistema.
- **Enunciado:** Crea una página web con al menos header, contenido principal (cards) y footer. Define todas las variables de color, fondo, texto, bordes, sombras y radios en `:root` para el tema claro y en `[data-theme="dark"]` para el tema oscuro. Implementa un botón toggle que cambie `data-theme` en `<html>`. Persiste la elección en localStorage. Detecta `prefers-color-scheme` al cargar la página. Todas las transiciones de color deben ser suaves.
- **Criterios:** Variables completas para ambos temas (3 puntos), toggle funcional con JS (2 puntos), persistencia localStorage (2 puntos), detección preferencia sistema (2 puntos), transiciones suaves (1 punto).

### Actividad Guiada 2: Galería de cards con BEM y animaciones

- **RA:** RA2
- **Objetivo:** Aplicar la metodología BEM para crear una galería de tarjetas con animaciones de entrada y efectos hover.
- **Enunciado:** Diseña 6 tarjetas de cursos usando BEM (bloque `.course-card`, elementos `__image`, `__title`, `__description`, `__price`, `__badge`, modificadores `--featured`, `--sold-out`). Aplica `@keyframes` para animaciones de entrada escalonadas. Efectos hover con `transition` en sombra y transform. Respeta `prefers-reduced-motion`.
- **Criterios:** BEM correcto en los 6 componentes (4 puntos), animaciones de entrada escalonadas (2 puntos), efectos hover con transition (2 puntos), prefers-reduced-motion implementado (1 punto), responsive (1 punto).

### Actividad Guiada 3: Tipografía fluida con clamp()

- **RA:** RA2
- **Objetivo:** Implementar un sistema de tipografía completamente fluida usando clamp() como alternativa a media queries.
- **Enunciado:** Construye una landing page donde todos los tamaños de fuente, espaciados y dimensiones usen `clamp()`. Aplica tipografía fluida a h1, h2, h3, p, y también a paddings y gaps. Usa `min()` para anchos máximos de contenedor y `max()` para anchos mínimos de elementos. La página debe ser legible desde 320px hasta 2560px sin usar una sola media query.
- **Criterios:** Tipografía fluida correcta en todos los niveles (3 puntos), espaciados fluidos (2 puntos), min()/max() correctos (2 puntos), legibilidad en todo el rango 320px-2560px sin media queries (3 puntos).

### Actividad Guiada 4: Tooltips y decoraciones con pseudoelementos

- **RA:** RA2
- **Objetivo:** Crear elementos decorativos y funcionales usando exclusivamente ::before y ::after, sin modificar el HTML.
- **Enunciado:** Crea una página que muestre: (1) tooltips en botones usando `attr(data-tooltip)` en `::after`, (2) iconos decorativos antes de enlaces externos con `::before`, (3) un efecto de subrayado animado en enlaces con `::after`, (4) contadores CSS para numerar figuras automáticamente, (5) badges de notificación usando `::after` con `content: attr(data-count)`. Todo sin JavaScript (excepto los contadores dinámicos).
- **Criterios:** Tooltips funcionales con ::after (2 puntos), decoraciones de enlaces (2 puntos), subrayado animado (2 puntos), contadores CSS (2 puntos), badges con attr() (2 puntos).

### Actividad Guiada 5: Dashboard con transiciones y animaciones

- **RA:** RA2
- **Objetivo:** Crear un panel de control con animaciones de entrada, micro-interacciones y gestión de estados de carga.
- **Enunciado:** Diseña un dashboard con: header, sidebar, área de contenido con 4 cards de estadísticas. Las cards deben entrar con animación escalonada al cargar. Implementa animación de pulso en indicadores de "en vivo". Usa transiciones en hover de cards (elevación + sombra). Añade un skeleton loader animado para simular carga. Respeta prefers-reduced-motion.
- **Criterios:** Animaciones de entrada (2 puntos), micro-interacciones hover (2 puntos), skeleton loader (2 puntos), prefers-reduced-motion (2 puntos), diseño responsive (2 puntos).

## Actividades propuestas

### Actividad Propuesta 1: Refactorización de CSS legacy a CSS moderno

- **RA:** RA2
- **Objetivo:** Transformar una hoja de estilos legacy (con !important, selectores anidados profundos, unidades absolutas) en CSS moderno usando variables, @layer, unidades relativas y selectores planos.
- **Enunciado:** Se proporciona una hoja de estilos de 200 líneas con malas prácticas. Refactorízala aplicando: variables CSS para colores y espaciados, capas @layer para organizar por prioridad, sustitución de px por rem/em, selectores BEM planos, sustitución de !important por capas, y tipografía fluida con clamp(). La apariencia visual final debe ser idéntica.
- **Criterios:** Variables CSS bien organizadas (3 puntos), @layer correcto (3 puntos), unidades relativas (2 puntos), sin !important (2 puntos).

### Actividad Propuesta 2: Componente de acordeón animado CSS puro

- **RA:** RA2
- **Objetivo:** Crear un componente acordeón completamente funcional y animado usando solo HTML y CSS (sin JavaScript), con details/summary o con el hack del checkbox.
- **Enunciado:** Crea un componente acordeón que muestre preguntas frecuentes. Al hacer clic en una pregunta, la respuesta debe desplegarse con una animación suave de altura. El diseño debe ser responsive y profesional. Los iconos (+/-) deben animarse con rotate. Implementa apertura exclusiva (solo un item abierto a la vez).
- **Criterios:** Animaciones de apertura/cierre fluidas (3 puntos), iconos animados (2 puntos), diseño responsive (2 puntos), accesibilidad con teclado (2 puntos), apertura exclusiva (1 punto).

### Actividad Propuesta 3: Landing page con parallax CSS puro

- **RA:** RA2
- **Objetivo:** Crear una landing page con efecto parallax implementado exclusivamente con CSS (sin JavaScript), usando background-attachment: fixed y capas de fondo.
- **Enunciado:** Diseña una landing page para un producto digital con 4 secciones de altura completa (100vh). Cada sección debe tener una imagen de fondo diferente con efecto parallax. El contenido debe estar centrado en cada sección. Implementa transiciones suaves al hacer scroll entre secciones. Añade un menú de navegación fijo (sticky) que cambie de estilo al hacer scroll.
- **Criterios:** Efecto parallax correcto (3 puntos), secciones 100vh (2 puntos), menú sticky funcional (2 puntos), diseño visual profesional (2 puntos), responsive (1 punto).

### Actividad Propuesta 4: Formulario con validación visual CSS-only

- **RA:** RA2 y RA5
- **Objetivo:** Crear un formulario donde toda la validación visual (colores, iconos, mensajes) se gestione exclusivamente con CSS usando :valid, :invalid y pseudoelementos.
- **Enunciado:** Diseña un formulario de registro con campos: nombre, email, password, confirmar password. Usa :valid/:invalid para mostrar bordes verdes/rojos. Muestra iconos de check/cross con ::after. Muestra mensajes de error con CSS (sin JS). Añade barra de fortaleza de password visual con CSS. Implementa :focus-within para resaltar el fieldset activo.
- **Criterios:** Validación visual CSS completa (4 puntos), iconos check/cross (2 puntos), barra fortaleza (2 puntos), :focus-within (1 punto), responsive (1 punto).

### Actividad Propuesta 5: Micro-interacciones y animaciones de interfaz

- **RA:** RA2
- **Objetivo:** Implementar un conjunto de micro-interacciones profesionales que mejoren la experiencia de usuario sin resultar intrusivas.
- **Enunciado:** Crea una página que muestre: (1) botones con efecto ripple al hacer clic (CSS puro con ::after y animación), (2) skeleton loaders animados, (3) notificación toast que aparece y desaparece con animación, (4) interruptor toggle animado, (5) tarjetas con efecto de tilt 3D sutil en hover. Todo con CSS, mínimo JavaScript.
- **Criterios:** Botones ripple (2 puntos), skeleton loaders (2 puntos), toast notification (2 puntos), toggle switch (2 puntos), efecto tilt (2 puntos).

## Actividades de ampliación

### Actividad de Ampliación 1: Design System completo con CSS moderno

- **RA:** RA1 y RA2
- **Objetivo:** Crear un mini design system completo con tokens de diseño, componentes reutilizables y documentación, usando exclusivamente CSS moderno.
- **Enunciado:** Desarrolla un design system para una aplicación de gestión de tareas que incluya: (1) tokens de diseño como variables CSS (colores, tipografía, espaciado, sombras, radios), (2) componentes: botones (primary, secondary, ghost, danger, sizes), cards, inputs, badges, alerts, modals, (3) temas claro y oscuro, (4) página de documentación que muestre todos los componentes, (5) todo organizado con @layer. Entrega un único archivo HTML con todo el CSS embebido.
- **Criterios:** Tokens completos (3 puntos), 5+ componentes funcionales (3 puntos), temas claro/oscuro (2 puntos), documentación (1 punto), organización @layer (1 punto).

### Actividad de Ampliación 2: Juego de memoria CSS-only con animaciones

- **RA:** RA2 y RA4
- **Objetivo:** Crear un juego de memoria (memory match) funcional usando exclusivamente HTML y CSS, sin JavaScript, aprovechando la pseudoclase :checked y técnicas avanzadas.
- **Enunciado:** Crea un tablero de 4x4 cartas (16 cartas, 8 parejas). Al hacer clic en una carta (usando label+checkbox oculto), esta debe girar con animación 3D. Si dos cartas coinciden, deben permanecer visibles. Implementa: animación de giro 3D con transform y perspective, indicador de parejas encontradas, botón de reinicio, animación de victoria, diseño responsive.
- **Criterios:** Mecánica de giro con CSS (3 puntos), animación 3D correcta (2 puntos), tablero 4x4 funcional (2 puntos), reinicio (1 punto), animación de victoria (1 punto), responsive (1 punto).

### Actividad de Ampliación 3: Clon responsive de la interfaz de Spotify con CSS Grid y Flexbox

- **RA:** RA1, RA2
- **Objetivo:** Replicar la interfaz principal de Spotify Web Player usando exclusivamente HTML y CSS (sin frameworks), demostrando dominio de layout moderno.
- **Enunciado:** Reproduce la interfaz de Spotify con: sidebar izquierda (playlists, navegación), área principal (playlists destacadas, albums en grid), barra de reproducción inferior fija, y header superior con navegación. Implementa diseño responsive que se adapte a: desktop (>1024px), tablet (768-1024px), mobile (<768px). En mobile, la sidebar debe colapsar y la barra inferior debe reorganizarse. Usa CSS Grid para el layout principal y Flexbox para componentes internos.
- **Criterios:** Layout Grid correcto (3 puntos), Flexbox en componentes (2 puntos), responsive 3 breakpoints (3 puntos), fidelidad visual (1 punto), código organizado y comentado (1 punto).

## Buenas prácticas

1. **Usa `box-sizing: border-box` universalmente.** Aplica `*, *::before, *::after { box-sizing: border-box; }` como primera regla. Simplifica todos los cálculos de dimensiones y evita el comportamiento por defecto contraintuitivo.

2. **Prefiere `rem` sobre `px` para tipografía y espaciado.** Define un `font-size` base en `html` (normalmente 16px = 1rem) y usa `rem` para todo lo demás. Los usuarios que necesiten aumentar el texto podrán hacerlo y toda la interfaz escalará proporcionalmente.

3. **Usa variables CSS para todo valor repetido.** Colores, espaciados, sombras, radios, transiciones. Centralizar estos valores facilita cambios globales, temas y mantenimiento.

4. **Organiza el CSS en capas lógicas con @layer.** Define capas para reset, base, componentes y utilidades. Esto elimina la necesidad de `!important` y guerras de especificidad.

5. **Adopta una metodología de nomenclatura (BEM, utility-first) y sé consistente.** La consistencia en el naming es más importante que la metodología elegida.

6. **No anides selectores más de 3 niveles.** El anidamiento profundo aumenta la especificidad, reduce el rendimiento y hace el código frágil.

7. **Respeta siempre `prefers-reduced-motion`.** Envuelve o anula animaciones para usuarios que prefieren reducir movimiento. Es un requisito de accesibilidad, no opcional.

8. **Usa `:focus-visible` en lugar de `:focus` para estilos de foco.** Evita mostrar el anillo de foco al hacer clic con ratón, manteniéndolo para navegación por teclado.

9. **Diseña mobile-first.** Escribe los estilos base para móvil y usa `min-width` en media queries para añadir complejidad en pantallas mayores.

10. **Mantén los selectores de baja especificidad.** Usa clases en lugar de IDs. Evita selectores de tipo anidados. Esto facilita la sobrescritura y el mantenimiento.

11. **Usa `clamp()` para tipografía fluida en lugar de múltiples media queries.** Reduce drásticamente el código necesario para texto responsive.

12. **Agrupa las media queries junto a los componentes que modifican, no en un bloque separado al final.** Facilita encontrar y modificar todos los estilos de un componente.

## Errores frecuentes

1. **Abusar de `!important`.** Es el mayor síntoma de CSS mal organizado. Cada `!important` añade deuda técnica. Solución: usar @layer, reducir especificidad, o repensar la arquitectura CSS.

2. **No usar `box-sizing: border-box`.** Provoca que padding y border aumenten el tamaño total, causando desbordamientos y cálculos incorrectos. Solución: aplicar border-box universal al inicio.

3. **Usar `px` para todo.** Impide que la interfaz escale cuando el usuario cambia el tamaño de fuente base. Solución: usar `rem` para tipografía y espaciado, `px` solo para bordes finos y detalles.

4. **Anidar selectores profundamente.** `header nav ul li a span` es frágil y difícil de sobrescribir. Solución: usar clases planas (BEM, utility-first).

5. **Olvidar `prefers-reduced-motion`.** Las animaciones pueden causar mareos o náuseas a personas con trastornos vestibulares. Solución: siempre incluir la media query de reduced motion.

6. **Usar `display: none` para ocultar contenido que debe ser accesible.** Elimina el contenido del DOM de accesibilidad. Solución: usar técnicas de ocultación visual (clip, position absolute fuera de pantalla).

7. **No definir fallbacks para `var()`.** Si una variable no está definida, la propiedad usa el valor inicial. Solución: `var(--color, #fallback)`.

8. **Confundir `em` y `rem`.** `em` es relativo al padre (efecto compuesto). `rem` es relativo al root (consistente). Usar `em` donde se necesita `rem` causa tamaños inesperados.

9. **Posicionar elementos sin establecer un contexto de apilamiento.** `z-index` no funciona sin `position` (excepto flex/grid items). Solución: asegurar que el elemento tenga `position: relative/absolute/fixed/sticky`.

10. **No probar en dispositivos reales.** Lo que funciona en el simulador del navegador puede fallar en un dispositivo real.

## Resumen

Esta unidad ha cubierto el espectro completo del CSS profesional moderno. Hemos recorrido desde los fundamentos de la cascada y la especificidad hasta las técnicas más avanzadas de organización, animación y diseño responsivo. El alumnado ha aprendido que CSS moderno es mucho más que aplicar colores y fuentes: es un lenguaje de diseño completo con capacidades de cálculo, animación, tematización y maquetación avanzada.

Los selectores avanzados como `:has()`, `:is()`, `:where()` y `:not()` nos permiten escribir CSS más expresivo y con menos código. Las variables CSS (Custom Properties) han revolucionado la forma de gestionar temas y valores reutilizables, permitiendo cambios dinámicos sin modificar hojas de estilo. Las capas `@layer` resuelven décadas de problemas de especificidad proporcionando un mecanismo nativo de control de cascada.

La organización del código CSS es fundamental en proyectos profesionales. Metodologías como BEM, ITCSS y enfoques utility-first como Tailwind ofrecen diferentes caminos hacia el mismo objetivo: CSS mantenible, escalable y predecible. Las funciones matemáticas como `clamp()`, `min()` y `max()` nos permiten crear diseños verdaderamente fluidos que se adaptan a cualquier tamaño de pantalla sin depender exclusivamente de media queries.

El centrado de elementos —históricamente uno de los problemas más frustrantes de CSS— se resuelve hoy elegantemente con Flexbox y Grid. Las animaciones y transiciones, cuando se usan con moderación y respetando las preferencias del usuario (`prefers-reduced-motion`), mejoran la experiencia de uso y aportan profesionalidad a nuestras interfaces.

Dominar CSS profesional significa entender no solo la sintaxis, sino también la arquitectura, la organización y las mejores prácticas que permiten a equipos de desarrollo colaborar eficientemente en proyectos a largo plazo.

## Recursos complementarios

- **MDN Web Docs - CSS:** https://developer.mozilla.org/es/docs/Web/CSS - Documentación de referencia completa.
- **CSS-Tricks:** https://css-tricks.com/ - Guías, artículos y almanaque de propiedades CSS.
- **web.dev - Learn CSS:** https://web.dev/learn/css/ - Curso gratuito de Google.
- **Can I Use:** https://caniuse.com/ - Compatibilidad de características CSS por navegador.
- **BEM Methodology:** https://en.bem.info/methodology/ - Documentación oficial.
- **ITCSS (Harry Roberts):** https://www.creativebloq.com/web-design/manage-large-css-projects-itcss-101517528 - Arquitectura CSS.
- **Tailwind CSS Docs:** https://tailwindcss.com/docs - Documentación de utility-first.
- **Easing Functions:** https://easings.net/ - Referencia visual de funciones de easing.
- **CSS Grid Generator:** https://cssgrid-generator.netlify.app/ - Generador visual de layouts Grid.
- **Animista:** https://animista.net/ - Generador de animaciones CSS con vista previa.
