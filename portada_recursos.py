# -*- coding: utf-8 -*-
"""
Genera los recursos gráficos independientes de la portada:

  images/portada/
    fondo-desktop.webp                  1920×1080  degradado + patrón botánico translúcido
    fondo-mobile.webp                   1080×1920  versión vertical (centro despejado)
    ornamento-superior-izquierdo.svg    ramas doradas (foil champagne) de cada esquina
    ornamento-superior-derecho.svg
    ornamento-inferior-izquierdo.svg
    ornamento-inferior-derecho.svg
    laurel-izquierdo.svg / laurel-derecho.svg   ramitas del monograma
    remate-inferior.svg                 adorno central inferior
    corazon.svg                         corazón lineal del separador
    destello.svg                        destello de cuatro puntas

Uso:  python portada_recursos.py
Los fondos WEBP se rasterizan con Microsoft Edge (sin ventana) a partir de un SVG.
"""
import math, os, subprocess, tempfile
from PIL import Image

AQUI = os.path.dirname(os.path.abspath(__file__))
DEST = os.path.join(AQUI, "images", "portada")
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

HOJA = "M0 0C6-6.5 20-7.5 34 0C20 7.5 6 6.5 0 0Z"   # hoja apuntando a +x, 34 de largo


# --------------------------------------------------------------------------
# Geometría: hojas repartidas a lo largo de una curva de Bézier
# --------------------------------------------------------------------------
def bez(p, t):
    (x0, y0), (x1, y1), (x2, y2), (x3, y3) = p
    u = 1 - t
    x = u**3*x0 + 3*u*u*t*x1 + 3*u*t*t*x2 + t**3*x3
    y = u**3*y0 + 3*u*u*t*y1 + 3*u*t*t*y2 + t**3*y3
    dx = 3*u*u*(x1-x0) + 6*u*t*(x2-x1) + 3*t*t*(x3-x2)
    dy = 3*u*u*(y1-y0) + 6*u*t*(y2-y1) + 3*t*t*(y3-y2)
    return x, y, math.degrees(math.atan2(dy, dx))


def hojas(p, n, s0, s1, ang=50, t0=.1, t1=.93, punta=True):
    """Hojas alternadas a ambos lados de la curva p, que se achican hacia la punta."""
    out = []
    for k in range(n):
        t = t0 + (t1 - t0) * k / max(n - 1, 1)
        x, y, a = bez(p, t)
        lado = 1 if k % 2 else -1
        out.append((x, y, a + lado * ang, s0 + (s1 - s0) * t))
    if punta:
        x, y, a = bez(p, 1)
        out.append((x, y, a, s1 * .95))
    return out


def tallo(p):
    (x0, y0), (x1, y1), (x2, y2), (x3, y3) = p
    return f"M{x0:.1f} {y0:.1f}C{x1:.1f} {y1:.1f} {x2:.1f} {y2:.1f} {x3:.1f} {y3:.1f}"


def rama(curvas, color_hoja, color_tallo, ancho_tallo, vena=True, bayas=()):
    """curvas: lista de (puntos, n_hojas, escala_inicial, escala_final)."""
    t = "".join(f'<path d="{tallo(p)}"/>' for p, *_ in curvas)
    hs = []
    for p, n, s0, s1 in curvas:
        for x, y, r, s in hojas(p, n, s0, s1):
            hs.append(f'<g transform="translate({x:.1f} {y:.1f}) rotate({r:.1f}) scale({s:.2f})">'
                      f'<path d="{HOJA}"/>' + ('<path class="v" d="M3 0H30"/>' if vena else '') + '</g>')
    b = "".join(f'<circle cx="{x}" cy="{y}" r="{r}"/>' for x, y, r in bayas)
    return (f'<g fill="none" stroke="{color_tallo}" stroke-width="{ancho_tallo}" stroke-linecap="round">{t}</g>'
            f'<g fill="{color_hoja}">{"".join(hs)}</g>'
            + (f'<g fill="{color_hoja}">{b}</g>' if b else ''))


