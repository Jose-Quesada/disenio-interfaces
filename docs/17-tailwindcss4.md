---
icon: lucide/wind
---

# Unidad 17: Tailwind CSS 4 — Fundamentos y Aplicación Práctica

## Objetivos de aprendizaje

Al finalizar esta unidad, el alumnado será capaz de identificar el paradigma Utility First como alternativa metodológica al enfoque tradicional de hojas de estilo en cascada. El estudiante comprenderá el modelo de clases atómicas propuesto por Tailwind CSS y lo contrastará con las técnicas convencionales de maquetación, valorando las ventajas en productividad, consistencia visual y mantenibilidad que ofrece un framework basado en restricciones. El alumnado instalará y configurará Tailwind CSS 4 en un proyecto real gestionado con Vite, comprendiendo cada paso del proceso de construcción y el rol del plugin específico para el empaquetador. Aprenderá a interpretar y aplicar la escala numérica del sistema de diseño (espaciado, tipografía, colores, bordes) entendiendo la correspondencia entre valores nominales y unidades reales (rem, píxeles). Manejará con soltura las utilidades de layout, incluyendo display, posicionamiento, dimensionamiento, Flexbox y Grid, reconociendo la nomenclatura específica de Tailwind para cada propiedad CSS. Aplicará los conceptos de diseño responsivo Mobile First utilizando los breakpoints del framework y dominará la sintaxis de estados interactivos (hover, focus, active, disabled) y pseudoselectores (first, last, odd, even). Conocerá las novedades introducidas en la versión 4, incluyendo la nueva arquitectura de motor interno, la sintaxis de configuración mediante CSS nativo y la integración optimizada con Vite. Finalmente, el alumno será capaz de construir interfaces reales completas combinando utilidades de Tailwind, comparando el resultado con implementaciones equivalentes en CSS tradicional y valorando críticamente cuándo cada enfoque resulta más adecuado según el contexto del proyecto.

## Relación con los Resultados de Aprendizaje

Esta unidad desarrolla directamente el **Resultado de Aprendizaje 2 (RA2)** del módulo 0615 *Diseño de interfaces web* —"Crea interfaces web homogéneos definiendo y aplicando estilos"—, según el currículo oficial (RD 405/2023, BOE; currículo andaluz). El trabajo con Tailwind CSS permite alcanzar los criterios relacionados con la aplicación de estilos mediante frameworks CSS de utilidad (CE 2.i), la creación de layouts adaptables y responsivos y la implementación de componentes visuales coherentes con una guía de estilo definida (CE 2.g). Asimismo, se relaciona transversalmente con el **RA1** (planificación de interfaces, en cuanto a la selección razonada de frameworks y herramientas: CE 1.e) y con el **RA4** (integración de contenidos multimedia e interactivos), ya que los componentes construidos con Tailwind constituyen la base visual sobre la que se implementan las funcionalidades interactivas con JavaScript. La unidad contribuye a que el alumnado desarrolle la competencia profesional de maquetación avanzada, comprendiendo que la elección entre CSS tradicional, preprocesadores y frameworks utility-first no es arbitraria sino que responde a criterios de escalabilidad, mantenibilidad y productividad del equipo de desarrollo. Se trabajará también la competencia digital avanzada mediante el uso del ecosistema Node.js y herramientas de construcción modernas como Vite, así como la competencia de aprender a aprender al fomentar la consulta autónoma de la documentación oficial de Tailwind CSS como recurso de referencia continuo en el ejercicio profesional.

Esta unidad también contribuye al desarrollo de la competencia transversal de trabajo en equipo, ya que el enfoque Utility First de Tailwind CSS facilita la colaboración entre desarrolladores al proporcionar un lenguaje común de clases atómicas que elimina ambigüedades y reduce la fricción en las revisiones de código. Los estudiantes comprenderán que la adopción de un framework de diseño como Tailwind no es solo una decisión técnica sino estratégica, que impacta en la velocidad de desarrollo, la consistencia del producto final y la capacidad de incorporación de nuevos miembros al equipo.

## Conocimientos previos

Para abordar con éxito esta unidad, el alumnado debe dominar los fundamentos de HTML5 semántico, incluyendo la estructura correcta del DOM, el uso de etiquetas como header, nav, main, section, article, aside y footer, y la comprensión del modelo de caja (box model). Es imprescindible un conocimiento sólido de CSS3 a nivel de propiedades: selectores (tipo, clase, ID, atributo, pseudoclases, pseudoelementos), especificidad y cascada, propiedades de tipografía, color y fondo, modelo de caja (margin, padding, border), display y posicionamiento, Flexbox y Grid básicos, media queries y diseño responsivo Mobile First, transiciones y animaciones simples. El alumnado debe tener experiencia práctica previa en la maquetación de al menos tres interfaces completas (landing page, dashboard, formulario de registro) utilizando CSS tradicional o preprocesadores.

Se requiere también un conocimiento operativo del entorno Node.js: qué es npm, cómo inicializar un proyecto con package.json, cómo instalar dependencias de desarrollo y de producción, para qué sirve la carpeta node_modules y el archivo package-lock.json. Es recomendable haber trabajado previamente con algún empaquetador como Vite o Webpack a nivel básico (entender qué hace un bundler, qué es el hot module replacement, cómo se ejecutan los scripts de desarrollo y build). A nivel conceptual, el alumno debería haber experimentado las dificultades que plantea el CSS tradicional en proyectos grandes: colisiones de nombres de clases, especificidad descontrolada, dificultad para mantener la consistencia visual, archivos CSS que crecen sin control, y la paradoja de tener que inventar nombres semánticos para cada contenedor. Esta experiencia previa de "dolor CSS" es el mejor punto de partida para valorar el cambio de paradigma que propone Tailwind.

