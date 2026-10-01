#!/usr/bin/env python3
"""build.py — Genera las pantallas del flujo de Decisiones (4.03 a 4.13)."""
from pathlib import Path

BASE = Path(__file__).parent.resolve()

HEAD = '''<!DOCTYPE html>
<html lang="es-MX">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no, viewport-fit=cover">
  <meta name="theme-color" content="#0b1f5c">
  <title>__TITLE__ · Cine Financiero</title>
  <link rel="stylesheet" href="assets/styles.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@600;700;800&family=Figtree:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="icon" href="assets/logos-bancoppel-afore.png">
</head>
<body>
  <div class="stage">
    <div class="bg-deco" aria-hidden="true">
      <div class="circle-1"></div><div class="circle-2"></div><div class="circle-3"></div><div class="circle-4"></div>
    </div>
    <div class="film-strip"></div>

    <header class="app-header">
      <div class="app-header-inner">
        <div class="brand-logo"><img src="assets/logos-bancoppel-afore.png" alt="BanCoppel | Afore Coppel"></div>
        <div class="section-tag">
          <span class="clapper-icon">
            <svg viewBox="0 0 24 24" width="62%" height="62%" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 10h18v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><path d="m3.4 9.7-.6-2.4a1 1 0 0 1 .7-1.2l15-3.9a1 1 0 0 1 1.2.7l.6 2.4z"/><path d="m7.5 5 2.6 3.4M12.5 3.7l2.6 3.4"/><path d="m12 12.6.9 1.9 2 .3-1.5 1.4.4 2-1.8-1-1.8 1 .4-2-1.5-1.4 2-.3z"/></svg>
          </span>
          Decisiones <span class="yellow-dot">·</span> 4
        </div>
      </div>
    </header>

    <section class="stage-body">__BODY__</section>

    <footer class="app-footer">
      <div class="footer-block">
        <span class="icon-circle">
          <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3 5 6v5.5c0 4.3 3 7.9 7 9.5 4-1.6 7-5.2 7-9.5V6z"/><path d="m9 12 2 2 4-4"/></svg>
        </span>
        <p class="text-navy">Tu información está protegida.<br>Consulta el Aviso de privacidad.</p>
      </div>
      <div class="footer-block">
        <svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="var(--color-yellow-deep)" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18h6M10 21h4"/><path d="M12 3a6 6 0 0 0-3.6 10.8c.7.5 1.1 1.3 1.1 2.2h5c0-.9.4-1.7 1.1-2.2A6 6 0 0 0 12 3z"/></svg>
        <p><span class="label text-blue">Tip del Director</span><br><span class="italic text-blue">Tú eres el protagonista.</span></p>
      </div>
    </footer>
  </div>

  <button class="fullscreen-btn" id="fsBtn" type="button" title="Pantalla completa">
    <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 9V4h5M20 9V4h-5M4 15v5h5M20 15v5h-5"/></svg>
  </button>
__EXTRA_JS__
</body>
</html>
'''

def write(filename, title, body, extra_js=''):
    out = BASE / filename
    out.write_text(HEAD.replace('__TITLE__', title).replace('__BODY__', body).replace('__EXTRA_JS__', extra_js))
    print(f"  ✓ {filename}")


# ============== DECISIONES ==============

