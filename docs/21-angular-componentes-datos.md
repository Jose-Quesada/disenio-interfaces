---
icon: lucide/blocks
---

# Unidad 21: Angular — Data Binding, Directivas y Pipes

## Objetivos de aprendizaje

Al finalizar esta unidad, el alumnado será capaz de aplicar los tres tipos de data binding de Angular (interpolación, property binding y event binding) para conectar los datos del componente con la interfaz visual, comprendiendo el flujo unidireccional de información. Manejará las directivas estructurales `@if` y `@for` para condicionar la presencia de elementos en el DOM y repetir componentes sobre colecciones de datos, eliminando la necesidad de manipular HTML manualmente. Utilizará pipes (tuberías) para transformar datos en el template sin modificar el estado del componente: formato de números, fechas, moneda, capitalización de texto y búsqueda de texto. Diseñará interfaces interactivas donde el usuario modifica datos a través de eventos (clics, teclas, cambios de input) y la interfaz se actualiza automáticamente mediante two-way binding. Aplicará los principios de usabilidad estudiados en la Unidad 15 al diseñar estados visuales (cargando, vacío, error, éxito) que comunican claramente el estado de la aplicación a la persona usuaria. Construirá una interfaz completa tipo "lista de tareas" o "catálogo de productos" donde se combinan todos los mecanismos de binding y directivas para crear una experiencia interactiva coherente.

## Relación con los Resultados de Aprendizaje

Esta unidad se vincula directamente con el **Resultado de Aprendizaje 4 (RA4)** del módulo profesional 0615 *Diseño de interfaces web* —"Integra contenido multimedia en documentos web valorando su aportación y seleccionando adecuadamente los elementos interactivos"—. En concreto, permite alcanzar:

- **CE 4.a**: *"Se han reconocido y analizado las tecnologías relacionadas con la inclusión de contenido multimedia e interactivo."* Angular es una de esas tecnologías: sus directivas, pipes y sistema de binding son el mecanismo por el que se añade interactividad a los elementos del documento web.
- **CE 4.f**: *"Se ha añadido interactividad a elementos de un documento web."* El data binding y las directivas estructurales son la forma nativa de Angular de hacer que los elementos respondan a acciones del usuario (cambiar estado, mostrar/ocultar contenido, actualizar valores).
- **CE 4.g**: *"Se ha verificado el funcionamiento de los elementos multimedia e interactivos en distintos navegadores y dispositivos."* Se verifica mediante `ng serve` y DevTools en diferentes viewports.

Asimismo, se relaciona con el **RA2** (CE 2.i: "Se han analizado y utilizado tecnologías y frameworks para la creación de interfaces web") y con el **RA6** —"Desarrolla interfaces web amigables analizando y aplicando las pautas de usabilidad"— a través del diseño de estados visuales claros (skeleton loaders, mensajes de vacío, feedback de error) que mejoran la experiencia de usuario.

!!! note "Núcleo práctico del RA4"
    Esta unidad es el núcleo práctico del **RA4** en Angular. Mientras la Unidad 20 enseñó a "montar las piezas" (componentes, templates, estilos), esta unidad enseña a "darles vida" (datos que fluyen, condiciones que cambian, eventos que reaccionan).

## Conocimientos previos

Para abordar esta unidad con soltura, el alumnado debe:

1. Haber completado la Unidad 20: crear un proyecto Angular, generar componentes, entender la estructura de los tres archivos del componente y ejecutar `ng serve`.
2. Dominar JavaScript a nivel intermedio: arrays (métodos `map`, `filter`, `find`, `reduce`), objetos, funciones flecha, desestructuración, template literals, y el concepto de "referencia" vs "valor".
3. Comprender TypeScript básico: tipos primitivos (`string`, `number`, `boolean`, `any`), interfaces, tipos union, y la diferencia entre `let`/`const`.
4. Conocer HTML5 semántico y CSS (Unidades 7-11) para interpretar los templates que se generan.
5. Entender el concepto de "estado" en una aplicación: qué datos cambian con el tiempo y cómo eso afecta a lo que se muestra en pantalla.

## Contenidos

