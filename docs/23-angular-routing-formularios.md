---
icon: lucide/route
---

# Unidad 23: Angular — Enrutamiento y Formularios Reactivos

## Objetivos de aprendizaje

Al finalizar esta unidad, el alumnado será capaz de configurar el sistema de enrutamiento de Angular para crear aplicaciones de página única (SPA) con múltiples vistas navegables sin recargar la página, comprendiendo el concepto de SPA frente a la navegación tradicional. Definirá rutas con parámetros dinámicos (`:id`), rutas anidadas y rutas guardadas (lazy loading) para optimizar el tiempo de carga inicial. Construirá formularios reactivos con validación en tiempo real, comprendiendo la diferencia entre `FormGroup`, `FormControl` y `FormArray` y cuándo usar cada uno. Aplicará validadores integrados (`required`, `minLength`, `email`, `pattern`) y creará validadores personalizados para reglas de negocio específicas (contraseña que coincida, campos condicionales). Diseñará la experiencia de usuario de los formularios: mensajes de error contextualizados, estados visuales de validación (válido, inválido, sin tocar), deshabilitado del botón de envío hasta que el formulario sea válido, y feedback inmediato al usuario. Implementará un flujo completo de registro/login con enrutamiento protegido (guardas de ruta) y formularios reactivos validados, verificando su comportamiento en distintos navegadores y dispositivos.

## Relación con los Resultados de Aprendizaje

Esta unidad se vincula directamente con el **Resultado de Aprendizaje 4 (RA4)** del módulo profesional 0615 *Diseño de interfaces web* —"Integra contenido multimedia en documentos web valorando su aportación y seleccionando adecuadamente los elementos interactivos"—. En concreto:

- **CE 4.f**: *"Se ha añadido interactividad a elementos de un documento web."* Los formularios reactivos son el máximo exponente de la interactividad en una interfaz web: validación en tiempo real, estados visuales, mensajes contextuales y envío de datos. El enrutamiento permite que esa interactividad se extienda a múltiples vistas sin recargar.
- **CE 4.g**: *"Se ha verificado el funcionamiento de los elementos multimedia e interactivos en distintos navegadores y dispositivos."* Se verifica que las rutas funcionan correctamente (no dan 404 al recargar), que los formularios son usables en móvil (tamaño de targets táctiles, teclado apropiado) y que la validación se muestra de forma accesible.

Asimismo, contribuye al **RA6** —"Desarrolla interfaces web amigables analizando y aplicando las pautas de usabilidad"— de forma directa: el diseño de formularios es uno de los ámbitos donde la usabilidad tiene mayor impacto. Los principios de Nielsen (visibilidad del estado del sistema, reconocimiento en lugar de recuerdo, control y libertad del usuario) se aplican directamente en el diseño de formularios reactivos con validación en tiempo real.

Y al **RA1** (CE 1.e: "Se han utilizado y valorado distintas tecnologías para el diseño de documentos web") en cuanto que la arquitectura SPA con enrutamiento es una decisión tecnológica que el alumnado debe comprender y justificar frente al enfoque multi-página tradicional.

!!! note "Cierre del bloque de Angular"
    Esta unidad cierra el bloque de Angular del módulo, proporcionando las dos piezas que faltaban para tener una aplicación web completa: navegación entre vistas (routing) y captura de datos del usuario (formularios). Con las cuatro unidades de Angular (20-23), el alumnado tiene las herramientas para construir interfaces web dinámicas, interactivas y profesionales.

## Conocimientos previos

Para abordar esta unidad con soltura, el alumnado debe:

1. Haber completado las Unidades 20-22: crear proyectos Angular, trabajar con componentes, data binding, servicios y HttpClient.
2. Entender el concepto de SPA (Single Page Application): una aplicación web que carga un único documento HTML y luego actualiza el contenido dinámicamente mediante JavaScript, sin recargar la página. Diferencia con el modelo multi-página tradicional (cada navegación = petición HTTP completa + renderizado del servidor).
3. Conocer JavaScript a nivel intermedio-avanzado: closures, `this`, prototipos básicos, y el concepto de "reactividad" (cuando un dato cambia, todo lo que depende de él se actualiza).
4. Dominar TypeScript: interfaces, tipos, generics básicos, y la diferencia entre `class` y `interface`.
5. Haber trabajado con formularios HTML nativos (Unidad 7): etiquetas `<form>`, `<input>`, `<label>`, atributos de validación (`required`, `type="email"`, `pattern`), y el evento `submit`.

