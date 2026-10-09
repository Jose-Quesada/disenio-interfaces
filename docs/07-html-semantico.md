---
icon: lucide/file-code
---

# Unidad 7: HTML Semántico, Accesibilidad y SEO

## Objetivos de aprendizaje

Al finalizar esta unidad, el alumnado será capaz de comprender y aplicar los principios del HTML semántico para construir páginas web accesibles, mantenibles y optimizadas para motores de búsqueda. Se espera que identifique la diferencia entre el uso de elementos genéricos (`<div>`, `<span>`) frente a etiquetas semánticas (`<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>`, `<footer>`). Comprenderá la jerarquía de encabezados (único `<h1>`, sin saltos de nivel). Aprenderá a construir formularios accesibles con `<label>` asociadas, `<fieldset>`/`<legend>`, tipos HTML5 (`email`, `tel`, `number`, `date`, `search`, `range`, `color`, `file`) y validación nativa (`required`, `pattern`, `min`/`max`). Desarrollará navegación semántica con `<nav>` y listas, skip links y `aria-current`. Construirá tablas accesibles con `<caption>`, `scope` y sistema `id`/`headers`. Se introducirá en SEO técnico (meta description, Open Graph, Twitter Cards, JSON-LD con Schema.org). Comprenderá WAI-ARIA como complemento de HTML nativo. Explorará HTML5 avanzado: `<template>`, `<slot>`, `<picture>`, `srcset`/`sizes`, `loading="lazy"`, `decoding="async"` y metadatos PWA.

## Relación con los Resultados de Aprendizaje

Esta unidad se alinea directamente con el RA1 del módulo 0615 ("planificar la creación de una interfaz web valorando y aplicando especificaciones de diseño"). El HTML semántico constituye la base estructural de cualquier interfaz y su correcta aplicación es necesaria para cumplir los criterios de evaluación asociados. Se vincula con el criterio "se han reconocido los elementos que componen una interfaz web". También guarda relación con el RA2 ("creación de interfaces web utilizando hojas de estilos y lenguajes de marcas"), pues un marcado semántico correcto facilita la aplicación de CSS y JavaScript. Los contenidos conectan transversalmente con el RA4 ("integración de contenido multimedia y elementos interactivos") y con el RA5 ("evaluación de la accesibilidad y usabilidad de la interfaz"), siendo la accesibilidad uno de los pilares fundamentales de la unidad.

## Conocimientos previos

El alumnado debe poseer una base sólida en HTML: sintaxis básica, diferencia entre bloque y línea, estructura mínima HTML5 con `DOCTYPE`, etiquetas comunes (`<p>`, `<h1>`-`<h6>`, `<ol>`, `<ul>`, `<li>`, `<a>`, `<img>` con `src`/`alt`/`href`). Debe comprender el anidamiento de etiquetas y la jerarquía del DOM. Se presupone conocimiento básico de formularios (`<form>`, `<input>`, `<button>`). Es recomendable un primer contacto con CSS (selectores básicos, color, tipografía) y con las DevTools del navegador para inspeccionar el DOM y validar accesibilidad.

## Contenidos

1. **HTML semántico: concepto, fundamentos y beneficios.** Definición. Separación estructura/presentación/comportamiento. Diferencias con `<div>`/`<span>`. Beneficios: accesibilidad (roles ARIA implícitos), SEO (mejor indexación), mantenibilidad. Evolución desde HTML4/XHTML a HTML5.

2. **Estructura semántica completa.** Elementos: `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>`, `<footer>`, `<address>`. Propósito y reglas de anidamiento. Roles ARIA implícitos. `<figure>`/`<figcaption>`, `<time>`, `<mark>`, `<details>`/`<summary>`, `<dialog>`.

3. **Jerarquía de encabezados (h1-h6).** Único `<h1>` por página. Prohibición de saltos de nivel. Relación con accesibilidad: lectores de pantalla generan esquemas navegables.

4. **Accesibilidad básica.** Atributo `lang`. `alt` en imágenes. ARIA básicos: `aria-label`, `aria-labelledby`, `aria-describedby`, `role`, `tabindex`. `<label>` con `for`/`id`. `<fieldset>`/`<legend>`. `<caption>`.

5. **Formularios accesibles.** Tipos de `<input>` HTML5. Validación: `required`, `pattern`, `min`/`max`. `<datalist>`, `<output>`, `<progress>`, `<meter>`. `autocomplete`, `inputmode`.

6. **Navegación semántica.** `<nav>` + `<ul>`/`<li>`. `aria-current="page"`. Skip links. Breadcrumbs. Múltiples `<nav>` con `aria-label`.

7. **Tablas accesibles.** `<caption>`, `<thead>`, `<tbody>`, `<tfoot>`. `scope="col"`/`"row"`. Sistema `id`/`headers`. `aria-describedby`.

8. **SEO técnico.** Meta `description`. Open Graph. Twitter Cards. JSON-LD con Schema.org. Microdatos HTML.

9. **WAI-ARIA básico.** Primera regla de ARIA. Roles landmark. Estados: `aria-expanded`, `aria-hidden`, `aria-selected`. `aria-live`.

10. **HTML5 avanzado.** `<template>`. Web Components con `<slot>`. `<picture>`, `srcset`, `sizes`. `loading="lazy"`, `decoding="async"`.

11. **Metadatos globales.** `DOCTYPE`, `lang`, `charset`, `viewport`, `theme-color`, manifiesto PWA.

## Desarrollo teórico

### 1. HTML semántico: fundamentos y beneficios

!!! info "Definición"
    El **HTML semántico** es la práctica de utilizar elementos HTML que transmiten el significado y la función del contenido, tanto para el navegador como para desarrolladores y tecnologías de asistencia. En lugar de envolver todo en `<div>` y `<span>` genéricos, emplea etiquetas como `<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>` y `<footer>`, que describen explícitamente el propósito de cada bloque. La transición desde HTML4 —donde la maquetación se basaba en `<div id="header">` o `<div class="nav">`— hacia HTML5 representó un salto cualitativo alineado con la visión de la **web semántica** de Tim Berners-Lee, donde los datos están estructurados para que las máquinas puedan interpretarlos de manera significativa.

Los beneficios se articulan en tres ejes:

- **Accesibilidad** — los elementos semánticos proporcionan roles ARIA implícitos que los lectores de pantalla reconocen automáticamente: `<nav>` se anuncia como "navegación", `<main>` como "contenido principal", `<aside>` como "contenido complementario". Sin esta semántica, los usuarios de lectores de pantalla se enfrentan a una masa indiferenciada de `<div>` sin pistas sobre la función de cada bloque.
- **SEO** — Google, Bing y otros buscadores analizan la estructura semántica para comprender la jerarquía y relevancia del contenido. Usar `<article>` para contenidos autónomos, `<section>` con encabezados, y respetar la jerarquía de `<h1>` a `<h6>` ayuda a los algoritmos a indexar correctamente. Los datos estructurados JSON-LD complementan esta semántica habilitando *rich snippets*.
- **Mantenibilidad** — un código semántico es más legible: `<footer>` comunica inmediatamente "pie de página", mientras que `<div class="site-footer">` requiere descifrar convenciones. La semántica clara reduce comentarios, facilita el CSS y agiliza refactorizaciones. Además, favorece la separación de competencias siguiendo el principio de mejora progresiva.

### 2. Elementos de estructura semántica

- **`<header>`** — grupo de ayudas introductorias o de navegación (logotipo, título, nav, búsqueda). No confundir con `<head>`. Puede ser hijo de `<body>` (cabecera global) o de `<article>`/`<section>` (cabecera de sección). No anidar dentro de otro `<header>`, `<footer>` o `<address>`. Rol ARIA implícito: `banner` (cuando es hijo de `<body>`) o `generic`.
- **`<nav>`** — sección con enlaces de navegación principales. Solo para bloques de navegación relevantes, no para cualquier grupo de enlaces. Una página puede tener múltiples `<nav>` (principal, breadcrumbs, footer). Distinguirlos con `aria-label`. Su contenido se estructura como `<ul>` con `<li>` y `<a>`, ya que la navegación es conceptualmente una lista.
- **`<main>`** — contenido dominante del `<body>`. Debe ser único (solo uno visible). No puede ser descendiente de `<article>`, `<aside>`, `<footer>`, `<header>` o `<nav>`. Rol implícito: `main`. Es el destino típico del *skip link*.
- **`<section>`** — agrupación temática con encabezado propio. Divide contenido en partes lógicas. Debe tener encabezado. No usar como contenedor de estilos (para eso está `<div>`). Diferencia con `<article>`: `<section>` forma parte de un todo; `<article>` es autocontenido.
- **`<article>`** — composición autocontenida, reutilizable de forma independiente (post, comentario, widget). Puede anidarse y tener su propio `<header>` y `<footer>`.
- **`<aside>`** — contenido complementario indirectamente relacionado (barras laterales, glosarios). Rol implícito: `complementary`.
- **`<footer>`** — pie de página del ancestro de seccionamiento más cercano. Contiene copyright, enlaces, contacto (`<address>`). Rol implícito: `contentinfo` (hijo de `<body>`).
- **`<address>`** — información de contacto del autor del documento o artículo más próximo. No para direcciones postales arbitrarias.
- **`<figure>` / `<figcaption>`** — contenido autónomo (imagen, diagrama, código) con leyenda. Los lectores de pantalla los asocian automáticamente.
- **`<time>`** — fecha, hora o duración, con `datetime` para versión legible por máquina.
- **`<mark>`** — texto resaltado por relevancia contextual (términos de búsqueda).
- **`<details>` / `<summary>`** — contenido desplegable nativo sin JavaScript. Ideal para FAQs y acordeones. Atributo `open` para desplegado por defecto.
- **`<dialog>`** — ventana modal nativa con `.showModal()` y `.show()`. Gestión automática del foco, cierre con Escape y *backdrop*.

!!! tip "¿`<article>` o `<section>`?"
    Prueba rápida: **¿tendría sentido en un feed RSS?** Si es así, usar `<article>`. Si el bloque solo tiene sentido dentro de un contexto mayor, usar `<section>`.

### 3. Jerarquía de encabezados

!!! tip "Jerarquía estricta de encabezados"
    Los encabezados HTML (`<h1>` a `<h6>`) establecen la estructura jerárquica del contenido. La regla principal: **un único `<h1>` por página**, describiendo el tema principal. Respaldado por **WCAG 2.4.6** y por recomendaciones de buscadores. El `<h1>` puede diferir del `<title>` (que aparece en la pestaña y SERP).

    **No saltar niveles**: después de `<h2>` no puede aparecer `<h4>` sin un `<h3>`. Los saltos rompen el esquema lógico y confunden a lectores de pantalla y algoritmos. Estructura anidada: `<h2>` = sección principal, `<h3>` = subsección, etc.

El nivel se elige por posición lógica, no por tamaño visual (eso es CSS). Los lectores de pantalla permiten navegar entre encabezados mostrando una lista jerárquica. Los encabezados deben ser descriptivos y no genéricos.

### 4. Accesibilidad básica en HTML

- **`lang`** — declarado en `<html>` (ej.: `<html lang="es">`), permite a lectores de pantalla seleccionar el motor de voz correcto. También en elementos concretos para cambios de idioma.
- **`alt` en imágenes** — descripción textual equivalente. Imágenes decorativas: `alt=""` (vacío, sin espacio). Imágenes complejas: `alt` breve complementado con `aria-describedby`.
- **`title`** — *tooltip* al pasar el ratón. No usar como único medio de información importante (no accesible por teclado, táctil ni lectores de pantalla).
- **ARIA básicos** — `aria-label` etiqueta elementos sin texto visible; `aria-labelledby` reutiliza texto de otro elemento; `aria-describedby` enlaza a descripciones adicionales.

!!! warning "Evita `tabindex` positivo"
    `tabindex="0"` incluye el elemento en el orden natural de tabulación; `tabindex="-1"` permite el foco programático (`.focus()`). Los valores positivos (**1, 2, 3...**) deben evitarse: crean un orden de navegación artificial que confunde y es difícil de mantener.

### 5. Formularios accesibles

!!! tip "Regla de oro: etiqueta asociada"
    Práctica fundamental: asociar `<label>` con su campo mediante `for`/`id`. Amplía el área de interacción y permite el anuncio correcto por parte de los lectores de pantalla.

- **Agrupación** — `<fieldset>` crea grupo semántico, `<legend>` proporciona título. Los lectores anuncian la leyenda antes de cada control.
- **Tipos HTML5** — `email` (teclado con @), `tel` (numérico), `number` (incremento), `date` (selector nativo), `search`, `range` (deslizante), `color` (selector nativo), `file`.
- **Validación nativa** — `required`, `pattern` (regex), `min`/`max`, `minlength`/`maxlength`. Complementar con mensajes personalizados vía `aria-describedby`.
- **Elementos avanzados** — `<datalist>` (autocompletado), `<output>` (resultado), `<progress>` (tarea en curso), `<meter>` (medida escalar).
- **Atributos UX** — `autocomplete` (sugerencias con tokens estándar: `"name"`, `"email"`, `"tel"`, `"postal-code"`) e `inputmode` para teclado virtual: `"numeric"`, `"tel"`, `"email"`, `"url"`, `"decimal"`.

### 6. Navegación semántica

Construcción: `<nav>` como contenedor + `<ul>`/`<li>` con `<a>`. Los lectores de pantalla anuncian: "Lista de 5 elementos: Enlace, Inicio...".

- **Múltiples `<nav>` etiquetados** — se distinguen con `aria-label`: "Navegación principal", "Navegación del pie de página", "Breadcrumb".
- **`aria-current="page"`** — en el enlace activo, informa al lector de pantalla de la ubicación actual.

!!! tip "Skip links"
    Enlaces ocultos visualmente (**nunca** con `display:none` ni `hidden`) que aparecen al recibir foco y saltan al contenido principal (`<main>`). CSS típico: `position:absolute; top:-100px;` y `:focus { top:0; }`. Técnica moderna: `transform: translateY(-100%)` → `translateY(0)`.

### 7. Tablas accesibles

