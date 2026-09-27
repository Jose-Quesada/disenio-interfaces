# Unidad 22: Angular — Servicios, HttpClient y Consumo de APIs

## Objetivos de aprendizaje

Al finalizar esta unidad, el alumnado será capaz de crear servicios inyectables en Angular para centralizar la lógica de obtención de datos, comprendiendo el patrón de inyección de dependencias y sus ventajas para el mantenimiento y la testabilidad. Configurarán el `HttpClientModule` y ejecutarán peticiones HTTP GET, POST, PUT y DELETE contra APIs REST reales (JSONPlaceholder, OpenWeather, etc.), interpretando las respuestas como observables RxJS. Manejarán los estados asíncronos de una petición (cargando, éxito, error) implementando los patrones visuales estudiados en la Unidad 21 (skeleton loaders, mensajes de error con retry). Aplicarán el concepto de "fuente de verdad" separando la capa de presentación (componentes) de la capa de datos (servicios), comprendiendo cómo esta arquitectura facilita el trabajo en equipo y la reutilización de código. Consumirán una API REST pública para construir una interfaz completa tipo "clima", "noticias" o "catálogo de productos", mostrando los datos obtenidos con los componentes y pipes estudiados en unidades anteriores. Verificarán el funcionamiento en distintos navegadores y dispositivos, comprendiendo las implicaciones del CORS y la configuración de proxies en desarrollo.

## Relación con los Resultados de Aprendizaje

Esta unidad se vincula directamente con el **Resultado de Aprendizaje 4 (RA4)** del módulo profesional 0615 *Diseño de interfaces web* —"Integra contenido multimedia en documentos web valorando su aportación y seleccionando adecuadamente los elementos interactivos"—. En concreto:

- **CE 4.a**: *"Se han reconocido y analizado las tecnologías relacionadas con la inclusión de contenido multimedia e interactivo."* El `HttpClient` es la tecnología que permite a una interfaz web obtener datos dinámicamente desde un servidor, haciendo que el contenido sea interactivo y actualizable sin recargar la página.
- **CE 4.c**: *"Se han utilizado herramientas gráficas para el desarrollo de contenido multimedia interactivo."* Angular + HttpClient son esa herramienta: se construyen interfaces que muestran contenido (imágenes, textos, datos) obtenido en tiempo real.
- **CE 4.g**: *"Se ha verificado el funcionamiento de los elementos multimedia e interactivos en distintos navegadores y dispositivos."* Se verifica con DevTools (pestaña Network) que las peticiones se ejecutan correctamente y que la interfaz se adapta al viewport.

Asimismo, contribuye al **RA2** (CE 2.i: "Se han analizado y utilizado tecnologías y frameworks para la creación de interfaces web") en cuanto que el patrón de servicios inyectables es una característica distintiva de Angular como framework para la creación de interfaces escalables. Y al **RA6** (usabilidad) mediante el diseño de estados de carga, error y vacío que comunican claramente el estado de la aplicación a la persona usuaria durante las operaciones asíncronas.

!!! note "Cierre del bloque de interactividad (RA4)"
    Esta unidad cierra el bloque de "interactividad" del RA4 mostrando cómo una interfaz no solo reacciona a eventos locales (Unidad 21) sino que se conecta con fuentes de datos externas, completando el ciclo de una aplicación web moderna: obtener datos → procesarlos → mostrarlos → permitir acciones sobre ellos.

## Conocimientos previos

Para abordar esta unidad con soltura, el alumnado debe:

1. Haber completado las Unidades 20 y 21: crear proyectos Angular, trabajar con componentes, data binding, directivas estructurales y pipes.
2. Dominar JavaScript asíncrono a nivel conceptual: qué es una Promesa, `async/await`, el callback hell y por qué los observables son una alternativa más potente para flujos de datos continuos.
3. Conocer el protocolo HTTP a nivel básico: métodos (GET, POST, PUT, DELETE), códigos de estado (200, 400, 401, 404, 500), cabeceras (Content-Type, Authorization) y el concepto de API REST.
4. Entender qué es un observable RxJS a nivel conceptual: una "promesa que se puede suscribir, cancelar y combinar". No hace falta dominar RxJS en profundidad, solo comprender `subscribe()`, `pipe()` y los operadores básicos (`map`, `catchError`, `switchMap`).
5. Saber leer JSON e interpretar estructuras de datos anidadas (arrays de objetos, propiedades opcionales).

