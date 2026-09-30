---
icon: lucide/monitor-smartphone
---

# Unidad 11: Diseño Web Responsive

## Objetivos de aprendizaje

Al finalizar esta unidad, el alumnado será capaz de diseñar y desarrollar sitios web que se adapten óptimamente a cualquier dispositivo y tamaño de pantalla. Los objetivos concretos son: comprender la filosofía del diseño responsive y su diferencia con el diseño adaptativo; aplicar la metodología Mobile First como estrategia de desarrollo, entendiendo el concepto de mejora progresiva frente a degradación elegante; configurar correctamente la metaetiqueta viewport y comprender el impacto de cada uno de sus atributos en la experiencia móvil; seleccionar breakpoints basados en el contenido y no en dispositivos específicos, justificando cada punto de ruptura; dominar las media queries en todas sus variantes (tipos de medio, operadores lógicos, características del dispositivo) incluyendo las modernas como prefers-reduced-motion y prefers-color-scheme; implementar Container Queries para componentes reutilizables que se adaptan al tamaño de su contenedor, no al viewport; utilizar imágenes responsive mediante srcset, sizes y el elemento picture para servir la imagen óptima según el dispositivo; aplicar tipografía responsive con clamp() y unidades relativas para texto legible en cualquier tamaño; construir patrones de layout responsive como Column Drop, Mostly Fluid, Layout Shifter y Off Canvas; implementar menús de navegación responsive con diversas técnicas (hamburguesa CSS puro, hamburguesa con JS, off-canvas, bottom navigation móvil); diseñar tablas responsive con múltiples estrategias (scroll horizontal, colapso en cards, ocultación de columnas); y desarrollar un proyecto web completo aplicando todas las técnicas aprendidas.

## Relación con los Resultados de Aprendizaje

Esta unidad desarrolla el **Resultado de Aprendizaje 2 (RA2)** del módulo 0615 *Diseño de interfaces web* —"Crea interfaces web homogéneos definiendo y aplicando estilos"—, según el currículo oficial (RD 405/2023, BOE; currículo andaluz). En concreto, aborda el criterio CE 2.i ("Se han analizado y utilizado tecnologías y frameworks para la creación de interfaces web con un diseño responsive") y está profundamente vinculada a la verificación de la correcta visualización en diferentes navegadores y dispositivos. En el contexto del currículo de DAW, el diseño responsive es una competencia transversal fundamental, ya que la práctica totalidad de los proyectos web desarrollados durante el ciclo formativo deben funcionar correctamente en dispositivos móviles, tablets y ordenadores de escritorio. Esta unidad conecta además con el **RA6** ("Desarrolla interfaces web amigables analizando y aplicando las pautas de usabilidad establecidas"), pues un diseño responsive bien resuelto garantiza la facilidad de uso y navegación (CE 6.d) en cualquier dispositivo. Conecta directamente con el módulo de Desarrollo Web en Entorno Cliente, donde el alumnado implementará interfaces responsive con frameworks JavaScript, y con el módulo de Desarrollo Web en Entorno Servidor, donde las vistas generadas dinámicamente deben también ser responsive. A nivel profesional, el dominio del diseño responsive es un requisito indispensable en cualquier oferta de empleo de desarrollo web, ya que más del 60% del tráfico web global proviene de dispositivos móviles.

## Conocimientos previos

El alumnado debe dominar HTML semántico (elementos estructurales, formularios, tablas), CSS fundamental (modelo de cajas, posicionamiento, selectores, herencia y cascada), y tener experiencia práctica con Flexbox y CSS Grid. Debe comprender el concepto de viewport y las diferencias entre píxeles CSS y píxeles de dispositivo (device pixels vs CSS pixels, devicePixelRatio). Es necesario conocer las unidades de medida CSS (px, em, rem, %, vw, vh) y sus casos de uso. El alumnado debe haber trabajado con imágenes en la web (formatos, etiqueta img, imágenes de fondo CSS) y tener nociones básicas de rendimiento web. Se asume conocimiento previo de las herramientas de desarrollo del navegador (Chrome DevTools) incluyendo el modo de dispositivo móvil para simular diferentes tamaños de pantalla. Es recomendable haber comprendido los principios de usabilidad y experiencia de usuario (UX) para móviles, como el tamaño mínimo de los objetivos táctiles (44x44 puntos según las directrices de Apple y 48x48dp según Material Design).

## Contenidos

1. **Introducción al diseño responsive**: Orígenes (Ethan Marcotte, 2010). Evolución de la web móvil. Principios: grillas fluidas, imágenes flexibles, media queries. Diferencia entre responsive y adaptive design. El ecosistema de dispositivos actual.

2. **Viewport y la metaetiqueta viewport**: Qué es el viewport. Layout viewport vs visual viewport. Atributos: width=device-width, initial-scale, user-scalable, minimum-scale, maximum-scale. Configuración óptima para sitios responsive.

3. **Metodología Mobile First**: Filosofía de diseño empezando por el móvil. Ventajas: mejor rendimiento, enfoque en contenido esencial, mejora progresiva. Mobile First CSS: min-width vs max-width en media queries.

4. **Breakpoints**: Definición y estrategia de selección. Enfoque por contenido vs por dispositivo. Breakpoints comunes y su justificación. Uso exclusivo de min-width en el enfoque Mobile First. Ejemplos.

5. **Media Queries**: Sintaxis (@media). Tipos de medio (screen, print, all). Operadores lógicos (and, not, only, or/comma). Características de medio: width/height, min/max-width/height, orientation, aspect-ratio, resolution. Media queries de preferencias de usuario: prefers-reduced-motion, prefers-color-scheme (light/dark), prefers-contrast, prefers-reduced-data. Media queries de interacción: hover, pointer, any-hover, any-pointer.

6. **Container Queries**: Diferencia fundamental con media queries. Propiedades container-type, container-name. Regla @container. Unidades de contenedor (cqw, cqh, cqi, cqb, cqmin, cqmax). Casos de uso para componentes reutilizables.

7. **Imágenes responsive**: Problemática (imágenes demasiado grandes en móvil, resolución inadecuada en pantallas de alta densidad). Atributo srcset con descriptores w (ancho) y x (densidad). Atributo sizes para informar al navegador del tamaño de renderizado. Elemento picture con múltiples source para formatos modernos y dirección artística. loading="lazy" para carga diferida.

8. **Tipografía responsive**: clamp() para tamaño de fuente fluido. Ejemplo: font-size: clamp(1rem, 2.5vw, 2rem). Unidades relativas vs absolutas. Longitud de línea óptima (45-75 caracteres, unidad ch). Altura de línea responsive.

9. **Espaciado responsive**: Uso de clamp() para padding, margin y gap. Unidades de viewport para espaciados proporcionales. La función min() y max() en CSS.

10. **Patrones de layout responsive**: Column Drop, Mostly Fluid, Layout Shifter, Off Canvas. Implementación con CSS moderno (Grid, Flexbox).

11. **Menús responsive**: Hamburguesa con CSS puro (checkbox hack). Hamburguesa con JavaScript mínimo. Off-canvas con transiciones. Bottom navigation para móvil. Patrones de navegación responsive.

12. **Tablas responsive**: Scroll horizontal. Colapso en cards. Ocultación de columnas no esenciales. Uso de data-attributes con CSS.

13. **Proyecto completo responsive**: Desarrollo de una página web completa Mobile First.

## Desarrollo teórico

### 1. Introducción al diseño responsive

!!! info "Origen y pilares del diseño responsive"
    El diseño web responsive fue conceptualizado por **Ethan Marcotte** en su artículo seminal de **2010** en *A List Apart*. Marcotte identificó que la creciente diversidad de dispositivos con acceso a internet exigía un nuevo paradigma de diseño, uno que no creara versiones separadas del sitio para cada dispositivo, sino que el mismo contenido se adaptara fluidamente al contexto de visualización. Sus tres pilares fundamentales fueron:

    - **Grillas fluidas** — usando porcentajes en lugar de píxeles fijos.
    - **Imágenes flexibles** — que no desbordan su contenedor.
    - **Media queries** — reglas CSS condicionales basadas en características del dispositivo.

Antes del responsive design, la práctica común era el **diseño adaptativo** (*adaptive design*), que consistía en crear múltiples versiones fijas del sitio para diferentes anchos predefinidos (típicamente **320px**, **768px**, **1024px**). El servidor detectaba el dispositivo y servía la versión correspondiente. Este enfoque tenía problemas graves:

- **Mantenimiento costoso** — cada cambio debía replicarse en todas las versiones.
- **Imposibilidad de cubrir** todos los tamaños de pantalla existentes.
- **Duplicación de contenido** que perjudicaba al SEO.

El responsive design resuelve esto con un **único código base** que se adapta continuamente a cualquier ancho.

La situación actual ha superado incluso la visión original de Marcotte. El ecosistema de dispositivos incluye smartphones (desde **320px** hasta pantallas plegables de **400px+**), tablets (**600px** a **1200px**), portátiles (**1024px** a **1920px**), monitores de escritorio (**1920px** a **5120px**), televisores inteligentes, relojes, y próximamente dispositivos de realidad extendida. En **2025**, los datos de StatCounter muestran que el tráfico móvil representa aproximadamente el **58%** del total global, con picos superiores al **70%** en regiones como Asia y África. Esto hace que el diseño responsive no sea una opción, sino un requisito fundamental.

### 2. Viewport y la metaetiqueta viewport

!!! info "Definición"
    El **viewport** es el área visible de una página web dentro del navegador. En dispositivos móviles, existe una distinción crucial entre el **layout viewport** (el área sobre la que se renderiza la página, típicamente **980px** por defecto) y el **visual viewport** (el área realmente visible en la pantalla). Sin la metaetiqueta viewport correcta, los navegadores móviles asumen que la página está diseñada para escritorio y la renderizan a **980px** de ancho, reduciéndola después para que quepa en la pantalla. El resultado es texto minúsculo e ilegible que obliga al usuario a hacer zoom.

La metaetiqueta viewport se coloca en el `head` del HTML y corrige este comportamiento: `<meta name="viewport" content="width=device-width, initial-scale=1.0">`.

- **`width=device-width`** — establece el ancho del layout viewport igual al ancho de la pantalla del dispositivo en píxeles CSS (no en píxeles físicos). Por ejemplo, un iPhone 14 tiene un ancho físico de **1170px** pero reporta `device-width` como **390px** en modo portrait (por su `devicePixelRatio` de **3x**).
- **`initial-scale=1.0`** — establece el nivel de zoom inicial al **100%**, evitando que el navegador haga zoom out automático.

!!! warning "No deshabilites el zoom"
    El atributo `user-scalable=no` deshabilita el zoom del usuario y está **generalmente desaconsejado por razones de accesibilidad**.

Otros atributos del viewport son `minimum-scale` y `maximum-scale` (establecen límites al zoom) y `viewport-fit=cover` (para dispositivos con notch o "isla dinámica" en iPhones modernos, permitiendo que el contenido se extienda a áreas seguras).

!!! tip "Configuración recomendada"
    Para sitios responsive, la configuración mínima es `width=device-width, initial-scale=1.0`, **permitiendo siempre el zoom del usuario**.

### 3. Metodología Mobile First

!!! info "Definición"
    **Mobile First** es una filosofía de diseño y desarrollo que propone comenzar el proceso creativo desde la versión móvil (la más restrictiva) y progresivamente añadir complejidad para pantallas más grandes. Este enfoque, popularizado por **Luke Wroblewski**, invierte la práctica tradicional de diseñar primero para escritorio y luego adaptar a móvil.

Las ventajas del Mobile First son múltiples:

- **Prioriza el contenido** — el limitado espacio móvil fuerza a identificar qué es verdaderamente esencial y eliminar lo superfluo.
- **Mejora el rendimiento** — al cargar primero los estilos base (móvil) y luego añadir estilos adicionales mediante media queries, los dispositivos móviles solo descargan y procesan el CSS que necesitan.
- **Se alinea con la realidad estadística** del tráfico web actual, donde la mayoría de usuarios acceden desde móvil.

!!! tip "Regla de implementación"
    En CSS, Mobile First se implementa usando **exclusivamente `min-width`** en las media queries (nunca `max-width`). Los estilos base (fuera de cualquier media query) corresponden a la versión móvil; después se añaden media queries con `min-width` para ir añadiendo o sobrescribiendo estilos a medida que la pantalla crece.

Este enfoque se alinea con el principio de **mejora progresiva** (*progressive enhancement*): la versión base funciona en cualquier dispositivo, y los navegadores más capaces reciben mejoras adicionales. Lo opuesto sería la **degradación elegante** (*graceful degradation*): diseñar para el máximo y luego ir quitando funcionalidades para dispositivos menos capaces, práctica desaconsejada en la actualidad.

### 4. Breakpoints

!!! info "Definición"
    Los **breakpoints** son los puntos de ruptura donde el diseño cambia para adaptarse a un tamaño de pantalla diferente.

