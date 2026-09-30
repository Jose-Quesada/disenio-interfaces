---
icon: lucide/braces
---

# Unidad 18: Preprocesadores CSS — SASS/SCSS y LESS

## Objetivos de aprendizaje

Al finalizar esta unidad, el alumnado será capaz de:

1. Explicar qué es un preprocesador de estilos y por qué se necesita, diferenciándolo de las variables CSS nativas (Custom Properties).
2. Escribir hojas de estilo con SASS/SCSS empleando variables, interpolación, anidación, partials y `@extend`.
3. Reutilizar patrones mediante `@mixin` y `@include`, y encapsular lógica reutilizable con funciones (`@function`), bucles (`@for`, `@each`) y condicionales (`@if`).
4. Organizar un proyecto de estilos a escala real aplicando la arquitectura de módulos (`@use`/`@forward`) y una estructura de carpetas escalable (ITCSS / 7-1).
5. Compilar SASS a CSS estándar con `dart-sass` e integrarlo en el flujo de trabajo con Vite, verificando el resultado en el navegador.
6. Conocer las equivalencias en LESS y saber cuándo conviene un preprocesador frente a CSS nativo moderno o un framework utility-first (Tailwind).

## Relación con los Resultados de Aprendizaje

Esta unidad se vincula directamente con el **Resultado de Aprendizaje 2 (RA2)** del módulo profesional 0615 *Diseño de interfaces web*: *"Crea interfaces web homogéneos definiendo y aplicando estilos"*. En concreto, permite alcanzar el **criterio de evaluación 2.j**: *"Se han analizado y utilizado preprocesadores de estilos para traducir estilos comunes a un código estándar y reconocible por los navegadores"*, así como reforzar los criterios **2.c** (definir y asociar estilos globales en hojas externas), **2.g** (crear clases de estilos) y **2.i** (aplicar técnicas de diseño responsive, aquí mediante mixins de breakpoints).

Se apoya y complementa a la Unidad 8 (*CSS Profesional*), donde se trabajan selectores avanzados, especificidad, variables CSS nativas y animaciones, y a la Unidad 17 (*Tailwind CSS 4*), donde se estudia el enfoque utility-first. Esta unidad cierra el bloque de **estilos** del RA2 mostrando cómo los preprocesadores aportan mantenibilidad, reutilización y abstracción (variables, mixins, funciones, bucles) que el CSS plano no ofrece de forma tan cómoda.

!!! note "Nota sobre la numeración"
    La numeración de Resultados de Aprendizaje y Criterios de Evaluación empleada en esta unidad corresponde al currículo oficial del módulo 0615 (**RD 405/2023, BOE**; currículo andaluz). El **RA2** es el único resultado centrado en la **creación de interfaces homogéneas mediante estilos**; los preprocesadores son su herramienta natural.

## Conocimientos previos

Para abordar esta unidad con soltura, el alumnado debe:

1. Dominar CSS a nivel profesional (Unidad 8): selectores y especificidad, modelo de caja, `display`/posicionamiento, variables CSS (`--custom-property`, `var()`), media queries y animaciones.
2. Conocer Flexbox (Unidad 9) y CSS Grid (Unidad 10) para aplicar los patrones que se reutilizarán mediante mixins.
3. Haber trabajado el diseño responsive con metodología *mobile first* (Unidad 11).
4. Manejar la terminal y Node.js a nivel básico: instalar paquetes con `npm`, ejecutar scripts definidos en `package.json` y usar Vite como empaquetador (se retomará en la Unidad 17).
5. Comprender el concepto de "compilación": transformar un lenguaje intermedio (SASS/LESS) en CSS estándar que los navegadores sí entienden.

## Contenidos