Adicionalmente, el alumnado debe tener conocimientos fundamentales de diseño web responsivo, comprendiendo conceptos como viewport, breakpoints, unidades relativas (em, rem, vw, vh, %) frente a absolutas (px), y la filosofía Mobile First. Es recomendable familiaridad con las herramientas de desarrollo del navegador (Chrome DevTools o Firefox Developer Edition), ya que serán esenciales para depurar los estilos generados por Tailwind durante el desarrollo.

## Contenidos

1. **Introducción a Tailwind CSS**: origen, filosofía Utility First, comparativa con metodologías tradicionales (BEM, SMACSS, OOCSS) y con frameworks basados en componentes (Bootstrap, Foundation). Ventajas y desventajas del enfoque.

2. **Tailwind CSS 4**: novedades de la versión, diferencias con v3, nueva arquitectura del motor de generación de CSS (Oxide, escrito en Rust), sistema de configuración CSS-first, eliminación de dependencias de PostCSS en la integración con Vite.

3. **Instalación y configuración con Vite**: inicialización del proyecto con plantilla vanilla, instalación de dependencias (tailwindcss, @tailwindcss/vite), configuración del plugin en vite.config.js, importación del CSS base con @import "tailwindcss". Verificación del funcionamiento.

4. **Sistema de diseño y escala numérica**: correspondencia entre valores de clase y unidades rem/píxeles, fundamentos del diseño por restricciones. Escala completa (1 al 96) y su justificación práctica.

5. **Paleta de colores**: nombres de color disponibles (slate, gray, zinc, neutral, stone, red, orange, amber, yellow, lime, green, emerald, teal, cyan, sky, blue, indigo, violet, purple, fuchsia, pink, rose), escala 50-950, transparencia con notación de barra (bg-red-500/75), colores personalizados mediante @theme.

6. **Utilidades tipográficas**: tamaño de fuente (text-xs a text-9xl), peso (font-thin a font-black), alineación, color, decoración, altura de línea, espaciado de letras, familias tipográficas (font-sans, font-serif, font-mono).

7. **Espaciado**: margen (m-*), padding (p-*), espacio entre elementos flex/grid (gap-*). Direccionalidad: t, r, b, l, x, y.

8. **Layout**: display (block, inline, inline-block, flex, grid, hidden), posición (static, fixed, absolute, relative, sticky), z-index (z-0 a z-50, z-auto).

9. **Dimensionamiento**: anchura (w-*, w-full, w-screen, fracciones w-1/2), altura (h-*, h-full, h-screen), dimensiones mínimas y máximas.

10. **Flexbox con utilidades Tailwind**: dirección, envoltura, justificación, alineación, crecimiento (flex-1, flex-auto, flex-initial, flex-none), orden.

11. **Grid con utilidades Tailwind**: columnas (grid-cols-1 a grid-cols-12), filas, spanning (col-span-*, row-span-*), alineación, flujo automático.

12. **Diseño responsivo Mobile First**: breakpoints (sm: 640px, md: 768px, lg: 1024px, xl: 1280px, 2xl: 1536px). Sintaxis de prefijos. Estrategias de maquetación adaptativa.

13. **Estados interactivos y pseudoselectores**: hover:, focus:, focus-visible:, active:, visited:, disabled:, first:, last:, odd:, even:, group-hover:, peer-focus:, dark:.

14. **Bordes y anillos**: radio (rounded, rounded-md, rounded-lg, rounded-full), grosor, color, estilo (solid, dashed, dotted), outline y ring.

15. **Efectos visuales**: sombras (shadow-sm a shadow-2xl, shadow-inner), opacidad (opacity-0 a opacity-100), desenfoque (blur-sm a blur-3xl), backdrop-blur.

16. **Tablas**: table, table-auto, table-fixed, border-collapse, border-separate. Construcción de tablas estilizadas con utilidades.

17. **Animaciones y transiciones**: transition, duration, ease, delay, animate-spin, animate-ping, animate-pulse, animate-bounce. Animaciones personalizadas.

18. **Modo oscuro**: estrategias de implementación (class vs media), el prefijo dark:, toggle con JavaScript y localStorage, transición suave entre temas.

19. **Valores arbitrarios y personalización**: notación de corchetes (`w-[300px]`, `bg-[#1a1a1a]`), cuándo usar arbitrary values vs configuración del tema. Configuración con @theme en Tailwind v4.

20. **Herramientas complementarias**: Prettier plugin para ordenación automática de clases, Headless UI para componentes accesibles con React, Tailwind CSS IntelliSense para VS Code.

## Desarrollo teórico

### 1. El paradigma Utility First: una revolución en la forma de escribir CSS