DECISIONS = [
    {
        'id': 1,
        'question': 'Quieres convertir tu sueño en meta. ¿Cuál es el secreto para hacer un presupuesto exitoso?',
        'correct': 'C',
        'options': [
            ('A', 'Registrar detalladamente cada gasto que hiciste durante el mes.'),
            ('B', 'Recortar al máximo los gustos para ahorrar más.'),
            ('C', 'Diseñar un plan con mis ingresos y gastos y apegarme a él.'),
        ],
        'feedbacks': {
            'C': ('ok', 'Aprendió que el secreto es planear antes de gastar.', 'diseñó un plan con sus ingresos y gastos y se apegó a él'),
            'A': ('bad', 'Registrar gastos es mirar al pasado. El presupuesto es planear antes de usar tu dinero.', 'anotó con detalle cada gasto del mes, pero no planeó a dónde iría su dinero'),
            'B': ('bad', 'Un plan muy estricto es difícil de mantener. La clave es el equilibrio, no la prohibición.', 'se prohibió todos los gustos y el plan se volvió difícil de sostener'),
        },
        'result_titles': {'C': '¡Toma buena!', 'A': 'Aprende del paisaje', 'B': 'Aprende del paisaje'},
        'result_subtitles': {
            'C': 'Planeas, tomas el control y te olvidas del estrés.',
            'A': 'Sabes en qué se fue tu dinero, pero no decides a dónde va.',
            'B': 'Ahorras unos días, pero tu meta se vuelve una carga.',
        },
        'next_q': 2,
    },
    {
        'id': 2,
        'question': 'Tienes una meta clara por cumplir. ¿Cómo organizas tu dinero cuando lo recibes?',
        'correct': 'A',
        'options': [
            ('A', 'Primero separo lo que quiero ahorrar; lo demás lo gasto.'),
            ('B', 'Primero gasto y lo que sobre se ahorra.'),
            ('C', 'Celebro invitando a todos a comer.'),
        ],
        'feedbacks': {
            'A': ('ok', 'Separar el ahorro desde el principio garantiza que logres avanzar hacia tu meta.', 'separó primero lo que quería ahorrar y gastó el resto'),
            'B': ('bad', 'Si esperas a ver qué sobra, otros gastos pueden llevarse ese dinero.', 'gastó primero y esperó a que algo sobrara para ahorrar'),
            'C': ('bad', 'Es bueno celebrar, pero separar tu ahorro es clave para darte premios más grandes.', 'celebró invitando a todos a comer y su meta se quedó sin ahorro'),
        },
        'result_titles': {'A': '¡Toma buena!', 'B': 'Aprende del paisaje', 'C': 'Aprende del paisaje'},
        'result_subtitles': {
            'A': 'Separar primero tu ahorro asegura que tu meta avance cada mes.',
            'B': 'Lo que sobra casi nunca llega: tu meta se queda esperando.',
            'C': 'La fiesta estuvo buena, pero tu meta se quedó sin presupuesto.',
        },
        'next_q': 3,
    },
    {
        'id': 3,
        'question': 'Estás ahorrando para tu sueño y aparece un gasto urgente e inesperado. ¿Cómo lo pagas?',
        'correct': 'A',
        'options': [
            ('A', 'Uso mi fondo separado para emergencias.'),
            ('B', 'Uso el dinero destinado para mi meta.'),
            ('C', 'Pido un crédito.'),
        ],
        'feedbacks': {
            'A': ('ok', 'Tener un fondo para imprevistos te protege sin endeudarte ni sacarte de tus metas.', 'cubrió el imprevisto con su fondo para emergencias'),
            'B': ('bad', 'Tomar el dinero de tu meta resuelve hoy, pero te regresa varios pasos.', 'tomó el dinero de su meta para cubrir el imprevisto'),
            'C': ('bad', 'Endeudarte hace que la emergencia te salga más cara.', 'se endeudó para cubrir el imprevisto'),
        },
        'result_titles': {'A': '¡Toma buena!', 'B': '¡Corte!', 'C': '¡Corte!'},
        'result_subtitles': {
            'A': 'Tu fondo de emergencias hizo su trabajo y tu meta sigue intacta.',
            'B': 'Saliste del apuro, pero ahora tienes una deuda que pagar.',
            'C': 'Resolverías la emergencia, pero retrasarías tu meta.',
        },
        'next_q': None,
    },
]


def stepper(active):
    """active = número del step activo, 1-3."""
    html = ['<div class="stepper">']
    for i in range(1, 4):
        if i > 1:
            cls = 'bar active' if i <= active else 'bar'
            html.append(f'<div class="{cls}"></div>')
        if i < active:
            cls = 'dot done'
        elif i == active:
            cls = 'dot active'
        else:
            cls = 'dot'
        html.append(f'<div class="{cls}"></div>')
    html.append('</div>')
    return ''.join(html)