!!! warning "Tablas solo para datos tabulares"
    Nunca se utilizan para maquetar. Estructura correcta: `<caption>` (anunciado primero por los lectores), `<thead>` (encabezados), `<tbody>` (datos) y `<tfoot>` (totales, colocarlo antes de `<tbody>` en el código para que los lectores lo procesen de forma anticipada).

- **`<th>` con `scope`** — `scope="col"` aplica a toda la columna; `scope="row"` a toda la fila. El lector anuncia: "Trimestre 1, Software, 45.200 €".
- **Tablas complejas** — sistema `id`/`headers`: cada `<th>` tiene `id` único; cada `<td>` tiene `headers` con los `id` de sus encabezados.
- **Descripción larga** — `aria-describedby` en `<table>` enlaza a un párrafo explicativo.

### 8. SEO técnico

- **Meta description** — resumen de **120-160 caracteres** mostrado en la SERP. No influye en el ranking pero sí en el **CTR**.
- **Open Graph** — `og:title`, `og:description`, `og:image` (mínimo **1200×630 px**), `og:url`, `og:type`. Para Facebook, LinkedIn y WhatsApp.
- **Twitter Cards** — `twitter:card` (`summary` o `summary_large_image`), `twitter:title`, `twitter:description`, `twitter:image`. Si no existen, Twitter usa Open Graph como *fallback*.

!!! info "JSON-LD"
    `<script type="application/ld+json">` en `<head>`, con el vocabulario **Schema.org** para Organization, Person, Article, Product, Recipe, Event, FAQ y BreadcrumbList. Permite *rich snippets*: estrellas, precios, FAQs desplegables y paneles de conocimiento. **Google recomienda JSON-LD sobre microdatos.**

### 9. WAI-ARIA básico

!!! tip "Primera regla de ARIA"
    **No usar ARIA si existe equivalente HTML nativo.** Preferir `<button>` a `<div role="button" tabindex="0">`. Recrear elementos nativos con ARIA causa la mayoría de problemas de accesibilidad.

- **Roles landmark** — `banner`, `navigation`, `main`, `complementary`, `contentinfo`, `search`, `form`. Muchos ya están implícitos en HTML5 (no duplicar).
- **Estados** — `aria-expanded` (expandido/colapsado), `aria-hidden` (oculto para asistencia), `aria-selected` (seleccionado), `aria-disabled` (deshabilitado).
- **Regiones vivas** — `aria-live="polite"` (no intrusivo, espera), `aria-live="assertive"` (urgente, interrumpe). `aria-atomic="true"` para anunciar la región completa.

### 10. HTML5 avanzado

- **`<template>`** — HTML inerte no renderizado. Se clona con `.content.cloneNode(true)` y se inserta con JS. Ideal para estructuras repetitivas.
- **Web Components + `<slot>`** — Shadow DOM encapsula estilos. `<slot name="...">` proyecta contenido desde el *light DOM*. Slots nombrados y por defecto.

!!! tip "Imágenes responsivas"
    `<picture>` con `<source media="..." srcset="...">` para *art direction* y formatos modernos (WebP/AVIF) con *fallback* JPEG. `srcset` con descriptores `w` + `sizes` para la selección automática. `loading="lazy"` y `decoding="async"` para rendimiento.

### 11. Metadatos y configuración global

- **`<!DOCTYPE html>`** — activa el modo estándar.
- **`<html lang="es">`** — obligatorio para la accesibilidad.
- **`<meta charset="UTF-8">`** — debe ir pronto en `<head>`.
- **Viewport** — `<meta name="viewport" content="width=device-width, initial-scale=1.0">` habilita el diseño responsivo. **No usar** `user-scalable=no`.
- **`<meta name="theme-color">`** — personaliza la barra del navegador.
- **`<link rel="manifest">`** — habilita PWA.

## Ejemplos guiados

### Ejemplo 1: Estructura semántica completa de una página de artículo de blog

!!! example "Contexto pedagógico"
    Este ejemplo presenta una página de artículo de blog construida con HTML plenamente semántico, incluyendo todos los elementos principales de seccionamiento, navegación correcta, jerarquía de encabezados óptima, metadatos SEO, Open Graph, Twitter Cards y datos estructurados JSON-LD. Se incluye un enlace de salto (*skip link*) funcional, navegación con `aria-current`, y estructura de contenidos con `<article>`, `<section>`, `<aside>`, `<figure>` y `<footer>`.

=== "HTML"

    ``` html
    <!DOCTYPE html>
    <html lang="es">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta name="description" content="Artículo sobre los principios fundamentales del HTML semántico, su importancia para la accesibilidad y el SEO.">
      <meta name="theme-color" content="#2563eb">
      <title>HTML Semántico: Guía Completa | Mi Blog de Desarrollo Web</title>

      <!-- Open Graph: metadatos para compartir en redes sociales -->
      <meta property="og:title" content="HTML Semántico: Guía Completa">
      <meta property="og:description" content="Aprende los fundamentos del HTML semántico, su impacto en accesibilidad, SEO y mantenibilidad.">
      <meta property="og:image" content="https://ejemplo.com/img/html-semantico.png">
      <meta property="og:url" content="https://ejemplo.com/articulos/html-semantico">
      <meta property="og:type" content="article">

      <!-- Twitter Cards: metadatos para Twitter/X -->
      <meta name="twitter:card" content="summary_large_image">
      <meta name="twitter:title" content="HTML Semántico: Guía Completa">
      <meta name="twitter:description" content="Fundamentos del HTML semántico para accesibilidad y SEO.">
      <meta name="twitter:image" content="https://ejemplo.com/img/html-semantico.png">

      <!-- Datos estructurados JSON-LD (Schema.org) para SEO -->
      <script type="application/ld+json">
      {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": "HTML Semántico: Guía Completa",
        "author": { "@type": "Person", "name": "María López García" },
        "datePublished": "2025-01-15",
        "image": "https://ejemplo.com/img/html-semantico.png",
        "publisher": { "@type": "Organization", "name": "Mi Blog de Desarrollo Web" }
      }
      </script>

      <link rel="stylesheet" href="./styles.css">
    </head>
    <body>
      <!-- ENLACE DE SALTO AL CONTENIDO PRINCIPAL (skip link).
           Es el primer elemento interactivo de la página.
           Permite a usuarios de teclado y lectores de pantalla
           saltar directamente al contenido principal sin tener
           que tabular por toda la navegación. -->
      <a href="#contenido-principal" class="skip-link" aria-label="Saltar al contenido principal">
        Saltar al contenido principal
      </a>

      <!-- CABECERA GLOBAL DEL SITIO -->
      <header>
        <!-- Logotipo con enlace a la página de inicio.
             aria-label proporciona el texto accesible del enlace. -->
        <a href="/" aria-label="Ir a la página de inicio de Mi Blog">
          <img src="https://dummyimage.com/200x200/ccc/000.png&text=logo.svg" alt="Logotipo de Mi Blog de Desarrollo Web" width="180" height="50">
        </a>

        <!-- NAVEGACIÓN PRINCIPAL: patrón nav + ul/li.
             Este es el patrón semántico correcto para menús.
             aria-label distingue esta navegación de otras en la página. -->
        <nav aria-label="Navegación principal">
          <ul>
            <li><a href="/">Inicio</a></li>
            <!-- aria-current="page" informa al lector de pantalla
                 que este enlace corresponde a la página actual. -->
            <li><a href="/articulos/" aria-current="page">Artículos</a></li>
            <li><a href="/tutoriales/">Tutoriales</a></li>
            <li><a href="/acerca-de/">Acerca de</a></li>
            <li><a href="/contacto/">Contacto</a></li>
          </ul>
        </nav>

        <!-- Formulario de búsqueda con role="search" para
             identificarlo como región de búsqueda accesible -->
        <form role="search" action="/buscar/" method="get">
          <label for="busqueda-header">Buscar en el sitio:</label>
          <input type="search" id="busqueda-header" name="q"
                 placeholder="Escribe tu búsqueda...">
          <button type="submit">Buscar</button>
        </form>
      </header>

      <!-- CONTENIDO PRINCIPAL: único en la página, destino del skip link -->
      <main id="contenido-principal">

        <!-- ARTÍCULO: contenido autocontenido e independiente.
             Tiene sentido por sí mismo y podría distribuirse aisladamente. -->
        <article>
          <!-- Cabecera del artículo con título y metadatos -->
          <header>
            <!-- ÚNICO h1 de la página: describe el tema principal del documento -->
            <h1>HTML Semántico: La Base de una Web Accesible y Bien Posicionada</h1>
            <p>
              Publicado el <time datetime="2025-01-15">15 de enero de 2025</time>
              por <a href="/autores/maria-lopez/" rel="author">María López García</a>
            </p>
            <!-- Categorías del artículo como lista semántica -->
            <ul aria-label="Categorías del artículo">
              <li><a href="/categorias/html/">HTML</a></li>
              <li><a href="/categorias/accesibilidad/">Accesibilidad</a></li>
              <li><a href="/categorias/seo/">SEO</a></li>
            </ul>
          </header>

          <!-- Cuerpo del artículo: sections con encabezados jerárquicos (h2, h3).
               Cada section tiene aria-labelledby que apunta a su encabezado.
               La jerarquía de encabezados es estricta: h1 → h2 → h3, sin saltos. -->
          <section aria-labelledby="introduccion">
            <h2 id="introduccion">Introducción al HTML Semántico</h2>
            <p>
              El HTML semántico es mucho más que una tendencia moderna: es una necesidad
              fundamental para construir webs que sean verdaderamente accesibles, mantenibles
              y eficaces en los motores de búsqueda. Consiste en utilizar los elementos HTML
              según su propósito original, en lugar de recurrir sistemáticamente a elementos
              genéricos como <code>&lt;div&gt;</code> y <code>&lt;span&gt;</code>.
            </p>
            <p>
              Cuando envolvemos el contenido en elementos con significado, proporcionamos
              información valiosa sobre la estructura y jerarquía a navegadores, motores de
              búsqueda y lectores de pantalla. La transición desde HTML4 hacia HTML5
              representó un salto cualitativo fundamental en el desarrollo web.
            </p>
          </section>

          <section aria-labelledby="beneficios">
            <h2 id="beneficios">Beneficios Clave del HTML Semántico</h2>

            <!-- Subsecciones con h3: jerarquía correcta, sin saltos -->
            <section aria-labelledby="beneficio-accesibilidad">
              <h3 id="beneficio-accesibilidad">Accesibilidad Mejorada</h3>
              <p>
                Los elementos semánticos como <code>&lt;nav&gt;</code> o
                <code>&lt;main&gt;</code> llevan roles ARIA implícitos que los
                lectores de pantalla reconocen automáticamente. Esto permite a
                personas con discapacidad visual navegar eficientemente entre
                regiones mediante atajos de teclado.
              </p>
            </section>

            <section aria-labelledby="beneficio-seo">
              <h3 id="beneficio-seo">Optimización para Motores de Búsqueda</h3>
              <p>
                Google y otros buscadores analizan la estructura semántica para
                comprender la relevancia del contenido. Un <code>&lt;article&gt;</code>
                bien estructurado con encabezados jerárquicos correctos tiene más
                probabilidades de aparecer en posiciones destacadas.
              </p>
            </section>

            <section aria-labelledby="beneficio-mantenibilidad">
              <h3 id="beneficio-mantenibilidad">Mantenibilidad del Código</h3>
              <p>
                Un código HTML semántico es más legible: cualquier desarrollador
                entiende inmediatamente que <code>&lt;footer&gt;</code> es el pie
                de página. La semántica clara reduce la deuda técnica y acelera
                el mantenimiento y la incorporación de nuevos miembros al equipo.
              </p>
            </section>
          </section>

          <!-- FIGURA SEMÁNTICA con imagen y pie de figura.
               <figure> envuelve contenido ilustrativo autónomo.
               <figcaption> proporciona la leyenda accesible. -->
          <figure>
            <img src="https://dummyimage.com/800x600/ccc/000.png&text=estructura-html5.png"
                 alt="Diagrama de una página web mostrando la disposición de header, nav, main, article, section, aside y footer, con cada región coloreada y etiquetada según el estándar HTML5"
                 width="800" height="500"
                 loading="lazy"
                 decoding="async">
            <figcaption>
              <strong>Figura 1:</strong> Estructura típica de una página HTML5 con
              elementos semánticos. Las regiones coloreadas representan cada uno
              de los elementos de seccionamiento del estándar actual.
            </figcaption>
          </figure>

          <section aria-labelledby="conclusiones">
            <h2 id="conclusiones">Conclusiones</h2>
            <p>
              La adopción del HTML semántico no es una opción, sino una responsabilidad
              profesional. Cada elemento que elegimos tiene impacto directo en la
              experiencia de personas con diversas capacidades, en la visibilidad de
              nuestro contenido en buscadores y en la calidad a largo plazo de nuestro
              código. Invertir en aprender y aplicar correctamente la semántica HTML
              es una de las decisiones más rentables como desarrolladores web.
            </p>
          </section>

          <!-- Pie del artículo con información del autor y navegación entre artículos -->
          <footer>
            <address>
              <img src="https://dummyimage.com/800x600/ccc/000.png&text=autora-maria.jpg" alt="Fotografía de María López García"
                   width="80" height="80" loading="lazy">
              <p>
                <strong>María López García</strong> es desarrolladora web senior y
                consultora de accesibilidad con más de 10 años de experiencia.
              </p>
              <p>Contacto: <a href="mailto:maria.lopez@ejemplo.com">maria.lopez@ejemplo.com</a></p>
            </address>

            <!-- Navegación entre artículos (anterior/siguiente) -->
            <nav aria-label="Navegación entre artículos">
              <ul>
                <li><a href="/articulos/css-grid/" rel="prev">&larr; CSS Grid</a></li>
                <li><a href="/articulos/javascript-accesible/" rel="next">JavaScript Accesible &rarr;</a></li>
              </ul>
            </nav>
          </footer>
        </article>

        <!-- BARRA LATERAL: contenido complementario relacionado -->
        <aside aria-labelledby="sidebar-titulo">
          <h2 id="sidebar-titulo">Contenido Relacionado</h2>
          <section aria-labelledby="articulos-relacionados">
            <h3 id="articulos-relacionados">Artículos Relacionados</h3>
            <ul>
              <li><a href="/articulos/aria-basico/">Introducción a WAI-ARIA</a></li>
              <li><a href="/articulos/formularios-accesibles/">Formularios Web Accesibles</a></li>
              <li><a href="/articulos/seo-tecnico/">SEO Técnico para Desarrolladores</a></li>
            </ul>
          </section>
          <section aria-labelledby="categorias-populares">
            <h3 id="categorias-populares">Categorías Populares</h3>
            <ul>
              <li><a href="/categorias/html/">HTML</a> (42 artículos)</li>
              <li><a href="/categorias/css/">CSS</a> (38 artículos)</li>
              <li><a href="/categorias/javascript/">JavaScript</a> (56 artículos)</li>
              <li><a href="/categorias/accesibilidad/">Accesibilidad</a> (27 artículos)</li>
            </ul>
          </section>
        </aside>
      </main>

      <!-- PIE DE PÁGINA GLOBAL DEL SITIO -->
      <footer role="contentinfo">
        <nav aria-label="Navegación del pie de página">
          <ul>
            <li><a href="/privacidad/">Política de Privacidad</a></li>
            <li><a href="/cookies/">Política de Cookies</a></li>
            <li><a href="/aviso-legal/">Aviso Legal</a></li>
          </ul>
        </nav>
        <p>&copy; 2025 Mi Blog de Desarrollo Web. Todos los derechos reservados.</p>
        <address>
          <p>Contacto: <a href="mailto:info@ejemplo.com">info@ejemplo.com</a></p>
        </address>
      </footer>
    </body>
    </html>
    ```