La decisión más importante sobre breakpoints es cómo elegirlos. La recomendación de los expertos (y del **W3C**) es seleccionar breakpoints basados en el **contenido**, no en **dispositivos** específicos. Esto significa que los breakpoints deben determinarse observando el diseño: se añade un breakpoint cuando el contenido «se rompe» visualmente (líneas de texto demasiado largas o cortas, columnas que colapsan, imágenes que se desalinean).

A pesar de esta recomendación, en la práctica docente es útil conocer los rangos de breakpoints comunes:

| Breakpoint | Transición habitual |
|------------|---------------------|
| **480px** | Móvil pequeño a móvil grande |
| **768px** | Móvil/tablet pequeña a tablet |
| **1024px** | Tablet a escritorio pequeño |
| **1280px** | Escritorio estándar |

Para proyectos propios, la estrategia recomendada es: comienza con **cero breakpoints** y usa técnicas fluidas (Grid con `auto-fit`/`minmax`, Flexbox con `wrap`, `clamp()` para tamaños). Solo cuando el diseño lo exija, añade breakpoints en los puntos exactos donde el contenido deja de verse bien.

En un enfoque Mobile First, todos los breakpoints usan `min-width`. Por ejemplo: `@media (min-width: 768px) { ... }` se lee como «cuando la pantalla tenga al menos **768px** de ancho, aplica estos estilos». Esto contrasta con el enfoque Desktop First, que usa `max-width`: `@media (max-width: 768px) { ... }` («cuando la pantalla tenga como máximo **768px**, sobrescribe estos estilos»). Mobile First produce código más limpio y con mejor rendimiento.

### 5. Media Queries avanzadas

!!! info "Definición"
    Las **media queries** son el mecanismo de CSS para aplicar estilos condicionalmente según las características del dispositivo o del agente de usuario. La sintaxis básica es `@media [tipo] [operador] (característica) { reglas }`.

- **Tipos de medio** — `screen` (pantallas), `print` (impresión) y `all` (todos, por defecto).
- **Operadores lógicos** — `and` (intersección), `not` (negación), `only` (para navegadores antiguos que no soportan media queries) y la coma `,` (que actúa como **OR** lógico).

Las características de medio han evolucionado significativamente:

- **Clásicas** — `width`, `min-width`, `max-width` (ancho del viewport), `height` (alto del viewport), `orientation: portrait | landscape` (orientación del dispositivo), `aspect-ratio` (relación de aspecto) y `resolution` (densidad de píxeles en dpi/dppx).
- **Preferencias de usuario** (especialmente importantes para accesibilidad) — `prefers-reduced-motion: reduce` (el usuario prefiere reducir animaciones), `prefers-color-scheme: dark | light` (esquema de color preferido), `prefers-contrast: more | less` (preferencia de contraste) y `prefers-reduced-data: reduce` (ahorro de datos).
- **Interacción** (cruciales para detectar capacidades táctiles) — `hover: hover | none` (si el dispositivo soporta hover), `pointer: coarse | fine` (tipo de puntero, dedo vs ratón), y `any-hover` / `any-pointer` (consideran todos los dispositivos de entrada).

Un ejemplo de consulta compleja: `@media screen and (min-width: 768px) and (hover: hover) and (prefers-color-scheme: dark) { ... }` aplica estilos solo en pantallas de al menos **768px**, con capacidad de hover, cuando el usuario prefiere modo oscuro.

### 6. Container Queries

!!! info "Definición"
    Las **Container Queries** representan la evolución más significativa en diseño responsive desde las media queries originales. Mientras que las media queries consultan el tamaño del **viewport** (la ventana del navegador), las container queries consultan el tamaño de un elemento **contenedor** específico. Esto resuelve el problema fundamental de los componentes reutilizables: un componente puede renderizarse en diferentes contextos (una barra lateral estrecha, una zona de contenido ancha, un modal) y necesita adaptarse a su contenedor, no al viewport global.

Para usar container queries:

1. Define un contenedor con **`container-type`** (que puede ser `inline-size` para consultas de ancho, `size` para ancho y alto, o `normal` para consultas de estilo) y opcionalmente **`container-name`** para nombrarlo.
2. Aplica estilos condicionales con la regla **`@container`**: `@container (min-width: 400px) { .componente { ... } }`.
3. Utiliza las unidades de contenedor asociadas: **`cqw`** (1% del ancho del contenedor), **`cqh`** (1% del alto), **`cqi`** y **`cqb`** (ejes inline y block), **`cqmin`** y **`cqmax`**.

!!! tip "Ventaja práctica"
    Con media queries, un componente de tarjeta en una página necesitaba lógica condicional compleja si podía aparecer tanto en un sidebar de **300px** como en una zona central de **800px**. Con container queries, el componente simplemente consulta el tamaño de su contenedor padre y se adapta en consecuencia, independientemente del contexto de página. Esto hace que los componentes sean verdaderamente **reutilizables y autónomos**.

### 7. Imágenes responsive

El problema de las imágenes responsive es doble: por un lado, servir imágenes excesivamente grandes a dispositivos móviles malgasta ancho de banda y ralentiza la carga; por otro, las pantallas de alta densidad (**Retina**, **2x**, **3x**) necesitan imágenes con mayor resolución para verse nítidas. La solución implica varios mecanismos HTML trabajando en conjunto.

El atributo `srcset` en la etiqueta `<img>` permite al navegador elegir entre múltiples versiones de la misma imagen:

- **Descriptor `w`** (ancho intrínseco) — `srcset="imagen-400.jpg 400w, imagen-800.jpg 800w, imagen-1200.jpg 1200w"`.
- **Descriptor `x`** (densidad) — `srcset="imagen.jpg 1x, imagen@2x.jpg 2x, imagen@3x.jpg 3x"`.
- **`sizes`** — describe el tamaño de renderizado de la imagen en diferentes condiciones de viewport; combinado con `w`, permite al navegador seleccionar la fuente más adecuada.
- **`<picture>`** — permite **dirección artística** (*art direction*): servir imágenes recortadas o con composición diferente según el tamaño de pantalla, usando múltiples elementos `<source>` con condiciones `media`. También permite servir formatos modernos como **WebP** o **AVIF** con fallback a JPEG/PNG para navegadores que no los soporten.

Para el rendimiento de carga:

- **`loading="lazy"`** — pospone la carga de imágenes que están fuera del viewport hasta que el usuario se acerca a ellas mediante scroll. Reduce drásticamente el tiempo de carga inicial y el consumo de datos.
- **`fetchpriority="high"`** — permite priorizar imágenes críticas como el héroe.

### 8. Tipografía responsive

!!! info "Tipografía fluida con clamp()"
    La tipografía responsive busca mantener la legibilidad óptima en cualquier tamaño de pantalla. La herramienta más potente para esto es la función CSS **`clamp()`**, que acepta tres valores: **mínimo**, **valor preferido** (fluido) y **máximo**. Por ejemplo: `font-size: clamp(1rem, 2.5vw, 2rem)` establece que el tamaño de fuente será como mínimo **1rem**, como máximo **2rem**, y entre ambos extremos variará fluidamente al **2.5%** del ancho del viewport.

Esta función elimina la necesidad de múltiples media queries para ajustar tamaños de fuente en cada breakpoint. Recomendaciones:

- **Escala tipográfica responsive** — para los encabezados (`h1` a `h6`): `h1 { font-size: clamp(2rem, 5vw, 4rem); }`, `h2 { font-size: clamp(1.5rem, 3.5vw, 3rem); }`, etc.
- **Longitud de línea** — la unidad `ch` (ancho del carácter "0" de la fuente actual) es ideal para controlarla: `max-width: 65ch` limita cada línea a unos **65 caracteres**, el ancho óptimo de lectura según estudios de legibilidad.
- **Altura de línea** — para `line-height` se recomienda un valor sin unidades (p. ej. **1.5-1.6** para texto corrido) que se ajuste automáticamente a cualquier tamaño de fuente.

### 9. Espaciado responsive

!!! tip "Espaciado fluido"
    Al igual que la tipografía, el espaciado (`padding`, `margin`, `gap`) puede hacerse fluido con **`clamp()`**. Por ejemplo: `padding: clamp(1rem, 5vw, 4rem)` crea un padding que crece proporcionalmente con la pantalla pero nunca es menor de **1rem** ni mayor de **4rem**. Las unidades de viewport (`vw`, `vh`, `vmin`, `vmax`) son ideales para espaciados que escalan con la pantalla: `gap: 2vw` crea más separación en pantallas grandes y menos en pequeñas.

    Las funciones **`min()`** y **`max()`** complementan a `clamp()`: `width: min(100%, 600px)` asegura que un elemento nunca sea más ancho que **600px** ni más ancho que su contenedor; `padding: max(1rem, 2vw)` usa el mayor de los dos valores, garantizando un mínimo de **1rem** pero permitiendo más espacio en pantallas grandes.

### 10. Patrones de layout responsive

Existen varios patrones de layout responsive establecidos:

| Patrón | Descripción | Implementación |
|--------|-------------|----------------|
| **Column Drop** | Las columnas se muestran en fila en desktop y se apilan verticalmente al reducir el ancho, «dejándose caer» una debajo de otra. Es el patrón más simple. | Flexbox (`flex-wrap: wrap`) o Grid (`grid-template-columns` cambiando con media queries). |
| **Mostly Fluid** | Similar al Column Drop pero con márgenes fluidos que se ajustan al ancho. Es el patrón más común en la web moderna. | `max-width` para limitar el ancho máximo y porcentajes para los márgenes. |
| **Layout Shifter** | El más complejo: implica una reorganización completa de los elementos en diferentes breakpoints. | CSS Grid con `grid-template-areas`, que permite redefinir completamente el mapa de áreas en cada media query sin modificar el HTML. |
| **Off Canvas** | Oculta contenido (normalmente un menú de navegación) fuera de la pantalla en móvil y lo muestra al activar un botón (hamburguesa). | `position: fixed` y `transform: translateX()` para la animación de deslizamiento, combinado con un overlay semitransparente. |

## Ejemplos guiados

### Ejemplo Guiado 1: Meta viewport correcta y Mobile First CSS

!!! example "Contexto pedagógico"
    Este ejemplo demuestra la configuración esencial del viewport para cualquier proyecto responsive y la estructura CSS Mobile First. Los estilos base (fuera de media queries) definen el diseño móvil. Las media queries con min-width añaden estilos progresivamente para pantallas más grandes.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <!--
    ===== META VIEWPORT =====
    width=device-width: el viewport se ajusta al ancho del dispositivo.
    initial-scale=1.0: nivel de zoom inicial al 100%.
    Sin esta etiqueta, el móvil muestra la página a 980px de ancho en miniatura.
  -->
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ejemplo 1 - Mobile First CSS</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }

    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      line-height: 1.6;
      padding: 1rem;
    }

    /* ===== ESTILOS BASE (MÓVIL) ===== */
    /*
     * Estos estilos se aplican a TODOS los dispositivos.
     * Definen el diseño más simple: una columna, sin sidebar.
     * Mobile First: empezamos por el caso más restrictivo.
     */
    .header {
      background: #1a1a2e;
      color: #fff;
      padding: 1rem;
      text-align: center;
    }

    .nav {
      background: #16213e;
      padding: 0.5rem;
    }

    /* En móvil, los enlaces de navegación se apilan verticalmente */
    .nav a {
      color: #fff;
      text-decoration: none;
      padding: 0.5rem;
      display: block; /* Cada enlace en su propia línea en móvil */
      text-align: center;
    }

    .main {
      padding: 1rem 0;
    }

    /* El sidebar se muestra debajo del contenido en móvil */
    .sidebar {
      background: #f0f0f0;
      padding: 1rem;
      margin-top: 1rem;
    }

    .footer {
      background: #1a1a2e;
      color: #ccc;
      text-align: center;
      padding: 1rem;
      margin-top: 1rem;
    }

    /*
     * ===== BREAKPOINT: TABLET (>= 768px) =====
     * min-width: 768px -> cuando la pantalla tenga AL MENOS 768px.
     * La navegación se vuelve horizontal.
     */
    @media (min-width: 768px) {
      body { padding: 2rem; }

      .nav a {
        display: inline-block; /* Enlaces en línea horizontal */
      }

      .nav { text-align: center; }
    }

    /*
     * ===== BREAKPOINT: DESKTOP (>= 1024px) =====
     * min-width: 1024px -> pantallas de escritorio.
     * El layout ahora tiene sidebar a la derecha.
     */
    @media (min-width: 1024px) {
      .container {
        display: grid;
        grid-template-columns: 2fr 1fr; /* Contenido (2/3) + Sidebar (1/3) */
        gap: 2rem;
        max-width: 1200px;
        margin: 0 auto;
      }

      .sidebar { margin-top: 0; } /* Quitamos el margin móvil */
    }
  </style>
