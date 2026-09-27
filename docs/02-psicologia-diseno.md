# Unidad 2: Psicología Cognitiva Aplicada al Diseño de Interfaces

## Objetivos de aprendizaje

Al finalizar esta unidad, el alumnado será capaz de:

1. Aplicar los principios de jerarquía visual, contraste, proximidad, repetición, alineación y balance al diseño de interfaces web, justificando cada decisión con fundamentos psicológicos y perceptivos.
2. Comprender y aplicar las leyes psicológicas que rigen la interacción persona-ordenador (Hick, Fitts, efecto de posición serial, carga cognitiva) al diseño de menús, botones, formularios y arquitectura de información.
3. Analizar interfaces web reales (Spotify, Notion, GitHub, Twitter) identificando qué principios y leyes se aplican y evaluando su impacto en la experiencia de usuario.
4. Construir diseños de interfaz que minimicen la carga cognitiva, faciliten la toma de decisiones y reduzcan la fricción en la interacción.
5. Seleccionar y aplicar patrones de diseño justificados mediante leyes psicológicas y principios perceptivos.
6. Evaluar críticamente la consistencia interna y externa de una interfaz, proponiendo mejoras basadas en principios psicológicos.

## Relación con los Resultados de Aprendizaje

- **RA1. Planifica la creación de una interfaz web valorando y aplicando especificaciones de diseño.** La comprensión de las leyes psicológicas (Hick, Fitts, carga cognitiva) permite al alumnado planificar estructuras de navegación y disposición de elementos que anticipen el comportamiento del usuario, reduciendo iteraciones de rediseño.
- **RA2. Crea interfaces web homogéneos definiendo y aplicando estilos.** Los principios de jerarquía, contraste, repetición, alineación y consistencia son las herramientas fundamentales para crear interfaces cohesivas donde todos los elementos responden a un mismo sistema visual.
- **RA5. Desarrolla interfaces web accesibles, analizando las pautas establecidas y aplicando técnicas de verificación.** La aplicación de la ley de Fitts (tamaño de zonas interactivas), el contraste mínimo y la reducción de carga cognitiva son directamente relevantes para la accesibilidad cognitiva y motriz.
- **RA6. Desarrolla interfaces web amigables analizando y aplicando las pautas de usabilidad establecidas.** La minimización de la carga cognitiva y el diseño de flujos predecibles mejoran la facilidad de uso y la satisfacción del usuario, núcleo de la usabilidad.

## Conocimientos previos

1. **Conceptos básicos de diseño visual:** Principios de la Gestalt estudiados en la Unidad 1 (proximidad, semejanza, continuidad, cierre, figura-fondo).
2. **Fundamentos de CSS:** Selectores, modelo de caja, unidades de medida, media queries, Flexbox y Grid en nivel básico.
3. **Competencias digitales:** Manejo de las DevTools del navegador para inspeccionar y modificar estilos en tiempo real.
4. **Actitud analítica:** Disposición a observar críticamente las interfaces que se utilizan a diario y preguntarse por qué funcionan (o por qué no).

## Contenidos

### 1. Jerarquía visual
- Definición y propósito en el diseño de interfaces
- Técnicas para establecer jerarquía: tamaño, color, posición, contraste, espacio en blanco, repetición
- Patrones de escaneo visual: patrón en F y patrón en Z
- Aplicación práctica: diseño de páginas de contenido denso

### 2. Contraste
- Tipos de contraste: color, tamaño, forma, tipografía
- Relación de contraste mínima según WCAG 2.1 (AA: 4.5:1, AAA: 7:1)
- Herramientas de verificación de contraste
- El contraste como herramienta de jerarquía y accesibilidad

### 3. Proximidad
- Principio de agrupación: espaciado entre elementos
- Creación de relaciones visuales mediante la distancia
- Espaciado consistente como parte del sistema de diseño
- El espacio en blanco como elemento activo de diseño

### 4. Repetición
- Consistencia visual mediante repetición de patrones
- Patrones de diseño y sistemas de diseño
- Componentes reutilizables: botones, tarjetas, formularios
- Variación controlada dentro de la repetición

### 5. Alineación
- Tipos de alineación: izquierda, derecha, centro, justificada
- Uso de cuadrículas (grids) en diseño web
- Líneas invisibles y guías visuales
- Alineación y legibilidad del texto

### 6. Balance
- Balance simétrico vs asimétrico
- Balance radial y su aplicación en diseño web
- Peso visual de los elementos: factores que influyen
- Distribución de elementos para crear equilibrio

### 7. Consistencia
- Consistencia interna vs consistencia externa
- Componentes reutilizables y predictibilidad
- El valor de la familiaridad en la experiencia de usuario
- Sistemas de diseño como herramienta de consistencia

### 8. Ley de Hick
- Relación entre número de opciones y tiempo de decisión
- Aplicación al diseño de menús y navegación
- Simplificación progresiva: chunking y categorización

### 9. Ley de Fitts
- Relación entre tamaño, distancia y tiempo de adquisición de objetivos
- Aplicación al diseño de botones y zonas de interacción
- Implicaciones para el diseño mobile y touch

### 10. Efecto de posición serial
- Efecto de primacía y efecto de recencia
- Aplicación a listas, menús y barras de navegación
- Organización de contenido para maximizar el recuerdo

### 11. Carga cognitiva
- Teoría de la carga cognitiva aplicada a interfaces
- Simplificación de formularios y procesos
- Estrategias para reducir la carga cognitiva en la web

## Desarrollo teórico

### 1. Jerarquía visual

!!! info "Definición"
    La **jerarquía visual** es el principio de diseño que organiza los elementos de una interfaz **por orden de importancia**, de manera que la persona usuaria pueda identificar instantáneamente qué es lo más relevante, dónde debe mirar primero y qué acciones tiene disponibles. Es la herramienta fundamental para guiar la atención de forma predecible y eficiente, asegurando que la información más crítica sea percibida primero.

Las técnicas para establecer jerarquía visual son múltiples y deben usarse de forma combinada:

- **Tamaño** — el indicador más poderoso: los elementos más grandes se perciben como más importantes.
- **Color** — el contraste cromático atrae la atención: los colores vibrantes y saturados destacan frente a los neutros y desaturados.
- **Posición** — depende de los patrones culturales de lectura; en culturas occidentales, la **esquina superior izquierda** tiene la máxima jerarquía posicional.
- **Espacio en blanco** — un elemento rodeado de abundante espacio negativo adquiere importancia.

Los **patrones de escaneo visual** describen la trayectoria típica que sigue la mirada al examinar una página web:

- **Patrón en F** — identificado por el Nielsen Norman Group mediante *eye-tracking*; es el más común para páginas de contenido textual. La persona usuaria lee la primera línea horizontalmente (el titular), luego desciende y lee otra línea horizontal más corta, y finalmente desciende por el margen izquierdo escaneando verticalmente.
- **Patrón en Z** — característico de las *landing pages*: la mirada recorre la página desde la esquina superior izquierda a la derecha, desciende en diagonal y termina en la esquina inferior derecha.

!!! tip "Implicación práctica"
    - En el patrón **F**: la información más importante debe situarse en las **dos primeras líneas**.
    - En el patrón **Z**: el botón de llamada a la acción debe colocarse en la **esquina inferior derecha**.

### 2. Contraste

!!! info "Definición"
    El **contraste** es la diferencia perceptible entre dos o más elementos visuales. Sin contraste, una interfaz es visualmente plana, monótona y difícil de navegar. Además, es un **requisito fundamental de accesibilidad**: las personas con baja visión, cataratas, daltonismo o fatiga visual necesitan suficiente contraste para distinguir el texto del fondo y los elementos interactivos de los decorativos.

Los tipos de contraste que podemos manipular en diseño web son:

- **Color** — medido mediante la relación de luminancia entre dos colores.
- **Tamaño** — elementos grandes frente a pequeños.
- **Forma** — elementos orgánicos frente a geométricos.
- **Tipografía** — *serif* frente a *sans-serif*, **bold** frente a *light*.