FOIL = ('<linearGradient id="oro" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="#F8EBC8"/><stop offset=".3" stop-color="#E2C68A"/>'
        '<stop offset=".55" stop-color="#D6B779"/><stop offset=".78" stop-color="#B08A47"/>'
        '<stop offset="1" stop-color="#EAD5A2"/></linearGradient>'
        '<linearGradient id="oro-tallo" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="#E9D3A0"/><stop offset="1" stop-color="#B8924E"/></linearGradient>'
        '<filter id="relieve" x="-10%" y="-10%" width="120%" height="120%">'
        '<feDropShadow dx="0" dy="1.2" stdDeviation="1.1" flood-color="#5A2840" flood-opacity=".35"/></filter>')
ESTILO_VENA = '<style>.v{fill:none;stroke:#7A5A2E;stroke-opacity:.35;stroke-width:.8}</style>'


def svg(viewbox, cuerpo, defs=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{viewbox}">'
            f'<defs>{FOIL}{defs}</defs>{ESTILO_VENA}{cuerpo}</svg>')


# --------------------------------------------------------------------------
# Ornamento de esquina (dibujado para la esquina superior izquierda, 400×400)
# Tres ramas: a lo largo del borde superior, en diagonal y a lo largo del borde izquierdo.
# --------------------------------------------------------------------------
_M = 24  # margen interior para que ninguna hoja quede cortada en el borde del archivo
RAMAS_ESQUINA_BASE = [
    (((20, 20), (95, 14), (190, 30), (318, 66)), 15, 1.15, .6),   # borde superior
    (((20, 20), (78, 70), (134, 124), (206, 206)), 11, 1.1, .6),   # diagonal
    (((20, 20), (14, 95), (30, 190), (66, 318)), 15, 1.15, .6),    # borde izquierdo
    (((150, 32), (170, 58), (200, 72), (238, 76)), 6, .8, .5),     # ramitas
    (((32, 150), (58, 170), (72, 200), (76, 238)), 6, .8, .5),
]
BAYAS = [(x + _M, y + _M, r) for x, y, r in
         [(118, 46, 3.6), (128, 54, 2.8), (46, 118, 3.6), (54, 128, 2.8), (150, 150, 3.2), (226, 104, 2.6), (104, 226, 2.6)]]
RAMAS_ESQUINA = [(tuple((x + _M, y + _M) for x, y in p), n, s0, s1) for p, n, s0, s1 in RAMAS_ESQUINA_BASE]


def ornamento_esquina(transform):
    # la sombra va en un grupo sin transformar para que caiga siempre hacia abajo
    cuerpo = (f'<g filter="url(#relieve)"><g transform="{transform}">'
              + rama(RAMAS_ESQUINA, "url(#oro)", "url(#oro-tallo)", 1.8, bayas=BAYAS) + '</g></g>')
    return svg("0 0 400 400", cuerpo)


# Ramita de laurel para el monograma (120×60), dibujada hacia arriba-derecha
def laurel(espejo):
    p = ((6, 52), (36, 47), (72, 32), (112, 8))
    tr = 'transform="translate(120 0) scale(-1 1)"' if espejo else ''
    return svg("0 0 120 60", f'<g filter="url(#relieve)"><g {tr}>' + rama([(p, 9, .55, .42)], "url(#oro)", "url(#oro-tallo)", 1.3) + '</g></g>')