</head>
<body>
  <header class="header">
    <h1>Mi Sitio Web</h1>
  </header>

  <nav class="nav">
    <a href="#">Inicio</a>
    <a href="#">Servicios</a>
    <a href="#">Portafolio</a>
    <a href="#">Blog</a>
    <a href="#">Contacto</a>
  </nav>

  <div class="container">
    <main class="main">
      <h2>Contenido Principal</h2>
      <p>Este sitio demuestra la metodología Mobile First. Los estilos base
      definen la versión móvil. Las media queries con min-width añaden
      mejoras progresivamente para tablets y desktop.</p>
    </main>

    <aside class="sidebar">
      <h3>Sidebar</h3>
      <p>En móvil, este sidebar aparece debajo del contenido. En desktop,
      se muestra a la derecha gracias al grid definido en la media query.</p>
    </aside>
  </div>

  <footer class="footer">
    2025 Mi Sitio Web. Diseño responsive Mobile First.
  </footer>
</body>
</html>
```

### Ejemplo Guiado 2: Menú hamburguesa con CSS puro (checkbox hack)

!!! example "Contexto pedagógico"
    El menú hamburguesa es el patrón de navegación responsive más extendido. Este ejemplo muestra la implementación con CSS puro, sin JavaScript, usando un checkbox oculto y el selector de hermanos adyacentes (~) para controlar la visibilidad del menú. Es una técnica elegante que funciona en todos los navegadores.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ejemplo 2 - Menú Hamburguesa CSS Puro</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: 'Segoe UI', sans-serif; }

    /* ===== BARRA DE NAVEGACIÓN ===== */
    .navbar {
      background: #1a1a2e;
      color: #fff;
      padding: 1rem;
      position: relative;
    }

    .navbar__header {
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .navbar__brand {
      font-size: 1.3rem;
      font-weight: 700;
    }

    /*
     * ===== TRUCO DEL CHECKBOX OCULTO =====
     * Ocultamos visualmente el checkbox pero permanece funcional.
     * La etiqueta label asociada (for="menu-toggle") actúa como botón.
     * Al hacer clic en el label, el checkbox cambia de estado.
     * Usamos :checked + selectores para mostrar/ocultar el menú.
     */
    .navbar__toggle {
      display: none; /* Ocultamos el checkbox nativo */
    }

    /*
     * El label estilizado como icono hamburguesa.
     * cursor: pointer indica que es interactivo.
     * Las 3 líneas se crean con el propio texto o con CSS.
     */
    .navbar__toggle-label {
      font-size: 1.8rem;
      cursor: pointer;
      user-select: none; /* Evita seleccionar el texto del icono */
      display: block;
      padding: 0.25rem;
    }

    /*
     * ===== MENÚ (OCULTO POR DEFECTO EN MÓVIL) =====
     * max-height: 0 + overflow: hidden oculta el menú.
     * transition suaviza la apertura/cierre.
     */
    .navbar__menu {
      max-height: 0;
      overflow: hidden;
      transition: max-height 0.4s ease;
    }

    /*
     * ===== MAGIA DEL CHECKBOX HACK =====
     * Cuando el checkbox está marcado (:checked), el menú se expande.
     * El selector ~ busca hermanos adyacentes (no solo inmediatos).
     * max-height: 500px es suficientemente grande para mostrar todo el menú.
     */
    .navbar__toggle:checked ~ .navbar__menu {
      max-height: 500px;
    }

    .navbar__menu a {
      display: block;
      color: #fff;
      text-decoration: none;
      padding: 0.75rem 1rem;
      border-top: 1px solid rgba(255, 255, 255, 0.1);
      transition: background 0.3s;
    }

    .navbar__menu a:hover {
      background: rgba(255, 255, 255, 0.1);
    }

    /* ===== DESKTOP: MENÚ SIEMPRE VISIBLE ===== */
    @media (min-width: 768px) {
      /*
       * En desktop ocultamos el label (hamburguesa)
       * y mostramos el menú horizontalmente.
       */
      .navbar__toggle-label {
        display: none;
      }

      .navbar {
        display: flex;
        align-items: center;
        justify-content: space-between;
      }

      .navbar__menu {
        max-height: none; /* Anulamos la restricción de altura */
        overflow: visible;
        display: flex;
        gap: 1rem;
      }

      .navbar__menu a {
        border-top: none;
        padding: 0.5rem 1rem;
        border-radius: 4px;
      }
    }

    /* ===== CONTENIDO DE EJEMPLO ===== */
    .content {
      padding: 2rem;
      max-width: 800px;
      margin: 0 auto;
    }
  </style>
</head>
<body>
  <nav class="navbar">
    <div class="navbar__header">
      <span class="navbar__brand">Mi Empresa</span>
      <!--
        El input checkbox está oculto (display:none).
        El label con for="menu-toggle" lo controla.
      -->
      <label for="menu-toggle" class="navbar__toggle-label">&#9776;</label>
    </div>

    <!-- Checkbox oculto que controla el menú -->
    <input type="checkbox" id="menu-toggle" class="navbar__toggle">

    <!-- Menú de navegación -->
    <div class="navbar__menu">
      <a href="#">Inicio</a>
      <a href="#">Servicios</a>
      <a href="#">Proyectos</a>
      <a href="#">Sobre nosotros</a>
      <a href="#">Contacto</a>
    </div>
  </nav>

  <div class="content">
    <h1>Menú Hamburguesa con CSS Puro</h1>
    <p>Este menú utiliza el truco del checkbox oculto (checkbox hack).
    No requiere JavaScript. Haz clic en el icono de hamburguesa para
    desplegar el menú en versión móvil.</p>
    <p>Redimensiona la ventana a menos de 768px para ver el menú responsive.</p>
  </div>
</body>
</html>
```

### Ejemplo Guiado 3: Imágenes responsive con srcset y picture