## Contenidos

1. **Arquitectura de capas en Angular.** Separación entre presentación (componentes) y lógica de datos (servicios). El patrón "dumb component / smart component": el componente presentacional solo muestra lo que le pasan por `@Input`; el componente contenedor obtiene los datos del servicio y los pasa abajo. Ventajas: testabilidad, reutilización, menor acoplamiento.

2. **Creación de servicios.** Comando `ng generate service nombre`. El decorador `@Injectable({ providedIn: 'root' })` y qué significa (singleton a nivel de aplicación). Inyección en componentes mediante el constructor: `constructor(private http: HttpClient)`. Diferencia entre `providedIn: 'root'` y `providedIn: ComponentX` (escopo local).

3. **Configuración del HttpClient.** Importar `provideHttpClient()` en `app.config.ts` (Angular 15+) o importar `HttpClientModule` (versión clásica). El objeto de configuración: interceptores, headers por defecto, timeout. Verificación de que el módulo está activo.

4. **Peticiones GET.** Sintaxis: `this.http.get<T>(url)`. Genérico `<T>` para tipar la respuesta. Suscripción al observable: `.subscribe({ next, error, complete })` o con operador `.pipe()`. Ejemplo: obtener una lista de productos desde JSONPlaceholder (`https://jsonplaceholder.typicode.com/products`). Manejo del estado `cargando` en el componente.

5. **Peticiones POST, PUT y DELETE.** `this.http.post(url, datos)`, `this.http.put(url, datos)`, `this.http.delete(url)`. Cuándo usar cada método (semántica REST). Ejemplo: crear un nuevo elemento (POST), modificar uno existente (PUT), eliminarlo (DELETE). Verificación en la pestaña Network de DevTools.

6. **Observables y operadores esenciales.** Diferencia entre Promesa (una vez) y Observable (flujo continuo). Operadores más usados: `map` (transformar datos), `catchError` (manejar errores sin romper el flujo), `tap` (efectos secundarios como setear `cargando=true`), `switchMap` (cancelar peticiones anteriores al hacer una nueva, útil en buscadores). El patrón de "estado de carga" con `tap`.

7. **Manejo de errores.** Estructura del error de HttpClient (`HttpErrorResponse`: status, error, message). Patrones de UI: toast de error, banner inline, pantalla completa de error. El patrón retry (botón "Reintentar"). Distinción entre errores de red (timeout, offline) y errores de servidor (4xx, 5xx). Mensajes comprensibles para la persona usuaria (no técnicos).

8. **CORS y proxy de desarrollo.** Qué es CORS (Cross-Origin Resource Sharing) y por qué el navegador bloquea peticiones a otro dominio. La solución en desarrollo: `proxy.conf.json` con Angular CLI (`ng serve --proxy-config proxy.conf.json`). En producción: configurar las cabeceras CORS en el servidor o usar un backend como proxy.

9. **Consumo de APIs reales.** Ejemplos públicos sin clave: JSONPlaceholder (CRUD simulado), Open-Meteo (clima, sin API key), Wikipedia API (búsqueda), REST Countries (datos de países). Estructura típica de una respuesta JSON y cómo mapearla a interfaces TypeScript. Manejo de datos opcionales (`?` en TypeScript) y valores por defecto.

10. **Integración con componentes.** El servicio como "puente" entre el mundo externo (API) y la interfaz (componentes). Patrón: el componente llama a `cargarDatos()` del servicio en `ngOnInit()`, el servicio devuelve un observable, el componente se suscribe y actualiza sus propiedades. Los datos fluyen hacia abajo (`@Input`), los eventos hacia arriba (`@Output`). El servicio no conoce la UI; el componente no hace peticiones HTTP directamente.

## Desarrollo teórico

### 1. ¿Por qué servicios? Separar "qué se muestra" de "de dónde vienen los datos"