1. **Introducción a los preprocesadores.** Definición y propósito. Diferencias entre CSS nativo, preprocesador y framework utility-first. Ventajas: abstracción, reutilización, mantenibilidad, escalabilidad. Panorama de herramientas (SASS/SCSS, LESS, Stylus) y elección de SASS/SCSS como estándar de facto.
2. **Sintaxis SASS vs SCSS.** Sintaxis indented (`.sass`) frente a sintaxis con llaves y punto y coma (`.scss`). Convenciones del ecosistema moderno (recomendación de SCSS).
3. **Variables e interpolación.** Declaración con `$`, tipado (números, colores, cadenas, listas, mapas), alcance, sobreescritura (`!default`) e interpolación `#{}` en selectores y propiedades.
4. **Anidación y referencia al padre.** Anidación de selectores, uso del `&` (pseudoestados, selectores descendientes, combinaciones), límites recomendados de profundidad.
5. **Partials y módulos.** Archivos parciales con prefijo `_`, sistema de módulos `@use`/`@forward` frente al legado `@import`, namespaces, carga de variables y mixins sin emitir CSS, y organización en carpetas.
6. **Reutilización: `@extend`.** Herencia de selectores, ventajas sobre la duplicación, limitaciones (pseudoestados, especificidad).
7. **Mixins.** `@mixin`/`@include`, parámetros con valores por defecto, argumentos nominales y variables (`...$args`), mixins que generan bloques condicionales, patrones habituales (breakpoints, flex-centrado, truncado de texto, tarjetas).
8. **Funciones.** `@function`/`@return`, funciones propias (escala tipográfica, cálculo de rem, conversión de unidades) y uso del sistema de unidades.
9. **Control de flujo.** Bucle `@for`, iteración sobre listas/mapas con `@each`, condicionales `@if`/`@else`, generación programática de clases (escalas de espaciado, grid de columnas).
10. **Mapas y listas.** Estructuras de datos, acceso por índice/clave (`map-get`, `nth`), patrones de "design tokens" en SASS.
11. **Arquitectura del proyecto de estilos.** Estructura escalable (ITCSS / 7-1: settings, tools, generic, elements, objects, components, utilities), flujo de compilación y buenas prácticas de nomenclatura.
12. **Compilación e integración.** `dart-sass` (recomendado frente a Ruby SASS en desuso), scripts de `package.json`, integración con Vite (`vite-plugin-sass` o el soporte nativo), opción `--watch`, minificación y mapas de fuentes (`source maps`).
13. **LESS (visión comparativa).** Sintaxis, variables `@`, mixins y parámetros, diferencias clave frente a SASS y cuándo se encuentra en proyectos legados.
14. **Preprocesador vs CSS nativo vs Tailwind.** Cuándo usar cada enfoque: variables nativas para temas en runtime, SASS para abstracción en tiempo de compilación, Tailwind para productividad utility-first; combinaciones híbridas (tokens + Custom Properties).

## Desarrollo teórico

### 1. ¿Por qué un preprocesador?

El CSS es un lenguaje de *hojas de estilos en cascada* pensado para describir la presentación, **no para programar**. Cuando una base de estilos crece (cientos o miles de reglas), surgen limitaciones reales: repetir valores (colores, espaciados, breakpoints) en muchos sitios, duplicar bloques de propiedades similares, o generar patrones repetitivos (escalas, columnas) a mano.

