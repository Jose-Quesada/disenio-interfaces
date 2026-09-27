# Unidad 12: Integración de Contenido Multimedia en la Web

## Objetivos de aprendizaje

Al finalizar esta unidad, el alumnado será capaz de integrar, optimizar y gestionar contenido multimedia en interfaces web de forma profesional. Los objetivos concretos son: seleccionar el formato de imagen adecuado (JPEG, PNG, SVG, WebP, AVIF) para cada contexto, justificando la elección en función de las necesidades de compresión, transparencia, escalabilidad y rendimiento; optimizar imágenes web aplicando técnicas de compresión, redimensionamiento y carga diferida mediante herramientas como Squoosh, Sharp y los atributos nativos `loading="lazy"` y `decoding="async"`; implementar imágenes responsive completas utilizando `srcset`, `sizes` y el elemento `picture` con múltiples fuentes para diferentes resoluciones, formatos y dirección artística; integrar contenido de audio en páginas web usando el elemento `<audio>` con sus atributos y controles, seleccionando el formato adecuado (MP3, AAC, OGG) según la compatibilidad requerida; integrar contenido de vídeo usando el elemento `<video>` con sus atributos de reproducción, subtítulos mediante el elemento `<track>` con archivos WebVTT, y técnicas de embedding responsive para vídeos de YouTube y Vimeo; crear animaciones CSS mediante `@keyframes` y transiciones para enriquecer la experiencia de usuario, aplicando curvas de easing y propiedades aceleradas por GPU; desarrollar animaciones SVG tanto con CSS (animaciones de trazado, stroke-dasharray) como con herramientas profesionales (Lottie/Bodymovin); aplicar buenas prácticas de rendimiento multimedia incluyendo `will-change`, `prefers-reduced-motion`, `requestAnimationFrame` y compresión de recursos; diseñar microinteracciones que mejoren la usabilidad sin sobrecargar la interfaz; y analizar estrategias multimedia de sitios web profesionales para fundamentar las decisiones de diseño propias.

## Relación con los Resultados de Aprendizaje

Esta unidad aborda el Resultado de Aprendizaje 4 del módulo 0615 Diseño de Interfaces Web según el currículo oficial andaluz de DAW: "integrar contenido multimedia en las interfaces web, aplicando criterios de usabilidad y accesibilidad". Los criterios de evaluación vinculados son: CE 4.a ("identificar los formatos de archivos multimedia adecuados para la web"), CE 4.b ("aplicar técnicas de optimización de archivos multimedia para reducir su peso"), CE 4.c ("integrar elementos multimedia en las páginas web utilizando las etiquetas HTML apropiadas"), CE 4.d ("aplicar criterios de accesibilidad a los contenidos multimedia, proporcionando alternativas textuales y subtítulos"), y CE 4.e ("verificar que los elementos multimedia se visualizan correctamente en diferentes navegadores y dispositivos"). Esta unidad conecta directamente con el módulo de Desarrollo Web en Entorno Cliente, donde se programarán interacciones multimedia complejas con JavaScript, y con el módulo de Desarrollo Web en Entorno Servidor, donde se gestionará la subida, almacenamiento y servicio de archivos multimedia. La competencia profesional asociada es la capacidad de crear experiencias web ricas y accesibles que integren armoniosamente texto, imagen, audio, vídeo y animación optimizados para el contexto de consumo del usuario.

## Conocimientos previos

El alumnado debe dominar HTML semántico y las etiquetas básicas de medios (`<img>`, `<figure>`, `<figcaption>`). Debe conocer CSS fundamental incluyendo selectores avanzados, pseudo-clases (`:hover`, `:focus`, `:active`), transiciones básicas (`transition`) y transformaciones 2D (`transform: translate, scale, rotate`). Se requiere comprensión de los conceptos de diseño responsive (media queries, viewport, Mobile First) para entender la integración multimedia en contextos adaptables. Es necesario conocer los principios de accesibilidad web (alternativas textuales con `alt`, contraste de color) ya que el contenido multimedia presenta desafíos de accesibilidad específicos. El alumnado debe estar familiarizado con las herramientas de desarrollo del navegador (Chrome DevTools) para depurar la carga de recursos multimedia (pestaña Network). Son recomendables nociones básicas de edición de imágenes (recorte, redimensionado) aunque no se requiere software específico. Para la sección de animaciones es útil comprender el concepto de fotogramas y línea de tiempo.

## Contenidos

1. **Formatos de imagen para web**: JPEG (compresión con pérdida, fotografías), PNG (sin pérdida, transparencia, capturas de pantalla), SVG (vectorial, escalable, animable), WebP (compresión superior, lossy+lossless+alpha), AVIF (última generación, máxima compresión). Tabla comparativa con casos de uso, ventajas y limitaciones de cada formato.

2. **Optimización de imágenes**: Compresión con pérdida vs sin pérdida. Herramientas: Squoosh (online, visual), TinyPNG (compresión PNG/JPEG), ImageOptim (escritorio), Sharp (librería Node.js para automatización). Dimensiones correctas (no cargar imágenes más grandes de lo necesario). Lazy loading nativo (`loading="lazy"`). Decodificación asíncrona (`decoding="async"`). Fetch Priority (`fetchpriority`).

3. **SVG en profundidad**: Creación y edición de SVG (herramientas: Inkscape, Illustrator, Figma). Optimización con SVGO (eliminación de metadatos, comentarios, precisión innecesaria). Métodos de inserción en HTML: inline (acceso a elementos internos con CSS/JS), etiqueta `<img>` (simple, cacheable), CSS `background-image`, etiqueta `<object>`. Sprites SVG. Animación de SVG con CSS.

4. **Imágenes responsive avanzadas**: `srcset` con descriptores `w` (ancho) y `x` (densidad). Atributo `sizes` con media conditions. Elemento `<picture>` con múltiples `<source>` para diferentes formatos y breakpoints. Art direction: diferentes recortes/composiciones según el dispositivo. Imágenes de fondo responsive con `image-set()`.

5. **Audio en la web**: Formatos de audio (MP3, AAC, OGG Vorbis, WAV). Tabla comparativa de compatibilidad, compresión y calidad. Etiqueta `<audio>`: atributos `controls`, `autoplay`, `loop`, `muted`, `preload`. Múltiples fuentes con `<source>` para compatibilidad cruzada. Accesibilidad: transcripciones textuales, controles accesibles, descripciones de audio.

6. **Vídeo en la web**: Formatos de vídeo (MP4/H.264, WebM/VP8-VP9, OGG/Theora). Códecs y contenedores: diferencia y relación. Etiqueta `<video>`: atributos `controls`, `poster`, `preload`, `autoplay` (con `muted` + `playsinline` para móvil). Múltiples fuentes con `<source>`. Optimización con FFmpeg (compresión, resolución, bitrate). Streaming adaptativo (HLS, DASH). CDN para vídeo.

7. **Accesibilidad multimedia**: Subtítulos con `<track kind="subtitles">` y archivos WebVTT. Descripciones de audio (`<track kind="descriptions">`). Transcripciones textuales completas. Capítulos en vídeos largos. Controles accesibles por teclado.

8. **Embedding de vídeo externo**: YouTube, Vimeo (iframe). Truco del padding-bottom 56.25% para mantener relación de aspecto 16:9. Atributos de URL para personalizar la reproducción (autoplay, controles, inicio). Consideraciones de privacidad (modo de privacidad mejorada de YouTube).

9. **CSS Animations**: Regla `@keyframes`. Propiedades de animación: `animation-name`, `animation-duration`, `animation-delay`, `animation-timing-function`, `animation-iteration-count`, `animation-direction`, `animation-fill-mode`, `animation-play-state`. Curvas de easing: `ease`, `linear`, `ease-in`, `ease-out`, `ease-in-out`, `cubic-bezier()`. Función `steps()` para animaciones frame a frame.

10. **CSS Transitions**: Propiedades animables. Triggers (hover, focus, clase). `transition-property`, `transition-duration`, `transition-timing-function`, `transition-delay`. Ejemplos prácticos: botones, menús, modales.

11. **Rendimiento en animaciones**: `will-change` (avisar al navegador de cambios futuros). Propiedades aceleradas por GPU: `transform` y `opacity`. Evitar animar propiedades que causan layout/paint. `requestAnimationFrame` para animaciones JavaScript. `prefers-reduced-motion` para respetar preferencias del usuario.

12. **Lottie y animaciones vectoriales**: Qué es Lottie (librería de Airbnb). Flujo de trabajo: After Effects + extensión Bodymovin -> archivo JSON -> reproducción web. Uso con lottie-web y lottie-react. Ventajas: ligero, escalable, interactivo, complejidad ilimitada.

13. **Microinteracciones**: Definición, propósito en UX, ejemplos prácticos (botón like animado, notificaciones, pull-to-refresh, skeleton loaders, confirmación visual de acciones).

## Desarrollo teórico

### 1. Formatos de imagen para la web

La elección del formato de imagen es una decisión de diseño que impacta directamente en el rendimiento, la calidad visual y la experiencia del usuario. Los formatos se dividen en dos grandes familias:

- **Raster** — mapas de bits, formados por píxeles.
- **Vectoriales** — formas geométricas definidas matemáticamente.

**JPEG (Joint Photographic Experts Group)** es el formato con pérdida (lossy) más extendido para fotografías. Alcanza ratios de compresión de **10:1 a 20:1** con pérdida de calidad apenas perceptible, lo que lo hace ideal para imágenes con muchos colores y gradientes (fotos de paisajes, retratos, productos). No soporta transparencia ni animación. El formato progresivo (progressive JPEG) permite una carga incremental: primero se muestra una versión borrosa que se va refinando, mejorando la percepción de velocidad.

**PNG (Portable Network Graphics)** es sin pérdida (lossless), lo que garantiza fidelidad absoluta al original a costa de archivos más pesados. Soporta transparencia total (canal alpha) con 256 niveles de opacidad (PNG-24) o transparencia binaria (PNG-8). Es el formato ideal para capturas de pantalla, logotipos, iconos, ilustraciones con áreas planas de color y cualquier imagen que requiera texto nítido. No está pensado para fotografías (el tamaño sería excesivo).

**SVG (Scalable Vector Graphics)** es un formato vectorial basado en XML. Al ser vectorial, escala infinitamente sin pérdida de calidad, lo que lo hace perfecto para iconos, logotipos, ilustraciones y gráficos. Los archivos SVG son texto y por tanto pueden editarse con cualquier editor de código, comprimirse con gzip, e indexarse por buscadores. Soportan animación y pueden incluir interactividad mediante CSS y JavaScript. Su tamaño es independiente de las dimensiones de visualización.

**WebP** es un formato moderno desarrollado por Google que ofrece compresión superior tanto en modo lossy (vs JPEG) como en modo lossless (vs PNG). Reduce el tamaño de archivo entre un **25%** y un **35%** respecto a JPEG con calidad equivalente. Soporta transparencia (canal alpha) y animación, lo que lo convierte en un reemplazo universal. Está soportado por el **97%** de los navegadores actuales. Su principal inconveniente es que herramientas como Photoshop no lo soportan nativamente sin plugins.

**AVIF (AV1 Image File Format)** es el formato más moderno, basado en el códec de vídeo AV1. Ofrece compresión aún mejor que WebP (**20-30%** adicional) con calidad sobresaliente. Soporta HDR, profundidad de color de **12 bits**, transparencia y animación. El soporte en navegadores es bueno (**>93%**) pero inferior al de WebP. Es el formato recomendado para proyectos que prioricen el rendimiento sobre la compatibilidad absoluta.

| Formato | Compresión | Transparencia | Animación | Uso ideal |
|---------|------------|---------------|-----------|-----------|
| **JPEG** | Con pérdida (**10:1** a **20:1**) | No | No | Fotografías con muchos colores y gradientes |
| **PNG** | Sin pérdida | Sí (canal alpha) | No | Capturas, logotipos, iconos e ilustraciones con áreas planas |
| **SVG** | Vectorial (escala sin pérdida) | Sí | Sí | Iconos, logotipos, ilustraciones y gráficos |
| **WebP** | Con pérdida y sin pérdida (**25-35%** menos que JPEG) | Sí (canal alpha) | Sí | Reemplazo universal (soporte del **97%** de los navegadores) |
| **AVIF** | Con pérdida (mejor que WebP, **20-30%** adicional) | Sí | Sí | Prioridad al rendimiento (soporte **>93%**) |

!!! tip "Estrategia de formatos"
    La estrategia recomendada es servir **AVIF** a navegadores que lo soporten, **WebP** como fallback, y **JPEG/PNG** como último recurso, usando el elemento `<picture>`.

### 2. Optimización de imágenes web

Las imágenes suelen representar entre el **50%** y el **70%** del peso total de una página web, por lo que su optimización tiene un impacto directo y significativo en el rendimiento. La optimización abarca varias dimensiones:

!!! tip "Técnicas de optimización"
    - **Dimensiones correctas** — el error más común es servir imágenes con dimensiones mayores que el espacio que ocupan en pantalla. Si una imagen se muestra a **400px** de ancho, no debe cargarse a **2000px**. Las herramientas de desarrollo permiten ver el tamaño «intrínseco» vs «renderizado» de cada imagen. La solución es generar variantes de cada imagen a diferentes resoluciones y servirlas mediante `srcset`.
    - **Compresión** — la compresión lossy (JPEG, WebP lossy) descarta información visual que el ojo humano apenas percibe, logrando reducciones drásticas de tamaño. Herramientas como Squoosh permiten ajustar interactivamente el nivel de compresión y comparar visualmente el resultado con el original. La compresión lossless (PNG, WebP lossless) reduce el tamaño reorganizando los datos sin perder un solo píxel, mediante técnicas como la eliminación de metadatos EXIF, la reducción de la paleta de colores (en PNG-8) y la optimización de los algoritmos de compresión.
    - **Lazy loading** — el atributo nativo `loading="lazy"` en etiquetas `<img>` e `<iframe>` indica al navegador que posponga la carga de ese recurso hasta que esté próximo a entrar en el viewport. Esto reduce el tiempo de carga inicial y ahorra ancho de banda (especialmente importante en conexiones móviles). Para casos más avanzados (como carga bajo demanda controlada por JavaScript), se usa la API Intersection Observer.
    - **Decodificación asíncrona** — `decoding="async"` permite que el navegador decodifique la imagen en segundo plano sin bloquear el renderizado del resto de la página. Es útil para imágenes grandes fuera del viewport inicial.
    - **Priorización** — `fetchpriority="high"` en la imagen del héroe (LCP - Largest Contentful Paint) le dice al navegador que la cargue con máxima prioridad, mejorando la métrica LCP de Core Web Vitals. `fetchpriority="low"` en imágenes no críticas evita que compitan por ancho de banda con recursos más importantes.
    - **Automatización** — para proyectos profesionales, la optimización debe automatizarse. Sharp (Node.js) permite redimensionar, comprimir y convertir formatos por lotes. Herramientas de build como Vite o Webpack pueden integrar plugins que optimizan imágenes durante la construcción del proyecto.

### 3. SVG en profundidad

!!! info "SVG: formato vectorial para la web"
    SVG merece un tratamiento extenso por sus capacidades únicas como formato vectorial para la web. A diferencia de los formatos raster, SVG describe gráficos mediante primitivas geométricas: rectángulos, círculos, elipses, líneas, polígonos, trazados (paths), y texto. Como está basado en **XML**, un archivo SVG es legible y editable, lo que abre posibilidades que los formatos raster no tienen.

La **creación de SVG** puede realizarse con editores vectoriales (**Inkscape** - gratuito, **Illustrator** - profesional, **Figma** - colaborativo) o directamente escribiendo el código XML. La optimización con **SVGO** elimina información innecesaria (metadatos de editor, comentarios, precisión decimal excesiva, espacios en blanco) reduciendo típicamente el tamaño entre un **20%** y un **50%**.

Los **métodos de inserción** de SVG en HTML determinan qué se puede hacer con él:

- **Inline** — pegando el código SVG directamente en el HTML permite acceder a cada elemento interno con CSS y JavaScript para animar colores, formas y transformaciones, siendo el método más potente.
- **`<img src="icono.svg">`** — es el más simple pero no permite manipular elementos internos, aunque sí se beneficia del almacenamiento en caché del navegador.
- **`background-image: url(icono.svg)`** — funciona igual que `<img>`.
- **`<object>`** — permite incluir SVG externos con cierto nivel de interacción pero su comportamiento es inconsistente entre navegadores.

!!! tip "Sprites SVG"
    Los **sprites SVG** son una técnica para combinar múltiples iconos en un solo archivo, similar a los sprites de imágenes tradicionales. Mediante `<symbol>` y `<use>`, se definen los iconos una vez y se referencian múltiples veces en la página, ahorrando peticiones HTTP y permitiendo cambiar colores mediante la propiedad `fill` heredada con `currentColor`.

### 4. Audio en la web

El audio en la web ha evolucionado desde los molestos reproductores automáticos de los años 90 hasta experiencias controladas y accesibles. El elemento `<audio>` de HTML5 proporciona una forma nativa y semántica de incluir audio sin necesidad de plugins.

Los **formatos de audio** principales son:

| Formato | Características | Soporte |
|---------|-----------------|---------|
| **MP3** (MPEG-1 Audio Layer 3) | El más universal, con buena compresión | Absolutamente todos los navegadores |
| **AAC** (Advanced Audio Coding) | Mejor calidad que MP3 a la misma tasa de bits | Formato preferido por Apple |
| **OGG Vorbis** | Código abierto sin patentes | Firefox y Chrome, pero no Safari |
| **WAV** | Sin compresión, fiel al original, archivos enormes | Solo para casos donde la calidad sin pérdida sea imprescindible |

La etiqueta `<audio>` acepta los atributos:

- **`controls`** — muestra los controles nativos del navegador (play/pause, volumen, progreso).
- **`autoplay`** — reproducción automática, bloqueado por la mayoría de navegadores si no va acompañado de `muted`.
- **`loop`** — repetición continua.
- **`muted`** — silenciado.
- **`preload`** — `none`/`metadata`/`auto`: controla cuánto contenido se precarga.

Para máxima compatibilidad, se proporcionan múltiples fuentes dentro de `<audio>` con elementos `<source>` en diferentes formatos: primero **OGG** (menor tamaño), luego **MP3** (compatibilidad universal).

!!! tip "Accesibilidad del audio"
    La **accesibilidad** del audio requiere transcripciones textuales completas del contenido hablado, que deben colocarse cerca del reproductor. Para contenidos de audio complejos (podcasts con múltiples interlocutores), la transcripción debe identificar quién habla. Los controles nativos del navegador son generalmente accesibles por teclado, pero los reproductores personalizados deben implementar cuidadosamente la navegación por teclado, etiquetas ARIA y gestión del foco.

### 5. Vídeo en la web

El vídeo es el contenido más complejo y pesado de servir en la web, pero también uno de los más efectivos para comunicación y marketing. El elemento `<video>` de HTML5, al igual que `<audio>`, proporciona reproducción nativa.

!!! info "Códec vs contenedor"
    Los **códecs y contenedores** son conceptos que a menudo se confunden. El **contenedor** (MP4, WebM, OGG) es el formato del archivo que agrupa las pistas de vídeo, audio, subtítulos y metadatos. El **códec** (H.264, VP8, VP9, AV1, Theora) es el algoritmo que comprime y descomprime cada pista. Un archivo **MP4** típicamente contiene vídeo codificado con **H.264** y audio con **AAC**. Un archivo **WebM** contiene vídeo **VP8/VP9** y audio **OGG Vorbis/Opus**.

La combinación más compatible es **MP4 con H.264 + AAC**, soportada por todos los navegadores. **WebM con VP8/VP9** ofrece mejor compresión y es de código abierto, pero Safari no lo soporta (aunque sí soporta WebM desde 2021). La recomendación es proporcionar ambos formatos: `<source src="video.webm" type="video/webm">` seguido de `<source src="video.mp4" type="video/mp4">`.

La **optimización de vídeo** con FFmpeg permite controlar:

- **Resolución** — escalar a **1080p**, **720p** o **480p** según necesidad.
- **Bitrate** — menor bitrate = menor tamaño pero menor calidad.
- **Códec** y **fotogramas por segundo**.
- **Fotogramas clave** — para extraer el poster.

El **streaming adaptativo** (HLS de Apple o DASH estándar) divide el vídeo en segmentos y ofrece múltiples calidades, permitiendo al reproductor cambiar dinámicamente según la conexión del usuario. Servir vídeo desde una **CDN** reduce la latencia y mejora la experiencia global.

!!! tip "Vídeo responsive"
    Para **vídeo responsive**, el truco del `padding-bottom` **56.25%** (9/16 = 56.25%) crea un contenedor con relación de aspecto fija que se adapta a cualquier ancho: el contenedor padre tiene `position: relative; padding-bottom: 56.25%`, y el `<iframe>` o `<video>` interno tiene `position: absolute; width: 100%; height: 100%`.

### 6. Accesibilidad en contenido multimedia

!!! warning "Requisito legal y ético"
    La accesibilidad del contenido multimedia es un **requisito legal** (**Real Decreto 1112/2018** en España, que transpone la Directiva Europea **2016/2102**) y ético. Para vídeos, el elemento `<track>` permite asociar archivos de subtítulos en formato WebVTT: `<track kind="subtitles" src="subtitulos.vtt" srclang="es" label="Español" default>`. **WebVTT** es un formato de texto plano que asocia cada línea de subtítulo con un rango de tiempo. Los subtítulos no solo ayudan a personas sordas o con dificultades auditivas, sino también a quienes ven el vídeo en entornos ruidosos o sin auriculares.

Además de subtítulos, existen:

- **Descripciones de audio** (`kind="descriptions"`) — narraciones que describen lo que sucede visualmente para personas ciegas.
- **Capítulos** (`kind="chapters"`) — permiten navegar por secciones del vídeo.
- **Transcripciones textuales completas** — texto íntegro del contenido hablado más descripciones de las acciones visuales; deben proporcionarse como contenido HTML junto al vídeo, beneficiando también al SEO.

Para audio, la accesibilidad se centra en las transcripciones y en garantizar que los controles del reproductor sean operables por teclado y lectores de pantalla. Para imágenes, el atributo `alt` proporciona texto alternativo que los lectores de pantalla leen en lugar de la imagen. Las imágenes decorativas deben usar **`alt=""`** (vacío, no ausente) para que los lectores las ignoren.

### 7. CSS Animations y Transitions

Las animaciones CSS permiten crear movimiento y dinamismo en las interfaces web sin necesidad de JavaScript, aprovechando la aceleración por hardware del navegador para un rendimiento óptimo.

!!! info "Transiciones vs animaciones"
    Las **transiciones** (`transition`) suavizan el cambio entre dos estados de un elemento. Se disparan cuando una propiedad CSS cambia de valor (típicamente por eventos como `:hover`, `:focus`, o al añadir/quitar una clase con JavaScript). La sintaxis es: `transition: propiedad duración timing-function retraso`. Se puede animar la mayoría de propiedades CSS, pero **`transform`** y **`opacity`** son las más eficientes porque solo requieren composición por GPU, sin necesidad de recalcular el layout o repintar.

    Las **animaciones** (`animation` + `@keyframes`) permiten secuencias complejas independientes de eventos. La regla `@keyframes` define los estados intermedios de la animación mediante porcentajes de progreso (**0%** = inicio, **100%** = final). Las propiedades de `animation` controlan la duración, el retraso, la función de aceleración, el número de iteraciones, la dirección, el modo de relleno (cómo se ve el elemento antes/después de la animación) y el estado de reproducción.

Las **curvas de easing** definen cómo progresa la animación en el tiempo:

- **`linear`** — velocidad constante.
- **`ease`** (por defecto) — acelera al principio y decelera al final.
- **`ease-in`** — acelera progresivamente.
- **`ease-out`** — decelera progresivamente.
- **`ease-in-out`** — combina ambas.
- **`cubic-bezier()`** — permite crear curvas personalizadas.
- **`steps()`** — divide la animación en saltos discretos, útil para animaciones sprite (como un personaje caminando).

### 8. Rendimiento en animaciones

No todas las propiedades CSS son iguales en términos de rendimiento de animación. El navegador pasa por tres etapas al renderizar cambios: **Layout** (recalcular posiciones y tamaños), **Paint** (rellenar píxeles), y **Composite** (ensamblar capas en pantalla).

| Propiedades | Etapas del renderizado | Coste |
|-------------|------------------------|-------|
| `width`, `height`, `margin`, `padding` | Layout + Paint + Composite | El más alto: fuerzan las tres etapas |
| `color`, `background-color`, `box-shadow` | Paint + Composite | Medio |
| `transform` (translate, scale, rotate), `opacity` | Composite | El más bajo: el navegador las maneja en una capa separada de la GPU |

La propiedad **`will-change`** avisa al navegador de que un elemento va a cambiar, permitiéndole crear una capa de GPU anticipadamente: `will-change: transform, opacity`. Debe usarse con **moderación** (no aplicar a todos los elementos) y solo cuando la animación es inminente, ya que cada capa GPU consume memoria.

!!! warning "prefers-reduced-motion"
    La media query `prefers-reduced-motion: reduce` es fundamental para accesibilidad. Los usuarios pueden configurar su sistema operativo para reducir animaciones (por trastornos vestibulares, migrañas o simple preferencia). Respetar esta preferencia es **tan importante como respetar el modo oscuro**. La implementación típica desactiva o reduce drásticamente las animaciones.

### 9. Lottie y animaciones vectoriales

!!! info "Lottie"
    **Lottie** es una librería de código abierto creada por **Airbnb** que renderiza animaciones exportadas desde Adobe After Effects en tiempo real. El flujo de trabajo es: un diseñador crea una animación en After Effects, la exporta como **JSON** usando la extensión gratuita **Bodymovin**, y el desarrollador la reproduce en la web usando **lottie-web** (para vanilla JS) o **lottie-react** (para React).

Las ventajas sobre otros formatos de animación son significativas:

- **Extremadamente ligeros** — los archivos JSON de Lottie pesan unos pocos KB frente a los cientos de KB o MB de un GIF o vídeo equivalente.
- **Vectoriales** — la animación escala infinitamente.
- **Interactivas** — se puede controlar la reproducción, velocidad y dirección programáticamente.
- **Calidad profesional** — las mismas animaciones que verías en una app nativa.

Lottie se usa extensivamente en apps como **Uber**, **Google Pay**, **Duolingo** y muchas más para iconos animados, pantallas de carga, onboarding, y microinteracciones complejas.

## Ejemplos guiados

### Ejemplo Guiado 1: Galería de imágenes con lazy loading y formatos modernos

!!! example "Contexto pedagógico"
    Implementación de una galería que optimiza la carga mediante lazy loading nativo, usa WebP/AVIF con fallback, y aplica dimensiones correctas con srcset. Incluye placeholders que ocupan espacio para evitar layout shift.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ejemplo 1 - Galería Optimizada</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      background: #f5f5f5;
      padding: 2rem;
    }

    h1 { text-align: center; margin-bottom: 2rem; }

    /*
     * ===== GALERÍA CON GRID RESPONSIVE =====
     * repeat(auto-fill, minmax(300px, 1fr)):
     * Crea tantas columnas como quepan con mínimo 300px.
     * Las imágenes se adaptan fluidamente al ancho disponible.
     */
    .gallery {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
      gap: 1rem;
      max-width: 1200px;
      margin: 0 auto;
    }

    /*
     * ===== TARJETA DE IMAGEN =====
     * Cada imagen está dentro de una tarjeta con sombra y bordes redondeados.
     * El contenedor tiene position: relative para el overlay.
     */
    .gallery__item {
      position: relative;
      border-radius: 12px;
      overflow: hidden;
      box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
      background: #e0e0e0;
      /*
       * ASPECT RATIO: 4/3 = 75% de padding-bottom.
       * Esto reserva espacio antes de que la imagen cargue,
       * evitando cambios bruscos de layout (CLS).
       * aspect-ratio es moderno; padding-bottom es fallback.
       */
      aspect-ratio: 4 / 3;
    }

    /*
     * La imagen ocupa todo el espacio de la tarjeta.
     * object-fit: cover recorta la imagen para llenar el contenedor
     * sin distorsionarse, manteniendo su relación de aspecto.
     */
    .gallery__img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      /*
       * Transición suave cuando la imagen termina de cargar.
       * La imagen empieza con opacity: 0 (definido en el HTML inline)
       * y transiciona a opacity: 1 al completar la carga.
       */
      transition: opacity 0.4s ease;
    }

    /*
     * Overlay informativo que aparece al hacer hover.
     * Muestra el título y la descripción de la imagen.
     */
    .gallery__overlay {
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      background: linear-gradient(transparent, rgba(0,0,0,0.7));
      color: #fff;
      padding: 2rem 1rem 1rem;
      transform: translateY(100%); /* Oculto debajo de la imagen */
      transition: transform 0.3s ease;
    }

    .gallery__item:hover .gallery__overlay {
      transform: translateY(0); /* Desliza hacia arriba al hacer hover */
    }

    .gallery__overlay h3 { font-size: 1.1rem; margin-bottom: 0.25rem; }
    .gallery__overlay p { font-size: 0.85rem; opacity: 0.8; }

    /* Indicador de carga visible mientras la imagen no ha terminado */
    .gallery__loader {
      position: absolute;
      inset: 0;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #999;
      font-size: 0.9rem;
    }
  </style>
</head>
<body>
  <h1>Galería de imágenes optimizada</h1>
  <div class="gallery">
    <!--
      ===== TARJETA 1: IMAGEN RESPONSIVE CON WEBP =====
      - picture: permite múltiples sources con condiciones
      - El source WebP se sirve si el navegador lo soporta
      - El img con JPEG es el fallback universal
      - srcset con descriptores w: el navegador elige la resolución
      - sizes: informa del tamaño de renderizado según el viewport
      - loading="lazy": carga diferida, solo cuando está cerca del viewport
      - decoding="async": decodificación en segundo plano
    -->
    <div class="gallery__item">
      <span class="gallery__loader">Cargando...</span>
      <picture>
        <!-- Formato WebP para navegadores que lo soportan -->
        <source
          srcset="foto-1-400.webp 400w, foto-1-800.webp 800w, foto-1-1200.webp 1200w"
          sizes="(max-width: 600px) 100vw, (max-width: 900px) 50vw, 33vw"
          type="image/webp"
        >
        <!-- Fallback JPEG universal -->
        <img
          src="foto-1-400.jpg"
          srcset="foto-1-400.jpg 400w, foto-1-800.jpg 800w, foto-1-1200.jpg 1200w"
          sizes="(max-width: 600px) 100vw, (max-width: 900px) 50vw, 33vw"
          alt="Paisaje montañoso al atardecer con reflejos en el lago"
          class="gallery__img"
          loading="lazy"
          decoding="async"
          width="400"
          height="300"
          onload="this.style.opacity='1'; this.previousElementSibling.style.display='none'"
          style="opacity: 0;"
        >
      </picture>
      <div class="gallery__overlay">
        <h3>Atardecer en los Alpes</h3>
        <p>Naturaleza · Suiza · 2024</p>
      </div>
    </div>

    <!-- Tarjeta 2 (misma estructura, diferentes imágenes) -->
    <div class="gallery__item">
      <span class="gallery__loader">Cargando...</span>
      <picture>
        <source srcset="foto-2-400.webp 400w, foto-2-800.webp 800w" sizes="(max-width: 600px) 100vw, 50vw" type="image/webp">
        <img src="foto-2-400.jpg" srcset="foto-2-400.jpg 400w, foto-2-800.jpg 800w" sizes="(max-width: 600px) 100vw, 50vw" alt="Arquitectura moderna con líneas geométricas" class="gallery__img" loading="lazy" decoding="async" width="400" height="300" onload="this.style.opacity='1'; this.previousElementSibling.style.display='none'" style="opacity: 0;">
      </picture>
      <div class="gallery__overlay">
        <h3>Arquitectura contemporánea</h3>
        <p>Arquitectura · Japón · 2024</p>
      </div>
    </div>

    <!-- Tarjeta 3 -->
    <div class="gallery__item">
      <span class="gallery__loader">Cargando...</span>
      <picture>
        <source srcset="foto-3-400.webp 400w, foto-3-800.webp 800w" sizes="(max-width: 600px) 100vw, 50vw" type="image/webp">
        <img src="foto-3-400.jpg" srcset="foto-3-400.jpg 400w, foto-3-800.jpg 800w" sizes="(max-width: 600px) 100vw, 50vw" alt="Retrato en blanco y negro de persona mayor" class="gallery__img" loading="lazy" decoding="async" width="400" height="300" onload="this.style.opacity='1'; this.previousElementSibling.style.display='none'" style="opacity: 0;">
      </picture>
      <div class="gallery__overlay">
        <h3>Sabiduría ancestral</h3>
        <p>Retratos · Perú · 2024</p>
      </div>
    </div>

    <!-- Tarjetas 4-6 con el mismo patrón -->
    <div class="gallery__item">
      <span class="gallery__loader">Cargando...</span>
      <picture>
        <source srcset="foto-4-400.webp 400w, foto-4-800.webp 800w" sizes="(max-width: 600px) 100vw, 50vw" type="image/webp">
        <img src="foto-4-400.jpg" srcset="foto-4-400.jpg 400w, foto-4-800.jpg 800w" sizes="(max-width: 600px) 100vw, 50vw" alt="Mercado callejero con puestos de especias" class="gallery__img" loading="lazy" decoding="async" width="400" height="300" onload="this.style.opacity='1'; this.previousElementSibling.style.display='none'" style="opacity: 0;">
      </picture>
      <div class="gallery__overlay">
        <h3>Mercado de especias</h3>
        <p>Viajes · Marruecos · 2024</p>
      </div>
    </div>

    <div class="gallery__item">
      <span class="gallery__loader">Cargando...</span>
      <picture>
        <source srcset="foto-5-400.webp 400w, foto-5-800.webp 800w" sizes="(max-width: 600px) 100vw, 50vw" type="image/webp">
        <img src="foto-5-400.jpg" srcset="foto-5-400.jpg 400w, foto-5-800.jpg 800w" sizes="(max-width: 600px) 100vw, 50vw" alt="Olas del océano rompiendo contra las rocas" class="gallery__img" loading="lazy" decoding="async" width="400" height="300" onload="this.style.opacity='1'; this.previousElementSibling.style.display='none'" style="opacity: 0;">
      </picture>
      <div class="gallery__overlay">
        <h3>Furia del océano</h3>
        <p>Naturaleza · Portugal · 2024</p>
      </div>
    </div>

    <div class="gallery__item">
      <span class="gallery__loader">Cargando...</span>
      <picture>
        <source srcset="foto-6-400.webp 400w, foto-6-800.webp 800w" sizes="(max-width: 600px) 100vw, 50vw" type="image/webp">
        <img src="foto-6-400.jpg" srcset="foto-6-400.jpg 400w, foto-6-800.jpg 800w" sizes="(max-width: 600px) 100vw, 50vw" alt="Bosque de bambú con rayos de sol filtrándose" class="gallery__img" loading="lazy" decoding="async" width="400" height="300" onload="this.style.opacity='1'; this.previousElementSibling.style.display='none'" style="opacity: 0;">
      </picture>
      <div class="gallery__overlay">
        <h3>Bosque de bambú</h3>
        <p>Naturaleza · Japón · 2023</p>
      </div>
    </div>
  </div>