!!! info "Tres ventajas de un servicio"
    Hasta ahora, los datos en nuestros componentes eran arrays literales definidos en el propio componente (`this.productos = [...]`). Esto funciona para prototipos, pero en una aplicación real los datos provienen de un servidor: una base de datos, una API externa, un servicio de clima, un sistema de usuarios. Centralizar esa lógica en un **servicio** aporta tres ventajas fundamentales:

    - **Reutilización:** el mismo servicio puede ser inyectado en múltiples componentes sin duplicar código. El `ProductoService` puede usarse en la página de catálogo, en el carrito y en las recomendaciones.
    - **Testabilidad:** al aislar la lógica de datos en un servicio, se puede testear independientemente de la UI. Se puede "mockear" (sustituir por una versión falsa) en tests de componentes para verificar que la interfaz reacciona correctamente sin depender de un servidor real.
    - **Mantenibilidad:** si cambia la URL de la API o el formato de la respuesta, solo se modifica el servicio, no los diez componentes que la consumen. El componente solo sabe que "el servicio me da productos", no cómo se obtienen.

### 2. Inyección de dependencias: Angular te lo entrega

!!! info "Inyección de dependencias"
    En lugar de crear instancias del servicio manualmente (`const svc = new ProductoService()`), Angular usa **inyección de dependencias**: declaras en el constructor qué necesitas y Angular lo "inyecta" automáticamente.

```typescript
@Injectable({ providedIn: 'root' })
export class ClimaService {
  private http = inject(HttpClient); // Forma moderna (Angular 14+)

  getClima(lat: number, lon: number) {
    return this.http.get<ClimaResponse>(
      `https://api.open-meteo.com/v1/forecast?latitude=${lat}&longitude=${lon}&current_weather=true`
    );
  }
}
```

```typescript
@Component({ ... })
export class ClimaComponent {
  private climaService = inject(ClimaService); // Forma moderna
  // O clásico: constructor(private climaService: ClimaService) {}

  clima: ClimaResponse | null = null;
  cargando = false;
  error: string | null = null;

  ngOnInit() {
    this.cargar(40.4168, -3.7038); // Córdoba
  }

  cargar(lat: number, lon: number) {
    this.cargando = true;
    this.error = null;

    this.climaService.getClima(lat, lon).subscribe({
      next: (data) => {
        this.clima = data;
        this.cargando = false;
      },
      error: (err) => {
        this.error = 'No se pudo obtener el clima. Inténtalo de nuevo.';
        this.cargando = false;
      }
    });
  }
}
```

!!! tip "El trío: cargando, error y datos"
    El patrón `cargando` / `error` / `datos` es el trío fundamental del manejo asíncrono en la UI: en cualquier momento, el componente está en uno de estos tres estados y la interfaz se renderiza en consecuencia.

### 3. HttpClient: el cliente HTTP de Angular

!!! info "HttpClient"
    El `HttpClient` es un wrapper sobre `fetch`/`XMLHttpRequest` que devuelve **observables** en lugar de promesas. Esto permite componer peticiones, cancelarlas, combinarlas y manejar errores de forma elegante con operadores RxJS.

Los métodos básicos:

```typescript
// GET: obtener recursos
this.http.get<Producto[]>(`${API_URL}/productos`);

// POST: crear un recurso
this.http.post<Producto>(`${API_URL}/productos`, nuevoProducto);

// PUT: reemplazar un recurso completo
this.http.put<Producto>(`${API_URL}/productos/1`, datosActualizados);

// PATCH: actualizar parcialmente
this.http.patch(`${API_URL}/productos/1`, { nombre: 'Nuevo nombre' });

