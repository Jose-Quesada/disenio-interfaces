---
icon: lucide/scale
---

# Unidad 19: Marco Legal del Contenido Multimedia y Preparación de Archivos para la Web

## Objetivos de aprendizaje

Al finalizar esta unidad, el alumnado será capaz de:

1. Explicar qué es el derecho de autor (propiedad intelectual) y cómo se aplica al contenido multimedia utilizado en la web (imágenes, audio, vídeo, tipografías, iconos).
2. Identificar y distinguir los principales tipos de **licencias** (dominio público, licencias propias, Creative Commons y sus variantes), sabiendo leer las condiciones de uso de cada recurso.
3. Seleccionar fuentes legales de contenido multimedia (bancos de imágenes/audio/vídeo con licencia adecuada, generadores) y documentar la procedencia y licencia de cada activo empleado en un proyecto.
4. Preparar archivos multimedia para la web aplicando el flujo completo: captura/generación → tratamiento → optimización → exportación al formato adecuado según su finalidad (CE 3.c–3.g), respetando la guía de estilo.
5. Reconocer los riesgos legales y buenas prácticas (atribución, limitaciones, licencias de tipografías web y de frameworks) para publicar contenido multimedia sin infringir derechos de terceros.

## Relación con los Resultados de Aprendizaje

Esta unidad se vincula directamente con el **Resultado de Aprendizaje 3 (RA3)** del módulo profesional 0615 *Diseño de interfaces web*: *"Prepara archivos multimedia para la web, analizando sus características y manejando herramientas específicas"*. Cubre de forma explícita el **criterio de evaluación 3.a**: *"Se han reconocido las implicaciones de las licencias y los derechos de autor en el uso de material multimedia"*, que no se aborda en ninguna otra unidad del módulo, y refuerza los criterios **3.c** (analizar herramientas para generar contenido multimedia), **3.d** (tratamiento digital de la imagen), **3.e** (manipulación de audio y vídeo), **3.f** (animaciones a partir de imágenes fijas) y **3.g** (importar/exportar en diversos formatos según su finalidad).

Complementa a la Unidad 12 (*Integración de Contenido Multimedia en la Web*), centrada en el aspecto técnico de **formatos, optimización e integración** (RA4), aportando aquí la dimensión **legal y de preparación** que el RA3 exige. Juntas, ambas unidades cubren íntegramente los RA3 y RA4 del módulo.

!!! note "Nota sobre la numeración"
    La numeración de Resultados de Aprendizaje y Criterios de Evaluación corresponde al currículo oficial del módulo 0615 (**RD 405/2023, BOE**; currículo andaluz). El **RA3** es el resultado dedicado a la **preparación** de archivos multimedia; esta unidad cierra su criterio legal (**3.a**), habitualmente omitido.

## Conocimientos previos

Para abordar esta unidad con soltura, el alumnado debe:

1. Haber trabajado la Unidad 12 (*Integración de Contenido Multimedia en la Web*): formatos de imagen (JPEG, PNG, SVG, WebP, AVIF), optimización y etiquetas `<img>`, `<audio>` y `<video>`.
2. Conocer los fundamentos de HTML semántico (Unidad 7) para incorporar correctamente los recursos y sus metadatos.
3. Manejar herramientas básicas de tratamiento de imagen (p. ej., GIMP, Photoshop o alternativas online como Squoosh) y de audio/vídeo (Audacity, FFmpeg).
4. Tener nociones de propiedad intelectual a nivel ciudadano: qué es una obra protegida y quién detiene los derechos por defecto.

## Contenidos