=== "CSS"

    ``` css
    /* Skip link: oculto hasta que recibe el foco del teclado.
       Usamos position:absolute y top negativo para ocultarlo visualmente,
       pero sigue siendo accesible para lectores de pantalla y teclado. */
    .skip-link {
      position: absolute;
      top: -100px;
      left: 0;
      background: #2563eb;
      color: #ffffff;
      padding: 12px 24px;
      z-index: 10000;
      text-decoration: none;
      font-weight: bold;
      border-radius: 0 0 4px 0;
      transition: top 0.2s ease;
    }
    /* Al recibir foco con Tab, el enlace aparece en la parte superior */
    .skip-link:focus {
      top: 0;
      outline: 3px solid #93c5fd;
      outline-offset: 2px;
    }
    ```

### Ejemplo 2: Formulario de registro accesible completo

!!! example "Contexto pedagógico"
    Formulario que demuestra buenas prácticas: etiquetas con `for`/`id`, agrupación con `fieldset`/`legend`, tipos HTML5 especializados, validación nativa, mensajes de error con `aria-describedby` y `role="alert"`, `datalist` para sugerencias, `output` para mostrar valores, `meter` para fortaleza de contraseña y atributos `autocomplete` e `inputmode`.

=== "HTML"

    ``` html
    <!DOCTYPE html>
    <html lang="es">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Formulario de Registro Accesible | Ejemplo Didáctico</title>
      <link rel="stylesheet" href="./styles.css">
    </head>
    <body>
      <main>
        <div class="formulario-contenedor">
          <h1>Crear Cuenta</h1>
          <p class="formulario-descripcion" id="form-descripcion">
            Completa los campos obligatorios (*) para registrarte.
            Tus datos serán tratados conforme a nuestra política de privacidad.
          </p>

          <!-- FORMULARIO ACCESIBLE: aria-describedby enlaza con la descripción -->
          <form action="/registro/" method="post" novalidate aria-describedby="form-descripcion">

            <!-- SECCIÓN 1: Datos Personales -->
            <fieldset>
              <legend>Datos Personales</legend>

              <!-- Campo: Nombre completo -->
              <div class="campo">
                <label for="nombre" class="campo-requerido">Nombre completo</label>
                <input type="text" id="nombre" name="nombre" required
                       minlength="3" maxlength="100" autocomplete="name"
                       placeholder="Ej: María García López"
                       aria-describedby="nombre-error" inputmode="text">
                <div class="mensaje-error" id="nombre-error" role="alert">
                  <span aria-hidden="true">&#9888;</span> El nombre debe tener entre 3 y 100 caracteres.
                </div>
              </div>

              <!-- Campo: Correo electrónico (type="email" con validación automática) -->
              <div class="campo">
                <label for="email" class="campo-requerido">Correo electrónico</label>
                <input type="email" id="email" name="email" required
                       autocomplete="email" placeholder="usuario@dominio.com"
                       aria-describedby="email-error" inputmode="email">
                <div class="mensaje-error" id="email-error" role="alert">
                  <span aria-hidden="true">&#9888;</span> Introduce un correo electrónico válido.
                </div>
              </div>

              <!-- Campo: Teléfono (opcional, type="tel" para teclado numérico) -->
              <div class="campo">
                <label for="telefono">Teléfono <span style="font-weight:400;color:#64748b;">(opcional)</span></label>
                <input type="tel" id="telefono" name="telefono" autocomplete="tel"
                       placeholder="+34 612 345 678"
                       pattern="[+]?[0-9\s()-]{7,15}"
                       aria-describedby="telefono-error" inputmode="tel">
                <div class="mensaje-error" id="telefono-error" role="alert">
                  <span aria-hidden="true">&#9888;</span> Introduce un número de teléfono válido (7-15 dígitos).
                </div>
              </div>

              <!-- Campo: Fecha de nacimiento (type="date" con selector nativo) -->
              <div class="campo">
                <label for="fecha-nacimiento" class="campo-requerido">Fecha de nacimiento</label>
                <input type="date" id="fecha-nacimiento" name="fecha_nacimiento" required
                       min="1900-01-01" max="2025-12-31"
                       autocomplete="bday" aria-describedby="fecha-error">
                <div class="mensaje-error" id="fecha-error" role="alert">
                  <span aria-hidden="true">&#9888;</span> Debes ser mayor de edad para registrarte.
                </div>
              </div>
            </fieldset>

            <!-- SECCIÓN 2: Datos de la Cuenta -->
            <fieldset>
              <legend>Datos de la Cuenta</legend>

              <!-- Campo: Nombre de usuario -->
              <div class="campo">
                <label for="usuario" class="campo-requerido">Nombre de usuario</label>
                <input type="text" id="usuario" name="usuario" required
                       minlength="4" maxlength="20" pattern="[a-zA-Z0-9_]+"
                       autocomplete="username" placeholder="Sin espacios"
                       aria-describedby="usuario-error">
                <div class="mensaje-error" id="usuario-error" role="alert">
                  <span aria-hidden="true">&#9888;</span> Solo letras, números y guiones bajos (4-20 caracteres).
                </div>
              </div>

              <!-- Campo: Contraseña con indicador de fortaleza (meter) -->
              <div class="campo">
                <label for="password" class="campo-requerido">Contraseña</label>
                <input type="password" id="password" name="password" required
                       minlength="8" maxlength="128" autocomplete="new-password"
                       aria-describedby="password-error password-requisitos"
                       placeholder="Mínimo 8 caracteres">
                <!-- METER: indicador gráfico de fortaleza de 0 a 100 -->
                <meter id="fortaleza-password" min="0" max="100"
                       low="33" high="66" optimum="80" value="0"
                       aria-label="Fortaleza de la contraseña: 0%"
                       style="width:100%;height:6px;border-radius:3px;margin-top:8px;background:#e2e8f0;">
                </meter>
                <div class="mensaje-error" id="password-error" role="alert">
                  <span aria-hidden="true">&#9888;</span> La contraseña debe tener al menos 8 caracteres.
                </div>
                <p id="password-requisitos" style="font-size:0.8rem;color:#64748b;margin-top:4px;">
                  Para mayor seguridad, incluye mayúsculas, minúsculas, números y caracteres especiales.
                </p>
              </div>

              <!-- Campo: País con datalist para sugerencias de autocompletado -->
              <div class="campo">
                <label for="pais" class="campo-requerido">País de residencia</label>
                <input type="text" id="pais" name="pais" list="lista-paises" required
                       autocomplete="country-name" placeholder="Escribe tu país..."
                       aria-describedby="pais-error" inputmode="text">
                <!-- DATALIST: lista de sugerencias vinculada al input mediante list="lista-paises" -->
                <datalist id="lista-paises">
                  <option value="España"><option value="México">
                  <option value="Argentina"><option value="Colombia">
                  <option value="Chile"><option value="Perú">
                  <option value="Venezuela"><option value="Ecuador">
                  <option value="Uruguay"><option value="Paraguay">
                  <option value="Bolivia"><option value="Costa Rica">
                  <option value="Panamá"><option value="Cuba">
                  <option value="República Dominicana"><option value="Guatemala">
                </datalist>
                <div class="mensaje-error" id="pais-error" role="alert">
                  <span aria-hidden="true">&#9888;</span> Selecciona o escribe tu país de residencia.
                </div>
              </div>

              <!-- Campo: Tamaño de fuente con range y output vinculados -->
              <div class="campo">
                <label for="tamano-fuente">Tamaño de fuente preferido</label>
                <div style="display:flex;align-items:center;gap:12px;">
                  <span aria-hidden="true" style="font-size:0.8rem;">A</span>
                  <input type="range" id="tamano-fuente" name="tamano_fuente"
                         min="12" max="24" value="16" step="1"
                         aria-label="Tamaño de fuente preferido en píxeles"
                         style="flex:1;">
                  <span aria-hidden="true" style="font-size:1.2rem;">A</span>
                  <!-- OUTPUT: vinculado al range con for, muestra el valor actual -->
                  <output for="tamano-fuente" id="valor-fuente"
                          style="font-weight:700;min-width:2.5rem;text-align:center;">16px</output>
                </div>
              </div>
            </fieldset>

            <!-- SECCIÓN 3: Preferencias -->
            <fieldset>
              <legend>Preferencias de Comunicación</legend>

              <!-- Radio buttons accesibles: role="radiogroup" + aria-labelledby -->
              <div class="campo">
                <p id="frecuencia-label" style="font-weight:600;margin-bottom:8px;color:#334155;">
                  Frecuencia de notificaciones:</p>
                <div role="radiogroup" aria-labelledby="frecuencia-label">
                  <label style="display:flex;align-items:center;gap:8px;margin-bottom:8px;font-weight:400;">
                    <input type="radio" name="frecuencia" value="diaria" checked> Diaria
                  </label>
                  <label style="display:flex;align-items:center;gap:8px;margin-bottom:8px;font-weight:400;">
                    <input type="radio" name="frecuencia" value="semanal"> Semanal
                  </label>
                  <label style="display:flex;align-items:center;gap:8px;margin-bottom:8px;font-weight:400;">
                    <input type="radio" name="frecuencia" value="mensual"> Mensual
                  </label>
                  <label style="display:flex;align-items:center;gap:8px;font-weight:400;">
                    <input type="radio" name="frecuencia" value="nunca"> No deseo notificaciones
                  </label>
                </div>
              </div>

              <!-- Campo: Color de tema con type="color" -->
              <div class="campo">
                <label for="color-tema">Color de tema preferido</label>
                <div style="display:flex;align-items:center;gap:12px;">
                  <input type="color" id="color-tema" name="color_tema" value="#2563eb"
                         aria-label="Selecciona tu color de tema preferido">
                  <span style="font-size:0.85rem;color:#64748b;">
                    Este color personalizará tu interfaz
                  </span>
                </div>
              </div>

              <!-- Checkbox de aceptación de términos (required) -->
              <div class="campo">
                <label style="display:flex;align-items:flex-start;gap:8px;font-weight:400;">
                  <input type="checkbox" name="terminos" required
                         aria-describedby="terminos-error" style="width:auto;margin-top:3px;">
                  <span>He leído y acepto los
                    <a href="/terminos/" target="_blank" rel="noopener">Términos y Condiciones</a>
                    y la <a href="/privacidad/" target="_blank" rel="noopener">Política de Privacidad</a>.
                  </span>
                </label>
                <div class="mensaje-error" id="terminos-error" role="alert" style="margin-left:26px;">
                  <span aria-hidden="true">&#9888;</span> Debes aceptar los términos para continuar.
                </div>
              </div>
            </fieldset>

            <button type="submit" class="boton-enviar">Crear Cuenta</button>
          </form>
        </div>
      </main>

      <script src="./script.js"></script>
    </body>
    </html>
    ```

=== "CSS"

    ``` css
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      background: #f5f7fa; color: #1a1a2e; line-height: 1.6;
      padding: 40px 20px; display: flex; justify-content: center;
    }
    .formulario-contenedor {
      background: #fff; border-radius: 12px;
      box-shadow: 0 4px 24px rgba(0,0,0,0.08);
      padding: 40px; max-width: 640px; width: 100%;
    }
    h1 { margin-bottom: 8px; color: #2563eb; font-size: 1.8rem; }
    .formulario-descripcion { margin-bottom: 32px; color: #64748b; font-size: 0.95rem; }
    fieldset {
      border: 1px solid #e2e8f0; border-radius: 8px;
      padding: 24px; margin-bottom: 24px;
    }
    legend { font-weight: 700; color: #1e293b; padding: 0 8px; font-size: 1.1rem; }
    .campo { margin-bottom: 20px; }
    .campo label { display: block; font-weight: 600; margin-bottom: 6px; color: #334155; font-size: 0.9rem; }
    .campo-requerido::after { content: " *"; color: #dc2626; font-weight: 700; }
    .campo input, .campo select, .campo textarea {
      width: 100%; padding: 10px 14px; border: 2px solid #e2e8f0;
      border-radius: 6px; font-size: 1rem; font-family: inherit;
      transition: border-color 0.2s, box-shadow 0.2s;
      background: #fafbfc; color: #1e293b;
    }
    .campo input:focus, .campo select:focus, .campo textarea:focus {
      outline: none; border-color: #2563eb;
      box-shadow: 0 0 0 3px rgba(37,99,235,0.15); background: #fff;
    }
    .campo input:invalid:not(:placeholder-shown) { border-color: #dc2626; }
    .campo input:valid:not(:placeholder-shown) { border-color: #16a34a; }
    .mensaje-error {
      color: #dc2626; font-size: 0.825rem; margin-top: 4px;
      display: none; align-items: center; gap: 4px;
    }
    /* Mostrar mensaje de error cuando el campo es inválido y ha sido tocado */
    .campo input:invalid:not(:placeholder-shown) + .mensaje-error { display: flex; }
    .boton-enviar {
      width: 100%; padding: 14px 24px; background: #2563eb;
      color: #fff; border: none; border-radius: 8px;
      font-size: 1.1rem; font-weight: 700; cursor: pointer;
      transition: background 0.2s, transform 0.1s;
    }
    .boton-enviar:hover { background: #1d4ed8; }
    .boton-enviar:active { transform: scale(0.98); }
    .boton-enviar:focus-visible { outline: 3px solid #93c5fd; outline-offset: 2px; }
    @media (max-width: 480px) { .formulario-contenedor { padding: 24px 16px; } }
    ```