Según las **[WCAG 2.1](https://es.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines)**, los ratios mínimos de contraste son:

| Nivel | Texto normal | Texto grande (≥18px o ≥14px en negrita) |
|-------|--------------|------------------------------------------|
| **AA** | **4.5:1** | **3:1** |
| **AAA** | **7:1** | **4.5:1** |

Las herramientas de verificación de contraste son fundamentales en el flujo de trabajo:

- **WebAIM Contrast Checker** — introduce códigos de color y devuelve el ratio.
- **Stark** — plugin para Figma, Sketch y Adobe XD que verifica el contraste directamente en los mockups.
- **Panel de Accesibilidad de Chrome DevTools** — muestra el ratio de cualquier elemento seleccionado.

### 3. Proximidad

!!! info "Definición"
    El principio de **proximidad**, heredado de las leyes de la Gestalt, establece que los elementos que están **físicamente cerca** unos de otros tienden a percibirse como un grupo relacionado. Es una de las herramientas más potentes del diseño de interfaces, ya que permite comunicar relaciones entre elementos sin bordes, fondos de color, iconos ni texto explicativo.

!!! tip "Regla fundamental"
    El espacio **dentro** de un grupo debe ser **menor** que el espacio **entre** grupos distintos. En un formulario, la etiqueta «Nombre» debe estar más cerca de su campo de texto que del campo «Email» que le precede; si se invierte, la persona usuaria puede asociar la etiqueta al campo equivocado.

El **espacio en blanco** no es un lujo, es una necesidad funcional: agrupa, separa, jerarquiza y da respiro visual. La implementación técnica en CSS se basa en una **escala de espaciado consistente** con una unidad base (por ejemplo, **8px**) utilizando exclusivamente múltiplos de ella.

### 4. Repetición

!!! info "Definición"
    El principio de **repetición** establece que la consistencia en los elementos visuales (colores, tipografías, formas, espaciados, estilos de iconos) crea una sensación de **unidad** que facilita la navegación y reduce la carga cognitiva: quien aprende que todos los botones de acción primaria son azules, que todos los enlaces están subrayados o que todas las tarjetas tienen la misma estructura puede aplicar ese conocimiento a cada pantalla nueva sin tener que reaprenderlo.

La repetición es el fundamento de los **sistemas de diseño** (*design systems*): catálogos de patrones visuales repetibles que garantizan la consistencia de la interfaz. **Google** (Material Design), **IBM** (Carbon), **Atlassian** y **Shopify** han desarrollado sistemas de diseño exhaustivos. A escala más modesta, cualquier proyecto debería disponer de un conjunto básico de patrones repetibles: estilos de botones, de tarjetas y de formularios, paleta y escala tipográfica.

!!! tip "Variación controlada"
    La repetición **no implica monotonía**. Introducir diferencias sutiles dentro de un patrón hace que una interfaz sea interesante sin dejar de ser coherente.

### 5. Alineación

!!! info "Definición"
    La **alineación** establece que ningún elemento debe colocarse de forma arbitraria. Cada elemento debe tener una conexión visual con al menos otro elemento, creando **líneas invisibles** que guían la mirada y transmiten orden y profesionalidad.

Tipos de alineación:

- **Izquierda** — la más natural para textos en lenguas occidentales; crea un borde limpio para anclar la mirada.
- **Centro** — adecuada para titulares y mensajes cortos, pero dificulta la legibilidad en textos largos.
- **Derecha** — usada para datos numéricos en tablas y para crear tensión visual asimétrica.
- **Justificada** — crea bloques de texto con bordes rectos a ambos lados, pero puede generar espaciados irregulares entre palabras.

Las cuadrículas **CSS Grid** son la herramienta fundamental para implementar alineación en diseño web.

### 6. Balance

!!! info "Definición"
    El **balance** o equilibrio visual es la distribución del peso visual de los elementos en la composición. Cada elemento tiene un peso visual determinado por su **tamaño, color, posición, complejidad y aislamiento**.

- **Balance simétrico** — transmite estabilidad y formalidad.
- **Balance asimétrico** — transmite dinamismo y creatividad.
- **Balance radial** — organiza los elementos en torno a un punto central; en la web se aplica puntualmente en portadas y elementos destacados.

La elección entre ambos debe alinearse con la **personalidad de la marca** y las expectativas de la audiencia objetivo.

### 7. Consistencia

!!! info "Definición"
    La **consistencia** garantiza que elementos similares se comporten y se muestren de manera similar en toda la interfaz. Es el **principio más importante desde el punto de vista de la UX**, porque permite transferir el aprendizaje entre pantallas.

- **Consistencia interna** — coherencia dentro del mismo producto.
- **Consistencia externa** — coherencia con las convenciones del resto de productos que la persona usuaria utiliza.

### 8. Ley de Hick

La **ley de Hick** establece que el tiempo para tomar una decisión aumenta logarítmicamente con el número de opciones:

> **T = b × log2(n + 1)**

En diseño de interfaces, cada opción adicional en un menú incrementa el tiempo de procesamiento. La solución es la **categorización jerárquica**: organizar **15 enlaces** en **4 categorías de 3-4 enlaces** cada una, de modo que la decisión se tome en **dos pasos más simples** en lugar de uno complejo. La **divulgación progresiva** —mostrar inicialmente solo las opciones más utilizadas— es otra estrategia eficaz.

### 9. Ley de Fitts

La **ley de Fitts** establece que el tiempo para alcanzar un objetivo depende de la distancia y del tamaño:

> **T = a + b × log2(2D / W + 1)**

Los objetivos de interacción deben ser **grandes y cercanos**. Las guías oficiales son explícitas:

- **Apple:** mínimo **44×44 puntos** para zonas interactivas en iOS.
- **Google:** mínimo **48×48 dp** en Material Design.

En mobile, las acciones frecuentes deben situarse en las **zonas de fácil alcance para el pulgar** (mitad inferior central).

### 10. Efecto de posición serial

El **efecto de posición serial** describe cómo la posición en una secuencia afecta a la probabilidad de recuerdo:

- **Efecto de primacía** — los primeros elementos se recuerdan mejor.
- **Efecto de recencia** — los últimos también.
- **Zona intermedia** — los elementos centrales son los peor recordados.

En diseño web, esto implica colocar los elementos **más importantes al principio** de menús y listas, y aprovechar tanto la primacía como la recencia para ubicar estratégicamente **llamadas a la acción** y contenido promocionado.

### 11. Carga cognitiva

!!! info "Definición"
    La **teoría de la carga cognitiva** establece que la memoria de trabajo humana tiene una capacidad limitada: **7 ± 2 elementos**. En diseño de interfaces, cada elemento que la persona usuaria debe percibir, recordar o procesar consume recursos de esa memoria limitada.

Estrategias para reducir la carga cognitiva:

- **Agrupar** la información (*chunking*).
- **Dividir** procesos complejos en pasos secuenciales.
- **Eliminar** información irrelevante.
- **Reconocer** en lugar de recordar.
- **Utilizar** convenciones familiares.
- **Proporcionar** retroalimentación inmediata.

En formularios, cada campo adicional incrementa la carga de forma **no lineal**, por lo que reducir el número de campos visibles tiene un impacto desproporcionadamente positivo en la tasa de finalización.


## Ejemplos guiados

### Ejemplo 1: Patrón de escaneo en F implementado en una página de blog

!!! example "Contexto pedagógico"
    Este ejemplo implementa una página de blog diseñada para aprovechar el patrón de escaneo en **F**, colocando estratégicamente la información clave en las zonas donde el ojo se detiene según los estudios de *eye-tracking* del Nielsen Norman Group.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Patrón de escaneo en F</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }

    body {
      font-family: Georgia, serif;
      background: #fafafa;
      color: #333;
      line-height: 1.7;
    }

    .contenedor {
      max-width: 720px;
      margin: 0 auto;
      padding: 3rem 1.5rem;
    }

    /*
     * PRIMERA LÍNEA HORIZONTAL DEL PATRÓN F: EL TÍTULO
     * El ojo recorre esta línea completamente.
     * Por eso el título debe ser impactante y ocupar toda la anchura.
     */
    h1 {
      font-size: 2.2rem;
      font-weight: 800;
      color: #111;
      line-height: 1.2;
      margin-bottom: 0.75rem;
      letter-spacing: -0.3px;
    }

    /*
     * SEGUNDA LÍNEA HORIZONTAL DEL PATRÓN F: METADATOS Y ENTRADILLA
     * El ojo recorre esta línea pero con menor amplitud.
     * Aquí va la información contextual que ayuda a decidir si seguir leyendo.
     */
    .metadatos {
      font-family: 'Segoe UI', sans-serif;
      font-size: 0.8rem;
      color: #999;
      text-transform: uppercase;
      letter-spacing: 1px;
      margin-bottom: 1.5rem;
    }

    .entradilla {
      font-size: 1.2rem;
      color: #555;
      font-style: italic;
      margin-bottom: 2rem;
      padding-bottom: 1.5rem;
      border-bottom: 1px solid #e0e0e0;
    }

    /*
     * BARRIDO VERTICAL DEL PATRÓN F: MARGEN IZQUIERDO
     * El ojo desciende por el margen izquierdo escaneando
     * las primeras palabras de cada párrafo.
     * Por eso los subtítulos y las primeras palabras de cada
     * párrafo deben contener información relevante.
     */
    h2 {
      font-family: 'Segoe UI', sans-serif;
      font-size: 1.35rem;
      font-weight: 700;
      color: #1a1a2e;
      margin-top: 2rem;
      margin-bottom: 0.75rem;
    }

    p {
      font-size: 1.05rem;
      margin-bottom: 1.25rem;
    }

    /*
     * CITA DESTACADA: Ruptura del patrón F para capturar atención
     * El borde lateral y el fondo diferente interrumpen el flujo
     * y hacen que la mirada se detenga.
     */
    blockquote {
      border-left: 4px solid #667eea;
      margin: 2rem 0;
      padding: 1rem 1.5rem;
      background: #f0f4ff;
      font-style: italic;
      color: #2d3250;
      font-size: 1.1rem;
    }

    /*
     * LISTA: Los bullet points son escaneados eficientemente
     * porque crean puntos de anclaje vertical para la mirada.
     */
    ul {
      margin: 1rem 0 1.5rem 1.5rem;
    }

    li {
      margin-bottom: 0.5rem;
      font-size: 1.05rem;
    }

    li::marker {
      color: #667eea;
    }
  </style>