La historia del desarrollo web frontend ha transitado por diversas etapas en lo que respecta a la gestión de estilos. En los primeros años de la web, el CSS se escribía de forma monolítica en uno o pocos archivos, con selectores anidados que reflejaban la estructura del DOM. Este enfoque, aunque intuitivo al principio, generaba problemas graves de especificidad, acoplamiento entre estructura HTML y estilos CSS, y una creciente dificultad para modificar componentes sin efectos colaterales imprevistos. Para resolver estos problemas surgieron metodologías como BEM (Block Element Modifier), SMACSS (Scalable and Modular Architecture for CSS) y OOCSS (Object Oriented CSS), que propusieron convenciones de nomenclatura y organización basadas en componentes. Estas metodologías mejoraron la mantenibilidad pero introdujeron una nueva carga cognitiva: la necesidad de inventar nombres de clases semánticos para cada elemento, decisión que a menudo derivaba en debates interminables dentro del equipo de desarrollo. Paralelamente, frameworks como Bootstrap, Foundation o Materialize ofrecieron componentes preconstruidos con estilos ya definidos, acelerando el desarrollo pero limitando la personalización y generando sitios web con una apariencia reconocible y poco diferenciada.

Es en este contexto donde **Adam Wathan**, creador de Tailwind CSS, propone un cambio de paradigma radical:

!!! info "Utility First"
    En lugar de escribir CSS semántico con nombres de clases descriptivos, se utilizan **clases atómicas de propósito único** que se aplican directamente en el HTML. Cada clase de Tailwind corresponde, aproximadamente, a **una declaración CSS individual**.

    Por ejemplo, en lugar de crear una clase `.card` con múltiples propiedades, construimos la tarjeta componiendo clases como `bg-white`, `rounded-lg`, `shadow-md`, `p-6`, `flex`, `flex-col`, `gap-4`.

    Esta aproximación, denominada **Utility First**, genera inicialmente rechazo en muchos desarrolladores acostumbrados al CSS tradicional, pues el HTML resultante parece más verboso y aparentemente menos semántico. Sin embargo, la experiencia práctica en proyectos reales demuestra que esta verbosidad se compensa con creces mediante la **eliminación de la fricción constante** de alternar entre archivos HTML y CSS, la **desaparición de problemas de cascada y especificidad**, la **garantía de consistencia visual** al trabajar con un sistema de diseño predefinido mediante restricciones, y el hecho de que el CSS resultante en producción es **mínimo**, pues solo contiene las clases realmente utilizadas en el proyecto (*purgado de CSS* o *tree-shaking*).

Tailwind no es un simple conjunto de utilidades: es un **sistema de diseño completo** materializado en clases atómicas, que ofrece una paleta de colores, una escala tipográfica, una escala de espaciado, unas sombras, unos bordes y unos breakpoints responsivos que, **por restricción**, garantizan coherencia visual.

!!! quote "Adam Wathan"
    «Tailwind te da el poder de construir cualquier diseño sin tener que luchar contra estilos predefinidos.»

**Ventajas del enfoque Utility First:**

- **Productividad máxima** — no se pierde tiempo cambiando de contexto entre HTML y CSS, ya que todo se define en el mismo archivo.
- **Consistencia garantizada** — la escala de valores predefinidos impide que cada desarrollador use medidas arbitrarias, resultando en un diseño más cohesionado.
- **CSS mínimo en producción** — Tailwind analiza el proyecto y elimina automáticamente las clases no utilizadas, generando archivos CSS de solo unos pocos kilobytes.
- **No hay que inventar nombres** — se elimina la carga cognitiva de nombrar cada contenedor, cada *wrapper*, cada variante.
- **Refactorización sin miedo** — al modificar una clase en el HTML, no hay riesgo de afectar a otros componentes, ya que cada clase es independiente y no hay herencia CSS compleja.

**Desventajas más citadas:**

- **Verbosidad en el HTML** — puede resultar abrumadora al principio, especialmente en componentes complejos que acumulan muchas clases.
- **Curva de aprendizaje inicial** — memorizar la nomenclatura de las clases, aunque la documentación y las extensiones IDE resuelven esto rápidamente.
- **Tendencia a repetir combinaciones de clases** — en Tailwind se soluciona extrayendo componentes (en el framework de tu elección) o usando `@apply` para crear clases personalizadas.
- **Dificultad para desarrolladores acostumbrados a la separación estricta de *concerns*** (HTML semántico + CSS separado), que deben adaptarse a un nuevo modelo mental.

### 2. Tailwind CSS 4: la evolución del framework

La versión 4 de Tailwind CSS, lanzada a principios de 2025, representa la mayor reescritura del framework desde su creación. El objetivo principal de esta versión ha sido simplificar radicalmente la experiencia de instalación y configuración, eliminando gran parte del boilerplate que las versiones anteriores requerían. La novedad más significativa es la introducción de un nuevo motor interno, denominado "Oxide", escrito en Rust, que reemplaza al antiguo generador de CSS basado en JavaScript. Este nuevo motor es hasta diez veces más rápido en la generación del CSS y reduce drásticamente el tiempo de compilación tanto en desarrollo (hot reload instantáneo) como en producción (builds significativamente más rápidas).

Otra innovación fundamental de la versión 4 es la configuración CSS-first. En Tailwind v3, la configuración principal residía en un archivo JavaScript (`tailwind.config.js`) donde se definían las extensiones de tema, los plugins, el contenido a escanear y las variantes personalizadas. En v4, esta configuración migra hacia el propio CSS, permitiendo definir la configuración mediante directivas CSS nativas y funciones como `@theme`. Esto acerca Tailwind a los estándares CSS emergentes y reduce la dependencia de archivos de configuración JavaScript, simplificando la integración con cualquier herramienta que procese CSS.