## Contenidos

1. **SPA y enrutamiento: el modelo mental.** Qué es una SPA y por qué Angular la implementa con un "router" en cliente. La URL como estado: cada ruta corresponde a una vista (componente). El `RouterOutlet` como punto de montaje. Diferencia entre navegación en cliente (pushState) y recarga completa. Implicaciones para SEO y accesibilidad (deep linking, botón atrás del navegador).

2. **Configuración de rutas.** Archivo `app.routes.ts`: estructura del array de `Routes`. Propiedades: `path`, `component`, `title`, `loadComponent` (lazy loading), `children` (rutas anidadas), `redirectTo`, `**` (ruta comodín 404). El componente raíz con `<router-outlet />`. Generación de rutas con `ng generate route nombre`.

3. **Navegación programática y enlaces.** Directiva `[routerLink]` para crear enlaces internos (equivalente a `<a href>` pero sin recarga). Navegación programática: `this.router.navigate(['/ruta', id])`. Parámetros de ruta: `path: 'producto/:id'` y obtención con `this.route.snapshot.params['id']` o reactivo `this.route.paramMap`. Query params: `?busqueda=angular&pagina=2`.

4. **Lazy loading y code splitting.** Cargar componentes solo cuando se navega a su ruta: `loadComponent: () => import('./perezoso/perezoso.component').then(m => m.PerezosoComponent)`. Ventajas: reducción del bundle inicial, mejor tiempo de carga percibido. Cuándo aplicarlo: vistas pesadas (dashboards con gráficos), secciones que no todos los usuarios visitan.

5. **Guardas de ruta (Route Guards).** Interceptar la navegación antes de cargar un componente. `CanActivate`: proteger rutas que requieren autenticación (login). `CanDeactivate`: avisar si hay cambios sin guardar antes de salir. Implementación con clases que implementan `CanActivateFn` (Angular 15+ funcional). Redirección a `/login` con `state: { returnUrl }`.

6. **Formularios reactivos: arquitectura.** Diferencia entre Template Driven (`ngModel`) y Reactive Forms (`FormGroup`). Por qué los reactivos son preferibles en aplicaciones de tamaño medio-grande: testabilidad, escalabilidad, validación centralizada, manejo de formularios dinámicos. Estructura: `FormBuilder` para crear grupos, `FormControl` para campos individuales, `FormArray` para listas dinámicas.

7. **Validación en tiempo real.** Validadores integrados: `Validators.required`, `Validators.minLength(n)`, `Validators.email`, `Validators.pattern(regex)`, `Validators.min/max`. Validadores personalizados: funciones que reciben un `AbstractControl` y devuelven `ValidationErrors | null`. Patrones de UX: mostrar el error solo después de que el campo ha sido "tocado" (`touched`), no al escribir la primera letra. El estado `pristine` vs `dirty` vs `touched`.

8. **Estados visuales del formulario.** Clases CSS condicionales según el estado: `[class.error]="campo.invalid && campo.touched"`. Mensajes de error específicos por validador (no "inválido" sino "Debe tener al menos 8 caracteres"). El botón de envío deshabilitado (`[disabled]="form.invalid"`). Feedback de éxito tras el envío (toast, redirección, pantalla de confirmación).

9. **Formularios dinámicos con FormArray.** Listas de campos que crecen y decrecen: direcciones adicionales, ítems de un carrito, pasos de un wizard. `formArray.push()`, `formArray.removeAt(i)`. Validación del array completo (mínimo 1 elemento, sin duplicados).

10. **Flujo completo de registro.** Integrar enrutamiento + formularios reactivos + servicio: ruta `/registro` con formulario validado → envío al servicio (POST) → estado de carga → éxito (redirección a dashboard) o error (mostrar mensaje inline). Ruta protegida `/dashboard` que redirige a `/login` si no hay sesión. Guardar `returnUrl` para volver a la página solicitada tras el login.

## Desarrollo teórico

### 1. SPA: la URL como estado de la aplicación