1. **Interpolación de propiedades.** Sintaxis `{{ expresión }}`. Qué expresiones son válidas (variables, propiedades, métodos, operaciones aritméticas simples). Limitaciones: no se pueden usar declaraciones (`let`, `const`), bucles ni condicionales. El contexto de evaluación y el warning "ExpressionChangedAfterItWasChecked".

2. **Property binding.** Sintaxis `[propiedad]="expresión"`. Diferencia con la interpolación: permite bindar a propiedades que no son texto (atributos HTML como `src`, `href`, `class`, `style`, `disabled`, `hidden`). Ejemplos: `[src]="urlImagen"`, `[class.activo]="estaSeleccionado"`, `[style.width.px]="ancho"`.

3. **Event binding.** Sintaxis `(evento)="expresión"`. Eventos comunes: `(click)`, `(input)`, `(change)`, `(keyup)`, `(submit)`, `(mouseenter)`, `(mouseleave)`. La variable de evento `$event` y sus propiedades (`$event.target.value`, `$event.key`, `$event.preventDefault()`). Diferencia entre eventos nativos del DOM y eventos personalizados de componentes (`@Output`).

4. **Two-way binding.** Sintaxis `[(propiedad)]="variable"` como azúcar sintáctico de property + event binding. El caso especial `ngModel` para inputs de formulario: `<input [(ngModel)]="nombre">`. Flujo: el usuario escribe → el valor se actualiza en la variable → la interfaz se re-renderiza con el nuevo valor.

5. **Directiva estructural @if.** Sintaxis `@if (condición) { ... } @else if (otraCond) { ... } @else { ... }`. Diferencia con `[hidden]` y `*ngIf` (versión antigua). Cuándo usar `@if` (elemento no existe en el DOM) frente a `[style.display]` (elemento existe pero está oculto). Implicaciones para accesibilidad: un elemento eliminado del DOM no es anunciado por lectores de pantalla.

6. **Directiva estructural @for.** Sintaxis `@for (item of lista; track item.id) { ... }`. El contexto de la directiva: `$implicit` (el elemento actual), `first`, `last`, `even`, `odd`, `count`, `index`. La cláusula `track` y su importancia para el rendimiento (evita re-renderizado innecesario). Bucles anidados. Iterar sobre objetos con `@for (valor, clave of obj; track clave)`.

7. **Pipes integrados.** `date` (formato de fechas: `'medium'`, `'short'`, `'EEEE, d MMMM yyyy'`), `currency` (simbolo, código ISO, formato de decimales), `number` (decimales, agrupación), `uppercase`, `lowercase`, `titlecase`, `json`, `slice`. Sintaxis: `{{ valor | pipe }}` y con argumentos: `{{ precio | currency:'EUR':'1.2-2' }}`.

8. **Pipes personalizados.** Crear una clase que implemente `PipeTransform<T, R>`. Decorador `@Pipe({ name: 'nombre', standalone: true })`. Ejemplos prácticos: pipe de búsqueda (filtrar texto), pipe de pluralización ("3 productos" vs "1 producto"), pipe de enmascarado (mostrar solo últimos 4 dígitos de un número de tarjeta).

9. **Estados visuales y feedback.** Patrones de UI: estado vacío (lista sin elementos → mensaje + CTA), estado de carga (skeleton screens, spinners), estado de error (mensaje + retry), estado de éxito (toast, checkmark). Implementación con `@if` condicionando la vista según el estado del componente. Relación con las pautas de usabilidad (RA6): la interfaz siempre debe comunicar su estado actual.

10. **Comunicación entre componentes avanzada.** `@Input()` y `@Output()` con `EventEmitter`. El patrón "componente presentacional" (recibe datos por input, emite eventos por output, no tiene estado propio). Servicios inyectados como alternativa para comunicación entre componentes no relacionados (hermano, tío-nieto).

## Desarrollo teórico

### 1. Data binding: el motor de la reactividad

!!! info "Definición"
    El concepto central de Angular es que **la interfaz es una función de los datos**. No se manipula el DOM directamente ("cambia el texto del párrafo a X"); se declaran las relaciones entre datos y elementos, y Angular se encarga de actualizar el DOM cuando los datos cambian.

Existen tres formas de establecer esa relación:

- **Interpolación (`{{ }}`):** la más simple. Se usa para insertar texto en el template. `{{ nombre }}` renderiza el valor de la propiedad `nombre`. También acepta expresiones simples: `{{ precio * iva + precio }}`, `{{ estaActivo ? 'Sí' : 'No' }}`.
- **Property binding (`\[prop\]`):** cuando la propiedad a bindar no es texto. El atributo `src` de una imagen, la clase CSS de un elemento, el estilo inline, el estado `disabled` de un botón. La sintaxis con corchetes `[src]="url"` es equivalente a `src="{{ url }}"` pero más explícita y permite valores booleanos (`[disabled]="!estaHabilitado"`).
- **Event binding (`(evento)`):** la forma inversa: el usuario hace algo en el DOM y se ejecuta código TypeScript. `(click)="incrementar()"`, `(input)="onCambio($event)"`. La variable `$event` contiene el objeto de evento nativo del navegador, de donde se extrae lo necesario (`$event.target.value` para inputs).
- **Two-way binding (`\[(prop)\]`):** combina los dos anteriores en una sintaxis compacta. `[(ngModel)]="nombre"` es equivalente a `[ngModel]="nombre" (ngModelChange)="nombre = $event"`. Es el mecanismo por el que un input de formulario "se mantiene en sincronía" con la variable del componente: el usuario escribe → Angular actualiza la variable → si algún otro elemento depende de esa variable, también se actualiza.

!!! warning "Limitaciones de la interpolación"
    La restricción clave es que no se puede "declarar" nada dentro: no `let x = 5`, no `for`, no `if`. Solo se "lee" y se "calcula".

### 2. Directivas estructurales: condicionar y repetir

!!! info "Definición"
    Las directivas estructurales modifican el **DOM** (añaden o eliminan elementos), a diferencia de las directivas de propiedad que solo cambian atributos.

**`@if`:** elimina del DOM todo el bloque cuando la condición es falsa.

!!! warning "Accesibilidad: @if frente a display: none"
    Esto tiene implicaciones importantes para accesibilidad: un elemento eliminado no existe para lectores de pantalla, mientras que uno con `display: none` sigue en el árbol (aunque también se ignora). Para elementos que se muestran/ocultan frecuentemente y deben mantener su estado (un formulario parcialmente completado), puede preferirse `[hidden]` o `@if` con cuidado.

```html
@if (cargaEnCurso) {
  <div class="skeleton" aria-busy="true">
    <div class="skeleton-line"></div>
    <div class="skeleton-line corto"></div>
  </div>
} @else if (hayError) {
  <div class="mensaje-error" role="alert">
    <p>No se pudieron cargar los datos.</p>
    <button (click)="reintentar()">Reintentar</button>
  </div>
} @else {
  @for (item de items; track item.id) {
    <app-item-card [item]="item" />
  }
}
```

**`@for`:** repite un bloque para cada elemento de una colección.

!!! tip "Usa siempre la cláusula track"
    La cláusula `track` es **crítica**: le dice a Angular "cómo identificar cada elemento" para optimizar el diffing. Si se itera sobre un array de objetos, `track item.id` evita re-crear los componentes cuando el array se reordena. Sin `track`, Angular usa la identidad por referencia y puede regenerar todo el DOM en cada cambio.

```html
@for (producto of productos; track producto.id; let i = index; let first = first; let last = last) {
  <app-producto-card [producto]="producto" [esPrimero]="first" />
}
@if (productos.length === 0) {
  <div class="estado-vacio">
    <p>No hay productos en esta categoría.</p>
    <button (click)="limpiarFiltros()">Ver todos</button>
  </div>
}
```

### 3. Pipes: transformar sin mutar

!!! info "Qué es un pipe"
    Un pipe es una función pura que recibe un valor y devuelve otro, transformándolo para su presentación. Se aplica directamente en el template sin tocar el componente TypeScript. Esto mantiene la lógica de presentación separada de la lógica de datos.

Los pipes integrados más usados en diseño de interfaces:

| Pipe | Uso en template | Resultado |
| ---- | --------------- | --------- |
| `date` | `{{ fecha }}` con `date:'EEEE d MMMM yyyy'` | "lunes 15 septiembre 2026". Formato `'medium'` → "15/9/26, 14:30:00" |
| `currency` | `{{ precio }}` con `currency:'EUR':'1.2-2'` | "89,95 €". El segundo argumento es el formato de decimales (mín-máx) |
| `number` | `{{ visitas }}` con `number:'1.0-0'` | "1.234" (con agrupación de miles) |
| `uppercase` / `lowercase` / `titlecase` | transformaciones directas de texto | para etiquetas, badges y encabezados |
| `slice` | `{{ descripcion }}` con `slice:0:80:'...'` | trunca a 80 caracteres con elipsis |

Para crear un pipe personalizado:

```typescript
import { Pipe, PipeTransform } from '@angular/core';

@Pipe({ name: 'pluralizar', standalone: true })
export class PluralizarPipe implements PipeTransform<string, string> {
  transform(valor: string, singular: string, plural?: string): string {
    const n = parseInt(valor, 10);
    const sufijo = n === 1 ? singular : (plural ?? singular + 's');
    return `${n} ${sufijo}`;
  }
}
```

Uso en template: `{{ items.length | pluralizar:'producto' }}` → "3 productos" o "1 producto".

### 4. Estados visuales: la interfaz siempre comunica

!!! tip "La interfaz siempre comunica"
    Una de las competencias más importantes del diseño de interfaces es que **la persona usuaria siempre sepa qué está pasando**. Angular facilita esto mediante patrones claros.

**Estado vacío:** cuando una lista no tiene elementos, no se muestra un espacio en blanco. Se muestra un mensaje descriptivo y una acción sugerida (CTA).

```html
@if (tareas.length === 0) {
  <div class="vacio">
    <svg class="icono-vacio" width="64" height="64" aria-hidden="true">
      <!-- icono SVG -->
    </svg>
    <h3>No tienes tareas pendientes</h3>
    <p>Añade tu primera tarea para empezar a organizar tu día.</p>
    <button class="btn-primario" (click)="abrirModalNuevaTarea()">Crear tarea</button>
  </div>
}
```

**Estado de carga:** mientras se obtienen datos, se muestra un skeleton (esqueleto) que imita la estructura visual del contenido final. Esto reduce la ansiedad perceptual frente a una pantalla en blanco o un spinner genérico.

```html
@if (cargando) {
  <div class="skeleton-lista" aria-busy="true" aria-label="Cargando tareas">
    @for (i of [1,2,3,4]; track $index) {
      <div class="skeleton-item">
        <div class="skeleton-circulo"></div>
        <div class="skeleton-texto">
          <div class="linea larga"></div>
          <div class="linea corta"></div>
        </div>
      </div>
    }
  </div>
}
```

**Estado de error:** se muestra el mensaje del error de forma comprensible (no "500 Internal Server Error" sino "No pudimos conectar. Comprueba tu conexión a internet.") y una acción de reintentar. El atributo `role="alert"` garantiza que los lectores de pantalla anuncien el cambio.

**Estado de éxito:** feedback inmediato tras una acción (tarea añadida, formulario enviado). Un toast o un checkmark temporal confirma la operación sin interrumpir el flujo.

### 5. @Input y @Output: la comunicación padre-hijo

Cuando un componente necesita recibir datos de su padre, se usan `@Input()`:

```typescript
@Component({ ... })
export class ProgresoComponent {
  @Input() valor = 0;        // Por defecto 0 si no se pasa
  @Input() maximo = 100;
  @Input() etiqueta = '';
}
```

```html
<!-- En el padre -->
<app-progreso [valor]="tareasCompletadas" [maximo]="tareasTotales" [etiqueta]="'Progreso del proyecto'" />
```

Cuando el hijo necesita notificar algo al padre, se usa `@Output()` con un `EventEmitter`:

```typescript
@Component({ ... })
export class BuscadorComponent {
  @Output() onBuscar = new EventEmitter<string>();

  buscar(termino: string) {
    this.onBuscar.emit(termino);
  }
}
```

```html
<!-- En el padre -->
<app-buscador (onBuscar)="filtrarProductos($event)" />
```

!!! tip "Datos abajo, eventos arriba"
    Este patrón "datos abajo, eventos arriba" mantiene la arquitectura predecible: el padre controla el estado, los hijos son presentacionales y reactivos.