!!! example "Contexto pedagógico"
    Demostración completa de imágenes responsive usando srcset con descriptores w, el atributo sizes, y el elemento picture para dirección artística y formatos modernos.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ejemplo 3 - Imágenes Responsive</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      padding: 2rem;
      max-width: 1200px;
      margin: 0 auto;
      background: #f5f5f5;
    }

    h1 { margin-bottom: 2rem; }
    section { margin-bottom: 3rem; background: #fff; padding: 1.5rem; border-radius: 12px; }
    h2 { margin-bottom: 1rem; color: #333; }
    p { color: #666; margin-bottom: 1rem; }

    .demo-image {
      width: 100%;
      height: auto;
      border-radius: 8px;
    }
  </style>
</head>
<body>
  <h1>Imágenes Responsive en HTML</h1>

  <!--
    ===== MÉTODO 1: SRCSET CON DESCRIPTORES DE DENSIDAD (X) =====
    El navegador elige la imagen según la densidad de píxeles del dispositivo.
    1x: pantallas normales. 2x: pantallas Retina. 3x: pantallas de muy alta densidad.
    El atributo src actúa como fallback para navegadores que no soportan srcset.
  -->
  <section>
    <h2>Método 1: srcset con descriptores de densidad (x)</h2>
    <p>El navegador selecciona la imagen según el devicePixelRatio del dispositivo.
    En una pantalla Retina (2x), cargará la versión @2x.</p>
    <img
      src="imagen-1x.jpg"
      srcset="imagen-1x.jpg 1x, imagen-2x.jpg 2x, imagen-3x.jpg 3x"
      alt="Imagen con descriptores de densidad"
      class="demo-image"
      loading="lazy"
      width="800"
      height="400"
    >
    <!--
      IMPORTANTE: loading="lazy" difiere la carga hasta que la imagen
      esté cerca del viewport. Ahorra ancho de banda en móvil.
      width/height ayudan al navegador a reservar espacio y evitar
      layout shift (CLS - Cumulative Layout Shift).
    -->
  </section>

  <!--
    ===== MÉTODO 2: SRCSET CON DESCRIPTORES DE ANCHO (W) + SIZES =====
    En lugar de densidad, indicamos al navegador el ancho intrínseco
    de cada imagen. El atributo sizes le dice al navegador qué tamaño
    ocupará la imagen en el layout para cada condición.
  -->
  <section>
    <h2>Método 2: srcset con descriptores de ancho (w) + sizes</h2>
    <p>
      sizes indica que en viewports hasta 600px la imagen ocupa 100vw,
      hasta 900px ocupa 50vw, y en pantallas mayores 33vw.
      El navegador usa esta info + srcset para elegir la mejor fuente.
    </p>
    <img
      src="imagen-400.jpg"
      srcset="imagen-400.jpg 400w, imagen-800.jpg 800w, imagen-1200.jpg 1200w"
      sizes="(max-width: 600px) 100vw, (max-width: 900px) 50vw, 33vw"
      alt="Imagen con descriptores de ancho"
      class="demo-image"
      loading="lazy"
      width="800"
      height="400"
    >
  </section>

  <!--
    ===== MÉTODO 3: PICTURE PARA ART DIRECTION Y FORMATOS =====
    El elemento picture permite múltiples source con condiciones media.
    Ideal para servir imágenes recortadas/diferentes según el dispositivo
    (art direction) y para formatos modernos (WebP, AVIF) con fallback.
  -->
  <section>
    <h2>Método 3: picture para art direction y formatos modernos</h2>
    <p>En móvil se muestra una imagen recortada (versión vertical).
    En desktop se muestra la versión panorámica. Además se sirve WebP
    si el navegador lo soporta, con fallback a JPEG.</p>

    <picture>
      <!-- En móvil (max-width: 768px): imagen vertical en WebP -->
      <source
        srcset="hero-mobile.webp"
        media="(max-width: 768px)"
        type="image/webp"
      >
      <!-- En móvil: fallback JPEG para navegadores sin WebP -->
      <source
        srcset="hero-mobile.jpg"
        media="(max-width: 768px)"
      >
      <!-- En desktop: imagen horizontal en WebP -->
      <source
        srcset="hero-desktop.webp"
        type="image/webp"
      >
      <!-- Fallback final: JPEG para cualquier navegador -->
      <img
        src="hero-desktop.jpg"
        alt="Imagen hero responsive"
        class="demo-image"
        loading="lazy"
        width="1200"
        height="600"
      >
    </picture>
  </section>
</body>
</html>
```

### Ejemplo Guiado 4: Tipografía responsive con clamp()

!!! example "Contexto pedagógico"
    Implementación de un sistema de tipografía completamente fluido usando CSS clamp(). Sin una sola media query, los tamaños de fuente se adaptan suavemente entre un mínimo y un máximo según el ancho del viewport.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ejemplo 4 - Tipografía Responsive con clamp()</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }

    body {
      font-family: 'Georgia', 'Times New Roman', serif;
      background: #fafafa;
      color: #333;
    }

    /*
     * ===== SISTEMA DE TIPOGRAFÍA RESPONSIVE =====
     *
     * clamp(min, preferido, max):
     *   min: tamaño mínimo (nunca será más pequeño, ni en móvil).
     *   preferido: valor fluido basado en viewport (2.5vw).
     *   max: tamaño máximo (nunca será más grande, ni en pantallas 4K).
     *
     * Ventajas: sin media queries, transiciones suaves,
     * consistencia en todos los dispositivos.
     */
    :root {
      /* Tamaño de fuente base fluido */
      --fs-base: clamp(1rem, 0.8rem + 0.5vw, 1.25rem);

      /* Escala tipográfica completa */
      --fs-h1: clamp(2rem, 1.5rem + 3vw, 4rem);
      --fs-h2: clamp(1.5rem, 1.2rem + 2vw, 3rem);
      --fs-h3: clamp(1.25rem, 1rem + 1.5vw, 2rem);
      --fs-small: clamp(0.75rem, 0.7rem + 0.25vw, 0.9rem);

      /* Longitud de línea óptima: 65 caracteres */
      --line-width: 65ch;
    }

    body { font-size: var(--fs-base); }

    /*
     * ===== ARTÍCULO DE EJEMPLO =====
     * max-width: 65ch asegura líneas de ~65 caracteres.
     * La unidad ch mide el ancho del carácter "0" en la fuente actual.
     * 65 caracteres por línea es el óptimo para lectura según estudios.
     */
    .article {
      max-width: var(--line-width);
      margin: 0 auto;
      padding: clamp(1rem, 5vw, 4rem);
    }

    h1 { font-size: var(--fs-h1); line-height: 1.1; margin-bottom: 1.5rem; }
    h2 { font-size: var(--fs-h2); line-height: 1.2; margin: 2rem 0 1rem; }
    h3 { font-size: var(--fs-h3); line-height: 1.3; margin: 1.5rem 0 0.75rem; }
    p { margin-bottom: 1.5rem; line-height: 1.7; }
    small { font-size: var(--fs-small); color: #666; }

    /*
     * ===== ESPACIADO FLUIDO =====
     * clamp() también se aplica a padding, margin y gap.
     * Esto crea layouts que "respiran" proporcionalmente.
     */
    .card {
      background: #fff;
      border-radius: 12px;
      box-shadow: 0 2px 12px rgba(0, 0, 0, 0.06);
      padding: clamp(1rem, 3vw, 2.5rem);
      margin: clamp(1rem, 4vw, 3rem) 0;
    }

    /* Demostración visual: barra que muestra el tamaño actual */
    .font-meter {
      background: #1a1a2e;
      color: #fff;
      padding: 0.5rem 1rem;
      border-radius: 8px;
      position: fixed;
      bottom: 1rem;
      right: 1rem;
      font-family: 'Courier New', monospace;
      font-size: 0.8rem;
    }
  </style>
</head>
<body>
  <article class="article">
    <h1>Tipografía Responsive: El futuro es fluido</h1>
    <p><small>Publicado el 10 de mayo de 2025 · 8 min de lectura</small></p>

    <p>La tipografía web ha evolucionado desde tamaños fijos en píxeles hasta
    sistemas completamente fluidos que se adaptan a cualquier dispositivo sin
    necesidad de media queries. La función clamp() de CSS es la clave de esta
    evolución.</p>

    <div class="card">
      <h2>¿Qué es clamp()?</h2>
      <p>La función CSS clamp() acepta tres parámetros: un valor mínimo, un valor
      preferido (generalmente basado en viewport) y un valor máximo. El navegador
      calcula el valor resultante y lo mantiene siempre dentro del rango definido,
      adaptándose suavemente al tamaño de pantalla.</p>

      <h3>Ventajas del enfoque fluido</h3>
      <p>El texto se adapta de forma continua a cualquier ancho de pantalla,
      sin saltos bruscos en los breakpoints. Esto significa que la tipografía
      se ve bien en 320px, 768px, 1024px y cualquier tamaño intermedio, sin
      necesidad de predefinir puntos de ruptura.</p>
    </div>

    <h2>La importancia de la longitud de línea</h2>
    <p>Los estudios de legibilidad coinciden en que la longitud óptima de línea
    para texto continuo está entre 45 y 75 caracteres. Líneas demasiado largas
    dificultan el seguimiento visual; líneas demasiado cortas fuerzan saltos
    frecuentes que rompen el ritmo de lectura. La unidad ch de CSS nos permite
    respetar esta restricción independientemente del tamaño de fuente.</p>
  </article>

  <!-- Indicador visual del tamaño de viewport actual -->
  <div class="font-meter">Viewport: <span id="vp-width"></span>px</div>
  <script>
    // Muestra el ancho actual del viewport en tiempo real
    document.getElementById('vp-width').textContent = window.innerWidth;
    window.addEventListener('resize', () => {
      document.getElementById('vp-width').textContent = window.innerWidth;
    });
  </script>
</body>
</html>
```


### Ejemplo Guiado 5: Container Queries - Componentes que se adaptan a su contenedor

!!! example "Contexto pedagógico"
    Las Container Queries permiten que un componente se adapte al tamaño de su elemento contenedor, no al viewport. Esto es revolucionario para componentes reutilizables que pueden aparecer en diferentes contextos de una misma página.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ejemplo 5 - Container Queries</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      padding: 2rem;
      background: #f0f2f5;
    }

    h1 { text-align: center; margin-bottom: 2rem; }

    /*
     * ===== DEMOSTRACIÓN DE CONTAINER QUERIES =====
     * Dos contenedores de diferente ancho (300px y 700px).
     * Cada uno contiene una tarjeta con container query.
     * La tarjeta se adapta al contenedor, no al viewport.
     */
    .demo {
      display: grid;
      grid-template-columns: 1fr 2fr;
      gap: 2rem;
      max-width: 1100px;
      margin: 0 auto;
    }

    .demo__sidebar {
      background: #fff;
      border-radius: 12px;
      padding: 1.5rem;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
    }

    .demo__main {
      background: #fff;
      border-radius: 12px;
      padding: 1.5rem;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
    }

    /*
     * ===== DEFINICIÓN DEL CONTENEDOR =====
     * container-type: inline-size habilita consultas basadas en el ancho.
     * container-name: opcional, permite nombrar el contenedor para referenciarlo.
     * A partir de aquí, podemos usar @container para consultar su tamaño.
     */
    .card-wrapper {
      container-type: inline-size;
      container-name: card;
    }

    /*
     * ===== COMPONENTE TARJETA =====
     * La tarjeta se adapta según el ancho de .card-wrapper (su contenedor),
     * NO según el ancho del viewport.
     *
     * Por defecto (contenedor estrecho, < 400px): layout vertical.
     * Cuando el contenedor tiene >= 400px: layout horizontal con imagen a la izquierda.
     */
    .card {
      background: #fff;
      border: 1px solid #e0e0e0;
      border-radius: 12px;
      overflow: hidden;
      display: grid;
      gap: 1rem;
    }

    /* Versión por defecto: imagen arriba (móvil / contenedor estrecho) */
    .card__image {
      background: linear-gradient(135deg, #667eea, #764ba2);
      color: #fff;
      display: flex;
      align-items: center;
      justify-content: center;
      min-height: 150px;
      font-size: 2rem;
    }

    .card__body { padding: 1rem; }
    .card__title { font-size: 1.1rem; margin-bottom: 0.5rem; }
    .card__text { color: #666; font-size: 0.9rem; }

    /*
     * ===== CONTAINER QUERY =====
     * @container card (min-width: 400px):
     *   "Cuando el contenedor llamado 'card' tenga al menos 400px de ancho..."
     */
    @container card (min-width: 400px) {
      .card {
        grid-template-columns: 1fr 2fr;
      }

      .card__image {
        min-height: 100%;
      }

      .card__body {
        padding: 1.5rem;
      }

      .card__title {
        font-size: 1.3rem;
      }
    }

    /*
     * ===== UNIDADES DE CONTENEDOR =====
     * cqw: 1% del ancho del contenedor.
     * Estas unidades son relativas al contenedor, no al viewport.
     */
    .tag {
      display: inline-block;
      background: #667eea;
      color: #fff;
      padding: 0.25rem 0.75rem;
      border-radius: 20px;
      font-size: clamp(0.7rem, 3cqi, 0.9rem);
      margin-top: 0.5rem;
    }

    .section-label {
      font-size: 0.8rem;
      text-transform: uppercase;
      color: #999;
      margin-bottom: 1rem;
      letter-spacing: 0.5px;
    }
  </style>
</head>
<body>
  <h1>Container Queries: Mismo componente, diferente contexto</h1>

  <div class="demo">
    <!--
      Columna izquierda (estrecha, ~300px):
      La tarjeta se renderizará en modo vertical porque el contenedor
      es más estrecho que 400px. @container card no se activa.
    -->
    <div class="demo__sidebar">
      <p class="section-label">Sidebar (contenedor ~300px)</p>
      <div class="card-wrapper">
        <div class="card">
          <div class="card__image">IMG</div>
          <div class="card__body">
            <h3 class="card__title">Tarjeta en sidebar</h3>
            <p class="card__text">Esta tarjeta se adapta al sidebar estrecho.
            Imagen arriba, contenido abajo. Layout vertical.</p>
            <span class="tag">CSS</span>
          </div>
        </div>
      </div>
    </div>

    <!--
      Columna derecha (ancha, ~700px):
      La MISMA tarjeta ahora se renderiza en modo horizontal porque
      el contenedor supera los 400px. @container card se activa.
    -->
    <div class="demo__main">
      <p class="section-label">Contenido principal (contenedor ~700px)</p>
      <div class="card-wrapper">
        <div class="card">
          <div class="card__image">IMG</div>
          <div class="card__body">
            <h3 class="card__title">Tarjeta en zona principal</h3>
            <p class="card__text">La misma tarjeta, pero ahora el contenedor
            es más ancho. Layout horizontal con imagen a la izquierda. Todo
            controlado por @container, sin media queries.</p>
            <span class="tag">Container Queries</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</body>
</html>
```

### Ejemplo Guiado 6: Tabla responsive con 3 estrategias

!!! example "Contexto pedagógico"
    Las tablas son uno de los elementos más problemáticos en diseño responsive. Este ejemplo demuestra tres estrategias: scroll horizontal, colapso en cards (ideal para móvil), y ocultación de columnas no esenciales.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ejemplo 6 - Tablas Responsive</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      padding: 2rem;
      background: #f5f6fa;
    }

    h2 { margin: 2rem 0 1rem; color: #333; }
    p { color: #666; margin-bottom: 1rem; }

    /* Estilos base para todas las tablas */
    table {
      width: 100%;
      border-collapse: collapse;
      background: #fff;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
      border-radius: 8px;
      overflow: hidden;
    }

    th, td {
      padding: 0.75rem 1rem;
      text-align: left;
      border-bottom: 1px solid #eee;
    }

    th {
      background: #1a1a2e;
      color: #fff;
      font-weight: 600;
    }

    tr:hover td { background: #f8f9fa; }

    /*
     * ===== ESTRATEGIA 1: SCROLL HORIZONTAL =====
     * La solución más simple: envolver la tabla en un contenedor
     * con overflow-x: auto. En móvil aparece una barra de scroll.
     * Ideal cuando la tabla tiene muchas columnas y los datos
     * no pueden reorganizarse en formato vertical.
     */
    .table-scroll {
      overflow-x: auto;
      -webkit-overflow-scrolling: touch; /* Scroll suave en iOS */
    }

    .table-scroll table {
      min-width: 700px; /* Ancho mínimo para que todas las columnas quepan */
    }

    /*
     * ===== ESTRATEGIA 2: COLAPSO EN CARDS =====
     * En móvil, cada fila se convierte en una "tarjeta" vertical.
     * Usamos data-label en los td para mostrar el nombre de la columna.
     * El contenido de data-label se muestra con CSS ::before.
     * Esta técnica es excelente para tablas con pocas columnas
     * donde cada registro tiene sentido como unidad independiente.
     */
    .table-cards thead {
      /* En desktop mostramos la cabecera normalmente */
    }

    @media (max-width: 600px) {
      .table-cards thead {
        display: none; /* Ocultamos la cabecera en móvil */
      }

      .table-cards tr {
        display: block;
        margin-bottom: 1rem;
        border: 1px solid #ddd;
        border-radius: 8px;
      }

      .table-cards td {
        display: block;
        text-align: right;
        padding: 0.5rem 1rem;
        border-bottom: 1px solid #f0f0f0;
      }

      /*
       * ::before muestra el nombre de la columna desde data-label.
       * content: attr(data-label) lee el atributo HTML.
       */
      .table-cards td::before {
        content: attr(data-label);
        float: left;
        font-weight: 600;
        color: #1a1a2e;
      }

      .table-cards td:last-child { border-bottom: none; }
    }

    /*
     * ===== ESTRATEGIA 3: OCULTAR COLUMNAS NO ESENCIALES =====
     * En pantallas pequeñas, ocultamos las columnas menos importantes.
     * Usamos clases semánticas: .col-esencial, .col-secundaria, .col-opcional.
     * Esto preserva el formato de tabla pero reduce el ancho.
     */
    @media (max-width: 768px) {
      .col-opcional { display: none; }
    }

    @media (max-width: 480px) {
      .col-secundaria { display: none; }
    }
  </style>
</head>
<body>
  <h1>Estrategias para Tablas Responsive</h1>

  <!-- ESTRATEGIA 1: Scroll horizontal -->
  <section>
    <h2>Estrategia 1: Scroll horizontal</h2>
    <p>Envuelve la tabla en un contenedor con overflow-x: auto.
    En móvil, el usuario puede deslizar horizontalmente para ver todas las columnas.</p>
    <div class="table-scroll">
      <table>
        <thead>
          <tr>
            <th>ID</th><th>Nombre</th><th>Email</th><th>Teléfono</th><th>Ciudad</th><th>País</th><th>Fecha</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>1</td><td>María García</td><td>maria@email.com</td><td>+34 600 111 222</td><td>Málaga</td><td>España</td><td>2025-01-15</td>
          </tr>
          <tr>
            <td>2</td><td>Carlos Ruiz</td><td>carlos@email.com</td><td>+34 600 333 444</td><td>Sevilla</td><td>España</td><td>2025-02-20</td>
          </tr>
          <tr>
            <td>3</td><td>Ana López</td><td>ana@email.com</td><td>+34 600 555 666</td><td>Granada</td><td>España</td><td>2025-03-10</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <!-- ESTRATEGIA 2: Cards -->
  <section>
    <h2>Estrategia 2: Colapso en tarjetas (cards)</h2>
    <p>En móvil, cada fila se convierte en una tarjeta. Los data-label muestran el nombre de cada columna. Redimensiona a menos de 600px para ver el efecto.</p>
    <table class="table-cards">
      <thead>
        <tr>
          <th>Producto</th><th>Categoría</th><th>Precio</th><th>Stock</th><th>Ventas</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td data-label="Producto">Portátil Pro 15"</td>
          <td data-label="Categoría">Electrónica</td>
          <td data-label="Precio">999,00 €</td>
          <td data-label="Stock">45</td>
          <td data-label="Ventas">230</td>
        </tr>
        <tr>
          <td data-label="Producto">Monitor 4K 27"</td>
          <td data-label="Categoría">Monitores</td>
          <td data-label="Precio">449,00 €</td>
          <td data-label="Stock">18</td>
          <td data-label="Ventas">98</td>
        </tr>
        <tr>
          <td data-label="Producto">Teclado Mecánico</td>
          <td data-label="Categoría">Periféricos</td>
          <td data-label="Precio">89,99 €</td>
          <td data-label="Stock">120</td>
          <td data-label="Ventas">450</td>
        </tr>
      </tbody>
    </table>
  </section>

  <!-- ESTRATEGIA 3: Ocultar columnas -->
  <section>
    <h2>Estrategia 3: Ocultar columnas no esenciales</h2>
    <p>Columnas con clase .col-opcional se ocultan a 768px. Columnas .col-secundaria a 480px. Las columnas esenciales siempre visibles.</p>
    <table>
      <thead>
        <tr>
          <th class="col-esencial">ID</th>
          <th class="col-esencial">Cliente</th>
          <th class="col-secundaria">Email</th>
          <th class="col-opcional">Teléfono</th>
          <th class="col-opcional">Notas</th>
          <th class="col-esencial">Estado</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td class="col-esencial">#1024</td>
          <td class="col-esencial">Juan Pérez</td>
          <td class="col-secundaria">juan@email.com</td>
          <td class="col-opcional">+34 666 777 888</td>
          <td class="col-opcional">Entrega urgente solicitada</td>
          <td class="col-esencial">Pendiente</td>
        </tr>
        <tr>
          <td class="col-esencial">#1025</td>
          <td class="col-esencial">Laura Díaz</td>
          <td class="col-secundaria">laura@email.com</td>
          <td class="col-opcional">+34 666 999 000</td>
          <td class="col-opcional">Cliente VIP</td>
          <td class="col-esencial">Completado</td>
        </tr>
      </tbody>
    </table>
  </section>
</body>
</html>
```

### Ejemplo Guiado 7: Media Queries modernas - prefers-color-scheme, prefers-reduced-motion

!!! example "Contexto pedagógico"
    Demostración de las media queries de preferencias de usuario, que permiten adaptar la experiencia a las necesidades y preferencias de cada persona. El modo oscuro y la reducción de movimiento son las dos más importantes para accesibilidad.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ejemplo 7 - Media Queries de Preferencias</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: 'Segoe UI', system-ui, sans-serif; }

    /*
     * ===== VARIABLES CSS PARA TEMA CLARO (POR DEFECTO) =====
     * Definimos las variables con valores de tema claro.
     * Estas se sobrescriben en prefers-color-scheme: dark.
     */
    :root {
      --bg: #ffffff;
      --bg-secondary: #f5f5f5;
      --text: #1a1a2e;
      --text-secondary: #666666;
      --border: #e0e0e0;
      --accent: #6c5ce7;
      --card-bg: #ffffff;
      --card-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
    }

    /*
     * ===== TEMA OSCURO =====
     * Cuando el usuario tiene configurado el modo oscuro en su sistema,
     * sobrescribimos todas las variables con valores oscuros.
     * NO necesitamos clases .dark ni JavaScript.
     */
    @media (prefers-color-scheme: dark) {
      :root {
        --bg: #0d1117;
        --bg-secondary: #161b22;
        --text: #e6edf3;
        --text-secondary: #8b949e;
        --border: #30363d;
        --accent: #7c6cf0;
        --card-bg: #161b22;
        --card-shadow: 0 2px 12px rgba(0, 0, 0, 0.3);
      }
    }

    body {
      background: var(--bg);
      color: var(--text);
      transition: background 0.3s, color 0.3s;
    }

    .container {
      max-width: 800px;
      margin: 0 auto;
      padding: 2rem;
    }

    h1 { margin-bottom: 1rem; color: var(--accent); }
    p { color: var(--text-secondary); line-height: 1.6; margin-bottom: 1rem; }

    .card {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 1.5rem;
      margin-bottom: 1.5rem;
      box-shadow: var(--card-shadow);
    }

    /*
     * ===== PREFIERE MOVIMIENTO REDUCIDO =====
     * Respeta la configuración de accesibilidad del sistema operativo.
     * Si el usuario ha activado "Reducir movimiento", eliminamos
     * o reducimos drásticamente las animaciones y transiciones.
     */
    @media (prefers-reduced-motion: reduce) {
      *,
      *::before,
      *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
        scroll-behavior: auto !important;
      }
    }

    /*
     * Animación de ejemplo que se desactiva con prefers-reduced-motion.
     * En condiciones normales, la tarjeta se eleva al hacer hover.
     */
    .animated-card {
      transition: transform 0.3s, box-shadow 0.3s;
    }

    .animated-card:hover {
      transform: translateY(-4px);
      box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
    }

    /*
     * La animación de pulso se elimina completamente
     * en modo de movimiento reducido.
     */
    @keyframes pulse {
      0%, 100% { transform: scale(1); }
      50% { transform: scale(1.05); }
    }

    .pulse-demo {
      display: inline-block;
      padding: 0.5rem 1.5rem;
      background: var(--accent);
      color: #fff;
      border-radius: 25px;
      animation: pulse 2s infinite;
    }

    /* ===== MEDIA QUERY PARA IMPRESIÓN ===== */
    @media print {
      body { font-size: 12pt; }
      .no-print { display: none; }
      .card { box-shadow: none; border: 1px solid #ccc; break-inside: avoid; }
      a { color: #000; text-decoration: underline; }
    }

    .theme-indicator {
      display: inline-block;
      padding: 0.25rem 0.75rem;
      border-radius: 20px;
      font-size: 0.8rem;
      background: var(--bg-secondary);
      border: 1px solid var(--border);
    }

    .no-print { margin-top: 1rem; }
  </style>
</head>
<body>
  <div class="container">
    <h1>Media Queries de Preferencias de Usuario</h1>

    <p>
      <span class="theme-indicator">
        Tema actual: <span id="theme-label">detectando...</span>
      </span>
    </p>

    <div class="card animated-card">
      <h2>Tarjeta con animación hover</h2>
      <p>Pasa el ratón por encima para ver la animación. Si tu sistema tiene
      "Reducir movimiento" activado, la animación se desactivará automáticamente
      gracias a prefers-reduced-motion: reduce.</p>
    </div>

    <div class="card">
      <h2>Demostración de pulso</h2>
      <span class="pulse-demo">Botón animado</span>
      <p style="margin-top: 1rem;">Este botón tiene una animación de pulso. Con
      prefers-reduced-motion: reduce, la animación se detiene inmediatamente
      (duración de 0.01ms, una sola iteración).</p>
    </div>

    <div class="card no-print">
      <h2>Modo oscuro automático</h2>
      <p>Este sitio se adapta automáticamente al modo claro u oscuro según la
      configuración de tu sistema operativo. Cambia la preferencia en los ajustes
      de tu dispositivo para ver la diferencia.</p>
      <p>Esto se logra con @media (prefers-color-scheme: dark) y variables CSS,
      sin necesidad de JavaScript ni clases adicionales.</p>
    </div>

    <p class="no-print" style="text-align:center; color: var(--text-secondary);">
      Este párrafo tiene clase .no-print - no aparecerá al imprimir la página.
    </p>
  </div>

  <!-- Script para detectar el tema actual -->
  <script>
    // Detectamos el esquema de color actual del sistema
    const isDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    document.getElementById('theme-label').textContent = isDark ? 'Oscuro' : 'Claro';

    // Escuchamos cambios en tiempo real
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
      document.getElementById('theme-label').textContent = e.matches ? 'Oscuro' : 'Claro';
    });
  </script>
</body>
</html>
```


### Ejemplo Guiado 8: Layout Shifter con Grid Template Areas

!!! example "Contexto pedagógico"
    El patrón Layout Shifter es el más potente de los patrones responsive. Consiste en reorganizar completamente la disposición de los elementos en diferentes breakpoints. CSS Grid con grid-template-areas lo hace trivial, ya que basta con redefinir el mapa de áreas en cada media query.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ejemplo 8 - Layout Shifter con Grid</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: 'Segoe UI', sans-serif; min-height: 100vh; }

    /*
     * ===== LAYOUT SHIFTER =====
     * El layout cambia completamente entre breakpoints.
     * Móvil: todo en 1 columna.
     * Tablet: 2 columnas (sidebar + contenido).
     * Desktop: 3 columnas (sidebar izq + contenido + sidebar der).
     *
     * La magia está en redefinir grid-template-areas en cada
     * media query. El HTML no cambia en absoluto.
     */
    .page {
      display: grid;
      min-height: 100vh;
      gap: 0;
    }

    /* ===== MÓVIL (por defecto, < 768px) ===== */
    /* Layout: una sola columna con todas las secciones apiladas */
    .page {
      grid-template-columns: 1fr;
      grid-template-rows: auto;
      grid-template-areas:
        "header"
        "nav"
        "content"
        "sidebar-left"
        "sidebar-right"
        "footer";
    }

    /* ===== TABLET (>= 768px) ===== */
    /* Layout: 2 columnas. Sidebar izquierdo arriba a la izquierda */
    @media (min-width: 768px) {
      .page {
        grid-template-columns: 250px 1fr;
        grid-template-rows: auto auto 1fr auto;
        grid-template-areas:
          "header       header"
          "nav          nav"
          "sidebar-left content"
          "sidebar-right sidebar-right"
          "footer       footer";
      }
    }

    /* ===== DESKTOP (>= 1024px) ===== */
    /* Layout: 3 columnas completas con dos sidebars */
    @media (min-width: 1024px) {
      .page {
        grid-template-columns: 250px 1fr 250px;
        grid-template-rows: auto auto 1fr auto;
        grid-template-areas:
          "header        header        header"
          "nav           nav           nav"
          "sidebar-left  content       sidebar-right"
          "footer        footer        footer";
      }
    }

    /* ===== ESTILOS VISUALES ===== */
    .header  { grid-area: header;  background: #1a1a2e; color: #fff; padding: 1.5rem; text-align: center; }
    .nav     { grid-area: nav;     background: #16213e; color: #fff; padding: 1rem; }
    .nav a   { color: #ccc; text-decoration: none; margin: 0 1rem; }
    .content { grid-area: content; background: #fff; padding: 2rem; }
    .sidebar-left  { grid-area: sidebar-left;  background: #f0f0f0; padding: 1.5rem; }
    .sidebar-right { grid-area: sidebar-right; background: #e8e8e8; padding: 1.5rem; }
    .footer  { grid-area: footer;  background: #1a1a2e; color: #ccc; padding: 1.5rem; text-align: center; }

    /* Indicador visual del breakpoint activo */
    .breakpoint-indicator {
      position: fixed;
      bottom: 1rem;
      left: 1rem;
      background: #1a1a2e;
      color: #fff;
      padding: 0.5rem 1rem;
      border-radius: 8px;
      font-size: 0.8rem;
      font-family: monospace;
    }

    @media (min-width: 1024px) {
      .breakpoint-indicator { background: #10b981; }
    }
  </style>
</head>
<body>
  <div class="page">
    <header class="header">
      <h1>Layout Shifter</h1>
      <p>El layout se reorganiza completamente en cada breakpoint</p>
    </header>

    <nav class="nav">
      <a href="#">Inicio</a>
      <a href="#">Artículos</a>
      <a href="#">Galería</a>
      <a href="#">Contacto</a>
    </nav>

    <main class="content">
      <h2>Contenido Principal</h2>
      <p>Observa cómo cambia la disposición de este contenido y los sidebars
      al redimensionar la ventana. En móvil, los sidebars están debajo del
      contenido. En tablet, el sidebar izquierdo aparece a la izquierda.
      En desktop, ambos sidebars flanquean el contenido.</p>
      <p>Todo esto se logra redefiniendo grid-template-areas en cada media query.
      El HTML permanece idéntico en todos los breakpoints.</p>
    </main>

    <aside class="sidebar-left">
      <h3>Sidebar Izquierdo</h3>
      <p>En móvil: debajo del contenido.</p>
      <p>En tablet: a la izquierda.</p>
      <p>En desktop: a la izquierda.</p>
    </aside>

    <aside class="sidebar-right">
      <h3>Sidebar Derecho</h3>
      <p>En móvil: al final de la página.</p>
      <p>En tablet: debajo en ancho completo.</p>
      <p>En desktop: a la derecha del contenido.</p>
    </aside>

    <footer class="footer">
      2025 Layout Shifter Demo
    </footer>
  </div>

  <div class="breakpoint-indicator">
    Breakpoint: <span id="bp-label">Móvil</span>
  </div>

  <script>
    function updateBreakpoint() {
      const w = window.innerWidth;
      let label = 'Móvil (< 768px)';
      if (w >= 1024) label = 'Desktop (>= 1024px)';
      else if (w >= 768) label = 'Tablet (768-1023px)';
      document.getElementById('bp-label').textContent = label;
    }
    window.addEventListener('resize', updateBreakpoint);
    updateBreakpoint();
  </script>
</body>
</html>
```

### Ejemplo Guiado 9: Menú off-canvas con transición CSS

!!! example "Contexto pedagógico"
    Un menú off-canvas que se desliza desde la izquierda en dispositivos móviles y permanece visible en desktop. Implementado con CSS transitions y una mínima lógica JavaScript, superior al checkbox hack porque permite animaciones suaves y control del foco.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ejemplo 9 - Menú Off-Canvas</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      overflow-x: hidden; /* Evita scroll horizontal cuando el menú está fuera */
    }

    /*
     * ===== MENÚ OFF-CANVAS =====
     * En móvil, el menú está oculto fuera de la pantalla (translateX(-100%)).
     * Al activarse, se desliza hacia dentro con una transición suave.
     * Un overlay semitransparente cubre el contenido principal.
     */
    .offcanvas {
      position: fixed;
      top: 0;
      left: 0;
      width: 280px; /* Ancho del menú en móvil */
      height: 100vh;
      background: #1a1a2e;
      color: #fff;
      z-index: 1000;
      /*
       * Transform: translateX(-100%) mueve el menú completamente
       * fuera de la pantalla hacia la izquierda.
       * transition suaviza el movimiento de entrada/salida.
       */
      transform: translateX(-100%);
      transition: transform 0.3s ease;
      padding: 1.5rem;
      overflow-y: auto;
    }

    /* Clase que se añade con JS para mostrar el menú */
    .offcanvas--open {
      transform: translateX(0);
    }

    .offcanvas__close {
      background: none;
      border: none;
      color: #fff;
      font-size: 1.8rem;
      cursor: pointer;
      position: absolute;
      top: 1rem;
      right: 1rem;
    }

    .offcanvas a {
      display: block;
      color: #ccc;
      text-decoration: none;
      padding: 0.75rem 1rem;
      border-radius: 8px;
      margin-bottom: 0.25rem;
      transition: background 0.2s;
    }

    .offcanvas a:hover {
      background: rgba(255, 255, 255, 0.1);
      color: #fff;
    }

    /*
     * ===== OVERLAY =====
     * Capa semitransparente que cubre el contenido cuando el menú está abierto.
     * opacity: 0 (invisible) -> opacity: 1 (visible) con transición.
     * pointer-events: none evita que bloquee clicks cuando está oculto.
     */
    .overlay {
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.5);
      z-index: 999;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.3s ease;
    }

    .overlay--visible {
      opacity: 1;
      pointer-events: auto;
    }

    /* ===== CABECERA PRINCIPAL ===== */
    .main-header {
      background: #1a1a2e;
      color: #fff;
      padding: 1rem 1.5rem;
      display: flex;
      align-items: center;
      gap: 1rem;
    }

    .main-header__menu-btn {
      background: none;
      border: 1px solid rgba(255, 255, 255, 0.3);
      color: #fff;
      font-size: 1.5rem;
      padding: 0.25rem 0.5rem;
      border-radius: 6px;
      cursor: pointer;
      display: none; /* Oculto en desktop */
    }

    .main-header__brand {
      font-size: 1.3rem;
      font-weight: 700;
    }

    /* ===== NAVEGACIÓN DESKTOP (siempre visible) ===== */
    .desktop-nav {
      display: flex;
      gap: 1rem;
      margin-left: auto;
    }

    .desktop-nav a {
      color: #ccc;
      text-decoration: none;
      padding: 0.5rem 0.75rem;
      border-radius: 4px;
      transition: background 0.2s;
    }

    .desktop-nav a:hover { background: rgba(255,255,255,0.1); color: #fff; }

    /* Contenido */
    .content {
      padding: 2rem;
      max-width: 800px;
      margin: 0 auto;
      line-height: 1.7;
    }

    /*
     * ===== RESPONSIVE =====
     * En móvil: ocultamos la nav desktop, mostramos el botón hamburguesa.
     * En desktop: mostramos la nav desktop, ocultamos el botón.
     */
    @media (max-width: 768px) {
      .main-header__menu-btn { display: block; }
      .desktop-nav { display: none; }
    }
  </style>
</head>
<body>
  <!-- Overlay que oscurece el fondo -->
  <div class="overlay" id="overlay"></div>

  <!-- Menú off-canvas (oculto fuera de pantalla en móvil) -->
  <nav class="offcanvas" id="offcanvas">
    <button class="offcanvas__close" id="close-menu">&times;</button>
    <h2 style="margin-bottom:1.5rem;">Menú</h2>
    <a href="#">Inicio</a>
    <a href="#">Servicios</a>
    <a href="#">Proyectos</a>
    <a href="#">Blog</a>
    <a href="#">Contacto</a>
    <hr style="border-color:rgba(255,255,255,0.1); margin:1rem 0;">
    <a href="#">Mi cuenta</a>
    <a href="#">Configuración</a>
    <a href="#">Cerrar sesión</a>
  </nav>

  <!-- Cabecera principal -->
  <header class="main-header">
    <button class="main-header__menu-btn" id="open-menu">&#9776;</button>
    <span class="main-header__brand">OffCanvas Demo</span>
    <nav class="desktop-nav">
      <a href="#">Inicio</a>
      <a href="#">Servicios</a>
      <a href="#">Proyectos</a>
      <a href="#">Blog</a>
      <a href="#">Contacto</a>
    </nav>
  </header>

  <!-- Contenido -->
  <div class="content">
    <h1>Menú Off-Canvas con Transiciones CSS</h1>
    <p>En dispositivos móviles, haz clic en el botón de hamburguesa para abrir
    el menú lateral. El menú se desliza suavemente desde la izquierda y un
    overlay semitransparente cubre el contenido. Haz clic fuera del menú o en
    la X para cerrarlo.</p>
    <p>En desktop, el menú se muestra siempre visible como navegación horizontal
    en la cabecera, sin necesidad de off-canvas.</p>
  </div>

  <script>
    const offcanvas = document.getElementById('offcanvas');
    const overlay = document.getElementById('overlay');
    const openBtn = document.getElementById('open-menu');
    const closeBtn = document.getElementById('close-menu');

    function openMenu() {
      offcanvas.classList.add('offcanvas--open');
      overlay.classList.add('overlay--visible');
      document.body.style.overflow = 'hidden'; /* Bloquea scroll del body */
    }

    function closeMenu() {
      offcanvas.classList.remove('offcanvas--open');
      overlay.classList.remove('overlay--visible');
      document.body.style.overflow = '';
    }

    openBtn.addEventListener('click', openMenu);
    closeBtn.addEventListener('click', closeMenu);
    overlay.addEventListener('click', closeMenu);

    // Cerrar con la tecla Escape (accesibilidad)
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && offcanvas.classList.contains('offcanvas--open')) {
        closeMenu();
      }
    });
  </script>