def page_pregunta(d):
    body_lines = [
        '<div class="card">',
        stepper(d['id']),
        '<span class="eyebrow">Decisión ' + str(d['id']) + ' de 3</span>',
        '<h1 class="t-hero" style="margin-top:14px; font-size:clamp(1.8rem, 4vh, 2.8rem);">',
        '<span class="underline-anim">' + d['question'].split('?')[0].split('.')[0] + '.</span>',
        '</h1>',
        '<p class="t-body" style="font-size:clamp(1.05rem, 2.4vh, 1.2rem); max-width:60ch; margin-top:1.5vh; opacity:.85;">',
        d['question'],
        '</p>',
        '<div class="options" id="opts">',
    ]
    for letter, text in d['options']:
        body_lines.append(
            '<div class="option" data-letter="' + letter + '" onclick="selectOption(this, \'' + letter + '\')">'
            '<span class="letter">' + letter + '</span>'
            '<span class="opt-text">' + text + '</span>'
            '</div>'
        )
    body_lines.extend([
        '</div>',
        '<a class="cta cta-primary cta-block" id="confirmBtn" href="#" style="opacity:.4; pointer-events:none;">'
        'Elige una respuesta</a>',
        '<div style="margin-top:18px; display:flex; align-items:center; gap:12px; padding:14px 18px; background:var(--color-yellow-soft); border-radius:12px;">'
        '<div class="director-avatar" style="width:48px; height:48px; border-radius:12px;">'
        '<img src="assets/director-ia.png" alt=""></div>'
        '<div>'
        '<span class="director-tag">Director IA</span>'
        '<p class="director-msg" style="font-size:0.9rem;">Tómate tu tiempo. Piensa como si fuera tu sueño el que está en juego.</p>'
        '</div></div>',
        '</div>',
    ])
    body = '\n          '.join(body_lines)

    js = '''
  <script>
    function selectOption(el, letter) {
      document.querySelectorAll('#opts .option').forEach(function(o){ o.classList.remove('selected'); });
      el.classList.add('selected');
      var btn = document.getElementById('confirmBtn');
      btn.style.opacity = '1';
      btn.style.pointerEvents = 'auto';
      btn.href = '4-consecuencia-__DECID__ + '.html?choice=' + letter;
      btn.textContent = 'Confirmar mi decisión';
    }
  </script>
'''.replace('__DECID__', str(d['id']) + ".html?choice='").replace("+ letter;", "+ letter;")
    write(f'3-pregunta-{d["id"]}.html', f'Pregunta {d["id"]}', body, extra_js=js)


