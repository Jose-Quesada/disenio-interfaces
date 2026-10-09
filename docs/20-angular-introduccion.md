---
icon: lucide/rocket
---

# Unidad 20: Angular — Introducción y Primeros Componentes

## Objetivos de aprendizaje

Al finalizar esta unidad, el alumnado será capaz de instalar y configurar el entorno de desarrollo de Angular utilizando la CLI (Command Line Interface), comprendiendo el rol de cada herramienta del ecosistema (Node.js, npm, Angular CLI). Creará proyectos Angular desde cero e interpretará la estructura de carpetas generada, identificando el propósito de cada directorio y archivo. Comprenderá el concepto de componente como unidad fundamental de construcción de interfaces web, diferenciándolo de los elementos HTML tradicionales. Diseñará templates (plantillas) utilizando la sintaxis de Angular para componer interfaces visuales reutilizables, aplicando los principios de diseño estudiados en unidades anteriores (jerarquía visual, espaciado consistente, tipografía). Aplicará estilos encapsulados a cada componente mediante ViewEncapsulation, comprendiendo cómo esta característica garantiza la homogeneidad y el aislamiento visual de las interfaces. Construirá una interfaz web básica completa (landing page con cabecera, contenido principal y pie) utilizando componentes anidados, verificando su comportamiento en distintos tamaños de viewport. Valorará críticamente Angular frente a otros frameworks (React, Vue) y frente al enfoque de HTML/CSS/Tailwind puro, identificando los contextos donde cada herramienta resulta más adecuada según el tamaño del proyecto, la complejidad de la interfaz y las necesidades de mantenimiento.

## Relación con los Resultados de Aprendizaje

Esta unidad se vincula directamente con el **Resultado de Aprendizaje 2 (RA2)** del módulo profesional 0615 *Diseño de interfaces web* —"Crea interfaces web homogéneos definiendo y aplicando estilos"—, según el currículo oficial (RD 405/2023, BOE; currículo andaluz). El trabajo con Angular permite alcanzar el **criterio de evaluación 2.i**: *"Se han analizado y utilizado tecnologías y frameworks para la creación de interfaces web con un diseño responsive"*, ya que Angular es exactamente una tecnología/framework para la creación de interfaces web. Asimismo, se relaciona con el **CE 2.g** (crear clases de estilos), en cuanto que cada componente Angular genera una clase CSS aislada mediante ViewEncapsulation, y con el **CE 1.e** (RA1): *"Se han utilizado y valorado distintas tecnologías para el diseño de documentos web"*, pues el alumnado compara Angular con los enfoques anteriores (HTML+CSS, Tailwind) valorando cuándo cada uno es más apropiado.

La unidad contribuye también al **RA4** —"Integra contenido multimedia en documentos web valorando su aportación y seleccionando adecuadamente los elementos interactivos"— a través del **CE 4.a**: *"Se han reconocido y analizado las tecnologías relacionadas con la inclusión de contenido multimedia e interactivo"*, ya que Angular proporciona el ecosistema (componentes, directivas, data binding) sobre el que se implementa la interactividad de las interfaces. El alumnado comprende que Angular no es una alternativa a HTML/CSS sino una capa superior que los organiza en unidades reutilizables y reactivas.

!!! note "Nota de encuadre"
    Esta unidad cierra el bloque de «tecnologías y frameworks» del **RA2** (**CE 2.i**), complementando la Unidad 17 (*Tailwind CSS*) y la Unidad 18 (*Preprocesadores*). Mientras Tailwind resuelve la pregunta «¿cómo escribo estilos?», Angular resuelve «¿cómo organizo mi interfaz en piezas reutilizables que reaccionan a los datos?».

## Conocimientos previos

Para abordar esta unidad con soltura, el alumnado debe:

1. Dominar HTML5 semántico (Unidad 7): estructura del DOM, etiquetas de bloque e inline, formularios, atributos ARIA básicos.
2. Manejar CSS a nivel profesional (Unidades 8-11): modelo de caja, Flexbox, Grid, variables CSS, media queries, diseño responsive mobile-first.
3. Haber trabajado con Tailwind CSS (Unidad 17) o preprocesadores (Unidad 18), comprendiendo el concepto de "framework" como sistema de restricciones que acelera el desarrollo.
4. Conocer JavaScript básico: variables (`let`, `const`), funciones, arrays, objetos, métodos de array (`map`, `filter`, `find`), template literals, y la sintaxis ES6+ (clases, import/export).
5. Manejar la terminal: navegación por directorios, ejecución de comandos, lectura de salida de consola.
6. Tener instalado Node.js (versión LTS) y npm en el equipo, comprendiendo qué es un gestor de paquetes y para qué sirve `package.json`.

## Contenidos

1. **Panorama del ecosistema frontend.** ¿Qué es un framework de JavaScript? Diferencias entre librería y framework. Panorama actual: React, Vue, Angular, Svelte. Criterios de elección según contexto (tamaño del equipo, complejidad, curva de aprendizaje, empleo en el sector).

2. **Angular: origen y filosofía.** Creado por Google (2016, reescrito desde cero en TypeScript), arquitectura basada en componentes, enfoque declarativo, inyección de dependencias, sistema de módulos. Angular vs AngularJS (diferencias fundamentales).

3. **Instalación del entorno.** Requisitos: Node.js LTS, npm o pnpm. Instalación global de Angular CLI (`npm install -g @angular/cli`). Verificación de la instalación. Configuración inicial de Git.

4. **Creación de un proyecto.** Comando `ng new` y sus opciones (`--style=scss`, `--routing`, `--ssr`). Estructura generada: `src/app/` (componentes, servicios), `src/assets/`, `angular.json` (configuración del build), `package.json`. El archivo `main.ts` como punto de entrada.

5. **El componente: unidad fundamental.** Definición: un componente es una clase TypeScript + un template HTML + estilos CSS encapsulados. Generación con `ng generate component nombre`. Los cuatro archivos que se crean (`*.component.ts`, `*.component.html`, `*.component.scss`, `*.component.spec.ts`). El decorador `@Component` y sus propiedades: `selector`, `templateUrl`, `styleUrls`, `standalone`.

6. **El template (plantilla).** Sintaxis de Angular en el HTML del componente: interpolación `{{ }}`, propiedad binding `[prop]`, event binding `(evento)`, directivas estructurales `*ngIf` y `*ngFor`, dos-way binding `[(ngModel)]`. Diferencias con HTML puro.

7. **Estilos encapsulados.** ViewEncapsulation (Emulated, ShadowDom, None). Cómo cada componente tiene su propia hoja de estilos que no "fuga" al resto de la aplicación. Implicaciones para el diseño: coherencia visual garantizada por aislamiento. Uso de `::ng-deep` como escape hatch y sus riesgos.

8. **Composición de componentes.** Componentes anidados (un componente dentro del template de otro). Comunicación padre-hijo con `@Input()` y `@Output()`. El concepto de "componente contenedor" vs "componente presentacional". Construcción de una interfaz completa componiendo piezas pequeñas.

9. **Diseño responsive en Angular.** Aplicación de media queries dentro de los estilos del componente. Uso de CSS Grid y Flexbox dentro de templates. Estrategia mobile-first: diseñar el template base para móvil y añadir complejidad con `@media (min-width: ...)`. Verificación con DevTools.

10. **Ejecución y build.** `ng serve` (servidor de desarrollo con hot reload), `ng build` (compilación para producción). El proceso de compilación: TypeScript → JavaScript, SCSS → CSS, templates → código de renderizado. El rol del bundler (esbuild en Angular 17+).

## Desarrollo teórico

### 1. ¿Por qué un framework? De HTML plano a interfaces componibles

