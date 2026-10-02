---
icon: lucide/mouse-pointer-click
---

# Unidad 13: Interactividad Web

## Objetivos de aprendizaje

Al finalizar esta unidad, el alumnado será capaz de:

- Comprender el concepto de interactividad web y distinguirlo de la mera animación visual, valorando su impacto en la experiencia de usuario (UX) y su papel esencial en la construcción de interfaces modernas, responsivas y atractivas que fidelizan al usuario.
- Identificar, manejar y delegar los principales eventos JavaScript en interfaces de usuario (ratón, teclado, táctiles, formularios, scroll y resize) aplicando las opciones avanzadas de `addEventListener` (`once`, `passive`, `capture`) para optimizar el rendimiento y la experiencia en dispositivos móviles.
- Diseñar e implementar microinteracciones completas que incluyan los cuatro elementos fundamentales definidos por Dan Saffer: disparador, reglas, retroalimentación y bucles/modos, comprendiendo cómo cada uno contribuye a una experiencia de usuario memorable y a la percepción de calidad del producto digital.
- Crear animaciones de interfaz mediante transiciones CSS (`transition`), animaciones con `@keyframes` y la API Web Animations (`element.animate()`), decidiendo la técnica más adecuada según el caso de uso y las necesidades específicas de control, rendimiento y mantenibilidad.
- Construir componentes interactivos completos (carruseles accesibles, acordeones FAQ, sistemas de tabs con indicador animado, modales con trampa de foco, galerías con lightbox, formularios con validación en tiempo real, notificaciones toast, dark mode toggle con persistencia, scroll reveal y drag and drop) con código HTML, CSS y JavaScript funcional, comentado en español y siguiendo las mejores prácticas profesionales de desarrollo.
- Aplicar técnicas de optimización del rendimiento en interacciones (debounce, throttle, `requestAnimationFrame`, `will-change`, Intersection Observer) evitando el layout thrashing y garantizando animaciones fluidas a 60 fps incluso en dispositivos de gama media-baja.
- Integrar buenas prácticas de accesibilidad en cada componente interactivo desarrollado: gestión del foco, regiones aria-live, trampas de foco en modales, navegación por teclado completa y anuncio de cambios de estado mediante atributos ARIA (`aria-expanded`, `aria-selected`, `aria-pressed`, `aria-current`), cumpliendo con las pautas WCAG 2.1 nivel AA.
- Evaluar la interactividad de sitios web reales como Twitter, Notion y Linear, analizando críticamente las decisiones de diseño, la implementación técnica, el balance entre funcionalidad y rendimiento, y la atención al detalle en las microinteracciones.

## Relación con los Resultados de Aprendizaje

Esta unidad contribuye de manera directa a los siguientes Resultados de Aprendizaje oficiales del módulo 0615 *Diseño de interfaces web* (RD 405/2023, BOE; currículo andaluz):

- **RA1: Planifica la creación de una interfaz web valorando y aplicando especificaciones de diseño.** La selección de estilos de interactividad, la definición de microinteracciones, la planificación de los eventos necesarios y la elección de técnicas de animación forman parte esencial de la fase de diseño y planificación de cualquier interfaz web moderna. El alumnado aprende a anticipar las necesidades de interacción del usuario y a plasmarlas en un plan técnico viable antes de escribir una sola línea de código, considerando las restricciones de rendimiento y accesibilidad.
- **RA2: Crea interfaces web homogéneos definiendo y aplicando estilos.** La implementación de componentes interactivos con CSS y JavaScript manteniendo una experiencia coherente en toda la aplicación contribuye directamente a la homogeneidad visual y funcional de la interfaz. Se insiste en la creación de patrones de interacción reutilizables y la utilización de variables CSS y sistemas de diseño que aseguren que cada componente se comporte de forma predecible y consistente; las transiciones CSS y las animaciones con `@keyframes` extienden las capacidades de las hojas de estilo para dotar de dinamismo y retroalimentación visual a los componentes, permitiendo estados intermedios y transiciones entre estados sin sacrificar la mantenibilidad del código CSS.
- **RA4: Integra contenido multimedia en documentos web valorando su aportación y seleccionando adecuadamente los elementos interactivos.** Esta unidad desarrolla de forma intensiva y práctica la integración de interactividad con JavaScript y CSS, cubriendo componentes esenciales como carruseles, modales, galerías, formularios dinámicos y sistemas de notificaciones, todos ellos implementados con código completo, funcional y desplegable en cualquier proyecto web real.
- **RA5: Desarrolla interfaces web accesibles, analizando las pautas establecidas y aplicando técnicas de verificación.** Los criterios de accesibilidad se integran transversalmente en cada componente interactivo desarrollado durante la unidad. El alumnado aprende que la accesibilidad no es una característica adicional sino un requisito inherente al desarrollo de cualquier componente, implementando gestión del foco, navegación por teclado, roles y atributos ARIA como parte natural del proceso de desarrollo.
- **RA6: Desarrolla interfaces web amigables analizando y aplicando las pautas de usabilidad establecidas.** Las microinteracciones bien diseñadas, la retroalimentación inmediata a las acciones del usuario y los patrones de diseño consistentes mejoran directamente la usabilidad y reducen la carga cognitiva, contribuyendo a interfaces más intuitivas, eficientes y satisfactorias que los usuarios disfrutan utilizar.

## Conocimientos previos

Antes de abordar esta unidad, el alumnado debe dominar los siguientes conocimientos:

- **HTML semántico avanzado:** Estructura completa de documentos HTML5 con uso correcto de etiquetas semánticas (`section`, `article`, `nav`, `main`, `header`, `footer`, `aside`), formularios completos con todos sus tipos de campo (`input` de tipo text, email, password, number, date, checkbox, radio, file, range, search, tel, url; `select` con `optgroup`; `textarea`; `datalist`; `output`; `progress`; `meter`), atributos globales (`id`, `class`, `data-*`, `tabindex`, `aria-*`, `hidden`, `title`, `lang`, `dir`) y anidamiento válido según las especificaciones del W3C. Es fundamental comprender la diferencia entre elementos de bloque y en línea, el modelo de formulario, y los atributos de validación nativos (`required`, `pattern`, `min`, `max`, `minlength`, `maxlength`, `step`), ya que en esta unidad los utilizaremos para crear formularios con validación en tiempo real que combinen las capacidades nativas del navegador con retroalimentación visual personalizada.

- **CSS avanzado:** Dominio completo del modelo de cajas (box model con `box-sizing: border-box`), posicionamiento en todas sus variantes (`relative`, `absolute`, `fixed`, `sticky`), Flexbox (propiedades del contenedor: `display: flex`, `flex-direction`, `flex-wrap`, `justify-content`, `align-items`, `align-content`, `gap`; propiedades de los hijos: `flex-grow`, `flex-shrink`, `flex-basis`, `order`, `align-self`) y CSS Grid (`grid-template-columns`, `grid-template-rows`, `grid-template-areas`, `grid-column`, `grid-row`, `gap`, función `fr`, `minmax`, `auto-fill`, `auto-fit`). Manejo de variables CSS (`--custom-property` y `var()`), pseudoclases (`:hover`, `:focus`, `:active`, `:focus-visible`, `:focus-within`, `:checked`, `:disabled`, `:enabled`, `:nth-child`, `:first-child`, `:last-child`, `:not()`, `:is()`, `:where()`), pseudoelementos (`::before`, `::after`, `::placeholder`, `::selection`) y comprensión profunda de la especificidad y la cascada. Conocimiento de media queries (`@media`) y diseño responsive con unidades relativas (`em`, `rem`, `vw`, `vh`, `%`, `ch`, `dvh`, `svh`).

- **JavaScript fundamental (ES6+):** Sintaxis moderna incluyendo arrow functions, template literals, destructuring de objetos y arrays, operadores spread/rest, parámetros por defecto, módulos ES6 (`import`/`export`), promesas (`async`/`await`), y clases. Manejo del DOM: selección de elementos (`querySelector`, `querySelectorAll`, `getElementById`, `getElementsByClassName`), creación y manipulación de nodos (`createElement`, `appendChild`, `insertBefore`, `removeChild`, `replaceChild`, `insertAdjacentHTML`, `cloneNode`), manipulación de clases (`classList.add`, `remove`, `toggle`, `contains`, `replace`), atributos (`setAttribute`, `getAttribute`, `removeAttribute`, `hasAttribute`, manipulación de `dataset`), estilos inline (`element.style.propiedad`, `getComputedStyle`), y contenido (`textContent`, `innerHTML`, `innerText`). Manejo de eventos con `addEventListener`, `removeEventListener`, el objeto `event` y sus métodos (`preventDefault`, `stopPropagation`). Comprensión de closures, ámbito de variables (`let`, `const`, `var`) y el bucle de eventos (event loop). Familiaridad con `localStorage` y `sessionStorage` para la persistencia de preferencias.

- **Control de versiones con Git:** Manejo práctico de repositorios: `git init`, `git clone`, `git add`, `git commit -m`, `git push`, `git pull`, `git branch`, `git checkout`, `git merge`, `git status`, `git log`, `git diff`. Comprensión del flujo de trabajo básico y resolución de conflictos simples.

- **Herramientas de desarrollo del navegador:** Uso fluido de las DevTools de Chrome/Firefox para inspeccionar y modificar el DOM en tiempo real, depurar JavaScript con breakpoints, analizar el rendimiento en la pestaña Performance, auditar accesibilidad con Lighthouse, simular dispositivos móviles y condiciones de red en modo responsive, y trabajar con la consola para ejecutar código y visualizar logs.

## Contenidos

### 1. Fundamentos de la interactividad web
1.1. Definición de interactividad web. Diferencias con animación pasiva.
1.2. Importancia de la interactividad en la experiencia de usuario (UX): retroalimentación, guía de atención, reducción de carga cognitiva, percepción de velocidad, satisfacción emocional.
1.3. Tipos de interactividad: reactiva (respuesta a acciones), proactiva (anticipación de necesidades) y predictiva (basada en datos y patrones de comportamiento).
1.4. Modelo mental del usuario y principio de la menor sorpresa.

### 2. Eventos JavaScript para interfaces de usuario
2.1. Modelo de eventos del DOM: fases de captura, objetivo y burbujeo.
2.2. Eventos de ratón: `click`, `dblclick`, `mousedown`, `mouseup`, `mousemove`, `mouseenter`, `mouseleave`, `mouseover`, `mouseout`.
2.3. Eventos táctiles: `touchstart`, `touchend`, `touchmove`. El retardo de 300ms y `touch-action: manipulation`.
2.4. Eventos de teclado: `keydown`, `keyup`. `event.key` vs `event.code`.
2.5. Eventos de ventana: `scroll`, `resize`. Passive listeners.
2.6. Eventos de foco: `focus`, `blur`, `focusin`, `focusout`.
2.7. Eventos de formulario: `change`, `input`, `submit`.
2.8. Eventos de animación: `transitionend`, `animationend`, `animationstart`.
2.9. Delegación de eventos (event delegation): fundamento, ventajas y limitaciones.
2.10. Opciones avanzadas en `addEventListener`: `{ once, passive, capture }`.

### 3. Microinteracciones
3.1. Definición de microinteracción según Dan Saffer.
3.2. Los cuatro elementos: trigger, rules, feedback, loops/modes.
3.3. Implementación detallada de: botón de like animado, toggle switch, notificación toast, pull-to-refresh, efecto ripple, loading skeleton, swipe gesture.

### 4. Animaciones en la interfaz de usuario
4.1. Transiciones CSS (`transition`): propiedades, timing functions, retardo.
4.2. Animaciones CSS (`@keyframes`): keyframes, subpropiedades, iteraciones, dirección.
4.3. Web Animations API: `element.animate()`, objeto `Animation`, control programático.
4.4. Regla práctica de decisión entre las tres técnicas.

### 5. Transiciones CSS en componentes específicos
5.1. Menú desplegable suave. 5.2. Acordeón animado. 5.3. Modal fade in/out. 5.4. Tooltip con delay. 5.5. Tabs con indicador animado. 5.6. Dropdown con max-height.

### 6. Menús interactivos
6.1. Menú hamburguesa con morphing. 6.2. Mega menú con hover+focus. 6.3. Off-canvas con overlay. 6.4. Dropdown multinivel. 6.5. Sticky header inteligente. 6.6. Bottom navigation animado.

### 7. Componentes dinámicos completos
7.1. Carrusel/slider accesible. 7.2. Acordeón FAQ. 7.3. Tabs dinámicos. 7.4. Modal con focus trapping. 7.5. Galería con lightbox. 7.6. Formulario con validación en tiempo real. 7.7. Toast notifications. 7.8. Dark mode toggle. 7.9. Scroll reveal. 7.10. Drag and drop.

### 8. Rendimiento en interacciones
8.1. Debounce vs throttle. 8.2. `requestAnimationFrame`. 8.3. Layout thrashing. 8.4. `will-change`. 8.5. Intersection Observer. 8.6. Passive event listeners.

### 9. Accesibilidad en componentes interactivos
9.1. Focus management. 9.2. Aria-live regions. 9.3. Focus trapping. 9.4. Navegación por teclado. 9.5. Atributos ARIA de estado.


## Desarrollo teórico

### 1. ¿Qué es la interactividad web?

!!! info "Definición"
    La **interactividad web** se define como la capacidad de una página o aplicación para responder a las acciones del usuario de manera significativa y en tiempo real, estableciendo un diálogo bidireccional entre el sistema y quien lo utiliza. No debe confundirse en ningún caso con la **animación pasiva**, que consiste en movimientos o cambios visuales que ocurren de forma autónoma, sin intervención del usuario, como un banner animado que se reproduce en bucle, un carrusel que avanza automáticamente sin control del usuario o una animación de carga que simplemente se reproduce. La diferencia fundamental radica en la intencionalidad y en la relación causa-efecto: en una animación pasiva, el usuario es mero espectador que contempla; en la interactividad, el usuario es agente activo que provoca una respuesta concreta del sistema y recibe confirmación de que su acción ha sido procesada.

Para comprender esta diferencia con un ejemplo concreto, imaginemos un botón de "Me gusta" en una red social:

!!! example "Ejemplo: el botón de «Me gusta»"
    Cuando el usuario hace clic, el icono del corazón se rellena de color rojo mediante una animación de latido, el contador numérico se incrementa con una sutil animación, y el botón cambia de estado visual. El usuario ha iniciado la acción voluntariamente y recibe confirmación visual inmediata de que su acción ha sido registrada por el sistema. Este acoplamiento entre la acción del usuario y la respuesta del sistema es la esencia de la interactividad. Si el mismo corazón cambiara de color automáticamente sin intervención del usuario, estaríamos ante una animación pasiva que podría resultar confusa o incluso engañosa.

Desde la perspectiva de la experiencia de usuario (UX), la interactividad bien diseñada cumple cinco funciones psicológicas y funcionales que se complementan entre sí:

- **Proporciona retroalimentación inmediata** — el usuario sabe instantáneamente que su acción ha sido registrada, eliminando la incertidumbre y la ansiedad que genera una interfaz que no responde o lo hace con retardo.
- **Guía la atención** del usuario hacia elementos importantes de la interfaz mediante cambios visuales que contrastan con el resto del contenido, ayudando a establecer jerarquías visuales y flujos de interacción naturales.
- **Reduce la carga cognitiva** al hacer predecible y consistente el comportamiento del sistema: si cada botón responde de manera similar en toda la aplicación, el usuario no necesita aprender cada interacción individualmente, sino que transfiere su conocimiento previo.
- **Aumenta la percepción subjetiva de velocidad** — una animación de carga bien diseñada (como un *skeleton screen* que anticipa la estructura del contenido) puede hacer que una espera de tres segundos parezca de un segundo, mientras que una pantalla congelada sin ninguna retroalimentación hace que incluso 500 milisegundos de procesamiento parezcan una eternidad.
- **Genera satisfacción emocional** a través de microinteracciones placenteras que convierten tareas puramente funcionales en experiencias memorables y humanas, creando lo que Don Norman denomina "diseño emocional" en su libro *Emotional Design*.

Podemos clasificar la interactividad en tres niveles progresivos de sofisticación que se construyen unos sobre otros:

- **Interactividad reactiva** — el nivel más básico y fundamental: el sistema responde directamente a una acción explícita del usuario, como hacer clic en un botón, arrastrar un elemento, escribir en un campo de texto o seleccionar una opción de un menú. Es el nivel mínimo indispensable para cualquier interfaz funcional.
- **Interactividad proactiva** — va un paso más allá: el sistema anticipa las necesidades del usuario y ofrece sugerencias, información o acciones antes de que el usuario las solicite explícitamente. Ejemplos incluyen el autocompletado de búsquedas que sugiere términos mientras el usuario escribe, las notificaciones contextuales que aparecen cuando el usuario lleva cierto tiempo en una página sin interactuar, o los asistentes virtuales que ofrecen ayuda basándose en la página que el usuario está visitando.
- **Interactividad predictiva** — el nivel más avanzado: el sistema emplea datos históricos, patrones de comportamiento y algoritmos de aprendizaje automático para predecir lo que el usuario desea hacer, ofreciendo atajos, recomendaciones personalizadas, precarga de contenido probable o automatización de tareas repetitivas (como sugerir respuestas rápidas en un chat).

!!! info "Modelo mental y ley de Jakob"
    El **modelo mental** del usuario es un concepto crucial en el diseño de interactividad que ningún desarrollador debería ignorar. Cada usuario llega a nuestra interfaz con un conjunto de expectativas, creencias y suposiciones sobre cómo debería funcionar, formadas por su experiencia acumulada en cientos de otros sitios web y aplicaciones que ha utilizado a lo largo de su vida. Estas expectativas constituyen su modelo mental, una representación interna del funcionamiento del sistema. Cuando nuestro diseño se alinea con estos modelos mentales (por ejemplo, un icono de lupa siempre significa "buscar", un icono de tres rayas horizontales siempre abre un menú de navegación, un botón con aspecto tridimensional siempre es *clickable*), la interacción fluye de manera intuitiva y el usuario puede operar la interfaz casi sin pensarlo. Sin embargo, cuando nos desviamos de estos modelos mentales establecidos, generamos fricción cognitiva, confusión, errores del usuario y, en última instancia, abandono de la tarea. Este principio, conocido formalmente como el **principio de la menor sorpresa** o **ley de Jakob** (enunciada por Jakob Nielsen, co-fundador del Nielsen Norman Group), establece que los usuarios pasan la mayor parte de su tiempo en otros sitios web, y por lo tanto prefieren que nuestro sitio funcione exactamente de la misma manera que todos los demás sitios que ya conocen.