1. **Propiedad intelectual y derecho de autor.** Concepto de obra original. Derechos morales y patrimoniales. Duración de la protección. El autor como titular por defecto y cesión de derechos. Diferencias entre copyright y otras figuras (marcas, patentes).
2. **El dominio público.** Qué significa que una obra esté en dominio público (caducidad de la protección, abdicación, obras del sector público según jurisdicción). Fuentes y precauciones (no todo lo "encontrable" es dominio público).
3. **Licencias y condiciones de uso.** Licencia implícita vs explícita. Términos de servicio de bancos de recursos. Qué implica "uso comercial", "uso editorial", "modificación permitida" o "atribución requerida".
4. **Creative Commons (CC).** Las seis combinaciones (CC BY, CC BY-SA, CC BY-NC, CC BY-ND, CC BY-NC-SA, CC BY-NC-ND). Cómo leer el sello CC. Licencias CC0 y dominio público dedicado. Limitaciones y conflictos entre licencias.
5. **Fuentes legales de contenido multimedia.** Bancos de imágenes (Unsplash, Pexels, Pixabay), audio (Freesound, Incompetech), vídeo (Pexels, Coverr), iconos e ilustraciones (Flaticon, SVG Repo, Heroicons), tipografías web (Google Fonts y sus licencias). Criterios para elegir la fuente adecuada al proyecto.
6. **Tipografías, iconos y frameworks: licencias específicas.** Licencia de uso web de fuentes (self-hosting vs CDN, número de vistas, uso comercial). Licencias de iconos y de componentes de UI. Riesgo de usar assets "gratuitos" con restricciones ocultas.
7. **Flujo de preparación de archivos multimedia.** Captura/generación → tratamiento digital (reducción de color, recorte, limpieza) → optimización (compresión, dimensiones, metadatos EXIF) → exportación al formato según finalidad (CE 3.d–3.g). Documentación de la cadena de custodia del activo.
8. **Atribución y registro de fuentes.** Cómo citar correctamente una obra con licencia CC (autor, título, licencia, enlace — patrón TATL). Cuaderno/registro de activos del proyecto (inventario con licencia y URL de origen).
9. **Riesgos legales y buenas prácticas.** Consecuencias de la infracción (takedowns, sanciones). Buena fe y diligencia debida. Uso justo/fair use (limitado y jurisdiccionalmente variable). Protocolo ante la duda: sustituir por recurso con licencia clara.
10. **Aplicación a la guía de estilo.** Definir en la guía del proyecto (Unidad 4) la política de activos multimedia: licencias admitidas, fuentes autorizadas, formato de atribución y responsable de cada activo (CE 3.h).

## Desarrollo teórico

### 1. Propiedad intelectual y derecho de autor

El **derecho de autor** protege las obras literarias, artísticas y científicas originales desde el momento de su creación, sin necesidad de registro. Distingue dos bloques:

- **Derechos morales:** inalienables e irrenunciables en gran parte del ordenamiento (p. ej., el derecho a la paternidad de la obra).
- **Derechos patrimoniales:** explotación económica (reproducción, distribución, comunicación pública, transformación) que pueden cederse o licenciarse; en España y la UE suelen durar **toda la vida del autor más 70 años** tras su fallecimiento.

En el diseño web esto es crítico:

!!! warning "Regla por defecto"
    **Por defecto, todo contenido multimedia que no hayas creado tú está protegido.** Copiar una imagen de Google Images, un vídeo de YouTube o una canción de Spotify para tu proyecto constituye, en general, una **infracción**, aunque la web sea educativa o sin ánimo de lucro. La excepción **no es** «no cobro», sino **contar con el permiso del titular** (compra, licencia o que la obra esté en dominio público / tenga una licencia que lo permita).

### 2. El dominio público

Una obra entra en **dominio público** cuando deja de estar protegida (típicamente por caducar el plazo) o cuando su titular renuncia a los derechos. Entonces cualquiera puede usarla libremente, incluso comercialmente y sin atribución (aunque esta es cortés). Fuentes habituales: obras con más de **70 años** de la muerte del autor (pintura clásica, literatura), algunas obras del sector público según la legislación aplicable, y recursos publicados bajo **CC0**.

!!! warning "Precaución: «parece antiguo» no es dominio público"
    Algunos países protegen **ediciones o fotografías** de obras en dominio público; el aspecto antiguo de un recurso **no equivale** a que sea libre de derechos.

### 3. Licencias y condiciones de uso

Una **licencia** es el permiso que el titular concede para usar la obra bajo condiciones concretas. Debe leerse siempre:

