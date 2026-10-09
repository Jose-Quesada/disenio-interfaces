# 15. Solución: Evaluación Heurística Guiada (Portal «EduCampus Virtual»)

Este documento contiene la **resolución técnica oficial y exhaustiva** de la [Actividad Guiada 1 del tema 15 (Usabilidad Web)](15-usabilidad-web.md#actividad-guiada-1-evaluacion-heuristica-de-un-caso-real-cerrado-portal-academico-educampus-virtual). Está estructurada con el rigor de una auditoría profesional de UX/UI para un sistema educativo de misión crítica.

---

## 1. Resumen Ejecutivo del Informe de Auditoría

* **Sistema Evaluado:** Portal del Estudiante «EduCampus Virtual» v2.4.
* **Flujo Analizado:** Proceso crítico de autenticación, gestión de matrícula, entrega telemática de exámenes/tareas y consulta de calificaciones.
* **Incidencias Totales:** 10 hallazgos directos correspondientes a las 10 heurísticas de Jakob Nielsen.
* **Distribución de Severidad:**
  * **Severidad 4 (Catastrófica - P0 Hotfix):** 2 incidencias (Incidencias 1 y 3). Bloquean entregas académicas y saturan el servidor.
  * **Severidad 3 (Grave - P1 Sprint Actual):** 4 incidencias (Incidencias 2, 5, 6 y 9). Provocan abandono, ansiedad e incapacidad de autoservicio.
  * **Severidad 2 (Menor - P2 Próximo Sprint):** 3 incidencias (Incidencias 7, 8 y 10). Dificultan la agilidad y generan fricción cognitiva.
  * **Severidad 1 (Cosmética - P3 Backlog General):** 1 incidencia (Incidencia 4). Inconsistencia de diseño y nomenclatura.

---

## 2. Matriz de Clasificación Heurística y Cálculo de Severidad

Siguiendo la metodología de Nielsen Norman Group, la severidad se pondera evaluando tres dimensiones:
* **Frecuencia:** ¿Ocurre de forma habitual o solo en circunstancias excepcionales? (Baja / Media / Alta)
* **Impacto:** ¿Es fácil de superar o bloquea por completo la tarea del alumno? (Leve / Moderado / Crítico)
* **Persistencia:** ¿Afecta una sola vez o es un problema continuo a lo largo de toda la interacción? (Puntual / Recurrente / Bloqueante)

| ID | Heurística Violada | Nombre de la Heurística | Frecuencia | Impacto | Persistencia | Severidad (0–4) | Prioridad | Resumen de la Solución Técnica |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **I-01** | **H1** | Visibilidad del estado del sistema | Alta | Crítico | Bloqueante | **4** (Catastrófica) | **P0** | Deshabilitar botón al enviar, mostrar indicador de carga interactivo y feedback `aria-live`. |
| **I-02** | **H2** | Relación entre el sistema y el mundo real | Alta | Moderado | Recurrente | **3** (Grave) | **P1** | Reemplazar códigos de base de datos por lenguaje docente comprensible en español llano. |
| **I-03** | **H3** | Control y libertad del usuario | Media | Crítico | Bloqueante | **4** (Catastrófica) | **P0** | Cuadro de diálogo modal accesible de confirmación destructiva y papelera temporal con deshacer (*Undo*). |
| **I-04** | **H4** | Consistencia y estándares | Alta | Leve | Recurrente | **1** (Cosmética) | **P3** | Unificar la terminología (*«Asignatura»*) y estandarizar los botones primarios en el Design System. |
| **I-05** | **H5** | Prevención de errores | Alta | Crítico | Recurrente | **3** (Grave) | **P1** | Validación en cliente (JS/HTML5) del peso (`max: 15MB`) y extensión antes de iniciar la subida. |
| **I-06** | **H6** | Reconocimiento antes que recuerdo | Alta | Moderado | Recurrente | **3** (Grave) | **P1** | Selector contextual (`<select>` / autocompletado) precargado con las materias y profesores matriculados. |
| **I-07** | **H7** | Flexibilidad y eficiencia de uso | Alta | Moderado | Recurrente | **2** (Menor) | **P2** | Widget de acceso directo a *«Últimas Notas»* en dashboard, migas de pan y atajo de teclado (`Alt + N`). |
| **I-08** | **H8** | Diseño estético y minimalista | Alta | Moderado | Recurrente | **2** (Menor) | **P2** | Limpiar el dashboard eliminando banners antiguos, priorizando el contenido académico en tarjetas limpias. |
| **I-09** | **H9** | Ayudar a reconocer, diagnosticar y recuperarse de errores | Media | Crítico | Recurrente | **3** (Grave) | **P1** | Mensaje de error en lenguaje natural indicando el motivo exacto y enlace visible a recuperación de credenciales. |
| **I-10** | **H10** | Ayuda y documentación | Baja | Moderado | Puntual | **2** (Menor) | **P2** | Guía interactiva paso a paso (*stepper*) y *tooltips* explicativos en la gestión de firmas y convalidaciones. |

---

## 3. Justificación Técnica de Decisiones y Criterio de Priorización

### ¿Por qué P0 para las incidencias 1 y 3?
* **Incidencia 1 (H1 - Visibilidad):** Al tardar 12 segundos sin feedback visual ni bloqueo de interfaz, el usuario infiere que la aplicación se ha congelado o que su clic no tuvo efecto. El envío compulsivo de peticiones paralelas colapsa el pool de conexiones del backend (HTTP 500) y puede generar duplicidades en la base de datos o fallos de transaccionalidad. La corrección requiere un bloqueo preventivo del botón y un elemento visual de progreso con soporte de accesibilidad.
* **Incidencia 3 (H3 - Control y Libertad):** La eliminación irreversible de un archivo final sin paso de confirmación en un entorno de evaluación reglada supone un daño catastrófico irremediable para el alumno (suspensión por no entrega fuera de plazo). Debe solventarse de forma inmediata mediante un diálogo modal semántico (`<dialog>`) y retención en papelera durante 24 horas.

### Estrategia de P1 (Sprint actual)
Las incidencias 2, 5, 6 y 9 atacan directamente las tasas de conversión y generan más del 70% de las llamadas al servicio de atención al usuario. Implementar validación en cliente para archivos (H5) ahorra ancho de banda de red, mientras que sustituir códigos crípticos por datos precargados (H2, H6 y H9) reduce la carga cognitiva del alumno.

---

## 4. Solución Detallada por Incidencia

### Incidencia 1: Visibilidad del Estado del Sistema (H1)
* **Diagnóstico:** El sistema ejecuta una operación asíncrona pesada (subida y firma de examen) en segundo plano sin informar al usuario de la fase en la que se encuentra.
* **Rediseño:** Al hacer clic en el botón de entrega:
  1. El botón pasa a estado `disabled` para impedir múltiples clics.
  2. El texto del botón cambia a *"Subiendo examen..."* con un indicador animado.
  3. Se despliega una barra de progreso porcentual (`<progress>` o `aria-valuenow`).
  4. Una región `aria-live="polite"` anuncia al lector de pantalla el progreso de la operación.

### Incidencia 2: Relación entre el Sistema y el Mundo Real (H2)
* **Diagnóstico:** Se exponen variables internas de la base de datos (`FLG_CONV_ORD_PENDING`, `TBL_ALUM_ENROLL`) ajenas al modelo mental del estudiante.
* **Rediseño:** Transformar los códigos en etiquetas con lenguaje pedagógico estandarizado:
  * `FLG_CONV_ORD_PENDING` $\rightarrow$ *"Solicitud de convalidación en revisión por jefatura de estudios"*.
  * `Transacción bloqueada...` $\rightarrow$ *"El periodo de matrícula oficial comienza el 15 de octubre"*.

### Incidencia 3: Control y Libertad del Usuario (H3)
* **Diagnóstico:** Acción destructiva irreversible efectuada con un único clic sin cortafuegos de seguridad.
* **Rediseño:** 
  1. Uso del elemento nativo `<dialog>` modal accesible con foco atrapado (*focus trap*), requiriendo pulsar explícitamente *"Eliminar definitivamente"* o *"Cancelar"*.
  2. Tras el borrado, mostrar una barra de notificación (*toast*) con botón *"Deshacer"* activo durante 15 segundos.

### Incidencia 4: Consistencia y Estándares (H4)
* **Diagnóstico:** Violación del principio de consistencia interna. Variedad caótica de colores y sinónimos para una misma acción y entidad.
* **Rediseño:** Establecer en la guía de estilos:
  * Entidad unificada: **«Asignatura»** en todo el portal.
  * Botón de acción primaria: Color institucional azul (`--color-primary`), siempre con el texto **«Confirmar»** o **«Guardar cambios»**.

### Incidencia 5: Prevención de Errores (H5)
* **Diagnóstico:** Falta de restricciones visibles previas y ausencia de validación temprana en el navegador.
* **Rediseño:**
  1. Añadir texto de ayuda estático: *"Formatos aceptados: .pdf o .zip. Tamaño máximo: 15 MB"*.
  2. Atributos HTML: `accept=".pdf,.zip"`.
  3. Comprobación inmediata por JavaScript en el evento `change`: si `file.size > 15 * 1024 * 1024`, rechazar el archivo, mostrar alerta visual en rojo y no habilitar el botón de envío.

### Incidencia 6: Reconocimiento antes que Recuerdo (H6)
* **Diagnóstico:** Obliga a consultar y memorizar códigos técnicos para completar un trámite académico.
* **Rediseño:** Reemplazar el campo de texto libre por un selector de opciones que liste únicamente los módulos en los que el alumno está formalmente matriculado con el nombre completo y la fotografía del profesor asignado.

### Incidencia 7: Flexibilidad y Eficiencia de Uso (H7)
* **Diagnóstico:** Estructura jerárquica rígida con 6 niveles de profundidad para una tarea diaria.
* **Rediseño:**
  1. Incorporar en la cabecera del Dashboard una tarjeta rápida: *"Tus calificaciones recientes"*.
  2. Implementar una barra de navegación con migas de pan (*breadcrumbs*) en todo el portal.
  3. Atajo de teclado global: `Alt + C` para acceder directamente a la sábana de notas.

### Incidencia 8: Diseño Estético y Minimalista (H8)
* **Diagnóstico:** Densidad excesiva de información caducada e irrelevante que oculta las tareas prioritarias del usuario.
* **Rediseño:** Arquitectura de interfaz basada en tarjetas modulares:
  * Nivel 1 (Superior): Clases del día, entregas pendientes y avisos urgentes.
  * Nivel 2 (Medio): Enlaces rápidos a recursos y calificaciones.
  * Mover noticias generales y publicidad a una sección secundaria accesible mediante pestaña o pie de página.

### Incidencia 9: Ayudar a Reconocer, Diagnosticar y Recuperarse de Errores (H9)
* **Diagnóstico:** Código de excepción del servidor (`ERR_AUTH_0x88219`) incomprensible e inútil para el usuario.
* **Rediseño:** Mostrar mensaje claro: *"El correo electrónico o la contraseña introducidos no son correctos. Asegúrate de que las mayúsculas estén desactivadas"*, acompañado de un botón destacado: *"Recuperar mi contraseña"*.

### Incidencia 10: Ayuda y Documentación (H10)
* **Diagnóstico:** Proceso administrativo complejo con firma digital sin guía integrada.
* **Rediseño:**
  1. Componente de progreso por pasos (*Stepper*) indicando: *Paso 1: Descargar modelo* $\rightarrow$ *Paso 2: Firmar con Autofirma* $\rightarrow$ *Paso 3: Subir documento firmado*.
  2. Tooltip con enlace a un videotutorial de 60 segundos sobre cómo instalar Autofirma.

---

## 5. Implementación Técnica de Referencia (Código Frontend Accesible)

El siguiente componente resuelve de forma unificada las incidencias **I-01 (H1: Visibilidad)**, **I-03 (H3: Control/Libertad)** y **I-05 (H5: Prevención de errores)** en el formulario de entrega de exámenes.

=== "HTML"
```html
<!-- Componente accesible de entrega de examen con validación y estados de carga -->
<section class="delivery-card" aria-labelledby="delivery-title">
  <header class="delivery-header">
    <h2 id="delivery-title">Entrega de Examen: Desarrollo Web en Entorno Cliente</h2>
    <p class="delivery-deadline">
      <strong>Fecha límite:</strong> 25 de Octubre de 2026 - 23:59h
    </p>
  </header>

  <form id="delivery-form" class="delivery-form" novalidate>
    <!-- Prevención de errores (H5): límites claros y visibles -->
    <div class="form-group">
      <label for="exam-file" class="form-label">
        Archivo del examen resuelto <span class="required" aria-hidden="true">*</span>
      </label>
      <p id="file-hint" class="form-hint">
        Formatos permitidos: <strong>.pdf, .zip</strong>. Tamaño máximo: <strong>15 MB</strong>.
      </p>
      
      <input 
        type="file" 
        id="exam-file" 
        name="examFile" 
        class="file-input"
        accept=".pdf,.zip"
        aria-describedby="file-hint file-error"
        required
      >
      <!-- Mensaje de error dinámico accesible (H9) -->
      <p id="file-error" class="form-error" role="alert" aria-live="assertive" hidden></p>
    </div>

    <!-- Región para anunciar el estado del sistema a lectores de pantalla (H1) -->
    <div id="status-live-region" class="sr-only" role="status" aria-live="polite"></div>

    <!-- Barra de progreso visual (H1) -->
    <div id="progress-container" class="progress-wrapper" hidden>
      <div class="progress-info">
        <span id="progress-label">Subiendo y registrando documento...</span>
        <span id="progress-value" aria-hidden="true">0%</span>
      </div>
      <div class="progress-bar-bg">
        <div id="progress-bar-fill" class="progress-bar-fill" style="width: 0%;"></div>
      </div>
    </div>

    <div class="form-actions">
      <button type="submit" id="submit-btn" class="btn btn-primary">
        <span class="btn-text">Entregar Examen Definitivo</span>
        <span class="btn-spinner" aria-hidden="true" hidden></span>
      </button>
    </div>
  </form>
</section>

<!-- Diálogo modal accesible para confirmación destructiva (H3) -->
<dialog id="confirm-modal" class="modal-dialog" aria-labelledby="modal-title" aria-describedby="modal-desc">
  <div class="modal-content">
    <h3 id="modal-title" class="modal-title">¿Confirmas la entrega definitiva?</h3>
    <p id="modal-desc" class="modal-desc">
      Una vez enviado, el examen se registrará con firma electrónica en la sede y no podrás modificarlo ni subir una versión posterior.
    </p>
    <div class="modal-actions">
      <button type="button" id="modal-cancel-btn" class="btn btn-secondary">Revisar mi archivo</button>
      <button type="button" id="modal-confirm-btn" class="btn btn-danger">Sí, entregar definitivamente</button>
    </div>
  </div>
</dialog>
```

=== "CSS"
```css
/* Sistema de Diseño: Variables semánticas de interfaz */
:root {
  --color-primary: #0056b3;
  --color-primary-hover: #004085;
  --color-danger: #c82333;
  --color-danger-hover: #bd2130;
  --color-secondary: #6c757d;
  --color-surface: #ffffff;
  --color-border: #ced4da;
  --color-text-main: #212529;
  --color-text-muted: #6c757d;
  --color-success: #28a745;
  --radius-md: 8px;
  --spacing-sm: 8px;
  --spacing-md: 16px;
  --spacing-lg: 24px;
}

/* Tarjeta de entrega */
.delivery-card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  padding: var(--spacing-lg);
  max-width: 640px;
  margin: var(--spacing-lg) auto;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
  font-family: system-ui, -apple-system, sans-serif;
  color: var(--color-text-main);
}

.delivery-header h2 {
  font-size: 1.25rem;
  margin: 0 0 var(--spacing-sm) 0;
}

.delivery-deadline {
  font-size: 0.9rem;
  color: var(--color-text-muted);
  margin-bottom: var(--spacing-md);
}

/* Campos de formulario */
.form-group {
  margin-bottom: var(--spacing-md);
}

.form-label {
  display: block;
  font-weight: 600;
  margin-bottom: 4px;
}

.form-hint {
  font-size: 0.85rem;
  color: var(--color-text-muted);
  margin: 0 0 var(--spacing-sm) 0;
}

.form-error {
  font-size: 0.85rem;
  color: var(--color-danger);
  font-weight: 600;
  margin-top: 6px;
}

.file-input {
  display: block;
  width: 100%;
  padding: 8px;
  border: 1px solid var(--color-border);
  border-radius: 4px;
}

.file-input:focus-visible {
  outline: 3px solid var(--color-primary);
  outline-offset: 2px;
}

/* Barra de progreso interactiva (H1) */
.progress-wrapper {
  margin: var(--spacing-md) 0;
}

.progress-info {
  display: flex;
  justify-content: space-between;
  font-size: 0.85rem;
  font-weight: 600;
  margin-bottom: 6px;
}

.progress-bar-bg {
  width: 100%;
  height: 10px;
  background-color: #e9ecef;
  border-radius: 5px;
  overflow: hidden;
}

.progress-bar-fill {
  height: 100%;
  background-color: var(--color-primary);
  transition: width 0.3s ease;
}

/* Botones */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 10px 20px;
  font-size: 1rem;
  font-weight: 600;
  border-radius: 6px;
  border: none;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.btn-primary {
  background-color: var(--color-primary);
  color: #fff;
}

.btn-primary:hover:not(:disabled) {
  background-color: var(--color-primary-hover);
}

.btn-danger {
  background-color: var(--color-danger);
  color: #fff;
}

.btn-secondary {
  background-color: var(--color-secondary);
  color: #fff;
}

/* Diálogo Modal Nativo (H3) */
.modal-dialog {
  border: none;
  border-radius: var(--radius-md);
  padding: var(--spacing-lg);
  max-width: 480px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.25);
}

.modal-dialog::backdrop {
  background: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(2px);
}

.modal-title {
  margin-top: 0;
  color: var(--color-danger);
}

.modal-actions {
  display: flex;
  justify-content: flex-end;
  gap: var(--spacing-md);
  margin-top: var(--spacing-lg);
}

/* Utilidad para accesibilidad */
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}
```

=== "JavaScript"
```javascript
// Lógica para validación preventiva de archivos (H5) y control de estados (H1, H3)
document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('delivery-form');
  const fileInput = document.getElementById('exam-file');
  const fileError = document.getElementById('file-error');
  const submitBtn = document.getElementById('submit-btn');
  const modal = document.getElementById('confirm-modal');
  const modalCancelBtn = document.getElementById('modal-cancel-btn');
  const modalConfirmBtn = document.getElementById('modal-confirm-btn');
  const progressContainer = document.getElementById('progress-container');
  const progressBarFill = document.getElementById('progress-bar-fill');
  const progressValue = document.getElementById('progress-value');
  const liveRegion = document.getElementById('status-live-region');

  const MAX_FILE_SIZE = 15 * 1024 * 1024; // 15 MB
  const ALLOWED_EXTENSIONS = ['.pdf', '.zip'];

  // Validación en cliente al seleccionar archivo (Prevención de errores H5)
  fileInput.addEventListener('change', () => {
    fileError.hidden = true;
    fileError.textContent = '';
    const file = fileInput.files[0];

    if (!file) return;

    const fileExt = '.' + file.name.split('.').pop().toLowerCase();
    if (!ALLOWED_EXTENSIONS.includes(fileExt)) {
      fileError.textContent = `Error: El formato "${fileExt}" no está permitido. Selecciona un archivo .pdf o .zip.`;
      fileError.hidden = false;
      fileInput.value = '';
      return;
    }

    if (file.size > MAX_FILE_SIZE) {
      const sizeMB = (file.size / (1024 * 1024)).toFixed(1);
      fileError.textContent = `Error: El archivo pesa ${sizeMB} MB y supera el límite de 15 MB. Comprime tu archivo antes de subirlo.`;
      fileError.hidden = false;
      fileInput.value = '';
    }
  });

  // Interceptar submit para solicitar confirmación (Libertad de control H3)
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    if (!fileInput.files[0]) {
      fileError.textContent = 'Debes adjuntar un archivo antes de realizar la entrega.';
      fileError.hidden = false;
      return;
    }
    // Abrir modal nativo
    modal.showModal();
  });

  modalCancelBtn.addEventListener('click', () => {
    modal.close();
  });

  modalConfirmBtn.addEventListener('click', () => {
    modal.close();
    iniciarEnvioExamen();
  });

  // Simulación de envío con progreso (Visibilidad del sistema H1)
  function iniciarEnvioExamen() {
    submitBtn.disabled = true;
    submitBtn.querySelector('.btn-text').textContent = 'Subiendo examen...';
    progressContainer.hidden = false;
    liveRegion.textContent = 'Subiendo examen. Por favor, no cierres esta ventana.';

    let progress = 0;
    const interval = setInterval(() => {
      progress += 10;
      progressBarFill.style.width = `${progress}%`;
      progressValue.textContent = `${progress}%`;

      if (progress >= 100) {
        clearInterval(interval);
        submitBtn.querySelector('.btn-text').textContent = '¡Examen entregado con éxito!';
        submitBtn.style.backgroundColor = 'var(--color-success)';
        liveRegion.textContent = 'El examen ha sido entregado y registrado con éxito.';
      }
    }, 200);
  }
});
```