### 2. Eventos JavaScript para UI: la base técnica de la interactividad

!!! info "Modelo de eventos del DOM"
    Los eventos constituyen el mecanismo fundamental mediante el cual JavaScript detecta y responde a las acciones del usuario en el entorno del navegador. El modelo de eventos del DOM, estandarizado por el W3C a lo largo de más de dos décadas de evolución, define un flujo de propagación en tres fases que todo desarrollador front-end debe comprender en profundidad:

    - **Fase de captura** (*capture phase*) — primera etapa: el evento desciende desde el nodo raíz `document` pasando por cada ancestro en el árbol del DOM hasta alcanzar el elemento objetivo que originó el evento.
    - **Fase de objetivo** (*target phase*) — ocurre exactamente cuando el evento llega al elemento que lo disparó; es en este momento cuando los listeners registrados directamente sobre el elemento objetivo se ejecutan.
    - **Fase de burbujeo** (*bubble phase*) — etapa final: el evento asciende de vuelta desde el elemento objetivo hacia `document`, pasando nuevamente por cada ancestro en orden inverso.

Este modelo trifásico es el que permite patrones avanzados como la delegación de eventos, y su comprensión es indispensable para evitar comportamientos inesperados cuando múltiples listeners en diferentes niveles del DOM compiten por el mismo evento.

Los **eventos de ratón** constituyen la familia más utilizada en interfaces de escritorio y merecen un análisis pormenorizado:

- **`click`** — es, con diferencia, el evento más común: se dispara cuando el usuario presiona y suelta el botón principal del ratón sobre el mismo elemento. Es crucial entender que `click` es un evento compuesto que engloba implícitamente `mousedown` (presionar el botón) y `mouseup` (soltarlo). Esta composición tiene implicaciones prácticas importantes: si el usuario presiona el botón sobre un elemento, arrastra el cursor fuera de sus límites y suelta en otro lugar, se dispararán `mousedown` y `mouseup` en los elementos correspondientes, pero no se generará un evento `click` sobre ninguno de ellos, ya que la condición de "presionar y soltar sobre el mismo elemento" no se cumple.
- **`dblclick`** (doble clic) — menos común pero importante en contextos específicos como editores de texto (seleccionar palabra), gestores de archivos (abrir elemento) o tablas de datos (editar celda). Es importante señalar que `dblclick` siempre va precedido de dos eventos `click`, lo que puede causar conflictos si se manejan ambos en el mismo elemento.
- **`mouseenter` y `mouseleave`** — merecen una mención especial porque son preferibles a sus contrapartes `mouseover` y `mouseout` en la mayoría de las situaciones. La diferencia crucial es que `mouseenter`/`mouseleave` no burbujean desde los elementos hijos del elemento objetivo, mientras que `mouseover`/`mouseout` sí lo hacen. Esto significa que, en un componente con elementos anidados (por ejemplo, un botón con un icono SVG y un texto), `mouseenter` se disparará una única vez al entrar en el botón, independientemente de que el cursor pase por encima del SVG o del texto. En cambio, `mouseover` se dispararía repetidamente cada vez que el cursor cruce los límites de cualquiera de los elementos internos, complicando innecesariamente la lógica de interacción y pudiendo causar parpadeos visuales.

Los **eventos táctiles** (`touchstart`, `touchmove`, `touchend`, `touchcancel`) son la contrapartida de los eventos de ratón en el mundo de los dispositivos móviles y tabletas, y presentan particularidades que es necesario conocer. El objeto `TouchEvent` contiene tres colecciones de puntos de contacto:

- **`touches`** — lista todos los dedos que actualmente están en contacto con la pantalla, independientemente del elemento.
- **`targetTouches`** — lista solo aquellos dedos cuyo punto de contacto inicial fue dentro del elemento objetivo del evento.
- **`changedTouches`** — lista los dedos que han cambiado y que son relevantes para este evento concreto (el dedo que se levantó en `touchend`, el dedo que se movió en `touchmove`).

La implementación de gestos multitáctiles como el *pinch-to-zoom* o la rotación requiere procesar estas colecciones para calcular distancias, ángulos y velocidades entre múltiples puntos de contacto.

!!! tip "Elimina el retardo de 300 ms"
    Un aspecto crítico del desarrollo táctil es el retardo de aproximadamente **300 milisegundos** que los navegadores móviles introducen en el evento `click`. Este retardo existe para permitir que el navegador distinga entre un simple toque y un doble toque (que normalmente se usa para hacer zoom). Sin embargo, hace que las aplicaciones web se sientan lentas y poco responsivas comparadas con las aplicaciones nativas. **La solución moderna es aplicar la directiva CSS `touch-action: manipulation`** al elemento o al documento completo, lo que indica al navegador que no es necesario esperar por el doble toque y que los eventos de puntero deben manejarse inmediatamente.

Los **eventos de teclado** (`keydown`, `keyup`) son la puerta de entrada a la interactividad para usuarios que navegan sin ratón, ya sea por preferencia personal, por necesidad derivada de una discapacidad motriz, o por contexto (como desarrolladores y usuarios avanzados que prefieren la eficiencia del teclado). `keydown` se dispara en el momento en que se presiona una tecla y, si se mantiene presionada, continúa disparándose repetidamente a intervalos regulares (con un retardo inicial y una frecuencia de repetición que dependen de la configuración del sistema operativo). `keyup` se dispara una única vez al soltar la tecla. Es importante manejar `keydown` y no `keyup` para las interacciones de interfaz, ya que el usuario espera una respuesta inmediata al presionar, no al soltar.

Las propiedades `event.key` y `event.code` proporcionan información complementaria sobre la tecla pulsada, pero con propósitos distintos:

| Propiedad | Devuelve | Ejemplos | Cuándo usarla |
|-----------|----------|----------|---------------|
| **`event.key`** | Valor lógico o semántico de la tecla tal como el usuario lo percibe | `"ArrowUp"`, `"Escape"`, `"Enter"`, `"a"`, `"1"`, `"+"` | La gran mayoría de interacciones de interfaz de usuario, ya que refleja la intención del usuario |
| **`event.code`** | Posición física de la tecla en el teclado, independientemente de la distribución (QWERTY, AZERTY, QWERTZ) | `"KeyA"`, `"Digit1"`, `"ArrowUp"` | Casos muy específicos como videojuegos (donde la posición física de las teclas importa para la ergonomía), pero rara vez para interfaces web estándar |

Los **eventos de formulario** merecen un análisis detallado por su ubicuidad en el desarrollo web:

- **`input`** — se dispara inmediatamente cada vez que el valor de un campo cambia, sin importar la causa: tecleo, pegado desde el portapapeles, arrastre de texto, selección de una sugerencia de autocompletado, o modificación programática del valor. Esta inmediatez lo convierte en el evento ideal para implementar validación en tiempo real, búsquedas con autocompletado, contadores de caracteres y cualquier otra funcionalidad que requiera responder instantáneamente a lo que el usuario escribe.
- **`change`** — solo se dispara cuando el campo pierde el foco después de haber modificado su valor. Esto lo hace más adecuado para acciones costosas que no deberían ejecutarse con cada pulsación de tecla, como una petición al servidor para validar la unicidad de un nombre de usuario.
- **`submit`** — se dispara al enviar el formulario completo, ya sea mediante un botón de tipo `submit`, pulsando Enter en un campo de texto, o mediante `form.requestSubmit()` en JavaScript. Es el último punto de control donde se puede validar el formulario en su conjunto y potencialmente cancelar el envío con `event.preventDefault()`.

!!! info "Delegación de eventos"
    La **delegación de eventos** (*event delegation*) es uno de los patrones de diseño más poderosos y elegantes del desarrollo web, y todo profesional debe dominarlo. El patrón explota la fase de burbujeo para manejar eventos de múltiples elementos (potencialmente cientos o incluso miles) con un único listener colocado estratégicamente en un ancestro común. La idea es simple pero de gran alcance: en lugar de asignar un listener individual a cada elemento de una lista (lo que consumiría memoria proporcional al número de elementos y requeriría reasignar listeners cada vez que se añaden o eliminan elementos dinámicamente), asignamos un solo listener al contenedor padre y, dentro de la función manejadora, determinamos mediante `event.target` qué elemento hijo específico fue el origen real del evento.

Este patrón ofrece tres ventajas convincentes:

- **Reduce significativamente el consumo de memoria** al minimizar el número de listeners activos en la página, lo cual es especialmente relevante en aplicaciones con listas muy largas (tablas de datos, feeds de redes sociales, bandejas de entrada de correo).
- **Maneja automática y transparentemente los elementos añadidos al DOM** de forma dinámica después de la carga inicial, sin necesidad de reasignar listeners, ya que los eventos de estos nuevos elementos también burbujearán hasta el ancestro común.
- **Centraliza la lógica de manejo de eventos** en un solo lugar del código, facilitando el mantenimiento y la depuración.

!!! note "Límite de la delegación"
    No todos los eventos burbujean de forma natural. Los eventos `focus` y `blur` no burbujean (aunque `focusin` y `focusout` proporcionan alternativas que sí lo hacen). Los eventos `scroll`, `mouseenter` y `mouseleave` tampoco burbujean. Por tanto, la delegación no es aplicable universalmente y debe combinarse con otras estrategias cuando sea necesario.

Las **opciones avanzadas** de `addEventListener` amplían significativamente el control del desarrollador sobre el comportamiento de los listeners. La sintaxis moderna permite pasar un objeto de opciones como tercer parámetro en lugar del booleano `useCapture` tradicional:

- **`{ once: true }`** — registra un listener que se elimina automáticamente tras ejecutarse una sola vez, lo cual es perfecto para eventos que solo necesitan manejarse una vez en el ciclo de vida de la página (como la confirmación de que el usuario ha leído un aviso, o la inicialización diferida de un componente).
- **`{ passive: true }`** — particularmente importante para el rendimiento en dispositivos móviles: le comunica al navegador que el listener nunca llamará a `preventDefault()`, permitiendo que el motor de renderizado continúe con el desplazamiento (*scroll*) sin esperar a que el código JavaScript termine de ejecutarse, lo que resulta en un *scroll* mucho más fluido.
- **`{ capture: true }`** — registra el listener en la fase de captura en lugar de la fase de burbujeo, permitiendo interceptar eventos antes de que alcancen a sus destinos naturales. Es especialmente útil para implementar el patrón de "cerrar al hacer clic fuera", donde un listener en `document` captura cualquier clic y verifica si fue dentro o fuera del componente que se desea cerrar.

### 3. Microinteracciones: la magia del detalle