## Ejemplos guiados

### Ejemplo 1: Lista de tareas interactiva con todos los mecanismos de binding

!!! example "Contexto pedagógico"
    Se construye una lista de tareas (todo list) que integra interpolación, property binding, event binding, two-way binding, @if, @for y un pipe personalizado. Es el ejercicio "hola mundo" del desarrollo frontend interactivo, pero elevado a nivel de diseño de interfaces con estados visuales completos.

```typescript
// src/app/tareas/tareas.component.ts
import { Component } from '@angular/core';

interface Tarea {
  id: number;
  texto: string;
  completada: boolean;
  creada: Date;
}

@Component({
  selector: 'app-tareas',
  templateUrl: './tareas.component.html',
  styleUrls: ['./tareas.component.scss'],
  standalone: true,
})
export class TareasComponent {
  tareas: Tarea[] = [
    { id: 1, texto: 'Diseñar wireframes de la app', completada: true, creada: new Date('2026-09-20') },
    { id: 2, texto: 'Implementar componente de login', completada: false, creada: new Date('2026-09-21') },
    { id: 3, texto: 'Revisar accesibilidad WCAG', completada: false, creada: new Date('2026-09-22') },
  ];
  nuevaTarea = '';
  filtro = 'todas'; // 'todas' | 'pendientes' | 'completadas'

  get tareasFiltradas(): Tarea[] {
    switch (this.filtro) {
      case 'pendientes': return this.tareas.filter(t => !t.completada);
      case 'completadas': return this.tareas.filter(t => t.completada);
      default: return this.tareas;
    }
  }

  get pendientes(): number {
    return this.tareas.filter(t => !t.completada).length;
  }

  addTarea(): void {
    if (this.nuevaTarea.trim()) {
      this.tareas.push({
        id: Date.now(),
        texto: this.nuevaTarea.trim(),
        completada: false,
        creada: new Date(),
      });
      this.nuevaTarea = '';
    }
  }

  toggle(tarea: Tarea): void {
    tarea.completada = !tarea.completada;
  }

  eliminar(id: number): void {
    this.tareas = this.tareas.filter(t => t.id !== id);
  }
}
```

```html
<!-- src/app/tareas/tareas.component.html -->
<section class="panel-tareas">
  <header class="cabecera-panel">
    <h1>Mis tareas</h1>
    @if (pendientes > 0) {
      <span class="badge">{{ pendientes }} pendientes</span>
    } @else if (tareas.length > 0) {
      <span class="badge exito">¡Todo hecho!</span>
    }
  </header>

  <!-- Formulario de nueva tarea -->
  <form class="formulario-nueva" (submit)="addTarea()">
    <input
      type="text"
      placeholder="Añadir nueva tarea..."
      [(ngModel)]="nuevaTarea"
      name="nuevaTarea"
      aria-label="Texto de la nueva tarea"
    >
    <button type="submit" [disabled]="!nuevaTarea.trim()" aria-label="Añadir tarea">+</button>
  </form>

  <!-- Filtros -->
  <div class="filtros" role="tablist" aria-label="Filtrar tareas">
    @for (f of ['todas', 'pendientes', 'completadas']; track f) {
      <button
        [class.activo]="filtro === f"
        (click)="filtro = f"
        role="tab"
        [attr.aria-selected]="filtro === f"
      >
        {{ f }}
      </button>
    }
  </div>

  <!-- Lista de tareas -->
  @if (tareasFiltradas.length > 0) {
    <ul class="lista-tareas" role="list">
      @for (tarea of tareasFiltradas; track tarea.id) {
        <li class="item-tarea" [class.completada]="tarea.completada">
          <input
            type="checkbox"
            [checked]="tarea.completada"
            (change)="toggle(tarea)"
            [id]="'tarea-' + tarea.id"
            [attr.aria-label]="'Marcar ' + tarea.texto + ' como ' + (tarea.completada ? 'pendiente' : 'completada')"
          >
          <label [for]="'tarea-' + tarea.id">
            {{ tarea.texto }}
            <small class="fecha">{{ tarea.creada | date:'d MMM' }}</small>
          </label>
          <button class="btn-eliminar" (click)="eliminar(tarea.id)" aria-label="Eliminar tarea">✕</button>
        </li>
      }
    </ul>
  } @else {
    <div class="estado-vacio">
      @if (filtro === 'todas') {
        <p>No tienes tareas. ¡Añade la primera!</p>
      } @else if (filtro === 'pendientes') {
        <p>No hay tareas pendientes. ¡Buen trabajo!</p>
      } @else {
        <p>Aún no has completado ninguna tarea.</p>
      }
    </div>
  }
</section>
```