def remate():
    hs = "".join(f'<g transform="translate({x} {y}) rotate({r}) scale({s})"><path d="{HOJA}"/><path class="v" d="M3 0H30"/></g>'
                 for x, y, r, s in [(120, 26, -90, .62), (118, 27, -145, .5), (122, 27, -35, .5),
                                    (104, 26, 180, .42), (136, 26, 0, .42)])
    cuerpo = ('<g filter="url(#relieve)">'
              '<path d="M8 26H90M150 26H232" stroke="#D6B779" stroke-width="1.1" fill="none"/>'
              f'<g fill="url(#oro)">{hs}<circle cx="120" cy="29" r="2.4"/><circle cx="94" cy="26" r="1.6"/>'
              '<circle cx="146" cy="26" r="1.6"/></g></g>')
    return svg("0 0 240 44", cuerpo)


def corazon():
    return svg("0 0 48 48", '<path filter="url(#relieve)" fill="none" stroke="url(#oro)" stroke-width="2" '
                            'd="M24 41S6 30.4 6 17.6C6 11.7 10.4 8 15.3 8c3.8 0 6.9 2.2 8.7 5.4C25.8 10.2 28.9 8 32.7 8 37.6 8 42 11.7 42 17.6 42 30.4 24 41 24 41z"/>')


def destello():
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="-20 -20 40 40"><defs>'
            '<radialGradient id="h"><stop offset="0" stop-color="#FFF8EC" stop-opacity=".9"/>'
            '<stop offset="1" stop-color="#FFF8EC" stop-opacity="0"/></radialGradient></defs>'
            '<circle r="14" fill="url(#h)" opacity=".6"/>'
            '<path fill="#FFFBF3" d="M0-14C1.3-3 3-1.3 14 0C3 1.3 1.3 3 0 14C-1.3 3-3 1.3-14 0C-3-1.3-1.3-3 0-14Z"/></svg>')


# --------------------------------------------------------------------------
# Fondos: degradado + ramas translúcidas (≈8 %) + destellos discretos.
# El centro queda despejado para el contenido.
# --------------------------------------------------------------------------
def fondo(w, h):
    fondo_base = (
        '<radialGradient id="g1" cx="50%" cy="42%" r="75%">'
        '<stop offset="0" stop-color="#D49BB2"/><stop offset=".35" stop-color="#C7839F"/>'
        '<stop offset=".7" stop-color="#B46F8C"/><stop offset="1" stop-color="#A85F7D"/></radialGradient>'
        '<linearGradient id="malva" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset=".35" stop-color="#76486F" stop-opacity="0"/><stop offset="1" stop-color="#76486F" stop-opacity=".42"/></linearGradient>'
        '<radialGradient id="vineta" cx="50%" cy="45%" r="70%">'
        '<stop offset=".55" stop-color="#5A2840" stop-opacity="0"/><stop offset="1" stop-color="#5A2840" stop-opacity=".22"/></radialGradient>'
        '<radialGradient id="bokeh"><stop offset="0" stop-color="#FFF5EF" stop-opacity=".55"/>'
        '<stop offset="1" stop-color="#FFF5EF" stop-opacity="0"/></radialGradient>')
    capas = [f'<rect width="{w}" height="{h}" fill="url(#g1)"/>',
             f'<rect width="{w}" height="{h}" fill="url(#malva)"/>']

    def rama_translucida(tx, ty, rot, esc, espejo=False):
        curvas = [(((0, 0), (120, -40), (260, -10), (420, -120)), 14, 1.6, .9),
                  (((150, -30), (190, -110), (250, -150), (330, -170)), 7, 1.2, .8),
                  (((260, -20), (300, 30), (360, 50), (430, 40)), 6, 1.1, .7)]
        sx = -esc if espejo else esc
        return (f'<g transform="translate({tx} {ty}) rotate({rot}) scale({sx} {esc})" opacity=".085">'
                + rama(curvas, "#FFF5EF", "#FFF5EF", 2.2, vena=False) + '</g>')

    if w > h:   # horizontal: ramas en los laterales, centro libre
        capas += [rama_translucida(-40, h * .78, -62, 1.25), rama_translucida(w + 40, h * .78, 62, 1.25, True),
                  rama_translucida(-60, h * .30, -20, .9), rama_translucida(w + 60, h * .30, 20, .9, True)]
        bokeh = [(.17, .26, 120), (.83, .30, 140), (.12, .72, 90), (.88, .70, 110), (.32, .14, 60), (.69, .86, 70)]
        brillos = [(.21, .33, 5), (.27, .52, 4), (.73, .28, 5), (.78, .55, 4), (.40, .12, 3), (.61, .90, 3), (.09, .47, 3), (.92, .44, 3)]
    else:       # vertical: ramas arriba y abajo por los lados
        capas += [rama_translucida(-60, h * .30, -70, 1.15), rama_translucida(w + 60, h * .30, 70, 1.15, True),
                  rama_translucida(-60, h * .92, -40, 1.05), rama_translucida(w + 60, h * .92, 40, 1.05, True)]
        bokeh = [(.20, .14, 110), (.80, .18, 120), (.18, .84, 100), (.82, .80, 110), (.50, .06, 70), (.50, .95, 70)]
        brillos = [(.22, .22, 5), (.78, .26, 5), (.15, .55, 4), (.85, .52, 4), (.30, .80, 4), (.70, .84, 4), (.50, .10, 3)]
    capas += [f'<path transform="translate({x*w:.0f} {y*h:.0f}) scale({s/10})" fill="#FFF8EC" opacity=".55" '
              'd="M0-10C1-2 2-1 10 0C2 1 1 2 0 10C-1 2-2 1-10 0C-2-1-1-2 0-10Z"/>' for x, y, s in brillos]
    capas.append(f'<rect width="{w}" height="{h}" fill="url(#vineta)"/>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">'
            f'<defs>{fondo_base}</defs>{"".join(capas)}</svg>')