Hasta la Unidad 19, el alumnado ha trabajado con una progresión natural: HTML para estructura, CSS para presentación, Tailwind para productividad en estilos, y preprocesadores para abstracción. Este enfoque funciona perfectamente para sitios web estáticos o de contenido (portafolios, blogs, landing pages simples). Sin embargo, cuando la interfaz se convierte en una **aplicación** —con estado que cambia, datos que se actualizan desde un servidor, navegación sin recargar páginas, formularios con validación compleja y decenas de vistas interconectadas— el modelo de "un archivo HTML + un archivo CSS" se vuelve insostenible.

!!! info "Tres conceptos que introduce un framework"
    Un framework de JavaScript como Angular resuelve este problema introduciendo tres conceptos clave:

    - **Componentes** — la interfaz se descompone en **piezas reutilizables** (una tarjeta, un botón, un formulario, un menú) que se componen jerárquicamente como bloques de construcción.
    - **Reactividad** — cuando los datos cambian, la interfaz **se actualiza automáticamente** sin manipular el DOM a mano. El desarrollador declara «cuando X cambia, muestra Y» y el framework se encarga de ejecutarlo.
    - **Estructura impuesta** — el framework define **cómo organizar el código** (dónde van los componentes, cómo se comunican, cómo se gestiona la navegación), eliminando las decisiones arbitrarias que en proyectos grandes generan caos.

Angular es el framework más **«opinionado»** del ecosistema: toma decisiones por ti (arquitectura, patrones de comunicación, gestión de estado, inyección de dependencias). Esto lo hace ideal para **equipos grandes y aplicaciones complejas**, pero impone una **curva de aprendizaje inicial mayor** que React o Vue. En el contexto del módulo de Diseño de Interfaces, Angular es valioso porque enseña al alumnado a pensar en la interfaz como un **sistema de componentes reutilizables**, no como una página plana.

### 2. Instalación y creación del proyecto

El primer paso es verificar que Node.js está instalado:

```bash
node --version   # Debe mostrar v18.x o superior
npm --version    # Debe mostrar 9.x o superior
```

La instalación de Angular CLI es un comando global:

```bash
npm install -g @angular/cli
```

Una vez instalado, la verificación es `ng version`. La creación del proyecto se realiza desde el directorio donde se quiere ubicar:

```bash
ng new mi-app --style=scss --routing --skip-git
```

Las opciones más relevantes:

- **`--style=scss`** — activa SCSS como preprocesador de estilos (relacionado con la Unidad 18).
- **`--routing`** — añade el sistema de enrutamiento desde el inicio.
- **`--skip-git`** — evita inicializar un repositorio Git si ya se trabaja dentro de uno.

La estructura generada es:

```
mi-app/
├── src/
│   ├── app/
│   │   ├── app.component.ts       # Componente raíz (contenedor de toda la app)
│   │   ├── app.component.html     # Su template
│   │   ├── app.component.scss     # Sus estilos
│   │   ├── app.routes.ts          # Definición de rutas
│   │   └── app.config.ts          # Configuración de la aplicación
│   ├── assets/                    # Imágenes, fuentes, JSON
│   ├── styles.scss                # Estilos globales (reset, variables CSS)
│   └── index.html               # HTML base del documento
├── angular.json                 # Configuración del build
├── package.json                 # Dependencias y scripts
└── tsconfig.json               # Configuración de TypeScript
```

El punto de entrada es `src/main.ts`, que importa el componente raíz y lo "arranca" en el elemento `<app-root>` del `index.html`.

### 3. El componente: tres archivos, una unidad

!!! info "Definición: componente Angular"
    Un **componente** es la unidad fundamental de construcción de interfaces en Angular: una **clase TypeScript + un template HTML + estilos CSS encapsulados**. Cada componente Angular está formado por tres archivos que trabajan juntos:

**El archivo TypeScript (`*.component.ts`)** define la lógica y los datos:

```typescript
import { Component } from '@angular/core';

@Component({
  selector: 'app-tarjeta-producto',
  templateUrl: './tarjeta-producto.component.html',
  styleUrls: ['./tarjeta-producto.component.scss'],
  standalone: true,
})
export class TarjetaProductoComponent {
  nombre = 'Cafetera Espresso';
  precio = 89.95;
  descripcion = 'Cafetera de alta presión con molinillo integrado';

  estaEnOferta(): boolean {
    return this.precio < 100;
  }
}
```

**El template (`*.component.html`)** define la estructura visual:

```html
<article class="tarjeta">
  <h2>{{ nombre }}</h2>
  <p class="precio">{{ precio | currency:'EUR' }}</p>
  <p>{{ descripcion }}</p>
  @if (estaEnOferta()) {
    <span class="badge">Oferta</span>
  }
</article>
```

**Los estilos (`*.component.scss`)** definen la presentación, encapsulados:

```scss
.tarjeta {
  background: #ffffff;
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  transition: transform 0.2s ease, box-shadow 0.2s ease;

  &:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
  }
}

.precio {
  font-size: 1.75rem;
  font-weight: 700;
  color: #1a202c;
}

.badge {
  display: inline-block;
  background: #48bb78;
  color: white;
  font-size: 0.75rem;
  font-weight: 600;
  padding: 0.25rem 0.75rem;
  border-radius: 20px;
}
```

El decorador `@Component` es lo que **registra** el componente en Angular. Sus propiedades principales:

| Propiedad | Qué define |
|-----------|------------|
| `selector` | la etiqueta HTML con la que se usará en otros templates (`<app-tarjeta-producto>`) |
| `templateUrl` | la ruta del archivo de template (`*.component.html`) |
| `styleUrls` | la ruta de los estilos encapsulados (`*.component.scss`) |
| `standalone` | si el componente puede importarse **directamente** donde se necesite |

La propiedad `standalone: true` (desde **Angular 15**) indica que el componente **no necesita pertenecer a un módulo clásico**.

### 4. ViewEncapsulation: aislamiento visual por diseño

!!! info "Definición: encapsulamiento de vistas"
    Una de las características más relevantes de Angular para el diseño de interfaces es el **encapsulamiento de vistas** (*ViewEncapsulation*). Cuando defines estilos en `tarjeta-producto.component.scss`, esos estilos **solo afectan al interior de ese componente**. La clase `.tarjeta` **no «fuga»** a otros componentes ni se ve afectada por estilos globales (salvo los definidos en `styles.scss`).

!!! tip "Implicación para el diseño: caja negra predecible"
    Cada componente es una «caja negra» **visualmente predecible**. Si el diseñador define que todas las tarjetas tienen `border-radius: 12px` y un `box-shadow` específico, ese estilo está **garantizado** sin importar dónde se use la tarjeta en la aplicación. Se elimina el problema clásico del CSS donde una regla global puede romper un componente específico por especificidad.

El encapsulamiento se logra mediante atributos únicos generados automáticamente (algo como `_ngcontent-abc123`) que se añaden a las etiquetas HTML y a los selectores CSS, haciendo que cada regla solo coincida con los elementos de su propio componente.

### 5. Composición: construyendo la interfaz pieza a pieza

La filosofía de Angular es **componer** interfaces a partir de componentes pequeños y especializados, no escribir una página monolítica. Una landing page típica se descompone así:

```
AppComponent (contenedor raíz)
├── HeaderComponent (logo, navegación, CTA)
├── HeroComponent (titular principal, subtítulo, botón)
├── FeaturesComponent (grid de características)
│   └── FeatureCardComponent (repetido N veces con *ngFor)
├── TestimonialsComponent (slider de opiniones)
│   └── TestimonialCardComponent
├── PricingComponent (tarifas)
│   └── PricingCardComponent (repetido 3 veces)
└── FooterComponent (enlaces, redes sociales, legal)
```

Cada componente es responsable de su propio HTML, CSS y lógica. La comunicación entre ellos se realiza mediante `@Input()` (el padre pasa datos al hijo) y `@Output()` (el hijo emite eventos al padre).