// DELETE: eliminar
this.http.delete(`${API_URL}/productos/1`);
```

| Método | Uso | Ejemplo |
| ------ | --- | ------- |
| `GET` | Obtener recursos | `` this.http.get<Producto[]>(`${API_URL}/productos`); `` |
| `POST` | Crear un recurso | `` this.http.post<Producto>(`${API_URL}/productos`, nuevoProducto); `` |
| `PUT` | Reemplazar un recurso completo | `` this.http.put<Producto>(`${API_URL}/productos/1`, datosActualizados); `` |
| `PATCH` | Actualizar parcialmente | `` this.http.patch(`${API_URL}/productos/1`, { nombre: 'Nuevo nombre' }); `` |
| `DELETE` | Eliminar | `` this.http.delete(`${API_URL}/productos/1`); `` |

!!! warning "Sin .subscribe() no hay petición"
    Cada método devuelve un `Observable<T>` que hay que suscribir. Sin `.subscribe()`, la petición **no se ejecuta** (los observables son fríos por defecto).

### 4. Operadores RxJS esenciales para la UI

No hace falta dominar RxJS completo. Para el módulo de Diseño de Interfaces, cuatro operadores cubren el 90% de los casos:

**`map`:** transforma los datos antes de llegar al componente. Útil para extraer solo lo necesario de una respuesta grande.

```typescript
this.http.get<ClimaCompleto>(url).pipe(
  map(resp => ({
    temperatura: resp.current_weather.temperature,
    viento: resp.current_weather.windspeed,
    condicion: this.describirCondicion(resp.current_weather.weathercode)
  }))
).subscribe(data => this.resumen = data);
```

**`catchError`:** intercepta errores sin romper el flujo. Permite establecer un estado de error en el componente y devolver un valor vacío para que la app no crashee.

```typescript
import { catchError, of } from 'rxjs';

this.http.get<Producto[]>(url).pipe(
  catchError(err => {
    this.error = 'Error al cargar productos.';
    return of([]); // Devuelve array vacío como fallback
  })
).subscribe(productos => this.productos = productos);
```

**`tap`:** efectos secundarios sin transformar el dato. El caso de uso principal: setear `cargando = true` antes y `cargando = false` después.

```typescript
import { tap } from 'rxjs';

this.http.get(url).pipe(
  tap(() => this.cargando = true),
  map(data => data.items),
  tap(() => this.cargando = false)
).subscribe(items => this.items = items);
```

!!! tip "Buscadores: cambia a switchMap"
    **`switchMap`:** cuando se hace una nueva petición, cancela la anterior. Esencial en buscadores con autocompletado donde el usuario escribe rápido y no quieres que una respuesta vieja sobrescriba a una nueva.

```typescript
import { switchMap } from 'rxjs';
import { Subject } from 'rxjs';

// En un componente de búsqueda:
private termino$ = new Subject<string>();

constructor() {
  this.termino$.pipe(
    debounceTime(300), // Espera 300ms sin escritura
    switchMap(termino => this.servicio.buscar(termino))
  ).subscribe(resultados => this.resultados = resultados);
}

onInput(cambio: Event) {
  this.termino$.next((cambio.target as HTMLInputElement).value);
}
```

### 5. Manejo de errores: la interfaz siempre responde

!!! tip "La interfaz siempre responde"
    Un error de red o de servidor **nunca** debe dejar la interfaz en blanco o congelada. Los patrones recomendados son los siguientes:

**Error inline (banner):** para operaciones dentro de una sección de la página. Un banner rojo con el mensaje y un botón "Reintentar" que vuelve a ejecutar la petición.

```html
@if (error) {
  <div class="banner-error" role="alert">
    <span>{{ error }}</span>
    <button (click)="cargar()">Reintentar</button>
  </div>
}
```

**Pantalla de error:** para fallos críticos que impiden toda la funcionalidad. Un mensaje claro, una ilustración amigable y una acción de recuperación.

**Toast temporal:** para errores menores (un elemento no se pudo añadir al carrito pero el resto funciona). Aparece en la esquina, se autodestruye a los 4 segundos.

!!! tip "Regla de oro: mensajes comprensibles"
    El mensaje debe ser **comprensible para la persona usuaria**, no para un desarrollador. "No pudimos conectar con el servidor" es mejor que "Error 502: Bad Gateway". El detalle técnico va a la consola (`console.error(err)`), no a la UI.

### 6. CORS: el problema y su solución en desarrollo

!!! info "¿Qué es CORS?"
    Cuando el navegador hace una petición desde `http://localhost:4200` a `https://api.ejemplo.com`, el servidor de destino debe incluir la cabecera `Access-Control-Allow-Origin` para permitirlo. Si no la incluye, el navegador bloquea la respuesta (aunque la petición sí se envía).

En desarrollo, Angular CLI permite configurar un **proxy** que reenvía las peticiones desde el mismo origen, evitando CORS:

```json
// proxy.conf.json
{
  "/api": {
    "target": "https://jsonplaceholder.typicode.com",
    "secure": false,
    "pathRewrite": { "^/api": "" }
  }
}
```