def rasterizar(svg_txt, w, h, destino):
    with tempfile.TemporaryDirectory() as tmp:
        html = os.path.join(tmp, "f.html"); png = os.path.join(tmp, "f.png")
        open(html, "w", encoding="utf-8").write(
            f'<!DOCTYPE html><html><body style="margin:0;overflow:hidden">{svg_txt}</body></html>')
        subprocess.run([EDGE, "--headless=new", "--disable-gpu", "--hide-scrollbars", f"--window-size={w},{h}",
                        f"--user-data-dir={os.path.join(tmp, 'perfil')}", f"--screenshot={png}",
                        "file:///" + html.replace("\\", "/")], check=True, capture_output=True, timeout=120)
        Image.open(png).convert("RGB").crop((0, 0, w, h)).save(destino, "WEBP", quality=82, method=6)


def main():
    os.makedirs(DEST, exist_ok=True)
    archivos = {
        "ornamento-superior-izquierdo.svg": ornamento_esquina(""),
        "ornamento-superior-derecho.svg": ornamento_esquina("translate(400 0) scale(-1 1)"),
        "ornamento-inferior-izquierdo.svg": ornamento_esquina("translate(0 400) scale(1 -1)"),
        "ornamento-inferior-derecho.svg": ornamento_esquina("translate(400 400) scale(-1 -1)"),
        "laurel-izquierdo.svg": laurel(False),
        "laurel-derecho.svg": laurel(True),
        "remate-inferior.svg": remate(),
        "corazon.svg": corazon(),
        "destello.svg": destello(),
    }
    for nombre, txt in archivos.items():
        open(os.path.join(DEST, nombre), "w", encoding="utf-8").write(txt)
    rasterizar(fondo(1920, 1080), 1920, 1080, os.path.join(DEST, "fondo-desktop.webp"))
    rasterizar(fondo(1080, 1920), 1080, 1920, os.path.join(DEST, "fondo-mobile.webp"))
    for f in sorted(os.listdir(DEST)):
        print(f"{f:40s} {os.path.getsize(os.path.join(DEST, f)) / 1024:7.1f} KB")


if __name__ == "__main__":
    main()