def page_consecuencia(d):
    nxt = '5-produccion.html' if d['next_q'] is None else f'3-pregunta-{d["next_q"]}.html'

    options_js = '{' + ', '.join([f'"{l}":{repr(t)}' for l, t in d['options']]) + '}'
    feedbacks_js = '{' + ', '.join([f'"{l}":[{t[0]!r},{t[1]!r},{t[2]!r}]' for l, t in d['feedbacks'].items()]) + '}'
    titles_js = '{' + ', '.join([f'"{l}":{repr(t)}' for l, t in d['result_titles'].items()]) + '}'
    subtitles_js = '{' + ', '.join([f'"{l}":{repr(t)}' for l, t in d['result_subtitles'].items()]) + '}'

    body = '''
      <div class="card" id="card">
          <span class="eyebrow" id="eyebrow">
              <span class="dot-red"></span> Decisión __DID__ de 3
          </span>

          <div style="display:flex; align-items:center; gap:14px; margin-top:14px;">
              <span style="display:grid; place-items:center; width:64px; height:64px; border-radius:50%; background:var(--color-yellow); color:var(--color-navy); font-family:var(--font-display); font-weight:800; font-size:1.5rem;" id="letterBadge">C</span>
              <h1 class="t-hero" id="title" style="margin-top:0; font-size:clamp(1.6rem, 3.8vh, 2.6rem);">¡Toma buena!</h1>
          </div>

          <p class="t-body" id="subtitle" style="font-size:clamp(1.05rem, 2.4vh, 1.2rem); max-width:60ch; margin-top:2vh; opacity:.85;">
              Planeas, tomas el control y te olvidas del estrés.
          </p>

          <div id="feedbacks" style="margin-top:18px;"></div>

          <a class="cta cta-primary cta-block" id="continueBtn" href="__NEXT__" style="margin-top:24px;">
              Siguiente decisión
              <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 5l7 7-7 7"/></svg>
          </a>

          <div style="margin-top:18px; padding:14px 18px; background:var(--color-white); border:1px solid var(--color-sky); border-radius:12px;">
              <p style="font-family:var(--font-display); font-weight:800; font-size:0.8rem; letter-spacing:1.5px; color:var(--color-blue); text-transform:uppercase; margin-bottom:6px;">Director IA</p>
              <p id="directorMsg" class="director-msg" style="font-size:0.9rem;">Tu fondo de emergencias hizo su trabajo y tu meta sigue intacta.</p>
          </div>
        </div>
'''.replace('__DID__', str(d['id'])).replace('__NEXT__', nxt)

    js = '''
  <script>
    var OPTIONS = __OPTIONS__;
    var FEEDBACKS = __FEEDBACKS__;
    var TITLES = __TITLES__;
    var SUBTITLES = __SUBTITLES__;
    var params = new URLSearchParams(location.search);
    var choice = (params.get('choice') || '__CORRECT__').toUpperCase();
    var correct = '__CORRECT__';
    var isOk = choice === correct;

    document.getElementById('letterBadge').textContent = choice;
    document.getElementById('title').textContent = TITLES[choice];
    document.getElementById('subtitle').textContent = SUBTITLES[choice];

    var fbEl = document.getElementById('feedbacks');
    var mine = FEEDBACKS[choice];
    var labelMap = {ok:'¡Correcto!', bad:'Aprende del paisaje'};
    var iconMap = {ok:'\\u2713', bad:'\\u2715'};
    fbEl.innerHTML = '<div class="feedback ' + mine[0] + '">' +
        '<span class="icon">' + iconMap[mine[0]] + '</span>' +
        '<div><strong>' + choice + ' \\u2014 ' + labelMap[mine[0]] + '</strong> ' +
        mine[2] + '. ' + mine[1] + '</div>' +
    '</div>';

    var badge = document.getElementById('letterBadge');
    if (isOk) { badge.style.background = 'var(--color-green)'; badge.style.color = '#fff'; }
    else { badge.style.background = 'var(--color-red)'; badge.style.color = '#fff'; }

    var did = '__DID__';
    var dirMsg = isOk
      ? 'Aprendi\\u00f3 que el secreto es planear antes de gastar.'
      : (correct === 'C' && did === '1' ? 'Aprendi\\u00f3 que el secreto es planear antes de gastar.' :
         correct === 'A' && did === '2' ? 'Aprendi\\u00f3 que el ahorro se separa primero, no al final.' :
         correct === 'A' && did === '3' ? 'Descubri\\u00f3 por qu\\u00e9 vale la pena un fondo para emergencias.' :
         'De cada toma y de cada corte se aprende: su meta est\\u00e1 m\\u00e1s cerca que nunca.');
    document.getElementById('directorMsg').textContent = dirMsg;

    document.getElementById('continueBtn').textContent = isOk ? 'Siguiente decisi\\u00f3n' : 'Continuar';
  </script>
'''.replace('__OPTIONS__', options_js).replace('__FEEDBACKS__', feedbacks_js).replace('__TITLES__', titles_js).replace('__SUBTITLES__', subtitles_js).replace('__CORRECT__', d['correct']).replace('__DID__', str(d['id']))

    write(f'4-consecuencia-{d["id"]}.html', f'Consecuencia {d["id"]}', body, extra_js=js)