</body>
</html>
```

### Ejemplo Guiado 10: Proyecto completo responsive Mobile First

!!! example "Contexto pedagógico"
    Proyecto final que integra todas las técnicas aprendidas: Mobile First, Grid con áreas, tipografía y espaciado fluidos con clamp(), imágenes responsive, menú hamburguesa, y media queries estratégicas. Una página web profesional completamente responsive.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <!-- VIEWPORT: imprescindible para responsive -->
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Proyecto Responsive Completo</title>
  <style>
    /* ===== RESET ===== */
    * { margin: 0; padding: 0; box-sizing: border-box; }

    /*
     * ===== VARIABLES Y TIPOGRAFÍA FLUIDA =====
     * Todo el sistema tipográfico usa clamp() para adaptarse
     * suavemente a cualquier ancho de pantalla.
     */
    :root {
      --color-primary: #2563eb;
      --color-dark: #1e293b;
      --color-light: #f8fafc;
      --color-muted: #64748b;
      --fs-h1: clamp(2rem, 5vw, 3.5rem);
      --fs-h2: clamp(1.5rem, 3vw, 2.5rem);
      --fs-body: clamp(1rem, 0.9rem + 0.3vw, 1.15rem);
      --spacing: clamp(1rem, 4vw, 3rem);
    }

    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      font-size: var(--fs-body);
      color: var(--color-dark);
      line-height: 1.6;
    }

    /* ===== UTILIDADES ===== */
    .container {
      width: min(100% - 2rem, 1100px);
      margin-inline: auto;
    }

    .btn {
      display: inline-block;
      padding: 0.75rem 2rem;
      border-radius: 8px;
      font-weight: 600;
      text-decoration: none;
      cursor: pointer;
      border: none;
      font-size: inherit;
      transition: transform 0.2s;
    }

    .btn:hover { transform: translateY(-2px); }
    .btn--primary { background: var(--color-primary); color: #fff; }
    .btn--outline { background: transparent; border: 2px solid #fff; color: #fff; }

    /*
     * ===== CABECERA (MÓVIL: hamburguesa) =====
     * Layout base Mobile First: logo + botón hamburguesa.
     * El menú se oculta con max-height: 0.
     */
    .header {
      background: #fff;
      box-shadow: 0 1px 3px rgba(0,0,0,0.1);
      position: sticky;
      top: 0;
      z-index: 100;
      padding: 1rem;
    }

    .header__inner {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
    }

    .header__logo { font-size: 1.3rem; font-weight: 700; color: var(--color-primary); }
    .header__toggle { display: block; background: none; border: none; font-size: 1.8rem; cursor: pointer; color: var(--color-dark); }
    .header__checkbox { display: none; }
    .header__nav { width: 100%; max-height: 0; overflow: hidden; transition: max-height 0.4s ease; }

    /* Checkbox hack para abrir/cerrar el menú */
    .header__checkbox:checked ~ .header__nav { max-height: 400px; }

    .header__nav a {
      display: block;
      padding: 0.75rem 0;
      color: var(--color-dark);
      text-decoration: none;
      border-top: 1px solid #f0f0f0;
      transition: color 0.2s;
    }

    .header__nav a:hover { color: var(--color-primary); }

    /* ===== HÉROE ===== */
    .hero {
      background: linear-gradient(135deg, var(--color-primary), #7c3aed);
      color: #fff;
      padding: var(--spacing) 1rem;
      text-align: center;
    }

    .hero h1 { font-size: var(--fs-h1); line-height: 1.15; margin-bottom: 1rem; }
    .hero p { font-size: var(--fs-body); opacity: 0.9; margin-bottom: 2rem; max-width: 600px; margin-inline: auto; }

    .hero__buttons { display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; }

    /* ===== CARACTERÍSTICAS ===== */
    .features { padding: var(--spacing) 0; }
    .features h2 { font-size: var(--fs-h2); text-align: center; margin-bottom: var(--spacing); }
    .features__grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 2rem;
    }

    .feature { text-align: center; padding: 1.5rem; }
    .feature__icon { font-size: 2.5rem; margin-bottom: 0.5rem; display: block; }
    .feature h3 { margin-bottom: 0.5rem; }
    .feature p { color: var(--color-muted); }

    /* ===== TESTIMONIOS ===== */
    .testimonials { background: var(--color-light); padding: var(--spacing) 0; }
    .testimonials h2 { font-size: var(--fs-h2); text-align: center; margin-bottom: var(--spacing); }
    .testimonials__grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 2rem;
    }

    .testimonial { background: #fff; padding: 1.5rem; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }
    .testimonial__text { font-style: italic; margin-bottom: 1rem; }
    .testimonial__author { font-weight: 600; }

    /* ===== CTA ===== */
    .cta {
      background: var(--color-dark);
      color: #fff;
      text-align: center;
      padding: var(--spacing) 1rem;
    }

    .cta h2 { font-size: var(--fs-h2); margin-bottom: 1rem; }
    .cta p { color: var(--color-muted); margin-bottom: 2rem; }

    /* ===== FOOTER ===== */
    .footer {
      background: #0f172a;
      color: #94a3b8;
      padding: var(--spacing) 0;
    }

    .footer__grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 2rem;
      margin-bottom: 2rem;
    }

    .footer__col h4 { color: #fff; margin-bottom: 1rem; }
    .footer__col a { display: block; color: #94a3b8; text-decoration: none; padding: 0.25rem 0; transition: color 0.2s; }
    .footer__col a:hover { color: #fff; }
    .footer__bottom { text-align: center; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 2rem; font-size: 0.9rem; }

    /* ===== MEDIA QUERIES ===== */
    /* Tablet: menú horizontal siempre visible, sin hamburguesa */
    @media (min-width: 768px) {
      .header__toggle { display: none; }
      .header__inner { flex-wrap: nowrap; }
      .header__nav {
        width: auto;
        max-height: none;
        overflow: visible;
        display: flex;
        gap: 1.5rem;
      }
      .header__nav a { border-top: none; padding: 0.25rem 0; }
    }
  </style>
</head>
<body>
  <!-- ===== CABECERA ===== -->
  <header class="header">
    <div class="header__inner container">
      <span class="header__logo">Empresa</span>
      <label for="menu-toggle" class="header__toggle">&#9776;</label>
      <input type="checkbox" id="menu-toggle" class="header__checkbox">
      <nav class="header__nav">
        <a href="#">Inicio</a>
        <a href="#">Servicios</a>
        <a href="#">Proyectos</a>
        <a href="#">Blog</a>
        <a href="#">Contacto</a>
      </nav>
    </div>
  </header>

  <!-- ===== HÉROE ===== -->
  <section class="hero">
    <div class="container">
      <h1>Creamos experiencias digitales que transforman negocios</h1>
      <p>Somos un equipo de diseñadores y desarrolladores apasionados por crear productos digitales que marcan la diferencia.</p>
      <div class="hero__buttons">
        <a href="#" class="btn btn--primary">Comenzar proyecto</a>
        <a href="#" class="btn btn--outline">Conocer más</a>
      </div>
    </div>
  </section>

  <!-- ===== CARACTERÍSTICAS ===== -->
  <section class="features">
    <div class="container">
      <h2>Lo que ofrecemos</h2>
      <div class="features__grid">
        <div class="feature">
          <span class="feature__icon">🎯</span>
          <h3>Estrategia digital</h3>
          <p>Definimos la hoja de ruta para alcanzar tus objetivos de negocio en el entorno digital.</p>
        </div>
        <div class="feature">
          <span class="feature__icon">🎨</span>
          <h3>Diseño UX/UI</h3>
          <p>Creamos interfaces intuitivas y atractivas centradas en la experiencia del usuario final.</p>
        </div>
        <div class="feature">
          <span class="feature__icon">💻</span>
          <h3>Desarrollo web</h3>
          <p>Construimos aplicaciones web modernas, rápidas y escalables con las mejores tecnologías.</p>
        </div>
        <div class="feature">
          <span class="feature__icon">📱</span>
          <h3>100% Responsive</h3>
          <p>Todos nuestros proyectos se adaptan perfectamente a cualquier dispositivo y tamaño de pantalla.</p>
        </div>
        <div class="feature">
          <span class="feature__icon">🔒</span>
          <h3>Seguridad</h3>
          <p>Implementamos las mejores prácticas de seguridad para proteger tus datos y los de tus usuarios.</p>
        </div>
        <div class="feature">
          <span class="feature__icon">📊</span>
          <h3>Analítica web</h3>
          <p>Medimos y optimizamos el rendimiento de tu sitio para maximizar los resultados de tu inversión.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- ===== TESTIMONIOS ===== -->
  <section class="testimonials">
    <div class="container">
      <h2>Lo que dicen nuestros clientes</h2>
      <div class="testimonials__grid">
        <div class="testimonial">
          <p class="testimonial__text">"Transformaron nuestra presencia online por completo. El nuevo sitio web duplicó nuestras conversiones en solo tres meses."</p>
          <p class="testimonial__author">María García · CEO TechStart</p>
        </div>
        <div class="testimonial">
          <p class="testimonial__text">"Trabajar con ellos fue un placer. Entregaron a tiempo y la calidad del producto final superó nuestras expectativas."</p>
          <p class="testimonial__author">Carlos Ruiz · Director Marketing</p>
        </div>
        <div class="testimonial">
          <p class="testimonial__text">"El equipo entendió perfectamente nuestra visión y la tradujo en una interfaz elegante y funcional."</p>
          <p class="testimonial__author">Ana López · Fundadora EcoShop</p>
        </div>
      </div>
    </div>
  </section>

  <!-- ===== CTA ===== -->
  <section class="cta">
    <div class="container">
      <h2>¿Listo para empezar?</h2>
      <p>Cuéntanos tu proyecto y te ayudaremos a hacerlo realidad.</p>
      <a href="#" class="btn btn--primary">Contactar ahora</a>
    </div>
  </section>

  <!-- ===== FOOTER ===== -->
  <footer class="footer">
    <div class="container">
      <div class="footer__grid">
        <div class="footer__col">
          <h4>Empresa</h4>
          <p>Desarrollo web profesional desde 2018.</p>
        </div>
        <div class="footer__col">
          <h4>Servicios</h4>
          <a href="#">Desarrollo Web</a>
          <a href="#">Apps Móviles</a>
          <a href="#">Consultoría UX/UI</a>
        </div>
        <div class="footer__col">
          <h4>Enlaces</h4>
          <a href="#">Blog</a>
          <a href="#">Proyectos</a>
          <a href="#">Contacto</a>
        </div>
        <div class="footer__col">
          <h4>Legal</h4>
          <a href="#">Aviso legal</a>
          <a href="#">Privacidad</a>
          <a href="#">Cookies</a>
        </div>
      </div>
      <div class="footer__bottom">2025 Empresa. Todos los derechos reservados.</div>
    </div>
  </footer>
</body>
</html>
```