```bash
ng serve --proxy-config proxy.conf.json
```

!!! tip "Proxy en desarrollo"
    En el código, se usa la URL relativa: `this.http.get('/api/products')` en lugar de la URL completa. En producción, el CORS debe resolverse en el servidor (cabeceras) o mediante un backend propio que actúe como intermediario.

## Ejemplos guiados

### Ejemplo 1: App de clima con Open-Meteo (API sin clave)

!!! example "Contexto pedagógico"
    Se construye una interfaz completa que obtiene datos del clima en tiempo real desde una API pública, mostrando el patrón completo: servicio → componente → template con estados. Se aplican los principios de jerarquía visual y feedback del usuario.

```typescript
// src/app/clima/clima.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { inject } from '@angular/core';

export interface ClimaActual {
  temperatura: number;
  sensacion: number;
  viento: number;
  direccionViento: number;
  condicion: string;
  icono: string;
}

@Injectable({ providedIn: 'root' })
export class ClimaService {
  private http = inject(HttpClient);
  private urlBase = 'https://api.open-meteo.com/v1/forecast';

  getClima(lat: number, lon: number): Promise<ClimaActual> {
    return this.http.get<any>(this.urlBase, {
      params: {
        latitude: String(lat),
        longitude: String(lon),
        current_weather: 'true'
      }
    }).toPromise().then(data => ({
      temperatura: data.current_weather.temperature,
      sensacion: data.current_weather.apparent_temperature,
      viento: data.current_weather.windspeed,
      direccionViento: data.current_weather.winddirection,
      condicion: this.describirCondicion(data.current_weather.weathercode),
      icono: this.iconoCondicion(data.current_weather.weathercode)
    }));
  }

  private describirCondicion(codigo: number): string {
    const condiciones: Record<number, string> = {
      0: 'Despejado', 1: 'Mayormente despejado', 2: 'Parcialmente nublado',
      3: 'Cubierto', 45: 'Niebla', 48: 'Niebla con escarcha',
      51: 'Llovizna ligera', 53: 'Llovizna', 55: 'Llovizna intensa',
      61: 'Lluvia ligera', 63: 'Lluvia', 65: 'Lluvia intensa',
      71: 'Nevada ligera', 73: 'Nevada', 80: 'Chubascos',
      95: 'Tormenta', 96: 'Tormenta con granizo'
    };
    return condiciones[codigo] ?? 'Desconocida';
  }

  private iconoCondicion(codigo: number): string {
    if (codigo === 0) return '☀️';
    if (codigo <= 2) return '🌤️';
    if (codigo === 3) return '☁️';
    if (codigo >= 45 && codigo <= 48) return '🌫️';
    if (codigo >= 51 && codigo <= 67) return '🌧️';
    if (codigo >= 71 && codigo <= 77) return '❄️';
    if (codigo >= 80 && codigo <= 82) return '🌦️';
    if (codigo >= 95) return '⛈️';
    return '🌡️';
  }
}
```

```typescript
// src/app/clima/clima.component.ts
import { Component, OnInit } from '@angular/core';
import { ClimaService, ClimaActual } from './clima.service';

@Component({
  selector: 'app-clima',
  templateUrl: './clima.component.html',
  styleUrls: ['./clima.component.scss'],
  standalone: true,
})
export class ClimaComponent implements OnInit {
  private climaService = this.climaService; // inyectado

  clima: ClimaActual | null = null;
  cargando = false;
  error: string | null = null;
  ciudad = 'Córdoba';

  constructor(private _climaService: ClimaService) {}

  ngOnInit() {
    this.cargar();
  }

  cargar() {
    this.cargando = true;
    this.error = null;

    // Coordenadas de Córdoba (40.4168, -3.7038)
    this.climaService.getClima(40.4168, -3.7038).then(data => {
      this.clima = data;
      this.cargando = false;
    }).catch(() => {
      this.error = 'No se pudo obtener el clima. Comprueba tu conexión.';
      this.cargando = false;
    });
  }

  get direccionCardinal(): string {
    if (!this.clima) return '';
    const dirs = ['N', 'NE', 'E', 'SE', 'S', 'SO', 'O', 'NO'];
    const idx = Math.round(this.clima.direccionViento / 45) % 8;
    return dirs[idx];
  }
}
```