```scss
// src/app/tareas/tareas.component.scss
.panel-tareas {
  max-width: 560px;
  margin: 2rem auto;
  background: #ffffff;
  border-radius: 16px;
  box-shadow: 0 4px 24px rgba(0, 0, 0, 0.08);
  padding: 2rem;
}

.cabecera-panel {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 1.5rem;

  h1 {
    font-size: 1.5rem;
    font-weight: 800;
    color: #1a202c;
  }
}

.badge {
  background: #667eea;
  color: white;
  font-size: 0.75rem;
  font-weight: 700;
  padding: 0.3rem 0.75rem;
  border-radius: 20px;

  &.exito {
    background: #48bb78;
  }
}

.formulario-nueva {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 1.5rem;

  input {
    flex: 1;
    padding: 0.75rem 1rem;
    border: 2px solid #e2e8f0;
    border-radius: 8px;
    font-size: 0.95rem;
    transition: border-color 0.2s ease;

    &:focus {
      outline: none;
      border-color: #667eea;
    }
  }

  button {
    width: 48px;
    height: 48px;
    background: #667eea;
    color: white;
    border: none;
    border-radius: 8px;
    font-size: 1.5rem;
    cursor: pointer;
    transition: background 0.2s ease, transform 0.1s ease;

    &:hover:not(:disabled) {
      background: #5a67d8;
      transform: scale(1.05);
    }

    &:disabled {
      opacity: 0.4;
      cursor: not-allowed;
    }
  }
}

.filtros {
  display: flex;
  gap: 0.25rem;
  margin-bottom: 1.5rem;
  background: #f7fafc;
  border-radius: 8px;
  padding: 0.25rem;

  button {
    flex: 1;
    padding: 0.5rem;
    border: none;
    background: transparent;
    border-radius: 6px;
    font-size: 0.85rem;
    font-weight: 500;
    color: #718096;
    cursor: pointer;
    text-transform: capitalize;
    transition: all 0.2s ease;

    &.activo {
      background: #ffffff;
      color: #1a202c;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    }
  }
}

.lista-tareas {
  list-style: none;
  padding: 0;

  .item-tarea {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 0.875rem 1rem;
    border-radius: 8px;
    transition: background 0.15s ease;

    &:hover {
      background: #f7fafc;
    }

    &.completada label {
      text-decoration: line-through;
      color: #a0aec0;
    }

    input[type="checkbox"] {
      width: 20px;
      height: 20px;
      accent-color: #667eea;
      cursor: pointer;
    }

    label {
      flex: 1;
      font-size: 0.95rem;
      color: #2d3748;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 0.5rem;

      .fecha {
        font-size: 0.75rem;
        color: #a0aec0;
        white-space: nowrap;
      }
    }

    .btn-eliminar {
      background: none;
      border: none;
      color: #a0aec0;
      font-size: 1rem;
      cursor: pointer;
      padding: 0.25rem;
      border-radius: 4px;
      opacity: 0;
      transition: opacity 0.15s ease, color 0.15s ease;

      .item-tarea:hover & {
        opacity: 1;
      }

      &:hover {
        color: #e53e3e;
      }
    }
  }
}

.estado-vacio {
  text-align: center;
  padding: 2rem;
  color: #a0aec0;
  font-size: 0.95rem;
}

// Responsive
@media (max-width: 480px) {
  .panel-tareas {
    margin: 1rem;
    padding: 1.25rem;
    border-radius: 12px;
  }

  .filtros button {
    font-size: 0.75rem;
    padding: 0.4rem;
  }
}
```