!!! info "Definición"
    El concepto de "microinteracción" fue articulado y popularizado por Dan Saffer en su libro *Microinteractions: Designing with Details* (O'Reilly Media, 2013), que rápidamente se convirtió en una referencia obligada para diseñadores y desarrolladores de productos digitales. Saffer define una microinteracción como un momento contenido y autocontenido dentro de un producto digital que realiza exactamente una única tarea específica. Son los momentos pequeños pero significativos que, acumulados a lo largo de la experiencia de uso, definen en gran medida la calidad percibida de un producto digital.

Como afirma Saffer:

!!! quote "Dan Saffer"
    La diferencia entre un producto que amas y uno que meramente toleras son, a menudo, las microinteracciones.

Ejemplos canónicos de microinteracciones incluyen:

- el botón de "Me gusta" de cualquier red social;
- el indicador de progreso al enviar un formulario;
- la notificación efímera que confirma que un archivo se ha guardado;
- la vibración táctil al activar el modo silencio en un teléfono;
- el deslizamiento lateral para desbloquear la pantalla;
- el sonido de obturador al realizar una captura de pantalla;
- el indicador de escritura (los tres puntos animados) en una aplicación de mensajería que nos dice que la otra persona está redactando un mensaje.

!!! info "Los cuatro elementos"
    Según el modelo conceptual de Saffer, toda microinteracción, sin importar su complejidad aparente, se puede descomponer en cuatro elementos estructurales fundamentales que el diseñador debe considerar de forma explícita y deliberada:

    - **Trigger** (disparador) — el mecanismo que pone en marcha la microinteracción. Los disparadores pueden ser iniciados por el usuario (un clic, un toque, un deslizamiento, un comando de voz, un gesto) o iniciados por el sistema (cuando se cumple una condición predefinida, como que llegue un mensaje nuevo, que se agote un temporizador, que se detecte un error de conexión, o que el usuario alcance un punto concreto en el scroll de la página).
    - **Rules** (reglas) — la lógica interna de la microinteracción: determinan qué sucede exactamente una vez que el trigger se ha activado, qué datos se procesan, qué condiciones lógicas se evalúan, qué flujo de ejecución se sigue. En términos de implementación web, las reglas se corresponden con el código JavaScript que ejecuta la lógica de negocio.
    - **Feedback** (retroalimentación) — toda manifestación sensorial (visual, audible o háptica) que el sistema emite para comunicar al usuario lo que está ocurriendo como resultado de su acción o del trigger del sistema. La retroalimentación es, esencialmente, el lenguaje mediante el cual el sistema dialoga con el usuario. Puede adoptar muchas formas: un icono que cambia de forma y color, una animación de carga que indica progreso, un sonido de confirmación, una vibración del dispositivo, o un mensaje de texto que confirma una acción.
    - **Loops and modes** (bucles y modos) — gobiernan el comportamiento de la microinteracción a lo largo del tiempo, en repeticiones sucesivas y en diferentes contextos o situaciones. Preguntas que este elemento ayuda a responder incluyen: ¿qué sucede si el usuario repite la acción muchas veces seguidas? ¿La microinteracción se comporta diferente tras la primera ejecución? ¿Hay un número máximo de repeticiones? ¿Existe un modo o estado alternativo si no hay conexión de red? ¿Cómo se comporta la microinteracción cuando el sistema está bajo carga pesada?

Para ilustrar este modelo con un ejemplo concreto y cercano, analicemos la microinteracción del botón de "Me gusta" (*favorite*/*like*) en Twitter:

!!! example "Análisis: el botón de «Me gusta» en Twitter"
    El **trigger** es iniciado por el usuario mediante un clic o toque sobre el icono del corazón que aparece debajo de cada tweet. Las **rules** determinan el siguiente flujo lógico: si el usuario no ha dado "like" a este tweet previamente, se registra el like (se añade a la lista de tweets gustados del usuario), se incrementa el contador público de likes, y se notifica al autor del tweet. Si el usuario ya había dado "like", se revierte la acción (se elimina de la lista), se decrementa el contador, y se retira la notificación. El nuevo estado se envía al servidor de forma asíncrona mediante una petición HTTP, y la interfaz se actualiza de forma optimista (sin esperar la confirmación del servidor) para proporcionar una sensación de inmediatez.

    La **retroalimentación** incluye tres canales sensoriales: visualmente, el corazón pasa de su estado vacío (contorno gris) a relleno (rojo intenso) acompañado de una breve animación de escala que simula un latido, y pequeñas partículas o chispas pueden desprenderse del icono; numéricamente, el contador de likes se actualiza mostrando el nuevo valor con una sutil animación de transición; y hápticamente (en la aplicación móvil), el dispositivo emite una breve vibración que el usuario asocia con la confirmación de la acción. Los **loops and modes** contemplan escenarios como: si la petición al servidor falla (por falta de conexión o error del backend), la interfaz revierte el cambio optimista (el corazón vuelve a su estado anterior), se muestra un mensaje de error discreto (un toast), y se permite al usuario reintentar la acción. Además, el contador puede actualizarse en tiempo real para reflejar los likes de otros usuarios que ocurren simultáneamente.

Veamos ahora la implementación técnica de otras microinteracciones paradigmáticas que todo desarrollador front-end debería conocer y ser capaz de implementar:

- **Toggle switch** — un interruptor binario que alterna entre dos estados mutuamente excluyentes. La implementación recomendada utiliza un `<input type="checkbox">` oculto visualmente pero plenamente funcional (lo que garantiza accesibilidad nativa y compatibilidad con formularios) y construye toda la apariencia visual mediante elementos `<span>` estilizados con CSS. El círculo interior (*thumb*) se anima horizontalmente mediante `transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1)`, desplazándose hacia la derecha cuando el checkbox está marcado (`:checked`). El color de fondo del carril (*track*) también transiciona suavemente. Los atributos ARIA `role="switch"` y `aria-checked` complementan la semántica para tecnologías asistivas, anunciando correctamente el estado del interruptor.

- **Notificación toast** — un mensaje efímero que aparece en una esquina de la pantalla para comunicar información no bloqueante al usuario. La implementación de un sistema de toasts profesional requiere: una cola de mensajes que gestione el orden de aparición y evite saturar la pantalla si se generan muchas notificaciones simultáneas; animaciones de entrada (*slide-in* + *fade-in*) y salida (*slide-out* + *fade-out*) definidas con `@keyframes`; un temporizador configurable para el *auto-dismiss* (típicamente entre **3 y 8 segundos** según la longitud del mensaje); la posibilidad de que el usuario descarte manualmente la notificación mediante un botón de cierre; tipado visual por niveles de severidad (éxito con borde verde, error con borde rojo, advertencia con borde amarillo, información con borde azul); y un límite máximo de toasts visibles simultáneamente (normalmente **3-5**) para no abrumar al usuario.

- **Efecto ripple** — popularizado por Material Design de Google, el *ripple* es una onda de tinta que se expande circularmente desde el punto exacto donde el usuario tocó o hizo clic sobre un elemento interactivo. La implementación crea dinámicamente un elemento `<span>` absolutamente posicionado en las coordenadas del clic (restando el *offset* del elemento contenedor respecto al *viewport*). A este *span* se le aplica una animación `@keyframes` que escala el círculo desde un radio de 0 hasta un diámetro suficiente para cubrir completamente el elemento (calculado como `Math.hypot(ancho, alto) * 2`, es decir, el doble de la diagonal del rectángulo). Simultáneamente, la opacidad se reduce gradualmente para crear un efecto de desvanecimiento. Una vez que la animación termina, el *span* se elimina del DOM. La animación utiliza `transform: scale()` y `opacity`, que son propiedades que solo afectan a la capa de composición y no disparan *reflow*, garantizando un rendimiento óptimo.

- **Loading skeleton** — como alternativa moderna a los *spinners* y barras de progreso tradicionales, los *skeleton screens* muestran formas esqueléticas (rectángulos y círculos con esquinas redondeadas) que ocupan aproximadamente el mismo espacio y posición que el contenido real que está por cargar. Estas formas tienen un degradado animado que se desplaza horizontalmente creando un efecto de brillo (*shimmer*), similar a la luz que se refleja en una superficie metálica al moverse. La animación se implementa con un `background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%)` con un `background-size` del doble del ancho del elemento y una animación que desplaza el `background-position` de **0%** a **200%**. Las ventajas de los *skeletons* sobre los *spinners* son múltiples: comunican al usuario qué tipo de contenido va a aparecer y dónde, reducen la percepción subjetiva del tiempo de espera, y eliminan el molesto efecto de saltos de layout (CLS) porque el espacio ya está reservado desde el primer momento.

- **Swipe gesture** — el gesto de deslizar horizontalmente para revelar acciones ocultas debajo de un elemento de lista (patrón conocido como *swipe to action*, *swipe to delete* o *swipe to archive*) es ubicuo en aplicaciones móviles modernas. La implementación requiere un seguimiento preciso de la trayectoria táctil. En `touchstart`, se captura la coordenada X inicial del dedo. En `touchmove`, se calcula la distancia recorrida (*deltaX*) y se desplaza el elemento visualmente mediante `transform: translateX(deltaX)`, limitando el desplazamiento máximo (normalmente al ancho de las acciones ocultas) y aplicando resistencia (la velocidad de desplazamiento se reduce a medida que nos acercamos al límite). En `touchend`, se evalúan dos criterios para decidir si la acción se completa o se revierte: la distancia total recorrida (si supera un umbral, típicamente el **40-50%** del ancho de las acciones) y la velocidad del gesto (si el usuario deslizó rápidamente aunque no llegara al umbral de distancia). Si se supera cualquiera de estos criterios, el elemento se anima hasta su posición final revelando completamente las acciones; en caso contrario, el elemento regresa a su posición original con una animación elástica (usando `cubic-bezier` con *overshoot*).

### 4. Animaciones UI: transiciones, keyframes y Web Animations API

El ecosistema de animación en la plataforma web moderna ofrece tres herramientas principales con diferentes niveles de abstracción, control y complejidad. La capacidad de elegir correctamente entre ellas, evaluando los requisitos específicos de cada situación, es una habilidad que distingue al desarrollador front-end senior del junior.

Las **transiciones CSS** constituyen el mecanismo más simple, declarativo y accesible para crear animaciones. Se definen mediante la propiedad abreviada `transition` (o sus cuatro subpropiedades: `transition-property`, `transition-duration`, `transition-timing-function`, `transition-delay`) sobre un elemento del DOM. El funcionamiento es conceptualmente simple: cuando una propiedad CSS específica del elemento cambia de valor —ya sea por la aplicación de una nueva clase, por la activación de una pseudoclase como `:hover`, `:focus` o `:active`, o por la modificación programática del atributo `style` desde JavaScript—, el navegador no aplica el cambio de forma instantánea, sino que interpola suavemente los valores intermedios entre el estado inicial y el estado final durante el período de tiempo especificado. La sintaxis completa es `transition: <property> <duration> <timing-function> <delay>`. Las transiciones son la herramienta ideal para animaciones simples disparadas directamente por la interacción del usuario, como cambios de color en botones al pasar el ratón, desplazamientos sutiles al hacer foco, o expansión suave de elementos. Su principal limitación es que solo pueden animar entre dos estados (inicial y final); no permiten secuencias de múltiples etapas, no pueden ejecutarse en bucle automáticamente, y no ofrecen control sobre la dirección de reproducción. Sin embargo, su simplicidad, su rendimiento (el navegador las optimiza de forma nativa) y la facilidad con la que se integran en el flujo normal de CSS las convierten en la primera opción que debería considerarse para cualquier necesidad de animación.

Las **animaciones con `@keyframes`** representan un salto significativo en expresividad y control. A diferencia de las transiciones, que solo definen los estados inicial y final, las animaciones permiten especificar una secuencia arbitraria de fotogramas clave (keyframes) que describen el estado del elemento en momentos concretos de la línea de tiempo de la animación. La regla `@keyframes nombreDeLaAnimacion` define estos fotogramas mediante porcentajes (0%, 25%, 50%, 75%, 100%) o las palabras clave equivalentes `from` (0%) y `to` (100%). Dentro de cada bloque de porcentaje, se especifican las propiedades CSS que deben aplicarse en ese momento. El navegador se encarga de interpolar automáticamente los valores entre fotogramas consecutivos. Una vez definida la regla `@keyframes`, la animación se vincula al elemento deseado mediante la propiedad abreviada `animation` (o sus numerosas subpropiedades). Esta técnica permite animaciones complejas y expresivas: rebotes (combinando `cubic-bezier()` con valores que superan 1 para crear overshoot), vibraciones, pulsaciones rítmicas, efectos de latido, trayectorias curvas (combinando múltiples `translate`, `rotate` y `scale`), y animaciones de partículas. La propiedad `animation-iteration-count: infinite` permite crear animaciones en bucle continuo sin intervención adicional. La propiedad `animation-direction: alternate` hace que en iteraciones pares la animación se reproduzca en sentido normal y en las impares en sentido inverso, creando efectos de vaivén natural. La propiedad `animation-fill-mode` controla si los estilos de la animación se aplican antes de comenzar (`backwards`), después de terminar (`forwards`), ambos (`both`), o ninguno (`none`), lo cual es crucial para evitar que el elemento "salte" visualmente al finalizar la animación.

La **Web Animations API** (WAAPI) representa la convergencia entre el mundo declarativo de CSS y el control programático de JavaScript. Expuesta a través del método `element.animate(keyframes, options)`, permite crear, controlar y manipular animaciones directamente desde código JavaScript utilizando una sintaxis que refleja de forma casi directa la estructura de las reglas `@keyframes` de CSS. El primer argumento es un array de objetos, donde cada objeto representa un fotograma clave con las propiedades CSS (en notación camelCase) y sus valores, además de un offset opcional (equivalente al porcentaje en CSS). El segundo argumento es un objeto de opciones que especifica la duración (`duration` en milisegundos), el número de iteraciones (`iterations`, donde `Infinity` equivale a `infinite` en CSS), la dirección (`direction`), el modo de relleno (`fill`), la función de temporización (`easing`), el retardo (`delay`), y otras opciones avanzadas como `endDelay`, `iterationStart` y `composite`.

El método `element.animate()` retorna un objeto de tipo `Animation` que expone una API rica y bien diseñada para el control programático. El objeto `Animation` ofrece métodos como `.play()` (inicia o reanuda la reproducción), `.pause()` (pausa manteniendo la posición actual), `.reverse()` (invierte la dirección de reproducción), `.cancel()` (cancela la animación y la reinicia), `.finish()` (salta inmediatamente al final de la animación), y `.updatePlaybackRate(rate)` (cambia la velocidad de reproducción, donde 1 es la velocidad normal, 2 el doble de rápido, 0.5 la mitad). También expone propiedades como `.playState` (cuyo valor puede ser "idle", "running", "paused" o "finished"), `.currentTime` (el tiempo actual de la animación en milisegundos, que puede ser leído y modificado para buscar posiciones arbitrarias), `.playbackRate`, y `.effect` (el objeto `AnimationEffect` subyacente que contiene los keyframes y las opciones de timing). Además, el objeto `Animation` proporciona dos promesas: `.finished` (que se resuelve cuando la animación termina normalmente o se rechaza si es cancelada) y `.ready` (que se resuelve cuando la animación está lista para reproducirse, lo cual es útil para coordinaciones complejas).

La WAAPI es la herramienta indicada para escenarios donde la animación depende de valores que solo pueden conocerse en tiempo de ejecución (por ejemplo, animar un elemento hasta una posición calculada basándose en el tamaño del viewport, en la posición del ratón o en datos recibidos del servidor), cuando se necesita orquestar múltiples animaciones con dependencias secuenciales o paralelas complejas, cuando se requiere pausar, reanudar o cancelar animaciones en respuesta a interacciones del usuario, o cuando la animación necesita sincronizarse con otras operaciones asíncronas como peticiones de red.

| Herramienta | Naturaleza | Ideal para | Limitaciones |
|-------------|-----------|------------|--------------|
| **Transiciones CSS** | Declarativa, dos estados | Cambios simples disparados por la interacción (*hover*, *focus*, clic para alternar clases): color, desplazamientos sutiles, expansión | Solo dos estados; sin secuencias de etapas, sin bucle automático ni control de dirección |
| **`@keyframes`** | Declarativa, secuencia de fotogramas | Animaciones complejas y estáticas con múltiples etapas, bucles (`infinite`), vaivén (`alternate`) y relleno (`fill-mode`) | No puede depender de valores calculados en tiempo de ejecución |
| **Web Animations API** | Programática (JavaScript) | Valores conocidos solo en ejecución (posición del cursor, tamaño del *viewport*, datos del servidor), orquestación y control (`play`/`pause`/`reverse`) | Más verbosa; requiere gestionar manualmente el ciclo de vida |

!!! tip "Regla práctica de decisión"
    Para cambios simples de estado disparados directamente por la interacción del usuario (*hover*, *focus*, clic para alternar clases), usa **transiciones CSS**, ya que son la opción más simple, declarativa y mantenible. Para animaciones complejas con múltiples etapas que no dependen de valores de ejecución y que pueden definirse de forma estática, usa **`@keyframes`**. Para animaciones dinámicas que dependen de valores calculados en JavaScript o que requieren control programático granular, usa la **Web Animations API**.

### 5. Rendimiento en interacciones: fluidez a 60 fps

!!! info "Presupuesto de 16,67 ms por fotograma"
    La fluidez de una interfaz se mide en fotogramas por segundo (*frames per second*, fps), una métrica heredada del mundo de los videojuegos y la animación cinematográfica. El umbral de percepción humana para una animación fluida y sin saltos perceptibles se sitúa en los **60 fps**, lo que otorga al desarrollador un presupuesto máximo de aproximadamente **16,67 milisegundos** (1000 ms dividido entre 60) para calcular, estilizar, maquetar y pintar cada fotograma. Si el navegador tarda más de esos 16,67 ms en completar un fotograma, la tasa de refresco efectiva cae (por ejemplo, a 30 fps si tarda 33 ms o a 15 fps si tarda 66 ms) y el usuario percibe un tartamudeo visual conocido como **jank**.

    Este *jank* tiene consecuencias medibles: los usuarios califican las interfaces entrecortadas como de baja calidad, asocian la lentitud con falta de profesionalidad, y son más propensos a abandonar la tarea o el sitio. Por lo tanto, optimizar el rendimiento de las interacciones no es una microoptimización opcional sino una responsabilidad central del desarrollador front-end.

El patrón **debounce** aborda el problema de funciones costosas que se invocan en rápida sucesión. Su mecanismo es simple: cada nueva llamada reinicia un temporizador interno (`setTimeout`), cancelando cualquier ejecución pendiente (`clearTimeout`). La función solo se ejecuta cuando ha transcurrido un período de inactividad (sin nuevas llamadas) igual al retardo configurado. Es ideal para eventos de alta frecuencia donde solo nos importa el estado final, como el evento `input` en un campo de búsqueda con sugerencias remotas (no queremos enviar una petición HTTP por cada letra tecleada, sino solo cuando el usuario se detiene), o el evento `resize` para recalcular un layout complejo (no necesitamos recalcular en cada píxel de cambio, solo cuando el usuario suelta el borde de la ventana).

El patrón **throttle**, complementario pero conceptualmente distinto, garantiza que una función se ejecute como máximo una vez cada intervalo de tiempo fijo, sin importar cuántas veces se dispare el evento desencadenante. A diferencia de debounce (que espera a que termine la ráfaga), throttle proporciona una frecuencia de actualización garantizada y predecible durante la ráfaga. Es la elección correcta para eventos como `scroll` y `mousemove`, donde necesitamos proporcionar retroalimentación visual continua al usuario (por ejemplo, actualizar una barra de progreso de lectura, reposicionar un tooltip que sigue al cursor, o aplicar un efecto parallax) pero sin abrumar el hilo principal con ejecuciones excesivas. Un intervalo típico para *throttle* en animaciones de *scroll* es de **100-200 ms**, que corresponde a 5-10 actualizaciones por segundo, suficiente para que el ojo humano perciba fluidez sin desperdiciar ciclos de CPU.

| Criterio | **debounce** | **throttle** |
|----------|--------------|--------------|
| **Cuándo ejecuta** | Cuando ha transcurrido un período de inactividad igual al retardo configurado (al final de la ráfaga) | Como máximo una vez cada intervalo de tiempo fijo, durante toda la ráfaga |
| **Mecanismo** | Cada llamada reinicia un `setTimeout` y cancela la pendiente con `clearTimeout` | Ejecuta en cada intervalo fijo, ignorando las llamadas intermedias |
| **Casos de uso** | `input` en búsquedas con sugerencias remotas, `resize` para recalcular un layout complejo | `scroll` y `mousemove`: barra de progreso de lectura, *tooltip* que sigue al cursor, efecto *parallax* |

La función **`requestAnimationFrame`** (rAF) es la herramienta canónica para animaciones en bucle mediante JavaScript, y su uso debería reemplazar completamente a `setInterval` y `setTimeout` para este propósito. rAF programa un callback para que se ejecute justo antes del siguiente repintado del navegador (es decir, al inicio del pipeline de renderizado del siguiente fotograma), lo que permite al motor de renderizado optimizar la animación globalmente, sincronizándola con la tasa de refresco nativa del monitor y agrupando múltiples callbacks rAF en un solo ciclo de repintado. Las ventajas sobre los temporizadores tradicionales son sustanciales: la animación se pausa automáticamente cuando la pestaña del navegador no está visible, ahorrando batería y ciclos de CPU; el navegador puede optimizar el momento exacto de ejecución para minimizar el jank; y la animación nunca se ejecutará más rápido que la tasa de refresco del hardware (evitando trabajo inútil). El patrón idiomático en JavaScript consiste en una función recursiva que calcula el progreso de la animación (típicamente usando la marca de tiempo de alta resolución `timestamp` que rAF pasa como argumento al callback, o usando `performance.now()` para mayor precisión), actualiza el DOM, y se llama a sí misma mediante `requestAnimationFrame(nombreDeLaFuncion)` si la animación no ha concluido.

El **layout thrashing** (también denominado "forced synchronous layout" o "reflow forzado síncrono") es un anti-patrón de rendimiento sutil pero potencialmente devastador. Ocurre cuando el código JavaScript intercala operaciones de lectura de propiedades geométricas del DOM (como `offsetWidth`, `offsetHeight`, `offsetTop`, `offsetLeft`, `getBoundingClientRect()`, `scrollTop`, `scrollLeft`, `getComputedStyle()`, `clientWidth`, `clientHeight`) con operaciones de escritura que modifican el layout (como cambiar clases, modificar el atributo `style`, añadir o eliminar elementos del DOM, o modificar el contenido textual). El problema surge porque los navegadores modernos, en un intento de optimizar el rendimiento, posponen el costoso recálculo del layout (reflow) hasta que sea estrictamente necesario, normalmente justo antes del repintado. Sin embargo, si el código JavaScript realiza una operación de lectura después de una escritura pendiente, el navegador se ve forzado a ejecutar el reflow de manera síncrona e inmediata para poder devolver un valor geométrico correcto y actualizado. Si este patrón (escritura, luego lectura, luego escritura, luego lectura) se repite dentro de un bucle (por ejemplo, al iterar sobre cientos de elementos para posicionarlos), el rendimiento se degrada catastróficamente, ya que cada iteración fuerza un costoso reflow.

!!! tip "Separa lecturas y escrituras por lotes"
    La solución canónica al *layout thrashing* consiste en aplicar el principio de separación estricta de fases (*read/write batching*):

    - **Fase de lecturas** — se realizan todas las lecturas necesarias del DOM, almacenando los valores obtenidos en variables JavaScript.
    - **Fase de cálculo** — se procesan esos valores para calcular los nuevos estados y posiciones.
    - **Fase de escrituras** — se aplican todas las escrituras al DOM de una sola vez.

    De esta manera, el navegador solo necesita calcular un *reflow* al final de todas las escrituras, en lugar de un *reflow* por cada par de lectura/escritura. Librerías como FastDOM (desarrollada por el equipo de Google) automatizan y garantizan este patrón encolando operaciones de lectura y escritura para ejecutarlas en el momento óptimo dentro del ciclo de renderizado.

La propiedad CSS **`will-change`** es un mecanismo de optimización que permite al desarrollador comunicar proactivamente al navegador que un determinado elemento va a experimentar cambios en propiedades específicas en el futuro cercano.

!!! warning "`will-change`: úsalo con moderación"
    Esta información permite al navegador preparar optimizaciones anticipadas, como promocionar el elemento a su propia capa de composición (*GPU layer*), lo que acelera significativamente las transformaciones y cambios de opacidad al no requerir repintado del resto de la página. La sintaxis es `will-change: transform`, `will-change: opacity`, o `will-change: transform, opacity`.

    Sin embargo, esta propiedad debe utilizarse con extrema prudencia, ya que cada capa de composición consume memoria de vídeo (VRAM) proporcional a las dimensiones del elemento, y crear demasiadas capas o capas excesivamente grandes puede agotar la memoria de la GPU, especialmente en dispositivos móviles con recursos limitados. La práctica recomendada es aplicar `will-change` de forma dinámica justo antes de que la animación comience (por ejemplo, en el manejador del evento `mouseenter` o en respuesta a un clic que inicia una transición) y removerla en cuanto la animación termina (en los eventos `transitionend` o `animationend`, o al restaurar el estado original). **No debe aplicarse de forma estática** en la hoja de estilos a elementos que podrían no llegar a animarse nunca.

La API **Intersection Observer** proporciona una forma moderna, eficiente y asíncrona de observar cuándo un elemento del DOM entra, sale o intersecta con otro elemento (normalmente el viewport del navegador, aunque puede configurarse cualquier ancestro con scroll). Esta API reemplaza los enfoques tradicionales y problemáticos basados en listeners del evento `scroll` combinados con llamadas a `getBoundingClientRect()` o bibliotecas de detección de visibilidad. El observer se crea con `new IntersectionObserver(callback, options)`, donde el callback recibe un array de objetos `IntersectionObserverEntry` (uno por cada elemento observado que ha cambiado su estado de intersección) y las opciones incluyen `root` (el elemento ancestro de referencia, por defecto el viewport), `rootMargin` (márgenes virtuales para expandir o contraer el área de detección, similares a los márgenes CSS) y `threshold` (un número entre 0 y 1, o un array de números, que especifica qué porcentaje del elemento debe ser visible para disparar el callback; 0 significa que se dispara en cuanto un solo píxel es visible, 1 significa que se dispara solo cuando el elemento está completamente visible). Los casos de uso de Intersection Observer son numerosos y variados: lazy loading de imágenes (cargar la imagen solo cuando está a punto de entrar en el viewport), animaciones de entrada al hacer scroll (scroll reveal), carga infinita (añadir más contenido cuando el usuario se acerca al final de la lista), seguimiento de impresiones para analíticas (saber qué contenido ha sido realmente visto por el usuario), y reproducción/pausa automática de vídeos y animaciones según su visibilidad.

### 6. Accesibilidad en componentes interactivos

!!! warning "La interactividad sin accesibilidad"
    La interactividad sin accesibilidad es un fracaso del diseño inclusivo que excluye a una parte sustancial de la población mundial —según la OMS, **más del 15%**, es decir, más de mil millones de personas, viven con algún tipo de discapacidad— y expone al sitio a riesgos legales por incumplimiento de normativas. Accesibilidad e interactividad no son conceptos opuestos ni un compromiso; son dos caras de la misma moneda del diseño profesional. **Un componente interactivo verdaderamente bien diseñado es, por definición, accesible.**

La **gestión del foco** (*focus management*) es el primer pilar de la accesibilidad interactiva y, posiblemente, el aspecto que más frecuentemente se descuida.

!!! tip "Gestión del foco en cada cambio de contexto"
    En aplicaciones de una sola página (SPA), donde el contenido se reemplaza dinámicamente sin recarga completa del documento, es extremadamente fácil que el foco del teclado se pierda. El foco puede quedar apuntando a un elemento que ya ha sido eliminado del DOM, o retroceder al elemento `<body>` dejando al usuario de teclado sin referencia de dónde se encuentra.

    Cada vez que se produce un cambio de contexto significativo —abrir una nueva vista, mostrar un modal, cargar contenido asíncrono, mostrar resultados de búsqueda— el desarrollador debe mover el foco de forma programática al lugar lógico y esperable:

    - **Al abrir un modal** — al primer elemento interactivo dentro del mismo (normalmente el botón de cierre o el campo de formulario principal).
    - **Al cerrar el modal** — de vuelta al botón o enlace que lo abrió.
    - **Al navegar a una nueva sección en una SPA** — al encabezado principal (`<h1>`) o al primer contenido relevante.

    Para elementos no interactivos por defecto que necesitan recibir foco (como un `<h1>` o un `<div>` que actúa como contenedor de una región), se debe usar `tabindex="-1"`, que permite el foco programático (`.focus()`) pero excluye el elemento del orden natural de tabulación (no se alcanza presionando Tab).

La **trampa de foco** (*focus trapping*) es un patrón de accesibilidad crítico para componentes que se superponen al resto de la interfaz, como modales, diálogos, menús desplegables a pantalla completa y hojas inferiores (*bottom sheets*).

!!! info "Trampa de foco (focus trapping)"
    El principio es simple: mientras el componente está abierto, el foco del teclado debe permanecer confinado estrictamente dentro de sus límites, ciclando circularmente. Al presionar Tab estando en el último elemento enfocable del componente, el foco debe regresar al primer elemento enfocable, en lugar de escaparse al resto de la página que queda detrás. Análogamente, al presionar Shift+Tab en el primer elemento, el foco debe saltar al último.

    La implementación requiere:

    - **Mantener una lista actualizada** de todos los elementos que pueden recibir foco dentro del contenedor, identificados mediante un selector CSS exhaustivo que cubra enlaces, botones, campos de formulario, elementos con `tabindex >= 0` y elementos con `contenteditable="true"`.
    - **Interceptar el evento `keydown`** para la tecla Tab.
    - **Evaluar la posición actual del foco** y moverlo al extremo opuesto cuando corresponda.

    Es importante recordar que los `<input type="radio">` de un mismo grupo (`name`) forman un único punto de tabulación, navegándose internamente con flechas, y que los `<select multiple>` tienen un comportamiento de foco particular.

Las **regiones `aria-live`** son el mecanismo estándar para comunicar cambios dinámicos en el contenido del DOM a los usuarios de lectores de pantalla, sin necesidad de mover el foco a la región modificada (lo cual sería disruptivo y desorientador). El atributo `aria-live` acepta dos valores principales:

| Valor | Comportamiento del lector de pantalla | Cuándo usarla |
|-------|--------------------------------------|---------------|
| **`aria-live="polite"`** | Espera a terminar su tarea actual (por ejemplo, leer un párrafo o un mensaje) antes de anunciar el nuevo contenido | La gran mayoría de actualizaciones dinámicas: notificaciones toast, contadores, carga de resultados de búsqueda, mensajes de estado |
| **`aria-live="assertive"`** | Interrumpe inmediatamente lo que esté haciendo para anunciar el cambio de forma urgente | Exclusivamente mensajes críticos: errores que impiden continuar con la tarea, alertas de seguridad, avisos de tiempo límite o de cierre de sesión inminente |

El abuso de `aria-live="assertive"` es contraproducente ya que interrumpe constantemente la experiencia del usuario.

El atributo complementario `aria-atomic="true"` indica al lector de pantalla que debe anunciar la región completa como un todo, no solo los fragmentos que han cambiado. Por ejemplo, si una región contiene "Resultados: 5 encontrados" y luego cambia a "Resultados: 12 encontrados", con `aria-atomic="true"` el lector anunciará la frase completa, mientras que sin él podría anunciar solo "12 encontrados", perdiendo el contexto de qué significa ese número. `aria-relevant` permite especificar qué tipo de cambios deben ser anunciados: `"additions"` (nodos añadidos), `"removals"` (nodos eliminados), `"text"` (cambios en el texto) o `"all"` (por defecto, equivale a `"additions text"`).

Existen roles ARIA que poseen un comportamiento `aria-live` implícito, lo que simplifica su uso:

| Rol | Equivalencia implícita | Uso recomendado |
|-----|------------------------|-----------------|
| **`role="alert"`** | `aria-live="assertive"` + `aria-atomic="true"` | Mensajes de error críticos y alertas que requieren atención inmediata |
| **`role="status"`** | `aria-live="polite"` + `aria-atomic="true"` | Información de estado no urgente: «Mensaje enviado correctamente», «Guardando...», «3 elementos seleccionados» |
| **`role="log"`** | Similar a `status` | Regiones con contenido que se añade secuencialmente (historial de chat, consola de logs); anuncia por defecto solo las nuevas adiciones |
| **`role="marquee"`** | `aria-live="off"` por defecto | Caso especial que **no debería usarse** |

Los **atributos ARIA de estado** constituyen el vocabulario mediante el cual los componentes interactivos personalizados comunican su estado dinámico a las tecnologías asistivas. Sin estos atributos, un lector de pantalla no puede distinguir si un botón que controla un panel está actualmente expandido o colapsado, si la pestaña en la que está el foco es la activa o no, o si un interruptor está en posición de encendido o apagado. Los atributos más importantes son:

- `aria-expanded="true|false"`: se aplica al elemento que controla la visibilidad de otro (por ejemplo, un botón de acordeón, un botón de menú desplegable). Indica al lector de pantalla si el panel/menú controlado está actualmente visible o no.
- `aria-selected="true|false"`: se aplica a elementos dentro de un conjunto de opciones seleccionables, como pestañas en un tablist, opciones en un listbox o items en un tree. Solo un elemento del conjunto debe tener `aria-selected="true"` en cada momento.
- `aria-pressed="true|false|mixed"`: se aplica a botones de tipo toggle. A diferencia de un botón normal que ejecuta una acción puntual, un botón toggle mantiene un estado persistente de "presionado" o "no presionado".
- `aria-current="page|step|location|date|time|true"`: indica el elemento actual dentro de un conjunto, como la página activa en una paginación, el paso actual en un wizard, o la ubicación actual en un breadcrumb.
- `aria-checked="true|false|mixed"`: indica el estado de un checkbox, radio button o switch personalizado.
- `aria-disabled="true"`: comunica que un elemento está deshabilitado sin necesidad de usar la propiedad `disabled` de HTML, que no es válida para elementos como `<div>` o `<li>`.



## Ejemplos guiados

### Ejemplo Guiado 1: Botón de Like con Animación de Latido

!!! example "Contexto pedagógico"
    Construiremos un botón de "Me gusta" completamente funcional con las siguientes características: alterna entre los estados "sin like" y "con like" al hacer clic o presionar Enter/Espacio, aplica animación de latido mediante `@keyframes`, actualiza un contador con animación numérica, y es plenamente accesible mediante `aria-pressed` y un `aria-label` descriptivo que anuncia el estado completo.

=== "HTML"

    ``` html
    <!-- Componente: Botón de Like Animado con todas las funcionalidades -->
    <div class="ejemplo-container">
      <h3>Ejemplo 1: Botón de Like</h3>
      <button class="like-btn" id="likeBtn" aria-pressed="false" aria-label="Me gusta. 0 me gustas">
        <svg class="heart-icon" viewBox="0 0 24 24" width="22" height="22" aria-hidden="true">
          <path class="heart-path" d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5
            2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3
            19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"
            fill="none" stroke="currentColor" stroke-width="2"/>
        </svg>
        <span class="like-count" id="likeCount" aria-hidden="true">0</span>
      </button>
    </div>

    <link rel="stylesheet" href="./styles.css">

    <script src="./script.js"></script>
    ```

=== "CSS"

    ``` css
    .ejemplo-container { padding: 1.5rem; font-family: system-ui, sans-serif; max-width: 400px; margin: 0 auto; text-align: center; }
    .ejemplo-container h3 { margin-bottom: 1rem; color: #333; }
    .like-btn {
      display: inline-flex; align-items: center; gap: 0.5rem;
      padding: 0.7rem 1.4rem; border: 2px solid #e0e0e0; border-radius: 2rem;
      background: #fff; color: #666; font-size: 1rem; font-weight: 500;
      cursor: pointer; outline: none;
      transition: background-color 0.3s ease, border-color 0.3s ease, color 0.3s ease, transform 0.15s ease;
    }
    .like-btn:hover { border-color: #ff6b81; color: #ff6b81; background: #fff5f5; }
    .like-btn:focus-visible { box-shadow: 0 0 0 3px rgba(255,107,129,0.4); border-color: #ff6b81; }
    .like-btn:active { transform: scale(0.95); }
    .like-btn.liked { background: #ff6b81; border-color: #ff6b81; color: #fff; }
    .like-btn.liked:hover { background: #ff5274; border-color: #ff5274; color: #fff; }
    .heart-icon { transition: transform 0.3s cubic-bezier(0.68,-0.55,0.265,1.55); flex-shrink: 0; }
    .heart-path { transition: fill 0.3s ease; }
    .like-btn.liked .heart-path { fill: currentColor; }
    .like-btn.liked .heart-icon { animation: heartbeat 0.4s ease-in-out; }
    @keyframes heartbeat {
      0%{transform:scale(1)}25%{transform:scale(1.3)}40%{transform:scale(0.95)}
      55%{transform:scale(1.15)}70%{transform:scale(0.98)}100%{transform:scale(1)}
    }
    .like-count { transition: transform 0.2s ease; }
    .like-count.updating { animation: countPop 0.3s ease; }
    @keyframes countPop {
      0%{transform:scale(1);opacity:1}50%{transform:scale(1.4);opacity:0.5}100%{transform:scale(1);opacity:1}
    }
    ```

=== "JS"

    ``` js
    (function() {
      var btn = document.getElementById('likeBtn');
      var countEl = document.getElementById('likeCount');
      var liked = false;
      var count = 0;

      function updateUI() {
        btn.classList.toggle('liked', liked);
        btn.setAttribute('aria-pressed', liked ? 'true' : 'false');
        countEl.textContent = count;
        btn.setAttribute('aria-label',
          'Me gusta. ' + (count === 0 ? 'Sin me gustas' : count + ' me gustas') +
          (liked ? '. Te gusta' : '. No te gusta')
        );
      }

      function animateCount() {
        void countEl.offsetWidth;
        countEl.classList.add('updating');
        setTimeout(function() { countEl.classList.remove('updating'); }, 300);
      }

      function toggleLike() {
        liked = !liked;
        count += liked ? 1 : -1;
        if (count < 0) count = 0;
        animateCount();
        updateUI();
      }

      btn.addEventListener('click', toggleLike);
      btn.addEventListener('keydown', function(e) {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); toggleLike(); }
      });
      updateUI();
    })();
    ```

### Ejemplo Guiado 2: Toggle Switch Accesible

!!! example "Contexto pedagógico"
    Implementaremos un interruptor binario completamente accesible utilizando un checkbox oculto como base semántica y spans estilizados para la apariencia visual. El switch responde a clic, teclado (Enter/Espacio), anuncia su estado con `aria-checked` y emite un mensaje mediante `aria-live`.

=== "HTML"

    ``` html
    <div class="ejemplo-container">
      <h3>Ejemplo 2: Toggle Switch</h3>
      <label class="toggle-label">
        <span class="toggle-text">Notificaciones push</span>
        <input type="checkbox" class="toggle-input" id="notifToggle" role="switch" aria-checked="false">
        <span class="toggle-track" aria-hidden="true">
          <span class="toggle-thumb"></span>
        </span>
      </label>
      <div class="toggle-status" aria-live="polite" id="toggleStatus"></div>
    </div>

    <link rel="stylesheet" href="./styles.css">

    <script src="./script.js"></script>
    ```

=== "CSS"

    ``` css
    .toggle-label { display: inline-flex; align-items: center; gap: 0.75rem; cursor: pointer; user-select: none; font-size: 1rem; color: #333; }
    .toggle-input { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0,0,0,0); }
    .toggle-track {
      position: relative; display: inline-block; width: 52px; height: 28px;
      background: #c0c0c0; border-radius: 14px; border: 2px solid #c0c0c0; flex-shrink: 0;
      transition: background-color 0.3s ease, border-color 0.3s ease;
    }
    .toggle-thumb {
      position: absolute; top: 2px; left: 2px; width: 20px; height: 20px;
      background: #fff; border-radius: 50%; box-shadow: 0 1px 3px rgba(0,0,0,0.2);
      transition: transform 0.3s cubic-bezier(0.4,0,0.2,1);
    }
    .toggle-label:hover .toggle-track { background: #a8a8a8; border-color: #a8a8a8; }
    .toggle-input:checked ~ .toggle-track { background: #4cd964; border-color: #4cd964; }
    .toggle-input:checked ~ .toggle-track .toggle-thumb { transform: translateX(24px); }
    .toggle-input:focus-visible ~ .toggle-track { box-shadow: 0 0 0 3px rgba(76,217,100,0.4); }
    .toggle-status { font-size: 0.85rem; color: #666; margin-top: 0.5rem; }
    ```

=== "JS"

    ``` js
    (function() {
      var toggle = document.getElementById('notifToggle');
      var status = document.getElementById('toggleStatus');
      function update() {
        toggle.setAttribute('aria-checked', toggle.checked ? 'true' : 'false');
        status.textContent = 'Notificaciones: ' + (toggle.checked ? 'activadas' : 'desactivadas');
      }
      toggle.addEventListener('change', update);
      update();
    })();
    ```

### Ejemplo Guiado 3: Notificaciones Toast con Cola y Auto-Dismiss

!!! example "Contexto pedagógico"
    Desarrollamos un sistema completo de notificaciones efímeras que gestiona una cola de mensajes, aplica animaciones de slide-in/slide-out, permite auto-dismiss configurable, cierre manual y respeta un límite máximo de toasts visibles. Cada toast es una región `role="status"` para accesibilidad.

=== "HTML"

    ``` html
    <div class="ejemplo-container">
      <h3>Ejemplo 3: Sistema Toast</h3>
      <div style="display:flex;gap:0.5rem;flex-wrap:wrap;">
        <button onclick="mostrarToast('exito','Operación completada')" class="btn-demo btn-exito">Éxito</button>
        <button onclick="mostrarToast('error','Error de conexión')" class="btn-demo btn-error">Error</button>
        <button onclick="mostrarToast('aviso','Sesión próxima a expirar')" class="btn-demo btn-aviso">Aviso</button>
        <button onclick="mostrarToast('info','Nueva versión disponible')" class="btn-demo btn-info">Info</button>
      </div>
      <div class="toast-container" id="toastContainer" aria-label="Notificaciones"></div>
    </div>

    <link rel="stylesheet" href="./styles.css">

    <script src="./script.js"></script>
    ```

=== "CSS"

    ``` css
    .btn-demo { padding: 0.5rem 1rem; border: none; border-radius: 0.5rem; color: #fff; cursor: pointer; font-weight: 500; }
    .btn-exito { background: #28a745; } .btn-error { background: #dc3545; }
    .btn-aviso { background: #ffc107; color: #333; } .btn-info { background: #17a2b8; }
    .toast-container {
      position: fixed; bottom: 1rem; right: 1rem; z-index: 9999;
      display: flex; flex-direction: column-reverse; gap: 0.5rem; max-width: 380px;
    }
    .toast {
      display: flex; align-items: center; gap: 0.5rem; padding: 0.75rem 1rem;
      background: #fff; border-radius: 0.5rem; box-shadow: 0 4px 16px rgba(0,0,0,0.15);
      border-left: 4px solid #6c757d; font-size: 0.9rem;
      animation: toastIn 0.35s ease forwards;
    }
    @keyframes toastIn { from{transform:translateX(120%);opacity:0} to{transform:translateX(0);opacity:1} }
    .toast.saliendo { animation: toastOut 0.3s ease forwards; }
    @keyframes toastOut { to{transform:translateX(120%);opacity:0;max-height:0;margin:0} }
    .toast.exito{border-left-color:#28a745}.toast.error{border-left-color:#dc3545}
    .toast.aviso{border-left-color:#ffc107}.toast.info{border-left-color:#17a2b8}
    .toast-cerrar{background:none;border:none;font-size:1.2rem;cursor:pointer;color:#999;padding:0 0.25rem}
    ```

=== "JS"

    ``` js
    var iconosToast = { exito: '\u2705', error: '\u274C', aviso: '\u26A0\uFE0F', info: '\u2139\uFE0F' };
    function mostrarToast(tipo, mensaje, duracion) {
      duracion = duracion || 4000;
      var contenedor = document.getElementById('toastContainer');
      var toast = document.createElement('div');
      toast.className = 'toast ' + tipo;
      toast.setAttribute('role', 'status');
      toast.innerHTML = '<span aria-hidden="true">' + (iconosToast[tipo] || '') + '</span>' +
        '<span style="flex:1">' + mensaje + '</span>' +
        '<button class="toast-cerrar" aria-label="Cerrar">&times;</button>';
      contenedor.insertBefore(toast, contenedor.firstChild);
      var timer = setTimeout(eliminar, duracion);
      function eliminar() {
        if (timer) clearTimeout(timer);
        toast.classList.add('saliendo');
        setTimeout(function() { if (toast.parentNode) toast.remove(); }, 300);
      }
      toast.querySelector('.toast-cerrar').addEventListener('click', eliminar);
      toast.addEventListener('mouseenter', function() { if (timer) { clearTimeout(timer); timer = null; } });
      toast.addEventListener('mouseleave', function() { if (!timer) timer = setTimeout(eliminar, duracion); });
      var toasts = contenedor.querySelectorAll('.toast');
      if (toasts.length > 5) { toasts[toasts.length - 1].classList.add('saliendo'); }
    }
    ```

### Ejemplo Guiado 4: Modal Accesible con Focus Trapping

=== "HTML"

    ``` html
    <div class="ejemplo-container">
      <h3>Ejemplo 4: Modal Accesible</h3>
      <button class="btn-demo btn-exito" id="abrirModal" aria-haspopup="dialog">Abrir Modal</button>
    </div>
    <div class="modal-overlay" id="modalOverlay" aria-hidden="true"></div>
    <div class="modal-dialog" id="modalDialog" role="dialog" aria-modal="true" aria-labelledby="modalTitle" aria-hidden="true">
      <div class="modal-box">
        <div class="modal-header">
          <h3 id="modalTitle" style="margin:0">Confirmar acción</h3>
          <button class="modal-close-btn" id="modalClose" aria-label="Cerrar">&times;</button>
        </div>
        <div class="modal-body"><p>¿Estás seguro de realizar esta acción? No se puede deshacer.</p></div>
        <div class="modal-footer">
          <button class="btn-demo" style="background:#6c757d" id="modalCancel">Cancelar</button>
          <button class="btn-demo btn-error" id="modalConfirm">Confirmar</button>
        </div>
      </div>
    </div>

    <link rel="stylesheet" href="./styles.css">

    <script src="./script.js"></script>
    ```

=== "CSS"

    ``` css
    .modal-overlay { position: fixed; inset:0; background: rgba(0,0,0,0.5); z-index: 1000; opacity:0; visibility:hidden; transition: opacity 0.3s ease, visibility 0.3s ease; }
    .modal-overlay.visible { opacity:1; visibility:visible; }
    .modal-dialog { position: fixed; inset:0; z-index:1001; display:flex; align-items:center; justify-content:center; opacity:0; visibility:hidden; transition: opacity 0.3s ease, visibility 0.3s ease; }
    .modal-dialog.visible { opacity:1; visibility:visible; }
    .modal-box { background: #fff; border-radius: 0.75rem; box-shadow: 0 10px 40px rgba(0,0,0,0.2); width:90%; max-width:450px; transform:translateY(20px); transition: transform 0.3s ease; }
    .modal-dialog.visible .modal-box { transform:translateY(0); }
    .modal-header { display:flex; justify-content:space-between; align-items:center; padding:1rem 1.25rem; border-bottom:1px solid #eee; }
    .modal-body { padding: 1.25rem; color: #555; line-height: 1.6; }
    .modal-footer { display:flex; justify-content:flex-end; gap:0.5rem; padding: 0.75rem 1.25rem; border-top:1px solid #eee; }
    .modal-close-btn { background:none; border:none; font-size:1.5rem; cursor:pointer; color:#999; }
    ```

=== "JS"

    ``` js
    (function() {
      var overlay = document.getElementById('modalOverlay');
      var dialog = document.getElementById('modalDialog');
      var btnOpen = document.getElementById('abrirModal');
      var btnClose = document.getElementById('modalClose');
      var btnCancel = document.getElementById('modalCancel');
      var btnConfirm = document.getElementById('modalConfirm');
      var lastFocus = null;

      function getFocusable() {
        return dialog.querySelectorAll('button:not([disabled]), [tabindex]:not([tabindex="-1"])');
      }

      function trapFocus(e) {
        if (e.key !== 'Tab') return;
        var focusable = getFocusable();
        if (focusable.length === 0) return;
        var first = focusable[0];
        var last = focusable[focusable.length - 1];
        if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
        else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
      }

      function openModal() {
        lastFocus = document.activeElement;
        overlay.classList.add('visible'); dialog.classList.add('visible');
        overlay.setAttribute('aria-hidden', 'false'); dialog.setAttribute('aria-hidden', 'false');
        document.body.style.overflow = 'hidden';
        setTimeout(function() { btnClose.focus(); }, 100);
        dialog.addEventListener('keydown', trapFocus);
      }

      function closeModal() {
        overlay.classList.remove('visible'); dialog.classList.remove('visible');
        overlay.setAttribute('aria-hidden', 'true'); dialog.setAttribute('aria-hidden', 'true');
        document.body.style.overflow = '';
        dialog.removeEventListener('keydown', trapFocus);
        if (lastFocus) { lastFocus.focus(); lastFocus = null; }
      }

      btnOpen.addEventListener('click', openModal);
      btnClose.addEventListener('click', closeModal);
      btnCancel.addEventListener('click', closeModal);
      overlay.addEventListener('click', closeModal);
      btnConfirm.addEventListener('click', function() { closeModal(); });

      document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && dialog.classList.contains('visible')) closeModal();
      });
    })();
    ```

### Ejemplo Guiado 5: Acordeón FAQ Accesible

=== "HTML"

    ``` html
    <div class="ejemplo-container">
      <h3>Ejemplo 5: Acordeón FAQ</h3>
      <div class="faq-list">
        <div class="faq-item">
          <button class="faq-btn" aria-expanded="false" aria-controls="faq1">¿Cuál es el plazo de entrega? <span class="faq-arrow" aria-hidden="true">+</span></button>
          <div class="faq-panel" id="faq1" role="region" aria-labelledby="faq-btn1" hidden>
            <div class="faq-content">El plazo estándar es de 3 a 5 días laborables para envíos nacionales. Los envíos internacionales pueden tardar entre 7 y 15 días según el destino y los trámites aduaneros.</div>
          </div>
        </div>
        <div class="faq-item">
          <button class="faq-btn" aria-expanded="false" aria-controls="faq2">¿Puedo devolver un producto? <span class="faq-arrow" aria-hidden="true">+</span></button>
          <div class="faq-panel" id="faq2" role="region" aria-labelledby="faq-btn2" hidden>
            <div class="faq-content">Dispones de 30 días desde la recepción. El producto debe estar en su embalaje original y sin signos de uso. Los cambios de talla tienen devolución gratuita.</div>
          </div>
        </div>
        <div class="faq-item">
          <button class="faq-btn" aria-expanded="false" aria-controls="faq3">¿Qué métodos de pago aceptáis? <span class="faq-arrow" aria-hidden="true">+</span></button>
          <div class="faq-panel" id="faq3" role="region" aria-labelledby="faq-btn3" hidden>
            <div class="faq-content">Aceptamos Visa, Mastercard, American Express, PayPal, transferencia bancaria y financiación mediante Klarna. Todos los pagos usan cifrado SSL.</div>
          </div>
        </div>
      </div>
    </div>

    <link rel="stylesheet" href="./styles.css">

    <script src="./script.js"></script>
    ```

=== "CSS"

    ``` css
    .faq-list { max-width: 600px; }
    .faq-item { border: 1px solid #e0e0e0; border-radius: 0.5rem; margin-bottom: 0.5rem; overflow: hidden; background: #fff; }
    .faq-btn { display: flex; justify-content: space-between; align-items: center; width: 100%; padding: 0.9rem 1.1rem; background: none; border: none; font-size: 0.95rem; font-weight: 500; color: #333; cursor: pointer; text-align: left; }
    .faq-btn:hover { background: #f8f9fa; }
    .faq-btn:focus-visible { outline: 3px solid #4a90d9; outline-offset: -3px; border-radius: 0.5rem; }
    .faq-btn[aria-expanded="true"] { color: #4a90d9; background: #f0f5ff; }
    .faq-arrow { font-size: 1.3rem; transition: transform 0.3s ease; color: #999; }
    .faq-btn[aria-expanded="true"] .faq-arrow { transform: rotate(45deg); color: #4a90d9; }
    .faq-panel { max-height: 0; overflow: hidden; opacity: 0; transition: max-height 0.4s ease, opacity 0.3s ease; }
    .faq-panel:not([hidden]) { max-height: 300px; opacity: 1; }
    .faq-content { padding: 0 1.1rem 1.1rem; color: #555; line-height: 1.7; }
    ```

=== "JS"

    ``` js
    (function() {
      var btns = document.querySelectorAll('.faq-btn');
      var btnArray = Array.from(btns);

      function togglePanel(btn) {
        var panel = document.getElementById(btn.getAttribute('aria-controls'));
        var expanded = btn.getAttribute('aria-expanded') === 'true';
        btn.setAttribute('aria-expanded', !expanded);
        if (expanded) panel.setAttribute('hidden', '');
        else panel.removeAttribute('hidden');
      }

      btnArray.forEach(function(btn, i) {
        btn.addEventListener('click', function() { togglePanel(btn); });
        btn.addEventListener('keydown', function(e) {
          var target = null;
          if (e.key === 'ArrowDown') { e.preventDefault(); target = btnArray[(i+1) % btnArray.length]; }
          else if (e.key === 'ArrowUp') { e.preventDefault(); target = btnArray[(i-1+btnArray.length) % btnArray.length]; }
          else if (e.key === 'Home') { e.preventDefault(); target = btnArray[0]; }
          else if (e.key === 'End') { e.preventDefault(); target = btnArray[btnArray.length-1]; }
          else if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); togglePanel(btn); }
          if (target) target.focus();
        });
      });
    })();
    ```

### Ejemplo Guiado 6: Tabs con Indicador Animado

=== "HTML"

    ``` html
    <div class="ejemplo-container">
      <h3>Ejemplo 6: Sistema de Tabs</h3>
      <div class="tabs-wrapper">
        <div class="tabs-nav" role="tablist" aria-label="Panel de configuración">
          <button class="tab-btn active" role="tab" aria-selected="true" aria-controls="tabPanel1" tabindex="0">General</button>
          <button class="tab-btn" role="tab" aria-selected="false" aria-controls="tabPanel2" tabindex="-1">Seguridad</button>
          <button class="tab-btn" role="tab" aria-selected="false" aria-controls="tabPanel3" tabindex="-1">Notificaciones</button>
          <span class="tab-indicator" aria-hidden="true"></span>
        </div>
        <div class="tab-panel" id="tabPanel1" role="tabpanel"><p>Ajusta idioma, zona horaria, formato de fecha y moneda predeterminada.</p></div>
        <div class="tab-panel" id="tabPanel2" role="tabpanel" hidden><p>Configura autenticación en dos factores, cambia contraseña y revisa dispositivos conectados.</p></div>
        <div class="tab-panel" id="tabPanel3" role="tabpanel" hidden><p>Gestiona notificaciones por email, push y dentro de la app. Modo No Molestar configurable.</p></div>
      </div>
    </div>

    <link rel="stylesheet" href="./styles.css">

    <script src="./script.js"></script>
    ```

=== "CSS"

    ``` css
    .tabs-wrapper { max-width: 600px; }
    .tabs-nav { display: flex; position: relative; border-bottom: 2px solid #e0e0e0; }
    .tab-btn { padding: 0.7rem 1.2rem; background: none; border: none; font-size: 0.9rem; font-weight: 500; color: #666; cursor: pointer; outline: none; transition: color 0.25s; }
    .tab-btn.active { color: #4a90d9; }
    .tab-btn:focus-visible { box-shadow: inset 0 0 0 3px #4a90d9; border-radius: 4px 4px 0 0; }
    .tab-indicator { position: absolute; bottom: -2px; left: 0; height: 3px; background: #4a90d9; border-radius: 3px 3px 0 0; transition: left 0.3s ease, width 0.3s ease; }
    .tab-panel { padding: 1.2rem; background: #fff; border: 1px solid #e0e0e0; border-top: none; border-radius: 0 0 0.5rem 0.5rem; animation: fadeIn 0.3s ease; color: #555; line-height: 1.6; }
    @keyframes fadeIn { from{opacity:0;transform:translateY(6px)} to{opacity:1;transform:translateY(0)} }
    ```

=== "JS"

    ``` js
    (function() {
      var tabs = Array.from(document.querySelectorAll('.tab-btn'));
      var panels = Array.from(document.querySelectorAll('.tab-panel'));
      var indicator = document.querySelector('.tab-indicator');
      var nav = document.querySelector('.tabs-nav');

      function moveIndicator(tab) {
        var tabRect = tab.getBoundingClientRect();
        var navRect = nav.getBoundingClientRect();
        indicator.style.left = (tabRect.left - navRect.left) + 'px';
        indicator.style.width = tabRect.width + 'px';
      }

      function activateTab(tab) {
        tabs.forEach(function(t) { t.classList.remove('active'); t.setAttribute('aria-selected','false'); t.setAttribute('tabindex','-1'); });
        panels.forEach(function(p) { p.setAttribute('hidden',''); });
        tab.classList.add('active');
        tab.setAttribute('aria-selected','true');
        tab.setAttribute('tabindex','0');
        var panel = document.getElementById(tab.getAttribute('aria-controls'));
        if (panel) panel.removeAttribute('hidden');
        moveIndicator(tab);
      }

      tabs.forEach(function(tab, i) {
        tab.addEventListener('click', function() { activateTab(tab); });
      });

      nav.addEventListener('keydown', function(e) {
        var idx = tabs.indexOf(document.activeElement);
        if (idx === -1) return;
        var target = null;
        if (e.key === 'ArrowRight') { e.preventDefault(); target = tabs[(idx+1) % tabs.length]; }
        else if (e.key === 'ArrowLeft') { e.preventDefault(); target = tabs[(idx-1+tabs.length) % tabs.length]; }
        else if (e.key === 'Home') { e.preventDefault(); target = tabs[0]; }
        else if (e.key === 'End') { e.preventDefault(); target = tabs[tabs.length-1]; }
        else if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); activateTab(document.activeElement); return; }
        if (target) target.focus();
      });

      var initial = document.querySelector('.tab-btn.active');
      if (initial) moveIndicator(initial);
      window.addEventListener('resize', function() {
        var active = document.querySelector('.tab-btn.active');
        if (active) moveIndicator(active);
      });
    })();
    ```

### Ejemplo Guiado 7: Carrusel Accesible con Dots y Arrows

=== "HTML"

    ``` html
    <div class="ejemplo-container">
      <h3>Ejemplo 7: Carrusel Slider</h3>
      <div class="carousel" aria-roledescription="carrusel" aria-label="Galería destacada">
        <button class="carousel-arrow carousel-prev" aria-label="Anterior">&lsaquo;</button>
        <div class="carousel-viewport">
          <ul class="carousel-track">
            <li class="carousel-slide active" role="group" aria-roledescription="diapositiva" aria-label="1 de 4">
              <div style="background:linear-gradient(135deg,#667eea,#764ba2);min-height:200px;display:flex;align-items:center;justify-content:center;color:#fff;font-size:1.3rem;border-radius:0.5rem">Slide 1</div>
            </li>
            <li class="carousel-slide" role="group" aria-roledescription="diapositiva" aria-label="2 de 4">
              <div style="background:linear-gradient(135deg,#f093fb,#f5576c);min-height:200px;display:flex;align-items:center;justify-content:center;color:#fff;font-size:1.3rem;border-radius:0.5rem">Slide 2</div>
            </li>
            <li class="carousel-slide" role="group" aria-roledescription="diapositiva" aria-label="3 de 4">
              <div style="background:linear-gradient(135deg,#4facfe,#00f2fe);min-height:200px;display:flex;align-items:center;justify-content:center;color:#fff;font-size:1.3rem;border-radius:0.5rem">Slide 3</div>
            </li>
            <li class="carousel-slide" role="group" aria-roledescription="diapositiva" aria-label="4 de 4">
              <div style="background:linear-gradient(135deg,#fa709a,#fee140);min-height:200px;display:flex;align-items:center;justify-content:center;color:#fff;font-size:1.3rem;border-radius:0.5rem">Slide 4</div>
            </li>
          </ul>
        </div>
        <button class="carousel-arrow carousel-next" aria-label="Siguiente">&rsaquo;</button>
        <div class="carousel-dots" aria-label="Navegación"></div>
      </div>
    </div>

    <link rel="stylesheet" href="./styles.css">

    <script src="./script.js"></script>
    ```

=== "CSS"

    ``` css
    .carousel { position: relative; max-width: 600px; }
    .carousel-viewport { overflow: hidden; border-radius: 0.5rem; }
    .carousel-track { display: flex; list-style: none; margin: 0; padding: 0; transition: transform 0.5s ease; }
    .carousel-slide { flex: 0 0 100%; min-width: 0; }
    .carousel-arrow {
      position: absolute; top: 50%; transform: translateY(-50%); z-index: 10;
      background: rgba(255,255,255,0.9); border: none; width: 36px; height: 36px;
      border-radius: 50%; font-size: 1.6rem; color: #333; cursor: pointer;
      box-shadow: 0 2px 6px rgba(0,0,0,0.15); display: flex; align-items: center; justify-content: center;
    }
    .carousel-prev { left: 0.5rem; } .carousel-next { right: 0.5rem; }
    .carousel-arrow:focus-visible { outline: 3px solid #4a90d9; outline-offset: 2px; }
    .carousel-dots { display: flex; justify-content: center; gap: 0.5rem; padding: 0.8rem 0; }
    .carousel-dot { width: 10px; height: 10px; border-radius: 50%; border: 2px solid #c0c0c0; background: transparent; cursor: pointer; padding: 0; transition: background 0.3s, border-color 0.3s; }
    .carousel-dot.active { background: #4a90d9; border-color: #4a90d9; }
    ```

=== "JS"

    ``` js
    (function() {
      var track = document.querySelector('.carousel-track');
      var dotsContainer = document.querySelector('.carousel-dots');
      var slides = Array.from(document.querySelectorAll('.carousel-slide'));
      var current = 0;
      var total = slides.length;
      var timer = null;

      function generateDots() {
        dotsContainer.innerHTML = '';
        slides.forEach(function(_, i) {
          var dot = document.createElement('button');
          dot.className = 'carousel-dot' + (i === current ? ' active' : '');
          dot.setAttribute('aria-label', 'Ir a diapositiva ' + (i+1));
          dot.addEventListener('click', function() { goTo(i); resetTimer(); });
          dotsContainer.appendChild(dot);
        });
      }

      function updateDots() {
        var dots = dotsContainer.querySelectorAll('.carousel-dot');
        dots.forEach(function(d, i) { d.classList.toggle('active', i === current); });
      }

      function goTo(i) {
        current = ((i % total) + total) % total;
        track.style.transform = 'translateX(-' + (current * 100) + '%)';
        updateDots();
      }

      function next() { goTo(current + 1); }
      function prev() { goTo(current - 1); }
      function resetTimer() { if (timer) clearInterval(timer); timer = setInterval(next, 4000); }

      document.querySelector('.carousel-prev').addEventListener('click', function() { prev(); resetTimer(); });
      document.querySelector('.carousel-next').addEventListener('click', function() { next(); resetTimer(); });
      generateDots(); goTo(0); resetTimer();
    })();
    ```

### Ejemplo Guiado 8: Dark Mode Toggle con localStorage

=== "HTML"

    ``` html
    <div class="ejemplo-container">
      <h3>Ejemplo 8: Dark Mode Toggle</h3>
      <button class="dark-toggle" id="darkToggle" aria-pressed="false" aria-label="Activar modo oscuro">
        <span class="dark-icon-sun">&#9728;&#65039;</span>
        <span class="dark-icon-moon">&#127769;</span>
      </button>
      <div class="dark-card">
        <h4>Tarjeta de ejemplo</h4>
        <p>Este texto cambia de color según el tema activo. La preferencia se guarda en localStorage y se respeta la configuración del sistema.</p>
      </div>
    </div>

    <link rel="stylesheet" href="./styles.css">

    <script src="./script.js"></script>
    ```

=== "CSS"

    ``` css
    :root {
      --bg: #fff; --text: #333; --card-bg: #f8f9fa; --border: #e0e0e0;
      --transition-theme: background-color 0.4s ease, color 0.3s ease, border-color 0.3s ease;
    }
    html.dark {
      --bg: #1a1a2e; --text: #e0e0e0; --card-bg: #16213e; --border: #333355;
    }
    body { background: var(--bg); color: var(--text); transition: var(--transition-theme); }
    .dark-card { background: var(--card-bg); border: 1px solid var(--border); border-radius: 0.75rem; padding: 1.5rem; margin-top: 1rem; transition: var(--transition-theme); }
    .dark-card h4 { margin: 0 0 0.5rem; }
    .dark-card p { margin: 0; line-height: 1.6; opacity: 0.8; }
    .dark-toggle {
      background: var(--card-bg); border: 2px solid var(--border); border-radius: 50%;
      width: 44px; height: 44px; cursor: pointer; font-size: 1.3rem;
      display: flex; align-items: center; justify-content: center;
      transition: var(--transition-theme);
      color: var(--text);
    }
    .dark-toggle:focus-visible { outline: 3px solid #4a90d9; outline-offset: 3px; }
    html:not(.dark) .dark-icon-moon { display: none; }
    html.dark .dark-icon-sun { display: none; }
    ```

=== "JS"

    ``` js
    (function() {
      var toggle = document.getElementById('darkToggle');
      var html = document.documentElement;
      function apply(active) {
        html.classList.toggle('dark', active);
        toggle.setAttribute('aria-pressed', active ? 'true' : 'false');
        toggle.setAttribute('aria-label', active ? 'Activar modo claro' : 'Activar modo oscuro');
        try { localStorage.setItem('theme', active ? 'dark' : 'light'); } catch(e) {}
      }
      toggle.addEventListener('click', function() { apply(!html.classList.contains('dark')); });
      // Inicializar: localStorage > preferencia del sistema > claro
      var saved = localStorage.getItem('theme');
      if (saved === 'dark') apply(true);
      else if (saved === 'light') apply(false);
      else if (window.matchMedia('(prefers-color-scheme: dark)').matches) apply(true);
      else apply(false);
    })();
    ```

### Ejemplo Guiado 9: Scroll Reveal con Intersection Observer

=== "HTML"

    ``` html
    <div class="ejemplo-container">
      <h3>Ejemplo 9: Scroll Reveal</h3>
      <p style="color:#666;margin-bottom:1.5rem">Haz scroll para ver las animaciones de entrada.</p>
      <div class="reveal-item" style="min-height:80px;background:var(--card-bg);border-radius:0.5rem;padding:1.5rem;margin-bottom:1rem;border:1px solid var(--border)">
        <strong>Elemento 1</strong><br>Este elemento aparece con animación al hacer scroll.
      </div>
      <div class="reveal-item" style="min-height:80px;background:var(--card-bg);border-radius:0.5rem;padding:1.5rem;margin-bottom:1rem;border:1px solid var(--border)">
        <strong>Elemento 2</strong><br>Cada elemento se revela de forma independiente.
      </div>
      <div class="reveal-item" style="min-height:80px;background:var(--card-bg);border-radius:0.5rem;padding:1.5rem;margin-bottom:1rem;border:1px solid var(--border)">
        <strong>Elemento 3</strong><br>Usamos Intersection Observer para máxima eficiencia.
      </div>
    </div>

    <link rel="stylesheet" href="./styles.css">

    <script src="./script.js"></script>
    ```

=== "CSS"

    ``` css
    .reveal-item {
      opacity: 0;
      transform: translateY(30px);
      transition: opacity 0.6s ease, transform 0.6s ease;
    }
    .reveal-item.revealed {
      opacity: 1;
      transform: translateY(0);
    }
    ```

=== "JS"

    ``` js
    (function() {
      var observer = new IntersectionObserver(function(entries) {
        entries.forEach(function(entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('revealed');
            observer.unobserve(entry.target); // Solo una vez
          }
        });
      }, { threshold: 0.15, rootMargin: '0px 0px -30px 0px' });

      document.querySelectorAll('.reveal-item').forEach(function(el) {
        observer.observe(el);
      });
    })();
    ```

### Ejemplo Guiado 10: Drag and Drop para Reordenar Lista

=== "HTML"

    ``` html
    <div class="ejemplo-container">
      <h3>Ejemplo 10: Drag and Drop</h3>
      <ul class="draggable-list" id="dragList">
        <li class="drag-item" draggable="true">&#9776; Tarea 1: Revisar documentación</li>
        <li class="drag-item" draggable="true">&#9776; Tarea 2: Implementar API</li>
        <li class="drag-item" draggable="true">&#9776; Tarea 3: Escribir tests</li>
        <li class="drag-item" draggable="true">&#9776; Tarea 4: Desplegar en staging</li>
      </ul>
    </div>

    <link rel="stylesheet" href="./styles.css">

    <script src="./script.js"></script>
    ```

=== "CSS"

    ``` css
    .draggable-list { list-style: none; padding: 0; max-width: 450px; }
    .drag-item {
      padding: 0.8rem 1rem; margin-bottom: 0.4rem; background: #fff;
      border: 1px solid #e0e0e0; border-radius: 0.5rem; cursor: grab;
      transition: background 0.2s, border-color 0.2s, box-shadow 0.2s;
    }
    .drag-item:hover { background: #f8f9fa; border-color: #c0c0c0; }
    .drag-item:active { cursor: grabbing; }
    .drag-item.dragging { opacity: 0.5; background: #f0f0f0; }
    .drag-item.drag-over { border-color: #4a90d9; border-style: dashed; background: #f0f5ff; }
    ```

=== "JS"

    ``` js
    (function() {
      var list = document.getElementById('dragList');
      var items = list.querySelectorAll('.drag-item');
      var draggedItem = null;

      items.forEach(function(item) {
        item.addEventListener('dragstart', function(e) {
          draggedItem = this;
          this.classList.add('dragging');
          e.dataTransfer.effectAllowed = 'move';
          e.dataTransfer.setData('text/plain', this.textContent);
        });

        item.addEventListener('dragend', function() {
          this.classList.remove('dragging');
          document.querySelectorAll('.drag-item').forEach(function(el) { el.classList.remove('drag-over'); });
          draggedItem = null;
        });

        item.addEventListener('dragover', function(e) {
          e.preventDefault();
          if (this !== draggedItem) this.classList.add('drag-over');
          e.dataTransfer.dropEffect = 'move';
        });

        item.addEventListener('dragleave', function() {
          this.classList.remove('drag-over');
        });

        item.addEventListener('drop', function(e) {
          e.preventDefault();
          this.classList.remove('drag-over');
          if (this !== draggedItem) {
            var all = Array.from(list.querySelectorAll('.drag-item'));
            var from = all.indexOf(draggedItem);
            var to = all.indexOf(this);
            if (from < to) {
              list.insertBefore(draggedItem, this.nextSibling);
            } else {
              list.insertBefore(draggedItem, this);
            }
          }
        });
      });
    })();
    ```


## Casos reales

### Caso Real 1: Twitter/X — La maestría de la microinteracción

Twitter (ahora X) es un estudio de caso fascinante sobre cómo las microinteracciones pueden definir la experiencia completa de un producto. Analicemos en profundidad las decisiones de interactividad que hacen de esta plataforma un referente del diseño de interfaces:

- **Botón de Like (corazón)** — cuando un usuario hace clic en el corazón, Twitter no se limita a cambiar el color del icono. Despliega una coreografía completa de retroalimentación: el corazón ejecuta una animación de escala en tres fases (expansión rápida, contracción parcial, retorno a escala normal) que dura aproximadamente **400 ms** y utiliza una curva de *easing* que sobresale ligeramente de 1 (*overshoot*), creando un efecto elástico. Simultáneamente, pequeñas partículas o chispas de colores (confeti) se desprenden del icono en direcciones radiales con una animación de opacidad y desplazamiento, añadiendo una capa de deleite visual. El contador de likes se actualiza con una transición numérica. En la app nativa móvil, se emite una breve vibración háptica (aproximamente **15 ms**) que proporciona confirmación táctil. Si la petición al servidor falla, el cambio se revierte localmente y aparece un *toast* de error sutil. Esta microinteracción ejemplifica los cuatro elementos de Saffer: *trigger* (clic/toque), *rules* (toggle like, petición asíncrona, actualización optimista), *feedback* (visual + háptico multicanal), y *loops* (reintento en error, sincronización en tiempo real).
- **Indicador de scroll con actualización de contador** — en la versión web, Twitter implementa un sutil indicador en la parte superior que muestra cuántos tweets nuevos hay sin leer mientras el usuario hace *scroll*. Utiliza Intersection Observer para detectar cuándo el usuario ha leído tweets, *throttle* para el evento `scroll`, y `requestAnimationFrame` para actualizar el contador sin *jank*.
- **Carga de tweets (*infinite scroll*)** — Twitter utiliza Intersection Observer para detectar cuándo el usuario se acerca al final del *timeline* y cargar asíncronamente más tweets. Antes de cargar, muestra *skeleton screens* (rectángulos con *shimmer*) que anticipan la estructura del contenido que está por llegar, evitando saltos de *layout* y reduciendo la percepción de espera.

### Caso Real 2: Notion — Interactividad al servicio de la productividad

Notion es un ejemplo magistral de cómo la interactividad puede hacer que una herramienta compleja se sienta simple e intuitiva. Analicemos sus decisiones:

- **Drag and drop omnipresente** — Notion permite arrastrar cualquier bloque de contenido (texto, imágenes, tablas, bases de datos) para reordenarlo en la página o moverlo a otra página. Implementa la API HTML5 Drag and Drop con un sofisticado sistema de indicadores visuales: durante el arrastre, aparece una línea azul horizontal que muestra exactamente dónde se insertará el bloque al soltarlo, calculada dinámicamente según la posición del cursor. Esta retroalimentación reduce drásticamente los errores de colocación.
- **Menú slash (`/`) contextual** — al escribir "/" en cualquier bloque, aparece un menú flotante con cientos de comandos. La implementación es un prodigio de rendimiento: utiliza *debounce* en la búsqueda (**300 ms**), virtualización para manejar cientos de items sin degradar el rendimiento, navegación completa por teclado con flechas y filtrado por texto, y `aria-activedescendant` para mantener la accesibilidad en un componente tan dinámico.
- **Sidebar colapsable con animación** — la barra lateral se colapsa y expande con una transición suave que utiliza `transform: translateX()` en lugar de animar el `width`, lo que garantiza 60 fps porque las transformaciones solo afectan a la capa de composición y no disparan *reflow*. El botón *toggle* utiliza `aria-expanded` para comunicar el estado.

### Caso Real 3: Linear — La referencia en rendimiento y detalle

Linear, la aplicación de gestión de proyectos para equipos de desarrollo, es ampliamente reconocida en la comunidad tech por establecer un nuevo estándar de fluidez y atención al detalle en interfaces web. Analicemos sus decisiones:

- **Teclas de acceso rápido universales** — Linear implementa un sistema de atajos de teclado que cubre prácticamente cada acción posible, con un diálogo de ayuda (Cmd+K) que lista todos los atajos disponibles con búsqueda en tiempo real. La detección de atajos utiliza `keydown` en `document` con verificación de modificadores (`event.metaKey`, `event.ctrlKey`, `event.shiftKey`) y un sistema de prioridades para evitar conflictos. Los atajos se agrupan por contexto (lista de issues, detalle de issue, editor) y se desactivan automáticamente cuando un campo de texto tiene el foco.
- **Animaciones con velocidades variables** — Linear ajusta la duración de las animaciones según el contexto. Las transiciones de navegación entre vistas son rápidas (**150-200 ms**) para no entorpecer el flujo de trabajo. Los *tooltips* y *popovers* tienen un ligero retardo de aparición (**200 ms**) para no aparecer accidentalmente al mover el ratón, pero desaparecen instantáneamente (**0 ms**) al mover el cursor fuera. Esta calibración refleja una profunda comprensión de cómo las personas interactúan con herramientas profesionales.
- **Command palette (Cmd+K)** — el paleta de comandos de Linear es un modelo de implementación. Aparece con una animación de escala+opacidad que dura **150 ms** (lo suficientemente rápida para no sentirse lenta, lo suficientemente larga para que el cerebro registre la transición). Implementa *focus trapping*, navegación por teclado completa, búsqueda con *debounce* (**150 ms** — más agresivo que los 300 ms típicos porque los usuarios de Linear son *developers* que escriben rápido), y `aria-live` para anunciar el número de resultados.


## Actividades guiadas

### Actividad Guiada 1: Construcción de un Sistema de Validación de Formulario en Tiempo Real

**Objetivo:** Construir un formulario de registro con validación visual en tiempo real que proporcione retroalimentación inmediata al usuario en cada campo mediante iconos, colores y mensajes de error accesibles.

**Material necesario:** Editor de código (VS Code), navegador con DevTools, conocimientos previos de HTML, CSS y JavaScript (eventos, DOM, validación con expresiones regulares).

**Duración estimada:** 90 minutos.

**Desarrollo paso a paso:**

1. **Crear la estructura HTML semántica:** Define un `<form>` con `novalidate` (para desactivar la validación nativa y usar la nuestra). Crea campos para nombre, email, contraseña y confirmación de contraseña. Cada campo debe tener su `<label>` asociado mediante `for`/`id`, un contenedor para el mensaje de error con `aria-live="polite"` y un `<span>` para el icono de estado. Añade un `<fieldset>` con `<legend>` para agrupar los campos y un botón de submit.

2. **Definir las reglas de validación en JavaScript:** Crea un objeto de configuración donde cada campo tenga asociado un array de reglas. Cada regla es un objeto con una función de validación (que recibe el valor y devuelve `true` si es válido) y un mensaje de error. Implementa reglas para: campo requerido, longitud mínima, longitud máxima, formato de email (regex), complejidad de contraseña (mínimo una mayúscula, un número, un carácter especial), y coincidencia entre contraseña y confirmación.

3. **Implementar la validación por campo:** Crea una función `validarCampo(input)` que itere sobre las reglas del campo, ejecute cada validación y determine el primer error encontrado o `null` si es válido. Esta función debe también activar/desactivar las clases CSS correspondientes (`valido` o `invalido`), mostrar/ocultar el mensaje de error, y actualizar el icono de estado.

4. **Implementar la validación en tiempo real con debounce:** Conecta el evento `input` de cada campo a la función de validación, pero envuelta en un debounce de 300 ms para no validar en cada pulsación. Conecta también el evento `blur` para validar inmediatamente cuando el usuario abandona el campo (sin debounce).

5. **Añadir animaciones de feedback:** Define transiciones CSS para los cambios de color del borde del input, la aparición/desaparición del mensaje de error (usando `max-height` y `opacity`), y una animación de "shake" (vibración horizontal) para los campos inválidos al perder el foco.

6. **Validación final en submit:** En el evento `submit`, valida todos los campos. Si hay errores, previene el envío, enfoca el primer campo inválido y muestra un resumen de errores en una región `aria-live="assertive"`. Si todo es válido, muestra un toast de éxito.

**Entregable:** Un archivo HTML único con el formulario completo, funcional y estilizado, con todos los comentarios explicativos.

### Actividad Guiada 2: Implementación de un Menú Hamburguesa con Animación de Morphing

**Objetivo:** Construir un menú de navegación responsive que en dispositivos móviles muestre un icono de hamburguesa con animación de transformación a X, desplegando un menú con transición suave y overlay.

**Material necesario:** Editor de código, navegador con DevTools, conocimientos de CSS transitions, `@keyframes` y JavaScript para eventos.

**Duración estimada:** 60 minutos.

**Desarrollo paso a paso:**

1. **Estructura HTML:** Construye un `<header>` con un `<nav>` que contenga el logo a la izquierda, una lista de enlaces `<ul>` en el centro (oculta en móvil), y un `<button>` con `aria-expanded="false"` que contenga tres `<span>` (las rayas de la hamburguesa). Usa `aria-controls` para vincular el botón con el menú y `aria-label` en el botón.

2. **Estilos CSS base:** Define el layout con Flexbox. Establece los estilos de escritorio (menú horizontal visible) y utiliza una media query a 768px para ocultar el menú horizontal y mostrar el botón hamburguesa.

3. **Animación de morphing:** Cada `<span>` de la hamburguesa es una barra horizontal. Define transiciones CSS para `transform` y `opacity` con una duración de 0.3 s y `cubic-bezier`. Cuando el menú está abierto (clase `.open` en el botón), el primer span rota 45 grados y se traslada para formar la diagonal ascendente de la X, el segundo span se desvanece (opacity: 0), y el tercer span rota -45 grados y se traslada para formar la diagonal descendente.

4. **Menú desplegable en móvil:** El menú móvil es un panel que se posiciona debajo del header con `position: absolute`. La animación de apertura/cierre utiliza `max-height` y `opacity` con transiciones CSS. Alternativamente, para un efecto más profesional, usa `transform: scaleY()` desde `transform-origin: top` para un despliegue desde arriba.

5. **Overlay semitransparente:** Añade un `<div>` overlay que cubra el resto de la pantalla cuando el menú está abierto, con fade in/out.

6. **JavaScript de control:** El clic en el botón hamburguesa alterna las clases y los atributos `aria-expanded`. El clic en el overlay o en un enlace del menú cierra el menú. La tecla Escape también cierra el menú y devuelve el foco al botón hamburguesa. Implementa cierre al hacer clic fuera mediante un listener en `document` con fase de captura.

7. **Accesibilidad:** Cuando el menú se abre, mueve el foco al primer enlace del menú. Cuando se cierra, devuelve el foco al botón hamburguesa. Asegura que todos los elementos sean operables por teclado y que el menú oculte su contenido de los lectores de pantalla cuando está cerrado.

**Entregable:** Código HTML/CSS/JS completo con el menú responsive funcional.

### Actividad Guiada 3: Galería de Imágenes con Lightbox y Navegación por Teclado

**Objetivo:** Crear una galería de imágenes en grid que al hacer clic en cualquier miniatura abra un lightbox a pantalla completa con navegación entre imágenes, soporte completo de teclado, y cumplimiento de pautas de accesibilidad.

**Duración estimada:** 75 minutos.

**Desarrollo paso a paso:**

1. **Grid de miniaturas:** Diseña una cuadrícula responsiva con CSS Grid (`grid-template-columns: repeat(auto-fill, minmax(250px, 1fr))`) para las miniaturas. Cada miniatura es un `<button>` (para ser accesible por teclado) que contiene una imagen y, opcionalmente, un caption. Usa `data-*` attributes para almacenar la URL de la imagen a tamaño completo y el caption.

2. **Estructura del lightbox:** Crea los elementos del lightbox ocultos inicialmente: overlay (`role="dialog"`, `aria-modal="true"`), botón de cierre, botones de navegación anterior/siguiente, contenedor de la imagen (`<img>`), caption, y contador.

3. **Apertura del lightbox:** Al hacer clic en una miniatura, recopila los datos de todas las imágenes (para saber el total y poder navegar), muestra el lightbox con animación fade, bloquea el scroll del body (`overflow: hidden`), y enfoca el botón de cierre.

4. **Navegación entre imágenes:** Implementa navegación mediante botones, teclado (ArrowLeft/ArrowRight) y gestos táctiles (swipe). Al cambiar de imagen, actualiza el `src`, el caption, el contador y el `alt` del `<img>`.

5. **Gestión del foco y cierre:** Implementa focus trapping dentro del lightbox (Tab/Shift+Tab). Cierra con Escape, clic en overlay, o botón de cierre. Al cerrar, devuelve el foco a la miniatura que abrió el lightbox.

6. **Precarga de imágenes:** Para una experiencia fluida, precarga la imagen siguiente y anterior creando elementos `<img>` en memoria (`new Image()`) y estableciendo su `src`. Esto evita que el usuario vea un parpadeo o tiempo de carga al navegar.

**Entregable:** Archivo HTML con galería completamente funcional y comentada.

### Actividad Guiada 4: Sistema de Pestañas (Tabs) con Contenido Cargado Asíncronamente

**Objetivo:** Construir un componente de pestañas donde cada panel cargue su contenido desde una API simulada, mostrando skeleton screens durante la carga y manejando estados de error.

**Duración estimada:** 90 minutos.

**Desarrollo paso a paso:**

1. **Estructura de tabs:** Crea la lista de pestañas con `role="tablist"`, cada una con `role="tab"`, `aria-selected` y `aria-controls`. Añade un indicador animado inferior que se deslice entre pestañas al cambiar de selección.

2. **Paneles dinámicos:** Cada panel (`role="tabpanel"`) comienza vacío. Al activar una pestaña por primera vez, se muestra un skeleton screen (tres rectángulos con shimmer) mientras se realiza la carga asíncrona. Si el contenido ya fue cargado previamente, se muestra inmediatamente desde la caché.

3. **Simulación de API:** Crea una función que simule una petición asíncrona con `setTimeout` y una promesa. Debe tardar entre 500 y 1500 ms aleatoriamente para simular latencia de red realista. Cada panel tiene contenido diferente. Implementa también un caso de error (falla aleatoriamente el 10% de las veces) para mostrar cómo manejar estados de error.

4. **Caché de contenido:** Almacena el contenido cargado en un objeto `Map` indexado por el ID del panel. Si el contenido ya existe en caché, se muestra inmediatamente. Si no, se inicia la carga. Esto mejora la eficiencia y evita recargas innecesarias.

5. **Estados de la UI:** Implementa cuatro estados visuales para cada panel: vacío (panel no visitado aún), cargando (skeleton screen), éxito (contenido renderizado), y error (mensaje con botón de reintentar).

**Entregable:** Componente de tabs con carga asíncrona y gestión de estados completo.

### Actividad Guiada 5: Implementación de un Buscador con Autocompletado y Debounce

**Objetivo:** Construir un campo de búsqueda que muestre sugerencias en tiempo real mientras el usuario escribe, utilizando debounce, teclado (flechas para navegar sugerencias) y accesibilidad con `aria-autocomplete`, `aria-activedescendant` y `role="listbox"`.

**Duración estimada:** 75 minutos.

**Desarrollo paso a paso:**

1. **Campo de búsqueda:** Un `<input type="search">` con `role="combobox"`, `aria-autocomplete="list"`, `aria-expanded`, `aria-owns` y `aria-activedescendant`. Una lista `<ul role="listbox">` oculta inicialmente donde aparecerán las sugerencias.

2. **Simulación de backend:** Crea un array de datos (mínimo 100 items: nombres de ciudades, productos, películas, etc.). La búsqueda debe filtrar por coincidencia parcial (substring) sin distinción de mayúsculas/minúsculas.

3. **Debounce en la búsqueda:** Implementa un debounce de 300 ms en el evento `input`. La función debounced envuelve la lógica de filtrado y renderizado de sugerencias.

4. **Renderizado de sugerencias:** Cada sugerencia es un `<li role="option">`. Limita el número de sugerencias visibles a 8-10 para no abrumar al usuario y por rendimiento. Destaca visualmente la parte del texto que coincide con la búsqueda (usando `<mark>` o `<strong>`).

5. **Navegación por teclado:** Flecha abajo/arriba mueven la selección virtual (actualizando `aria-activedescendant` y una clase CSS visual). Enter selecciona la sugerencia actual. Escape cierra las sugerencias. Tab selecciona y mueve el foco al siguiente elemento.

6. **Clic en sugerencia:** Selecciona el valor y cierra la lista. También permite navegar a la página de resultados pulsando Enter después de escribir sin seleccionar sugerencia.

**Entregable:** Campo de búsqueda con autocompletado completamente funcional y accesible.


## Actividades propuestas

### Actividad Propuesta 1: Implementar un Scroll Spy (Navegación por Anclas con Indicador)

Crea una página de documentación larga con múltiples secciones (mínimo 6) y una barra de navegación lateral fija. La barra debe resaltar automáticamente la sección actualmente visible mediante Intersection Observer y un indicador visual animado. La navegación debe permitir clic para desplazamiento suave (`scroll-behavior: smooth`). Implementa también un indicador de progreso de lectura en la parte superior de la página mediante el evento `scroll` con throttle. Todos los enlaces deben implementar `aria-current="true"` en la sección activa.

**Criterios de evaluación:**

- Uso correcto de Intersection Observer (2 puntos)
- Scroll suave y animaciones de transición (2 puntos)
- Accesibilidad con `aria-current` y navegación por teclado (2 puntos)
- Throttle en el evento scroll para el indicador de progreso (2 puntos)
- Código limpio, comentado y buenas prácticas (2 puntos)

### Actividad Propuesta 2: Construir un Kanban Board con Drag and Drop entre Columnas

Desarrolla un tablero Kanban simple con tres columnas (Por hacer, En progreso, Hecho). Cada columna contiene tarjetas que pueden arrastrarse entre columnas y reordenarse dentro de la misma columna. Implementa la API HTML5 Drag and Drop, con indicadores visuales durante el arrastre (silueta fantasma, zona de drop resaltada, tarjeta origen semitransparente). Añade teclado para mover tarjetas (Ctrl+ArrowKeys para mover entre columnas, ArrowKeys para reordenar dentro de la columna). Incluye un contador de tarjetas por columna que se actualice con animación.

**Criterios de evaluación:**

- Drag and Drop funcional entre columnas y reordenación (3 puntos)
- Indicadores visuales durante el arrastre (2 puntos)
- Soporte de teclado completo (2 puntos)
- Contadores animados y diseño responsive (2 puntos)
- Código organizado y comentado (1 punto)

### Actividad Propuesta 3: Crear un Reproductor de Vídeo Personalizado Accesible

Construye los controles personalizados de un reproductor de vídeo HTML5. Debe incluir: play/pause con animación de transición, barra de progreso clickable y arrastrable, control de volumen con slider y mute/unmute, velocidad de reproducción, pantalla completa, y tiempo actual/restante. Todos los controles deben ser accesibles por teclado con roles y atributos ARIA apropiados (`role="slider"`, `aria-valuenow`, `aria-valuemin`, `aria-valuemax`, `aria-label`). Añade atajos de teclado: Espacio para play/pause, flechas para adelantar/retroceder, M para mute.

**Criterios de evaluación:**

- Controles funcionales completos con la API de vídeo HTML5 (3 puntos)
- Accesibilidad de todos los controles (2 puntos)
- Diseño visual atractivo y animaciones (2 puntos)
- Atajos de teclado y enfoque visible (2 puntos)
- Código limpio y estructurado (1 punto)

### Actividad Propuesta 4: Desarrollar un Asistente Virtual (Chatbot) con Animaciones

Crea una interfaz de chatbot con una ventana de conversación. El chatbot simula respuestas automáticas basadas en palabras clave del usuario. Implementa: burbujas de chat con animación de entrada escalonada, indicador de "escribiendo..." con tres puntos animados, scroll automático al último mensaje, campo de entrada con envío por Enter, historial de conversación en localStorage. Diseña una interfaz atractiva con avatares, colores diferenciados para usuario y bot, y animaciones suaves. Añade accesibilidad con `aria-live` para nuevos mensajes y navegación por teclado.

**Criterios de evaluación:**

- Sistema de conversación funcional con respuestas automáticas (2 puntos)
- Animaciones de entrada de mensajes y typing indicator (2 puntos)
- Persistencia en localStorage y scroll automático (2 puntos)
- Diseño visual y experiencia de usuario (2 puntos)
- Accesibilidad con aria-live y teclado (2 puntos)

### Actividad Propuesta 5: Construir un Selector de Fecha (Date Picker) Accesible

Implementa un selector de fecha personalizado que se abra al hacer clic en un campo de texto o al presionar la tecla flecha abajo. Debe incluir: navegación por meses (anterior/siguiente), visualización de calendario mensual con encabezados de días de la semana, resaltado del día actual y del día seleccionado, días del mes anterior/siguiente atenuados, transiciones suaves al cambiar de mes. Navegación completa por teclado: flechas para mover el día, PageUp/PageDown para cambiar de mes, Home/End para primer/último día del mes, Enter para seleccionar, Escape para cerrar. Usa `role="grid"`, `role="gridcell"`, `aria-selected` y `aria-label`.

**Criterios de evaluación:**

- Calendario funcional con toda la navegación y selección (3 puntos)
- Navegación por teclado completa según patrón ARIA Grid (2 puntos)
- Atributos ARIA correctos y compatibilidad con lectores de pantalla (2 puntos)
- Animaciones y diseño visual (2 puntos)
- Código documentado (1 punto)


## Actividades de ampliación

### Actividad de Ampliación 1: Framework de Microinteracciones Reutilizables

**Descripción:** Diseña y desarrolla una pequeña librería o conjunto de clases JavaScript que encapsule las microinteracciones más comunes como componentes reutilizables. La librería debe exponer una API limpia que permita inicializar cualquier microinteracción con una simple llamada, pasando el elemento DOM y un objeto de opciones.

**Requisitos específicos:**

- Implementa al menos 6 microinteracciones como clases independientes: `LikeButton`, `ToggleSwitch`, `Toast`, `Ripple`, `Skeleton`, y `RevealOnScroll`.
- Cada clase debe aceptar un elemento DOM y un objeto de configuración con valores por defecto que puedan sobrescribirse.
- Las microinteracciones deben ser autocontenidas (todo el CSS necesario se inyecta mediante JavaScript si no está ya presente).
- La librería debe incluir una función de inicialización por lotes mediante selectores CSS: `MicroUI.init('.like-btn', LikeButton, { animationDuration: 400 })`.
- Documenta la API con JSDoc.
- Escribe tests unitarios básicos para al menos 3 de las clases.

**Criterios de evaluación:**

- Arquitectura limpia con clases bien diseñadas (3 puntos)
- Funcionalidad completa de las 6 microinteracciones (3 puntos)
- Documentación JSDoc y tests (2 puntos)
- Inicialización por lotes y CSS autocontenido (2 puntos)

### Actividad de Ampliación 2: Dashboard Interactivo con Gráficos y Datos en Tiempo Real

**Descripción:** Construye un panel de control (dashboard) completo que muestre datos simulados con actualizaciones en tiempo real y componentes interactivos sofisticados.

**Requisitos específicos:**

- Diseña el layout con CSS Grid: cabecera, barra lateral colapsable, área principal con tarjetas redimensionables.
- Las tarjetas del dashboard deben ser arrastrables para reorganizarlas (drag and drop en grid).
- Cada tarjeta puede cambiar entre tres tamaños (pequeño, mediano, grande) con transiciones animadas.
- Simula datos en tiempo real que se actualizan cada 2-5 segundos con animación de cambio de valor (flash verde si sube, rojo si baja).
- Implementa al menos 4 tipos de visualización: contador numérico animado, barra de progreso circular SVG animada, gráfico de barras simple con CSS, y lista de eventos con scroll reveal.
- Todos los componentes deben ser accesibles con roles y atributos ARIA apropiados.
- El layout y las preferencias del usuario (tarjetas visibles, orden, tamaño) se persisten en localStorage.

**Criterios de evaluación:**

- Dashboard completo y funcional (3 puntos)
- Drag and drop, redimensionamiento y animaciones fluidas (3 puntos)
- Datos en tiempo real con feedback visual (2 puntos)
- Persistencia de preferencias y accesibilidad (2 puntos)

### Actividad de Ampliación 3: Clon Interactivo de una Funcionalidad de Trello

**Descripción:** Implementa una réplica funcional de la interfaz de tablero de Trello, incluyendo las interacciones más características de este producto.

**Requisitos específicos:**

- **Tablero con columnas desplazables horizontalmente:** Las columnas se organizan con Flexbox en fila y el contenedor tiene `overflow-x: auto` con estilo personalizado de scrollbar.
- **Tarjetas dentro de columnas** que pueden arrastrarse entre columnas (HTML5 Drag and Drop con touch events para móvil).
- **Añadir nuevas tarjetas y columnas** con formularios inline que se expanden al hacer clic (transición de altura).
- **Menú contextual** en cada tarjeta (clic derecho o botón de tres puntos) que muestra opciones con un dropdown animado.
- **Modal de detalle** que se abre al hacer clic en una tarjeta, mostrando descripción, checklist y comentarios simulados.
- **Búsqueda en tiempo real** que filtra tarjetas en todas las columnas simultáneamente, con debounce y resaltado de coincidencias.
- **Atajos de teclado:** `n` para nueva tarjeta, `f` para buscar, `Esc` para cerrar modales, `Ctrl+Z` para deshacer último movimiento (implementa un historial simple de acciones).
- Accesibilidad completa: navegación por teclado entre columnas y tarjetas, roles ARIA (`role="list"`, `role="listitem"`), y regiones live.

**Criterios de evaluación:**

- Interfaz completa con todas las funcionalidades de Trello especificadas (4 puntos)
- Drag and drop funcional en escritorio y táctil (2 puntos)
- Búsqueda, atajos de teclado y sistema de deshacer (2 puntos)
- Accesibilidad y diseño responsive (2 puntos)


## Buenas prácticas

### Planificación y arquitectura

Antes de escribir cualquier línea de código, dedica tiempo a planificar la arquitectura de interactividad de tu sitio o aplicación. Identifica todos los componentes interactivos necesarios, define su comportamiento esperado en cada estado (reposo, hover, focus, activo, carga, error, vacío), y documenta las interacciones de teclado esperadas siguiendo los patrones ARIA Authoring Practices. Una práctica recomendada es crear un "inventario de interacción" en formato tabla con columnas para: componente, trigger, reglas, feedback, teclado y estados.

### Separación de responsabilidades

Mantén una separación clara entre estructura (HTML), presentación (CSS) y comportamiento (JavaScript). Nunca mezcles las tres capas. El HTML debe ser semántico y accesible sin JavaScript ni CSS. El CSS debe encargarse de todas las animaciones y transiciones posibles de forma declarativa. El JavaScript debe usarse solo para lo que CSS no puede hacer: gestionar estado, responder a eventos, actualizar el DOM, y comunicarse con APIs. Evita aplicar estilos inline desde JavaScript; en su lugar, alterna clases CSS que ya tengan definidas las animaciones y transiciones en la hoja de estilos.

### Preferencia por animaciones CSS sobre JavaScript

Siempre que sea posible, prefiere transiciones y animaciones CSS sobre animaciones JavaScript. Las animaciones CSS son optimizadas por el motor de renderizado del navegador, pueden ejecutarse en la GPU en su propia capa de composición, y no bloquean el hilo principal. En particular, prefiere animar siempre las propiedades `transform` y `opacity`, ya que el navegador puede manejarlas completamente en la capa de composición sin disparar reflow ni repaint. Evita animar propiedades que disparen reflow como `width`, `height`, `top`, `left`, `margin`, `padding` o `font-size`. Si necesitas animar dimensiones, considera usar `transform: scale()` como alternativa.

### Accesibilidad desde el diseño inicial

La accesibilidad no es una capa que se añade al final. Debe integrarse desde la fase de diseño y planificación. Cada vez que crees un componente interactivo, pregúntate: ¿funciona sin ratón, usando solo el teclado? ¿Un lector de pantalla puede entender qué es este componente, qué estado tiene y qué acción realiza? ¿El orden de tabulación es lógico? ¿El foco es siempre visible? ¿Los cambios dinámicos se anuncian correctamente? Incorpora estas preguntas en tu checklist mental de desarrollo.

### Gestión del foco

Después de cualquier interacción que cambie el contexto, mueve el foco al lugar esperado. Al abrir un modal, enfoca el primer elemento interactivo dentro de él. Al cerrarlo, devuelve el foco al elemento que lo abrió. Al navegar en una SPA, enfoca el encabezado principal de la nueva vista. Al enviar un formulario con errores, enfoca el primer campo con error. Al mostrar resultados de búsqueda, enfoca el contenedor de resultados. Usa `element.focus()` con `{ preventScroll: false }` para evitar desplazamientos indeseados.

### Optimización del rendimiento

Aplica sistemáticamente las técnicas de optimización aprendidas: debounce para eventos `input` y `resize`, throttle para eventos `scroll` y `mousemove`, `requestAnimationFrame` para animaciones en bucle, Intersection Observer para detección de visibilidad, passive listeners para scroll y touch, y `will-change` aplicado dinámicamente solo durante las animaciones. Monitoriza el rendimiento con las DevTools (pestaña Performance, grabadora de rendimiento, medidor de FPS) para identificar cuellos de botella y verificar que las animaciones se mantienen a 60 fps en dispositivos reales, no solo en el potente ordenador de desarrollo.

### Código limpio y mantenible

Usa nombres descriptivos en español o inglés (según el estándar del equipo) para variables, funciones y clases. Extrae la lógica compleja en funciones con una única responsabilidad. Documenta el código con comentarios que expliquen el "por qué", no el "qué" (el código ya dice qué hace). Agrupa el código relacionado (por ejemplo, toda la lógica de un componente en una IIFE o clase). Usa `'use strict'` al principio de cada script. Prefiere `const` y `let` sobre `var`. Usa arrow functions para callbacks cortos y `function` para funciones con nombre que necesitan su propio `this`.


## Errores frecuentes

### Error 1: Animar propiedades que disparan reflow

Uno de los errores más comunes y perjudiciales para el rendimiento es animar propiedades CSS que fuerzan un recálculo completo del layout. Propiedades como `width`, `height`, `top`, `left`, `right`, `bottom`, `margin`, `padding` y `border-width` disparan reflow cada vez que cambian, lo que implica que el navegador debe recalcular las posiciones y dimensiones de todos los elementos afectados. En su lugar, utiliza `transform: scale()`, `transform: translate()`, `transform: rotate()` y `opacity`, que solo afectan a la capa de composición y la GPU puede manejarlas de forma independiente sin involucrar al CPU en el reflow.

**Solución:** Sustituye `width`/`height` por `transform: scale()`. Sustituye `top`/`left` por `transform: translate()`. Si necesitas animar una altura, considera la técnica `max-height` con un valor suficientemente grande (aunque no es perfecta, es mejor que animar `height`).

### Error 2: No gestionar el foco en componentes dinámicos

Cuando se abre un modal, se muestran resultados de búsqueda, o se navega en una SPA, muchos desarrolladores olvidan mover el foco al lugar adecuado. El resultado es que el foco se pierde (queda en el `body` o en un elemento invisible), y el usuario de teclado debe navegar desde el principio para encontrar el contenido. En el caso de modales sin focus trapping, el usuario puede seguir navegando por la página que está detrás del modal sin ser consciente de ello.

**Solución:** Implementa una función de gestión de foco en cada componente interactivo. Al abrir: `elementoDestino.focus()`. Al cerrar: `elementoOrigen.focus()`. En modales, implementa focus trapping con detección de Tab y Shift+Tab.

### Error 3: Usar click en lugar de input para validación en tiempo real

Usar el evento `click` o `change` para validar formularios proporciona una experiencia pobre, ya que el usuario no recibe retroalimentación hasta que abandona el campo. Por otro lado, usar `input` sin debounce para validaciones que implican peticiones al servidor (como comprobar disponibilidad de nombre de usuario) puede saturar el backend.

**Solución:** Usa `input` con debounce (300 ms) para validaciones en tiempo real. Combínalo con `blur` para una validación inmediata al abandonar el campo. Para validaciones pesadas (peticiones al servidor), usa un debounce más largo (500-800 ms).

### Error 4: Ignorar la navegación por teclado

Muchos componentes interactivos (dropdowns, tooltips, carruseles, tabs) se implementan pensando exclusivamente en el ratón. Los eventos se limitan a `click`, `mouseenter` y `mouseleave`, ignorando completamente a los usuarios que navegan con teclado.

**Solución:** Para cada componente interactivo, consulta los patrones de diseño ARIA Authoring Practices e implementa las interacciones de teclado especificadas: flechas para navegar entre opciones, Enter/Espacio para activar, Escape para cerrar/descartar, Tab para entrar y salir del componente.

### Error 5: No limpiar event listeners y temporizadores

Al eliminar elementos del DOM que tenían listeners o temporizadores activos, estos quedan huérfanos y pueden causar memory leaks (fugas de memoria) o comportamientos inesperados (un temporizador que intenta actualizar un elemento que ya no existe).

**Solución:** Siempre limpia los recursos al destruir un componente. Usa `clearTimeout`/`clearInterval` para cancelar temporizadores. Usa `removeEventListener` para desconectar listeners, especialmente los de `document` o `window`. Considera usar la opción `{ once: true }` para listeners que solo necesitan ejecutarse una vez. Usa `AbortController` (con `signal`) para eliminar grupos de listeners de una sola vez.

### Error 6: Delegación de eventos sin verificar event.target

Al implementar event delegation, un error común es asumir que `event.target` es exactamente el elemento hijo esperado, sin considerar que podría ser un elemento anidado más profundo. Por ejemplo, en una lista de tarjetas con botones, `event.target` podría ser el texto del botón, el icono SVG dentro del botón, o el botón mismo.

**Solución:** Usa `event.target.closest(selector)` en lugar de `event.target` directamente. El método `closest()` recorre los ancestros del elemento hasta encontrar uno que coincida con el selector, garantizando que obtienes el elemento contenedor correcto sin importar en qué hijo hizo clic el usuario.

### Error 7: Anidar temporizadores para animaciones secuenciales

Para crear animaciones secuenciales (primero fade out, luego cambiar contenido, luego fade in), muchos desarrolladores anidan `setTimeout`, lo que produce código difícil de leer, mantener y depurar (callback hell).

**Solución:** Utiliza el evento `transitionend` o `animationend` para encadenar animaciones de forma declarativa. Alternativamente, utiliza promesas con `async/await` para expresar secuencias de forma lineal: `await fadeOut(elemento); cambiarContenido(); await fadeIn(elemento)`. La Web Animations API también proporciona la promesa `.finished` para este propósito.

### Error 8: No considerar el estado de carga y error

Muchos componentes interactivos se implementan asumiendo que todo funcionará correctamente. No se contempla qué mostrar mientras los datos se cargan, ni qué hacer si la carga falla.

**Solución:** Todo componente que dependa de datos asíncronos debe implementar al menos tres estados: cargando (skeleton screen o spinner), éxito (contenido), y error (mensaje descriptivo con opción de reintentar). Si el componente puede estar vacío legítimamente (lista sin elementos), implementa también un estado vacío con un mensaje orientativo y una llamada a la acción.

### Error 9: Abusar de will-change

Aplicar `will-change: transform, opacity` a docenas de elementos en la hoja de estilos, pensando que esto mejorará el rendimiento, es contraproducente. Cada elemento con `will-change` activo consume memoria de GPU para mantener su propia capa de composición, incluso si nunca llega a animarse.

**Solución:** Aplica `will-change` solo a los elementos que van a animarse, solo durante el período en que la animación está activa, y solo para las propiedades que realmente van a cambiar. Añádelo dinámicamente en el evento que inicia la animación (como `mouseenter`) y elimínalo cuando la animación termina (`transitionend`, `animationend`, `mouseleave`).

### Error 10: Validación solo en el cliente

Implementar validación exclusivamente en el lado del cliente (JavaScript) y confiar en que el servidor recibirá datos válidos es un grave error de seguridad. La validación del cliente es una conveniencia para el usuario, no una medida de seguridad, ya que cualquier usuario puede desactivar JavaScript o manipular las peticiones HTTP.

**Solución:** Implementa siempre validación en ambos lados. La validación del cliente (JavaScript, atributos HTML como `required`, `pattern`, `minlength`) proporciona retroalimentación inmediata y mejora la UX. La validación del servidor (obligatoria) garantiza la integridad y seguridad de los datos recibidos, independientemente de lo que ocurra en el cliente.

### Error 11: Usar innerHTML en lugar de textContent para texto de usuario

Usar `innerHTML` para insertar en el DOM texto que proviene de entradas del usuario puede crear vulnerabilidades de Cross-Site Scripting (XSS), permitiendo que un atacante inyecte código HTML o JavaScript malicioso.

**Solución:** Usa `textContent` (o `innerText`) para insertar texto plano en el DOM. Si necesitas insertar HTML, sanitízalo primero con una librería como DOMPurify. Nunca confíes en datos provenientes del usuario, de la URL (query strings) o de APIs externas sin sanitización.


## Resumen

La interactividad web constituye uno de los pilares fundamentales del desarrollo front-end moderno y esta unidad ha proporcionado al alumnado las herramientas conceptuales y prácticas necesarias para abordarla con rigor profesional. Hemos establecido una distinción clara entre animación pasiva e interactividad genuina, comprendiendo que la segunda implica un diálogo bidireccional usuario-sistema que se construye sobre cinco funciones esenciales: retroalimentación inmediata, guía de la atención, reducción de la carga cognitiva, aumento de la percepción de velocidad y generación de satisfacción emocional.

El estudio en profundidad de los eventos JavaScript —desde los fundamentos (fases de captura, objetivo y burbujeo) hasta técnicas avanzadas como la delegación de eventos y las opciones `{ once, passive, capture }`— ha dotado al alumnado de la base técnica necesaria para detectar y responder a cualquier acción del usuario, ya sea mediante ratón, teclado, pantalla táctil o cualquier otro dispositivo de entrada. Se ha hecho especial énfasis en la importancia de elegir el evento adecuado para cada situación (`input` para validación en tiempo real, `change` para acciones costosas, `keydown` para atajos de teclado) y en la necesidad de utilizar passive listeners para garantizar un scroll fluido en dispositivos móviles.

El concepto de microinteracción, articulado a través del modelo de Dan Saffer (trigger, rules, feedback, loops/modes), ha proporcionado un marco conceptual para diseñar y analizar los pequeños momentos que marcan la diferencia entre un producto funcional y uno memorable. Hemos implementado microinteracciones paradigmáticas —botón de like con latido, toggle switch, toasts, ripple, skeleton screens, swipe gestures— comprendiendo cómo cada una aborda los cuatro elementos del modelo.

La comparación sistemática entre transiciones CSS, animaciones `@keyframes` y la Web Animations API ha establecido criterios claros de decisión: transiciones para cambios simples de estado, keyframes para animaciones complejas declarativas, y WAAPI para control programático. Se ha insistido en la importancia de animar exclusivamente las propiedades `transform` y `opacity` para garantizar el rendimiento, evitando propiedades que disparen reflow.

Los diez componentes dinámicos completos (like button, toggle switch, toast, modal, acordeón FAQ, tabs, carrusel, galería lightbox, dark mode toggle, scroll reveal y drag and drop) han proporcionado implementaciones de referencia que el alumnado puede consultar, modificar y reutilizar en sus proyectos. Todos ellos comparten un denominador común: accesibilidad integrada desde el diseño, con gestión del foco, navegación por teclado, roles y atributos ARIA, y regiones aria-live.

El bloque de rendimiento ha cubierto las técnicas esenciales para mantener animaciones fluidas a 60 fps: debounce y throttle para eventos de alta frecuencia, `requestAnimationFrame` para bucles de animación, separación de lecturas y escrituras del DOM para evitar layout thrashing, `will-change` aplicado con criterio, Intersection Observer para detección eficiente de visibilidad, y passive listeners para optimizar el scroll.

Los tres casos reales analizados —Twitter, Notion y Linear— han mostrado cómo empresas líderes aplican estos mismos principios y técnicas en productos utilizados por millones de personas, demostrando que la teoría aprendida en la unidad tiene una aplicación directa e inmediata en la industria.

Finalmente, las buenas prácticas y los errores frecuentes han sintetizado la experiencia acumulada en el desarrollo de interfaces interactivas, proporcionando al alumnado una guía para evitar los tropiezos más comunes y adoptar hábitos de desarrollo profesional desde el primer día.

## Recursos complementarios

### Documentación oficial y estándares

- **MDN Web Docs - Eventos:** La documentación de referencia sobre todos los tipos de eventos en la web, incluyendo compatibilidad entre navegadores, ejemplos de uso y buenas prácticas. URL: https://developer.mozilla.org/es/docs/Web/Events
- **MDN Web Docs - Web Animations API:** Guía completa sobre la API de animaciones web con ejemplos progresivos. URL: https://developer.mozilla.org/en-US/docs/Web/API/Web_Animations_API
- **W3C ARIA Authoring Practices:** Patrones de diseño oficiales para componentes accesibles con ejemplos de teclado y atributos ARIA. URL: https://www.w3.org/WAI/ARIA/apg/patterns/
- **WCAG 2.1 - Quick Reference:** Referencia rápida de criterios de conformidad de accesibilidad. URL: https://www.w3.org/WAI/WCAG21/quickref/

### Libros recomendados

- **"Microinteractions: Designing with Details"** de Dan Saffer (O'Reilly, 2013). El libro fundacional sobre microinteracciones. Imprescindible para comprender la filosofía y la práctica del diseño de detalles interactivos.
- **"Web Animation using JavaScript: Develop & Design"** de Julian Shapiro (Peachpit Press, 2015). Cubre técnicas de animación con JavaScript, incluyendo requestAnimationFrame, la API Web Animations y librerías como Velocity.js, con un fuerte enfoque en rendimiento.
- **"Inclusive Components"** de Heydon Pickering (Smashing Magazine, 2019). Aborda el diseño y desarrollo de componentes web accesibles con ejemplos prácticos y detallados de implementación.
- **"High Performance Web Sites"** y **"Even Faster Web Sites"** de Steve Souders (O'Reilly). Clásicos sobre rendimiento web que todo desarrollador front-end debería leer.
- **"Refactoring UI"** de Adam Wathan y Steve Schoger. Aunque más orientado al diseño visual, contiene principios excelentes sobre jerarquía visual y diseño de interacción.

### Herramientas y extensiones

- **axe DevTools (Deque):** Extensión de navegador para auditorías automáticas de accesibilidad. URL: https://www.deque.com/axe/
- **WAVE (WebAIM):** Herramienta de evaluación de accesibilidad visual que superpone iconos sobre la página. URL: https://wave.webaim.org/
- **Lighthouse (Google):** Herramienta integrada en Chrome DevTools para auditar rendimiento, accesibilidad, buenas prácticas y SEO.
- **Responsively App:** Aplicación de escritorio gratuita para previsualizar sitios web en múltiples dispositivos simultáneamente, ideal para probar interactividad responsive.

### Artículos y blogs

- **"Debouncing and Throttling Explained Through Examples"** por David Corbacho (CSS-Tricks). Una de las mejores explicaciones visuales sobre debounce y throttle.
- **"Smooth as Butter: Achieving 60 FPS Animations with CSS3"** por José M. Pérez. Artículo profundo sobre el pipeline de renderizado y cómo optimizar animaciones CSS.
- **"A Complete Guide to Flexbox"** y **"A Complete Guide to Grid"** en CSS-Tricks. Referencias visuales completas sobre Flexbox y CSS Grid.
- **Blog de Smashing Magazine:** Publica regularmente artículos de alta calidad sobre desarrollo front-end, accesibilidad y diseño de interacción.

### Cursos y formación complementaria

- **"JavaScript: The Hard Parts"** de Will Sentance (Frontend Masters). Curso avanzado que profundiza en el event loop, closures, y el modelo de ejecución de JavaScript.
- **"Web Accessibility"** de Google (Udacity). Curso gratuito sobre fundamentos de accesibilidad web.
- **"Frontend Masters"** - Varios cursos sobre animaciones web, rendimiento y accesibilidad impartidos por profesionales de la industria.