!!! info "SPA con Angular"
    En una aplicación web tradicional (multi-página), cada navegación implica: petición HTTP al servidor → el servidor renderiza HTML completo → el navegador descarta el DOM actual y construye uno nuevo → la página "parpadea". El usuario pierde el estado (scroll, formularios parcialmente completados, animaciones en curso).

    En una SPA con Angular, todo ocurre en el cliente: se carga un único `index.html` con el bundle JavaScript, y desde ahí el **Router** de Angular gestiona las "páginas" como componentes que se montan y desmontan dinámicamente en un `<router-outlet />`. La URL cambia (mediante la History API del navegador: `pushState`, `replaceState`) pero no hay recarga. El botón "atrás" del navegador funciona porque el Router registra cada navegación en el historial.

Esto tiene implicaciones de diseño:

- **Profundidad de enlace:** la persona usuaria puede compartir una URL (`/producto/42`) y quien la abra verá directamente ese producto, no la página de inicio. El Router debe poder "hidratar" cualquier estado desde la URL.
- **Carga inicial vs navegación posterior:** la primera carga es pesada (todo el JavaScript), pero las navegaciones posteriores son instantáneas (solo cambia el componente montado). Por eso el lazy loading es crucial: no cargar en el bundle inicial lo que el 80% de los usuarios nunca verá.
- **Accesibilidad:** los enlaces deben ser `<a>` reales (con `routerLink`), no `<div (click)>`, para que sean navegables por teclado y anunciados por lectores de pantalla.

### 2. Estructura de rutas típica

```typescript
// src/app/app.routes.ts
import { Routes } from '@angular/router';

export const APP_ROUTES: Routes = [
  { path: '', redirectTo: 'inicio', pathMatch: 'full' },

  {
    path: 'inicio',
    loadComponent: () => import('./inicio/inicio.component').then(m => m.InicioComponent),
    title: 'Inicio'
  },

  {
    path: 'productos',
    loadComponent: () => import('./productos/productos.component').then(m => m.ProductosComponent),
    title: 'Productos',
    children: [
      { path: '', redirectTo: 'lista', pathMatch: 'full' },
      {
        path: 'lista',
        loadComponent: () => import('./productos/lista.component').then(m => m.ListaComponent)
      },
      {
        path: 'detalle/:id',
        loadComponent: () => import('./productos/detalle.component').then(m => m.DetalleComponent),
        title: (data: any) => `Producto ${data?.params?.id}`
      }
    ]
  },

  {
    path: 'cuenta',
    loadChildren: () => import('./cuenta/cuenta.routes').then(m => m.CUENTA_ROUTES),
    canActivate: [authGuard] // Solo usuarios autenticados
  },

  { path: '**', component: NotFoundComponent, title: 'Página no encontrada' }
];
```

| Propiedad | Descripción |
| --------- | ----------- |
| `path` | Fragmento de URL que identifica la ruta |
| `component` | Componente a montar en la ruta |
| `title` | Título de la vista |
| `loadComponent` | Lazy loading del componente |
| `children` | Rutas anidadas bajo esta ruta |
| `redirectTo` | Redirección a otra ruta |
| `**` | Ruta comodín (404) |

El componente raíz (`app.component.html`) solo contiene:

```html
<app-header />
<main class="contenido-principal">
  <router-outlet />
</main>
<app-footer />
```

!!! note "Qué cambia en cada navegación"
    Cada navegación reemplaza el contenido dentro de `<router-outlet />` sin tocar la cabecera ni el pie.

### 3. Formularios reactivos: control total sobre el estado

!!! info "Formularios reactivos"
    En un formulario template-driven (`ngModel`), el estado vive "esparcido" en el template y el componente no tiene una visión global de qué es válido y qué no. En un formulario reactivo, **todo el estado del formulario es un objeto TypeScript** (`FormGroup`) que puedes inspeccionar, modificar, serializar y testear desde el código:

```typescript
import { Component } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';

@Component({ ... })
export class RegistroComponent {
  form = this.fb.nonNullable.group({
    nombre: ['', [Validators.required, Validators.minLength(2)]],
    email: ['', [Validators.required, Validators.email]],
    password: ['', [
      Validators.required,
      Validators.minLength(8),
      Validators.pattern(/^(?=.*[A-Z])(?=.*\d).+$/) // Mayúsca y número
    ]],
    confirmarPassword: [''],
    terminos: [false, Validators.requiredTrue]
  }, {
    validators: contraseñasCoinciden // Validador a nivel de grupo
  });

  constructor(private fb: FormBuilder) {}

  get nombre() { return this.form.controls.nombre; }
  get email() { return this.form.controls.email; }
  get password() { return this.form.controls.password; }

  enviar() {
    if (this.form.invalid) {
      this.form.markAllAsTouched(); // Muestra todos los errores
      return;
    }
    // this.servicio.registrar(this.form.getRawValue());
  }
}
```