```html
<!-- src/app/clima/clima.component.html -->
<section class="panel-clima">
  <header>
    <h1>{{ ciudad }}</h1>
    <small>Clima actual</small>
  </header>

  <!-- ESTADO: CARGANDO -->
  @if (cargando) {
    <div class="skeleton-clima" aria-busy="true" aria-label="Cargando datos del clima">
      <div class="skeleton-icono"></div>
      <div class="skeleton-temp"></div>
      <div class="skeleton-detalle"></div>
      <div class="skeleton-detalle corto"></div>
    </div>
  }

  <!-- ESTADO: ERROR -->
  @else if (error) {
    <div class="estado-error" role="alert">
      <span class="icono-error" aria-hidden="true">⚠️</span>
      <p>{{ error }}</p>
      <button class="btn-reintentar" (click)="cargar()">Reintentar</button>
    </div>
  }

  <!-- ESTADO: DATOS CARGADOS -->
  @else if (clima) {
    <div class="datos-clima">
      <div class="temperatura-bloque">
        <span class="icono" aria-hidden="true">{{ clima.icono }}</span>
        <span class="valor">{{ clima.temperatura | number:'1.0-0' }}°</span>
      </div>
      <p class="condicion">{{ clima.condicion }}</p>

      <div class="detalles">
        <div class="detalle">
          <small>Sensación térmica</small>
          <strong>{{ clima.sensacion | number:'1.0-0' }}°C</strong>
        </div>
        <div class="detalle">
          <small>Viento</small>
          <strong>{{ clima.viento | number:'1.0-0' }} km/h {{ direccionCardinal }}</strong>
        </div>
      </div>
    </div>
  }
</section>
```

```scss
// src/app/clima/clima.component.scss
.panel-clima {
  max-width: 400px;
  margin: 3rem auto;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 20px;
  padding: 2.5rem;
  color: white;
  box-shadow: 0 20px 60px rgba(102, 126, 234, 0.3);

  header {
    display: flex;
    align-items: baseline;
    justify-content: space-between;
    margin-bottom: 2rem;

    h1 {
      font-size: 1.75rem;
      font-weight: 800;
    }

    small {
      opacity: 0.7;
      font-size: 0.85rem;
    }
  }
}

// Skeleton loader
.skeleton-clima {
  .skeleton-icono {
    width: 64px;
    height: 64px;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.2);
    margin-bottom: 1rem;
    animation: pulso 1.5s ease-in-out infinite;
  }

  .skeleton-temp {
    width: 120px;
    height: 48px;
    border-radius: 8px;
    background: rgba(255, 255, 255, 0.2);
    margin-bottom: 1rem;
    animation: pulso 1.5s ease-in-out infinite 0.2s;
  }

  .skeleton-detalle {
    width: 80%;
    height: 16px;
    border-radius: 4px;
    background: rgba(255, 255, 255, 0.15);
    margin-bottom: 0.5rem;
    animation: pulso 1.5s ease-in-out infinite 0.4s;

    &.corto {
      width: 50%;
    }
  }
}

@keyframes pulso {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}

// Error
.estado-error {
  text-align: center;
  padding: 2rem 0;

  .icono-error {
    font-size: 2.5rem;
    display: block;
    margin-bottom: 1rem;
  }

  p {
    margin-bottom: 1.5rem;
    opacity: 0.9;
  }

  .btn-reintentar {
    background: rgba(255, 255, 255, 0.2);
    color: white;
    border: 1px solid rgba(255, 255, 255, 0.4);
    padding: 0.6rem 1.5rem;
    border-radius: 8px;
    font-weight: 600;
    cursor: pointer;
    transition: background 0.2s ease;

    &:hover {
      background: rgba(255, 255, 255, 0.3);
    }
  }
}

// Datos
.datos-clima {
  text-align: center;
}

.temperatura-bloque {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  margin-bottom: 0.5rem;

  .icono {
    font-size: 3.5rem;
  }

  .valor {
    font-size: 4rem;
    font-weight: 800;
    line-height: 1;
  }
}

.condicion {
  font-size: 1.1rem;
  opacity: 0.9;
  margin-bottom: 2rem;
}

.detalles {
  display: flex;
  gap: 1rem;
  justify-content: center;
}

.detalle {
  background: rgba(255, 255, 255, 0.1);
  border-radius: 12px;
  padding: 1rem 1.5rem;
  text-align: center;

  small {
    display: block;
    opacity: 0.7;
    font-size: 0.75rem;
    margin-bottom: 0.25rem;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }

  strong {
    font-size: 1.1rem;
  }
}

// Responsive
@media (max-width: 480px) {
  .panel-clima {
    margin: 1rem;
    padding: 1.5rem;
    border-radius: 16px;
  }

  .temperatura-bloque .valor {
    font-size: 3rem;
  }

  .detalles {
    flex-direction: column;
    gap: 0.75rem;
  }
}
```