!!! tip "Patrón de comunicación padre-hijo"
    **Los datos fluyen hacia abajo, los eventos fluyen hacia arriba.** Este patrón mantiene la arquitectura **predecible** y facilita el mantenimiento.

### 6. Diseño responsive dentro del componente

El diseño responsive en Angular se aplica exactamente igual que en CSS puro: con media queries dentro de los estilos del componente. La diferencia es que esas media queries están encapsuladas: solo afectan a ese componente.

```scss
// feature-card.component.scss
.tarjeta {
  padding: 1rem;
  text-align: center;

  @media (min-width: 768px) {
    padding: 2rem;
    text-align: left;
  }

  @media (min-width: 1024px) {
    flex: 1;
    min-width: 280px;
  }
}
```

En el template, se puede condicionar la estructura visual según el viewport usando CSS Grid o Flexbox con `flex-wrap`, o bien usar directivas para mostrar/ocultar elementos:

```html
<!-- Menú completo en escritorio, hamburguesa en móvil -->
<nav class="nav-desktop">
  @for (item of menuItems; track item.label) {
    <a [href]="item.url">{{ item.label }}</a>
  }
</nav>
<button class="btn-hamburguesa" (click)="toggleMenu()">☰</button>
```

!!! tip "Estrategia mobile-first en Angular"
    La estrategia **mobile-first** se mantiene: los estilos base son para **móvil**, y las *media queries* `min-width` añaden complejidad progresivamente.

## Ejemplos guiados

### Ejemplo 1: Crear un proyecto y su primer componente

!!! example "Contexto pedagógico"
    El alumnado ejecuta por primera vez el **flujo completo de creación de un proyecto Angular**, generando un componente y observando cómo se renderiza en el navegador. Se enfatiza la **estructura generada** y el rol de cada archivo.

**Paso 1 — Crear el proyecto:**

```bash
mkdir E:\proyectos\angular-daw
cd E:\proyectos\angular-daw
ng new tienda-web --style=scss --routing --skip-git
cd tienda-web
```

**Paso 2 — Generar un componente de cabecera:**

```bash
ng generate component header
```

Esto crea en `src/app/header/`:

- `header.component.ts`
- `header.component.html`
- `header.component.scss`
- `header.component.spec.ts`

**Paso 3 — Escribir el template del header:**

```html
<!-- src/app/header/header.component.html -->
<header class="cabecera">
  <div class="contenedor">
    <a href="/" class="logo">MiTienda</a>
    <nav class="navegacion">
      @for (enlace of enlaces; track enlace.url) {
        <a [href]="enlace.url" class="enlace">{{ enlace.texto }}</a>
      }
    </nav>
    <button class="btn-carrito">🛒 <span class="contador">3</span></button>
  </div>
</header>
```

**Paso 4 — Definir los datos en el componente:**

```typescript
// src/app/header/header.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss'],
  standalone: true,
})
export class HeaderComponent {
  enlaces = [
    { texto: 'Inicio', url: '/' },
    { texto: 'Productos', url: '/productos' },
    { texto: 'Ofertas', url: '/ofertas' },
    { texto: 'Contacto', url: '/contacto' },
  ];
}
```

**Paso 5 — Estilizar con SCSS encapsulado:**

```scss
// src/app/header/header.component.scss
.cabecera {
  background: #ffffff;
  border-bottom: 1px solid #e2e8f0;
  position: sticky;
  top: 0;
  z-index: 100;
}

.contenedor {
  max-width: 1200px;
  margin: 0 auto;
  padding: 1rem 2rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 2rem;
}

.logo {
  font-size: 1.5rem;
  font-weight: 800;
  color: #1a202c;
  text-decoration: none;
}

.navegacion {
  display: flex;
  gap: 1.5rem;
}

.enlace {
  color: #4a5568;
  text-decoration: none;
  font-size: 0.95rem;
  font-weight: 500;
  transition: color 0.2s ease;

  &:hover {
    color: #667eea;
  }
}

.btn-carrito {
  position: relative;
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  padding: 0.5rem;
}

.contador {
  position: absolute;
  top: 0;
  right: 0;
  background: #667eea;
  color: white;
  font-size: 0.65rem;
  font-weight: 700;
  width: 18px;
  height: 18px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}

// Responsive: ocultar navegación en móvil
@media (max-width: 767px) {
  .navegacion {
    display: none;
  }
}
```

