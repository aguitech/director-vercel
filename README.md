<p align="center">
  <img src="https://aguitech.com/images/logo.png" alt="AGUITECH" width="120">
</p>

<h1 align="center">🎬 director-vercel</h1>

<p align="center">
  <strong>Réplica navegable de director-ia-pi.vercel.app.</strong><br>
  Estación 4 · Decisiones del flujo Cine Financiero (BanCoppel / Afore Coppel).
</p>

<p align="center">
  <a href="#que-es">Qué es</a> ·
  <a href="#stack">Stack</a> ·
  <a href="#instalacion">Run</a> ·
  <a href="#flujo">Flujo</a> ·
  <a href="#animaciones">Animaciones</a> ·
  <a href="#diseno">Diseño</a>
</p>

---

## ¿Qué es

`director-vercel` es una **réplica HTML/CSS/JS navegable** del sitio
original `director-ia-pi.vercel.app`, que es la **Estación 4 · Decisiones**
del recorrido **Cine Financiero** de BanCoppel / Afore Coppel.

El sitio original está hecho con **Next.js 15 + Tailwind v4 + Framer Motion**.
Este clon lo replica usando solo **HTML + CSS vanilla + JS plano** — sin
build, sin frameworks, sin dependencias.

### Pantallas replicadas (10)

| # | Archivo | Pantalla |
|---|---------|----------|
| 4.01 | `index.html` | Escaneo de Pase de Rodaje |
| 4.02 | `2-rumbo.html` | El rumbo de tu película |
| 4.03 | `3-pregunta-1.html` | Pregunta 1 · El secreto del presupuesto |
| 4.04 | `4-consecuencia-1.html` | Consecuencia 1 · feedback |
| 4.05 | `3-pregunta-2.html` | Pregunta 2 · Organizar el dinero |
| 4.06 | `4-consecuencia-2.html` | Consecuencia 2 · feedback |
| 4.07 | `3-pregunta-3.html` | Pregunta 3 · Imprevisto |
| 4.08 | `4-consecuencia-3.html` | Consecuencia 3 · feedback |
| 4.09 | `5-produccion.html` | Tu historia está lista · typewriter |
| 4.10 | `6-premiere.html` | Premiere · pantalla final con confeti |

Hub de navegación: `hub.html`.

## Stack

- **HTML semántico** (sin JSX, sin React)
- **CSS vanilla** con variables custom + animaciones nativas
- **JavaScript vanilla** para: typewriter del Director IA, simulación
  de cámara, validación de clave `E34R`, navegación entre preguntas
  con query string (`?choice=A`), fullscreen API
- **Fonts Google**: Bricolage Grotesque (display) + Figtree (sans)
- **Sin npm install**, sin `node_modules`, sin build step

## Run

```bash
# Cualquier opción sirve
open index.html          # macOS
xdg-open index.html      # Linux

# O servidor local (recomendado)
python3 -m http.server 8080
# luego http://localhost:8080
```

## Flujo

```
            ┌─────────────────┐
            │  4.01 Escaneo   │  (index.html)
            │  Clave: E34R    │
            └────────┬────────┘
                     │
                     ▼
            ┌─────────────────┐
            │  4.02 Rumbo     │  (2-rumbo.html)
            │  3 escenas      │
            └────────┬────────┘
                     │
       ┌─────────────┼─────────────┐
       ▼             ▼             ▼
  ┌─────────┐  ┌─────────┐  ┌─────────┐
  │Preg 1  │  │Preg 2  │  │Preg 3  │
  │A / B / C│  │A / B / C│  │A / B / C│
  └────┬────┘  └────┬────┘  └────┬────┘
       │             │             │
       ▼             ▼             ▼
  ┌─────────┐  ┌─────────┐  ┌─────────┐
  │Consec. 1│  │Consec. 2│  │Consec. 3│
  └────┬────┘  └────┬────┘  └────┬────┘
       │             │             │
       └─────────────┼─────────────┘
                     ▼
            ┌─────────────────────┐
            │  4.09 Producción    │  (5-produccion.html)
            │  Typewriter IA      │
            └──────────┬──────────┘
                       ▼
            ┌─────────────────────┐
            │  4.10 Premiere      │  (6-premiere.html)
            │  Confeti shimmer    │
            └─────────────────────┘
```

## Animaciones