</head>
<body>
  <div class="contenedor">
    <!-- PRIMERA LÍNEA F: Título completo, el ojo lo lee entero -->
    <h1>Cómo los principios psicológicos transforman el diseño de interfaces web modernas</h1>

    <!-- SEGUNDA LÍNEA F: Metadatos y entradilla -->
    <p class="metadatos">María García — 12 minutos de lectura — Psicología del Diseño</p>
    <p class="entradilla">
      La aplicación de leyes como Hick, Fitts y los principios de la Gestalt
      permite construir interfaces que las personas comprenden de forma intuitiva,
      reduciendo la fricción y aumentando la satisfacción de uso.
    </p>

    <!-- BARRIDO VERTICAL: El ojo desciende por la izquierda -->
    <!-- Observa que las primeras palabras de cada párrafo contienen
         la información esencial que alguien que escanea retendrá -->
    <p>
      <strong>Las leyes psicológicas</strong> que gobiernan la percepción humana no son
      un lujo académico, sino herramientas prácticas que todo diseñador de interfaces
      debería dominar. Comprender por qué ciertas disposiciones funcionan y otras
      generan confusión permite tomar decisiones basadas en evidencia.
    </p>

    <p>
      <strong>La ley de Hick</strong> nos enseña que cada opción adicional en un menú
      incrementa el tiempo de decisión del usuario. La solución no es eliminar opciones,
      sino categorizarlas jerárquicamente para reducir la carga cognitiva.
    </p>

    <h2>La ley de Fitts y el tamaño de los botones</h2>

    <p>
      <strong>Paul Fitts demostró</strong> en 1954 que el tiempo para alcanzar un objetivo
      depende de su tamaño y su distancia. Un botón pequeño en una esquina remota es
      difícil de pulsar; un botón grande y cercano es inmediato.
    </p>

    <blockquote>
      "El diseño no es solo cómo se ve o cómo se siente. El diseño es cómo funciona."
      — Steve Jobs
    </blockquote>

    <p>
      <strong>La carga cognitiva</strong> es el enemigo silencioso de la usabilidad.
      Cada elemento innecesario en una interfaz consume recursos de la limitada
      memoria de trabajo del usuario, aumentando la probabilidad de error y abandono.
    </p>

    <h2>Estrategias para reducir la carga cognitiva</h2>

    <ul>
      <li><strong>Fragmentar</strong> la información en unidades manejables (chunking)</li>
      <li><strong>Utilizar</strong> convenciones familiares en lugar de patrones novedosos</li>
      <li><strong>Mostrar</strong> opciones en lugar de obligar a recordarlas</li>
      <li><strong>Proporcionar</strong> retroalimentación inmediata a cada acción</li>
      <li><strong>Dividir</strong> procesos complejos en pasos secuenciales simples</li>
    </ul>

    <p>
      <strong>La conclusión</strong> es clara: el mejor diseño de interfaz no es el más
      original ni el más llamativo, sino aquel que la persona usuaria puede utilizar
      sin esfuerzo consciente, casi sin darse cuenta de que la interfaz está ahí.
    </p>
  </div>
</body>
</html>
```

!!! note "Explicación del resultado"
    Al visualizar esta página, la mirada sigue naturalmente el patrón en **F**. Primero recorre el título completo de izquierda a derecha. Luego desciende ligeramente y recorre los metadatos y la entradilla. Finalmente desciende por el margen izquierdo, deteniéndose en las palabras en negrita al inicio de cada párrafo y en los subtítulos. Se recomienda al alumnado leer la página con atención y luego intentar escanearla en **5 segundos**, anotando qué información retienen; comprobarán que coincide con los elementos situados en las zonas del patrón F.

---

### Ejemplo 2: Aplicación de la Ley de Hick en navegación categorizada

!!! example "Contexto pedagógico"
    Comparativa visual y matemática entre un menú con **12 opciones planas** y el mismo contenido organizado jerárquicamente, demostrando que la categorización reduce el tiempo de decisión según la fórmula de Hick.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ley de Hick - Navegación</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      background: #f5f5f5;
      padding: 2rem;
    }
    h1 {
      color: #1a202c;
      margin-bottom: 2rem;
      text-align: center;
    }
    .comparativa {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
      gap: 2rem;
      max-width: 1100px;
      margin: 0 auto;
    }
    .demo {
      background: white;
      border-radius: 12px;
      padding: 2rem;
      box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    }
    .demo h2 {
      font-size: 1.1rem;
      color: #2d3748;
      margin-bottom: 1.5rem;
      padding-bottom: 0.75rem;
      border-bottom: 2px solid #e2e8f0;
    }

    /* Versión A: 12 opciones planas - viola ley de Hick */
    .mal-diseno nav {
      display: flex;
      gap: 0.75rem;
      flex-wrap: wrap;
    }
    .mal-diseno nav a {
      padding: 0.5rem 1rem;
      background: #edf2f7;
      color: #4a5568;
      text-decoration: none;
      border-radius: 6px;
      font-size: 0.85rem;
      transition: background 0.2s;
    }
    .mal-diseno nav a:hover {
      background: #e2e8f0;
    }

    /* Versión B: 4 categorías de 3 enlaces - aplica ley de Hick */
    .buen-diseno nav {
      display: flex;
      gap: 2.5rem;
    }
    .buen-diseno .categoria {
      display: flex;
      flex-direction: column;
      gap: 0.35rem;
    }
    .buen-diseno .categoria-titulo {
      font-weight: 700;
      color: #1a202c;
      font-size: 0.8rem;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 0.5rem;
    }
    .buen-diseno .categoria a {
      padding: 0.35rem 0;
      color: #667eea;
      text-decoration: none;
      font-size: 0.9rem;
      transition: color 0.2s;
    }
    .buen-diseno .categoria a:hover {
      color: #5a67d8;
      text-decoration: underline;
    }

    .info-box {
      margin-top: 1.5rem;
      padding: 1rem;
      border-radius: 8px;
      font-size: 0.85rem;
    }
    .info-box.warning {
      background: #fff5f5;
      border-left: 4px solid #fc8181;
      color: #9b2c2c;
    }
    .info-box.success {
      background: #f0fff4;
      border-left: 4px solid #48bb78;
      color: #22543d;
    }
    .formula {
      font-family: 'Courier New', monospace;
      font-weight: 700;
    }
  </style>
</head>
<body>
  <h1>Ley de Hick aplicada a la navegación web</h1>
  <div class="comparativa">
    <div class="demo mal-diseno">
      <h2>Versión A: 12 opciones planas (No recomendado)</h2>
      <nav>
        <a href="#">Inicio</a> <a href="#">Sobre nosotros</a> <a href="#">Historia</a>
        <a href="#">Servicios web</a> <a href="#">Apps móviles</a> <a href="#">Consultoría</a>
        <a href="#">Blog</a> <a href="#">Guías</a> <a href="#">Webinars</a>
        <a href="#">Contacto</a> <a href="#">Soporte</a> <a href="#">FAQ</a>
      </nav>
      <div class="info-box warning">
        <span class="formula">T = b × log2(12) ≈ b × 3.58</span><br>
        La persona usuaria debe procesar 12 opciones simultáneamente.
        El tiempo de decisión es proporcional a log2(12).
      </div>
    </div>
    <div class="demo buen-diseno">
      <h2>Versión B: 4 categorías de 3 enlaces (Recomendado)</h2>
      <nav>
        <div class="categoria">
          <span class="categoria-titulo">Empresa</span>
          <a href="#">Inicio</a>
          <a href="#">Sobre nosotros</a>
          <a href="#">Historia</a>
        </div>
        <div class="categoria">
          <span class="categoria-titulo">Servicios</span>
          <a href="#">Web</a>
          <a href="#">Apps Móviles</a>
          <a href="#">Consultoría</a>
        </div>
        <div class="categoria">
          <span class="categoria-titulo">Recursos</span>
          <a href="#">Blog</a>
          <a href="#">Guías</a>
          <a href="#">Webinars</a>
        </div>
        <div class="categoria">
          <span class="categoria-titulo">Ayuda</span>
          <a href="#">Contacto</a>
          <a href="#">Soporte</a>
          <a href="#">FAQ</a>
        </div>
      </nav>
      <div class="info-box success">
        <span class="formula">T = b × log2(4) + b × log2(3) ≈ b × 2 + b × 1.58 = b × 3.58</span><br>
        Aunque la suma logarítmica es similar, la carga cognitiva percibida es mucho menor
        porque las decisiones se toman en dos pasos más simples en lugar de uno complejo.
        El cerebro prefiere dos decisiones fáciles a una difícil.
      </div>
    </div>
  </div>
</body>
</html>
```