**Paso 6 — Usar el componente en el componente raíz:**

```html
<!-- src/app/app.component.html -->
<app-header />
<main class="contenido">
  <h1>Bienvenido a MiTienda</h1>
  <p>Los mejores productos al mejor precio.</p>
</main>
```

```typescript
// src/app/app.component.ts
import { Component } from '@angular/core';
import { HeaderComponent } from './header/header.component';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
  standalone: true,
  imports: [HeaderComponent],
})
export class AppComponent {}
```

**Paso 7 — Ejecutar y verificar:**

```bash
ng serve
```

!!! tip "Verificación en el navegador"
    Navegar a `http://localhost:4200`. Se observa la cabecera con logo, navegación y botón de carrito. **Reducir el viewport por debajo de 768 px** y verificar que la navegación se oculta (*responsive*). Inspeccionar el DOM con DevTools para ver los atributos `_ngcontent-*` que garantizan el encapsulamiento.

### Ejemplo 2: Componente reutilizable de tarjeta con data binding básico

!!! example "Contexto pedagógico"
    Se demuestra cómo un mismo componente se **repite con datos diferentes** usando `@for`, y cómo las propiedades del componente se muestran mediante **interpolación**. Se aplica la **ley de semejanza** (Unidad 1): todas las tarjetas comparten estructura visual, pero el contenido varía.

```typescript
// src/app/productos/producto-card.component.ts
import { Component, Input } from '@angular/core';

export interface Producto {
  nombre: string;
  precio: number;
  imagen: string;
  categoria: string;
}

@Component({
  selector: 'app-producto-card',
  templateUrl: './producto-card.component.html',
  styleUrls: ['./producto-card.component.scss'],
  standalone: true,
})
export class ProductoCardComponent {
  @Input() producto!: Producto;
}
```

```html
<!-- src/app/productos/producto-card.component.html -->
<article class="tarjeta-producto">
  <div class="imagen-contenedor">
    <img [src]="producto.imagen" [alt]="producto.nombre" loading="lazy">
    @if (producto.categoria === 'oferta') {
      <span class="etiqueta-oferta">Oferta</span>
    }
  </div>
  <div class="info">
    <h3>{{ producto.nombre }}</h3>
    <p class="precio">{{ producto.precio | number:'1.2-2' }} €</p>
    <button class="btn-anadir">Añadir al carrito</button>
  </div>
</article>
```

```scss
// src/app/productos/producto-card.component.scss
.tarjeta-producto {
  background: #ffffff;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
  transition: transform 0.2s ease, box-shadow 0.2s ease;

  &:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
  }
}

.imagen-contenedor {
  position: relative;
  aspect-ratio: 4 / 3;
  overflow: hidden;

  img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.3s ease;
  }

  &:hover img {
    transform: scale(1.05);
  }
}

.etiqueta-oferta {
  position: absolute;
  top: 12px;
  left: 12px;
  background: #e53e3e;
  color: white;
  font-size: 0.7rem;
  font-weight: 700;
  padding: 0.3rem 0.6rem;
  border-radius: 4px;
  text-transform: uppercase;
}

.info {
  padding: 1rem 1.25rem 1.5rem;
}

h3 {
  font-size: 1rem;
  font-weight: 600;
  color: #1a202c;
  margin-bottom: 0.5rem;
}

.precio {
  font-size: 1.25rem;
  font-weight: 700;
  color: #667eea;
  margin-bottom: 1rem;
}

.btn-anadir {
  width: 100%;
  padding: 0.7rem;
  background: #667eea;
  color: white;
  border: none;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.2s ease;

  &:hover {
    background: #5a67d8;
  }
}
```