La instalación también se simplifica: en lugar de necesitar PostCSS más el plugin de Tailwind más el archivo de configuración, en v4 basta con instalar el paquete `tailwindcss` y, si usamos Vite, el plugin `@tailwindcss/vite`, importando posteriormente Tailwind en el CSS principal con un simple `@import "tailwindcss"`. Esta única línea reemplaza a las tres directivas `@tailwind base`, `@tailwind components` y `@tailwind utilities` de versiones anteriores.

Entre las mejoras adicionales destacan: compatibilidad mejorada con CSS nesting nativo (sin necesidad de PostCSS nesting), soporte nativo para capas CSS (@layer), ampliación de la paleta de colores, nuevas utilidades para animaciones y transiciones, y la eliminación de dependencias internas que lastraban el rendimiento. La migración desde v3 a v4 está asistida por una herramienta automática que analiza el proyecto y sugiere los cambios necesarios. Para nuevos proyectos, la recomendación oficial es comenzar directamente con v4.

Las diferencias clave entre v3 y v4:

| Aspecto | **Tailwind v3** | **Tailwind v4** |
|---------|-----------------|-----------------|
| **Archivo de configuración** | `tailwind.config.js` obligatorio por defecto | no lo requiere por defecto (aunque se puede usar si se prefiere) |
| **Configuración del tema** | `theme.extend` en JS | `@theme` en CSS |
| **Motor de generación** | generador en JavaScript | motor **Oxide**, escrito en **Rust** |
| **Instalación con Vite** | `postcss` + `autoprefixer` | `@tailwindcss/vite` |
| **Directivas CSS** | `@tailwind base/components/utilities` | `@import "tailwindcss"` |
| **Rendimiento de compilación** | referencia | mejora de un factor de **5-10x** |

### 3. Instalación paso a paso con Vite

El entorno de desarrollo recomendado por el equipo de Tailwind CSS para la versión 4 es Vite, un empaquetador ultrarrápido que aprovecha los módulos ES nativos del navegador durante el desarrollo y genera builds optimizadas con Rollup para producción. El proceso de instalación completo consta de los siguientes pasos, que el alumnado debe ejecutar y comprender:

**Paso 1: Crear un nuevo proyecto con Vite.** Ejecutamos el comando `npm create vite@latest mi-proyecto -- --template vanilla`. El flag `--template vanilla` indica que queremos un proyecto con HTML, CSS y JavaScript puros, sin frameworks como React o Vue. Esto genera una estructura mínima con `index.html`, `style.css`, `main.js` y `package.json`. Accedemos al directorio: `cd mi-proyecto`.

**Paso 2: Instalar dependencias base.** Con `npm install` instalamos Vite y las dependencias listadas en el package.json generado. En este punto, el proyecto funciona pero no incluye Tailwind.

**Paso 3: Instalar Tailwind CSS v4.** Ejecutamos `npm install tailwindcss @tailwindcss/vite`. El paquete `tailwindcss` contiene el núcleo del framework con el motor Oxide, mientras que `@tailwindcss/vite` es el adaptador que permite a Vite procesar correctamente las directivas de Tailwind durante el desarrollo y la construcción. A diferencia de v3, no necesitamos instalar PostCSS ni autoprefixer, ya que el plugin de Vite se encarga de todo internamente.

**Paso 4: Configurar Vite.** Editamos el archivo `vite.config.js` para importar y registrar el plugin de Tailwind:

```javascript
// vite.config.js
import { defineConfig } from 'vite'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  plugins: [
    tailwindcss(),
  ],
})
```

Esta configuración indica a Vite que procese todos los archivos CSS a través de Tailwind durante el desarrollo y la construcción. El plugin se encarga de escanear los archivos HTML y JavaScript en busca de clases de Tailwind, generar el CSS correspondiente y aplicar tree-shaking para eliminar las clases no utilizadas en producción.

**Paso 5: Importar Tailwind en el CSS.** Abrimos el archivo `style.css` y sustituimos su contenido (o añadimos al inicio) la directiva de importación:

```css
/* style.css */
@import "tailwindcss";
```

!!! info "Reemplazo de las directivas clásicas"
    Esta única línea es todo lo necesario. El motor de Tailwind v4 interpreta esta directiva y genera todo el CSS base (*reset*, variables CSS, utilidades) en función de las clases que se utilicen en el proyecto. **No se necesitan** las antiguas directivas `@tailwind base`, `@tailwind components` y `@tailwind utilities`.

**Paso 6: Verificar el funcionamiento.** En el archivo `index.html`, añadimos una línea de prueba que use clases de Tailwind:

```html
<h1 class="text-3xl font-bold text-blue-600">¡Tailwind CSS 4 funciona!</h1>
```

Iniciamos el servidor de desarrollo con `npm run dev`. Si el navegador muestra el texto con el estilo esperado (tamaño grande, negrita, color azul), la configuración está completa y funcionando correctamente. A partir de este momento, podemos utilizar cualquier clase de Tailwind en nuestro HTML y los cambios se reflejarán instantáneamente gracias al Hot Module Replacement (HMR) de Vite.

### 4. El sistema de diseño de Tailwind: escala numérica y restricciones