PRODUCCION_BODY = '''
      <div class="card">
          <span class="eyebrow"><span class="dot-red"></span> Producción</span>
          <h1 class="t-hero" style="margin-top:14px;">Tu historia está <span class="underline-anim">lista</span></h1>
          <p class="t-body" style="max-width:50ch; opacity:.85; margin-top:2vh;">Tus escenas y decisiones ya están registradas. Solo falta dar la orden final.</p>

          <div style="margin-top:3vh; display:grid; grid-template-columns:repeat(3,1fr); gap:12px;">
              <div style="padding:18px; background:var(--color-yellow-soft); border-radius:14px; text-align:center;">
                  <div style="font-size:34px;">🎬</div>
                  <div style="font-family:var(--font-display); font-weight:800; font-size:0.85rem; letter-spacing:1.5px; color:var(--color-navy); text-transform:uppercase; margin-top:8px;">3 escenas</div>
              </div>
              <div style="padding:18px; background:var(--color-yellow-soft); border-radius:14px; text-align:center;">
                  <div style="font-size:34px;">🪑</div>
                  <div style="font-family:var(--font-display); font-weight:800; font-size:0.85rem; letter-spacing:1.5px; color:var(--color-navy); text-transform:uppercase; margin-top:8px;">3 decisiones</div>
              </div>
              <div style="padding:18px; background:var(--color-green-soft); border-radius:14px; text-align:center;">
                  <div style="font-size:34px;">✓</div>
                  <div style="font-family:var(--font-display); font-weight:800; font-size:0.85rem; letter-spacing:1.5px; color:#1c5a30; text-transform:uppercase; margin-top:8px;">Tu historia</div>
              </div>
          </div>

          <div style="margin-top:3vh; padding:18px; background:var(--color-white); border:1px solid var(--color-sky); border-radius:14px;">
              <p style="font-family:var(--font-display); font-weight:800; font-size:0.8rem; letter-spacing:1.5px; color:var(--color-yellow-deep); text-transform:uppercase;">Resumen de producción</p>
              <p style="margin-top:6px; color:var(--color-ink); font-size:1rem;">Escribiendo el guion · Editando las escenas · Iluminando el set · Poniendo los créditos</p>
          </div>

          <div id="directorLine" style="margin-top:18px; display:flex; align-items:center; gap:12px; padding:14px 18px; background:var(--color-yellow-soft); border-radius:12px;">
              <div class="director-avatar" style="width:48px; height:48px; border-radius:12px;">
                  <img src="assets/director-ia.png" alt="">
              </div>
              <p class="director-msg" style="font-size:0.95rem;">, el Director IA está escribiendo tu historia.</p>
          </div>

          <a class="cta cta-primary cta-block" id="produceBtn" href="6-premiere.html" style="margin-top:24px; opacity:.4; pointer-events:none;">
              Producir mi película
              <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 5l7 7-7 7"/></svg>
          </a>
        </div>
'''
PRODUCCION_JS = '''
  <script>
    var line = document.querySelector('#directorLine .director-msg');
    var full = line.textContent;
    line.textContent = '';
    var btn = document.getElementById('produceBtn');
    var i = 0;
    var tick = setInterval(function() {
      line.textContent = full.slice(0, ++i);
      if (i >= full.length) {
        clearInterval(tick);
        setTimeout(function() { btn.style.opacity = '1'; btn.style.pointerEvents = 'auto'; }, 400);
      }
    }, 38);
    document.getElementById('fsBtn').addEventListener('click', function() {
      !document.fullscreenElement ? document.documentElement.requestFullscreen && document.documentElement.requestFullscreen() : document.exitFullscreen && document.exitFullscreen();
    });
  </script>
'''