- **Uso comercial vs no comercial:** si el proyecto genera ingresos (o está en un sitio monetizado), muchas licencias "no comerciales" (NC) lo prohíben.
- **Modificación permitida o no:** algunas licencias exigen que la obra se use "tal cual" (ND, *NoDerivatives*).
- **Atribución requerida:** casi todas las licencias gratuitas exigen creditar al autor.
- **Condiciones de servicio del banco:** cada plataforma añade sus propios términos (p. ej., prohibido revender el archivo tal cual, prohibido usarlo en logos de marca).

### 4. Creative Commons

**Creative Commons** ofrece un conjunto estándar de licencias que combinan cuatro condiciones:

| Condición | Significado |
|---|---|
| **BY** | Debes atribuir la autoría (TATL). |
| **NC** | Uso no comercial. |
| **ND** | Sin obras derivadas (no modificar). |
| **SA** | Compartir por igual (las modificaciones se licencian con los mismos términos). |

Las seis combinaciones posibles:

| Licencia | Combinación de condiciones |
|---|---|
| **CC BY** | solo **BY** (la más libre: solo atribución) |
| **CC BY-SA** | **BY + SA** (copyleft cultural) |
| **CC BY-NC** | **BY + NC** (sin uso comercial) |
| **CC BY-ND** | **BY + ND** (sin obras derivadas) |
| **CC BY-NC-SA** | **BY + NC + SA** (no comercial y compartir por igual) |
| **CC BY-NC-ND** | **BY + NC + ND** (la más restrictiva) |

Además, **CC0** es una **renuncia a derechos** (dedica la obra al dominio público).

!!! tip "Regla práctica: elegir licencia CC"
    Para un proyecto que **puedas modificar** y usar **comercialmente**, busca **CC0 o CC BY**; **evita NC/ND** salvo que encajen con el uso previsto.

### 5. Fuentes legales de contenido multimedia

- **Imágenes:** Unsplash, Pexels, Pixabay (licencias propias muy permisivas; revisa los términos de cada banco).
- **Audio/música:** Freesound (varias licencias CC), Incompetech (Kevin MacLeod, CC BY).
- **Vídeo:** Pexels, Coverr.
- **Iconos/ilustración:** SVG Repo, Heroicons, Flaticon (revisa licencia por icono y atribución).
- **Tipografías web:** Google Fonts (licencia SIL Open Font License, permite self-hosting y uso comercial), o fuentes de foundries con licencia web explícita.

Criterio de elección: compatibilidad de la licencia con el fin del proyecto (comercial/educativo), posibilidad de modificar, necesidad de atribución y fiabilidad de la fuente.

### 6. Tipografías, iconos y frameworks: licencias específicas

- **Fuentes web:** distinguir entre *descargar para usar localmente* y *licencia de embebido/web*. La OFL (Open Font License) lo permite; otras fuentes comerciales exigen comprar una licencia web por número de páginas vistas. Self-hostear una fuente comercial sin licencia es infracción.
- **Iconos y componentes:** muchos son CC BY o tienen licencias propias que exigen atribución o prohíben el uso en ciertos contextos (p. ej., logos). Los frameworks UI (Material, Bootstrap) suelen ser MIT/BSD, pero los *assets* gráficos pueden tener otra licencia.

### 7. Flujo de preparación de archivos multimedia

El flujo profesional de **preparación** (CE 3.c–3.g) es:

1. **Adquisición/generación:** crear el activo o obtenerlo de una fuente legal (documentando su licencia).
2. **Tratamiento digital:** recorte, corrección de color, limpieza, redimensionado al tamaño real de uso (CE 3.d–3.e).
3. **Optimización:** compresión (Squoosh/Sharp para imagen; FFmpeg para audio/vídeo), eliminación de metadatos EXIF innecesarios, elección de formato según contenido (fotografía → WebP/AVIF; UI/iconos → SVG; transparencia → PNG/WebP) (CE 3.g).
4. **Animación a partir de imágenes fijas:** secuencias, sprites o Lottie para microinteracciones (CE 3.f).
5. **Exportación según finalidad:** generar variantes por breakpoint (`srcset`/`sizes`) y por contexto (logo en claro/oscuro, vídeo con subtítulos).

!!! tip "Cadena de custodia"
    Cada activo debe dejar constancia de su **cadena de custodia**: **origen, licencia, autor, fecha y transformaciones aplicadas**.