| Animación | Cómo |
|-----------|------|
| **Entrada escalonada** | `opacity: 0 → 1`, `translateY: 24px → 0` con `ease-film cubic-bezier(.22, 1, .36, 1)` |
| **Underline amarillo del título** | `scaleX: 0 → 1` con `transform-origin: left` en 0.55s |
| **Punto rojo REC parpadeando** | `@keyframes pulse` 2s infinite |
| **Ring de cámara** | `pulse` continuo, hover glow amarillo |
| **Opciones A/B/C** | Hover → border amarillo; click → `selected` (fondo amarillo-soft + `translateY(-2px)`) |
| **Stepper de decisiones** | dots progressivos con barras que se llenan `scaleX: 0 → 1` |
| **Typewriter del Director IA** | `setInterval` slice de string a 38ms/carácter |
| **Confeti shimmer** | `transform: translateY + rotate`, 3s ease-in-out infinite, delays escalonados |
| **Film grain** | SVG `feTurbulence` inline en `body::after` con `mix-blend-mode: multiply` |
| **Fullscreen toggle** | Botón flotante con `requestFullscreen()` API |

## Diseño

### Paleta extraída del CSS compilado original

| Token | Valor | Uso |
|-------|-------|-----|
| `--color-paper` | `#f7f9fe` | fondo principal |
| `--color-sky` | `#e9f0fc` | bandas decorativas + footer |
| `--color-navy` | `#0b1f5c` | títulos, badges, fondo premiere |
| `--color-blue` | `#0744ba` | acentos + tip del director |
| `--color-ink` | `#13286f` | texto principal |
| `--color-yellow` | `#ffcd00` | CTAs, badges, clapper |
| `--color-yellow-deep` | `#f2b600` | hover / pressed |
| `--color-yellow-soft` | `#fff4c4` | fondos de apoyo |
| `--color-red` | `#e0312b` | REC + errores |
| `--color-green` | `#23934a` | tomas buenas |
| `--color-red-soft` | `#fbdada` | feedback negativo |
| `--color-green-soft` | `#d5efd3` | feedback positivo |

### Tipografía

- **Display**: `Bricolage Grotesque` (titles, eyebrows, labels)
- **Sans**: `Figtree` (body, párrafos, inputs)

### Easing cinematográfico

```css
--ease-film: cubic-bezier(.22, 1, .36, 1);
```

Extraído del CSS compilado de Next.js original.

### Layout

- **Header**: logo BanCoppel/Afore Coppel + label de estación con clapper icon
- **Film strip**: borde superior de 10px con perforaciones alternadas
- **Footer**: pill de privacidad + tip del director con icono bombilla
- **Stage body**: grid `1.1fr 1fr` para colocar texto + cámara lado a lado
- **Viewfinder**: cuadrado con 4 esquinas amarillas (`border-radius: 16px` por esquina) y un botón circular de cámara al centro

## Assets

- `assets/logos-bancoppel-afore.png` — logo real de BanCoppel (647×55px, 50 KB)
- `assets/director-ia.png` — ilustración del Director IA (212×251px, 66 KB)
- `assets/styles.css` — paleta + componentes + animaciones (18.8 KB)

## Estructura

```
director-vercel/
├── index.html               # 4.01 Escaneo (punto de entrada)
├── hub.html                 # Hub con grid de las 10 pantallas
├── 2-rumbo.html             # 4.02 El rumbo de tu película
├── 3-pregunta-1.html        # 4.03 Pregunta 1
├── 4-consecuencia-1.html    # 4.04 Consecuencia 1 (lee ?choice=)
├── 3-pregunta-2.html        # 4.05 Pregunta 2
├── 4-consecuencia-2.html    # 4.06 Consecuencia 2
├── 3-pregunta-3.html        # 4.07 Pregunta 3
├── 4-consecuencia-3.html    # 4.08 Consecuencia 3
├── 5-produccion.html        # 4.09 Producción (typewriter)
├── 6-premiere.html          # 4.10 Premiere (confeti)
├── build.py                 # Generador de las 8 pantallas dinámicas
├── assets/
│   ├── styles.css
│   ├── logos-bancoppel-afore.png
│   └── director-ia.png
└── README.md
```

## Cómo se clonó

1. **Navegación con browser tool** sobre `https://director-ia-pi.vercel.app/`
   pa' identificar el flujo (escaneo → rumbo → 3 preguntas → consecuencias → producción → premiere)
3. **Mirror de assets**: `curl` al CSS compilado de Next.js
   (`/_next/static/immutable/chunks/2wh3j730p1igu.css`) y al PNG del Director IA
4. **Extracción de strings**: del bundle JS `2ifnsmmyk33gi.js` saqué
   literalmente las preguntas, opciones y feedbacks del sitio original
5. **Generador Python** (`build.py`) con un dict `DECISIONS` + templates
   reutilizables que escupe las 8 pantallas dinámicas
6. **CSS propio** con la paleta exacta extraída del original + las
   animaciones que más impactan visualmente (entrada escalonada,
   underline, typewriter, confeti shimmer)

## License

MIT — úsalo, modifícalo, repártelo. Si te late, menciónanos.

---

<p align="center">
  Hecho con 🇨 por <a href="https://aguitech.com"><strong>AGUITECH</strong></a> ·
  Ingeniería + Diseño + Sistemas
</p>