</body>
</html>
```


### Ejemplo Guiado 2: Reproducción de audio y vídeo HTML5 con accesibilidad

!!! example "Contexto pedagógico"
    Ejemplo completo que demuestra la integración de audio y vídeo usando las etiquetas nativas de HTML5, con múltiples formatos para compatibilidad, subtítulos WebVTT accesibles, y el truco del padding-bottom para hacer el vídeo responsive.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ejemplo 2 - Audio y Vídeo HTML5</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      max-width: 800px;
      margin: 0 auto;
      padding: 2rem;
      background: #f8f9fa;
    }

    h1 { margin-bottom: 2rem; color: #1a1a2e; }
    section { background: #fff; padding: 1.5rem; border-radius: 12px; margin-bottom: 2rem; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }
    h2 { margin-bottom: 1rem; color: #333; font-size: 1.3rem; }

    /*
     * ===== VÍDEO RESPONSIVE =====
     * Truco del padding-bottom para mantener relación de aspecto 16:9.
     * Calculo: (9 / 16) * 100 = 56.25%
     * El contenedor tiene altura 0 + padding-bottom que fuerza la proporción.
     * El vídeo se posiciona absolutamente dentro ocupando todo el espacio.
     */
    .video-container {
      position: relative;
      padding-bottom: 56.25%; /* 16:9 */
      height: 0;
      overflow: hidden;
      border-radius: 8px;
    }

    .video-container video,
    .video-container iframe {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      border: none;
    }

    /* Estilos para el elemento audio */
    audio {
      width: 100%;
      margin: 0.5rem 0;
    }

    /* Información de formatos */
    .format-info {
      font-size: 0.85rem;
      color: #666;
      margin-top: 0.5rem;
      padding: 0.75rem;
      background: #f0f0f0;
      border-radius: 6px;
    }

    code { background: #e0e0e0; padding: 0.15rem 0.4rem; border-radius: 3px; font-size: 0.9em; }

    .transcript {
      margin-top: 1rem;
      padding: 1rem;
      background: #f9f9f9;
      border-left: 3px solid #6c5ce7;
      max-height: 200px;
      overflow-y: auto;
      font-size: 0.9rem;
      line-height: 1.6;
    }
  </style>
</head>
<body>
  <h1>Audio y Vídeo en HTML5</h1>

  <!-- ===== SECCIÓN DE VÍDEO ===== -->
  <section>
    <h2>Reproductor de Vídeo con subtítulos</h2>

    <!--
      Contenedor responsive 16:9.
      El vídeo se adapta a cualquier ancho manteniendo la proporción.
    -->
    <div class="video-container">
      <!--
        ===== ETIQUETA VIDEO =====
        controls: muestra los controles nativos del navegador.
        poster: imagen mostrada antes de la reproducción.
        preload="metadata": solo carga metadatos (duración, dimensiones),
          no el vídeo completo. Opciones: none, metadata, auto.
        crossorigin="anonymous": necesario para que funcionen los subtítulos
          en algunos servidores.
      -->
      <video controls poster="video-poster.jpg" preload="metadata" crossorigin="anonymous">
        <!--
          Primero WebM (código abierto, mejor compresión).
          El navegador prueba cada source en orden y usa el primero que soporte.
        -->
        <source src="video.webm" type="video/webm">
        <!-- Fallback MP4/H.264 (compatibilidad universal) -->
        <source src="video.mp4" type="video/mp4">

        <!--
          ===== SUBTÍTULOS CON WEBVTT =====
          kind="subtitles": subtítulos que traducen el audio.
          srclang="es": idioma de los subtítulos.
          label: nombre mostrado en el selector de subtítulos.
          default: activa estos subtítulos por defecto.
        -->
        <track kind="subtitles" src="subtitulos-es.vtt" srclang="es" label="Español" default>
        <track kind="subtitles" src="subtitulos-en.vtt" srclang="en" label="English">

        <!-- Descripción de audio para personas ciegas -->
        <track kind="descriptions" src="descripciones-es.vtt" srclang="es" label="Descripción de audio">

        <!-- Mensaje si el navegador no soporta la etiqueta video -->
        <p>Tu navegador no soporta la etiqueta de vídeo HTML5.</p>
      </video>
    </div>

    <!--
      Ejemplo de archivo WebVTT (subtitulos-es.vtt):
      WEBVTT

      00:00:01.000 --> 00:00:04.000
      Bienvenidos a este tutorial sobre HTML5.

      00:00:04.500 --> 00:00:08.000
      Hoy aprenderemos a integrar vídeo en la web.
    -->

    <p class="format-info">
      Formatos proporcionados: <code>WebM (VP9)</code> para navegadores modernos,
      <code>MP4 (H.264)</code> como fallback universal.
      Subtítulos en español e inglés disponibles.
    </p>

    <!-- Transcripción textual completa (accesibilidad + SEO) -->
    <div class="transcript">
      <strong>Transcripción:</strong>
      <p>Bienvenidos a este tutorial sobre HTML5. Hoy aprenderemos a integrar
      vídeo en la web de forma nativa, sin necesidad de plugins externos.
      Veremos cómo usar la etiqueta video, cómo proporcionar múltiples formatos
      para compatibilidad, y cómo añadir subtítulos accesibles.</p>
    </div>
  </section>

  <!-- ===== SECCIÓN DE AUDIO ===== -->
  <section>
    <h2>Reproductor de Audio</h2>

    <!--
      ===== ETIQUETA AUDIO =====
      Estructura similar a video pero más simple.
      controls: muestra play/pause, volumen, progreso.
    -->
    <audio controls preload="metadata">
      <!-- Primero OGG Vorbis (código abierto) -->
      <source src="audio.ogg" type="audio/ogg">
      <!-- Fallback MP3 (compatibilidad universal) -->
      <source src="audio.mp3" type="audio/mpeg">
      <p>Tu navegador no soporta audio HTML5.</p>
    </audio>

    <p class="format-info">
      Formatos: <code>OGG Vorbis</code> (menor tamaño) +
      <code>MP3</code> (compatibilidad total).
      Atributo <code>preload="metadata"</code>: solo carga la duración, no el audio completo.
    </p>

    <div class="transcript">
      <strong>Transcripción del audio:</strong>
      <p>Este es un ejemplo de contenido de audio con su correspondiente
      transcripción textual. Proporcionar transcripciones no solo es un
      requisito de accesibilidad, sino que también mejora el SEO y
      permite a los usuarios consumir el contenido en entornos donde
      no pueden escuchar audio.</p>
    </div>
  </section>

  <!-- ===== SECCIÓN DE VÍDEO EMBEBIDO (YouTube/Vimeo) ===== -->
  <section>
    <h2>Vídeo embebido de YouTube (responsive)</h2>

    <!--
      Mismo truco de padding-bottom para iframe responsive.
      Funciona exactamente igual que con la etiqueta video.
    -->
    <div class="video-container">
      <!--
        El src de YouTube incluye parámetros:
        - rel=0: no mostrar vídeos relacionados al final
        - modestbranding=1: branding reducido
        - start=30: comenzar en el segundo 30
      -->
      <iframe
        src="https://www.youtube-nocookie.com/embed/dQw4w9WgXcQ?rel=0&modestbranding=1"
        title="Vídeo tutorial de ejemplo"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen
        loading="lazy"
      ></iframe>
    </div>

    <p class="format-info">
      Usamos <code>youtube-nocookie.com</code> (modo de privacidad mejorada)
      que no instala cookies de seguimiento hasta que el usuario reproduce el vídeo.
      Atributo <code>loading="lazy"</code> en el iframe: no carga el vídeo hasta
      que está cerca del viewport.
    </p>
  </section>
</body>
</html>
```

### Ejemplo Guiado 3: Animaciones CSS - Loader spinner, fade in, slide in, botón like