```typescript
// src/app/productos/productos.component.ts
import { Component } from '@angular/core';
import { ProductoCardComponent, Producto } from './producto-card.component';

@Component({
  selector: 'app-productos',
  templateUrl: './productos.component.html',
  standalone: true,
  imports: [ProductoCardComponent],
})
export class ProductosComponent {
  productos: Producto[] = [
    { nombre: 'Cafetera Espresso Pro', precio: 89.95, imagen: '/assets/cafetera.jpg', categoria: 'oferta' },
    { nombre: 'Tetera Eléctrica Smart', precio: 45.00, imagen: '/assets/tetera.jpg', categoria: 'cocina' },
    { nombre: 'Batidora Profesional', precio: 129.99, imagen: '/assets/batidora.jpg', categoria: 'cocina' },
    { nombre: 'Tostadora Dual', precio: 34.50, imagen: '/assets/tostadora.jpg', categoria: 'oferta' },
  ];
}
```

```html
<!-- src/app/productos/productos.component.html -->
<section class="seccion-productos">
  <h2>Nuestros productos</h2>
  <div class="grid-productos">
    @for (producto of productos; track producto.nombre) {
      <app-producto-card [producto]="producto" />
    }
  </div>
</section>
```

```scss
// src/app/productos/productos.component.scss
.seccion-productos {
  max-width: 1200px;
  margin: 0 auto;
  padding: 3rem 2rem;

  h2 {
    font-size: 2rem;
    font-weight: 800;
    color: #1a202c;
    margin-bottom: 2rem;
    text-align: center;
  }
}

.grid-productos {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1.5rem;

  @media (min-width: 640px) {
    grid-template-columns: repeat(2, 1fr);
  }

  @media (min-width: 1024px) {
    grid-template-columns: repeat(4, 1fr);
  }
}
```

!!! note "Explicación del resultado"
    Al ejecutar `ng serve`, se observa una **cuadrícula de tarjetas de producto** que se adapta al *viewport* (**1 columna** en móvil, **2** en tablet, **4** en escritorio). Cada tarjeta es el **mismo componente** reutilizado con datos diferentes. La etiqueta *«Oferta»* solo aparece en los productos cuya categoría es `oferta` (directiva `@if`). El *pipe* `number` formatea el precio con **dos decimales**. Al pasar el cursor sobre una tarjeta, se eleva y la imagen hace *zoom* sutil.

## Actividades de práctica

1. **Proyecto guiado:** Crear un proyecto Angular llamado `mi-portfolio` con SCSS. Generar los componentes `header`, `hero`, `proyectos`, `sobre-mi` y `footer`. Componerlos en el `AppComponent`. Estilizar cada uno con SCSS encapsulado, aplicando una paleta de colores coherente (máximo 3 colores) y una escala tipográfica basada en rem. Verificar que el diseño es responsive en tres tamaños: 375px, 768px y 1200px.

2. **Componente reutilizable:** Crear un componente `tarjeta-skill` que muestre el nombre de una tecnología (ej: "Angular", "TypeScript", "SCSS") con un nivel de dominio (barra de progreso visual). Usarlo en un componente `skills` mediante `@for` iterando sobre un array de objetos. Aplicar la ley de semejanza: todas las tarjetas deben ser visualmente homogéneas.

3. **Comparativa:** Tomar la landing page construida con Tailwind en la Unidad 17 y reimplementarla usando componentes Angular. Documentar en un informe breve (una página) las ventajas y desventajas de cada enfoque para ese caso concreto: ¿dónde gana Angular? ¿Dónde gana Tailwind puro? ¿Cuándo usarías uno u otro en un proyecto real?

4. **Accesibilidad:** Añadir atributos ARIA apropiados a los componentes creados (`role`, `aria-label`, `aria-expanded` en el menú hamburguesa). Verificar con el auditor de accesibilidad de Chrome DevTools que no hay errores. Relacionar con la Unidad 14 (Accesibilidad web) y el RA5.