## Casos reales

### Caso 1: El País - Diseño responsive de un diario digital

El diario El País fue uno de los primeros grandes medios españoles en adoptar un diseño completamente responsive. Su implementación es un caso de estudio notable porque resuelve el desafío de presentar gran densidad informativa en cualquier dispositivo:

- **En desktop** — el layout usa un grid de **3 columnas** con la noticia principal ocupando la columna central y las secundarias en laterales.
- **En tablet** — el grid se reduce a **2 columnas** y las noticias menos relevantes se mueven debajo del pliegue.
- **En móvil** — todas las noticias se apilan en una columna única con tipografía optimizada para lectura en pantalla pequeña.

Lo más destacable es su uso de `srcset` y `picture` para las imágenes de portada: en móvil sirven versiones recortadas verticalmente de las mismas fotos, mientras que en desktop usan versiones horizontales, demostrando **dirección artística responsive**. También implementan `loading="lazy"` en todas las imágenes fuera de la portada para optimizar el rendimiento en conexiones móviles. Su sistema de navegación usa un **off-canvas** en móvil con animación de deslizamiento y una **barra de navegación fija** en desktop con submenús desplegables.

### Caso 2: Starbucks - Mobile First en ecommerce

La web de Starbucks es un excelente ejemplo de Mobile First aplicado al comercio electrónico. La experiencia móvil es la prioridad, con botones de tamaño táctil generoso (>48dp), formularios de pedido simplificados, y un menú de navegación inferior (bottom navigation) que sigue las guías de usabilidad móvil. En desktop, la misma funcionalidad se expande con imágenes más grandes, layouts de múltiples columnas para el menú de productos, y efectos hover que no existen en móvil. Su sistema de diseño responsivo se basa en contenedores fluidos que usan `max-width` para limitar el ancho en pantallas grandes, evitando que las líneas de texto se vuelvan ilegibles. La página de producto usa una estrategia interesante: en móvil, la imagen del producto y la descripción se apilan verticalmente; en desktop, la imagen ocupa el 50% izquierdo con scroll de miniaturas y la información de producto el 50% derecho con posición sticky. Destaca su uso de `picture` para servir imágenes WebP a navegadores compatibles con fallback a JPEG, logrando reducir el peso de las imágenes en un 30-40%.