!!! tip "La clave es nonNullable"
    La clave es `nonNullable`: evita el boilerplate de `!` y garantiza que cada campo siempre tiene un valor (string, number, boolean), nunca `null`. Esto simplifica enormemente el código del template.

### 4. Validación y UX: el error en el momento justo

!!! warning "El peor patrón de formulario"
    El peor patrón de formulario es mostrar todos los errores en rojo cuando la persona usuaria pulsa "Enviar" por primera vez, después de haber llenado cinco campos.

El mejor patrón (basado en las heurísticas de Nielsen) es:

!!! tip "Reglas de UX para validar"
    1. **No mostrar errores en campos que no se han tocado.** Un campo vacío y sin tocar no es "inválido" visualmente; es "sin completar".
    2. **Validar al perder el foco (`blur`).** Cuando la persona usuaria sale del campo, se valida y se muestra el error si lo hay. No mientras escribe (es frustrante ver el error desaparecer y reaparecer letra a letra).
    3. **Mensajes específicos y accionables.** No "Campo inválido" sino "La contraseña debe tener al menos 8 caracteres, una mayúscula y un número".
    4. **El botón de envío se deshabilita** solo cuando el formulario es objetivamente incompleto (campos requeridos vacíos). No se deshabilita por errores de formato (la persona usuaria debe poder pulsar para ver qué falta).
    5. **Al pulsar enviar con errores:** marcar todos los campos como `touched` (para mostrar los mensajes) y hacer scroll al primer campo inválido.

```html
<div class="campo" [class.invalid]="password.invalid && password.touched">
  <label for="password">Contraseña</label>
  <input
    id="password"
    type="password"
    formControlName="password"
    [attr.aria-invalid]="password.invalid && password.touched ? 'true' : 'false'"
    [attr.aria-describedby]="password.invalid && password.touched ? 'error-password' : null"
  >
  @if (password.invalid && password.touched) {
    <p id="error-password" class="mensaje-error" role="alert">
      @if (password.errors?.['minLength']) {
        Mínimo {{ password.errors?.['minLength']?.requiredLength }} caracteres.
      }
      @if (password.errors?.['pattern']) {
        Debe incluir una mayúscula y un número.
      }
    </p>
  }
</div>

<button type="submit" [disabled]="form.pending">
  Crear cuenta
</button>
```

### 5. Guardas de ruta: proteger lo que debe estar protegido

!!! info "Rutas públicas y rutas privadas"
    El patrón típico es: las rutas públicas (inicio, productos, login, registro) son accesibles sin autenticación. Las rutas privadas (dashboard, perfil, pedidos) requieren sesión.

El guard se implementa como una función (Angular 15+):

```typescript
// src/app/core/auth.guard.ts
import { inject } from '@angular/core';
import { CanActivateFn, Router } from '@angular/router';
import { AuthService } from './auth.service';

export const authGuard: CanActivateFn = (route, state) => {
  const auth = inject(AuthService);
  const router = inject(Router);

  if (auth.estaAutenticado()) {
    return true; // Permite la navegación
  }

  // Guarda de dónde venía para volver tras el login
  return router(['/login'], { queryParams: { returnUrl: state.url } });
};
```

En la configuración de rutas:

```typescript
{
  path: 'cuenta',
  canActivate: [authGuard],
  loadChildren: () => import('./cuenta/cuenta.routes').then(m => m.CUENTA_ROUTES)
}
```

!!! tip "Volver a la página solicitada"
    Tras el login exitoso, el servicio guarda el `returnUrl` y redirige.

```typescript
// En el componente de login, tras envío exitoso:
const returnUrl = this.route.snapshot.queryParamMap.get('returnUrl') ?? '/cuenta';
this.router.navigate([returnUrl]);
```

## Ejemplos guiados

### Ejemplo 1: SPA con enrutamiento completo (catálogo + detalle + 404)

!!! example "Contexto pedagógico"
    Se configura una aplicación con tres vistas principales y una ruta comodín, demostrando el flujo de navegación SPA, parámetros dinámicos y lazy loading.