!!! info "Definición: preprocesador de estilos"
    Un **preprocesador** añade al CSS las características que todo lenguaje de programación ofrece: **variables, funciones, mixins, bucles y condicionales**. El resultado es un código más **DRY** (*Don't Repeat Yourself*), mantenible y escalable.

Es importante no confundir tres capas distintas que conviven en el frontend moderno:

- **CSS nativo (Custom Properties):** las variables `--color` se resuelven en *tiempo de ejecución* por el navegador; pueden cambiar dinámicamente con JavaScript o media queries. Son ideales para **temas** (modo claro/oscuro) y ajustes en runtime.
- **Preprocesador (SASS/LESS):** la abstracción ocurre en *tiempo de compilación*; el navegador solo recibe CSS plano estándar. Es ideal para **reutilización y generación** de código (mixins, funciones, bucles).
- **Framework utility-first (Tailwind):** desplaza la decisión a clases utilitarias atómicas directamente en el HTML; maximiza la productividad y la consistencia mediante restricciones.

Un enfoque profesional suele combinarlos: definir *design tokens* como variables SASS (compilación) y exponer los que cambian en runtime como Custom Properties. La Unidad 17 profundiza en Tailwind; esta unidad se centra en el preprocesador.

### 2. Sintaxis: SASS frente a SCSS

SASS nació con una sintaxis propia basada en indentación (archivos `.sass`), sin llaves ni punto y coma:

```sass
.tarjeta
  padding: 1rem
  border-radius: 8px
  &__titulo
    font-weight: 700
```

La extensión **SCSS** (`.scss`) usa la sintaxis clásica de CSS con llaves y `;`, por lo que **todo el CSS válido es SCSS válido**. Es la más extendida en el ecosistema actual (Vite, Webpack, la mayoría de bibliotecas) y la que usaremos:

```scss
.tarjeta {
  padding: 1rem;
  border-radius: 8px;

  &__titulo {
    font-weight: 700;
  }
}
```

Resumen de las dos sintaxis:

| | **SASS (`.sass`)** | **SCSS (`.scss`)** |
|---|--------------------|--------------------|
| **Sintaxis** | indentación, sin llaves ni `;` | llaves y `;` (clásica de CSS) |
| **Compatibilidad** | requiere reescribir el CSS existente | **todo CSS válido es SCSS válido** |
| **Ecosistema** | uso residual | estándar de facto (Vite, Webpack, bibliotecas) |

!!! tip "Convención del ecosistema"
    La recomendación general es trabajar **siempre en SCSS** salvo que un proyecto *legacy* exija `.sass`.

### 3. Variables e interpolación

Las variables se declaran con `$` y evitan repetir valores:

```scss
$color-primario: #667eea;
$espaciado-base: 1rem;
$breakpoints: (
  "sm": 640px,
  "md": 768px,
  "lg": 1024px,
);

.btn {
  background: $color-primario;
  padding: $espaciado-base ($espaciado-base * 2); // expresión aritmética
}
```

La **interpolación** `#{}` permite inyectar variables dentro de selectores, nombres de propiedades o cadenas donde no se espera un valor simple:

```scss
$icono: "buscar";
.icono-#{$icono} { /* .icono-buscar */ }
```

La sobreescritura con `!default` solo asigna el valor si la variable no estaba definida antes (útil en parciales reutilizables):

```scss
$color-fondo: #f5f5f5 !default; // se respeta si el proyecto ya lo definió
```

### 4. Anidación y referencia al padre

La anidación refleja la jerarquía del DOM y agrupa estilos relacionados. El carácter `&` representa el **selector padre**:

```scss
.nav {
  &__item {
    padding: 0.5rem 1rem;

    &:hover { background: rgba(0, 0, 0, 0.05); } // .nav__item:hover
    &--activo { font-weight: 700; }             // .nav__item--activo
  }
}
```

!!! tip "Límite de profundidad en la anidación"
    Buena práctica: limitar la anidación a **2-3 niveles** para no inflar la especificidad ni acoplar demasiado el CSS al HTML.

### 5. Partials y sistema de módulos

Un **partial** es un archivo con prefijo `_` (p. ej. `_botones.scss`) que no se compila por sí solo, sino que se incorpora a otros. El sistema moderno de **módulos** usa `@use` y `@forward`:

```scss
// _variables.scss
$color-primario: #667eea;

// botones.scss
@use "variables" as v;

.btn {
  background: v.$color-primario; // namespace "v"
}
```

!!! warning "Evita el legado `@import`"
    `@use` carga variables, mixins y funciones **una sola vez** y sin emitir CSS extra; a diferencia del legado `@import`, que **duplicaba reglas**. Prefiere siempre `@use`/`@forward` (módulos) sobre `@import`.

Los **namespaces** evitan colisiones de nombres. `@forward` permite re-exportar un módulo desde otro (patrones de *facade*).

### 6. Reutilización con `@extend`

`@extend` hace que un selector herede las reglas de otro, evitando duplicar bloques:

```scss
%enlace-base {
  color: $color-primario;
  text-decoration: none;
}

a,
.btn-enlace {
  @extend %enlace-base;
}
```

El prefijo `%` crea un **placeholder** que no se emite como clase real.

!!! note "Limitaciones de `@extend`"
    `@extend` **no hereda pseudoestados** ni aumenta la especificidad de forma predecible en todos los casos; para lógica condicional es **preferible un mixin**.

### 7. Mixins

Los mixins encapsulan bloques reutilizables con parámetros, valores por defecto y argumentos nominales:

```scss
@mixin breakpoint($punto) {
  @media (min-width: map-get($breakpoints, $punto)) {
    @content;
  }
}

@mixin centrar-flex {
  display: flex;
  align-items: center;
  justify-content: center;
}

.hero {
  @include breakpoint("md") {
    font-size: 2rem; // media query generada por el mixin
  }
  @include centrar-flex;
}
```

Los mixins con `@content` actúan como *plantillas* que envuelven el código que les pasamos. Son la herramienta central para generar **breakpoints responsive** de forma DRY (CE 2.i) y patrones recurrentes.

### 8. Funciones

Las funciones reciben argumentos y devuelven un valor con `@return`, permitiendo cálculos reutilizables:

```scss
@function rem($px) {
  @return ($px / 16) * 1rem;
}

.titulo {
  font-size: rem(32); // -> 2rem
}
```

Con mapas y funciones se implementan **design tokens** (escalas de color, tipografía, espaciado) que se consumen en todo el proyecto.

### 9. Control de flujo: bucles y condicionales

SASS permite generar CSS programáticamente:

```scss
// Escala de espaciado: .p-1 .. .p-6
@for $i from 1 through 6 {
  .p-#{$i} { padding: ($i * 0.25rem); }
}

// Columnas de grid: .col-1 .. .col-12
$columnas: 12;
@each $c in range(1, $columnas) {
  .col-#{$c} { grid-column: span #{$c}; }
}

@if (map-has-key($breakpoints, "xl")) {
  // solo se emite si existe el breakpoint xl
}
```

`@for` itera rangos, `@each` recorre listas/mapas y `@if`/`@else` introduce ramas condicionales. Esto elimina la escritura manual de decenas de clases repetitivas.

### 10. Mapas como design tokens

Los mapas (equivalentes a objetos) organizan tokens por categorías:

```scss
$tokens: (
  "color": (
    "primario": #667eea,
    "secundario": #764ba2,
    "texto": #1a202c,
  ),
  "tipografia": (
    "base": 1rem,
    "escala": 1.25, // razón de la escala modular
  ),
);

@function token($categoria, $nombre) {
  @return map-get(map-get($tokens, $categoria), $nombre);
}

body { color: token("color", "texto"); }
```

### 11. Arquitectura del proyecto de estilos

Una estructura escalable separa responsabilidades (patrones ITCSS / 7-1):

```
styles/
├── settings/     # variables, tokens, configuración global
│   └── _variables.scss
├── tools/        # mixins y funciones (no emiten CSS)
│   ├── _mixins.scss
│   └── _functions.scss
├── generic/      # reset, box-sizing, estilos base
├── elements/     # selectores de etiquetas HTML (h1, a, table…)
├── objects/      # patrones de layout reutilizables (contenedor, grid)
├── components/   # componentes UI concretos (botón, tarjeta, modal)
└── utilities/    # clases utilitarias (centrado, espaciado, display)
```

!!! tip "Orden de carga"
    **El orden de carga importa**: de lo genérico a lo específico. Esta arquitectura, combinada con `@use`, hace mantenible una base de estilos grande.

### 12. Compilación e integración con Vite

!!! info "Compilador recomendado: `dart-sass`"
    `dart-sass` es el **compilador oficial y recomendado**; el antiguo **Ruby SASS está en desuso**. En un proyecto con Vite:

```jsonc
// package.json
{
  "scripts": {
    "dev": "vite",
    "build": "vite build"
  }
}
```

Vite integra SASS de forma nativa: basta con importar el SCSS principal en el punto de entrada y Vite lo compila al vuelo (con `--watch` implícito en desarrollo):

```scss
// main.scss
@use "settings/variables";
@use "tools/mixins";
@use "components/botones";
```

En producción, `vite build` emite CSS minificado. Se recomienda activar **source maps** (`--source-map`) en desarrollo para depurar el SCSS original en las DevTools.

### 13. LESS (visión comparativa)

LESS es el preprocesador más antiguo y aún aparece en proyectos legados (p. ej., Ant Design usó LESS). Sus diferencias clave: variables con `@` (`@color: red;`), mixins por herencia de selector o parámetros, y soporte de operaciones. La sintaxis es más cercana al CSS clásico. En proyectos nuevos se prefiere SASS/SCSS por su ecosistema y el sistema de módulos; conocer LESS permite mantener bases de código existentes.

### 14. ¿Preprocesador, CSS nativo o Tailwind?

- **CSS nativo (Custom Properties):** cuando el valor cambia en *runtime* (temas, modo oscuro) o el proyecto es pequeño y no justifica una herramienta extra.
- **SASS/SCSS:** cuando hay mucha lógica reutilizable (mixins de breakpoints, escalas generadas por bucles, design tokens compilados) y se busca mantener un CSS propio mantenible.
- **Tailwind (Unidad 17):** cuando se prioriza velocidad y consistencia mediante utilidades atómicas sin escribir hojas de estilo a medida.

En la práctica profesional es común combinar SASS para *tokens* y lógica con Custom Properties para *temas*, o usar Tailwind como capa principal y SASS solo para lo que el framework no cubre. La elección debe responder a criterios de escalabilidad, mantenibilidad y productividad del equipo (CE 2.j).

## Ejemplos guiados

### Ejemplo 1: Sistema de tokens + mixins responsive en SCSS

!!! example "Contexto pedagógico"
    Partimos de un **proyecto vacío con Vite** y creamos una base de estilos reutilizable que genera breakpoints y una escala de espaciado automáticamente.

```scss
// settings/_variables.scss
$color-primario: #667eea;
$color-fondo:    #f7fafc;
$breakpoints: ("sm": 640px, "md": 768px, "lg": 1024px);

// tools/_mixins.scss
@use "variables" as v;

@mixin bp($punto) {
  @media (min-width: map-get(v.$breakpoints, $punto)) {
    @content;
  }
}

// tools/_functions.scss
@function rem($px) { @return ($px / 16) * 1rem; }

// generic/_base.scss
@use "variables" as v;

* { box-sizing: border-box; }
body {
  margin: 0;
  background: v.$color-fondo;
  font-size: rem(16);
}

// objects/_contenedor.scss
@use "../tools/mixins" as t;

.contenedor {
  width: min(100% - 2rem, 72rem);
  margin-inline: auto;

  @include t.bp("md") { width: min(100% - 3rem, 80rem); }
}

// utilities/_espaciado.scss
@for $i from 1 through 6 {
  .p-#{$i} { padding: ($i * 0.25rem); }
  .m-#{$i} { margin: ($i * 0.25rem); }
}

// main.scss (punto de entrada)
@use "generic/base";
@use "objects/contenedor";
@use "utilities/espaciado";
```

!!! note "Explicación del resultado"
    Al compilar, Vite genera **CSS plano** con las *media queries* ya resueltas y las clases `.p-1`…`.p-6` / `.m-1`…`.m-6` generadas por el bucle. **El navegador no conoce SASS**: solo recibe CSS estándar (**CE 2.j**).

### Ejemplo 2: Mixin de tarjeta con variantes condicionales

```scss
@mixin tarjeta($radio: 8px, $elevacion: 1) {
  background: #fff;
  border-radius: $radio;
  padding: 1.5rem;
  box-shadow: 0 (#{$elevacion * 2}px) (#{$elevacion * 4}px) rgba(0, 0, 0, 0.08);

  @if ($elevacion > 2) {
    // variante "destacada" con más profundidad
    border: 2px solid #667eea;
  }
}

.tarjeta        { @include tarjeta(8px, 1); }
.tarjeta--alta { @include tarjeta(12px, 3); }
```

## Casos reales

- **Material Design / Bootstrap:** sus bases de estilos históricamente se construyeron con preprocesadores (Bootstrap utilizó SASS a partir de la versión 4) para generar utilidades, variantes de componentes y breakpoints mediante bucles y mixins.
- **Sistemas de diseño corporativos:** equipos grandes definen *design tokens* en SASS/LESS y los distribuyen; la migración de Ant Design de LESS a CSS-in-JS ilustra cómo la elección del preprocesador está ligada a necesidades de *theming* dinámico (temas por cliente).
- **Proyectos legados:** es habitual encontrar LESS en aplicaciones antiguas; saber leerlo y, si procede, migrarlo a SCSS o a Tailwind es una tarea profesional recurrente.

## Actividades guiadas

1. **Instalación.** Crea un proyecto con Vite (`npm create vite@latest`), instala `sass` como dependencia de desarrollo y configura el punto de entrada en SCSS. Verifica que el navegador recibe CSS compilado (inspecciona la hoja de estilos generada).
2. **Tokens.** Define un mapa `$tokens` con colores, tipografía y espaciado del proyecto y crea la función `token()` para consumirlo. Sustituye todos los valores "en crudo" de una hoja existente por tokens.
3. **Mixins responsive.** Crea el mixin `@mixin bp($punto)` y refactoriza las media queries repetidas de un layout usando breakpoints nominales.

## Actividades propuestas

1. **Refactorización DRY (RA2 / CE 2.j).** Toma una hoja de estilos CSS plana de ~300 líneas con valores repetidos y conviértela en SCSS: extrae variables, crea al menos tres mixins (breakpoint, centrado flex, tarjeta) y una función (`rem()`). Documenta cuántas líneas se ahorran y cómo mejora la mantenibilidad.
2. **Generación por bucles.** Genera con `@for`/`@each` las utilidades de espaciado (`p-*`, `m-*`) y un sistema de columnas de grid (`.col-1`…`.col-12`). Comprueba en el navegador que funcionan.
3. **Arquitectura 7-1.** Reorganiza el proyecto de la actividad anterior en la estructura settings/tools/generic/elements/objects/components/utilities usando `@use`, y explica el orden de carga elegido.

## Actividades de ampliación

1. **Comparativa.** Implementa el mismo componente (una tarjeta con variantes) tres veces: CSS nativo con Custom Properties, SASS y Tailwind. Redacta un informe comparando productividad, tamaño final del CSS emitido y cuándo conviene cada enfoque.
2. **Migración LESS→SCSS.** Localiza una base de estilos en LESS (p. ej., de un proyecto open source) y migra sus variables, mixins y anidaciones a SCSS, verificando que el resultado visual no cambia.

## Buenas prácticas

1. Usa **SCSS** (`.scss`) salvo que el proyecto exija `.sass`.
2. Prefiere `@use`/`@forward` (módulos) sobre el legado `@import`.
3. Limita la anidación a 2-3 niveles para no inflar la especificidad.
4. Centraliza valores repetidos en **tokens** (mapas) y consúmelos mediante funciones.
5. Genera patrones repetitivos con **bucles**, no a mano.
6. Mantén una **arquitectura de carpetas** clara y un orden de carga predecible.
7. Activa **source maps** en desarrollo para depurar el SCSS original.
8. Documenta mixins y funciones complejos; son la "API" interna del proyecto.

## Errores frecuentes

1. **Anidar en exceso:** produce selectores muy específicos que luego son difíciles de sobrescribir. Solución: limita la profundidad y usa BEM/objetos.
2. **Usar `@import` en lugar de `@use`:** duplica reglas y rompe el sistema de módulos. Migra a `@use`.
3. **Poner lógica en el HTML cuando corresponde al preprocesador:** los mixins/bucles pertenecen a la capa de estilos, no a clases sueltas repetidas.
4. **Compilar con Ruby SASS (en desuso):** usa `dart-sass` para evitar incompatibilidades y problemas de seguridad.
5. **Confundir variables SASS con Custom Properties:** las primeras se resuelven en compilación (no cambian en runtime); para temas dinámicos usa Custom Properties.
6. **Olvidar el `&` al anidar pseudoestados:** escribir `:hover` sin prefijo dentro de un bloque puede generar el selector equivocado si no se usa `&:hover`.

## Resumen

Un preprocesador como SASS/SCSS añade al CSS variables, mixins, funciones, bucles y condicionales, permitiendo construir bases de estilos DRY, escalables y mantenibles. El flujo es: escribir SCSS (con tokens, partials y arquitectura por capas) → compilar con `dart-sass`/Vite → obtener CSS estándar que el navegador entiende (CE 2.j). Las variables nativas resuelven temas en runtime; el preprocesador resuelve la reutilización en compilación; Tailwind ofrece una alternativa utility-first. Elegir entre ellos depende de los criterios de escalabilidad, mantenibilidad y productividad del equipo.

## Recursos complementarios

- **SASS (dart-sass) — documentación oficial:** https://sass-lang.com/documentation/
- **Guía de módulos SASS (`@use`/`@forward`):** https://sass-lang.com/documentation/best-practices/
- **Vite + SASS:** https://vitejs.dev/guide/features.html (sección CSS Pre-processors)
- **LESS — documentación oficial:** https://lesscss.org/
- **ITCSS (arquitectura de estilos):** https://itcss.io/
- **7-1 Architecture:** https://71project.com/