CONFETTI = ''.join([
    f'<div style="position:absolute; left:{x}%; top:{y}%; font-size:1.5rem; opacity:.6; animation:shimmer 3s ease-in-out infinite {delay}s;">✨</div>'
    for x, y, delay in [
        (8, 12, 0), (15, 30, .4), (22, 18, .8), (32, 8, 1.2),
        (45, 22, .3), (58, 14, .7), (68, 26, 1), (75, 18, 1.4),
        (85, 30, .6), (92, 12, 1), (5, 50, .5), (12, 65, .9),
        (50, 60, 1.3), (62, 70, .2), (78, 56, 1.1), (88, 65, .8),
    ]
])

PREMIERE_BODY = '''
      <div style="background:linear-gradient(135deg, var(--color-navy), var(--color-blue)); color:#fff; padding:5vh 4vw; border-radius:24px; text-align:center; box-shadow:var(--shadow-card); position:relative; overflow:hidden;">
          <div style="position:absolute; inset:0; background:radial-gradient(circle at 20% 30%, rgba(255,205,0,.15), transparent 50%), radial-gradient(circle at 80% 70%, rgba(7,68,186,.4), transparent 50%); pointer-events:none;"></div>
          <div style="position:relative; z-index:1;">
              <div style="font-size:54px; margin-bottom:14px;">🎬</div>
              <span class="eyebrow" style="background:rgba(255,205,0,.85); color:var(--color-navy); margin-bottom:14px;">
                  <span style="width:8px; height:8px; background:var(--color-red); border-radius:50%; display:inline-block;"></span>
                  Tu película · Estación 4
              </span>
              <h1 style="font-family:var(--font-display); font-weight:800; font-size:clamp(2.2rem, 5vh, 3.4rem); letter-spacing:-.02em; margin-top:14px;">
                  <span style="position:relative; display:inline-block;">
                      ¡Gracias por ser
                      <span style="position:absolute; left:0; right:0; bottom:-.12em; height:.16em; background:var(--color-yellow); border-radius:999px; transform-origin:left;"></span>
                  </span>
                  <br>protagonista,
              </h1>
              <p style="font-family:var(--font-display); font-weight:600; font-size:clamp(1.4rem, 3vh, 2rem); margin-top:14px; color:rgba(255,255,255,.9);">
                  <span id="userName">Arturo</span>!
              </p>
              <div style="margin-top:3vh; padding:18px; background:rgba(255,255,255,.1); border-radius:14px; border:1px solid rgba(255,255,255,.2); text-align:left;">
                  <p style="font-family:var(--font-display); font-weight:800; font-size:0.85rem; letter-spacing:1.5px; color:var(--color-yellow); text-transform:uppercase;">Tu cierre</p>
                  <p style="font-family:var(--font-sans); font-size:1.05rem; line-height:1.5; margin-top:8px; color:rgba(255,255,255,.95);">Tus tres escenas y decisiones ya están integradas. Pasa a recibir tu foto impresa.</p>
              </div>
              <div style="margin-top:24px; display:flex; gap:12px; justify-content:center; flex-wrap:wrap;">
                  <a class="cta cta-primary" href="index.html">
                      Empezar de nuevo
                      <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12a9 9 0 1 0 3-6.7L3 8"/><path d="M3 3v5h5"/></svg>
                  </a>
              </div>
              <p style="margin-top:14px; font-family:var(--font-display); font-weight:700; font-size:0.75rem; letter-spacing:1px; color:rgba(255,255,255,.5);">Si no, volveremos al inicio.</p>
          </div>
        </div>
        <div style="position:absolute; inset:0; pointer-events:none; overflow:hidden;">__CONFETTI__</div>
'''.replace('__CONFETTI__', CONFETTI)


if __name__ == '__main__':
    for d in DECISIONS:
        page_pregunta(d)
        page_consecuencia(d)

    write('5-produccion.html', 'Producción', PRODUCCION_BODY, extra_js=PRODUCCION_JS)
    write('6-premiere.html', 'Premiere · Tu película', PREMIERE_BODY)

    print(f"\n✅ {len(DECISIONS) * 2 + 2} pantallas generadas")