```typescript
// src/app/app.routes.ts
import { Routes } from '@angular/router';

export const APP_ROUTES: Routes = [
  { path: '', redirectTo: 'inicio', pathMatch: 'full' },
  {
    path: 'inicio',
    loadComponent: () => import('./inicio/inicio.component').then(m => m.InicioComponent),
    title: 'Inicio — MiTienda'
  },
  {
    path: 'productos',
    loadComponent: () => import('./productos/productos.component').then(m => m.ProductosComponent),
    title: 'Productos — MiTienda'
  },
  {
    path: 'productos/:id',
    loadComponent: () => import('./producto-detalle/producto-detalle.component').then(m => m.ProductoDetalleComponent),
    title: 'Producto — MiTienda'
  },
  {
    path: 'about',
    loadComponent: () => import('./about/about.component').then(m => m.AboutComponent),
    title: 'Sobre nosotros — MiTienda'
  },
  {
    path: '**',
    loadComponent: () => import('./not-found/not-found.component').then(m => m.NotFoundComponent),
    title: 'Página no encontrada'
  }
];
```

```html
<!-- src/app/inicio/inicio.component.html -->
<section class="hero">
  <h1>Bienvenido a MiTienda</h1>
  <p>Los mejores productos al mejor precio.</p>
  <a routerLink="/productos" class="btn-primario">Ver catálogo</a>
</section>

<section class="destacados">
  <h2>Productos destacados</h2>
  <div class="grid">
    @for (p of destacados; track p.id) {
      <a [routerLink]="['/productos', p.id]" class="tarjeta-link">
        <img [src]="p.imagen" [alt]="p.nombre">
        <h3>{{ p.nombre }}</h3>
        <span class="precio">{{ p.precio | currency:'EUR' }}</span>
      </a>
    }
  </div>
</section>
```

```typescript
// src/app/producto-detalle/producto-detalle.component.ts
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-producto-detalle',
  templateUrl: './producto-detalle.component.html',
  standalone: true,
})
export class ProductoDetalleComponent implements OnInit {
  id!: number;
  producto: any = null;
  cargando = true;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
  ) {}

  ngOnInit() {
    // Obtener el parámetro de la URL: /productos/42 → id = 42
    this.id = Number(this.route.snapshot.params['id']);
    this.cargarProducto(this.id);
  }

  cargarProducto(id: number) {
    this.cargando = true;
    // Simulación: en producción, this.servicio.obtenerPorId(id)
    setTimeout(() => {
      this.producto = { id, nombre: 'Cafetera Espresso Pro', precio: 89.95, descripcion: '...' };
      this.cargando = false;
    }, 800);
  }

  irAlCatálogo() {
    this.router.navigate(['/productos']);
  }
}
```

```html
<!-- src/app/producto-detalle/producto-detalle.component.html -->
@if (cargando) {
  <div class="skeleton" aria-busy="true">Cargando producto...</div>
} @else if (producto) {
  <nav class="breadcrumbs" aria-label="Ruta de navegación">
    <a routerLink="/productos">Productos</a>
    <span aria-hidden="true">/</span>
    <span aria-current="page">{{ producto.nombre }}</span>
  </nav>

  <article class="detalle">
    <h1>{{ producto.nombre }}</h1>
    <p class="precio">{{ producto.precio | currency:'EUR' }}</p>
    <p>{{ producto.descripcion }}</p>
    <button class="btn-primario">Añadir al carrito</button>
  </article>

  <a (click)="irAlCatálogo()" class="volver" role="button" tabindex="0">← Volver al catálogo</a>
} @else {
  <div class="no-encontrado">
    <h1>Producto no encontrado</h1>
    <p>El producto que buscas no existe o ha sido eliminado.</p>
    <a routerLink="/productos" class="btn-secundario">Ir al catálogo</a>
  </div>
}
```

```html
<!-- src/app/not-found/not-found.component.html -->
<section class="pagina-404">
  <span class="codigo" aria-hidden="true">404</span>
  <h1>Página no encontrada</h1>
  <p>La página que buscas no existe o ha sido movida.</p>
  <a routerLink="/" class="btn-primario">Volver al inicio</a>
</section>
```

!!! note "Explicación del resultado"
    Al navegar a `http://localhost:4200/productos/42`, se carga el componente de detalle con el parámetro `id=42`. Si se navega a `http://localhost:4200/ruta-inexistente`, se muestra la página 404. El botón "atrás" del navegador funciona correctamente (History API). En DevTools → Network, se observa que tras la carga inicial, las navegaciones no hacen peticiones HTTP al servidor (solo el lazy chunk se descarga la primera vez que se visita una ruta).