!!! note "Explicación del resultado"
    Al ejecutar `ng serve`, se observa un panel con degradado morado-azul. Inicialmente muestra el skeleton (barras que pulsan). A los pocos segundos, se reemplaza por los datos reales del clima en Córdoba: icono grande, temperatura en números enormes, condición textual y dos tarjetas de detalle (sensación térmica y viento). Si se corta la conexión a internet, aparece el estado de error con el botón "Reintentar". En móvil, las tarjetas de detalle se apilan verticalmente.

### Ejemplo 2: Catálogo de productos con JSONPlaceholder (CRUD simulado)

!!! example "Contexto pedagógico"
    Se demuestra el ciclo completo CRUD contra una API REST simulada. El alumnado ve cómo los métodos HTTP se mapean a acciones de la interfaz y cómo el estado visual cambia tras cada operación.

```typescript
// src/app/productos/productos.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { inject } from '@angular/core';

export interface Producto {
  id?: number;
  title: string;
  price: number;
  description: string;
  category: string;
}

@Injectable({ providedIn: 'root' })
export class ProductosService {
  private http = inject(HttpClient);
  private url = 'https://jsonplaceholder.typicode.com/products';

  obtenerTodos() {
    return this.http.get<Producto[]>(this.url);
  }

  crear(datos: Producto) {
    return this.http.post<Producto>(this.url, datos);
  }

  actualizar(id: number, datos: Partial<Producto>) {
    return this.http.put<Producto>(`${this.url}/${id}`, datos);
  }

  eliminar(id: number) {
    return this.http.delete(`${this.url}/${id}`);
  }
}
```

```typescript
// src/app/productos/gestion-productos.component.ts
import { Component, OnInit } from '@angular/core';
import { ProductosService, Producto } from './productos.service';

@Component({
  selector: 'app-gestion-productos',
  templateUrl: './gestion-productos.component.html',
  styleUrls: ['./gestion-productos.component.scss'],
  standalone: true,
})
export class GestionProductosComponent implements OnInit {
  private servicio = this._servicio;

  productos: Producto[] = [];
  cargando = false;
  error: string | null = null;
  mensajeExito: string | null = null;

  // Formulario de nuevo producto
  nuevoProducto: Producto = { title: '', price: 0, description: '', category: '' };

  constructor(private _servicio: ProductosService) {}

  ngOnInit() {
    this.cargar();
  }

  cargar() {
    this.cargando = true;
    this.error = null;

    this.servicio.obtenerTodos().subscribe({
      next: (data) => {
        this.productos = data;
        this.cargando = false;
      },
      error: () => {
        this.error = 'No se pudieron cargar los productos.';
        this.cargando = false;
      }
    });
  }

  crear() {
    if (!this.nuevoProducto.title.trim()) return;

    this.servicio.crear(this.nuevoProducto).subscribe({
      next: (creado) => {
        this.productos.unshift(creado);
        this.nuevoProducto = { title: '', price: 0, description: '', category: '' };
        this.mostrarExito('Producto creado correctamente.');
      },
      error: () => this.error = 'Error al crear el producto.'
    });
  }

  eliminar(id: number) {
    this.servicio.eliminar(id).subscribe({
      next: () => {
        this.productos = this.productos.filter(p => p.id !== id);
        this.mostrarExito('Producto eliminado.');
      },
      error: () => this.error = 'Error al eliminar el producto.'
    });
  }

  private mostrarExito(msg: string) {
    this.mensajeExito = msg;
    setTimeout(() => this.mensajeExito = null, 3000);
  }
}
```