Uno de los pilares que explican la productividad y consistencia que proporciona Tailwind CSS es su sistema de diseño numérico, que traduce propiedades CSS a una escala predefinida y razonada de valores. En lugar de escribir valores arbitrarios como `padding: 13px` o `margin: 27px`, Tailwind nos ofrece una escala de números que van desde el 0 hasta el 96, donde cada número representa un múltiplo de 0.25rem (equivalente a 4px con la configuración por defecto de 16px por rem). Esta escala no es arbitraria: ha sido cuidadosamente diseñada para cubrir prácticamente todas las necesidades de espaciado en diseño web, evitando la proliferación de valores inconsistentes que surge cuando cada desarrollador elige sus propias medidas.

La correspondencia es la siguiente (cada número es un múltiplo de **0.25rem**):

| Clase | Valor CSS | En píxeles |
|-------|-----------|------------|
| `p-1` | `0.25rem` | **4 px** |
| `p-2` | `0.5rem` | **8 px** |
| `p-3` | `0.75rem` | **12 px** |
| `p-4` | `1rem` | **16 px** |

La progresión no es estrictamente lineal: los primeros valores crecen de 1 en 1 y después se amplían los saltos (`0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 72, 80, 96`). Esta progresión concentra los incrementos pequeños donde más se necesitan (diseño de detalle, espaciados finos) y amplía los saltos en valores grandes (márgenes de sección).

!!! tip "Diseño por restricciones: ritmo vertical"
    Trabajar con una escala restringida tiene un beneficio psicológico y práctico inmediato: **elimina la parálisis por análisis**. En CSS tradicional, cuando un desarrollador necesita aplicar un margen, tiene a su disposición infinitos valores (**11 px**, **13 px**, **17 px**...) y debe tomar una decisión. Con Tailwind, la escala limita las opciones a valores que ya han demostrado funcionar bien juntos: si el diseño necesita **16 px** de *padding*, usamos `p-4`; si necesita **24 px**, usamos `p-6`.

    Esta restricción acelera la toma de decisiones y garantiza que todos los espaciados del proyecto sean múltiplos consistentes de **4 px**, creando un ritmo visual armónico que los diseñadores denominan **«vertical rhythm»**. La misma filosofía se aplica a tipografía, bordes redondeados, sombras y opacidades.

Es importante que el alumnado entienda que Tailwind utiliza **rem** como unidad base. Un rem equivale al `font-size` del elemento raíz (`html`), que por defecto son **16 px** en la mayoría de navegadores. Esto significa que los espaciados y tamaños de Tailwind **escalan proporcionalmente** si el usuario modifica el tamaño de fuente base en su navegador, contribuyendo a la **accesibilidad**.

!!! warning "Práctica no recomendada"
    Si en un proyecto se necesita cambiar la base a **10 px** (para facilitar cálculos mentales), se puede configurar mediante `font-size: 62.5%` en el `html`, pero **esta práctica no se recomienda** ya que rompe la correspondencia natural de la escala de Tailwind.

### 5. La paleta de colores de Tailwind

Tailwind CSS incluye una paleta de colores excepcionalmente completa y cuidadosamente curada por expertos en diseño. Está compuesta por 22 familias de color, cada una de las cuales se despliega en una escala de 11 tonos numerados del 50 al 950. Las familias disponibles son: slate (gris azulado, el neutro por defecto en Tailwind), gray (gris puro), zinc (gris cálido con matiz amarillento), neutral (gris verdaderamente neutro, sin matiz), stone (gris piedra con matiz marrón), red (rojo), orange (naranja), amber (ámbar), yellow (amarillo), lime (lima), green (verde), emerald (esmeralda), teal (verde azulado), cyan (cian), sky (azul cielo), blue (azul), indigo (índigo), violet (violeta), purple (púrpura), fuchsia (fucsia), pink (rosa) y rose (rosa rojizo).

Cada familia sigue una convención de nomenclatura que combina el nombre del color con el tono mediante un guion: `bg-red-500`, `text-blue-700`, `border-emerald-400`. El uso típico de cada rango de tono es:

| Tonalidad | Uso recomendado |
|-----------|-----------------|
| **50, 100, 200** | más claros: fondos sutiles y superficies de tarjeta |
| **400, 500, 600** | colores base: los que representan la identidad del color |
| **700, 800, 900, 950** | más oscuros: texto sobre fondos claros y creación de contraste |

Por ejemplo, un botón primario típico usaría `bg-blue-600 text-white` (fondo azul medio, texto blanco), y al hacer *hover* `hover:bg-blue-700` (se oscurece ligeramente).

Tailwind ofrece soporte para transparencia mediante la **notación de barra**. La sintaxis `bg-red-500/75` aplica el color `red-500` con una opacidad del **75 %**. Esto es equivalente a `background-color: rgba(239, 68, 68, 0.75)`. La notación usa la sintaxis `<color>-<tono>/<opacidad>`, donde la opacidad es un número de **0 a 100**. Esta característica es extremadamente útil para crear *overlays* semitransparentes, fondos con efecto vidrio esmerilado, o texto con opacidad reducida para crear jerarquía visual. Ejemplos: `bg-black/50` (negro al **50 %**), `text-white/70` (texto blanco al **70 %**), `bg-indigo-600/20` (índigo muy suave para fondos).

Para proyectos que requieren una paleta corporativa personalizada, Tailwind permite extender o reemplazar la paleta mediante la directiva `@theme` en el archivo CSS principal (en v4). Por ejemplo, para añadir colores de marca corporativa:

```css
@import "tailwindcss";
@theme {
  --color-primary: #3b82f6;
  --color-primary-dark: #1e40af;
  --color-secondary: #f59e0b;
  --color-accent: #ec4899;
}
```

Esto genera automáticamente las clases `bg-primary`, `text-primary`, `border-primary-dark`, etc., integrándose con los estados hover, focus y breakpoints responsivos. Además, al definir colores como variables CSS, se mantiene la consistencia con el sistema de diseño y se facilita la implementación de temas oscuros o múltiples temas.

### 6. Tipografía con utilidades de Tailwind

El control tipográfico en Tailwind es exhaustivo y cubre todas las propiedades CSS relacionadas con texto. La escala de tamaños de fuente va desde `text-xs` (0.75rem, 12px) hasta `text-9xl` (8rem, 128px), pasando por `text-sm`, `text-base` (1rem, 16px, el tamaño por defecto), `text-lg`, `text-xl`, `text-2xl`, `text-3xl`, `text-4xl`, `text-5xl`, `text-6xl`, `text-7xl` y `text-8xl`. Cada tamaño incluye automáticamente una altura de línea (line-height) razonable y proporcionada. Por ejemplo, `text-xl` aplica `font-size: 1.25rem` (20px) y `line-height: 1.75rem` (28px), mientras que `text-sm` aplica `font-size: 0.875rem` (14px) y `line-height: 1.25rem` (20px). Esta relación tamaño/altura de línea está calibrada para garantizar una legibilidad óptima.

El peso tipográfico se controla con clases como `font-thin` (100), `font-extralight` (200), `font-light` (300), `font-normal` (400), `font-medium` (500), `font-semibold` (600), `font-bold` (700), `font-extrabold` (800) y `font-black` (900). La alineación dispone de `text-left`, `text-center`, `text-right` y `text-justify`. El color de texto se aplica con el prefijo `text-` seguido del nombre de color y tono: `text-gray-900`, `text-blue-600`, `text-white`. La decoración incluye `underline`, `line-through` y `no-underline` (útil para quitar el subrayado por defecto de los enlaces). La transformación de texto ofrece `uppercase`, `lowercase`, `capitalize` y `normal-case`.

Para la altura de línea independiente del tamaño, Tailwind dispone de: `leading-none` (1, sin espacio extra), `leading-tight` (1.25, compacto para títulos), `leading-snug` (1.375), `leading-normal` (1.5, legible para texto corrido), `leading-relaxed` (1.625, aireado) y `leading-loose` (2, muy espaciado). El espaciado entre letras se maneja con `tracking-tighter` (-0.05em), `tracking-tight` (-0.025em), `tracking-normal` (0), `tracking-wide` (0.025em), `tracking-wider` (0.05em) y `tracking-widest` (0.1em). El `tracking-tight` es especialmente útil para títulos grandes, ya que un espaciado ligeramente reducido mejora la cohesión visual de las letras a tamaños grandes.

Las familias tipográficas se agrupan en tres categorías predefinidas: `font-sans` (pila sans-serif moderna: Inter, ui-sans-serif, system-ui, -apple-system, etc.), `font-serif` (pila serif: ui-serif, Georgia, Cambria, Times New Roman, serif) y `font-mono` (pila monoespaciada: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace). Para tipografías personalizadas, se pueden importar desde Google Fonts o servicios similares y registrarlas en el tema:

```css
@import "tailwindcss";
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Inter:wght@400;500;600;700&display=swap');

@theme {
  --font-display: 'Playfair Display', Georgia, serif;
  --font-body: 'Inter', ui-sans-serif, system-ui, sans-serif;
}
```

Esto genera las clases `font-display` y `font-body` que pueden usarse como cualquier otra utilidad tipográfica de Tailwind.

### 7. Espaciado, layout y dimensionamiento

El sistema de espaciado de Tailwind abarca margin, padding y gap usando la escala numérica común. Las utilidades de margen se escriben con el prefijo `m-` y las de padding con `p-`. Ambas pueden aplicarse con direccionalidad específica mediante sufijos: `mt-` (margin-top), `mr-` (margin-right), `mb-` (margin-bottom), `ml-` (margin-left), `mx-` (margin-left y margin-right), `my-` (margin-top y margin-bottom). La misma lógica se aplica al padding. Los valores negativos de margen, útiles para solapar elementos o ajustar posiciones, se aplican anteponiendo un guión: `-mt-4` (margen superior negativo de 1rem), `-ml-2` (margen izquierdo negativo de 0.5rem). El espaciado entre elementos hijos de contenedores flex y grid se gestiona con `gap-*`, `gap-x-*` y `gap-y-*`. A diferencia de `space-x-*` y `space-y-*` (que añaden margen entre hijos excepto al primero, técnica legacy), `gap` es la recomendación moderna ya que funciona en ambos contextos (flex y grid) y no presenta problemas con elementos que se envuelven a la siguiente línea.

Las utilidades de display abarcan `block`, `inline-block`, `inline`, `flex`, `inline-flex`, `grid`, `inline-grid`, `hidden` (equivale a `display: none`), `flow-root` (crea un nuevo contexto de formato de bloque, útil para clearfix moderno) y `contents` (hace que el elemento desaparezca del árbol de caja, exponiendo sus hijos al padre). Para posicionamiento: `static`, `fixed`, `absolute`, `relative` y `sticky`, combinables con las propiedades de desplazamiento `top-*`, `right-*`, `bottom-*`, `left-*` e `inset-*` (shorthand para las cuatro direcciones). El control de z-index ofrece valores predefinidos: `z-0`, `z-10`, `z-20`, `z-30`, `z-40`, `z-50` y `z-auto`.