!!! example "Contexto pedagógico"
    Conjunto de animaciones CSS prácticas y reutilizables. Incluye un spinner de carga (loader) usando solo CSS, animaciones de entrada (fade-in, slide-in) para revelar contenido al hacer scroll, y una microinteracción de botón like.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ejemplo 3 - Animaciones CSS Prácticas</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      padding: 2rem;
      background: #f0f2f5;
    }

    h1 { text-align: center; margin-bottom: 2rem; }
    h2 { margin: 2rem 0 1rem; font-size: 1.3rem; }

    .demo-area {
      display: flex;
      gap: 2rem;
      flex-wrap: wrap;
      align-items: center;
      justify-content: center;
      background: #fff;
      padding: 2rem;
      border-radius: 12px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.06);
      margin-bottom: 1rem;
    }

    /*
     * ===== 1. SPINNER / LOADER =====
     * Animación de carga circular infinita.
     * Solo necesita CSS, sin imágenes ni JavaScript.
     *
     * border-top con color crea un arco visible.
     * El resto del borde es transparente.
     * animation: spin 0.8s linear infinite:
     *   - 0.8s de duración
     *   - linear: velocidad constante
     *   - infinite: nunca para
     */
    .spinner {
      width: 50px;
      height: 50px;
      border: 4px solid #e0e0e0;
      border-top: 4px solid #6c5ce7;
      border-radius: 50%;
      animation: spin 0.8s linear infinite;
    }

    @keyframes spin {
      0% { transform: rotate(0deg); }
      100% { transform: rotate(360deg); }
    }

    /*
     * Variante: dots loader (tres puntos animados secuencialmente)
     * animation-delay escalonado crea el efecto de onda.
     */
    .dots-loader {
      display: flex;
      gap: 0.5rem;
    }

    .dot {
      width: 12px;
      height: 12px;
      background: #6c5ce7;
      border-radius: 50%;
      animation: bounce 1.4s ease-in-out infinite both;
    }

    /* Cada punto empieza en un momento diferente */
    .dot:nth-child(1) { animation-delay: 0s; }
    .dot:nth-child(2) { animation-delay: 0.16s; }
    .dot:nth-child(3) { animation-delay: 0.32s; }

    @keyframes bounce {
      0%, 80%, 100% {
        transform: scale(0.3);
        opacity: 0.3;
      }
      40% {
        transform: scale(1);
        opacity: 1;
      }
    }

    /*
     * ===== 2. FADE IN =====
     * El elemento aparece gradualmente desvaneciéndose.
     * opacity: 0 -> 1 con transición suave.
     */
    .fade-in {
      animation: fadeIn 1.5s ease;
    }

    @keyframes fadeIn {
      from { opacity: 0; }
      to { opacity: 1; }
    }

    /*
     * ===== 3. SLIDE IN DESDE LA IZQUIERDA =====
     * El elemento entra deslizándose desde fuera de la pantalla.
     * translateX(-50px) + opacity: 0 -> translateX(0) + opacity: 1.
     */
    .slide-in-left {
      animation: slideInLeft 0.8s ease-out;
    }

    @keyframes slideInLeft {
      from {
        transform: translateX(-50px);
        opacity: 0;
      }
      to {
        transform: translateX(0);
        opacity: 1;
      }
    }

    /*
     * ===== 4. SLIDE IN DESDE ABAJO =====
     * Útil para tarjetas que aparecen al hacer scroll.
     */
    .slide-in-up {
      animation: slideInUp 0.8s ease-out;
    }

    @keyframes slideInUp {
      from {
        transform: translateY(30px);
        opacity: 0;
      }
      to {
        transform: translateY(0);
        opacity: 1;
      }
    }

    /*
     * ===== 5. PULSE (llamada de atención) =====
     * El elemento pulsa rítmicamente.
     * Ideal para CTAs o notificaciones.
     */
    .pulse {
      display: inline-block;
      padding: 0.75rem 1.5rem;
      background: #6c5ce7;
      color: #fff;
      border-radius: 25px;
      animation: pulse 2s ease-in-out infinite;
    }

    @keyframes pulse {
      0%, 100% { transform: scale(1); }
      50% { transform: scale(1.05); }
    }

    /*
     * ===== 6. SHAKE (sacudida de error) =====
     * El elemento tiembla horizontalmente.
     * Útil para validación de formularios.
     */
    .shake {
      animation: shake 0.5s ease-in-out;
    }

    @keyframes shake {
      0%, 100% { transform: translateX(0); }
      20% { transform: translateX(-10px); }
      40% { transform: translateX(10px); }
      60% { transform: translateX(-6px); }
      80% { transform: translateX(6px); }
    }

    /*
     * ===== 7. BOTÓN LIKE (microinteracción) =====
     * Corazón que crece y cambia de color al hacer clic.
     * Usa transiciones para el estado normal y animación para el clic.
     */
    .like-btn {
      font-size: 2rem;
      background: none;
      border: none;
      cursor: pointer;
      transition: transform 0.2s;
      outline: none;
      user-select: none;
    }

    .like-btn:hover {
      transform: scale(1.2);
    }

    /*
     * Cuando se añade la clase .liked (via JS), el corazón
     * hace una animación de "pop" (crece y vuelve).
     */
    .like-btn.liked {
      animation: likePop 0.4s ease;
    }

    @keyframes likePop {
      0% { transform: scale(1); }
      30% { transform: scale(1.3); }
      60% { transform: scale(0.9); }
      100% { transform: scale(1); }
    }

    /*
     * ===== 8. SKELETON LOADER =====
     * Placeholder animado que simula contenido cargando.
     * Usa un gradiente animado que se desplaza.
     */
    .skeleton {
      width: 100%;
      height: 20px;
      background: linear-gradient(90deg, #e0e0e0 25%, #f0f0f0 50%, #e0e0e0 75%);
      background-size: 200% 100%;
      animation: shimmer 1.5s ease-in-out infinite;
      border-radius: 4px;
      margin-bottom: 0.5rem;
    }

    .skeleton--title { width: 60%; height: 28px; }
    .skeleton--text { width: 100%; }
    .skeleton--text-short { width: 80%; }
    .skeleton--avatar {
      width: 48px;
      height: 48px;
      border-radius: 50%;
    }

    @keyframes shimmer {
      0% { background-position: 200% 0; }
      100% { background-position: -200% 0; }
    }

    /* Cards de demostración */
    .card {
      background: linear-gradient(135deg, #667eea, #764ba2);
      color: #fff;
      padding: 1.5rem;
      border-radius: 12px;
      width: 250px;
      text-align: center;
    }

    .card--green { background: linear-gradient(135deg, #11998e, #38ef7d); }
    .card--orange { background: linear-gradient(135deg, #f12711, #f5af19); }

    /* ===== RESPETAR PREFERENCIAS DE MOVIMIENTO ===== */
    @media (prefers-reduced-motion: reduce) {
      *,
      *::before,
      *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
      }
    }
  </style>
</head>
<body>
  <h1>Animaciones CSS Prácticas</h1>

  <!-- SPINNERS -->
  <h2>1. Loader Spinner circular</h2>
  <div class="demo-area">
    <div class="spinner"></div>
    <span style="margin-left:1rem; color:#666;">Cargando...</span>
  </div>

  <h2>2. Loader de 3 puntos</h2>
  <div class="demo-area">
    <div class="dots-loader">
      <div class="dot"></div>
      <div class="dot"></div>
      <div class="dot"></div>
    </div>
  </div>

  <!-- ANIMACIONES DE ENTRADA -->
  <h2>3. Fade In, Slide In</h2>
  <div class="demo-area">
    <div class="card fade-in">
      <h3>Fade In</h3>
      <p>Aparezco suavemente</p>
    </div>
    <div class="card card--green slide-in-left" style="animation-delay: 0.3s;">
      <h3>Slide In Left</h3>
      <p>Entro desde la izquierda</p>
    </div>
    <div class="card card--orange slide-in-up" style="animation-delay: 0.6s;">
      <h3>Slide In Up</h3>
      <p>Subo desde abajo</p>
    </div>
  </div>

  <!-- PULSE Y SHAKE -->
  <h2>4. Botón Pulse (CTA animado)</h2>
  <div class="demo-area">
    <span class="pulse">¡Oferta limitada!</span>
  </div>

  <!-- BOTÓN LIKE -->
  <h2>5. Microinteracción: Botón Like</h2>
  <div class="demo-area">
    <button class="like-btn" onclick="toggleLike(this)">🤍</button>
    <span style="margin-left:0.5rem; color:#666;">Haz clic en el corazón</span>
  </div>

  <!-- SKELETON -->
  <h2>6. Skeleton Loader (contenido fantasma)</h2>
  <div class="demo-area" style="flex-direction: column; align-items: flex-start; width: 100%;">
    <div style="display:flex; gap:1rem; margin-bottom:1rem; align-items:center;">
      <div class="skeleton skeleton--avatar"></div>
      <div style="flex:1;">
        <div class="skeleton skeleton--title"></div>
        <div class="skeleton skeleton--text-short"></div>
      </div>
    </div>
    <div class="skeleton skeleton--text"></div>
    <div class="skeleton skeleton--text"></div>
    <div class="skeleton skeleton--text-short"></div>
  </div>

  <script>
    // Función para el botón like: alterna el estado y la animación
    function toggleLike(btn) {
      const isLiked = btn.textContent.trim() === '❤️';
      btn.textContent = isLiked ? '🤍' : '❤️';
      // Quitamos y volvemos a añadir la clase para reiniciar la animación
      btn.classList.remove('liked');
      void btn.offsetWidth; // Forzamos reflow para reiniciar animación
      btn.classList.add('liked');
    }
  </script>
</body>
</html>
```

### Ejemplo Guiado 4: Animación SVG - Dibujar trazado con stroke-dasharray

!!! example "Contexto pedagógico"
    Una técnica espectacular de animación SVG: hacer que un trazado se "dibuje a sí mismo" manipulando las propiedades stroke-dasharray y stroke-dashoffset. El efecto es ideal para logotipos animados, gráficos de progreso, o revelar ilustraciones.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ejemplo 4 - Animación SVG</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      background: #0d1117;
      color: #fff;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
      padding: 2rem;
    }

    h1 { margin-bottom: 2rem; font-size: 1.5rem; color: #58a6ff; }
    p { margin-bottom: 1.5rem; color: #8b949e; text-align: center; max-width: 500px; }

    .demo-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 2rem;
      width: 100%;
      max-width: 1000px;
    }

    .demo-card {
      background: #161b22;
      border: 1px solid #30363d;
      border-radius: 12px;
      padding: 1.5rem;
      text-align: center;
    }

    .demo-card h3 { margin-bottom: 1rem; color: #e6edf3; }
    svg { max-width: 100%; }

    /*
     * ===== ANIMACIÓN DE TRAZADO SVG =====
     *
     * Principio de funcionamiento:
     * 1. stroke-dasharray: establece el patrón de trazo-espacio.
     *    Un valor igual a la longitud total del path hace que
     *    "todo" sea trazo y "nada" sea espacio.
     *
     * 2. stroke-dashoffset: desplaza el inicio del patrón.
     *    Empezamos con offset = longitud total (todo invisible).
     *    Animamos hasta offset = 0 (todo visible).
     *
     * 3. El resultado visual: el trazo parece dibujarse solo.
     */

    /* Estilo base para los paths animados */
    .draw-path {
      stroke: #58a6ff;
      stroke-width: 3;
      fill: none; /* Sin relleno, solo el trazo */
      stroke-linecap: round; /* Extremos redondeados */
      stroke-linejoin: round; /* Uniones redondeadas */
    }

    /* Animación de dibujo */
    .draw-animation {
      animation: drawLine 3s ease-in-out forwards;
    }

    @keyframes drawLine {
      from {
        stroke-dashoffset: var(--path-length); /* Empieza "oculto" */
      }
      to {
        stroke-dashoffset: 0; /* Termina "visible" */
      }
    }

    /* Versión con bucle infinito: dibujar y borrar */
    .draw-loop {
      animation: drawLineLoop 4s ease-in-out infinite;
    }

    @keyframes drawLineLoop {
      0%, 100% { stroke-dashoffset: var(--path-length); }
      50% { stroke-dashoffset: 0; }
    }

    /*
     * ===== CORAZÓN SVG ANIMADO =====
     * Combina dibujo del trazo + relleno que aparece después.
     */
    .heart-path {
      stroke: #f85149;
      stroke-width: 3;
      stroke-dasharray: var(--path-length);
      stroke-dashoffset: var(--path-length);
      fill: none;
      animation: drawAndFill 2s ease-in-out forwards;
    }

    @keyframes drawAndFill {
      0% {
        stroke-dashoffset: var(--path-length);
        fill: transparent;
      }
      60% {
        stroke-dashoffset: 0;
        fill: transparent;
      }
      100% {
        stroke-dashoffset: 0;
        fill: #f85149;
      }
    }

    /*
     * ===== CÍRCULO DE PROGRESO =====
     * Útil para indicadores de carga o skills.
     * Animamos stroke-dashoffset para revelar el porcentaje.
     */
    .progress-circle {
      stroke: #3fb950;
      stroke-width: 8;
      fill: none;
      stroke-linecap: round;
      transform: rotate(-90deg); /* Empezar desde arriba */
      transform-origin: center;
      /*
       * La circunferencia de un círculo de radio 45 es 2*PI*r = 282.74
       * Para 75%: dashoffset = 282.74 * (1 - 0.75) = 70.69
       */
      stroke-dasharray: 283;
      stroke-dashoffset: 283;
      animation: progressAnim 2s ease-out forwards;
    }

    @keyframes progressAnim {
      to {
        stroke-dashoffset: 71; /* 75% de 283 ≈ 212 visible, 71 oculto */
      }
    }

    /* ===== RESPETAR PREFERENCIAS DE MOVIMIENTO ===== */
    @media (prefers-reduced-motion: reduce) {
      .draw-animation,
      .draw-loop,
      .heart-path,
      .progress-circle {
        animation: none;
        stroke-dashoffset: 0;
      }
      .heart-path { fill: #f85149; }
    }
  </style>
</head>
<body>
  <h1>Animaciones SVG: Dibujar trazados</h1>
  <p>La técnica stroke-dasharray + stroke-dashoffset permite que los trazados
  se "dibujen solos" revelándose progresivamente. Ideal para logotipos animados,
  ilustraciones y gráficos de progreso.</p>

  <div class="demo-grid">
    <!-- DEMO 1: Dibujar un rectángulo -->
    <div class="demo-card">
      <h3>1. Rectángulo (se dibuja)</h3>
      <svg viewBox="0 0 200 150" width="200" height="150">
        <rect
          x="20" y="20" width="160" height="110" rx="8"
          class="draw-path draw-animation"
          style="--path-length: 540;"
        />
      </svg>
      <p style="font-size:0.8rem;color:#8b949e;margin-top:0.5rem;">
        Perímetro = 2*(160+110) = 540
      </p>
    </div>

    <!-- DEMO 2: Dibujar un círculo -->
    <div class="demo-card">
      <h3>2. Círculo</h3>
      <svg viewBox="0 0 200 200" width="200" height="200">
        <circle
          cx="100" cy="100" r="70"
          class="draw-path draw-animation"
          style="--path-length: 440; animation-delay: 0.5s;"
        />
      </svg>
      <p style="font-size:0.8rem;color:#8b949e;margin-top:0.5rem;">
        Circunferencia = 2*PI*70 ≈ 440
      </p>
    </div>

    <!-- DEMO 3: Corazón que se dibuja y se rellena -->
    <div class="demo-card">
      <h3>3. Corazón (dibujar + rellenar)</h3>
      <svg viewBox="0 0 100 100" width="200" height="200">
        <path
          d="M50,85 L20,50 Q10,35 25,20 Q35,12 50,30 Q65,12 75,20 Q90,35 80,50 Z"
          class="heart-path"
          style="--path-length: 200;"
        />
      </svg>
      <p style="font-size:0.8rem;color:#8b949e;margin-top:0.5rem;">
        Primero se dibuja el trazo, luego se rellena
      </p>
    </div>

    <!-- DEMO 4: Gráfico de progreso circular -->
    <div class="demo-card">
      <h3>4. Gráfico de progreso (75%)</h3>
      <svg viewBox="0 0 120 120" width="200" height="200">
        <!-- Círculo de fondo (gris) -->
        <circle cx="60" cy="60" r="45" stroke="#30363d" stroke-width="8" fill="none" />
        <!-- Círculo de progreso (verde) -->
        <circle cx="60" cy="60" r="45" class="progress-circle" />
        <!-- Texto central -->
        <text x="60" y="65" text-anchor="middle" fill="#e6edf3" font-size="20" font-weight="bold">75%</text>
      </svg>
      <p style="font-size:0.8rem;color:#8b949e;margin-top:0.5rem;">
        stroke-dashoffset controla el porcentaje visible
      </p>
    </div>

    <!-- DEMO 5: Logo que se dibuja en bucle -->
    <div class="demo-card">
      <h3>5. Loop infinito</h3>
      <svg viewBox="0 0 200 100" width="200" height="100">
        <path
          d="M30,50 Q60,20 100,50 Q140,80 170,50"
          class="draw-path draw-loop"
          style="--path-length: 180;"
        />
      </svg>
      <p style="font-size:0.8rem;color:#8b949e;margin-top:0.5rem;">
        Se dibuja y se borra continuamente
      </p>
    </div>

    <!-- DEMO 6: Estrella -->
    <div class="demo-card">
      <h3>6. Polígono (estrella)</h3>
      <svg viewBox="0 0 200 200" width="200" height="200">
        <polygon
          points="100,10 120,70 185,70 135,110 150,175 100,135 50,175 65,110 15,70 80,70"
          class="draw-path draw-animation"
          style="--path-length: 520; animation-delay: 0.8s;"
        />
      </svg>
      <p style="font-size:0.8rem;color:#8b949e;margin-top:0.5rem;">
        Funciona con cualquier forma SVG
      </p>
    </div>
  </div>

  <script>
    /*
     * Script para calcular automáticamente la longitud de cada path
     * y establecerla como variable CSS (--path-length).
     * getTotalLength() mide el perímetro total del trazado.
     * Esto evita tener que calcular manualmente las longitudes.
     */
    document.querySelectorAll('.draw-path, .heart-path').forEach(path => {
      const length = path.getTotalLength();
      path.style.setProperty('--path-length', length);
      path.style.strokeDasharray = length;
    });
  </script>
</body>
</html>
```

### Ejemplo Guiado 5: Reproductor de vídeo personalizado con API de HTML5

!!! example "Contexto pedagógico"
    Aunque los controles nativos del navegador son funcionales, en proyectos profesionales a menudo necesitamos un reproductor personalizado. Este ejemplo muestra cómo controlar la reproducción de vídeo mediante la API JavaScript de HTML5, creando controles personalizados con HTML/CSS.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ejemplo 5 - Reproductor de Vídeo Personalizado</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      background: #0d1117;
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
      padding: 2rem;
    }

    /*
     * ===== CONTENEDOR DEL REPRODUCTOR =====
     * Agrupa el vídeo y los controles personalizados.
     * max-width: 800px para que no sea excesivamente grande.
     */
    .player {
      max-width: 800px;
      width: 100%;
      background: #000;
      border-radius: 12px;
      overflow: hidden;
      box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5);
    }

    /* El vídeo ocupa todo el ancho del reproductor */
    .player video {
      width: 100%;
      display: block;
    }

    /*
     * ===== BARRA DE CONTROLES PERSONALIZADA =====
     * Fondo oscuro semitransparente.
     * Grid para organizar los controles: play, progreso, tiempo, volumen.
     */
    .player__controls {
      background: rgba(0, 0, 0, 0.85);
      padding: 0.75rem 1rem;
      display: grid;
      grid-template-columns: auto 1fr auto;
      align-items: center;
      gap: 1rem;
    }

    /* Botones de play/pause y volumen */
    .player__btn {
      background: none;
      border: none;
      color: #fff;
      font-size: 1.2rem;
      cursor: pointer;
      padding: 0.25rem 0.5rem;
      border-radius: 4px;
      transition: background 0.2s;
    }

    .player__btn:hover { background: rgba(255, 255, 255, 0.15); }

    /*
     * ===== BARRA DE PROGRESO =====
     * Input range estilizado.
     * Muestra el progreso de reproducción y permite hacer clic para navegar.
     */
    .player__progress {
      -webkit-appearance: none;
      appearance: none;
      width: 100%;
      height: 5px;
      background: rgba(255, 255, 255, 0.2);
      border-radius: 3px;
      outline: none;
      cursor: pointer;
    }

    /* El "pulgar" (thumb) del input range */
    .player__progress::-webkit-slider-thumb {
      -webkit-appearance: none;
      appearance: none;
      width: 14px;
      height: 14px;
      background: #3b82f6;
      border-radius: 50%;
      cursor: pointer;
    }

    .player__progress::-moz-range-thumb {
      width: 14px;
      height: 14px;
      background: #3b82f6;
      border-radius: 50%;
      border: none;
      cursor: pointer;
    }

    /* Tiempo actual / duración total */
    .player__time {
      color: #ccc;
      font-size: 0.85rem;
      font-variant-numeric: tabular-nums; /* Números monoespaciados */
    }

    /* Grupo de la derecha: volumen + pantalla completa */
    .player__right {
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    /* Input range para el volumen */
    .player__volume {
      -webkit-appearance: none;
      appearance: none;
      width: 80px;
      height: 4px;
      background: rgba(255, 255, 255, 0.2);
      border-radius: 2px;
      outline: none;
      cursor: pointer;
    }

    .player__volume::-webkit-slider-thumb {
      -webkit-appearance: none;
      appearance: none;
      width: 12px;
      height: 12px;
      background: #fff;
      border-radius: 50%;
      cursor: pointer;
    }

    .player__volume::-moz-range-thumb {
      width: 12px;
      height: 12px;
      background: #fff;
      border-radius: 50%;
      border: none;
      cursor: pointer;
    }
  </style>
</head>
<body>
  <div class="player">
    <!--
      Vídeo sin controls nativos.
      La interacción se gestiona mediante JavaScript y nuestra barra personalizada.
    -->
    <video id="miVideo" poster="poster.jpg" preload="metadata">
      <source src="video.mp4" type="video/mp4">
      <source src="video.webm" type="video/webm">
      <track kind="subtitles" src="subtitulos.vtt" srclang="es" label="Español" default>
    </video>

    <!-- Controles personalizados -->
    <div class="player__controls">
      <!-- Botón Play/Pause -->
      <button id="btnPlay" class="player__btn" title="Reproducir">▶️</button>

      <!-- Barra de progreso -->
      <input type="range" id="barraProgreso" class="player__progress" value="0" min="0" max="100" step="0.1">

      <!-- Tiempo actual / total -->
      <span class="player__time" id="tiempo">0:00 / 0:00</span>

      <!-- Controles de volumen y pantalla completa -->
      <div class="player__right">
        <button id="btnMute" class="player__btn" title="Silenciar">🔊</button>
        <input type="range" id="controlVolumen" class="player__volume" value="100" min="0" max="100">
        <button id="btnFullscreen" class="player__btn" title="Pantalla completa">⛶</button>
      </div>
    </div>
  </div>

  <script>
    // ===== REFERENCIAS A LOS ELEMENTOS DEL DOM =====
    const video = document.getElementById('miVideo');
    const btnPlay = document.getElementById('btnPlay');
    const barraProgreso = document.getElementById('barraProgreso');
    const tiempoDisplay = document.getElementById('tiempo');
    const btnMute = document.getElementById('btnMute');
    const controlVolumen = document.getElementById('controlVolumen');
    const btnFullscreen = document.getElementById('btnFullscreen');

    // ===== FUNCIONES AUXILIARES =====
    // Convierte segundos a formato mm:ss
    function formatearTiempo(segundos) {
      const min = Math.floor(segundos / 60);
      const sec = Math.floor(segundos % 60);
      return min + ':' + (sec < 10 ? '0' : '') + sec;
    }

    // Actualiza el display de tiempo y la barra de progreso
    function actualizarProgreso() {
      if (video.duration) {
        const porcentaje = (video.currentTime / video.duration) * 100;
        barraProgreso.value = porcentaje;
        tiempoDisplay.textContent =
          formatearTiempo(video.currentTime) + ' / ' + formatearTiempo(video.duration);
      }
    }

    // ===== CONTROL PLAY/PAUSE =====
    btnPlay.addEventListener('click', () => {
      if (video.paused) {
        video.play();
        btnPlay.textContent = '⏸️';
      } else {
        video.pause();
        btnPlay.textContent = '▶️';
      }
    });

    // Actualizar botón cuando el vídeo termina
    video.addEventListener('ended', () => {
      btnPlay.textContent = '▶️';
    });

    // ===== BARRA DE PROGRESO INTERACTIVA =====
    // Cuando el usuario mueve la barra, saltamos a esa posición
    barraProgreso.addEventListener('input', () => {
      const tiempo = (barraProgreso.value / 100) * video.duration;
      video.currentTime = tiempo;
    });

    // Actualizar barra durante la reproducción
    video.addEventListener('timeupdate', actualizarProgreso);

    // Cuando los metadatos cargan, mostramos la duración
    video.addEventListener('loadedmetadata', actualizarProgreso);

    // ===== CONTROL DE VOLUMEN =====
    controlVolumen.addEventListener('input', () => {
      video.volume = controlVolumen.value / 100;
      // Actualizar icono según el nivel de volumen
      if (video.volume === 0) {
        btnMute.textContent = '🔇';
      } else if (video.volume < 0.5) {
        btnMute.textContent = '🔉';
      } else {
        btnMute.textContent = '🔊';
      }
    });

    // Botón de silencio
    btnMute.addEventListener('click', () => {
      video.muted = !video.muted;
      btnMute.textContent = video.muted ? '🔇' : '🔊';
      controlVolumen.value = video.muted ? 0 : video.volume * 100;
    });

    // ===== PANTALLA COMPLETA =====
    btnFullscreen.addEventListener('click', () => {
      if (document.fullscreenElement) {
        document.exitFullscreen();
      } else {
        // Solicitamos pantalla completa en el contenedor del reproductor
        document.querySelector('.player').requestFullscreen();
      }
    });

    // ===== ATAJOS DE TECLADO =====
    document.addEventListener('keydown', (e) => {
      // Espacio: play/pause (solo si no estamos en un input)
      if (e.code === 'Space' && e.target === document.body) {
        e.preventDefault();
        btnPlay.click();
      }
      // Flecha izquierda: retroceder 5 segundos
      if (e.code === 'ArrowLeft') {
        video.currentTime = Math.max(0, video.currentTime - 5);
      }
      // Flecha derecha: avanzar 5 segundos
      if (e.code === 'ArrowRight') {
        video.currentTime = Math.min(video.duration, video.currentTime + 5);
      }
      // Tecla M: silenciar/activar sonido
      if (e.code === 'KeyM') {
        btnMute.click();
      }
      // Tecla F: pantalla completa
      if (e.code === 'KeyF') {
        btnFullscreen.click();
      }
    });
  </script>
</body>
</html>
```


### Ejemplo Guiado 6: Transiciones CSS para menús y modales

!!! example "Contexto pedagógico"
    Las transiciones CSS suavizan los cambios de estado mejorando la experiencia de usuario. Este ejemplo muestra cómo aplicar transiciones a menús desplegables, tooltips y modales, usando transform y opacity para máximo rendimiento.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ejemplo 6 - Transiciones CSS</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      padding: 3rem;
      background: #f0f2f5;
    }

    h1 { margin-bottom: 2rem; }
    section { margin-bottom: 3rem; }
    h2 { margin-bottom: 1rem; font-size: 1.2rem; color: #333; }

    /* ===== 1. MENÚ DESPLEGABLE CON TRANSICIÓN ===== */
    .dropdown {
      position: relative;
      display: inline-block;
    }

    .dropdown__trigger {
      background: #6c5ce7;
      color: #fff;
      border: none;
      padding: 0.75rem 1.5rem;
      border-radius: 8px;
      cursor: pointer;
      font-size: 1rem;
    }

    /*
     * El menú está oculto por defecto con opacity: 0 y
     * transform: translateY (ligeramente desplazado hacia arriba).
     * pointer-events: none evita que reciba clicks cuando está oculto.
     * La transición suaviza ambos cambios.
     */
    .dropdown__menu {
      position: absolute;
      top: 100%;
      left: 0;
      background: #fff;
      border-radius: 8px;
      box-shadow: 0 4px 20px rgba(0,0,0,0.15);
      min-width: 200px;
      padding: 0.5rem 0;
      margin-top: 0.5rem;
      opacity: 0;
      transform: translateY(-10px);
      pointer-events: none;
      transition: opacity 0.25s, transform 0.25s;
    }

    /* Al hacer hover en el contenedor, mostramos el menú */
    .dropdown:hover .dropdown__menu {
      opacity: 1;
      transform: translateY(0);
      pointer-events: auto;
    }

    .dropdown__menu a {
      display: block;
      padding: 0.5rem 1.5rem;
      color: #333;
      text-decoration: none;
      transition: background 0.15s;
    }

    .dropdown__menu a:hover { background: #f0f0f0; }

    /* ===== 2. TOOLTIP CON TRANSICIÓN ===== */
    .tooltip {
      position: relative;
      display: inline-block;
      cursor: help;
      color: #6c5ce7;
      font-weight: 600;
      border-bottom: 1px dotted #6c5ce7;
    }

    /*
     * Tooltip posicionado arriba del elemento.
     * Transform: translateX(-50%) centra horizontalmente.
     * Opacity + visibility para ocultar.
     * Transition con delay: aparece tras 0.3s de hover
     * (evita tooltips accidentales al mover el ratón).
     */
    .tooltip::after {
      content: attr(data-tooltip);
      position: absolute;
      bottom: calc(100% + 8px);
      left: 50%;
      transform: translateX(-50%);
      background: #1a1a2e;
      color: #fff;
      padding: 0.4rem 0.8rem;
      border-radius: 6px;
      font-size: 0.85rem;
      font-weight: 400;
      white-space: nowrap;
      opacity: 0;
      visibility: hidden;
      transition: opacity 0.2s 0.3s, visibility 0.2s 0.3s;
    }

    .tooltip:hover::after {
      opacity: 1;
      visibility: visible;
    }

    /* ===== 3. MODAL CON TRANSICIÓN ===== */
    .modal-overlay {
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.5);
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 1000;
      opacity: 0;
      visibility: hidden;
      transition: opacity 0.3s, visibility 0.3s;
    }

    .modal-overlay--visible {
      opacity: 1;
      visibility: visible;
    }

    /*
     * El contenido del modal tiene su propia transición de escala.
     * Aparece con efecto "zoom in" suave.
     */
    .modal {
      background: #fff;
      border-radius: 16px;
      padding: 2rem;
      max-width: 500px;
      width: 90%;
      box-shadow: 0 20px 60px rgba(0,0,0,0.3);
      transform: scale(0.9);
      transition: transform 0.3s;
    }

    .modal-overlay--visible .modal {
      transform: scale(1);
    }

    .modal h2 { margin-bottom: 1rem; }
    .modal p { margin-bottom: 1.5rem; color: #666; }
    .modal__close {
      background: #6c5ce7;
      color: #fff;
      border: none;
      padding: 0.5rem 1.5rem;
      border-radius: 8px;
      cursor: pointer;
    }

    /* ===== 4. ACORDEÓN CON ALTURA ANIMADA ===== */
    .accordion {
      border: 1px solid #e0e0e0;
      border-radius: 8px;
      overflow: hidden;
      margin-bottom: 0.5rem;
    }

    .accordion__header {
      background: #f8f9fa;
      padding: 0.75rem 1rem;
      cursor: pointer;
      font-weight: 600;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .accordion__icon {
      transition: transform 0.3s;
    }

    .accordion--open .accordion__icon {
      transform: rotate(180deg);
    }

    /*
     * Truco para animar altura de auto a 0:
     * Usamos max-height + overflow hidden.
     * max-height debe ser mayor que la altura máxima del contenido.
     */
    .accordion__body {
      max-height: 0;
      overflow: hidden;
      transition: max-height 0.4s ease;
    }

    .accordion--open .accordion__body {
      max-height: 500px; /* Suficientemente grande para el contenido */
    }

    .accordion__content {
      padding: 1rem;
      border-top: 1px solid #e0e0e0;
    }

    /* ===== RESPETAR PREFERENCIAS ===== */
    @media (prefers-reduced-motion: reduce) {
      .dropdown__menu,
      .tooltip::after,
      .modal-overlay,
      .modal,
      .accordion__body {
        transition: none !important;
      }
    }
  </style>
</head>
<body>
  <h1>Transiciones CSS: Menús, Tooltips y Modales</h1>

  <!-- 1. MENÚ DESPLEGABLE -->
  <section>
    <h2>1. Menú desplegable con transición</h2>
    <div class="dropdown">
      <button class="dropdown__trigger">Mi Cuenta ▼</button>
      <div class="dropdown__menu">
        <a href="#">Mi Perfil</a>
        <a href="#">Configuración</a>
        <a href="#">Mis Pedidos</a>
        <hr style="border-color:#f0f0f0;">
        <a href="#">Cerrar Sesión</a>
      </div>
    </div>
  </section>

  <!-- 2. TOOLTIP -->
  <section>
    <h2>2. Tooltip informativo</h2>
    <p>Pasa el ratón sobre
      <span class="tooltip" data-tooltip="Search Engine Optimization: optimización para motores de búsqueda">SEO</span>
      para ver la definición. También prueba con
      <span class="tooltip" data-tooltip="Cumulative Layout Shift: métrica de estabilidad visual">CLS</span>.
    </p>
  </section>

  <!-- 3. MODAL -->
  <section>
    <h2>3. Modal con transición</h2>
    <button onclick="abrirModal()" style="padding:0.5rem 1.5rem; background:#6c5ce7; color:#fff; border:none; border-radius:8px; cursor:pointer;">
      Abrir Modal
    </button>
  </section>

  <!-- Modal (oculto por defecto) -->
  <div class="modal-overlay" id="modalOverlay">
    <div class="modal">
      <h2>Título del Modal</h2>
      <p>Este modal usa transiciones CSS para una aparición y desaparición suave. El overlay hace fade, el contenido hace zoom. Sin necesidad de librerías externas.</p>
      <button class="modal__close" onclick="cerrarModal()">Cerrar</button>
    </div>
  </div>

  <!-- 4. ACORDEÓN -->
  <section>
    <h2>4. Acordeón con altura animada</h2>
    <div class="accordion" onclick="toggleAcordeon(this)">
      <div class="accordion__header">
        <span>¿Qué es CSS Grid?</span>
        <span class="accordion__icon">▼</span>
      </div>
      <div class="accordion__body">
        <div class="accordion__content">
          CSS Grid es un sistema de maquetación bidimensional que permite controlar filas y columnas simultáneamente.
        </div>
      </div>
    </div>
    <div class="accordion" onclick="toggleAcordeon(this)">
      <div class="accordion__header">
        <span>¿Qué son las transiciones CSS?</span>
        <span class="accordion__icon">▼</span>
      </div>
      <div class="accordion__body">
        <div class="accordion__content">
          Las transiciones CSS permiten suavizar el cambio entre dos estados de una propiedad, creando animaciones fluidas sin JavaScript.
        </div>
      </div>
    </div>
  </section>

  <script>
    // Abrir modal
    function abrirModal() {
      document.getElementById('modalOverlay').classList.add('modal-overlay--visible');
    }

    // Cerrar modal
    function cerrarModal() {
      document.getElementById('modalOverlay').classList.remove('modal-overlay--visible');
    }

    // Cerrar modal al hacer clic fuera del contenido
    document.getElementById('modalOverlay').addEventListener('click', function(e) {
      if (e.target === this) cerrarModal();
    });

    // Toggle acordeón
    function toggleAcordeon(el) {
      el.classList.toggle('accordion--open');
    }

    // Cerrar modal con Escape
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') cerrarModal();
    });
  </script>
</body>
</html>
```

### Ejemplo Guiado 7: Microinteracciones avanzadas

!!! example "Contexto pedagógico"
    Colección de microinteracciones profesionales: botón de añadir al carrito con feedback visual, switch/toggle animado, notificación toast que aparece y desaparece, y pull-to-refresh simulado.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ejemplo 7 - Microinteracciones</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: 'Segoe UI', system-ui, sans-serif; padding: 2rem; background: #f5f6fa; }
    h1 { margin-bottom: 2rem; }
    section { background: #fff; padding: 1.5rem; border-radius: 12px; margin-bottom: 1.5rem; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }
    h2 { margin-bottom: 1rem; font-size: 1.1rem; }

    /*
     * ===== 1. BOTÓN AÑADIR AL CARRITO =====
     * Al hacer clic, el icono del carrito "salta" (rebota)
     * y un badge numérico aparece/actualiza.
     * Combina animación CSS + transición de estado.
     */
    .cart-btn {
      position: relative;
      background: #6c5ce7;
      color: #fff;
      border: none;
      padding: 0.75rem 1.5rem;
      border-radius: 30px;
      font-size: 1rem;
      cursor: pointer;
      transition: background 0.2s;
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
    }

    .cart-btn:hover { background: #5a4bd1; }

    /* Badge del carrito */
    .cart-badge {
      background: #fd79a8;
      color: #fff;
      width: 22px;
      height: 22px;
      border-radius: 50%;
      font-size: 0.75rem;
      display: grid;
      place-items: center;
      font-weight: 700;
      transition: transform 0.3s cubic-bezier(0.68, -0.55, 0.265, 1.55);
    }

    /* Clase que activa la animación de rebote */
    .cart-badge.bounce {
      animation: badgeBounce 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55);
    }

    @keyframes badgeBounce {
      0%, 100% { transform: scale(1); }
      40% { transform: scale(1.4); }
      70% { transform: scale(0.9); }
    }

    /*
     * ===== 2. SWITCH / TOGGLE =====
     * Interruptor de encendido/apagado con animación suave.
     * Usa un checkbox oculto + label estilizado.
     * El círculo se desliza horizontalmente con transición.
     */
    .toggle {
      display: inline-flex;
      align-items: center;
      gap: 0.75rem;
      cursor: pointer;
      user-select: none;
    }

    .toggle input { display: none; }

    /* El track (fondo del switch) */
    .toggle__track {
      width: 52px;
      height: 28px;
      background: #ccc;
      border-radius: 14px;
      position: relative;
      transition: background 0.3s;
    }

    /* El círculo que se desliza */
    .toggle__thumb {
      position: absolute;
      top: 3px;
      left: 3px;
      width: 22px;
      height: 22px;
      background: #fff;
      border-radius: 50%;
      transition: transform 0.3s cubic-bezier(0.68, -0.55, 0.265, 1.55);
      box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }

    /* Estado activo */
    .toggle input:checked + .toggle__track {
      background: #6c5ce7;
    }

    .toggle input:checked + .toggle__track .toggle__thumb {
      transform: translateX(24px);
    }

    /*
     * ===== 3. TOAST / NOTIFICACIÓN =====
     * Mensaje que aparece deslizándose desde la derecha
     * y desaparece automáticamente.
     */
    .toast-container {
      position: fixed;
      top: 1rem;
      right: 1rem;
      z-index: 9999;
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
    }

    .toast {
      background: #1a1a2e;
      color: #fff;
      padding: 1rem 1.5rem;
      border-radius: 8px;
      box-shadow: 0 4px 20px rgba(0,0,0,0.2);
      display: flex;
      align-items: center;
      gap: 0.75rem;
      min-width: 280px;
      animation: toastIn 0.4s ease-out;
      transition: opacity 0.3s, transform 0.3s;
    }

    .toast--removing {
      opacity: 0;
      transform: translateX(100%);
    }

    @keyframes toastIn {
      from { transform: translateX(100%); opacity: 0; }
      to { transform: translateX(0); opacity: 1; }
    }

    .toast--success { border-left: 4px solid #10b981; }
    .toast--error { border-left: 4px solid #ef4444; }
    .toast--warning { border-left: 4px solid #f59e0b; }

    /* ===== 4. PULL TO REFRESH (SIMULADO) ===== */
    .refresh-demo {
      text-align: center;
      padding: 2rem;
      background: #f0f0f0;
      border-radius: 8px;
    }

    .refresh-icon {
      display: inline-block;
      font-size: 2rem;
      cursor: pointer;
      transition: transform 0.3s;
    }

    .refresh-icon:active {
      transform: rotate(180deg);
    }

    .refresh-icon.spinning {
      animation: spinRefresh 1s ease-in-out;
    }

    @keyframes spinRefresh {
      from { transform: rotate(0deg); }
      to { transform: rotate(360deg); }
    }

    /* ===== 5. CONFIRMACIÓN VISUAL (CHECKMARK) ===== */
    .confirm-btn {
      background: #10b981;
      color: #fff;
      border: none;
      padding: 0.75rem 1.5rem;
      border-radius: 8px;
      font-size: 1rem;
      cursor: pointer;
      transition: background 0.2s, transform 0.2s;
    }

    .confirm-btn:hover { background: #059669; }
    .confirm-btn:active { transform: scale(0.96); }

    .confirm-btn.done {
      background: #059669;
      pointer-events: none;
      animation: confirmPop 0.4s ease;
    }

    @keyframes confirmPop {
      0% { transform: scale(1); }
      50% { transform: scale(1.1); }
      100% { transform: scale(1); }
    }
  </style>
</head>
<body>
  <h1>Microinteracciones</h1>

  <!-- 1. BOTÓN CARRITO -->
  <section>
    <h2>1. Botón añadir al carrito</h2>
    <button class="cart-btn" onclick="addToCart()">
      🛒 Añadir al carrito
      <span class="cart-badge" id="cartCount">0</span>
    </button>
  </section>

  <!-- 2. SWITCH / TOGGLE -->
  <section>
    <h2>2. Toggle Switch</h2>
    <label class="toggle">
      <span>Notificaciones</span>
      <input type="checkbox" checked>
      <div class="toggle__track">
        <div class="toggle__thumb"></div>
      </div>
    </label>
    <label class="toggle" style="margin-left:2rem;">
      <span>Modo oscuro</span>
      <input type="checkbox">
      <div class="toggle__track">
        <div class="toggle__thumb"></div>
      </div>
    </label>
  </section>

  <!-- 3. TOAST -->
  <section>
    <h2>3. Notificaciones Toast</h2>
    <button onclick="mostrarToast('success', 'Operación completada con éxito')" style="padding:0.5rem 1rem; background:#10b981; color:#fff; border:none; border-radius:6px; cursor:pointer; margin-right:0.5rem;">Éxito</button>
    <button onclick="mostrarToast('error', 'Ha ocurrido un error inesperado')" style="padding:0.5rem 1rem; background:#ef4444; color:#fff; border:none; border-radius:6px; cursor:pointer; margin-right:0.5rem;">Error</button>
    <button onclick="mostrarToast('warning', 'Revisa los datos introducidos')" style="padding:0.5rem 1rem; background:#f59e0b; color:#fff; border:none; border-radius:6px; cursor:pointer;">Aviso</button>
  </section>

  <!-- 4. PULL TO REFRESH -->
  <section>
    <h2>4. Indicador de recarga</h2>
    <div class="refresh-demo">
      <span class="refresh-icon" onclick="simularRefresh(this)">🔄</span>
      <p style="color:#666; margin-top:0.5rem;">Haz clic para simular recarga</p>
    </div>
  </section>

  <!-- 5. CONFIRMACIÓN -->
  <section>
    <h2>5. Botón de confirmación con feedback</h2>
    <button class="confirm-btn" onclick="confirmarAccion(this)">Guardar cambios</button>
  </section>

  <!-- Contenedor de toasts -->
  <div class="toast-container" id="toastContainer"></div>

  <script>
    // ===== CARRITO =====
    let cartItems = 0;
    function addToCart() {
      cartItems++;
      const badge = document.getElementById('cartCount');
      badge.textContent = cartItems;
      // Reiniciamos la animación quitando y añadiendo la clase
      badge.classList.remove('bounce');
      void badge.offsetWidth;
      badge.classList.add('bounce');
    }

    // ===== TOAST =====
    function mostrarToast(tipo, mensaje) {
      const container = document.getElementById('toastContainer');
      const toast = document.createElement('div');
      const iconos = { success: '✅', error: '❌', warning: '⚠️' };

      toast.className = 'toast toast--' + tipo;
      toast.innerHTML = '<span>' + (iconos[tipo] || '') + '</span> ' + mensaje;
      container.appendChild(toast);

      // Eliminar automáticamente después de 3 segundos
      setTimeout(() => {
        toast.classList.add('toast--removing');
        setTimeout(() => toast.remove(), 300);
      }, 3000);
    }

    // ===== REFRESH =====
    function simularRefresh(icon) {
      icon.classList.add('spinning');
      setTimeout(() => icon.classList.remove('spinning'), 1000);
    }

    // ===== CONFIRMACIÓN =====
    function confirmarAccion(btn) {
      btn.classList.add('done');
      btn.textContent = '✓ ¡Guardado!';
      setTimeout(() => {
        btn.classList.remove('done');
        btn.textContent = 'Guardar cambios';
      }, 2000);
    }
  </script>
</body>
</html>
```

### Ejemplo Guiado 8: Optimización con FFmpeg y configuración de vídeo

!!! example "Contexto pedagógico"
    Guía práctica (con comandos) para optimizar vídeos para la web usando FFmpeg. Incluye compresión, cambio de resolución, extracción de poster, y generación de versiones para streaming adaptativo.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ejemplo 8 - Optimización de vídeo con FFmpeg</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      max-width: 900px;
      margin: 0 auto;
      padding: 2rem;
      background: #1e293b;
      color: #e2e8f0;
    }
    h1 { color: #58a6ff; margin-bottom: 1rem; }
    h2 { color: #e2e8f0; margin: 2rem 0 0.75rem; font-size: 1.2rem; }
    p { color: #94a3b8; line-height: 1.6; margin-bottom: 1rem; }
    pre {
      background: #0f172a;
      color: #7dd3fc;
      padding: 1rem;
      border-radius: 8px;
      overflow-x: auto;
      font-size: 0.9rem;
      line-height: 1.5;
      margin: 0.5rem 0 1.5rem;
    }
    code { font-family: 'Fira Code', 'Cascadia Code', monospace; }
    table { width: 100%; border-collapse: collapse; margin: 1rem 0; background: #0f172a; border-radius: 8px; overflow: hidden; }
    th, td { padding: 0.75rem 1rem; text-align: left; border-bottom: 1px solid #30363d; }
    th { background: #161b22; color: #58a6ff; font-weight: 600; }
    td { color: #c9d1d9; }
    .note { background: #161b22; border-left: 4px solid #58a6ff; padding: 0.75rem 1rem; border-radius: 0 8px 8px 0; margin: 1rem 0; }

    .video-container {
      position: relative;
      padding-bottom: 56.25%;
      height: 0;
      overflow: hidden;
      border-radius: 8px;
      margin: 1rem 0;
    }
    .video-container video {
      position: absolute;
      top: 0; left: 0;
      width: 100%; height: 100%;
      border: none;
    }
  </style>
</head>
<body>
  <h1>Optimización de Vídeo Web con FFmpeg</h1>
  <p>FFmpeg es la herramienta de línea de comandos más potente para procesar audio y vídeo. Es software libre y está disponible para Windows, macOS y Linux. A continuación se muestran los comandos esenciales para preparar vídeos para la web.</p>

  <h2>1. Ver información de un vídeo</h2>
  <p>Antes de optimizar, necesitamos conocer las características del vídeo original.</p>
  <pre><code># Información detallada del archivo (códec, resolución, bitrate, duración)
ffprobe -v error -show_entries stream=codec_name,width,height,bit_rate,duration -of default=noprint_wrappers=1 video-original.mp4</code></pre>

  <h2>2. Comprimir para web (H.264 + AAC)</h2>
  <p>Este comando genera un MP4 optimizado para web con buena relación calidad/tamaño.</p>
  <pre><code># CRF 23 = buena calidad (menor número = mejor calidad, mayor archivo)
# preset medium = balance velocidad/compresión
# movflags +faststart = el vídeo empieza a reproducirse antes de descargar completamente
ffmpeg -i video-original.mp4 \
  -c:v libx264 -crf 23 -preset medium \
  -c:a aac -b:a 128k \
  -movflags +faststart \
  video-web.mp4</code></pre>

  <h2>3. Reducir resolución (escalar)</h2>
  <p>Para móvil no necesitamos 4K. Escalar a 720p o 1080p reduce drásticamente el tamaño.</p>
  <pre><code># Escalar a 1280x720 (720p) manteniendo la relación de aspecto
ffmpeg -i video-original.mp4 \
  -vf "scale=1280:-2" \
  -c:v libx264 -crf 23 -preset medium \
  -c:a aac -b:a 128k \
  -movflags +faststart \
  video-720p.mp4

# Escalar a 1920x1080 (1080p)
ffmpeg -i video-original.mp4 \
  -vf "scale=1920:-2" \
  -c:v libx264 -crf 23 -preset medium \
  -c:a aac -b:a 128k \
  -movflags +faststart \
  video-1080p.mp4</code></pre>

  <h2>4. Convertir a WebM (VP9) para navegadores modernos</h2>
  <p>WebM/VP9 ofrece mejor compresión que H.264 y es de código abierto.</p>
  <pre><code># WebM con VP9 y audio Opus
ffmpeg -i video-original.mp4 \
  -c:v libvpx-vp9 -crf 30 -b:v 0 \
  -c:a libopus -b:a 96k \
  video-web.webm</code></pre>

  <h2>5. Extraer un fotograma como poster</h2>
  <pre><code># Extraer el fotograma del segundo 2 como imagen JPG
ffmpeg -i video-original.mp4 -ss 00:00:02 -vframes 1 poster.jpg

# Extraer un fotograma cada 10 segundos (para galería de miniaturas)
ffmpeg -i video-original.mp4 -vf "fps=1/10" thumbnails/thumb-%03d.jpg</code></pre>

  <h2>6. Generar versiones para múltiples dispositivos (script batch)</h2>
  <pre><code>#!/bin/bash
# Script para generar versiones responsive de un vídeo
# Uso: ./optimizar-video.sh video-original.mp4

INPUT="$1"
BASENAME="${INPUT%.*}"

# 1080p
ffmpeg -i "$INPUT" -vf "scale=1920:-2" -c:v libx264 -crf 23 -preset medium -c:a aac -b:a 128k -movflags +faststart "${BASENAME}-1080p.mp4"

# 720p
ffmpeg -i "$INPUT" -vf "scale=1280:-2" -c:v libx264 -crf 23 -preset medium -c:a aac -b:a 128k -movflags +faststart "${BASENAME}-720p.mp4"

# 480p (móvil)
ffmpeg -i "$INPUT" -vf "scale=854:-2" -c:v libx264 -crf 26 -preset medium -c:a aac -b:a 96k -movflags +faststart "${BASENAME}-480p.mp4"

# WebM para cada resolución
ffmpeg -i "$INPUT" -vf "scale=1280:-2" -c:v libvpx-vp9 -crf 30 -b:v 0 -c:a libopus -b:a 96k "${BASENAME}-720p.webm"

echo "Optimización completada"</code></pre>

  <h2>7. Tabla comparativa de parámetros de compresión</h2>
  <table>
    <thead>
      <tr><th>Parámetro</th><th>Valor</th><th>Resultado</th></tr>
    </thead>
    <tbody>
      <tr><td>CRF (H.264)</td><td>18</td><td>Calidad visualmente sin pérdida, archivos grandes</td></tr>
      <tr><td>CRF (H.264)</td><td>23</td><td>Buena calidad, tamaño equilibrado (recomendado para web)</td></tr>
      <tr><td>CRF (H.264)</td><td>28</td><td>Calidad aceptable, archivos pequeños (móvil)</td></tr>
      <tr><td>Preset</td><td>veryslow</td><td>Máxima compresión, codificación muy lenta</td></tr>
      <tr><td>Preset</td><td>medium</td><td>Balance recomendado velocidad/compresión</td></tr>
      <tr><td>Preset</td><td>veryfast</td><td>Codificación rápida, menor compresión</td></tr>
      <tr><td>Bitrate audio</td><td>128k</td><td>Buena calidad de audio para web</td></tr>
      <tr><td>Bitrate audio</td><td>96k</td><td>Aceptable para voz/podcasts, menor tamaño</td></tr>
    </tbody>
  </table>

  <div class="note">
    <strong>Nota:</strong> FFmpeg debe instalarse en el sistema (<code>sudo apt install ffmpeg</code> en Ubuntu/Debian, <code>brew install ffmpeg</code> en macOS). Los valores de CRF son específicos de cada códec: H.264 usa 0-51 (23 recomendado), VP9 usa 0-63 (30 recomendado).
  </div>
</body>
</html>
```

### Ejemplo Guiado 9: SVG inline con animación CSS y sprite

!!! example "Contexto pedagógico"
    Demostración del poder del SVG inline: iconos animados que cambian de color con la herencia de currentColor, sprites SVG con symbol/use, y animación de propiedades SVG con CSS.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ejemplo 9 - SVG Inline y Animaciones</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      padding: 2rem;
      background: #f8f9fa;
    }

    h1 { margin-bottom: 2rem; }
    section { background: #fff; padding: 1.5rem; border-radius: 12px; margin-bottom: 1.5rem; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }
    h2 { margin-bottom: 1rem; font-size: 1.1rem; }

    /*
     * ===== ICONOS CON COLOR HEREDADO =====
     * fill: currentColor hace que el SVG tome el color del texto del padre.
     * Esto permite cambiar el color del icono simplemente cambiando color en CSS.
     */
    .icon {
      width: 32px;
      height: 32px;
      fill: currentColor;
      vertical-align: middle;
    }

    .icon-red { color: #ef4444; }
    .icon-green { color: #10b981; }
    .icon-blue { color: #3b82f6; }
    .icon-large { width: 64px; height: 64px; }

    .icon-row {
      display: flex;
      gap: 1.5rem;
      align-items: center;
    }

    /*
     * ===== ANIMACIÓN DE RELLENO SVG =====
     * Podemos animar fill, stroke, transformaciones...
     */
    .heart-svg {
      width: 80px;
      height: 80px;
      fill: #ccc;
      transition: fill 0.3s, transform 0.3s;
      cursor: pointer;
    }

    .heart-svg:hover {
      fill: #ef4444;
      transform: scale(1.2);
    }

    /*
     * ===== ANIMACIÓN DE CAMPANITA (NOTIFICACIÓN) =====
     * La campana se balancea como si sonara.
     */
    .bell-svg {
      width: 48px;
      height: 48px;
      cursor: pointer;
      transform-origin: top center;
      animation: ring 4s ease-in-out infinite;
    }

    @keyframes ring {
      0%, 10% { transform: rotate(0); }
      2% { transform: rotate(20deg); }
      4% { transform: rotate(-15deg); }
      6% { transform: rotate(10deg); }
      8% { transform: rotate(-5deg); }
    }

    /*
     * ===== LOGO CON GRADIENTE ANIMADO =====
     * Usamos un gradient SVG definido en defs y animado con CSS.
     */
    .logo-svg {
      width: 200px;
      height: 80px;
    }

    .logo-gradient-start { stop-color: #667eea; animation: gradShift 3s ease-in-out infinite alternate; }
    .logo-gradient-end { stop-color: #764ba2; animation: gradShift2 3s ease-in-out infinite alternate; }

    @keyframes gradShift {
      from { stop-color: #667eea; }
      to { stop-color: #f5576c; }
    }

    @keyframes gradShift2 {
      from { stop-color: #764ba2; }
      to { stop-color: #f093fb; }
    }

    /* ===== SPRITE SVG ===== */
    .sprite-icon {
      width: 40px;
      height: 40px;
      fill: currentColor;
    }

    .sprite-row {
      display: flex;
      gap: 1rem;
      color: #6c5ce7;
    }

    @media (prefers-reduced-motion: reduce) {
      .bell-svg { animation: none; }
      .logo-gradient-start, .logo-gradient-end { animation: none; }
    }
  </style>
</head>
<body>
  <!--
    ===== SPRITE SVG OCULTO =====
    Definimos todos los iconos como <symbol> dentro de un SVG oculto.
    Luego los referenciamos con <use> donde los necesitemos.
    Esto evita repetir el código SVG y facilita el mantenimiento.
  -->
  <svg style="display: none;" aria-hidden="true">
    <!-- Icono: Casa -->
    <symbol id="icon-home" viewBox="0 0 24 24">
      <path d="M12 3L4 9v12h5v-7h6v7h5V9l-8-6z"/>
    </symbol>
    <!-- Icono: Usuario -->
    <symbol id="icon-user" viewBox="0 0 24 24">
      <path d="M12 12c2.7 0 4.8-2.1 4.8-4.8S14.7 2.4 12 2.4 7.2 4.5 7.2 7.2 9.3 12 12 12zm0 2.4c-3.2 0-9.6 1.6-9.6 4.8v2.4h19.2v-2.4c0-3.2-6.4-4.8-9.6-4.8z"/>
    </symbol>
    <!-- Icono: Configuración -->
    <symbol id="icon-settings" viewBox="0 0 24 24">
      <path d="M19.1 12.9a7.3 7.3 0 000-1.8l1.9-1.5c.2-.1.2-.4.1-.6l-1.8-3.1c-.1-.2-.4-.3-.6-.2l-2.3.9a6.7 6.7 0 00-1.6-.9L14.3 3c0-.3-.2-.5-.5-.5h-3.6c-.3 0-.5.2-.5.5l-.5 2.6c-.6.2-1.1.5-1.6.9l-2.3-.9c-.2-.1-.5 0-.6.2l-1.8 3.1c-.1.2-.1.4.1.6l1.9 1.5c-.1.6-.1 1.2 0 1.8l-1.9 1.5c-.2.1-.2.4-.1.6l1.8 3.1c.1.2.4.3.6.2l2.3-.9c.5.4 1 .7 1.6.9l.5 2.6c0 .3.2.5.5.5h3.6c.3 0 .5-.2.5-.5l.5-2.6c.6-.2 1.1-.5 1.6-.9l2.3.9c.2.1.5 0 .6-.2l1.8-3.1c.1-.2.1-.4-.1-.6l-1.9-1.5zM12 15.6c-2 0-3.6-1.6-3.6-3.6s1.6-3.6 3.6-3.6 3.6 1.6 3.6 3.6-1.6 3.6-3.6 3.6z"/>
    </symbol>
  </svg>

  <h1>SVG Inline, Sprites y Animaciones</h1>

  <!-- 1. ICONOS CON COLOR HEREDADO -->
  <section>
    <h2>1. Iconos con currentColor (color heredado del padre)</h2>
    <p style="margin-bottom:1rem;">El mismo icono SVG toma diferentes colores según la clase CSS del contenedor:</p>
    <div class="icon-row">
      <span class="icon-red" style="display:flex;align-items:center;gap:0.5rem;">
        <svg class="icon" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/></svg> Rojo
      </span>
      <span class="icon-green" style="display:flex;align-items:center;gap:0.5rem;">
        <svg class="icon" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/></svg> Verde
      </span>
      <span class="icon-blue" style="display:flex;align-items:center;gap:0.5rem;">
        <svg class="icon icon-large" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/></svg> Azul (grande)
      </span>
    </div>
  </section>

  <!-- 2. SPRITE SVG -->
  <section>
    <h2>2. Sprites SVG con symbol/use</h2>
    <p style="margin-bottom:1rem;">Los iconos se definen una vez y se usan múltiples veces por referencia:</p>
    <div class="sprite-row">
      <svg class="sprite-icon"><use href="#icon-home"/></svg>
      <svg class="sprite-icon"><use href="#icon-user"/></svg>
      <svg class="sprite-icon"><use href="#icon-settings"/></svg>
    </div>
  </section>

  <!-- 3. CORAZÓN ANIMADO -->
  <section>
    <h2>3. Icono de corazón con animación hover</h2>
    <svg class="heart-svg" viewBox="0 0 24 24">
      <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
    </svg>
    <p style="color:#666; margin-top:0.5rem;">Pasa el ratón para ver la animación</p>
  </section>

  <!-- 4. CAMPANITA -->
  <section>
    <h2>4. Icono de notificación animado (campana)</h2>
    <svg class="bell-svg" viewBox="0 0 24 24" fill="#f59e0b">
      <path d="M12 22c1.1 0 2-.9 2-2h-4c0 1.1.89 2 2 2zm6-6v-5c0-3.07-1.64-5.64-4.5-6.32V4c0-.83-.67-1.5-1.5-1.5s-1.5.67-1.5 1.5v.68C7.63 5.36 6 7.92 6 11v5l-2 2v1h16v-1l-2-2z"/>
    </svg>
    <p style="color:#666; margin-top:0.5rem;">La campana se balancea automáticamente</p>
  </section>

  <!-- 5. LOGO CON GRADIENTE ANIMADO -->
  <section>
    <h2>5. Logo con gradiente SVG animado</h2>
    <svg class="logo-svg" viewBox="0 0 200 80">
      <defs>
        <linearGradient id="logoGrad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" class="logo-gradient-start"/>
          <stop offset="100%" class="logo-gradient-end"/>
        </linearGradient>
      </defs>
      <rect x="10" y="15" width="50" height="50" rx="12" fill="url(#logoGrad)"/>
      <text x="75" y="55" font-family="Arial, sans-serif" font-size="28" font-weight="700" fill="url(#logoGrad)">LOGO</text>
    </svg>
    <p style="color:#666; margin-top:0.5rem;">Los colores del gradiente cambian cíclicamente</p>
  </section>
</body>
</html>
```

### Ejemplo Guiado 10: Efecto parallax y animaciones al hacer scroll

!!! example "Contexto pedagógico"
    Combinación de animaciones CSS con detección de scroll usando Intersection Observer. Los elementos aparecen con fade-in y slide-in cuando entran en el viewport, y un efecto parallax sutil en la sección hero. Todo con respeto a prefers-reduced-motion.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ejemplo 10 - Animaciones al hacer Scroll</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: 'Segoe UI', system-ui, sans-serif; background: #f5f5f5; }

    /*
     * ===== EFECTO PARALLAX EN EL HÉROE =====
     * La imagen de fondo se mueve más lentamente que el contenido
     * al hacer scroll, creando sensación de profundidad.
     * background-attachment: fixed es la forma más simple.
     */
    .hero {
      background: linear-gradient(135deg, #667eea, #764ba2);
      color: #fff;
      min-height: 70vh;
      display: flex;
      align-items: center;
      justify-content: center;
      text-align: center;
      padding: 2rem;
      /* Efecto parallax: la imagen (o gradiente) se queda fija */
      background-attachment: fixed;
      background-size: cover;
    }

    .hero h1 { font-size: clamp(2rem, 5vw, 3.5rem); margin-bottom: 1rem; }
    .hero p { font-size: 1.2rem; opacity: 0.9; max-width: 600px; }

    .section {
      padding: clamp(3rem, 8vw, 6rem) 2rem;
      max-width: 1100px;
      margin: 0 auto;
    }

    .section h2 { font-size: 2rem; margin-bottom: 2rem; text-align: center; }

    /* Grid de tarjetas */
    .cards {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 2rem;
    }

    .card {
      background: #fff;
      padding: 2rem;
      border-radius: 12px;
      box-shadow: 0 2px 12px rgba(0,0,0,0.06);
      /*
       * ===== ESTADO INICIAL PARA ANIMACIÓN =====
       * Los elementos empiezan ocultos (opacity: 0) y desplazados.
       * La clase .revealed (añadida por JS al entrar en viewport)
       * activa la transición al estado visible.
       */
      opacity: 0;
      transform: translateY(30px);
      transition: opacity 0.6s ease, transform 0.6s ease;
    }

    /* Estado visible: se activa cuando JS añade la clase */
    .card.revealed {
      opacity: 1;
      transform: translateY(0);
    }

    /* Efecto escalonado: cada tarjeta aparece con un pequeño retraso */
    .card:nth-child(1) { transition-delay: 0s; }
    .card:nth-child(2) { transition-delay: 0.1s; }
    .card:nth-child(3) { transition-delay: 0.2s; }
    .card:nth-child(4) { transition-delay: 0.3s; }
    .card:nth-child(5) { transition-delay: 0.4s; }
    .card:nth-child(6) { transition-delay: 0.5s; }

    .card__icon { font-size: 2.5rem; margin-bottom: 1rem; display: block; }
    .card h3 { margin-bottom: 0.5rem; }

    /* ===== RESPETAR PREFERENCIAS DE MOVIMIENTO ===== */
    @media (prefers-reduced-motion: reduce) {
      .hero { background-attachment: scroll; }
      .card {
        opacity: 1;
        transform: none;
        transition: none;
      }
    }
  </style>
</head>
<body>
  <!-- Héroe con parallax -->
  <section class="hero">
    <div>
      <h1>Animaciones al hacer Scroll</h1>
      <p>Los elementos aparecen con animaciones suaves cuando entran en el viewport. Haz scroll hacia abajo para ver el efecto.</p>
    </div>
  </section>

  <!-- Sección 1 -->
  <section class="section">
    <h2>Nuestros Servicios</h2>
    <div class="cards">
      <div class="card">
        <span class="card__icon">🎨</span>
        <h3>Diseño Web</h3>
        <p>Interfaces modernas y atractivas que cautivan a tus usuarios desde el primer momento.</p>
      </div>
      <div class="card">
        <span class="card__icon">💻</span>
        <h3>Desarrollo Frontend</h3>
        <p>Implementación con las tecnologías más modernas: React, Vue, TypeScript.</p>
      </div>
      <div class="card">
        <span class="card__icon">⚡</span>
        <h3>Optimización</h3>
        <p>Mejoramos el rendimiento de tu web para que cargue en menos de 2 segundos.</p>
      </div>
    </div>
  </section>

  <!-- Sección 2 -->
  <section class="section" style="background:#fff;">
    <h2>Tecnologías que usamos</h2>
    <div class="cards">
      <div class="card">
        <span class="card__icon">📐</span>
        <h3>CSS Grid & Flexbox</h3>
        <p>Maquetación moderna sin limitaciones. Layouts complejos con código limpio.</p>
      </div>
      <div class="card">
        <span class="card__icon">🎯</span>
        <h3>Tailwind CSS</h3>
        <p>Framework utility-first para desarrollar interfaces rápidamente.</p>
      </div>
      <div class="card">
        <span class="card__icon">🚀</span>
        <h3>Astro & Next.js</h3>
        <p>Frameworks modernos que combinan lo mejor del SSR y el static generation.</p>
      </div>
    </div>
  </section>

  <!-- Sección 3 -->
  <section class="section">
    <h2>¿Por qué elegirnos?</h2>
    <div class="cards">
      <div class="card">
        <span class="card__icon">🤝</span>
        <h3>Compromiso</h3>
        <p>Nos involucramos en cada proyecto como si fuera nuestro.</p>
      </div>
      <div class="card">
        <span class="card__icon">📅</span>
        <h3>Puntualidad</h3>
        <p>Entregamos en los plazos acordados. Siempre.</p>
      </div>
      <div class="card">
        <span class="card__icon">💬</span>
        <h3>Comunicación</h3>
        <p>Te mantenemos informado durante todo el proceso de desarrollo.</p>
      </div>
    </div>
  </section>

  <script>
    /*
     * ===== INTERSECTION OBSERVER =====
     * API nativa del navegador para detectar cuándo un elemento
     * entra o sale del viewport. Mucho más eficiente que escuchar
     * el evento scroll (que se dispara constantemente).
     *
     * Configuración:
     * - threshold: 0.1 = se activa cuando al menos el 10% del elemento es visible
     * - rootMargin: '0px 0px -50px 0px' = se activa 50px antes de que el
     *   elemento entre completamente (efecto anticipatorio)
     */
    const observerOptions = {
      threshold: 0.1,
      rootMargin: '0px 0px -50px 0px'
    };

    /*
     * Callback del observer:
     * Se ejecuta cada vez que un elemento observado cruza el umbral.
     * entries es un array con todos los elementos que cambiaron de estado.
     */
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          // El elemento ha entrado en el viewport: añadimos la clase
          entry.target.classList.add('revealed');
          // Dejamos de observar este elemento (solo se anima una vez)
          observer.unobserve(entry.target);
        }
      });
    }, observerOptions);

    // Observamos todas las tarjetas
    document.querySelectorAll('.card').forEach(card => {
      observer.observe(card);
    });
  </script>
</body>
</html>
```


## Casos reales

### Caso 1: Apple - Excelencia en multimedia web

Apple es el referente mundial en integración multimedia web. Su página de producto (por ejemplo, del iPhone o MacBook) utiliza imágenes de producto de altísima calidad servidas mediante `<picture>` con múltiples resoluciones y formatos (**AVIF** para navegadores modernos, **JPEG** como fallback). Las imágenes de producto se cargan progresivamente: primero una versión de baja resolución que se muestra como placeholder, y cuando el usuario hace scroll, se cargan las versiones de alta resolución usando **Intersection Observer**. Apple fue pionero en el uso de vídeos de fondo en héroe (`autoplay`, `muted`, `loop`, sin controles) para demostrar productos en movimiento, siempre con el atributo `playsinline` para dispositivos móviles. Sus animaciones de scroll (elementos que aparecen, imágenes que se transforman) están implementadas con JavaScript de alto rendimiento que respeta `prefers-reduced-motion`. El detalle más impresionante es su uso de secuencias de imágenes (**sprite sheets**) animadas con JavaScript al hacer scroll para crear la ilusión de que el producto gira en 3D mientras el usuario se desplaza por la página, una técnica que logra un impacto visual extraordinario con un peso de archivo mínimo (un solo PNG de sprites en lugar de un vídeo de varios megas). También son ejemplares en accesibilidad: todas las imágenes tienen atributos `alt` descriptivos redactados por especialistas, y los vídeos incluyen subtítulos y descripciones de audio.

### Caso 2: Netflix - Streaming y optimización de vídeo

Netflix es el caso de estudio definitivo en optimización de vídeo a gran escala. Aunque su reproductor es una aplicación compleja, los principios que aplica son directamente relevantes para la web. Netflix codifica cada título en **más de 20 versiones diferentes**:

- **Múltiples resoluciones** — desde **240p** hasta **4K HDR**.
- **Múltiples códecs** — **AV1** para dispositivos modernos, **H.264/HEVC** para compatibilidad.
- **Múltiples bitrates**.

El reproductor selecciona dinámicamente la versión óptima según la conexión del usuario usando **streaming adaptativo (DASH)**. Para la web, su página de inicio utiliza imágenes de carátulas en formato **AVIF/WebP** con `loading="lazy"` y `decoding="async"` para optimizar la carga. Los avances (trailers) en la ficha de cada título usan vídeos cortos con `autoplay muted playsinline` y se detienen automáticamente al salir del viewport (usando Intersection Observer para pausar la reproducción), ahorrando ancho de banda. Su interfaz de usuario emplea microinteracciones sutiles: las carátulas se agrandan ligeramente al pasar el ratón o al hacer foco con teclado, con una transición de `transform: scale(1.1)` que no afecta al layout (la escala en transform no modifica el flujo del documento). También implementan skeleton screens (placeholders animados) mientras se cargan las imágenes, mejorando la percepción de velocidad.

### Caso 3: Medium - Imágenes, rendimiento y experiencia de lectura

Medium es la plataforma de publicación que mejor equilibra contenido textual y multimedia. Su enfoque en la experiencia de lectura les ha llevado a implementar una estrategia de carga de imágenes ejemplar. Utilizan placeholders de baja calidad (**LQIP** - Low Quality Image Placeholders): una versión extremadamente comprimida y borrosa de la imagen (típicamente un JPEG de **~200 bytes** en base64) que se muestra inmediatamente mientras la imagen real se carga de forma diferida. La transición entre el placeholder borroso y la imagen nítida (efecto «blur-up») crea una experiencia de carga muy pulida. Las imágenes dentro de los artículos usan `loading="lazy"` y el ancho máximo está limitado con CSS para no exceder el ancho de lectura óptimo. Los GIFs animados se convierten automáticamente a vídeos MP4 (mucho más eficientes: un GIF de **5MB** puede convertirse en un MP4 de **500KB** con la misma calidad visual), una práctica que debería ser estándar en la industria. Medium también destaca por sus animaciones sutiles:

- **Botones de aplauso** — microinteracción de confeti.
- **Menú de navegación** — aparece/desaparece con transición al hacer scroll.
- **Imágenes de los artículos** — se amplían en un lightbox con animación de zoom.

Todas estas animaciones respetan `prefers-reduced-motion`. Su modo oscuro está implementado con `prefers-color-scheme` y ajusta no solo los colores de fondo y texto, sino también el brillo y contraste de las imágenes.

## Actividades guiadas

### Actividad Guiada 1: Optimizar una galería de imágenes para un sitio web

El alumnado partirá de una galería con imágenes sin optimizar (JPEG a máxima calidad, 4000px de ancho, sin lazy loading) y la transformará en una galería profesional optimizada. Los pasos incluyen: usar Squoosh para generar versiones WebP a 400px, 800px y 1200px de ancho con compresión al 75%; implementar `<picture>` con `<source>` WebP y fallback JPEG; añadir `srcset` y `sizes` para cada imagen; aplicar `loading="lazy"` y `decoding="async"`; añadir `width` y `height` para evitar layout shift; y comparar el peso total de la página antes y después usando las herramientas de desarrollo. Se medirá la puntuación Lighthouse en móvil antes y después de la optimización.

### Actividad Guiada 2: Añadir subtítulos y transcripción a un vídeo

El alumnado trabajará con un vídeo de ejemplo para el que deberá crear subtítulos en formato WebVTT. Los pasos: visionar el vídeo y transcribir el audio con marcas de tiempo; crear el archivo `.vtt` con el formato correcto (WEBVTT header, marcas de tiempo en formato HH:MM:SS.mmm, texto del subtítulo); asociar el archivo al elemento `<video>` con `<track>`; probar los subtítulos en el navegador; crear una transcripción textual completa en HTML debajo del reproductor; y añadir descripciones de audio para elementos visuales importantes. Se verificará la accesibilidad con un lector de pantalla.

### Actividad Guiada 3: Construir un reproductor de audio personalizado

El alumnado creará un reproductor de audio con controles personalizados usando la API de HTML5. Partiendo de un elemento `<audio>` básico, diseñarán una interfaz con botones de play/pause, barra de progreso interactiva, control de volumen, y display de tiempo actual/total. Usarán los eventos `play`, `pause`, `timeupdate`, `loadedmetadata` y `ended` para sincronizar la interfaz con el estado de reproducción. Implementarán atajos de teclado (espacio para play/pause, flechas para avanzar/retroceder). Estilarán el reproductor para que sea responsive y accesible.

### Actividad Guiada 4: Crear animaciones de carga (spinner y skeleton)

El alumnado desarrollará un conjunto de animaciones de carga reutilizables. Implementarán: un spinner circular con `@keyframes` y `border-top` coloreado; un loader de tres puntos con `animation-delay` escalonado; un skeleton loader (placeholders que simulan texto, imágenes y avatares) con gradiente animado; y las integrarán en una interfaz de ejemplo. Discutirán cuándo usar cada tipo de loader según el contexto (spinner para acciones del sistema, skeleton para carga de páginas, dots para procesos breves). Aprenderán a respetar `prefers-reduced-motion` desactivando las animaciones.

### Actividad Guiada 5: Implementar animaciones de entrada al hacer scroll

El alumnado añadirá animaciones de revelación a una página existente. Usando Intersection Observer, detectarán cuándo los elementos entran en el viewport y añadirán clases CSS que activen animaciones de fade-in y slide-in. Crearán variantes de animación (desde izquierda, derecha, abajo, fade) y aplicarán retrasos escalonados para crear un efecto de cascada. Medirán el impacto en el rendimiento usando las herramientas de desarrollo (pestaña Rendimiento) y verificarán que las animaciones se desactivan con `prefers-reduced-motion`.

## Actividades propuestas

### Actividad Propuesta 1: Sitio de portafolio fotográfico con galería optimizada

Diseña y desarrolla un portafolio fotográfico online que demuestre el dominio de las técnicas de optimización de imágenes. La galería debe incluir al menos 12 fotografías con: versiones WebP y JPEG en 3 resoluciones cada una, lazy loading con Intersection Observer (para control más fino que el nativo), placeholders LQIP (blur-up), y lightbox con zoom animado al hacer clic en una imagen. El sitio debe incorporar una página "Sobre mí" con una imagen de perfil en formato AVIF/WebP con fallback y una sección de servicios con iconos SVG animados. Implementa el modo oscuro con `prefers-color-scheme`. Entrega el código completo y un documento explicando las decisiones de optimización tomadas para cada imagen.

### Actividad Propuesta 2: Plataforma de podcast con reproductor de audio avanzado

Crea la interfaz de una plataforma de podcast o audiolibros. Debe incluir: lista de episodios con carátulas, reproductor de audio persistente en la parte inferior (como Spotify), controles de reproducción personalizados (play/pause, avance/retroceso 15s, velocidad de reproducción 0.5x-2x), barra de progreso con buffer visual, y guardado de la posición de escucha en localStorage. Los episodios deben proporcionar transcripciones textuales sincronizadas (pueden ser estáticas de ejemplo). Implementa accesibilidad completa: navegación por teclado, etiquetas ARIA en los controles, y transcripciones visibles. El diseño debe ser responsive Mobile First.

### Actividad Propuesta 3: Animación de logo y pantalla de carga para una startup

Diseña e implementa la pantalla de carga animada (splash screen) y el logo animado de una startup tecnológica. La animación debe incluir: un logotipo SVG que se dibuja solo usando la técnica de stroke-dasharray/dashoffset, un eslogan que aparece con fade-in después del logo, y una transición suave a la página principal. Crea también versiones alternativas del logo: una versión estática para la cabecera del sitio, una versión animada sutil para el footer (usando la etiqueta `<use>` del sprite SVG para no duplicar código), y una versión para el modo oscuro con colores diferentes usando `currentColor`. Todo el sitio debe respetar `prefers-reduced-motion`.

### Actividad Propuesta 4: Microinteracciones para una aplicación de tareas

Implementa un conjunto de microinteracciones para una aplicación de gestión de tareas (to-do list). Las interacciones deben incluir: animación al añadir una nueva tarea (slide-in desde arriba), animación al completar una tarea (tachado con línea que se dibuja + desplazamiento suave al final de la lista), animación al eliminar una tarea (fade-out + colapso de altura), botón de "marcar todas como completadas" con efecto de onda expansiva, y contador de tareas pendientes con animación de número que cambia (efecto de slot machine). Las animaciones deben ser sutiles y funcionales, mejorando la comprensión de lo que está sucediendo en la interfaz. Implementa usando solo CSS para las animaciones simples y JavaScript mínimo para las interacciones que requieran lógica.

### Actividad Propuesta 5: Vídeo corporativo con reproductor personalizado y accesibilidad

Desarrolla una página para el vídeo corporativo de una empresa con un reproductor de vídeo personalizado completo. El reproductor debe incluir: controles personalizados (play/pause, volumen, progreso, pantalla completa, velocidad), atajos de teclado documentados, subtítulos en 2 idiomas (archivos WebVTT), botón para activar/desactivar descripción de audio, y transcripción completa con resaltado de la frase actual (usando el evento `cuechange` del track). La página debe tener: héroe con el vídeo como fondo (autoplay muted loop), sección "Sobre el proyecto" con imágenes optimizadas, y galería de fotogramas del vídeo. Optimiza el vídeo en al menos 2 resoluciones y 2 formatos (MP4 y WebM). Implementa carga lazy del vídeo principal con Intersection Observer para no penalizar el rendimiento.

## Actividades de ampliación

### Actividad de Ampliación 1: Pipeline de optimización multimedia automatizado

Investiga y configura un sistema automatizado de optimización multimedia para un proyecto web. Integra herramientas como Sharp (para imágenes), SVGO (para iconos SVG) y FFmpeg (para vídeo) en un flujo de trabajo con Node.js. Crea un script `optimizar-medios.js` que: recorra todas las imágenes del proyecto, genere versiones WebP y AVIF en 3 resoluciones, comprima JPEGs originales, optimice archivos SVG eliminando metadatos y reduciendo precisión, y genere versiones comprimidas de vídeos en MP4 y WebM. El script debe aceptar parámetros de configuración (calidad, resoluciones, formatos) y mostrar un informe con estadísticas de ahorro (peso original vs optimizado, porcentaje de reducción). Documenta el proceso de instalación y uso para que pueda ser adoptado por otros desarrolladores del equipo.

### Actividad de Ampliación 2: Estudio comparativo de rendimiento de formatos de imagen

Realiza un estudio científico comparando el rendimiento de los formatos de imagen JPEG, PNG, WebP y AVIF. Selecciona 10 imágenes de diferentes categorías (fotografía de paisaje, retrato, captura de pantalla con texto, ilustración con áreas planas, imagen con transparencia, imagen con gradiente, logotipo, fotografía nocturna, imagen con mucho detalle, meme/texto sobre imagen). Para cada imagen: genera versiones en los 4 formatos, ajusta la calidad/compresión para que todas tengan un SSIM (índice de similitud estructural) similar (>0.95 respecto al original), mide el tamaño de archivo resultante, y calcula el porcentaje de ahorro respecto al JPEG base. Presenta los resultados en tablas y gráficos. Determina en qué casos cada formato es óptimo. Publica el estudio como artículo en formato Markdown con las imágenes de ejemplo y las tablas de datos.

### Actividad de Ampliación 3: Componente Lottie interactivo

Aprende a crear y utilizar animaciones Lottie. Instala la extensión Bodymovin para After Effects (o usa una herramienta online compatible) y crea una animación sencilla (un icono animado, una pantalla de carga, o una ilustración con movimiento). Exporta la animación como JSON. Integra el archivo en una página web usando la librería lottie-web. Implementa interactividad: controla la reproducción con botones (play, pause, stop), cambia la velocidad de la animación con un slider, y sincroniza la animación con el scroll (la animación avanza a medida que el usuario se desplaza). Compara el peso del JSON de Lottie con el que tendría la misma animación en formato GIF y en formato MP4. Documenta las ventajas e inconvenientes de cada formato para animaciones web.

## Buenas prácticas

1. **Usa `<picture>` con múltiples `<source>` para servir el formato óptimo**: Comienza con AVIF (mejor compresión), luego WebP (excelente soporte), y finalmente JPEG/PNG como fallback. Esto reduce el peso de las imágenes entre un 50% y un 70% sin pérdida visual apreciable.

2. **Proporciona siempre `alt` en las imágenes**: `alt=""` para imágenes decorativas (los lectores de pantalla las ignoran), `alt="descripción significativa"` para imágenes de contenido. Un buen texto alternativo describe la función o información de la imagen, no su apariencia literal. Evita "foto de..." o "imagen de..."; el lector de pantalla ya anuncia que es una imagen.

3. **Nunca uses `autoplay` sin `muted`**: Las políticas de autoplay de los navegadores bloquean la reproducción automática con sonido. El atributo `playsinline` es necesario en iOS para que el vídeo se reproduzca en línea (sin abrir el reproductor nativo a pantalla completa).

4. **Optimiza las animaciones para GPU**: Anima exclusivamente `transform` (translate, scale, rotate) y `opacity`. Estas propiedades solo requieren composición (la etapa más barata del pipeline de renderizado). Evita animar `width`, `height`, `margin`, `top/left`, o `box-shadow`, que disparan recálculos de layout o repintado.

5. **Implementa `prefers-reduced-motion` siempre**: No es opcional. Desactiva o reduce drásticamente las animaciones cuando el usuario ha expresado esta preferencia en su sistema operativo. Esto afecta aproximadamente al 5% de los usuarios y es un requisito de accesibilidad WCAG 2.2.

6. **Usa `loading="lazy"` en imágenes y iframes fuera del viewport**: El atributo nativo es soportado por todos los navegadores modernos y es más simple y eficiente que las soluciones basadas en JavaScript. Combínalo con `fetchpriority="high"` en la imagen LCP (generalmente el héroe) para priorizar la carga de lo más importante.

7. **Añade subtítulos y transcripciones a todo el contenido de vídeo y audio**: Los subtítulos no solo benefician a personas con discapacidad auditiva, sino también a quienes consumen contenido en entornos ruidosos, en transporte público, o en silencio (bibliotecas, oficinas). Las transcripciones textuales mejoran el SEO y permiten buscar dentro del contenido.

8. **Comprime siempre los recursos multimedia antes de publicarlos**: Las imágenes y vídeos sin comprimir son la principal causa de sitios web lentos. Integra la compresión en el flujo de trabajo (Squoosh para trabajo manual, Sharp para automatización, plugins de Vite/Webpack para build). Nunca publiques imágenes directamente de una cámara o de un diseñador sin optimizar.

9. **Usa SVG para iconos, logotipos e ilustraciones vectoriales**: SVG es superior a las fuentes de iconos (Font Awesome, Material Icons) en accesibilidad, rendimiento y control. Con `currentColor` los iconos heredan el color del texto. Con `<symbol>` y `<use>` evitas duplicar código. Con CSS puedes animar cualquier propiedad del SVG.

10. **Mide el rendimiento multimedia con Lighthouse y WebPageTest**: Establece presupuestos de rendimiento (p.ej. "la página completa no debe superar 1.5MB, las imágenes no más de 500KB en total") y verifica en cada iteración. Presta especial atención a las métricas LCP (Largest Contentful Paint) y CLS (Cumulative Layout Shift), directamente afectadas por cómo gestionas las imágenes y vídeos.

## Errores frecuentes

1. **Servir imágenes con dimensiones mucho mayores que el espacio de visualización**: Una imagen de 4000px de ancho mostrada en un contenedor de 400px obliga al navegador a descargar, decodificar y redimensionar datos innecesarios. Usa `srcset` con múltiples resoluciones y genera versiones específicas para cada tamaño de visualización.

2. **Usar solo JPEG para todo tipo de imágenes**: JPEG no soporta transparencia y produce artefactos visibles en imágenes con texto o bordes nítidos (capturas de pantalla, logotipos). Para estos casos, PNG o WebP lossless son superiores. Para fotografías, WebP o AVIF reducen el tamaño un 30-50% respecto a JPEG sin pérdida de calidad.

3. **Autoplay con sonido sin consentimiento del usuario**: Los navegadores bloquean automáticamente la reproducción con audio no iniciada por el usuario. Vídeos de fondo o decorativos deben usar `autoplay muted loop playsinline`. Para contenido donde el audio es esencial, el usuario debe iniciar la reproducción explícitamente.

4. **Olvidar establecer `width` y `height` en las imágenes**: Sin dimensiones explícitas, el navegador no puede reservar espacio para la imagen, causando layout shift cuando la imagen termina de cargar (el contenido salta). Esto penaliza gravemente la métrica CLS de Core Web Vitals. `width` y `height` + `aspect-ratio` en CSS solucionan este problema.

5. **Animar propiedades que fuerzan layout o paint**: `width`, `height`, `margin`, `padding`, `top`, `left`, `box-shadow` son propiedades costosas de animar. Causan jank (tartamudeo) especialmente en dispositivos móviles. Usa `transform` y `opacity` para animaciones fluidas a 60fps.

6. **No incluir `playsinline` en vídeos para iOS**: Sin este atributo, Safari en iPhone abre el vídeo a pantalla completa, sacando al usuario del contexto de la página. Es necesario para cualquier vídeo que deba reproducirse en su ubicación natural dentro del layout.

7. **Usar GIFs animados en lugar de vídeos**: Un GIF de 5 segundos puede pesar 3-8 MB; el mismo contenido como MP4 pesa 300-800 KB. Los GIFs están limitados a 256 colores (bandas de color visibles), no soportan audio, y su compresión es extremadamente ineficiente. Siempre prefiere `<video>` para contenido animado.

8. **Ignorar el formato de los subtítulos WebVTT**: Errores comunes incluyen: olvidar la cabecera `WEBVTT` (obligatoria), usar el formato de tiempo incorrecto (`00:01:00.000`, no `1:00`), no separar los bloques con líneas en blanco, o incluir texto sin marcas de tiempo. Valida los archivos VTT con herramientas como el validador del W3C.

9. **No proporcionar fallback para formatos modernos**: Servir solo WebP o AVIF sin fallback JPEG/PNG rompe las imágenes en navegadores que no soportan estos formatos (aunque son pocos, existen). El elemento `<picture>` con múltiples `<source>` resuelve esto elegantemente.

10. **Animar sin considerar el contexto del usuario**: Animaciones que se disparan automáticamente, que duran demasiado, o que distraen del contenido principal degradan la experiencia. Toda animación debe tener un propósito (comunicar un cambio de estado, guiar la atención, proporcionar feedback) y ser lo suficientemente sutil para no molestar en usos repetidos.

## Resumen

La integración de contenido multimedia en la web es mucho más que insertar imágenes y vídeos en una página. Requiere un conocimiento profundo de formatos, técnicas de optimización, estrategias de carga, consideraciones de accesibilidad y mejores prácticas de rendimiento. A lo largo de esta unidad hemos cubierto todos estos aspectos, desde los fundamentos de los formatos de imagen (JPEG, PNG, SVG, WebP, AVIF) hasta técnicas avanzadas como animaciones SVG con stroke-dasharray, microinteracciones con CSS y JavaScript, y optimización de vídeo con FFmpeg.

Los puntos clave que el alumnado debe retener son: (1) la elección del formato multimedia correcto para cada contexto es una decisión de diseño con impacto directo en el rendimiento; (2) las imágenes responsive con `<picture>`, `srcset` y `sizes` no son opcionales sino imprescindibles en la web moderna; (3) la accesibilidad multimedia (alt, subtítulos, transcripciones) es un requisito, no una mejora; (4) las animaciones deben usar propiedades aceleradas por GPU y respetar las preferencias del usuario; (5) la optimización multimedia (compresión, lazy loading, formatos modernos) debe formar parte del flujo de trabajo habitual, no ser una tarea de última hora.

La tendencia en la industria apunta hacia formatos cada vez más eficientes (AVIF desbancará a JPEG y WebP progresivamente), animaciones más inteligentes (Lottie para animaciones vectoriales complejas, CSS para las simples) y herramientas de automatización que integran la optimización multimedia en el proceso de build, eliminando la fricción para el desarrollador.

## Recursos complementarios

- **Squoosh (https://squoosh.app/)**: Aplicación web progresiva de Google para comprimir imágenes de forma visual e interactiva. Permite comparar lado a lado el original y el optimizado, ajustar calidad, cambiar de formato, redimensionar, y ver el peso resultante. Imprescindible para trabajo manual con imágenes.

- **MDN Web Docs - Elementos multimedia (https://developer.mozilla.org/es/docs/Web/HTML/Elemento/video)**: Documentación oficial completa de los elementos `<video>`, `<audio>`, `<img>`, `<picture>` y `<track>` con ejemplos y tablas de compatibilidad.

- **FFmpeg (https://ffmpeg.org/)**: La navaja suiza del procesamiento multimedia. Software libre para convertir, comprimir, redimensionar y manipular audio y vídeo desde línea de comandos. Aprender los comandos básicos de FFmpeg es una inversión que todo desarrollador web debería hacer.

- **LottieFiles (https://lottiefiles.com/)**: Plataforma con miles de animaciones Lottie gratuitas y editor online. Permite explorar, personalizar y descargar animaciones para usar en proyectos web. Ideal para encontrar inspiración y recursos.

- **WebAIM - Accesibilidad multimedia**: Guías prácticas para implementar alternativas textuales, subtítulos, descripciones de audio y transcripciones cumpliendo con WCAG.

- **Can I Use (https://caniuse.com/)**: Verifica el soporte de formatos multimedia en navegadores: WebP, AVIF, WebM, VP9, AV1, Opus, etc. Datos actualizados diariamente.

- **SVGOMG (https://jakearchibald.github.io/svgomg/)**: Interfaz visual para SVGO, la herramienta de optimización de SVG. Muestra el resultado de la optimización en tiempo real y permite activar/desactivar plugins individualmente.

- **Lighthouse - Performance**: Herramienta de auditoría integrada en Chrome DevTools. Evalúa la optimización de imágenes (recomienda formatos modernos, lazy loading, dimensiones correctas), el tamaño de los recursos multimedia y el impacto en las Core Web Vitals.

- **Web Vitals - Guía de LCP (https://web.dev/articles/lcp)**: Documentación oficial de Google sobre cómo optimizar el Largest Contentful Paint, la métrica más afectada por la carga de imágenes y vídeos. Incluye estrategias específicas para recursos multimedia.

- **Curso "Animaciones CSS Profesionales" de freeCodeCamp**: Tutorial gratuito en vídeo que cubre desde los fundamentos de `@keyframes` hasta animaciones complejas con rendimiento óptimo, incluyendo `cubic-bezier()` y `steps()`.