### Caso 3: GitHub - Dashboard responsive para desarrolladores

GitHub implementa uno de los diseños responsive más complejos que existen: un dashboard para desarrolladores con tablas de actividad, gráficos de contribución, feeds de eventos, y repositorios. Su estrategia responsive es magistral en varios aspectos:

- **Container queries** en componentes como las tarjetas de repositorio, que aparecen en diferentes contextos (barra lateral, lista principal, resultados de búsqueda) y se adaptan al ancho del contenedor.
- **Modo oscuro** que va más allá de invertir colores: ajustan el contraste, la saturación y los colores de sintaxis del código para garantizar legibilidad en ambos esquemas.
- **Tablas de issues y pull requests** con ocultación selectiva de columnas y colapso en cards, mostrando la información crítica (título, etiquetas, estado) en todos los tamaños pero ocultando metadatos menos relevantes en móvil.
- **Navegación principal** que se transforma completamente: en desktop, una barra superior completa con todos los enlaces; en tablet, una barra simplificada; en móvil, un menú hamburguesa off-canvas con agrupación por secciones.

Su uso de `prefers-reduced-motion` respeta la configuración del usuario eliminando animaciones superfluas como los efectos hover en tarjetas.

## Actividades guiadas

### Actividad Guiada 1: Convertir un diseño de escritorio a Mobile First

El alumnado recibirá un diseño CSS existente creado con enfoque Desktop First (que usa `max-width` en media queries). Deberá refactorizarlo a Mobile First: identificar los estilos base que corresponden a la versión móvil, moverlos fuera de las media queries, y cambiar todas las consultas de `max-width` a `min-width`. Se trabajará sobre un layout de dos columnas con sidebar. El resultado debe ser funcionalmente idéntico pero con mejor rendimiento en móvil. Se verificará usando Chrome DevTools en modo dispositivo móvil y Lighthouse para comprobar la mejora en las métricas de rendimiento.

### Actividad Guiada 2: Implementar un sistema de tipografía fluida

El alumnado creará un sistema de tipografía completamente fluido sin media queries. Deberá definir variables CSS para tamaños de fuente usando `clamp()` en todos los niveles tipográficos (h1-h6, body, small, caption). Se calcularán los valores mínimo (móvil 320px) y máximo (desktop 1200px) para cada nivel manteniendo una escala armónica (1.25 ratio). Se implementará longitud de línea óptima con `max-width: 65ch` en el contenido principal. Se probará el resultado en dispositivos desde 320px hasta 2560px verificando que el texto siempre es legible y las proporciones se mantienen.

### Actividad Guiada 3: Construir un menú de navegación responsive

El alumnado implementará tres versiones de menú responsive para comparar sus ventajas: (a) hamburguesa con checkbox hack CSS puro, (b) hamburguesa con JavaScript mínimo (añadiendo/quitar clases), (c) bottom navigation bar para móvil con los 4-5 enlaces principales en la parte inferior. Se analizarán las ventajas de cada enfoque: el CSS puro no requiere JavaScript pero tiene limitaciones de animación; el enfoque JS permite transiciones suaves y gestión de foco; la bottom navigation es más accesible en móvil (los pulgares alcanzan fácilmente los botones inferiores). Se documentarán las conclusiones.

### Actividad Guiada 4: Crear una galería de imágenes completamente responsive

El alumnado construirá una galería de imágenes responsive que sirva la imagen óptima según el dispositivo. Deberá generar (o simular) versiones de cada imagen en 3 resoluciones (400w, 800w, 1200w) y 2 formatos (WebP, JPEG). Implementará `srcset` con descriptores `w` y el atributo `sizes` para que el navegador seleccione la resolución adecuada. Usará `<picture>` para servir WebP con fallback a JPEG. Añadirá `loading="lazy"` para carga diferida y `decoding="async"` para no bloquear el renderizado. El layout de la galería usará CSS Grid con `repeat(auto-fill, minmax(250px, 1fr))` para adaptarse fluidamente.

### Actividad Guiada 5: Probar y depurar un sitio responsive

Usando Chrome DevTools, el alumnado aprenderá a probar sistemáticamente un sitio responsive. Se cubrirá: el modo dispositivo (device toolbar) para simular diferentes móviles y tablets, la barra de dimensiones responsivas para redimensionar libremente, la emulación de conexiones lentas (Network throttling: 3G, 4G), la emulación de sensores (touch, geolocalización), el panel de media queries que muestra todos los breakpoints definidos, y Lighthouse para auditoría de rendimiento y mejores prácticas responsive. Se generará un informe con problemas detectados y soluciones aplicadas.

## Actividades propuestas

### Actividad Propuesta 1: Rediseñar la web del instituto

Diseña y desarrolla una versión responsive completa del sitio web de tu instituto usando Mobile First. Debe incluir: página de inicio con noticias destacadas, página de oferta educativa con grid de ciclos formativos, página de contacto con formulario y mapa responsive, y galería de instalaciones. Implementa al menos 3 breakpoints con cambios significativos de layout usando Grid. Los formularios deben ser usables en móvil (campos de tamaño táctil, teclados apropiados). El mapa debe ser responsive (iframe de Google Maps con relación de aspecto mantenida). Entrega el proyecto completo con HTML y CSS comentados.

### Actividad Propuesta 2: Aplicación de clima responsive

Crea una aplicación de clima (puede usar datos estáticos de ejemplo) con diseño responsive. La interfaz debe mostrar: ubicación actual, temperatura, condiciones climáticas, previsión por horas (scroll horizontal en móvil), previsión semanal (grid de 7 días), y gráficos de temperatura/humedad. En móvil, la información debe mostrarse en tarjetas apiladas. En tablet, usar 2 columnas. En desktop, un layout completo con sidebar de ubicaciones guardadas. Implementa modo oscuro automático con `prefers-color-scheme`. Usa `clamp()` para todos los tamaños de texto y `minmax()` para los grids.

### Actividad Propuesta 3: Portafolio personal responsive

Diseña y desarrolla tu portafolio profesional como desarrollador web con enfoque Mobile First. Secciones: héroe con presentación y foto, proyectos con grid de tarjetas (cada tarjeta con imagen, título, tecnologías, enlace), habilidades con barras de progreso, experiencia laboral con timeline responsive, y formulario de contacto. El timeline debe ser vertical en móvil y alternar izquierda/derecha en desktop. Las tarjetas de proyectos deben usar container queries para adaptarse tanto en el grid principal como si se insertan en un sidebar. Implementa animaciones de entrada (fade-in al hacer scroll) que se desactiven con `prefers-reduced-motion`.