!!! note "Explicación del resultado"
    Al ejecutar `ng serve`, se observa un panel con una lista de tareas funcional. El alumnado puede: añadir tareas (el input usa two-way binding con `nuevaTarea`), marcar/desmarcar (checkbox con event binding `(change)`), eliminar (botón que aparece al hacer hover), filtrar por estado (tabs con property binding `[class.activo]`). Los estados vacíos se muestran contextualmente según el filtro activo. La fecha se formatea con el pipe `date`. En móvil, el panel se adapta con menos padding y tipografía reducida.

### Ejemplo 2: Tarjeta de producto con estados y pipes

!!! example "Contexto pedagógico"
    Se muestra cómo combinar múltiples pipes y directivas en un componente de presentación típico de e-commerce, aplicando los principios de jerarquía visual y feedback del usuario.

```typescript
// src/app/productos/detalle-producto.component.ts
import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-detalle-producto',
  templateUrl: './detalle-producto.component.html',
  styleUrls: ['./detalle-producto.component.scss'],
  standalone: true,
})
export class DetalleProductoComponent {
  @Input() producto!: {
    nombre: string;
    precio: number;
    precioAnterior?: number;
    stock: number;
    rating: number;
    opiniones: number;
    descripcion: string;
    fechaLanzamiento: Date;
  };

  get descuento(): number {
    if (!this.producto.precioAnterior) return 0;
    return Math.round(
      ((this.producto.precioAnterior - this.producto.precio) / this.producto.precioAnterior) * 100
    );
  }

  get disponible(): boolean {
    return this.producto.stock > 0;
  }

  get stockBajo(): boolean {
    return this.producto.stock <= 5 && this.producto.stock > 0;
  }
}
```

```html
<!-- src/app/productos/detalle-producto.component.html -->
<article class="detalle">
  <div class="galeria">
    <img [src]="producto.imagen ?? '/assets/placeholder.jpg'" [alt]="producto.nombre" loading="lazy">
    @if (descuento > 0) {
      <span class="badge-descuento">-{{ descuento }}%</span>
    }
  </div>

  <div class="info-producto">
    <h1>{{ producto.nombre | titlecase }}</h1>

    <div class="rating" [attr.aria-label]="'Valoración: ' + producto.rating + ' de 5 estrellas'">
      @for (i of [1,2,3,4,5]; track i) {
        <span [class.llena]="i <= producto.rating" aria-hidden="true">★</span>
      }
      <small>{{ producto.opiniones | number:'1.0-0' }} opiniones</small>
    </div>

    <div class="precio-bloque">
      <span class="precio-actual">{{ producto.precio | currency:'EUR':'1.2-2' }}</span>
      @if (producto.precioAnterior) {
        <span class="precio-anterior">{{ producto.precioAnterior | currency:'EUR':'1.2-2' }}</span>
      }
    </div>

    <p class="descripcion">{{ producto.descripcion | slice:0:150:'…' }}</p>

    @if (disponible) {
      @if (stockBajo) {
        <p class="aviso-stock" role="status">¡Solo quedan {{ producto.stock }} unidades!</p>
      }
      <button class="btn-comprar" (click)="comprar()">Añadir al carrito</button>
    } @else {
      <p class="agotado" role="status">Agotado — Disponible próximamente</p>
      <button class="btn-aviso" (click)="suscribirAviso()">Avísame cuando vuelva</button>
    }

    <small class="meta">Lanzado el {{ producto.fechaLanzamiento | date:'LLLL yyyy' }}</small>
  </div>
</article>
```