### Ejemplo 2: Formulario de registro reactivo con validación completa

!!! example "Contexto pedagógico"
    Se construye un formulario de registro con todos los patrones de UX estudiados: validación en blur, mensajes específicos, botón deshabilitado, estados visuales y accesibilidad ARIA. Es el ejemplo "de referencia" para evaluar formularios en el módulo.

```typescript
// src/app/registro/registro.component.ts
import { Component } from '@angular/core';
import { FormBuilder, Validators, AbstractControl, ValidationErrors } from '@angular/forms';

@Component({
  selector: 'app-registro',
  templateUrl: './registro.component.html',
  styleUrls: ['./registro.component.scss'],
  standalone: true,
})
export class RegistroComponent {
  form = this.fb.nonNullable.group({
    nombre: ['', [Validators.required, Validators.minLength(2), Validators.maxLength(50)]],
    email: ['', [Validators.required, Validators.email]],
    password: ['', [
      Validators.required,
      Validators.minLength(8),
      Validators.pattern(/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$/)
    ]],
    confirmarPassword: [''],
    terminos: [false, Validators.requiredTrue]
  }, { validators: contraseñasCoinciden });

  enviado = false;
  errorServidor: string | null = null;

  constructor(private fb: FormBuilder) {}

  // Accessors cortos
  get nombre() { return this.form.controls.nombre; }
  get email() { return this.form.controls.email; }
  get password() { return this.form.controls.password; }
  get confirmarPassword() { return this.form.controls.confirmarPassword; }
  get terminos() { return this.form.controls.terminos; }

  enviar() {
    if (this.form.invalid) {
      this.form.markAllAsTouched();
      return;
    }

    this.errorServidor = null;
    // Simulación de envío al servidor
    setTimeout(() => {
      this.enviado = true;
    }, 1500);
  }
}

// Validador a nivel de grupo: las contraseñas deben coincidir
function contraseñasCoinciden(grupo: AbstractControl): ValidationErrors | null {
  const pass = grupo.get('password')?.value;
  const confirm = grupo.get('confirmarPassword')?.value;
  return (pass === confirm || !confirm) ? null : { noCoinciden: true };
}
```