!!! note "Explicación del resultado"
    Aunque la suma de los logaritmos es matemáticamente similar en ambos casos, la experiencia subjetiva es radicalmente diferente. Enfrentarse a **12 opciones simultáneas** produce ansiedad y parálisis de decisión («análisis parálisis»). En cambio, elegir primero entre **4 categorías** y luego entre **3 enlaces** dentro de la categoría seleccionada se percibe como más manejable, aunque la complejidad matemática subyacente sea comparable. La ley de Hick nos enseña que lo importante no es solo el número de opciones, sino **cómo se presentan**.

---

### Ejemplo 3: Ley de Fitts aplicada a zonas táctiles en diseño mobile

!!! example "Contexto pedagógico"
    Este ejemplo demuestra la aplicación de la ley de Fitts al diseño de una interfaz móvil para listar tareas. Se comparan dos versiones: una con **botones pequeños** difíciles de pulsar y otra con **zonas táctiles amplias** accesibles al pulgar.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ley de Fitts - Diseño Mobile</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }

    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      background: #f0f2f5;
      display: flex;
      justify-content: center;
      padding: 2rem;
    }

    /*
     * SIMULACIÓN DE PANTALLA MÓVIL
     * Ancho típico de smartphone: 375px
     */
    .pantalla-movil {
      width: 375px;
      background: #fff;
      border-radius: 24px;
      overflow: hidden;
      box-shadow: 0 12px 40px rgba(0,0,0,0.15);
    }

    .cabecera {
      background: linear-gradient(135deg, #667eea, #764ba2);
      color: #fff;
      padding: 1.5rem;
      text-align: center;
    }

    .cabecera h2 {
      font-size: 1.25rem;
      font-weight: 700;
    }

    .cabecera p {
      font-size: 0.8rem;
      opacity: 0.8;
      margin-top: 0.25rem;
    }

    .lista-tareas {
      padding: 1.25rem;
    }

    .tarea {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      padding: 0.75rem 0;
      border-bottom: 1px solid #f0f0f0;
    }

    .tarea:last-child {
      border-bottom: none;
    }

    .tarea-texto {
      flex: 1;
      font-size: 0.95rem;
      color: #2d3748;
    }

    .tarea-texto.completada {
      text-decoration: line-through;
      color: #a0aec0;
    }

    /*
     * VERSIÓN INCORRECTA: Botón pequeño
     *
     * Ancho (W) = 30px, muy por debajo de los 44px recomendados.
     * Difícil de pulsar en pantalla táctil.
     * La persona usuaria pulsará accidentalmente el texto de la tarea
     * en lugar del botón, generando frustración.
     */
    .boton-malo {
      width: 30px;
      height: 30px;
      border-radius: 6px;
      border: 2px solid #cbd5e0;
      background: none;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #a0aec0;
      font-size: 0.8rem;
      flex-shrink: 0;
    }

    /*
     * VERSIÓN CORRECTA: Zona táctil amplia
     *
     * Ancho (W) = 44px, cumple con las directrices de Apple para iOS.
     * Fácil de pulsar incluso con el pulgar en movimiento.
     * Incluye transición visual para feedback inmediato.
     */
    .boton-bueno {
      width: 44px;
      height: 44px;
      border-radius: 12px;
      border: none;
      background: #667eea;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #fff;
      font-size: 1.1rem;
      flex-shrink: 0;
      transition: background 0.15s, transform 0.15s;
    }

    .boton-bueno:hover {
      background: #5a67d8;
    }

    .boton-bueno:active {
      transform: scale(0.92);
    }

    /*
     * DESCRIPCIÓN DE LAS ZONAS DE CONFORT DEL PULGAR
     * Información visual para el alumnado
     */
    .info-zonas {
      margin-top: 1.5rem;
      padding: 1rem;
      background: #f7fafc;
      border-radius: 8px;
      font-size: 0.8rem;
      color: #718096;
    }

    .etiqueta {
      display: inline-block;
      padding: 0.15rem 0.5rem;
      border-radius: 4px;
      font-size: 0.7rem;
      font-weight: 700;
      text-transform: uppercase;
    }

    .etiqueta.malo {
      background: #fed7d7;
      color: #9b2c2c;
    }

    .etiqueta.bueno {
      background: #c6f6d5;
      color: #22543d;
    }
  </style>
</head>
<body>
  <div class="pantalla-movil">
    <div class="cabecera">
      <h2>Mis Tareas</h2>
      <p>3 pendientes para hoy</p>
    </div>

    <div class="lista-tareas">
      <!-- TAREA 1: Botón incorrecto -->
      <div class="tarea">
        <button class="boton-malo" aria-label="Marcar como completada">✓</button>
        <span class="tarea-texto">Revisar informe de diseño</span>
        <span class="etiqueta malo">30px</span>
      </div>

      <!-- TAREA 2: Botón correcto -->
      <div class="tarea">
        <button class="boton-bueno" aria-label="Marcar como completada">✓</button>
        <span class="tarea-texto">Preparar presentación DCU</span>
        <span class="etiqueta bueno">44px</span>
      </div>

      <!-- TAREA 3: Botón incorrecto -->
      <div class="tarea">
        <button class="boton-malo" aria-label="Marcar como completada">✓</button>
        <span class="tarea-texto">Actualizar guías de estilo</span>
        <span class="etiqueta malo">30px</span>
      </div>

      <!-- TAREA 4: Botón correcto -->
      <div class="tarea">
        <button class="boton-bueno" aria-label="Marcar como completada">✓</button>
        <span class="tarea-texto completada">Enviar feedback al equipo</span>
        <span class="etiqueta bueno">44px</span>
      </div>

      <!-- TAREA 5: Botón correcto -->
      <div class="tarea">
        <button class="boton-bueno" aria-label="Marcar como completada">✓</button>
        <span class="tarea-texto">Revisar contraste WCAG de la paleta</span>
        <span class="etiqueta bueno">44px</span>
      </div>
    </div>

    <div class="info-zonas">
      <strong>Ley de Fitts en mobile:</strong> T = a + b × log2(2D/W + 1)<br><br>
      <strong>Botones de 30px:</strong> W pequeño → Índice de Dificultad alto → Mayor tiempo, más errores.<br>
      <strong>Botones de 44px:</strong> W grande → Índice de Dificultad bajo → Interacción rápida y precisa.<br><br>
      Las directrices de Apple (44×44pt) y Google (48×48dp) no son arbitrarias: están calibradas
      para el tamaño medio de la yema del dedo índice adulto (aproximadamente 10-14mm).
      Si tu zona táctil es menor, la persona usuaria <em>fallará</em> al pulsar.
    </div>
  </div>
</body>
</html>
```

!!! note "Explicación del resultado"
    La interfaz simula una pantalla de smartphone real. Las tareas con botones de **30px** son objetivamente más difíciles de pulsar: requieren mayor precisión motriz, producen más errores (pulsar el texto en lugar del botón) y generan frustración. Los botones de **44px**, en cambio, son fáciles de pulsar incluso caminando o en transporte público. La ley de Fitts no es teoría abstracta: si abres esta página en tu móvil e intentas pulsar alternativamente los botones pequeños y grandes, **sentirás físicamente** la diferencia predicha por la fórmula.

---

### Ejemplo 4: Carga cognitiva en formularios — de monolítico a paso a paso

!!! example "Contexto pedagógico"
    Comparación entre un formulario monolítico de **10 campos** (alta carga cognitiva) y el mismo formulario dividido en **3 pasos secuenciales** (carga cognitiva reducida). Se demuestra cómo la fragmentación mejora la experiencia.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Carga Cognitiva - Formularios</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      background: #f5f5f5;
      padding: 2rem;
    }
    h1 { text-align: center; color: #1a202c; margin-bottom: 2rem; }
    .comparativa {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(420px, 1fr));
      gap: 2rem;
      max-width: 1100px;
      margin: 0 auto;
    }
    .demo {
      background: white;
      border-radius: 12px;
      padding: 2rem;
      box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    }
    .demo h2 {
      font-size: 1.1rem;
      color: #2d3748;
      margin-bottom: 1.5rem;
    }
    label {
      display: block;
      font-size: 0.85rem;
      font-weight: 600;
      color: #4a5568;
      margin-bottom: 0.35rem;
    }
    input[type="text"],
    input[type="email"],
    input[type="tel"],
    input[type="password"] {
      width: 100%;
      padding: 0.65rem 0.85rem;
      border: 2px solid #e2e8f0;
      border-radius: 8px;
      font-size: 0.95rem;
      color: #2d3748;
      margin-bottom: 1rem;
      transition: border-color 0.2s;
    }
    input:focus {
      outline: none;
      border-color: #667eea;
    }
    button {
      width: 100%;
      padding: 0.85rem;
      background: #667eea;
      color: white;
      border: none;
      border-radius: 8px;
      font-size: 1rem;
      font-weight: 600;
      cursor: pointer;
      margin-top: 0.5rem;
      transition: background 0.2s;
    }
    button:hover { background: #5a67d8; }

    /* Formulario paso a paso */
    .paso-indicador {
      display: flex;
      gap: 0.5rem;
      margin-bottom: 1.5rem;
    }
    .paso {
      flex: 1;
      height: 4px;
      background: #e2e8f0;
      border-radius: 2px;
    }
    .paso.activo {
      background: #667eea;
    }
    .paso.completado {
      background: #48bb78;
    }
    .paso-grupo {
      margin-bottom: 1rem;
    }
    .etiqueta-paso {
      font-size: 0.75rem;
      color: #a0aec0;
      text-transform: uppercase;
      letter-spacing: 1px;
      margin-bottom: 1rem;
    }
    .info-carga {
      margin-top: 1rem;
      padding: 1rem;
      border-radius: 8px;
      font-size: 0.85rem;
      line-height: 1.5;
    }
    .info-carga.alta {
      background: #fff5f5;
      border-left: 4px solid #fc8181;
      color: #9b2c2c;
    }
    .info-carga.baja {
      background: #f0fff4;
      border-left: 4px solid #48bb78;
      color: #22543d;
    }
  </style>
</head>
<body>
  <h1>Carga cognitiva en formularios: monolítico vs paso a paso</h1>
  <div class="comparativa">
    <!-- FORMULARIO MONOLÍTICO: Alta carga cognitiva -->
    <div class="demo">
      <h2>Versión A: Formulario monolítico</h2>
      <p style="color: #718096; font-size: 0.85rem; margin-bottom: 1.5rem;">10 campos visibles simultáneamente</p>

      <label>Nombre</label>
      <input type="text" placeholder="Tu nombre">

      <label>Apellidos</label>
      <input type="text" placeholder="Tus apellidos">

      <label>Email</label>
      <input type="email" placeholder="tu@email.com">

      <label>Teléfono</label>
      <input type="tel" placeholder="+34 600 000 000">

      <label>Dirección</label>
      <input type="text" placeholder="Calle, número, piso">

      <label>Ciudad</label>
      <input type="text" placeholder="Tu ciudad">

      <label>Código Postal</label>
      <input type="text" placeholder="28001">

      <label>Contraseña</label>
      <input type="password" placeholder="Mínimo 8 caracteres">

      <label>Repetir contraseña</label>
      <input type="password" placeholder="Repite la contraseña">

      <label>Nombre de usuario</label>
      <input type="text" placeholder="Elige un nombre de usuario">

      <button>Crear cuenta</button>

      <div class="info-carga alta">
        <strong>Carga cognitiva ALTA:</strong> 10 campos exigen que la persona usuaria procese, recuerde y complete
        mucha información simultáneamente. La probabilidad de abandono es elevada.
        La memoria de trabajo (7 ± 2 elementos) se satura.
      </div>
    </div>

    <!-- FORMULARIO PASO A PASO: Baja carga cognitiva -->
    <div class="demo">
      <h2>Versión B: Formulario en 3 pasos</h2>
      <p style="color: #718096; font-size: 0.85rem; margin-bottom: 1rem;">Información fragmentada secuencialmente</p>

      <div class="paso-indicador">
        <div class="paso completado"></div>
        <div class="paso completado"></div>
        <div class="paso activo"></div>
      </div>
      <p class="etiqueta-paso">Paso 3 de 3 — Datos de acceso</p>

      <div class="paso-grupo">
        <label>Contraseña</label>
        <input type="password" placeholder="Mínimo 8 caracteres">

        <label>Repetir contraseña</label>
        <input type="password" placeholder="Repite la contraseña">

        <label>Nombre de usuario</label>
        <input type="text" placeholder="Elige un nombre de usuario">
      </div>

      <button>Crear cuenta</button>

      <div class="info-carga baja">
        <strong>Carga cognitiva BAJA:</strong> Solo 3 campos visibles en este paso (el resto ya se completaron en los pasos 1 y 2).
        La memoria de trabajo opera muy por debajo de su límite.
        La barra de progreso proporciona sensación de avance y motiva a completar.
      </div>
    </div>
  </div>
</body>
</html>
```

!!! note "Explicación del resultado"
    El formulario monolítico presenta **10 campos simultáneos**, saturando la memoria de trabajo (límite: **7 ± 2 ítems**). La persona usuaria ve todo el trabajo que le queda por delante y puede desanimarse antes de empezar. El formulario paso a paso muestra solo **3-4 campos por paso**, manteniendo la carga cognitiva dentro de los límites manejables. Además, la barra de progreso proporciona *feedback* motivacional: la persona usuaria siente que avanza y está más cerca de la meta. Diversos estudios de usabilidad confirman que los formularios paso a paso pueden aumentar las conversiones entre un **10% y un 25%** respecto a sus equivalentes monolíticos.


## Casos reales

### Caso 1: Spotify — Jerarquía visual y consistencia en una app de consumo masivo

Spotify es un caso de estudio fascinante sobre cómo la jerarquía visual puede gestionar una cantidad masiva de contenido (millones de canciones, podcasts, playlists) sin abrumar a la persona usuaria. La interfaz de Spotify aplica múltiples principios psicológicos de forma magistral.

**Análisis paso a paso:**

1. **Jerarquía visual mediante tamaño y posición:** La portada del álbum o playlist ocupa la posición central y el mayor tamaño en cada vista, estableciendo el elemento de máxima jerarquía. El nombre de la canción y el artista ocupan el segundo nivel. Los controles de reproducción (play, siguiente, anterior) ocupan el tercer nivel pero están anclados en la parte inferior, una zona de fácil acceso para el pulgar según la ley de Fitts.

2. **Consistencia interna extrema:** La interfaz de Spotify es un ejemplo de consistencia interna bien ejecutada. El botón de reproducción tiene siempre la misma forma, posición y comportamiento. Las portadas de álbumes son siempre cuadradas. Los nombres de artistas son siempre enlaces. Esta consistencia permite que las personas usuarias naveguen por secciones muy diferentes (Buscar, Tu Biblioteca, Podcasts) con los mismos patrones mentales.

3. **Ley de Hick aplicada a la navegación:** Aunque Spotify ofrece acceso a millones de canciones, la navegación principal se reduce a solo 3 pestañas en la versión móvil (Inicio, Buscar, Tu Biblioteca). Esta drástica simplificación aplica la ley de Hick: la persona usuaria solo debe elegir entre 3 opciones principales. Dentro de cada pestaña, el contenido se organiza en categorías y subcategorías, aplicando chunking para gestionar la complejidad.

4. **Modo oscuro como herramienta de jerarquía:** El fondo oscuro (#121212) actúa como un lienzo neutro que hace que las portadas de los álbumes (coloridas y vibrantes) destaquen poderosamente. Es una aplicación del contraste y de la ley de figura-fondo: el fondo oscuro se retira perceptivamente, permitiendo que el contenido musical emerja como figura.

5. **Carga cognitiva gestionada mediante personalización:** Spotify reduce la carga cognitiva de elegir qué escuchar mediante listas personalizadas (Discover Weekly, Daily Mix) que eliminan la necesidad de decidir. En lugar de enfrentar a la persona usuaria a 80 millones de canciones, le presenta 30 recomendaciones personalizadas. Esta estrategia es una aplicación brillante de la ley de Hick y la teoría de la carga cognitiva: reducir opciones mostrando solo las relevantes.

!!! tip "Lección para el alumnado"
    La interfaz de Spotify demuestra que la complejidad del **backend** (millones de canciones) no debe transferirse a la interfaz. La persona usuaria no necesita ver toda la complejidad; necesita ver solo lo relevante para su tarea actual. La simplificación **no es eliminar funcionalidades**, es presentarlas en el momento adecuado.

---

### Caso 2: Notion — Carga cognitiva y flexibilidad controlada

Notion es una herramienta de productividad que combina notas, bases de datos, wikis y gestión de proyectos. Su mayor desafío de diseño es ofrecer una flexibilidad casi ilimitada sin abrumar a las personas usuarias con demasiadas opciones. Es un caso de estudio sobre el delicado equilibrio entre potencia y simplicidad.

**Análisis paso a paso:**

1. **Lienzo en blanco con comando slash:** Notion resuelve el problema de la sobrecarga de opciones mostrando inicialmente un lienzo en blanco. Las opciones aparecen solo cuando la persona usuaria escribe "/", desplegando un menú contextual con todas las posibilidades. Esta estrategia es una aplicación directa de la divulgación progresiva: las opciones existen pero no se muestran hasta que se solicitan, manteniendo la carga cognitiva al mínimo cuando no se necesitan.

2. **Jerarquía visual basada en tipografía:** Notion utiliza exclusivamente diferencias tipográficas (tamaño, peso, color) para establecer jerarquía. No hay bordes, sombras ni fondos de color excesivos. Los títulos de página son grandes y oscuros. Los encabezados (H1, H2, H3) tienen pesos progresivamente menores. El cuerpo de texto es ligero y gris medio. Esta jerarquía puramente tipográfica crea una interfaz limpia y profesional que no compite con el contenido del usuario.

3. **Efecto de posición serial en la barra lateral:** La barra lateral de Notion muestra las páginas en orden, y las personas usuarias tienden a recordar mejor las primeras y las últimas páginas de la lista. Notion permite anclar páginas al principio (favoritos) y muestra las más recientes al principio del historial, aprovechando tanto la primacía como la recencia.

4. **Consistencia interna con variación controlada:** Todos los bloques de Notion (texto, listas, tablas, bases de datos) comparten un sistema de espaciado y alineación consistente. Sin embargo, cada tipo de bloque tiene su propio "color de acento" sutil (azul para bases de datos, verde para listas de tareas) que permite identificarlos rápidamente sin romper la unidad visual.

5. **Reducción de carga cognitiva mediante plantillas:** Notion ofrece plantillas predefinidas para casos de uso comunes (notas de reunión, seguimiento de proyectos, base de conocimiento). Las plantillas eliminan la carga cognitiva de "¿cómo estructuro esto?" y permiten a la persona usuaria empezar a trabajar inmediatamente con una estructura probada.

!!! tip "Lección para el alumnado"
    Notion demuestra que la **flexibilidad extrema** no es incompatible con la baja carga cognitiva si se utilizan las estrategias adecuadas: divulgación progresiva, plantillas, jerarquía tipográfica clara y consistencia interna. El secreto no es limitar lo que el usuario puede hacer, sino **presentar las opciones de forma que solo aparezcan cuando son necesarias**.

---

### Caso 3: GitHub — Ley de Fitts y navegación eficiente para desarrolladores

GitHub es la plataforma de desarrollo colaborativo más utilizada del mundo. Su interfaz, utilizada diariamente por millones de desarrolladores, está optimizada para la eficiencia y la reducción de fricción en tareas repetitivas. Es un caso de estudio sobre diseño de interfaces para usuarios expertos que realizan las mismas tareas cientos de veces al día.

**Análisis paso a paso:**

1. **Ley de Fitts en la barra de navegación:** Los elementos más utilizados (Pull requests, Issues, Actions, Projects) están en la parte superior de la página del repositorio, en pestañas con áreas clicables amplias. GitHub aprendió que los desarrolladores pasan la mayor parte del tiempo en estas secciones y las situó en posiciones de fácil acceso, aplicando la ley de Fitts para minimizar la distancia del cursor.

2. **Botón verde de "Code" como aplicación de contraste:** El botón verde de descarga/clonación es el único elemento de color vibrante en la cabecera del repositorio. Todo lo demás es gris, negro o azul oscuro. Este contraste extremo hace que el botón sea imposible de ignorar, guiando a la persona usuaria hacia la acción principal. Es una aplicación del principio de contraste como herramienta de jerarquía: si todo es colorido, nada destaca; si solo un elemento es colorido, ese elemento domina la atención.

3. **Consistencia externa con las convenciones de Git:** GitHub no intentó reinventar la terminología ni los flujos de trabajo de Git. Los botones y etiquetas utilizan los mismos términos que los desarrolladores ya conocen (commit, push, pull, merge, branch, fork). Esta consistencia externa reduce la curva de aprendizaje a prácticamente cero para cualquier persona que ya conozca Git.

4. **Repetición en la visualización de código:** El visor de código de GitHub aplica el principio de repetición de forma rigurosa. Cada línea de código tiene la misma altura, la misma tipografía monoespaciada (Consolas, monospace), la misma numeración a la izquierda. Esta repetición crea un ritmo visual que permite a los desarrolladores escanear cientos de líneas de código eficientemente, detectando patrones y anomalías.

5. **Carga cognitiva en los Pull Requests:** La página de un Pull Request podría ser abrumadora (conversaciones, commits, checks, files changed, diff). GitHub utiliza pestañas para segmentar esta información, permitiendo a la persona usuaria centrarse en una cosa cada vez. La pestaña "Conversation" muestra los comentarios, la pestaña "Commits" muestra el historial, y la pestaña "Files changed" muestra el diff. Esta segmentación aplica el principio de chunking para mantener cada vista dentro de los límites de la memoria de trabajo.

!!! tip "Lección para el alumnado"
    GitHub demuestra que las interfaces para **usuarios expertos** deben priorizar la **eficiencia sobre la novedad**. Los desarrolladores no quieren una interfaz «sorprendente»; quieren una interfaz **predecible** que puedan navegar con memoria muscular. La consistencia, el contraste funcional (no decorativo) y la segmentación de información son las claves del diseño para usuarios frecuentes.

---

### Caso 4: Twitter/X — Efecto de posición serial y jerarquía en el feed

Twitter (ahora X) es un caso de estudio sobre cómo el efecto de posición serial y la jerarquía visual se aplican al diseño de feeds de contenido en tiempo real, donde la persona usuaria consume decenas o cientos de publicaciones en una sesión.

**Análisis paso a paso:**

1. **Efecto de primacía en el tweet fijado:** Twitter permite "fijar" un tweet en la parte superior del perfil, que siempre aparece primero independientemente de su fecha. Este tweet fijado se beneficia del efecto de primacía: es lo primero que ve cualquier visitante del perfil y, por tanto, lo que mejor recordará.

2. **Jerarquía visual en cada tweet:** Cada tweet tiene una jerarquía interna clara: el avatar y el nombre del usuario (identidad) en la parte superior izquierda, el contenido del tweet (el mensaje) en el centro con mayor tamaño tipográfico, y los metadatos e interacciones (respuestas, retweets, likes) en la parte inferior con iconos pequeños y color gris claro. Esta jerarquía permite escanear decenas de tweets rápidamente, identificando autor y contenido sin necesidad de leer cada palabra.

3. **Contraste para acciones destructivas vs constructivas:** El botón de "Me gusta" (corazón) utiliza el color rojo cuando está activo, creando un fuerte contraste con los otros iconos de interacción (grises). Este contraste no es casual: el rojo es el color de la emoción y la pasión en la psicología del color occidental, y se asocia con la acción de "me gusta" de forma intuitiva.

4. **Carga cognitiva en la composición de tweets:** El contador de caracteres (originalmente 140, ahora 280 para usuarios gratuitos) es un ejemplo de reducción de carga cognitiva: en lugar de obligar a la persona usuaria a contar manualmente si su texto cabe, el contador proporciona feedback en tiempo real. Cuando quedan menos de 20 caracteres, el contador cambia a color naranja; cuando se excede, cambia a rojo. Este sistema de alerta progresiva aplica los principios de retroalimentación inmediata para reducir la carga cognitiva.

5. **Patrón de escaneo en F en el timeline:** El timeline de Twitter es un ejemplo perfecto del patrón en F. El avatar y el nombre del autor están alineados a la izquierda (barrido vertical del patrón F), el contenido del tweet ocupa la barra horizontal superior de cada ítem, y las interacciones están en la parte inferior. Los estudios de eye-tracking confirman que las personas usuarias de Twitter escanean el timeline siguiendo exactamente este patrón, lo que permite procesar mucha información en poco tiempo.

!!! tip "Lección para el alumnado"
    Twitter demuestra que los principios psicológicos se aplican incluso en las interfaces más informales y dinámicas. El hecho de que el feed sea en tiempo real y el contenido sea generado por usuarios **no exime** de aplicar jerarquía, contraste y gestión de carga cognitiva. De hecho, en interfaces con mucho contenido dinámico, estos principios son **aún más importantes** para evitar el caos visual.


## Actividades guiadas

### Actividad guiada 1: Medición práctica de la Ley de Fitts en botones

**Objetivo:** Experimentar directamente la ley de Fitts midiendo el tiempo que se tarda en hacer clic en botones de diferentes tamaños y posiciones, y contrastar los resultados con la fórmula teórica.

**Metodología:** El alumnado, por parejas, utilizará una página web preparada por el docente con botones de diferentes tamaños (24px, 32px, 48px, 64px) colocados a diferentes distancias. Un miembro de la pareja medirá el tiempo con un cronómetro mientras el otro hace clic en los botones. Se registrarán los tiempos en una tabla y se calcularán las medias. Posteriormente se compararán con la predicción de la fórmula de Fitts: T = a + b × log2(2D/W + 1).

**Entregable:** Tabla de mediciones con tiempos reales, tiempos teóricos según la fórmula, y un breve análisis de las discrepancias observadas. Se valorará la reflexión sobre las implicaciones para el diseño de interfaces táctiles.

**Duración:** 60 minutos.

---

### Actividad guiada 2: Rediseño de un menú de navegación aplicando la Ley de Hick

**Objetivo:** Aplicar la ley de Hick para transformar un menú de navegación sobrecargado en una estructura navegable y cognitivamente eficiente.

**Enunciado:** El docente proporciona un menú de navegación de 20 enlaces desorganizados (simulando el sitio web de una gran universidad o administración pública). El alumnado debe: (1) analizar los enlaces y agruparlos por categorías semánticas, (2) diseñar una estructura jerárquica de máximo 3 niveles de profundidad, (3) implementar el menú en HTML y CSS, y (4) realizar una prueba con 3 compañeros/as para medir el tiempo que tardan en encontrar elementos concretos en el menú original frente al rediseñado.

**Entregable:** Código HTML/CSS del menú rediseñado, resultados de la prueba de tiempos (tabla comparativa), y breve justificación de las decisiones basada en la ley de Hick.

**Duración:** 120 minutos.

---

### Actividad guiada 3: Análisis de carga cognitiva en un proceso de registro

**Objetivo:** Evaluar críticamente la carga cognitiva de un proceso de registro real y proponer mejoras basadas en la teoría de Sweller.

**Enunciado:** El docente proporciona capturas de pantalla del proceso de registro de un servicio online real (puede ser un banco, una aerolínea o un servicio público). El alumnado debe: (1) identificar todos los elementos que contribuyen a la carga cognitiva (campos innecesarios, información redundante, instrucciones poco claras, falta de agrupación), (2) cuantificar la carga usando una escala subjetiva (1-5) para cada pantalla, (3) rediseñar el proceso reduciendo la carga cognitiva aplicando las estrategias estudiadas (chunking, fragmentación en pasos, eliminación de campos no esenciales, mejora de etiquetas, adición de valores por defecto inteligentes), y (4) dibujar wireframes del proceso rediseñado.

**Entregable:** Informe de evaluación de carga cognitiva con los problemas identificados, wireframes del proceso rediseñado, y justificación de cada mejora.

**Duración:** 150 minutos.

---

## Actividades propuestas

### Actividad propuesta 1: Calculadora visual de la Ley de Fitts

**Enunciado:** Construye una página web interactiva que funcione como "calculadora visual de la Ley de Fitts". La página debe permitir a la persona usuaria ajustar el tamaño de un botón (W) y su distancia desde el cursor (D) mediante sliders, y mostrar en tiempo real: (a) el Índice de Dificultad (ID = log2(2D/W + 1)), (b) una representación visual del botón con el tamaño y la posición seleccionados, (c) una simulación de un cursor moviéndose hacia el botón (animación CSS o canvas), y (d) una sección con recomendaciones de diseño basadas en los valores actuales (por ejemplo: "Este botón es demasiado pequeño para interacción táctil. Aumenta W a al menos 44px").

**Requisitos técnicos:** HTML, CSS y JavaScript vanilla. Sin frameworks. La interfaz debe ser responsive y funcionar tanto en escritorio como en móvil. La fórmula de Fitts debe estar implementada en JavaScript y los cálculos deben actualizarse en tiempo real al mover los sliders.

**Criterios de evaluación:**
- Corrección matemática de la implementación de la fórmula de Fitts (25%).
- Calidad de la interfaz visual y la representación gráfica del botón y cursor (25%).
- Utilidad pedagógica de las recomendaciones de diseño automáticas (25%).
- Calidad del código y comentarios (25%).

---

### Actividad propuesta 2: Auditoría de consistencia de una app móvil

**Enunciado:** Selecciona una aplicación móvil que utilices a diario y realiza una auditoría exhaustiva de su consistencia interna y externa. Documenta cada infracción de consistencia que encuentres con capturas de pantalla.

**Apartados de la auditoría:**
1. **Consistencia de color:** ¿Se utiliza el mismo color para la misma acción en todas las pantallas? ¿Los colores semánticos (éxito, error, advertencia) son consistentes?
2. **Consistencia tipográfica:** ¿Se respeta la misma escala tipográfica en todas las pantallas? ¿Hay textos con tamaños inconsistentes?
3. **Consistencia de espaciado:** ¿Los márgenes y rellenos siguen una escala predecible? ¿Hay pantallas con espaciados visiblemente diferentes?
4. **Consistencia de interacción:** ¿Los mismos gestos producen los mismos resultados? ¿Los botones similares se comportan de manera similar?
5. **Consistencia externa:** ¿La app respeta las convenciones del sistema operativo (iOS/Android)? ¿Utiliza los mismos iconos y gestos que otras apps similares?

**Entregable:** Informe de auditoría (mínimo 1500 palabras) con capturas de pantalla anotadas, tabla de infracciones priorizadas por gravedad, y recomendaciones de mejora.

---

### Actividad propuesta 3: Test A/B de formularios con diferente carga cognitiva

**Enunciado:** Diseña y ejecuta un pequeño test A/B comparando dos versiones de un formulario de contacto: la versión A con alta carga cognitiva (muchos campos, sin agrupar, sin indicaciones) y la versión B con baja carga cognitiva (campos agrupados por proximidad, etiquetas claras, campos opcionales marcados, barra de progreso si tiene varios pasos). Recluta al menos 10 personas (compañeros/as de clase, familiares, amigos) y mide: tiempo de completitud, tasa de errores (campos mal rellenados), y satisfacción subjetiva (pregunta: "del 1 al 5, ¿cómo de fácil te ha parecido rellenar este formulario?").

**Entregable:** Informe del test A/B con metodología, datos recogidos (tabla con tiempos, errores y puntuaciones de satisfacción), análisis estadístico básico (medias comparativas), y conclusiones sobre el impacto de la carga cognitiva en formularios.

---

## Actividades de ampliación

### Actividad de ampliación 1: Implementación de un sistema de diseño basado en principios psicológicos

**Enunciado:** Diseña e implementa un mini Design System en HTML y CSS que documente visualmente los principios psicológicos estudiados en esta unidad. El Design System debe incluir un "patrón" para cada principio:

- **Patrón Hick:** Componente de menú categorizado con variantes (1 nivel, 2 niveles, mega menú).
- **Patrón Fitts:** Componente de botón con variantes de tamaño (small 32px, medium 44px, large 56px) y reglas de uso (cuándo usar cada tamaño).
- **Patrón Carga Cognitiva:** Componente de formulario con variantes (inline, paso a paso, acordeón) y reglas de uso según la complejidad.
- **Patrón Consistencia:** Variables CSS para colores semánticos, espaciado y tipografía que demuestren cómo se mantiene la consistencia.

Cada patrón debe incluir: ejemplo visual, código HTML/CSS, explicación del principio psicológico subyacente, y recomendaciones de uso.

**Formato:** Página web funcional con navegación entre patrones.

---

### Actividad de ampliación 2: Análisis de eye-tracking simulado

**Enunciado:** Utilizando las DevTools del navegador y la extensión "Eye Tracking Simulator" (o simplemente superponiendo zonas de calor manualmente), analiza tres páginas de inicio de sitios web populares (Reddit, Wikipedia, BBC News) y dibuja sobre capturas de pantalla el recorrido visual predicho por el patrón en F. Para cada página, identifica:
- ¿Qué elementos caen en las zonas de máxima atención del patrón F?
- ¿Hay elementos importantes que quedan fuera de esas zonas?
- ¿Coincide la jerarquía visual implementada con las predicciones del patrón F?

**Entregable:** Informe con capturas de pantalla anotadas, mapas de calor dibujados, análisis de cada página, y recomendaciones de mejora para aquella página que peor aproveche los patrones de escaneo.

---

### Actividad de ampliación 3: Investigación sobre leyes psicológicas emergentes en UX

**Enunciado:** Investiga más allá de las leyes estudiadas en clase y explora otros principios psicológicos aplicables al diseño de interfaces. Algunas sugerencias: Ley de Jakob (las personas usuarias pasan la mayor parte del tiempo en otros sitios, por lo que prefieren que tu sitio funcione como los demás), Ley de Tesler (la complejidad total de un sistema es constante; solo puedes desplazarla, no eliminarla), Efecto Von Restorff (los elementos que destacan son más recordados), Efecto Zeigarnik (las tareas incompletas se recuerdan mejor que las completas), o Principio de Pareto (el 80% de los efectos proviene del 20% de las causas, aplicado a funcionalidades del software).

**Formato:** Prepara una presentación de 10 minutos sobre una de estas leyes que incluya: definición, experimento original que la demostró, aplicaciones al diseño de interfaces con ejemplos concretos, y una crítica sobre sus limitaciones.

---

## Buenas prácticas

1. **Mide el tamaño de tus zonas táctiles antes de lanzar:** Cada botón, enlace o zona interactiva debe tener al menos 44×44px (Apple) o 48×48dp (Google). Utiliza las DevTools del navegador para inspeccionar el tamaño real en píxeles CSS de cada elemento interactivo. Si es menor, la ley de Fitts predice que las personas usuarias cometerán errores y se frustrarán, especialmente en dispositivos móviles.

2. **Aplica el principio de divulgación progresiva por defecto:** Ante la duda entre mostrar muchas opciones o pocas, muestra pocas y ofrece un camino claro para acceder a más. Esta estrategia es siempre preferible porque comienza con baja carga cognitiva y permite a la persona usuaria decidir si necesita más complejidad.

3. **Agrupa visualmente por proximidad antes que por bordes:** El espaciado consistente comunica relaciones entre elementos de forma más elegante y menos intrusiva que los bordes y los fondos. Utiliza una escala de espaciado (4px, 8px, 16px, 32px, 48px) y asegúrate de que el espacio entre grupos es visiblemente mayor que el espacio dentro de cada grupo.

4. **Verifica la consistencia interna con una checklist:** Antes de dar por terminada una interfaz, recorre sistemáticamente todos los botones, todos los formularios, todos los mensajes de error y todas las pantallas comprobando que los estilos, comportamientos y textos son consistentes. Las personas usuarias confían en interfaces predecibles y desconfían de las inconsistentes.

5. **Diseña formularios como conversaciones, no como interrogatorios:** En lugar de presentar 15 campos fríos, divide los formularios en pasos lógicos, utiliza un tono conversacional ("¿Cómo te llamas?" en lugar de "Nombre:"), muestra solo los campos necesarios en cada paso, e incluye indicadores de progreso. La carga cognitiva se reduce drásticamente y las tasas de finalización aumentan.

---

## Errores frecuentes

1. **Sobrecargar los menús de navegación con demasiadas opciones:** El error más común derivado del desconocimiento de la ley de Hick es presentar docenas de enlaces en la navegación principal, asumiendo que "cuantas más opciones, mejor". El resultado es parálisis de decisión y abandono. La solución es categorizar, jerarquizar y utilizar divulgación progresiva.

2. **Crear botones pequeños por razones estéticas:** La tentación de hacer botones pequeños, sutiles y "elegantes" es grande, especialmente entre diseñadores con formación gráfica. Pero un botón de 28×28px es objetivamente difícil de pulsar. La ley de Fitts no es una opinión estética, es una ley psicomotriz validada experimentalmente durante décadas.

3. **Forzar a las personas usuarias a recordar información de una pantalla a otra:** Cuando un proceso de registro pide el email en la pantalla 1 y luego, en la pantalla 3, pide "introduce tu email para verificar", está forzando a la persona usuaria a recordar qué email utilizó. Esto consume memoria de trabajo innecesariamente. La interfaz debe recordar la información por la persona usuaria, no al revés.

4. **Romper la consistencia externa "para ser original":** Intentar reinventar patrones de interacción establecidos (como colocar el botón de búsqueda en una ubicación inesperada o usar un icono no estándar para "menú") es un error que genera fricción innecesaria. La originalidad en diseño de interfaces debe reservarse para la identidad visual, no para los patrones de interacción.

5. **Diseñar formularios sin tener en cuenta la carga cognitiva:** Presentar formularios de 12-15 campos sin agrupar, sin indicar cuáles son obligatorios, sin valores por defecto y sin validación en tiempo real es una receta para el abandono. Cada uno de estos defectos incrementa la carga cognitiva, y la suma de todos ellos puede hacer que incluso las personas más motivadas abandonen el proceso.

---

## Resumen

Esta unidad ha profundizado en los principios psicológicos y perceptivos que subyacen al diseño de interfaces web efectivas. Se ha abordado cada principio desde una doble perspectiva: la fundamentación psicológica (qué dice la ciencia sobre cómo las personas perciben, deciden e interactúan) y la aplicación práctica al diseño web (cómo traducir ese conocimiento en HTML y CSS). La jerarquía visual, el contraste, la proximidad, la repetición, la alineación, el balance y la consistencia forman el núcleo de herramientas del diseñador para organizar la información de forma que la persona usuaria la procese sin esfuerzo.

Las leyes psicológicas de la interacción —Hick, Fitts, efecto de posición serial y carga cognitiva— complementan los principios perceptivos proporcionando un marco cuantitativo y predictivo. La ley de Hick nos dice que más opciones implican decisiones más lentas; la ley de Fitts, que los objetivos pequeños y lejanos son difíciles de alcanzar; el efecto de posición serial, que el orden de los elementos importa; y la teoría de la carga cognitiva, que la memoria de trabajo tiene límites que debemos respetar.

Los casos de estudio de Spotify, Notion, GitHub y Twitter/X han demostrado que estos principios no son construcciones académicas abstractas, sino realidades que las empresas tecnológicas más exitosas aplican sistemáticamente en sus productos. La diferencia entre una interfaz mediocre y una excelente rara vez está en la tecnología o en el presupuesto; está en la aplicación disciplinada y coherente de principios psicológicos validados por décadas de investigación.

El alumnado debe interiorizar que cada decisión de diseño —el tamaño de un botón, el número de opciones en un menú, la agrupación de campos en un formulario, el color de un mensaje de error— tiene consecuencias psicológicas medibles en las personas que utilizan la interfaz. Diseñar sin conocer estos principios es como construir un puente sin conocer las leyes de la física: puede que aguante, pero las probabilidades de fracaso son innecesariamente altas.

---

## Recursos complementarios

### Libros y lecturas
- **Yablonski, Jon. (2020).** *Laws of UX: Using Psychology to Design Better Products & Services.* O'Reilly Media. — Una introducción accesible y visualmente atractiva a las principales leyes psicológicas aplicables al diseño de interfaces. Cada ley se explica en un capítulo breve con ejemplos prácticos.
- **Weinschenk, Susan M. (2011).** *100 Things Every Designer Needs to Know About People.* New Riders. — Compendio de principios psicológicos aplicados al diseño. Cubre percepción visual, memoria, atención y motivación.
- **Johnson, Jeff. (2020).** *Designing with the Mind in Mind: Simple Guide to Understanding User Interface Design Guidelines.* Morgan Kaufmann. — Un enfoque basado en la psicología cognitiva para explicar por qué las guías de diseño de interfaces son como son.
- **Sweller, John; Ayres, Paul; Kalyuga, Slava. (2011).** *Cognitive Load Theory.* Springer. — La obra académica de referencia sobre la teoría de la carga cognitiva, para quienes deseen profundizar más allá de la aplicación práctica.

### Herramientas en línea
- **Laws of UX** (https://lawsofux.com) — Sitio web creado por Jon Yablonski que presenta visualmente las principales leyes de UX con ejemplos y referencias.
- **NNgroup** (https://www.nngroup.com) — El Nielsen Norman Group publica regularmente artículos y vídeos sobre usabilidad y psicología del diseño basados en investigación empírica.
- **WebAIM Contrast Checker** (https://webaim.org/resources/contrastchecker/) — Herramienta para verificar el ratio de contraste de color según los estándares WCAG.
- **Stark** (https://www.getstark.co) — Plugin para Figma, Sketch y Adobe XD que verifica contraste, simula daltonismo y audita accesibilidad directamente en los mockups de diseño.
- **Google Material Design** (https://material.io) — Sistema de diseño de Google que aplica los principios estudiados (escala de espaciado, jerarquía tipográfica, zonas táctiles de 48dp).

### Vídeos recomendados
- **"The Science of Great UI"** — Charla de Mark Miller en TEDx donde explica principios psicológicos del diseño de interfaces con demostraciones interactivas.
- **"Psychology of Design"** — Serie de vídeos del canal de YouTube "Flux" (Ran Segall) que cubre leyes de UX con ejemplos prácticos.