### Actividad Propuesta 4: Dashboard de analíticas responsive

Construye un panel de control con gráficos y estadísticas que funcione en cualquier dispositivo. El dashboard debe incluir: KPIs (4 tarjetas de métricas), gráfico de líneas (ventas), gráfico de barras (usuarios), tabla de últimos pedidos, y lista de actividad. En móvil, todo se muestra en 1 columna con las tarjetas KPI en 2 columnas pequeñas. En tablet, se usa un grid de 2 columnas. En desktop, un layout completo de 4 columnas con el gráfico principal ocupando 3 columnas. La tabla de pedidos debe usar la estrategia de cards en móvil. Los gráficos pueden ser simulados con CSS (barras de altura variable). Implementa las 3 estrategias de tablas responsive vistas en clase.

### Actividad Propuesta 5: Landing page para un evento

Crea la landing page de un evento tecnológico (conferencia, hackathon, meetup) con diseño responsive Mobile First. Secciones: cabecera con cuenta atrás, héroe con fecha y lugar, ponentes (grid de tarjetas con foto/avatar), agenda/horario (componente responsive que en móvil muestre las sesiones como acordeón y en desktop como tabla), patrocinadores (grid de logos), FAQ (acordeón), y formulario de inscripción. El formulario debe ser especialmente usable en móvil con validación visual. La cuenta atrás debe ser visible pero no invasiva en móvil. Implementa `fetchpriority="high"` en la imagen del héroe y `loading="lazy"` en el resto.

## Actividades de ampliación

### Actividad de Ampliación 1: Sistema de diseño responsive propio

Desarrolla un sistema de diseño (design system) responsive completo documentado. Define tokens de diseño para: colores (con variantes claro/oscuro), tipografía (escala completa con clamp()), espaciado (escala con clamp() basada en el viewport), breakpoints (con justificación por contenido), sombras (3 niveles), bordes redondeados (3 tamaños). Crea componentes reutilizables con container queries: botón (3 tamaños, 3 variantes), tarjeta (3 layouts según contenedor), campo de formulario, badge, alerta, modal. Documenta cada componente con su comportamiento responsive y casos de uso. Implementa una página de demostración que muestre todos los componentes en diferentes contextos (sidebar, contenido principal, modal). Entrega el CSS del sistema de diseño y la documentación.

### Actividad de Ampliación 2: Auditoría responsive de sitios reales

Selecciona 5 sitios web populares de diferentes categorías (ecommerce, medio de comunicación, red social, banco, administración pública) y realiza una auditoría completa de su diseño responsive. Para cada sitio, evalúa: rendimiento en móvil (Lighthouse), uso de media queries vs container queries, estrategia de imágenes responsive, comportamiento de tablas, accesibilidad del menú de navegación, tamaño de objetivos táctiles, uso de tipografía fluida, y adaptación a pantallas intermedias (prueba en 320px, 375px, 414px, 768px, 1024px, 1280px, 1440px, 1920px). Identifica al menos un problema en cada sitio y propón una solución con código CSS. Presenta los resultados en un informe con capturas de pantalla, métricas comparativas y recomendaciones.

### Actividad de Ampliación 3: Framework CSS responsive minimalista

Crea tu propio micro-framework CSS responsive (sin dependencias, < 10KB) que proporcione las utilidades esenciales para diseño responsive. El framework debe incluir: sistema de grid de 12 columnas con breakpoints responsivos (clases .col-sm-*, .col-md-*, .col-lg-*), utilidades de espaciado responsive (clases .p-*, .m-*, .gap-* con valores fluidos), sistema de tipografía con clamp(), utilidades de visibilidad responsive (.hide-mobile, .show-desktop, etc.), y un reset CSS moderno. Escribe documentación de uso y crea una página de ejemplo que demuestre cada funcionalidad. Compara el peso y funcionalidad de tu framework con Bootstrap y Tailwind, analizando si merece la pena usar un framework completo o uno minimalista para proyectos pequeños.

## Buenas prácticas

1. **Empieza siempre por Mobile First**: Escribe los estilos base para móvil y añade complejidad con `min-width`. Esto mejora el rendimiento en dispositivos con menos recursos y te obliga a priorizar el contenido esencial. Los estilos base deben funcionar en la pantalla más pequeña soportada (generalmente 320px).

2. **Elige breakpoints basados en el contenido, no en dispositivos**: Redimensiona tu diseño gradualmente y añade un breakpoint cuando el contenido "se rompa" visualmente. Esto produce layouts más robustos que los basados en tamaños de dispositivos concretos, ya que se adaptan a cualquier pantalla presente y futura.

3. **Usa unidades relativas y fluidas siempre que sea posible**: `rem` y `em` para tipografía y espaciado, `%` y `fr` para anchos, `vw`/`vh` para alturas de sección, y `clamp()` para valores que necesiten límites. Las unidades absolutas (`px`) solo para bordes, sombras y detalles decorativos mínimos.

4. **Implementa `clamp()` para tipografía y espaciado**: Elimina docenas de media queries de ajuste tipográfico con una sola línea. `font-size: clamp(1rem, 0.8rem + 0.5vw, 1.25rem)` produce texto legible en cualquier pantalla sin saltos bruscos.

5. **Aprovecha los layouts fluidos de Grid y Flexbox**: `repeat(auto-fit, minmax(280px, 1fr))` en Grid y `flex-wrap: wrap` en Flexbox crean layouts que se adaptan automáticamente. Reserva las media queries para cambios estructurales mayores que no puedan resolverse de forma fluida.

6. **Usa `srcset` y `sizes` en todas las imágenes de contenido**: No sirvas imágenes de 2000px a dispositivos de 375px. Proporciona 3-4 resoluciones y deja que el navegador elija. Complementa con `<picture>` para formatos modernos y dirección artística.

7. **Implementa `loading="lazy"` en imágenes fuera del viewport inicial**: Reduce drásticamente el tiempo de carga en móvil. Las imágenes del héroe deben cargarse inmediatamente (`fetchpriority="high"`); el resto, bajo demanda.

8. **Respeta las preferencias del usuario**: Implementa `prefers-reduced-motion`, `prefers-color-scheme` y `prefers-contrast`. Son características de accesibilidad que, además, demuestran profesionalidad y respeto por el usuario.

9. **Prueba en dispositivos reales, no solo en el simulador**: El modo responsive de Chrome DevTools es útil pero no reproduce las condiciones reales de renderizado, rendimiento y experiencia táctil. Prueba al menos en un iPhone y un Android reales.

10. **Mide el rendimiento con Lighthouse**: Establece métricas objetivo (Performance > 90, CLS < 0.1, LCP < 2.5s) y verifica en cada iteración. El rendimiento es parte integral del diseño responsive, especialmente en móvil con conexiones lentas.

## Errores frecuentes

1. **Olvidar la metaetiqueta viewport**: Sin `<meta name="viewport" content="width=device-width, initial-scale=1.0">`, los navegadores móviles renderizan la página a 980px y luego la reducen. El resultado es texto minúsculo y una experiencia horrible. Es el error más común entre principiantes y afortunadamente el más fácil de corregir.

2. **Usar `max-width` en lugar de `min-width` (Desktop First en vez de Mobile First)**: Con `max-width`, los estilos base cargan todo el CSS de escritorio en móvil (peor rendimiento) y requieren sobrescribir estilos (cascada más compleja). Con `min-width`, el móvil solo carga los estilos que necesita y se añaden mejoras progresivamente.

3. **Elegir breakpoints basados en dispositivos populares**: Definir breakpoints en 320px, 768px, 1024px "porque son los tamaños del iPhone y el iPad" es una mala práctica. Los dispositivos cambian constantemente; tu diseño debe adaptarse al contenido, no al dispositivo de moda.

4. **Imágenes excesivamente grandes en móvil**: Servir la misma imagen de 3000px de ancho tanto a desktop como a móvil. La imagen se ve igual pero el móvil descarga 5-10 veces más datos de los necesarios. Usa srcset siempre.

5. **Texto demasiado pequeño o demasiado grande por usar `vw` sin límites**: `font-size: 2vw` produce texto microscópico en móvil y gigante en pantallas 4K. Siempre usa `clamp()` o media queries para acotar los valores de viewport.

6. **No probar en pantallas intermedias**: Los diseños se prueban solo en 375px (iPhone) y 1440px (escritorio), pero no en 600px, 800px o 1100px. Los problemas suelen aparecer en estas dimensiones intermedias donde el diseño ni es "móvil" ni es "escritorio". Prueba redimensionando libremente.

7. **Ignorar el modo paisaje en móvil**: Muchos diseños responsive solo consideran el móvil en portrait (vertical). Cuando el usuario gira el dispositivo a landscape (horizontal), el diseño puede romperse. El media query `orientation: landscape` o simplemente probar con anchos > 600px en móvil es necesario.

8. **Tablas que desbordan el viewport sin estrategia responsive**: Simplemente dejar que la tabla sobresalga por la derecha sin scroll horizontal ni adaptación. Implementa al menos una de las 3 estrategias (scroll, cards, ocultar columnas) para cualquier tabla con más de 3 columnas.

9. **Abusar de `display: none` para ocultar contenido en móvil**: Ocultar contenido "no esencial" en móvil puede parecer una buena idea, pero si ese contenido es importante para el usuario, le estás dando una experiencia de segunda clase. Si el contenido es prescindible, ¿por qué está en desktop? Repiensa la jerarquía del contenido.

10. **No considerar el tamaño de los objetivos táctiles**: Botones, enlaces y campos de formulario demasiado pequeños para pulsar con el dedo. Las directrices de Apple recomiendan mínimo 44x44 puntos; Material Design, 48x48dp. Usa `min-height` y `min-width` o `padding` suficiente en elementos interactivos.

## Resumen

El diseño responsive es mucho más que añadir media queries a un CSS de escritorio. Es una filosofía de diseño completa que sitúa al usuario y su dispositivo en el centro del proceso. A lo largo de esta unidad hemos recorrido el camino desde los fundamentos (viewport, breakpoints, media queries) hasta las técnicas más modernas (container queries, tipografía fluida con clamp(), imágenes responsive con srcset/picture).

Los puntos clave que el alumnado debe interiorizar son: (1) Mobile First como metodología de desarrollo que mejora el rendimiento y la experiencia en el dispositivo más común; (2) la selección de breakpoints basada en el contenido, no en dispositivos; (3) el uso de técnicas fluidas (clamp, minmax, auto-fill, porcentajes) para minimizar la dependencia de media queries; (4) las imágenes responsive como parte integral del diseño, no como optimización opcional; y (5) el respeto a las preferencias del usuario mediante media queries como prefers-reduced-motion y prefers-color-scheme.

La tendencia del sector apunta hacia componentes cada vez más autónomos gracias a las Container Queries, que permiten a un componente adaptarse a su contexto sin conocer el tamaño del viewport. Esto, combinado con las técnicas fluidas de CSS moderno, está reduciendo progresivamente la necesidad de media queries tradicionales, aunque éstas seguirán siendo necesarias para cambios estructurales del layout general.

## Recursos complementarios

- **Responsive Web Design - Ethan Marcotte (A List Apart, 2010)**: El artículo original que acuñó el término. Lectura obligatoria para entender los fundamentos históricos y conceptuales.

- **MDN Web Docs - Responsive Design (https://developer.mozilla.org/es/docs/Learn/CSS/CSS_layout/Responsive_Design)**: Tutorial completo en español con ejemplos prácticos de todas las técnicas responsive.

- **web.dev - Responsive Web Design (https://web.dev/learn/design/)**: Curso gratuito de Google con lecciones interactivas sobre diseño responsive moderno, incluyendo container queries y patrones de layout.

- **Responsively App (https://responsively.app/)**: Aplicación gratuita para probar sitios responsive en múltiples viewports simultáneamente. Mucho más eficiente que redimensionar el navegador manualmente.

- **Can I Use (https://caniuse.com/)**: Datos de soporte para cada característica: media queries nivel 4, container queries, srcset, picture, WebP, AVIF, clamp(). Imprescindible para decidir qué técnicas usar.

- **The Complete Guide to CSS Media Queries - CSS-Tricks**: Guía de referencia con todas las características de media queries, incluyendo las modernas de preferencias de usuario y interacción.

- **Squoosh (https://squoosh.app/)**: Herramienta de Google para comprimir y convertir imágenes a formatos modernos (WebP, AVIF). Ideal para generar las múltiples versiones necesarias para imágenes responsive.

- **Lighthouse - Chrome DevTools**: Auditor de rendimiento y buenas prácticas integrado en Chrome. Evalúa el diseño responsive, el rendimiento en móvil, y sugiere mejoras concretas.

- **Libro "Responsive Web Design" de Ethan Marcotte (A Book Apart)**: La obra de referencia sobre diseño responsive, actualizada con técnicas modernas de CSS.

- **Polypane (https://polypane.app/)**: Navegador diseñado específicamente para desarrollo responsive. Muestra múltiples viewports simultáneamente con sincronización de interacciones.