```html
<!-- src/app/registro/registro.component.html -->
<section class="panel-registro">
  @if (enviado) {
    <div class="exito" role="status">
      <span class="icono-check" aria-hidden="true">✓</span>
      <h2>¡Cuenta creada!</h2>
      <p>Revisa tu correo para verificar tu cuenta.</p>
      <a routerLink="/" class="btn-primario">Ir al inicio</a>
    </div>
  } @else {
    <h1>Crear cuenta</h1>
    <p class="subtitulo">Completa tus datos para registrarte</p>

    @if (errorServidor) {
      <div class="banner-error" role="alert">{{ errorServidor }}</div>
    }

    <form [formGroup]="form" (ngSubmit)="enviar()" novalidate>
      <!-- NOMBRE -->
      <div class="campo" [class.invalid]="nombre.invalid && nombre.touched">
        <label for="nombre">Nombre y apellidos</label>
        <input
          id="nombre"
          type="text"
          formControlName="nombre"
          autocomplete="name"
          [attr.aria-invalid]="nombre.invalid && nombre.touched ? 'true' : 'false'"
          [attr.aria-describedby]="nombre.invalid && nombre.touched ? 'err-nombre' : null"
        >
        @if (nombre.invalid && nombre.touched) {
          <p id="err-nombre" class="error-campo" role="alert">
            @if (nombre.errors?.['required']) { El nombre es obligatorio. }
            @if (nombre.errors?.['minLength']) { Mínimo 2 caracteres. }
          </p>
        }
      </div>

      <!-- EMAIL -->
      <div class="campo" [class.invalid]="email.invalid && email.touched">
        <label for="email">Correo electrónico</label>
        <input
          id="email"
          type="email"
          formControlName="email"
          autocomplete="email"
          [attr.aria-invalid]="email.invalid && email.touched ? 'true' : 'false'"
          [attr.aria-describedby]="email.invalid && email.touched ? 'err-email' : null"
        >
        @if (email.invalid && email.touched) {
          <p id="err-email" class="error-campo" role="alert">
            @if (email.errors?.['required']) { El email es obligatorio. }
            @if (email.errors?.['email']) { Introduce un correo válido (ej: nombre@dominio.com). }
          </p>
        }
      </div>

      <!-- CONTRASEÑA -->
      <div class="campo" [class.invalid]="password.invalid && password.touched">
        <label for="password">Contraseña</label>
        <input
          id="password"
          type="password"
          formControlName="password"
          autocomplete="new-password"
          [attr.aria-invalid]="password.invalid && password.touched ? 'true' : 'false'"
          [attr.aria-describedby]="password.invalid && password.touched ? 'err-password' : null"
        >
        @if (password.invalid && password.touched) {
          <p id="err-password" class="error-campo" role="alert">
            @if (password.errors?.['minLength']) { Mínimo 8 caracteres. }
            @if (password.errors?.['pattern']) { Debe incluir una mayúscula, una minúscula y un número. }
          </p>
        }
        <!-- Indicador de fuerza -->
        <div class="fuerza" aria-hidden="true">
          <div class="barra" [class.fuerte]="password.value.length >= 12 && password.valid"></div>
          <small>{{ password.value.length }}/8 mínimo</small>
        </div>
      </div>

      <!-- CONFIRMAR CONTRASEÑA -->
      <div class="campo" [class.invalid]="(form.errors?.['noCoinciden'] && confirmarPassword.touched) || (confirmarPassword.invalid && confirmarPassword.touched)">
        <label for="confirmar">Confirmar contraseña</label>
        <input
          id="confirmar"
          type="password"
          formControlName="confirmarPassword"
          autocomplete="new-password"
          [attr.aria-invalid]="form.errors?.['noCoinciden'] && confirmarPassword.touched ? 'true' : 'false'"
        >
        @if (form.errors?.['noCoinciden'] && confirmarPassword.touched) {
          <p class="error-campo" role="alert">Las contraseñas no coinciden.</p>
        }
      </div>

      <!-- TÉRMINOS -->
      <div class="campo checkbox" [class.invalid]="terminos.invalid && terminos.touched">
        <label for="terminos">
          <input
            id="terminos"
            type="checkbox"
            formControlName="terminos"
            [attr.aria-invalid]="terminos.invalid && terminos.touched ? 'true' : 'false'"
          >
          Acepto los <a href="/terminos" target="_blank" rel="noopener">términos y condiciones</a>
        </label>
        @if (terminos.invalid && terminos.touched) {
          <p class="error-campo" role="alert">Debes aceptar los términos para continuar.</p>
        }
      </div>

      <!-- BOTÓN DE ENVÍO -->
      <button type="submit" [disabled]="form.pending" class="btn-enviar">
        Crear cuenta
      </button>
    </form>
  }
</section>
```