```scss
// src/app/productos/detalle-producto.component.scss
.detalle {
  display: grid;
  grid-template-columns: 1fr;
  gap: 2rem;
  max-width: 900px;
  margin: 0 auto;
  padding: 2rem;

  @media (min-width: 768px) {
    grid-template-columns: 1fr 1fr;
  }
}

.galeria {
  position: relative;
  border-radius: 12px;
  overflow: hidden;
  aspect-ratio: 1;

  img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
}

.badge-descuento {
  position: absolute;
  top: 16px;
  left: 16px;
  background: #e53e3e;
  color: white;
  font-weight: 800;
  font-size: 1rem;
  padding: 0.4rem 0.8rem;
  border-radius: 6px;
}

.info-producto {
  h1 {
    font-size: 1.75rem;
    font-weight: 800;
    color: #1a202c;
    margin-bottom: 0.75rem;
  }
}

.rating {
  display: flex;
  align-items: center;
  gap: 0.25rem;
  margin-bottom: 1rem;
  color: #f6ad55;
  font-size: 1.1rem;

  span.vacia {
    color: #e2e8f0;
  }

  small {
    color: #718096;
    margin-left: 0.5rem;
    font-size: 0.8rem;
  }
}

.precio-bloque {
  display: flex;
  align-items: baseline;
  gap: 0.75rem;
  margin-bottom: 1rem;

  .precio-actual {
    font-size: 2rem;
    font-weight: 800;
    color: #1a202c;
  }

  .precio-anterior {
    font-size: 1.1rem;
    color: #a0aec0;
    text-decoration: line-through;
  }
}

.descripcion {
  color: #4a5568;
  line-height: 1.6;
  margin-bottom: 1.5rem;
}

.aviso-stock {
  color: #dd6b20;
  font-weight: 600;
  font-size: 0.9rem;
  margin-bottom: 0.75rem;
}

.btn-comprar {
  width: 100%;
  padding: 1rem;
  background: #667eea;
  color: white;
  border: none;
  border-radius: 10px;
  font-size: 1.05rem;
  font-weight: 700;
  cursor: pointer;
  transition: background 0.2s ease, transform 0.1s ease;

  &:hover {
    background: #5a67d8;
    transform: translateY(-1px);
  }
}

.btn-aviso {
  width: 100%;
  padding: 1rem;
  background: transparent;
  color: #667eea;
  border: 2px solid #667eea;
  border-radius: 10px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;

  &:hover {
    background: #ebf4ff;
  }
}

.agotado {
  color: #a0aec0;
  font-size: 1rem;
  margin-bottom: 1rem;
}

.meta {
  display: block;
  margin-top: 1.5rem;
  color: #a0aec0;
  font-size: 0.8rem;
}
```

!!! note "Explicación del resultado"
    Este componente demuestra la combinación de múltiples pipes (`titlecase`, `currency`, `number`, `slice`, `date`) y directivas (`@if` anidados, `@for` para estrellas) en un solo template. El estado visual cambia según el stock: si hay más de 5 unidades, se muestra el botón normal; si quedan pocas, aparece el aviso urgente; si está agotado, se cambia a "Avísame". La jerarquía visual sigue los principios de la Unidad 1: el precio es el elemento más grande y pesado, el nombre del producto es el segundo nivel, y la descripción y metadatos son información secundaria.

## Actividades de práctica

1. **Catálogo con filtros:** Crear un componente `catalogo` que muestre una cuadrícula de productos (mínimo 8). Añadir un input de búsqueda que filtre en tiempo real usando two-way binding y el método `filter()` de arrays. Añadir botones de filtro por categoría (todos, electrónica, hogar, deporte). Mostrar el estado vacío cuando no hay resultados. Aplicar la ley de proximidad: agrupar visualmente los controles de búsqueda/filtro separados de la cuadrícula de resultados.

2. **Dashboard de métricas:** Crear un componente `dashboard` que muestre 4 tarjetas de KPI (visitas, conversiones, ingresos, tickets medios) con datos numéricos formateados con pipes (`number`, `currency`). Añadir una barra de progreso para cada objetivo mensual usando property binding `[style.width.%]`. Simular la carga con un setTimeout de 2 segundos mostrando skeletons. Al "cargar", las tarjetas aparecen con una animación CSS (fade-in + slide-up).

3. **Comparación de estados:** Tomar el ejemplo de la lista de tareas y añadir tres escenarios: (a) datos cargados desde un JSON local, (b) error simulado (botón "Simular error" que muestra el estado de error con retry), (c) modo oscuro toggleable (clase `dark` en el body, variables CSS para colores). Documentar las decisiones de diseño tomadas para cada estado.

4. **Pipe personalizado:** Crear un pipe `relativo` que muestre fechas de forma relativa ("hace 3 días", "ayer", "hoy", "mañana") en lugar de la fecha absoluta. Usarlo en una lista de notificaciones simulada. Verificar que el output es correcto para cada caso y que el pipe no tiene efectos secundarios (es puro).