=== "JS"

    ``` js
    /* SCRIPT DE INTERACTIVIDAD: range↔output y fortaleza de contraseña */

    // 1. Sincronizar range con output
    const inputRange = document.getElementById('tamano-fuente');
    const outputRange = document.getElementById('valor-fuente');
    if (inputRange && outputRange) {
      inputRange.addEventListener('input', function() {
        outputRange.textContent = this.value + 'px';
      });
    }

    // 2. Calcular fortaleza de contraseña en tiempo real usando meter
    const passwordInput = document.getElementById('password');
    const fortalezaMeter = document.getElementById('fortaleza-password');
    if (passwordInput && fortalezaMeter) {
      passwordInput.addEventListener('input', function() {
        const valor = this.value;
        let puntuacion = 0;
        if (valor.length >= 8) puntuacion += 25;
        if (/[A-Z]/.test(valor)) puntuacion += 25;
        if (/[0-9]/.test(valor)) puntuacion += 25;
        if (/[^A-Za-z0-9]/.test(valor)) puntuacion += 25;
        fortalezaMeter.value = puntuacion;
        let etiqueta = puntuacion >= 75 ? 'Fuerte' : puntuacion >= 50 ? 'Moderada' : 'Débil';
        fortalezaMeter.setAttribute('aria-label',
          'Fortaleza de la contraseña: ' + puntuacion + '%, ' + etiqueta);
      });
    }

    // 3. Prevenir envío real (demo didáctica)
    document.querySelector('form').addEventListener('submit', function(e) {
      e.preventDefault();
      alert(this.checkValidity()
        ? '¡Formulario válido! En producción se enviaría al servidor.'
        : 'Corrige los errores indicados en rojo antes de enviar.');
    });
    ```

### Ejemplo 3: Tabla de datos accesible con scope y caption

=== "HTML"

    ``` html
    <!DOCTYPE html>
    <html lang="es">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Tabla de Datos Accesible | Ejemplo Didáctico</title>
      <link rel="stylesheet" href="./styles.css">
    </head>
    <body>
      <main>
        <div class="contenedor-tabla">
          <h1>Informe de Ventas - Ejercicio 2025</h1>
          <p id="descripcion-tabla" style="margin-bottom:16px;color:#64748b;">
            Desglose de ventas (en euros) por trimestre y categoría durante el
            ejercicio fiscal 2025. La columna "Total Anual" suma los cuatro trimestres
            y la fila "Total General" suma todas las categorías por trimestre.
          </p>
          <div class="tabla-scroll" role="region" aria-labelledby="titulo-tabla" tabindex="0">
            <table aria-describedby="descripcion-tabla">
              <caption id="titulo-tabla">
                Ventas por Trimestre y Categoría de Producto - 2025 (€)
              </caption>
              <thead>
                <tr>
                  <th scope="col">Categoría</th>
                  <th scope="col" class="numero">T1 (Ene-Mar)</th>
                  <th scope="col" class="numero">T2 (Abr-Jun)</th>
                  <th scope="col" class="numero">T3 (Jul-Sep)</th>
                  <th scope="col" class="numero">T4 (Oct-Dic)</th>
                  <th scope="col" class="numero">Total Anual</th>
                </tr>
              </thead>
              <!-- tfoot se coloca ANTES de tbody para que los lectores de pantalla
                   procesen el resumen antes de los datos detallados -->
              <tfoot>
                <tr>
                  <th scope="row">Total General</th>
                  <td class="numero"><strong>186.800 €</strong></td>
                  <td class="numero"><strong>206.500 €</strong></td>
                  <td class="numero"><strong>182.600 €</strong></td>
                  <td class="numero"><strong>237.800 €</strong></td>
                  <td class="numero"><strong>813.700 €</strong></td>
                </tr>
              </tfoot>
              <tbody>
                <tr>
                  <th scope="row">Software</th>
                  <td class="numero">45.200 €</td>
                  <td class="numero">52.800 €</td>
                  <td class="numero">48.100 €</td>
                  <td class="numero">61.300 €</td>
                  <td class="numero"><strong>207.400 €</strong></td>
                </tr>
                <tr>
                  <th scope="row">Hardware</th>
                  <td class="numero">78.500 €</td>
                  <td class="numero">82.100 €</td>
                  <td class="numero">75.600 €</td>
                  <td class="numero">95.200 €</td>
                  <td class="numero"><strong>331.400 €</strong></td>
                </tr>
                <tr>
                  <th scope="row">Consultoría</th>
                  <td class="numero">32.000 €</td>
                  <td class="numero">35.500 €</td>
                  <td class="numero">28.900 €</td>
                  <td class="numero">40.100 €</td>
                  <td class="numero"><strong>136.500 €</strong></td>
                </tr>
                <tr>
                  <th scope="row">Soporte Técnico</th>
                  <td class="numero">18.700 €</td>
                  <td class="numero">20.400 €</td>
                  <td class="numero">19.800 €</td>
                  <td class="numero">22.300 €</td>
                  <td class="numero"><strong>81.200 €</strong></td>
                </tr>
                <tr>
                  <th scope="row">Formación</th>
                  <td class="numero">12.400 €</td>
                  <td class="numero">15.700 €</td>
                  <td class="numero">10.200 €</td>
                  <td class="numero">18.900 €</td>
                  <td class="numero"><strong>57.200 €</strong></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </main>
    </body>
    </html>
    ```

=== "CSS"

    ``` css
    body { font-family: 'Segoe UI', system-ui, sans-serif; background: #f8fafc; padding: 40px 20px; color: #1e293b; }
    .contenedor-tabla {
      max-width: 900px; margin: 0 auto; background: #fff; border-radius: 12px;
      box-shadow: 0 2px 16px rgba(0,0,0,0.06); padding: 32px; overflow-x: auto;
    }
    h1 { color: #2563eb; margin-bottom: 24px; font-size: 1.6rem; }
    .tabla-scroll { overflow-x: auto; -webkit-overflow-scrolling: touch; }
    table { width: 100%; border-collapse: collapse; font-size: 0.95rem; min-width: 600px; }
    caption {
      caption-side: top; text-align: left; font-weight: 700;
      font-size: 1.1rem; padding: 12px 0; color: #1e293b;
    }
    thead th { background: #2563eb; color: #fff; padding: 12px 16px; text-align: left; font-weight: 600; white-space: nowrap; }
    tbody td { padding: 12px 16px; border-bottom: 1px solid #e2e8f0; }
    tbody tr:nth-child(even) { background: #f8fafc; }
    tbody tr:hover { background: #eff6ff; }
    td.numero { text-align: right; font-variant-numeric: tabular-nums; }
    tfoot td { padding: 14px 16px; font-weight: 700; background: #f1f5f9; border-top: 2px solid #2563eb; }
    @media (max-width: 600px) {
      .contenedor-tabla { padding: 16px; }
      table { font-size: 0.85rem; }
      thead th, tbody td, tfoot td { padding: 8px 10px; }
    }
    ```

### Ejemplo 4: Navegación con skip link, aria-current y breadcrumbs

=== "HTML"

    ``` html
    <!DOCTYPE html>
    <html lang="es">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Navegación Semántica con Skip Link | Ejemplo Didáctico</title>
      <link rel="stylesheet" href="./styles.css">
    </head>
    <body>
      <!-- SKIP LINK: primer elemento interactivo -->
      <a href="#contenido-principal" class="skip-link" aria-label="Saltar al contenido principal">
        Saltar al contenido principal
      </a>

      <header class="site-header">
        <a href="/" class="site-logo" aria-label="Ir a la página de inicio">TechAcademy</a>
        <nav class="nav-principal" aria-label="Navegación principal">
          <ul>
            <li><a href="/">Inicio</a></li>
            <li><a href="/cursos/" aria-current="page">Cursos</a></li>
            <li><a href="/tutoriales/">Tutoriales</a></li>
            <li><a href="/blog/">Blog</a></li>
            <li><a href="/contacto/">Contacto</a></li>
          </ul>
        </nav>
      </header>

      <main id="contenido-principal">
        <!-- BREADCRUMB semántico con lista ordenada y aria-label -->
        <nav class="breadcrumb" aria-label="Breadcrumb">
          <ol>
            <li><a href="/">Inicio</a></li>
            <li><a href="/cursos/">Cursos</a></li>
            <li><span aria-current="page">Desarrollo Web Frontend</span></li>
          </ol>
        </nav>

        <h1>Curso de Desarrollo Web Frontend</h1>
        <p>Curso intensivo de 300 horas para dominar HTML5 semántico, CSS3 avanzado, JavaScript moderno y frameworks como React y Vue.js.</p>
        <h2>Contenidos del Curso</h2>
        <p>Desde fundamentos de HTML semántico hasta técnicas avanzadas de animación CSS y manipulación del DOM con JavaScript vanilla.</p>
        <h2>Metodología</h2>
        <p>Aprendizaje práctico (learning by doing) con ejercicios guiados, proyectos incrementales y casos de estudio reales.</p>
        <h2>Requisitos Previos</h2>
        <p>No se requieren conocimientos previos de programación; solo manejo básico del ordenador.</p>
      </main>

      <footer class="site-footer" role="contentinfo">
        <p>&copy; 2025 TechAcademy. | <a href="/privacidad/">Privacidad</a> | <a href="/terminos/">Términos</a></p>
      </footer>
    </body>
    </html>
    ```

=== "CSS"

    ``` css
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: 'Segoe UI', system-ui, sans-serif; line-height: 1.6; color: #1e293b; }
    /* SKIP LINK: oculto hasta recibir foco con Tab */
    .skip-link {
      position: absolute; top: -100px; left: 0;
      background: #2563eb; color: #fff; padding: 12px 24px;
      z-index: 10000; text-decoration: none; font-weight: 700;
      transition: top 0.2s ease; border-radius: 0 0 6px 0;
    }
    .skip-link:focus { top: 0; outline: 3px solid #93c5fd; outline-offset: 2px; }
    /* HEADER */
    .site-header {
      background: #0f172a; color: #fff; padding: 0 24px;
      display: flex; align-items: center; justify-content: space-between;
      flex-wrap: wrap; min-height: 64px;
    }
    .site-logo { font-size: 1.4rem; font-weight: 700; text-decoration: none; color: #fff; padding: 16px 0; }
    .site-logo:hover { color: #93c5fd; }
    /* NAVEGACIÓN */
    .nav-principal ul { list-style: none; display: flex; gap: 4px; flex-wrap: wrap; }
    .nav-principal a {
      color: #cbd5e1; text-decoration: none; padding: 8px 16px;
      border-radius: 6px; display: block; font-weight: 500; font-size: 0.95rem;
      transition: background 0.2s, color 0.2s;
    }
    .nav-principal a:hover { background: rgba(255,255,255,0.1); color: #fff; }
    .nav-principal a:focus-visible { outline: 2px solid #93c5fd; outline-offset: 2px; }
    .nav-principal a[aria-current="page"] { background: #2563eb; color: #fff; }
    /* CONTENIDO PRINCIPAL */
    main { max-width: 800px; margin: 0 auto; padding: 40px 24px; }
    main h1 { color: #2563eb; margin-bottom: 16px; font-size: 2rem; }
    main h2 { color: #334155; margin-top: 32px; margin-bottom: 12px; }
    main p { margin-bottom: 16px; color: #475569; }
    /* BREADCRUMB */
    .breadcrumb { margin-bottom: 24px; }
    .breadcrumb ol { list-style: none; display: flex; gap: 8px; align-items: center; padding: 0; flex-wrap: wrap; }
    .breadcrumb li { display: flex; align-items: center; gap: 8px; font-size: 0.9rem; }
    .breadcrumb li + li::before { content: "\203A"; color: #94a3b8; font-weight: 700; }
    .breadcrumb a { color: #2563eb; text-decoration: none; }
    .breadcrumb a:hover { text-decoration: underline; }
    .breadcrumb li:last-child { color: #64748b; font-weight: 500; }
    /* FOOTER */
    .site-footer { background: #0f172a; color: #94a3b8; text-align: center; padding: 24px; font-size: 0.9rem; }
    .site-footer a { color: #93c5fd; text-decoration: none; }
    .site-footer a:hover { text-decoration: underline; }
    @media (max-width: 600px) {
      .site-header { flex-direction: column; align-items: flex-start; padding: 12px 16px; }
      .nav-principal ul { flex-direction: column; width: 100%; }
    }
    ```

### Ejemplo 5: FAQ accesible con details/summary (contenido desplegable nativo)