### 8. Atribución y registro de fuentes

!!! info "Patrón TATL de atribución"
    Para obras con **CC BY**, la atribución sigue el patrón **TATL**:

    - **T** — Título de la obra
    - **A** — Autor
    - **T** — Título de la licencia (con enlace)
    - **L** — Línea de «si modificaste, indícalo»

    Ejemplo: *«Fotografía de ciudad» por Ana García, CC BY 4.0 (<https://creativecommons.org/licenses/by/4.0/>)*

La buena práctica es mantener un **registro/inventario de activos** del proyecto (tabla con: activo, origen, autor, licencia, atribución, uso) que además alimenta la guía de estilo (**CE 3.h**).

### 9. Riesgos legales y buenas prácticas

- **Infracción:** puede derivar en retirada del contenido (takedown), demandas o sanciones; el riesgo no desaparece por ser un trabajo académico si se publica.
- **Diligencia debida:** documentar la licencia de cada activo es tu defensa. "No sabía" rara vez exime.
- **Fair use / uso legítimo:** figura limitada, jurisdiccionalmente variable y difícil de invocar; no debe usarse como coartada general.
- **Protocolo ante la duda:** si no puedes verificar la licencia, **sustituye** el activo por uno con licencia clara o créalo tú mismo.

### 10. Política de activos en la guía de estilo

La guía de estilo del proyecto (Unidad 4) debe fijar la **política de activos multimedia**: qué licencias se admiten (p. ej., "solo CC0/CC BY y dominio público"), fuentes autorizadas, formato obligatorio de atribución, quién es responsable de cada activo y dónde vive el inventario. Esto garantiza que todo el equipo aplique el mismo criterio legal y visual (CE 3.h).

## Ejemplos guiados

### Ejemplo 1: Elegir la licencia correcta para un proyecto comercial

!!! example "Contexto pedagógico"
    Una **tienda online** necesita fondo de portada, música de ambiente para vídeo promocional e iconos de categoría.

| Necesidad | Fuente elegida | Licencia | ¿Encaja? |
|---|---|---|---|
| Fondo (fotografía) | Pexels | Licencia Pexels (uso comercial permitido, sin atribución obligatoria) | Sí |
| Música ambiente | Incompetech (Kevin MacLeod) | CC BY 3.0 | Sí, **atribución obligatoria** en el vídeo/credits |
| Iconos | Heroicons | MIT | Sí, uso libre |

!!! note "Explicación del resultado"
    El **único activo con condición** es la música (**CC BY**), por lo que se añade una línea de crédito al final del vídeo. Si el proyecto **no pudiera mostrar créditos**, se buscaría una alternativa **CC0**.

### Ejemplo 2: Inventario de activos con atribución

```markdown
| Activo            | Origen              | Autor          | Licencia   | Atribución requerida | Uso        |
|-------------------|--------------------|----------------|------------|----------------------|------------|
| hero-city.jpg     | Pexels             | (Pexels)       | Pexels     | No                   | Portada    |
| bg-music.mp3      | Incompetech        | K. MacLeod     | CC BY 3.0  | Sí (TATL)            | Vídeo promo|
| icon-cart.svg     | Heroicons          | (Heroicons)    | MIT        | No                   | Carrito    |
```

## Casos reales

- **Wikipedia / Wikimedia:** todo su contenido multimedia se rige por licencias libres (CC BY-SA, CC0 o dominio público) y exige atribución; es el ejemplo paradigmático de gestión legal de activos a gran escala.
- **Sanciones por imágenes:** son frecuentes los casos de sitios penalizados por usar fotografías "de Google" con copyright; la lección profesional es siempre verificar la fuente y conservar la licencia.
- **Tipografías web:** incidentes por self-hostear fuentes comerciales sin licencia web recuerdan que el formato del activo no implica libertad de uso.

## Actividades guiadas

1. **Clasificación de licencias.** Dado un listado de 8 recursos (con su licencia), clasifícalos en "usables comercialmente sin atribución / usables con atribución / no usables para este proyecto" y justifica cada decisión.
2. **Registro de activos.** Crea el inventario (tabla) de los multimedia empleados en tu proyecto, indicando origen, autor, licencia y atribución. Verifica que ninguno quede "sin licencia identificable".

## Actividades propuestas

1. **Auditoría legal de un sitio real (RA3 / CE 3.a).** Selecciona una web pública y audita sus activos multimedia: identifica al menos 5 imágenes/vídeos/iconos, determina su probable titular/licencia y detecta posibles riesgos (imágenes sin atribución CC, música con copyright). Redacta un informe con recomendaciones de sustitución.
2. **Política de activos para la guía de estilo (CE 3.h).** Define la política de contenido multimedia de tu proyecto: licencias admitidas, fuentes autorizadas, formato de atribución e inventario. Intégrala en la guía de estilo de la Unidad 4.
3. **Flujo completo de preparación (CE 3.c–3.g).** A partir de una fotografía original y un clip de audio, aplica el flujo completo (tratamiento → optimización → exportación a varios formatos por finalidad) y documenta cada paso con las herramientas usadas.

## Actividades de ampliación

1. **Comparativa de bancos.** Compara 3 bancos de imágenes/audio en términos de licencia, calidad, búsqueda y atribución; elabora una recomendación motivada para un equipo de desarrollo.
2. **Estudio de licencias de tipografías.** Investiga las condiciones web de 5 familias tipográficas (OFL vs comerciales) y documenta qué permite cada una (self-hosting, número de vistas, uso en logotipos).

## Buenas prácticas

1. **Nunca asumas** que un contenido es libre porque lo encontraste en la web; verifica siempre la licencia.
2. **Documenta** origen, autor y licencia de cada activo en un inventario del proyecto.
3. Prefiere **CC0 / dominio público / licencias permisivas** cuando el uso sea comercial o implique modificación.
4. **Atribuye** correctamente (TATL) lo que exija BY; conserva el rastro de la atribución.
5. Revisa los **términos específicos del banco** además de la licencia general.
6. Fija una **política de activos** en la guía de estilo y asigna responsable a cada recurso.
7. Ante la duda, **sustituye** por un activo con licencia clara o créalo tú mismo.

## Errores frecuentes

1. **"Es gratis, lo uso":** gratuito ≠ libre de condiciones; hay que leer la licencia (comercial, atribución, modificación).
2. **Buscar en Google Images y descargar:** casi siempre infringe copyright; usa bancos con licencia explícita.
3. **Olvidar la atribución CC BY:** usar el activo sin creditar al autor incumple la licencia aunque sea "gratis".
4. **Self-hostear tipografías comerciales** sin licencia web: infringe los términos de la foundry.
5. **Usar NC/ND en proyectos comerciales o que modifican el activo:** incompatibilidad directa con la licencia.
6. **No dejar rastro documental:** sin inventario/licencias guardadas, no puedes demostrar la diligencia debida ante una reclamación.

## Resumen

El derecho de autor protege por defecto todo contenido multimedia; usarlo en la web exige contar con permiso (compra, licencia o dominio público). Las **licencias** —especialmente las de **Creative Commons**— definen qué se puede hacer: uso comercial, modificación y atribución. El flujo de **preparación** (adquisición → tratamiento → optimización → exportación por finalidad) debe ir acompañado de un **inventario de activos** con su licencia y atribución, y de una **política de activos** en la guía de estilo. Dominar este marco legal (CE 3.a) cierra el RA3 junto a la Unidad 12, que aporta el tratamiento técnico de formatos e integración (RA4).

## Recursos complementarios

- **Creative Commons — licencias:** https://creativecommons.org/licenses/
- **Guía para elegir una licencia CC:** https://choose.cc.es/ (y https://choosecreativecommons.org/)
- **Unsplash / Pexels / Pixabay (imágenes):** unsplash.com · pexels.com · pixabay.com
- **Freesound (audio, licencias CC):** freesound.org
- **Incompetech (música, Kevin MacLeod, CC BY):** incompetech.com
- **Google Fonts (SIL Open Font License):** fonts.google.com
- **SVG Repo / Heroicons (iconos):** svgrepo.com · heroicons.com
- **Propiedad intelectual — OEPM (España):** https://www.oepm.es