```scss
// src/app/registro/registro.component.scss
.panel-registro {
  max-width: 480px;
  margin: 3rem auto;
  padding: 2.5rem;
  background: #ffffff;
  border-radius: 16px;
  box-shadow: 0 4px 24px rgba(0, 0, 0, 0.08);

  h1 {
    font-size: 1.75rem;
    font-weight: 800;
    color: #1a202c;
    margin-bottom: 0.25rem;
  }

  .subtitulo {
    color: #718096;
    margin-bottom: 2rem;
    font-size: 0.95rem;
  }
}

.campo {
  margin-bottom: 1.25rem;

  label {
    display: block;
    font-size: 0.875rem;
    font-weight: 600;
    color: #4a5568;
    margin-bottom: 0.375rem;
  }

  input[type="text"],
  input[type="email"],
  input[type="password"] {
    width: 100%;
    padding: 0.75rem 1rem;
    border: 2px solid #e2e8f0;
    border-radius: 8px;
    font-size: 1rem;
    transition: border-color 0.2s ease, box-shadow 0.2s ease;

    &:focus {
      outline: none;
      border-color: #667eea;
      box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.15);
    }
  }

  &.invalid input {
    border-color: #e53e3e;

    &:focus {
      border-color: #e53e3e;
      box-shadow: 0 0 0 3px rgba(229, 62, 62, 0.15);
    }
  }
}

.error-campo {
  color: #e53e3e;
  font-size: 0.8rem;
  margin-top: 0.375rem;
  font-weight: 500;
}

.checkbox label {
  display: flex;
  align-items: flex-start;
  gap: 0.5rem;
  font-weight: 400;
  font-size: 0.9rem;
  color: #4a5568;
  cursor: pointer;

  input {
    margin-top: 0.2rem;
    width: 18px;
    height: 18px;
    accent-color: #667eea;
  }

  a {
    color: #667eea;
  }
}

.fuerza {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-top: 0.5rem;

  .barra {
    flex: 1;
    height: 4px;
    background: #e2e8f0;
    border-radius: 2px;
    overflow: hidden;
    position: relative;

    &::after {
      content: '';
      position: absolute;
      left: 0;
      top: 0;
      height: 100%;
      width: 30%;
      background: #e53e3e;
      border-radius: 2px;
      transition: width 0.3s ease, background 0.3s ease;
    }

    &.fuerte::after {
      width: 100%;
      background: #48bb78;
    }
  }

  small {
    color: #a0aec0;
    font-size: 0.7rem;
    white-space: nowrap;
  }
}

.btn-enviar {
  width: 100%;
  padding: 0.875rem;
  background: #667eea;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: 700;
  cursor: pointer;
  margin-top: 0.5rem;
  transition: background 0.2s ease, transform 0.1s ease;

  &:hover:not(:disabled) {
    background: #5a67d8;
    transform: translateY(-1px);
  }

  &:disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }
}

.banner-error {
  background: #fff5f5;
  border: 1px solid #feb2b2;
  color: #c53030;
  padding: 0.75rem 1rem;
  border-radius: 8px;
  margin-bottom: 1.5rem;
  font-size: 0.9rem;
}

.exito {
  text-align: center;
  padding: 2rem 0;

  .icono-check {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 64px;
    height: 64px;
    background: #c6f6d5;
    color: #276749;
    font-size: 2rem;
    border-radius: 50%;
    margin-bottom: 1rem;
  }

  h2 {
    color: #1a202c;
    margin-bottom: 0.5rem;
  }

  p {
    color: #718096;
    margin-bottom: 1.5rem;
  }
}

// Responsive
@media (max-width: 480px) {
  .panel-registro {
    margin: 1rem;
    padding: 1.5rem;
    border-radius: 12px;
  }
}
```

!!! note "Explicación del resultado"
    El formulario valida en tiempo real al perder el foco de cada campo. Los mensajes de error son específicos (no "inválido" sino "Mínimo 8 caracteres"). El indicador de fuerza de contraseña muestra una barra que crece y cambia de color (rojo → verde) según la complejidad. Si las contraseñas no coinciden, el error se muestra en el campo de confirmación. El botón "Crear cuenta" solo está deshabilitado durante el envío (`form.pending`). Tras el envío exitoso, se muestra una pantalla de confirmación con un checkmark verde. Todos los campos tienen `aria-invalid` y `aria-describedby` para lectores de pantalla. En móvil, el panel ocupa casi todo el ancho con padding reducido.

## Actividades de práctica

1. **SPA completa:** Tomar el proyecto de la actividad 1 de la Unidad 20 (mi-portfolio) y añadir enrutamiento con al menos cuatro vistas: inicio, proyectos (lista), proyecto-detalle (`:id`), contacto. Implementar lazy loading para todas las rutas. Añadir una ruta comodín 404. Verificar que el botón "atrás" del navegador funciona y que las URLs son compartibles (deep linking).

2. **Formulario de contacto con FormArray:** Crear un formulario de contacto que permita añadir múltiples mensajes (ej: "motivo principal" + "detalles adicionales" como lista dinámica). Usar `FormArray` para los detalles: botón "+ Añadir detalle" que añade un campo de texto, y botón "✕" que lo elimina. Validación: mínimo 1 mensaje, máximo 5 detalles. Los campos deben ser accesibles (labels únicos, `aria-label` en el botón de eliminar).

3. **Flujo de login con guardas:** Implementar un flujo completo: ruta `/login` con formulario reactivo (email + contraseña, validación básica), servicio `AuthService` que simula autenticación (guarda un flag en `localStorage`), guard `authGuard` que protege la ruta `/panel`. Tras el login, redirigir a `returnUrl` si existe. En `/panel`, mostrar un botón "Cerrar sesión" que limpia el estado y redirige a `/login`. Verificar que recargar la página en `/panel` sin sesión redirige correctamente.

4. **Auditoría de usabilidad:** Tomar el formulario de registro del ejemplo 2 y realizar una auditoría basada en las 10 heurísticas de Nielsen (Unidad 15). Documentar: ¿Qué heurísticas se cumplen? ¿Cuáles se violan? Proponer mejoras para al menos tres heurísticas no cumplidas. Presentar el informe con capturas de pantalla y justificación argumentada.