=== "HTML"

    ``` html
    <!DOCTYPE html>
    <html lang="es">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>FAQ Accesible con details/summary | Ejemplo Didáctico</title>
      <link rel="stylesheet" href="./styles.css">
    </head>
    <body>
      <main>
        <div class="faq-contenedor">
          <h1>Preguntas Frecuentes</h1>
          <p class="faq-subtitulo">Haz clic en cada pregunta para desplegar la respuesta.</p>

          <details>
            <summary>¿Qué es el HTML semántico y por qué es importante?</summary>
            <div class="faq-contenido">
              <p>El HTML semántico utiliza elementos según su significado y propósito original. Mejora la accesibilidad para lectores de pantalla, facilita el SEO y hace el código más mantenible y comprensible para otros desarrolladores.</p>
            </div>
          </details>

          <details>
            <summary>¿Cuál es la diferencia entre section y article?</summary>
            <div class="faq-contenido">
              <p><code>&lt;section&gt;</code> agrupa contenido temáticamente y forma parte de un todo mayor (requiere encabezado). <code>&lt;article&gt;</code> es autocontenido y tiene sentido por sí mismo; podría distribuirse de forma independiente (ej: en un feed RSS).</p>
            </div>
          </details>

          <details>
            <summary>¿Cómo hacer que un formulario sea accesible?</summary>
            <div class="faq-contenido">
              <ul>
                <li>Asociar <code>&lt;label&gt;</code> al campo con <code>for</code>/<code>id</code>.</li>
                <li>Agrupar campos con <code>&lt;fieldset&gt;</code> y <code>&lt;legend&gt;</code>.</li>
                <li>Usar tipos de input HTML5 (<code>email</code>, <code>tel</code>, <code>date</code>).</li>
                <li>Mensajes de error con <code>aria-describedby</code> y <code>role="alert"</code>.</li>
                <li>Garantizar navegación completa con teclado y foco visible.</li>
              </ul>
            </div>
          </details>

          <details>
            <summary>¿Qué son los roles ARIA y cuándo usarlos?</summary>
            <div class="faq-contenido">
              <p>Los roles ARIA definen la función de un elemento para tecnologías de asistencia. <strong>Regla de oro:</strong> usa el elemento HTML nativo siempre que exista. Prefiere <code>&lt;button&gt;</code> a <code>&lt;div role="button"&gt;</code>. ARIA complementa HTML, no lo sustituye.</p>
            </div>
          </details>

          <details>
            <summary>¿Cómo funcionan los datos estructurados JSON-LD para SEO?</summary>
            <div class="faq-contenido">
              <p>Se insertan con <code>&lt;script type="application/ld+json"&gt;</code> en el <code>&lt;head&gt;</code>. Usan Schema.org para describir el contenido a buscadores, que generan rich snippets: estrellas, precios, FAQs desplegables, paneles de conocimiento. Es el formato recomendado por Google.</p>
            </div>
          </details>
        </div>
      </main>
    </body>
    </html>
    ```

=== "CSS"

    ``` css
    body { font-family: 'Segoe UI', system-ui, sans-serif; background: #f1f5f9; padding: 40px 20px; color: #1e293b; line-height: 1.7; }
    .faq-contenedor { max-width: 720px; margin: 0 auto; }
    h1 { text-align: center; color: #2563eb; margin-bottom: 8px; font-size: 2rem; }
    .faq-subtitulo { text-align: center; color: #64748b; margin-bottom: 40px; }
    /* Cada FAQ es un elemento details */
    details {
      background: #fff; border: 1px solid #e2e8f0; border-radius: 8px;
      margin-bottom: 12px; overflow: hidden; transition: box-shadow 0.2s, border-color 0.2s;
    }
    details:hover { box-shadow: 0 2px 8px rgba(0,0,0,0.06); }
    /* Summary: cabecera clickable del acordeón */
    summary {
      padding: 18px 24px; font-weight: 700; font-size: 1.05rem; cursor: pointer;
      list-style: none; display: flex; align-items: center; justify-content: space-between;
      color: #1e293b; user-select: none;
    }
    summary::-webkit-details-marker { display: none; }
    /* Icono personalizado con pseudoelemento ::after */
    summary::after {
      content: "+"; font-size: 1.5rem; font-weight: 400; color: #2563eb;
      transition: transform 0.3s ease; width: 24px; text-align: center;
    }
    details[open] summary::after { transform: rotate(45deg); }
    .faq-contenido { padding: 0 24px 20px 24px; color: #475569; font-size: 0.95rem; }
    summary:focus-visible { outline: 3px solid #2563eb; outline-offset: -3px; border-radius: 8px; }
    details[open] { border-color: #2563eb; }
    details[open] summary { color: #2563eb; }
    code { background: #f1f5f9; padding: 2px 6px; border-radius: 4px; font-size: 0.9em; color: #e11d48; }
    ```

### Ejemplo 6: Imágenes responsivas con picture, srcset, lazy loading y decoding async

=== "HTML"

    ``` html
    <!DOCTYPE html>
    <html lang="es">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Imágenes Responsivas | Ejemplo Didáctico</title>
      <link rel="stylesheet" href="./styles.css">
    </head>
    <body>
      <main>
        <h1>Técnicas de Imágenes Responsivas en HTML5</h1>
        <p class="intro">Sirve imágenes optimizadas para cada dispositivo con atributos nativos de HTML5, sin depender de JavaScript ni librerías externas.</p>

        <section class="ejemplo" aria-labelledby="ej1">
          <h2 id="ej1">1. srcset con descriptores de densidad (1x, 2x, 3x)</h2>
          <p>El navegador elige automáticamente la imagen con la densidad de píxeles adecuada. Una pantalla Retina (2x) cargará la versión de mayor resolución.</p>
          <pre>&lt;img src="https://dummyimage.com/800x600/ccc/000.png&text=foto-1x.jpg"
         srcset="https://dummyimage.com/800x600/ccc/000.png&text=foto-1x.jpg 1x, https://dummyimage.com/800x600/ccc/000.png&text=foto-2x.jpg 2x, https://dummyimage.com/800x600/ccc/000.png&text=foto-3x.jpg 3x"
         alt="Paisaje montañoso al atardecer"
         width="800" height="400"&gt;</pre>
          <div class="img-placeholder">srcset 1x, 2x, 3x</div>
        </section>

        <section class="ejemplo" aria-labelledby="ej2">
          <h2 id="ej2">2. srcset con descriptores de ancho (w) + sizes</h2>
          <p>Los descriptores <code>w</code> indican el ancho intrínseco. El atributo <code>sizes</code> informa al navegador del espacio que ocupará la imagen en el layout para que elija la óptima antes de cargar el CSS.</p>
          <pre>&lt;img src="https://dummyimage.com/800x600/ccc/000.png&text=paisaje-800.jpg"
         srcset="https://dummyimage.com/400x300/ccc/000.png&text=paisaje-400.jpg 400w, https://dummyimage.com/800x600/ccc/000.png&text=paisaje-800.jpg 800w, https://dummyimage.com/1200x400/ccc/000.png&text=paisaje-1200.jpg 1200w, https://dummyimage.com/800x600/ccc/000.png&text=paisaje-1600.jpg 1600w"
         sizes="(max-width: 600px) 100vw, (max-width: 1200px) 50vw, 800px"
         alt="Vista panorámica de la ciudad"
         width="800" height="450"&gt;</pre>
          <div class="img-placeholder" style="background:linear-gradient(135deg,#f093fb 0%,#f5576c 100%);">srcset w + sizes</div>
        </section>

        <section class="ejemplo" aria-labelledby="ej3">
          <h2 id="ej3">3. Elemento picture para dirección de arte (Art Direction)</h2>
          <p>Define diferentes imágenes según condiciones como el ancho de la ventana. Aquí se muestra un recorte vertical en móvil y panorámico en escritorio.</p>
          <pre>&lt;picture&gt;
      &lt;source srcset="https://dummyimage.com/800x600/ccc/000.png&text=hero-mobile.jpg" media="(max-width: 600px)"&gt;
      &lt;source srcset="https://dummyimage.com/800x600/ccc/000.png&text=hero-desktop.jpg" media="(min-width: 601px)"&gt;
      &lt;img src="https://dummyimage.com/800x600/ccc/000.png&text=hero-desktop.jpg"
           alt="Equipo de desarrollo colaborando en la oficina"
           width="1200" height="600"&gt;
    &lt;/picture&gt;</pre>
          <div class="img-placeholder" style="background:linear-gradient(135deg,#89f7fe 0%,#66a6ff 100%);">picture art direction</div>
        </section>

        <section class="ejemplo" aria-labelledby="ej4">
          <h2 id="ej4">4. Formatos modernos con fallback (AVIF → WebP → JPEG)</h2>
          <p>WebP y AVIF ofrecen mejor compresión. Con <code>&lt;picture&gt;</code> servimos el mejor formato soportado por el navegador y un fallback JPEG universal.</p>
          <pre>&lt;picture&gt;
      &lt;source srcset="https://dummyimage.com/800x600/ccc/000.png&text=producto.avif" type="image/avif"&gt;
      &lt;source srcset="https://dummyimage.com/800x600/ccc/000.png&text=producto.webp" type="image/webp"&gt;
      &lt;img src="https://dummyimage.com/800x600/ccc/000.png&text=producto.jpg"
           alt="Zapatillas deportivas azules, vista lateral"
           width="600" height="600"
           loading="lazy"
           decoding="async"&gt;
    &lt;/picture&gt;</pre>
          <div class="img-placeholder" style="background:linear-gradient(135deg,#ffeaa7 0%,#fdcb6e 100%);">AVIF → WebP → JPEG</div>
        </section>

        <section class="ejemplo" aria-labelledby="ej5">
          <h2 id="ej5">5. Figura semántica completa con figcaption</h2>
          <figure>
            <div class="img-placeholder" style="min-height:250px;background:linear-gradient(135deg,#a29bfe 0%,#6c5ce7 100%);">
              Arquitectura de Tres Capas<br>
              <small>Frontend ↔ API REST ↔ Backend ↔ Base de Datos</small>
            </div>
            <figcaption><strong>Figura 1:</strong> Diagrama de la arquitectura de la aplicación. El frontend se comunica con el backend mediante API REST, y este persiste datos en PostgreSQL.</figcaption>
          </figure>
        </section>
      </main>
    </body>
    </html>
    ```

=== "CSS"

    ``` css
    body { font-family: 'Segoe UI', system-ui, sans-serif; max-width: 960px; margin: 0 auto; padding: 40px 20px; color: #1e293b; line-height: 1.7; background: #f8fafc; }
    h1 { color: #2563eb; margin-bottom: 8px; }
    .intro { color: #64748b; margin-bottom: 40px; }
    h2 { margin-top: 40px; color: #334155; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px; }
    .ejemplo { background: #fff; border-radius: 8px; padding: 24px; margin-bottom: 32px; box-shadow: 0 1px 6px rgba(0,0,0,0.06); }
    .ejemplo img { max-width: 100%; height: auto; border-radius: 6px; margin-top: 16px; }
    figure { margin: 0; }
    figcaption { font-size: 0.85rem; color: #64748b; margin-top: 8px; font-style: italic; }
    .img-placeholder {
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 6px;
      display: flex; align-items: center; justify-content: center; color: #fff;
      font-weight: 700; font-size: 1.2rem; min-height: 200px; width: 100%; text-align: center;
    }
    code { background: #f1f5f9; padding: 2px 6px; border-radius: 4px; color: #e11d48; }
    pre { background: #1e293b; color: #e2e8f0; padding: 20px; border-radius: 8px; overflow-x: auto; font-size: 0.88rem; line-height: 1.5; margin: 12px 0; }
    ```

### Ejemplo 7: Datos estructurados JSON-LD completos para SEO (receta)

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Receta tradicional de paella valenciana con todos los pasos detallados, ingredientes y tiempos de preparación.">
  <title>Paella Valenciana Tradicional | Cocina Mediterránea</title>
  <!-- Open Graph -->
  <meta property="og:title" content="Paella Valenciana Tradicional">
  <meta property="og:description" content="Receta auténtica de paella valenciana con conejo, pollo y verduras frescas.">
  <meta property="og:image" content="https://ejemplo.com/img/paella.jpg">
  <meta property="og:url" content="https://ejemplo.com/recetas/paella-valenciana/">
  <meta property="og:type" content="article">
  <!-- Twitter Cards -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Paella Valenciana Tradicional">
  <!-- DATOS ESTRUCTURADOS: Receta (Schema.org) - Permite rich snippets con estrellas y tiempos -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Recipe",
    "name": "Paella Valenciana Tradicional",
    "author": { "@type": "Person", "name": "Carmen García Ruiz" },
    "description": "Receta auténtica de paella valenciana con conejo, pollo, judía verde, garrofón y arroz bomba. Incluye todos los secretos para conseguir el socarrat perfecto.",
    "datePublished": "2024-03-15",
    "prepTime": "PT30M",
    "cookTime": "PT45M",
    "totalTime": "PT1H15M",
    "recipeYield": "6 raciones",
    "recipeCategory": "Plato principal",
    "recipeCuisine": "Española, Valenciana",
    "keywords": "paella, valenciana, arroz, receta tradicional",
    "image": "https://ejemplo.com/img/paella.jpg",
    "nutrition": {
      "@type": "NutritionInformation",
      "calories": "520 kcal por ración",
      "proteinContent": "32 g",
      "carbohydrateContent": "58 g",
      "fatContent": "18 g"
    },
    "aggregateRating": {
      "@type": "AggregateRating",
      "ratingValue": "4.7",
      "bestRating": "5",
      "reviewCount": "284"
    },
    "recipeIngredient": [
      "400 g de arroz bomba", "600 g de conejo troceado",
      "400 g de pollo troceado", "200 g de judía verde plana",
      "150 g de garrofón", "2 tomates maduros rallados",
      "1 cucharadita de pimentón dulce", "Azafrán en hebras",
      "Aceite de oliva virgen extra", "Sal"
    ],
    "recipeInstructions": [
      { "@type": "HowToStep", "position": 1, "text": "Sofríe el conejo y el pollo en aceite hasta dorar." },
      { "@type": "HowToStep", "position": 2, "text": "Añade la judía verde y sofríe 5 minutos." },
      { "@type": "HowToStep", "position": 3, "text": "Incorpora tomate rallado y cocina hasta evaporar el agua." },
      { "@type": "HowToStep", "position": 4, "text": "Añade pimentón, agua caliente, garrofón y azafrán." },
      { "@type": "HowToStep", "position": 5, "text": "Distribuye el arroz y cocina 8 min a fuego fuerte." },
      { "@type": "HowToStep", "position": 6, "text": "Reduce el fuego y cocina 10-12 min más." },
      { "@type": "HowToStep", "position": 7, "text": "Deja reposar tapado 5 min antes de servir." }
    ]
  }
  </script>
  <!-- DATOS ESTRUCTURADOS: BreadcrumbList -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      { "@type": "ListItem", "position": 1, "item": { "@id": "https://ejemplo.com/", "name": "Inicio" } },
      { "@type": "ListItem", "position": 2, "item": { "@id": "https://ejemplo.com/recetas/", "name": "Recetas" } },
      { "@type": "ListItem", "position": 3, "item": { "@id": "https://ejemplo.com/recetas/paella/", "name": "Paella Valenciana" } }
    ]
  }
  </script>