El dimensionamiento de anchura utiliza `w-*` (con la escala numérica), `w-full` (100%), `w-screen` (100vw), `w-min` (min-content), `w-max` (max-content), `w-fit` (fit-content) y fracciones: `w-1/2` (50%), `w-1/3`, `w-2/3`, `w-1/4`, `w-3/4`, `w-1/5`, `w-2/5`, `w-3/5`, `w-4/5`, `w-1/6`, `w-5/6`, `w-1/12`, `w-2/12` y así sucesivamente. Para altura: `h-*`, `h-full`, `h-screen`, `h-min`, `h-max`, `h-fit`. Las dimensiones mínimas y máximas: `min-w-*`, `max-w-*`, `min-h-*`, `max-h-*`. Tailwind incluye contenedores predefinidos para `max-w-`: `max-w-xs` (20rem, 320px), `max-w-sm` (24rem, 384px), `max-w-md` (28rem, 448px), `max-w-lg` (32rem, 512px), `max-w-xl` (36rem, 576px), `max-w-2xl` (42rem, 672px), `max-w-3xl` (48rem, 768px), `max-w-4xl` (56rem, 896px), `max-w-5xl` (64rem, 1024px), `max-w-6xl` (72rem, 1152px) y `max-w-7xl` (80rem, 1280px). Estos contenedores, combinados con `mx-auto`, son la forma recomendada de limitar la anchura del contenido en páginas web.

### 8. Flexbox y Grid con utilidades de Tailwind

Tailwind ofrece un mapeo completo y expresivo de Flexbox. Un contenedor flex se crea con `flex` (o `inline-flex`). La dirección con `flex-row`, `flex-row-reverse`, `flex-col` y `flex-col-reverse`. La envoltura con `flex-wrap`, `flex-wrap-reverse` y `flex-nowrap`. La justificación del eje principal: `justify-start`, `justify-end`, `justify-center`, `justify-between`, `justify-around`, `justify-evenly`. La alineación del eje transversal: `items-start`, `items-end`, `items-center`, `items-baseline`, `items-stretch`. La alineación de líneas múltiples: `content-start`, `content-center`, `content-end`, `content-between`, `content-around`, `content-evenly`. La alineación individual de un hijo: `self-auto`, `self-start`, `self-end`, `self-center`, `self-stretch`, `self-baseline`. El control de crecimiento: `flex-1` (flex: 1 1 0%), `flex-auto` (flex: 1 1 auto), `flex-initial` (flex: 0 1 auto), `flex-none` (flex: none), así como `grow`, `grow-0`, `shrink` y `shrink-0`. El orden: `order-first`, `order-last`, `order-none` y `order-1` a `order-12`.

El sistema Grid de Tailwind es igualmente completo. Un contenedor se crea con `grid` (o `inline-grid`). Las columnas: `grid-cols-1` hasta `grid-cols-12`, más `grid-cols-none`. Para layouts responsive se combinan con breakpoints: `grid-cols-1 md:grid-cols-2 lg:grid-cols-3`. El spanning: `col-span-1` a `col-span-12` y `col-span-full`. Las filas: `grid-rows-1` a `grid-rows-6` y `grid-rows-none`. El spanning de filas: `row-span-1` a `row-span-6` y `row-span-full`. El flujo automático: `grid-flow-row` (por defecto), `grid-flow-col`, `grid-flow-row-dense`, `grid-flow-col-dense`. El inicio y final explícitos: `col-start-*`, `col-end-*`, `row-start-*`, `row-end-*`, con valores del 1 al 13 y `auto`. Las propiedades abreviadas de alineación: `place-items-*`, `place-content-*`, `place-self-*`, que combinan align y justify en una sola clase.

### 9. Diseño responsivo Mobile First

Tailwind adopta el enfoque **Mobile First** como filosofía de diseño. Las clases **sin prefijo** definen el estilo base para el viewport más pequeño (móvil). Los breakpoints se aplican como **prefijos** que sobrescriben o añaden estilos en viewports progresivamente mayores:

| Prefijo | `min-width` |
|---------|-------------|
| `sm:` | **640 px** |
| `md:` | **768 px** |
| `lg:` | **1024 px** |
| `xl:` | **1280 px** |
| `2xl:` | **1536 px** |

La sintaxis es simple: se antepone el prefijo del breakpoint seguido de dos puntos a cualquier utilidad: `sm:p-4`, `md:flex`, `lg:grid-cols-3`, `xl:text-5xl`.

Un patrón común es definir un *grid* que se adapta progresivamente: `grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4`. En móvil, **una columna**; a partir de **640 px**, dos; desde **1024 px**, tres; y en pantallas grandes de **1280 px**, cuatro. Similarmente, un menú que se oculta en móvil y se muestra en escritorio: `hidden lg:flex`. Un *padding* que crece con el *viewport*: `px-4 sm:px-6 lg:px-8`. Un texto responsivo: `text-lg md:text-xl lg:text-2xl`.

La estrategia de trabajo recomendada es:

1. Comenzar maquetando para **móvil** (las clases base sin prefijo).
2. Comprobar que la experiencia es óptima en **pantallas pequeñas**.
3. Agregar progresivamente los prefijos `sm:`, `md:`, `lg:`, `xl:` para los puntos de ruptura donde el diseño necesita adaptarse.
4. **No intentar cubrir todos los breakpoints** para cada elemento; solo añadir variantes donde sea necesario.

Esta metodología evita el error común de diseñar para escritorio y luego intentar «comprimir» el diseño para móvil.

### 10. Estados interactivos, bordes, sombras, animaciones y modo oscuro

Los estados interactivos se aplican con prefijos similares a los breakpoints:

| Estado | Ejemplo | Qué hace |
|--------|---------|----------|
| `hover:` | `hover:bg-blue-700 hover:text-white` | al **pasar el cursor** |
| `focus:` | `focus:outline-none focus:ring-2 focus:ring-blue-500` | al **recibir el foco** |
| `focus-visible:` | — | solo para navegación por **teclado**, ideal para accesibilidad |
| `active:` | `active:scale-95` | durante la **pulsación** |
| `disabled:` | `disabled:opacity-50 disabled:cursor-not-allowed` | elementos **deshabilitados** |

Los pseudoselectores estructurales son `first:`, `last:`, `odd:`, `even:` (para tablas con filas alternas). `group-hover:` permite que un elemento reaccione al *hover* sobre su ancestro con clase `group`; `peer-focus:` permite que un elemento reaccione al *focus* de un hermano con clase `peer`. Ambos son extremadamente potentes para crear interacciones complejas **sin JavaScript**.

Los bordes ofrecen `rounded`, `rounded-md`, `rounded-lg`, `rounded-xl`, `rounded-2xl`, `rounded-3xl`, `rounded-full` (círculo/píldora). El grosor: `border`, `border-0`, `border-2`, `border-4`, `border-8`. Direccional: `border-t-*`, `border-b-*`, etc. El color: `border-gray-300`, `border-blue-500`. El estilo: `border-solid`, `border-dashed`, `border-dotted`, `border-double`, `border-none`. El outline: `outline-none`, `outline-*`, `outline-offset-*`. El ring (alternativa moderna al outline): `ring-0`, `ring-1`, `ring-2`, `ring-4`, `ring-8`, `ring-inset`, `ring-blue-500`.

Las sombras: `shadow-sm`, `shadow`, `shadow-md`, `shadow-lg`, `shadow-xl`, `shadow-2xl`, `shadow-inner`, `shadow-none`. Con color: `shadow-red-500/30`. La opacidad: `opacity-0` a `opacity-100` en incrementos de 5 y de 10. Los filtros: `blur-none`, `blur-sm`, `blur`, `blur-md`, `blur-lg`, `blur-xl`, `blur-2xl`, `blur-3xl`. Backdrop blur: `backdrop-blur-sm` a `backdrop-blur-3xl`, útil para overlays con efecto vidrio esmerilado.

Las transiciones: `transition` (aplica a propiedades comunes), `transition-all`, `transition-colors`, `transition-opacity`, `transition-shadow`, `transition-transform`. Duración: `duration-75`, `duration-100`, `duration-150`, `duration-200`, `duration-300`, `duration-500`, `duration-700`, `duration-1000`. Easing: `ease-linear`, `ease-in`, `ease-out`, `ease-in-out`. Delay: `delay-75` a `delay-1000`. Animaciones predefinidas: `animate-spin` (rotación infinita), `animate-ping` (escala y fade, notificaciones), `animate-pulse` (opacidad oscilante, skeleton loaders), `animate-bounce` (rebote). Personalización de keyframes en @theme.

El modo oscuro usa el prefijo `dark:`. Dos estrategias: `@media (prefers-color-scheme: dark)` (automática según SO) y selector `.dark` (manual con toggle JS). La recomendada es la de clase, que permite toggle independiente. Implementación: añadir/quitar clase `dark` en `<html>` con JS, persistir en localStorage. Ejemplo: `<body class="bg-white dark:bg-gray-900 text-gray-900 dark:text-white transition-colors duration-300">`. La transición `transition-colors duration-300` suaviza el cambio entre temas, mejorando la experiencia de usuario.

### 11. Valores arbitrarios y personalización

!!! tip "Regla práctica: valor arbitrario vs. token de diseño"
    **Si un valor arbitrario aparece una sola vez**, está bien; **si se repite**, debe extraerse a un *token* de diseño en `@theme`.

Tailwind ofrece un mecanismo de escape: los **valores arbitrarios** mediante notación de corchetes `[]`. Permiten inyectar cualquier valor CSS directamente: `w-[300px]`, `bg-[#1a1a1a]`, `text-[clamp(1rem,2vw,2rem)]`, `grid-cols-[200px_minmax(900px,_1fr)_100px]`, `shadow-[0_4px_20px_rgba(0,0,0,0.3)]`. Esta característica cubre casos donde la escala predefinida no contempla un valor específico. Solo se genera la regla CSS **exacta** para el valor especificado, manteniendo el CSS final reducido.

La configuración con @theme en v4 permite extender o sobrescribir cualquier parte del sistema:

```css
@import "tailwindcss";
@theme {
  --color-accent: #ff6b35;
  --font-size-display: 3.5rem;
  --font-size-display--line-height: 4rem;
  --spacing-section: 6rem;
  --radius-card: 1rem;
}
```

Esta configuración CSS-first es una de las grandes ventajas de Tailwind v4, eliminando la necesidad de un archivo JS de configuración separado.