```html
<!-- src/app/productos/gestion-productos.component.html -->
<section class="panel-gestion">
  <h1>Gestión de productos</h1>

  <!-- Toast de éxito -->
  @if (mensajeExito) {
    <div class="toast-exito" role="status">{{ mensajeExito }}</div>
  }

  <!-- Error -->
  @if (error) {
    <div class="banner-error" role="alert">
      {{ error }}
      <button (click)="cargar()">Reintentar</button>
    </div>
  }

  <!-- Formulario de creación -->
  <form class="form-nuevo" (submit)="crear(); $event.preventDefault()">
    <h2>Añadir producto</h2>
    <div class="grid-campos">
      <input type="text" [(ngModel)]="nuevoProducto.title" name="title" placeholder="Nombre *" required>
      <input type="number" [(ngModel)]="nuevoProducto.price" name="price" placeholder="Precio" step="0.01" min="0">
      <input type="text" [(ngModel)]="nuevoProducto.category" name="category" placeholder="Categoría">
      <textarea [(ngModel)]="nuevoProducto.description" name="description" placeholder="Descripción" rows="2"></textarea>
    </div>
    <button type="submit" [disabled]="!nuevoProducto.title.trim()">Crear</button>
  </form>

  <!-- Lista -->
  @if (cargando) {
    <div class="skeleton-lista">
      @for (i of [1,2,3]; track $index) {
        <div class="skeleton-fila"></div>
      }
    </div>
  } @else {
    <ul class="lista-productos">
      @for (producto of productos; track producto.id) {
        <li class="fila-producto">
          <div class="info">
            <strong>{{ producto.title }}</strong>
            <small>{{ producto.category | uppercase }}</small>
          </div>
          <span class="precio">{{ producto.price | currency:'EUR':'1.2-2' }}</span>
          <button class="btn-eliminar" (click)="eliminar(producto.id!)" aria-label="Eliminar {{ producto.title }}">✕</button>
        </li>
      }
    </ul>
  }
</section>
```

!!! note "Explicación del resultado"
    Se observa una interfaz de gestión con un formulario en la parte superior y una lista de productos debajo. Al cargar, aparecen los 20 productos de JSONPlaceholder (simulados). Al crear uno nuevo, aparece al inicio de la lista con un toast de confirmación que desaparece a los 3 segundos. Al eliminar, la fila se remove y aparece el toast. Los estados de carga (skeleton) y error (banner con retry) están implementados. La pestaña Network de DevTools permite verificar cada petición HTTP y su respuesta.

## Actividades de práctica

1. **App de noticias:** Consumir la API de `https://newsapi.org` (requiere clave gratuita) o `https://hnrss.org/api/` (sin clave, noticias de Hacker News). Mostrar un feed de noticias con título, fuente, fecha (pipe `date`) e imagen. Añadir un filtro por categoría (botones que cambian el parámetro de la URL). Implementar los tres estados: skeleton al cargar, lista con datos, y error con retry.

2. **Buscador de países:** Usar la API `https://restcountries.com/v3.1/`. Crear un input de búsqueda con debounce (espera 500ms tras dejar de escribir) que filtre los países por nombre. Mostrar los resultados en una cuadrícula de tarjetas con bandera, nombre, población (pipe `number`) y capital. Usar `switchMap` para cancelar peticiones anteriores si el usuario sigue escribiendo.

3. **Comparativa de APIs:** Documentar en un informe breve las diferencias entre consumir JSONPlaceholder (CRUD simulado, datos fijos) y una API real como Open-Meteo (datos dinámicos, sin persistencia). ¿Qué implicaciones tiene esto para el diseño de la interfaz? ¿Cómo cambia el manejo de errores? ¿Cuándo es apropiado usar un mock vs una API real en desarrollo?

4. **Interceptores básicos:** Crear un interceptor que añada automáticamente un header `X-Requested-With: XMLHttpRequest` a todas las peticiones y que registre en consola cada petición (URL, método, tiempo de respuesta). Comprobar en DevTools que el header aparece y que los logs se muestran. Reflexionar: ¿cuándo usarías un interceptor para añadir tokens JWT de autenticación?