</head>
<body>
  <main>
    <h1>Paella Valenciana Tradicional</h1>
    <p>Preparación: 30 min | Cocción: 45 min | Total: 1h 15min | 6 raciones</p>
    <p><strong>Valoración:</strong>
      <span aria-label="4.7 sobre 5 estrellas, 284 valoraciones">
        &#9733;&#9733;&#9733;&#9733;&#9734; 4.7/5 (284 valoraciones)
      </span>
    </p>
  </main>
</body>
</html>
```

### Ejemplo 8: Template HTML y Web Component básico con slot

=== "HTML"

    ``` html
    <!DOCTYPE html>
    <html lang="es">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Template y Web Components | Ejemplo Didáctico</title>
      <link rel="stylesheet" href="./styles2.css">
    </head>
    <body>
      <main class="contenedor">
        <h1>Template y Web Components con Slot</h1>

        <section class="seccion" aria-labelledby="seccion-template">
          <h2 id="seccion-template">1. Elemento &lt;template&gt; con JavaScript</h2>
          <p>El <code>&lt;template&gt;</code> contiene HTML inerte que no se renderiza hasta ser clonado con <code>.content.cloneNode(true)</code> e insertado en el DOM con JS. Ideal para estructuras repetitivas.</p>
          <button id="btn-agregar" type="button">+ Añadir Tarjeta desde Template</button>
          <div id="contenedor-tarjetas" aria-live="polite" style="margin-top:16px;"></div>
        </section>

        <section class="seccion" aria-labelledby="seccion-webcomponent">
          <h2 id="seccion-webcomponent">2. Web Component &lt;mi-tarjeta&gt; con slot</h2>
          <p>Componente personalizado con Shadow DOM y <code>&lt;slot&gt;</code> para proyección de contenido desde el HTML principal (light DOM). Los slots nombrados reciben contenido específico; el slot por defecto captura el resto.</p>
          <mi-tarjeta>
            <h3 slot="titulo">HTML Semántico</h3>
            <p slot="contenido">Estructura tus páginas con elementos HTML que transmiten significado real, mejorando accesibilidad, SEO y mantenibilidad.</p>
          </mi-tarjeta>
          <mi-tarjeta>
            <h3 slot="titulo">CSS Moderno</h3>
            <p slot="contenido">Domina Flexbox, Grid, variables CSS, capas (@layer), contenedores (@container) y las pseudoclases más recientes como :has().</p>
          </mi-tarjeta>
          <mi-tarjeta>
            <h3 slot="titulo">Accesibilidad Web</h3>
            <p slot="contenido">Construye interfaces inclusivas que todas las personas puedan utilizar, aplicando WAI-ARIA y diseño universal.</p>
          </mi-tarjeta>
        </section>
      </main>

      <!-- TEMPLATE: HTML inerte, no renderizado al cargar la página -->
      <template id="template-tarjeta">
        <article style="border:1px solid #e2e8f0;border-radius:6px;padding:16px;margin-bottom:8px;background:#f8fafc;">
          <h3 class="tarjeta-titulo" style="margin-bottom:6px;color:#2563eb;"></h3>
          <p class="tarjeta-contenido" style="color:#475569;font-size:0.92rem;"></p>
        </article>
      </template>

      <script src="./script.js"></script>
    </body>
    </html>
    ```

=== "CSS"

    ``` css
    body { font-family: 'Segoe UI', system-ui, sans-serif; background: #f1f5f9; padding: 40px 20px; color: #1e293b; }
    .contenedor { max-width: 800px; margin: 0 auto; }
    h1 { color: #2563eb; margin-bottom: 24px; }
    .seccion { background: #fff; border-radius: 8px; padding: 24px; margin-bottom: 32px; box-shadow: 0 1px 6px rgba(0,0,0,0.06); }
    h2 { margin-bottom: 16px; color: #334155; }
    button { background: #2563eb; color: #fff; border: none; padding: 10px 20px; border-radius: 6px; cursor: pointer; font-weight: 600; }
    button:hover { background: #1d4ed8; }
    mi-tarjeta { display: block; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin-bottom: 12px; background: #fff; transition: box-shadow 0.2s; }
    mi-tarjeta:hover { box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
    code { background: #f1f5f9; padding: 2px 6px; border-radius: 4px; }
    pre { background: #1e293b; color: #e2e8f0; padding: 16px; border-radius: 8px; overflow-x: auto; font-size: 0.85rem; }

    .tarjeta { font-family: 'Segoe UI', system-ui, sans-serif; }
    ::slotted([slot="titulo"]) { color: #2563eb; margin: 0 0 8px 0; font-size: 1.1rem; }
    ::slotted([slot="contenido"]) { color: #475569; line-height: 1.6; font-size: 0.92rem; margin: 0; }
    ```

=== "JS"

    ``` js
    /* 1. Clonar template y añadir tarjetas dinámicamente */
    const btnAgregar = document.getElementById('btn-agregar');
    const contenedor = document.getElementById('contenedor-tarjetas');
    const template = document.getElementById('template-tarjeta');
    let contador = 0;

    btnAgregar.addEventListener('click', function() {
      contador++;
      const clon = template.content.cloneNode(true); // true = clonación profunda
      clon.querySelector('.tarjeta-titulo').textContent = 'Tarjeta Dinámica #' + contador;
      clon.querySelector('.tarjeta-contenido').textContent =
        'Generada desde un &lt;template&gt; con JavaScript. Tarjeta número ' + contador + '.';
      contenedor.appendChild(clon);
    });

    /* 2. Definir Web Component &lt;mi-tarjeta&gt; con Shadow DOM y slot */
    class MiTarjeta extends HTMLElement {
      constructor() {
        super(); // Obligatorio: llamar al constructor padre
        const shadow = this.attachShadow({ mode: 'open' }); // Shadow DOM abierto
        shadow.innerHTML = `
          <style>
            .tarjeta { font-family: 'Segoe UI', system-ui, sans-serif; }
            ::slotted([slot="titulo"]) { color: #2563eb; margin: 0 0 8px 0; font-size: 1.1rem; }
            ::slotted([slot="contenido"]) { color: #475569; line-height: 1.6; font-size: 0.92rem; margin: 0; }
          </style>
          <div class="tarjeta">
            <slot name="titulo"></slot>
            <slot name="contenido"></slot>
            <slot></slot>
          </div>
        `;
      }
    }
    // Registrar el componente (el nombre DEBE contener un guión)
    customElements.define('mi-tarjeta', MiTarjeta);
    ```

## Casos reales

### Caso Real 1: GitHub (github.com) - HTML semántico a escala masiva

!!! example "Qué observar"
    GitHub, la plataforma de desarrollo colaborativo más grande del mundo, constituye un excelente caso de estudio de HTML semántico implementado a escala masiva. Al inspeccionar su página principal, observamos que utilizan elementos semánticos de forma extensa y correcta. La estructura principal se articula en torno a un `<header>` global que contiene una navegación con `<nav>` y una lista de enlaces. El logotipo está dentro de un enlace con `aria-label="Homepage"`. La navegación principal emplea `aria-label="Global"` para distinguirla de otras navegaciones. El contenido principal está en un `<main>`, y dentro de él se utilizan múltiples `<section>` con encabezados `<h2>` para cada bloque temático (productividad, seguridad, colaboración, CI/CD). GitHub hace uso extensivo de atributos ARIA: menús desplegables con `aria-expanded`, regiones con `aria-label`/`aria-labelledby`, y botones con `aria-describedby`. Usa `<details>`/`<summary>` para menús desplegables nativos en la navegación móvil. En SEO, utiliza Open Graph completo y datos JSON-LD de tipo `Organization`. Las imágenes incluyen `alt` descriptivos y `loading="lazy"`.

### Caso Real 2: MDN Web Docs (developer.mozilla.org) - Referencia de HTML semántico

!!! example "Qué observar"
    MDN Web Docs, mantenida por Mozilla, es posiblemente el mejor ejemplo de HTML semántico en la web. En una página de documentación encontramos: `<header>` global con logotipo, formulario de búsqueda con `role="search"` y navegación con `<nav aria-label="Main menu">`. El contenido principal usa `<article>` (cada página es autocontenida) con su propio `<header>` que contiene el `<h1>`. El contenido se organiza con `<section>` jerárquicas y encabezados perfectamente anidados sin saltos. Cada código de ejemplo está en un `<figure>` con `<figcaption>`. La barra lateral es un `<aside>` con `<nav>` interno. Incluye skip link, `aria-label` en iconos, `aria-expanded` en menús, meta description específica, Open Graph completo y JSON-LD de tipo `TechArticle`. También usa `theme-color` y manifiesto PWA.

### Caso Real 3: Patrón de tienda e-commerce (Shopify) - Formularios y productos

!!! example "Qué observar"
    Las tiendas e-commerce construidas con Shopify presentan desafíos únicos de semántica. La página de inicio usa `<header>` con navegación `<nav>` y listas. El carrito usa `aria-label="Cart"` y `aria-describedby` para información dinámica. Los listados de productos son `<ul>` con `<li>`, donde cada producto es un `<article>` (correcto: contenido autocontenido). Cada producto contiene imagen con `alt` descriptivo, nombre como `<h3>`, precio y botón "Añadir al carrito" como `<button>` (acción, no navegación). Las páginas de producto usan `<main>`; la galería de imágenes en `<figure>`. Los formularios de variantes (talla, color) usan `<fieldset>` con `<legend>` y radio buttons. La página de checkout es ejemplar: múltiples `<fieldset>` agrupados lógicamente con `<legend>`, todos los campos con `<label>` asociada, `required` en obligatorios, mensajes de error con `aria-describedby`, tipos HTML5 correctos (`email`, `tel`) y `autocomplete` apropiado para direcciones postales.

## Actividades guiadas

### Actividad Guiada 1: Construir la estructura semántica de una página de blog

**Resultado de Aprendizaje:** RA1 - Planificar la creación de una interfaz web valorando y aplicando especificaciones de diseño.  
**Objetivo:** Aprender a estructurar una página web completa utilizando exclusivamente elementos semánticos de HTML5, aplicando todos los principios de accesibilidad básica, jerarquía de encabezados y metadatos SEO.

**Enunciado:** Partiendo de un documento HTML en blanco, construye la estructura semántica completa de una página de blog personal. La página debe incluir: cabecera global con logotipo y navegación principal, contenido principal con un `<article>` que contenga al menos tres `<section>` con encabezados jerárquicos correctos (h2, h3, sin saltos), una barra lateral con información complementaria usando `<aside>`, y un pie de página global con enlaces legales. Implementa un enlace de salto al contenido principal (skip link), metadatos Open Graph y Twitter Cards completos, y datos estructurados JSON-LD de tipo `Article`. Todas las imágenes deben tener `alt` descriptivo. La navegación principal debe usar `aria-current="page"` y `aria-label` para distinguirla de otras navegaciones.

**Criterios de evaluación:**

- Utiliza correctamente `<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>` y `<footer>` (3 puntos).
- Existe un único `<h1>` y la jerarquía de encabezados no tiene saltos de nivel (2 puntos).
- Skip link funcional (apunta al `id` correcto y visible al recibir foco) (1 punto).
- Metadatos Open Graph, Twitter Cards y JSON-LD completos y válidos (2 puntos).
- Imágenes con textos alternativos significativos (1 punto).
- Navegación con `aria-current` y `aria-label` correctos (1 punto).

**Rúbrica:**

| Criterio | Insuficiente (0-4) | Satisfactorio (5-7) | Excelente (8-10) |
|----------|-------------------|---------------------|------------------|
| Elementos semánticos | Usa mayoría de divs; pocos elementos semánticos | Usa los elementos requeridos pero con algún error de anidamiento | Todos los elementos semánticos correctos y bien anidados |
| Jerarquía de encabezados | Más de un h1 o saltos de nivel | Un solo h1 pero algún salto de nivel | Un solo h1, jerarquía perfecta sin saltos |
| Accesibilidad | No tiene skip link, faltan alts | Tiene skip link y alts pero con carencias | Skip link funcional, alts descriptivos, aria-current y aria-label correctos |
| Metadatos SEO | Faltan la mayoría de metadatos | Metadatos presentes pero incompletos | OG, Twitter Cards y JSON-LD completos y válidos |

### Actividad Guiada 2: Formulario de pedido accesible paso a paso

**Resultado de Aprendizaje:** RA2 y RA5.  
**Objetivo:** Construir un formulario de pedido de comercio electrónico completamente accesible, aplicando todos los principios de formularios accesibles.

**Enunciado:** Diseña y codifica un formulario de pedido para una tienda online de productos tecnológicos. Debe contener al menos tres secciones lógicas agrupadas con `<fieldset>` y `<legend>`: (1) datos personales (nombre, email, teléfono), (2) dirección de envío (dirección, ciudad, código postal, país) y (3) método de pago (radio buttons para tarjeta, PayPal, transferencia). Cada sección debe tener campos obligatorios con `required` y asterisco visual. Usa tipos HTML5 adecuados (`email`, `tel`, `text`). Implementa validación con `pattern` para código postal y teléfono. Cada campo debe tener mensaje de error con `aria-describedby`. Añade `<datalist>` para país y `<output>` para mostrar dinámicamente el total. El formulario debe ser navegable con teclado.

**Criterios de evaluación:**

- Cada `<input>` tiene su `<label>` asociada con `for`/`id` (2 puntos).
- Campos agrupados con `<fieldset>`/`<legend>` (2 puntos).
- Tipos de input HTML5 especializados donde corresponde (1 punto).
- Mensajes de error vinculados con `aria-describedby` y `role="alert"` (2 puntos).
- Formulario navegable con teclado y foco visible (1 punto).
- Validación HTML5 funcional (2 puntos).

**Rúbrica:**

| Criterio | Insuficiente (0-4) | Satisfactorio (5-7) | Excelente (8-10) |
|----------|-------------------|---------------------|------------------|
| Labels y asociaciones | Muchos inputs sin label o sin for/id | Mayoría con label pero alguna asociación incorrecta | Todos los inputs con label correctamente asociada |
| Agrupación | Sin fieldset; todo en un solo bloque | Algunos fieldset pero faltan agrupaciones lógicas | Agrupación lógica completa con fieldset/legend |
| Tipos HTML5 | Usa type="text" para todo | Usa algunos tipos especializados | Usa el tipo HTML5 correcto en cada campo |
| Validación y errores | Sin validación ni mensajes de error | Validación básica sin mensajes personalizados | Validación HTML5 completa con mensajes aria-describedby |

### Actividad Guiada 3: Tabla de datos accesible con scope

**Resultado de Aprendizaje:** RA2.  
**Objetivo:** Construir una tabla de datos completamente accesible aplicando `<caption>`, `<thead>`, `<tbody>`, `<tfoot>`, `scope` y estilos responsivos.

**Enunciado:** Crea una tabla que muestre los resultados académicos de un grupo de estudiantes en tres asignaturas (HTML, CSS, JavaScript) durante dos trimestres. La tabla debe incluir: `<caption>` descriptivo, `<thead>` con encabezados de columna usando `scope="col"`, `<tbody>` con los nombres de los estudiantes usando `scope="row"`, y `<tfoot>` con la nota media de cada asignatura. Aplica estilos CSS para zebra striping, alineación de datos numéricos y diseño responsivo con scroll horizontal en móviles. Añade `aria-describedby` con una descripción larga de la tabla.

**Criterios de evaluación:**

- `<caption>` presente y descriptivo (1 punto).
- `<thead>`, `<tbody>` y `<tfoot>` correctamente utilizados (2 puntos).
- `scope="col"` en encabezados de columna y `scope="row"` en encabezados de fila (3 puntos).
- `aria-describedby` con descripción larga (1 punto).
- Estilos CSS: zebra striping, alineación numérica, responsividad (2 puntos).
- Código HTML válido y semánticamente correcto (1 punto).

### Actividad Guiada 4: Navegación con skip link, aria-current y breadcrumbs

**Resultado de Aprendizaje:** RA1 y RA5.  
**Objetivo:** Implementar una navegación completamente accesible con skip link, menú principal semántico, breadcrumbs y aria-current.

**Enunciado:** Construye la navegación de un sitio web de noticias con: (1) skip link que salte al contenido principal, (2) navegación principal con `<nav>` y lista, incluyendo `aria-current="page"` en la sección activa, (3) breadcrumbs semánticos con `<nav aria-label="Breadcrumb">` y lista ordenada, (4) navegación secundaria en el footer con enlaces legales, (5) estilos CSS para todos los estados (hover, focus-visible, active). El skip link debe ser visible solo al recibir foco.

**Criterios de evaluación:**

- Skip link funcional y correctamente estilado (2 puntos).
- Navegación principal con `<nav>`, `<ul>`/`<li>` y `aria-current` (2 puntos).
- Breadcrumbs semánticos con `aria-label` (2 puntos).
- Navegación secundaria en footer distinta de la principal (2 puntos).
- Estilos de foco visible en todos los elementos interactivos (1 punto).
- Diseño responsivo (1 punto).

### Actividad Guiada 5: Datos estructurados JSON-LD para una página de producto

**Resultado de Aprendizaje:** RA1.  
**Objetivo:** Implementar datos estructurados JSON-LD completos para la página de un producto de e-commerce, incluyendo nombre, precio, disponibilidad, valoración y breadcrumbs.

**Enunciado:** Crea la página HTML de un producto (auriculares inalámbricos) con todos los metadatos SEO: meta description, Open Graph, Twitter Cards y datos estructurados JSON-LD. Los JSON-LD deben incluir: tipo `Product` con nombre, descripción, imagen, marca, precio, disponibilidad y valoración agregada. También incluye un `BreadcrumbList` con la jerarquía: Inicio > Electrónica > Auriculares > \[nombre del producto\]. Valida el JSON-LD con la herramienta de prueba de datos estructurados de Google.

**Criterios de evaluación:**

- Meta description, Open Graph y Twitter Cards completos (2 puntos).
- JSON-LD de tipo Product con todas las propiedades requeridas (4 puntos).
- JSON-LD BreadcrumbList correcto (2 puntos).
- Página HTML semánticamente correcta (1 punto).
- JSON-LD sintácticamente válido (1 punto).

## Actividades propuestas

### Actividad Propuesta 1: Auditoría de accesibilidad de un sitio web real

**RA:** RA5. **Objetivo:** Analizar el HTML de un sitio web real, identificando buenas y malas prácticas de semántica y accesibilidad.  
**Enunciado:** Selecciona un sitio web de tu elección (puede ser una tienda online, un periódico digital o una red social). Utilizando las DevTools del navegador, inspecciona su código HTML y elabora un informe que identifique: (a) al menos 5 elementos semánticos utilizados correctamente, (b) al menos 3 problemas de accesibilidad (faltan `alt`, `label` sin `for`, saltos de encabezados, etc.), (c) una propuesta de mejora para cada problema encontrado. El informe debe incluir capturas de pantalla y fragmentos de código relevantes.  
**Criterios:** Identificación correcta de elementos semánticos (3 puntos), detección de problemas reales de accesibilidad (4 puntos), propuestas de mejora viables y bien fundamentadas (3 puntos).

### Actividad Propuesta 2: Conversión de divs a HTML semántico

**RA:** RA2. **Objetivo:** Transformar una página maquetada exclusivamente con `<div>` en una página con HTML semántico correcto.  
**Enunciado:** Se te proporciona una página web completa construida únicamente con elementos `<div>` y clases CSS. Tu tarea consiste en reescribir todo el HTML sustituyendo los `<div>` genéricos por los elementos semánticos de HTML5 apropiados (`<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>`, `<footer>`). También debes: añadir una jerarquía de encabezados correcta, implementar un skip link, añadir atributos `alt` a las imágenes que carecen de ellos, y asociar correctamente las etiquetas `<label>` en los formularios. La apariencia visual debe permanecer idéntica a la original.  
**Criterios:** Sustitución correcta de divs por elementos semánticos (5 puntos), jerarquía de encabezados correcta (2 puntos), skip link y accesibilidad básica implementados (3 puntos).

### Actividad Propuesta 3: Formulario de encuesta accesible

**RA:** RA2 y RA5. **Objetivo:** Diseñar un formulario de encuesta de satisfacción completamente accesible.  
**Enunciado:** Crea un formulario de encuesta para valorar un curso de formación. Debe incluir: datos del alumno (nombre, email), valoración numérica de 1 a 5 para diferentes aspectos (contenido, profesor, materiales, instalaciones) usando `<input type="range">` con `<output>` vinculado, un campo de comentarios (`<textarea>`) con `maxlength`, y un checkbox de consentimiento. Todo debe ser accesible: labels, fieldsets, mensajes de error, navegación por teclado.  
**Criterios:** Formulario completamente accesible (4 puntos), uso correcto de range+output (2 puntos), validación HTML5 funcional (2 puntos), diseño visual profesional y responsive (2 puntos).

### Actividad Propuesta 4: Página de preguntas frecuentes (FAQ) con details/summary

**RA:** RA2 y RA4. **Objetivo:** Crear una sección de FAQ interactiva y accesible usando elementos nativos HTML5 sin JavaScript.  
**Enunciado:** Diseña una página de preguntas frecuentes para un servicio de streaming de música. Debe contener al menos 8 preguntas con sus respuestas usando `<details>` y `<summary>`. Personaliza el estilo con CSS (transiciones, colores, iconos con `::after`). Incluye una sección de búsqueda/filtrado. La página debe ser completamente accesible y responsive.  
**Criterios:** Uso correcto de details/summary (3 puntos), estilos CSS personalizados (3 puntos), diseño responsive (2 puntos), accesibilidad (2 puntos).

### Actividad Propuesta 5: Página de artículo con SEO completo

**RA:** RA1. **Objetivo:** Crear una página de artículo periodístico optimizada para buscadores y redes sociales.  
**Enunciado:** Escribe y maqueta un artículo sobre "El impacto de la inteligencia artificial en el desarrollo web". La página debe incluir: estructura semántica completa, jerarquía de encabezados correcta, al menos 2 imágenes con `<figure>`/`<figcaption>`, metadatos Open Graph y Twitter Cards completos, datos estructurados JSON-LD de tipo `Article` y `BreadcrumbList`, y una sección de "artículos relacionados" en un `<aside>`. Usa la herramienta de validación de Schema.org para verificar los datos estructurados.  
**Criterios:** Estructura semántica correcta (3 puntos), SEO técnico completo (OG, Twitter, JSON-LD) (4 puntos), presentación visual profesional (2 puntos), validación Schema.org exitosa (1 punto).

## Actividades de ampliación

### Actividad de Ampliación 1: Web Component personalizado con Shadow DOM y slots

**Resultado de Aprendizaje:** RA4 - Integrar contenido multimedia y elementos interactivos.  
**Objetivo:** Crear un componente web personalizado reutilizable que encapsule una tarjeta de perfil de usuario, utilizando las tecnologías de Web Components: Custom Elements, Shadow DOM y slots HTML.

**Enunciado:** Desarrolla un componente `<perfil-usuario>` que muestre una tarjeta con foto, nombre, cargo y biografía breve. El componente debe: (1) usar Shadow DOM para encapsular estilos (sin que afecten al resto de la página ni sean afectados por estilos externos), (2) definir slots nombrados para `foto`, `nombre`, `cargo` y `biografia`, (3) incluir estilos CSS profesionales dentro del Shadow DOM (sombra, bordes redondeados, transiciones hover), (4) permitir personalizar el color de acento mediante una propiedad CSS personalizada (`--color-acento`) que atraviese el Shadow DOM, (5) crear al menos 4 instancias del componente en la misma página con diferentes datos, demostrando su reutilización. Publica el resultado en un único archivo HTML que funcione sin dependencias externas.

**Criterios de evaluación:**

- El componente se registra correctamente con `customElements.define()` y se puede usar en el HTML (2 puntos).
- Shadow DOM correctamente implementado con estilos encapsulados (2 puntos).
- Los slots nombrados funcionan correctamente y el contenido se proyecta desde el light DOM (2 puntos).
- La propiedad CSS personalizada `--color-acento` personaliza correctamente cada instancia (2 puntos).
- Diseño visual profesional y responsive (1 punto).
- El código JavaScript está correctamente comentado explicando cada parte (1 punto).

**Rúbrica:**

| Criterio | Insuficiente (0-4) | Satisfactorio (5-7) | Excelente (8-10) |
|----------|-------------------|---------------------|------------------|
| Custom Element | No se registra o tiene errores de JS | Se registra pero con funcionalidad limitada | Registro correcto, funciona en múltiples instancias |
| Shadow DOM | No usa Shadow DOM o está mal implementado | Shadow DOM presente pero estilos no encapsulados | Shadow DOM con estilos completamente encapsulados |
| Slots | No usa slots o no funcionan | Slots presentes pero no todos funcionan | Todos los slots nombrados funcionan correctamente |
| CSS Custom Property | No usa variables CSS | Usa variables pero no atraviesan el Shadow DOM | `--color-acento` personaliza cada instancia correctamente |

### Actividad de Ampliación 2: Sistema de pestañas accesible con WAI-ARIA

**Resultado de Aprendizaje:** RA5 - Evaluar la accesibilidad y usabilidad de la interfaz.  
**Objetivo:** Implementar un sistema de pestañas (tabs) completamente accesible utilizando WAI-ARIA, con gestión de foco por teclado y navegación mediante flechas.

**Enunciado:** Desarrolla un componente de pestañas que muestre información sobre diferentes frameworks CSS (Bootstrap, Tailwind, Foundation, Bulma). Cada pestaña debe contener una descripción, ventajas y desventajas del framework. El componente debe: (1) usar los roles ARIA `tablist`, `tab` y `tabpanel`, (2) implementar los estados `aria-selected` en las pestañas activas, (3) permitir navegación completa con teclado: Tab para entrar/salir del componente, flechas izquierda/derecha para cambiar de pestaña, (4) ocultar correctamente los paneles inactivos (`hidden` o `display:none`), (5) gestionar el foco para que al seleccionar una pestaña con ratón o teclado, el foco se mantenga en la pestaña seleccionada, (6) ser completamente responsive.

**Criterios de evaluación:**

- Roles ARIA `tablist`, `tab` y `tabpanel` correctamente implementados (3 puntos).
- Estados `aria-selected` actualizados correctamente al cambiar de pestaña (2 puntos).
- Navegación por teclado funcional (Tab, flechas, Home/End para primera/última pestaña) (3 puntos).
- Los paneles inactivos están correctamente ocultos para todos los usuarios (1 punto).
- Diseño visual profesional y responsive (1 punto).

### Actividad de Ampliación 3: Auditoría de accesibilidad con herramientas profesionales

**Resultado de Aprendizaje:** RA5 - Evaluar la accesibilidad y usabilidad de la interfaz.  
**Objetivo:** Realizar una auditoría profesional de accesibilidad de un sitio web real utilizando herramientas automáticas y manuales, elaborando un informe detallado con recomendaciones.

**Enunciado:** Selecciona un sitio web de un servicio público (ayuntamiento, universidad, biblioteca) y realiza una auditoría completa de accesibilidad. Debes: (1) ejecutar al menos 3 herramientas automáticas (WAVE, axe DevTools y Lighthouse), documentando los resultados con capturas de pantalla, (2) realizar una revisión manual comprobando: navegación con teclado (sin ratón), uso de un lector de pantalla (NVDA en Windows o VoiceOver en Mac), contraste de colores (usando la herramienta de contraste WCAG), zoom al 200%, (3) elaborar un informe en formato PDF que incluya: resumen ejecutivo, metodología empleada, problemas encontrados clasificados por nivel de gravedad (A, AA, AAA según WCAG 2.1), recomendaciones de corrección priorizadas, y conclusión final sobre el nivel de accesibilidad del sitio. Incluye fragmentos de código con las soluciones propuestas para al menos 5 de los problemas encontrados.

**Criterios de evaluación:**

- Uso correcto de al menos 3 herramientas automáticas con resultados documentados (2 puntos).
- Revisión manual completa documentada (3 puntos).
- Informe profesional bien estructurado con todos los apartados requeridos (3 puntos).
- Soluciones de código viables para al menos 5 problemas (2 puntos).

**Rúbrica:**

| Criterio | Insuficiente (0-4) | Satisfactorio (5-7) | Excelente (8-10) |
|----------|-------------------|---------------------|------------------|
| Herramientas automáticas | Usa solo 1 herramienta o resultados no documentados | Usa 2-3 herramientas pero documentación incompleta | 3+ herramientas con resultados bien documentados y capturas |
| Revisión manual | No realiza revisión manual o es muy superficial | Realiza parte de la revisión manual | Revisión manual completa: teclado, lector de pantalla, contraste, zoom |
| Informe | Informe desestructurado o incompleto | Informe con la mayoría de apartados | Informe profesional completo con todos los apartados y formato cuidado |
| Soluciones de código | No propone soluciones o son inviables | Propone soluciones pero no incluye código | 5+ soluciones con fragmentos de código funcionales |

## Buenas prácticas

1. **Usa siempre un único `<h1>` por página** que describa el tema principal. El `<h1>` es el elemento más importante para la estructura semántica y el SEO on-page. Coincide normalmente con el título del contenido, aunque puede diferir del `<title>`.

2. **No saltes niveles de encabezado.** Mantén una jerarquía estricta: `<h1>` → `<h2>` → `<h3>` → `<h4>`. Utiliza el nivel adecuado según la profundidad lógica del contenido, no según el tamaño visual deseado. Si necesitas un tamaño de fuente diferente, ajústalo con CSS.

3. **Utiliza elementos semánticos nativos siempre que sea posible**, antes de recurrir a ARIA. Un `<button>` nativo es siempre preferible a `<div role="button">`. Un `<nav>` es preferible a `<div role="navigation">`. La primera regla de ARIA debe guiar todas tus decisiones de marcado.

4. **Asocia siempre cada `<label>` con su campo de formulario** mediante los atributos `for` e `id`. Esta práctica, aparentemente simple, es la que más impacto tiene en la accesibilidad de los formularios. Nunca uses solo `placeholder` como sustituto de una etiqueta.

5. **Agrupa campos relacionados con `<fieldset>` y `<legend>`.** Esto es especialmente importante en formularios largos o complejos (checkout, registro, encuestas). La leyenda proporciona contexto que los lectores de pantalla anuncian antes de cada control del grupo.

6. **Proporciona siempre texto alternativo en las imágenes.** Usa `alt=""` para imágenes decorativas (sin espacio entre las comillas). Para imágenes informativas, describe la información que transmite la imagen, no su apariencia. Si la imagen es compleja (gráfico, infografía), complementa con `aria-describedby`.

7. **Implementa un skip link al inicio de cada página** que permita a usuarios de teclado y lectores de pantalla saltar directamente al contenido principal. Ocúltalo visualmente con CSS, pero mantenlo accesible y visible al recibir el foco.

8. **Usa tipos de input HTML5 especializados** (`email`, `tel`, `number`, `date`, `search`, `url`). No solo mejoran la experiencia en móviles mostrando teclados contextuales, sino que también proporcionan validación nativa y son reconocidos correctamente por los lectores de pantalla.

9. **Incluye siempre metadatos SEO completos**: meta description (120-160 caracteres, atractiva y con palabras clave), Open Graph (para compartir en redes sociales), Twitter Cards, y datos estructurados JSON-LD con Schema.org. Dedica tiempo a escribir buenas descripciones: son lo que los usuarios ven en los resultados de búsqueda y determinan si harán clic.

10. **Declara correctamente los metadatos del documento**: `<!DOCTYPE html>` en la primera línea, `<html lang="es">`, `<meta charset="UTF-8">` como primer elemento de `<head>`, y `<meta name="viewport">` para diseño responsivo sin restricciones de zoom.

11. **Construye la navegación con `<nav>` + `<ul>`/`<li>` + `<a>`.** Cuando existan varios `<nav>`, usa `aria-label` para diferenciarlos. Marca el enlace activo con `aria-current="page"`.

12. **Utiliza tablas solo para datos tabulares.** Incluye `<caption>`, usa `<th>` con `scope` para encabezados, y coloca `<tfoot>` antes de `<tbody>` para que los lectores de pantalla procesen primero el resumen.

## Errores frecuentes

1. **Usar `<div>` para todo.** Es el error más común entre principiantes. Construir toda la página con `<div>` y clases CSS impide que los lectores de pantalla y buscadores comprendan la estructura del documento. Solución: aprende y utiliza todos los elementos semánticos HTML5 disponibles.

2. **Múltiples `<h1>` en una misma página.** Algunos frameworks y constructores de sitios generan esto por defecto. Un solo `<h1>` por página es la norma. Los demás encabezados deben ser `<h2>`, `<h3>`, etc., según la profundidad jerárquica.

3. **Saltar niveles de encabezado.** Pasar de `<h2>` a `<h4>` sin un `<h3>` intermedio rompe el esquema del documento. Esto suele ocurrir cuando los estilos CSS predefinidos para `<h3>` no gustan visualmente. Solución: usar el nivel semántico correcto y ajustar el CSS.

4. **Usar `placeholder` como sustituto de `<label>`.** El placeholder desaparece al escribir, no es anunciado consistentemente por lectores de pantalla y no amplía el área de interacción. Solución: siempre incluye una `<label>` asociada con `for`/`id`.

5. **Botones implementados como `<div>` o `<a>`.** Usar `<div onclick="...">` o `<a href="#" onclick="...">` para acciones que no son navegación. Solución: si realiza una acción (enviar, abrir, cerrar, toggle), usa `<button>`. Si es navegación, usa `<a href="...">`.

6. **Imágenes sin `alt` o con `alt` no descriptivo.** Usar `alt="imagen"` o `alt="foto"` no proporciona información útil. Para imágenes decorativas, usar `alt=""` (vacío). Para imágenes informativas, describir el contenido que transmite la imagen.

7. **Formularios sin validación accesible.** Confiar solo en la validación del servidor o mostrar errores solo con color rojo (sin texto). Solución: usar validación HTML5 nativa + mensajes de error con texto asociados mediante `aria-describedby`.

8. **Uso incorrecto de `tabindex` con valores positivos.** `tabindex="1"`, `tabindex="2"` crean un orden artificial que raramente es correcto y es muy difícil de mantener. Solución: usa solo `tabindex="0"` o `tabindex="-1"`.

9. **Ocultar elementos con `display: none` o `hidden` cuando deben ser accesibles.** Los skip links, por ejemplo, deben ser accesibles para lectores de pantalla aunque estén visualmente ocultos. Solución: usar técnicas de ocultación visual con `position: absolute` y desplazamiento fuera de pantalla.

10. **Anidar elementos interactivos.** Un `<button>` dentro de un `<a>`, o viceversa, crea comportamientos impredecibles y viola la especificación HTML. Solución: no anidar elementos interactivos; si es necesario, repensar la estructura.

11. **Olvidar el atributo `lang` en `<html>`.** Esto afecta a la pronunciación de lectores de pantalla, traducción automática y corrección ortográfica. Solución: siempre incluir `<html lang="es">` (o el idioma correspondiente).

12. **No usar `aria-label` en navegaciones múltiples.** Cuando hay varios `<nav>`, los lectores de pantalla no pueden distinguirlos sin etiquetas. Solución: `<nav aria-label="Navegación principal">`, `<nav aria-label="Navegación del pie">`.

## Resumen

Esta unidad ha abordado en profundidad el HTML semántico y la accesibilidad web, dos competencias interrelacionadas y fundamentales para cualquier desarrollador web profesional. Hemos aprendido que el HTML semántico no es una opción estética sino una necesidad funcional: utilizar los elementos HTML según su propósito original (`<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>`, `<footer>`) proporciona significado estructural que beneficia a usuarios de lectores de pantalla, motores de búsqueda y otros desarrolladores.

La jerarquía de encabezados (`<h1>` a `<h6>`) debe ser estricta: un único `<h1>` por página, sin saltos de nivel, con encabezados descriptivos que permitan a los usuarios de tecnologías de asistencia navegar eficientemente por el contenido. Los formularios accesibles requieren atención al detalle: cada campo necesita su `<label>` asociada, los grupos de campos necesitan `<fieldset>` y `<legend>`, los tipos de input HTML5 especializados mejoran la experiencia en todos los dispositivos, y los mensajes de error deben ser claros y estar correctamente asociados mediante atributos ARIA.

La navegación semántica con `<nav>`, listas y `aria-current`, complementada con skip links, garantiza que todas las personas puedan orientarse y desplazarse por el sitio. Las tablas, cuando se usan exclusivamente para datos tabulares, requieren `<caption>`, `<thead>`, `<tbody>`, `<tfoot>` y atributos `scope` para ser comprensibles sin referencia visual. El SEO técnico mediante metaetiquetas, Open Graph, Twitter Cards y datos estructurados JSON-LD con Schema.org permite que nuestro contenido destaque en buscadores y redes sociales.

WAI-ARIA debe usarse como complemento, no como sustituto, del HTML nativo. La primera regla de ARIA nos recuerda que siempre es preferible el elemento HTML semántico antes que recrear su comportamiento con atributos ARIA. Finalmente, las características avanzadas de HTML5 (`<template>`, Web Components con `<slot>`, imágenes responsivas, lazy loading) nos permiten construir aplicaciones web modernas, eficientes y preparadas para el futuro.

El dominio del HTML semántico y la accesibilidad distingue a un desarrollador web profesional. No se trata solo de hacer que las páginas "funcionen", sino de garantizar que funcionen para todas las personas, en todos los dispositivos, y que nuestro contenido sea correctamente interpretado por los sistemas automáticos que indexan y procesan la web.

## Recursos complementarios

### Documentación oficial y especificaciones

- **HTML Living Standard (WHATWG):** https://html.spec.whatwg.org/ - La especificación viva de HTML, mantenida por el WHATWG. Referencia definitiva para todos los elementos y atributos HTML.
- **W3C HTML5 Specification:** https://www.w3.org/TR/html5/ - La recomendación oficial del W3C para HTML5.
- **WAI-ARIA Authoring Practices:** https://www.w3.org/WAI/ARIA/apg/ - Guía oficial del W3C con patrones de diseño accesibles para componentes web complejos (tabs, menús, diálogos, etc.).
- **WCAG 2.1 (Web Content Accessibility Guidelines):** https://www.w3.org/TR/WCAG21/ - Las pautas internacionales de accesibilidad web. Lectura obligatoria para entender los criterios de conformidad A, AA y AAA.
- **Schema.org:** https://schema.org/ - El vocabulario completo de datos estructurados. Documentación de todos los tipos y propiedades para JSON-LD y microdatos.

### Herramientas de validación y auditoría

- **WAVE Web Accessibility Evaluation Tool:** https://wave.webaim.org/ - Herramienta online y extensión de navegador para evaluar accesibilidad. Muestra errores, alertas y características de accesibilidad superpuestas sobre la página.
- **axe DevTools:** https://www.deque.com/axe/ - Extensión de navegador para auditoría de accesibilidad. Utilizada por Google, Microsoft y miles de equipos de desarrollo profesional.
- **Lighthouse (Google):** https://developer.chrome.com/docs/lighthouse/ - Herramienta integrada en Chrome DevTools que audita rendimiento, accesibilidad, SEO y buenas prácticas.
- **HTML Validator (W3C):** https://validator.w3.org/ - El validador oficial de HTML del W3C. Comprueba errores de sintaxis, anidamiento y uso de atributos.
- **Schema.org Validator (Google Rich Results Test):** https://search.google.com/test/rich-results - Valida datos estructurados y muestra cómo se verán en los resultados de búsqueda de Google.
- **Open Graph Debugger (Facebook):** https://developers.facebook.com/tools/debug/ - Depurador oficial de Open Graph. Muestra cómo se verá tu página al compartirla en Facebook.
- **Twitter Card Validator:** https://cards-dev.twitter.com/validator - Validador oficial de Twitter Cards.

### Guías y tutoriales recomendados

- **MDN Web Docs - HTML:** https://developer.mozilla.org/es/docs/Web/HTML - La referencia más completa y fiable de HTML en español, mantenida por Mozilla. Incluye documentación de cada elemento, ejemplos y compatibilidad.
- **web.dev - Learn Accessibility:** https://web.dev/learn/accessibility/ - Curso gratuito de accesibilidad web de Google. Cubre desde fundamentos hasta patrones avanzados con ejemplos prácticos.
- **A11y Project:** https://www.a11yproject.com/ - Comunidad y recursos sobre accesibilidad web. Incluye checklist, patrones y guías para desarrolladores.
- **Inclusive Components:** https://inclusive-components.design/ - Patrones de componentes web inclusivos con análisis detallado de decisiones de diseño y código accesible.

### Referencias rápidas (cheat sheets)

- **HTML5 Semantic Elements Cheat Sheet:** Resumen visual de todos los elementos semánticos HTML5 con descripciones y ejemplos de uso.
- **ARIA Cheat Sheet (Deque University):** Referencia rápida de roles, estados y propiedades ARIA con ejemplos prácticos.
- **JSON-LD Cheat Sheet:** Ejemplos de datos estructurados para los tipos más comunes de Schema.org.

### Lecturas complementarias

- **"Resilient Web Design" de Jeremy Keith:** Libro gratuito online sobre la filosofía de la web resiliente y la mejora progresiva.
- **"Accessibility for Everyone" de Laura Kalbag:** Introducción completa a la accesibilidad web para diseñadores y desarrolladores.
- **"Form Design Patterns" de Adam Silver:** Libro especializado en diseño de formularios web inclusivos y accesibles.
