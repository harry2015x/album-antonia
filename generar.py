# -*- coding: utf-8 -*-
"""
Genera el álbum de presentación 1920×1080 de Antonia.

Uso:  python generar.py
Crea:
  - fotos/                  copias optimizadas de las fotos elegidas
  - index.html             presentación (necesita la carpeta fotos/ al lado)
  - Antonia - Album (un solo archivo).html   con las fotos dentro, para llevar en una USB

Para cambiar una foto, un texto o el orden: edita la lista PAGINAS y vuelve a ejecutar.
Cada foto se indica por su ID del catálogo (catalogo.json). Para mover el encuadre
se puede escribir "ID@x,y" (porcentajes), por ejemplo "U027@50,20".
"""
import json, os, html
from PIL import Image, ImageOps, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
NOMBRE = "Antonia"
CAT = json.load(open(os.path.join(AQUI, "catalogo.json"), encoding="utf-8"))

# ---------------------------------------------------------------------------
# CONTENIDO: 65 páginas
# ---------------------------------------------------------------------------
CAP = {0: "Antonia", 1: "Capítulo I", 2: "Capítulo II", 3: "Capítulo III", 4: "Capítulo IV", 5: "Capítulo V"}

PAGINAS = [
    # --- Apertura -----------------------------------------------------------
    dict(t="cover", cap=0, fotos=["N086@50,40"]),
    dict(t="feature", cap=0, fotos=["N001@50,45"], icon="heart", eyebrow="Antes de ti",
         titulo="Donde todo <em>comenzó</em>", texto="Dos corazones que soñaron contigo mucho antes de conocerte.", firma="— mamá y papá"),
    dict(t="wide", cap=0, fotos=["N005@50,35"], icon="heart", eyebrow="Nuestra historia",
         titulo="Y un día <em>dijimos sí</em>", texto="Así empezó la familia que te estaba esperando."),

    # --- Capítulo I · Nacimiento (15) --------------------------------------
    dict(t="chapter", cap=1, fotos=["N012"], roman="I", eyebrow="Capítulo uno", titulo="<em>Nacimiento</em>",
         texto="El día en que el mundo se hizo más pequeño, más suave e infinitamente más bonito."),
    dict(t="feature", cap=1, lado="r", fotos=["N085@40,50"], icon="star", eyebrow="El primer encuentro",
         titulo="Bienvenida, <em>Antonia</em>", texto="Un instante bastó para saber que nada volvería a ser igual."),
    dict(t="trio", cap=1, icon="moon", titulo="Los primeros <em>días</em>",
         fotos=["N013", "N020", "N018"], caps=["Primer sueño", "Primera sonrisa", "Pura alegría"]),
    dict(t="duo", cap=1, fotos=["N014@50,40", "N043@50,40"], icon="heart", eyebrow="Papá",
         titulo="Los brazos de <em>papá</em>", texto="El lugar más seguro del mundo."),
    dict(t="mosaic", cap=1, fotos=["N028@50,40", "N029", "N031", "N030", "N026"], icon="heart",
         titulo="Brazos que <em>abrazan</em>", texto="Mamá, abuelas y todo el amor que te recibió."),
    dict(t="feature", cap=1, fotos=["N034"], icon="moon", eyebrow="Su primer nido",
         titulo="Un rincón <em>hecho de amor</em>", texto="Cada detalle preparado con ilusión, esperando tu llegada."),
    dict(t="quad", cap=1, icon="moon", titulo="Dulces <em>sueños</em>", fotos=["N010", "N011", "N015", "N017"]),
    dict(t="wide", cap=1, fotos=["N073"], icon="heart", eyebrow="Mamá y yo",
         titulo="Mejilla con <em>mejilla</em>", texto="Hay abrazos que se quedan para siempre."),
    dict(t="grid6", cap=1, fotos=["N021", "N025", "N036", "N037@50,30", "N047", "N057"], icon="flower",
         titulo="Cada día más <em>bonita</em>", texto="Pequeños cambios que llenaban la casa de alegría."),
    dict(t="trio", cap=1, icon="star", titulo="Pequeña <em>estrella</em>",
         fotos=["N039", "N040", "N042"], caps=["Lista para posar", "Con estilo", "Día de piscina"]),
    dict(t="duo", cap=1, fotos=["N078@50,40", "N080@50,40"], icon="heart", eyebrow="Complicidad",
         titulo="Sonrisas <em>compartidas</em>", texto="Las mejores fotos siempre son en compañía."),
    dict(t="mosaic", cap=1, fotos=["N050@50,35", "N067", "N070", "N071", "N081"], icon="camera",
         titulo="Mis compañeros de <em>aventura</em>", texto="Papá, mamá y una lista larga de paseos por delante."),
    dict(t="quad", cap=1, icon="flower", titulo="Creciendo <em>con amor</em>", fotos=["N051", "N055", "N069", "N084"]),
    dict(t="feature", cap=1, lado="r", fotos=["N076"], icon="star", eyebrow="Control de peso",
         titulo="Cada gramo, <em>un logro</em>", texto="Crecer sana, fuerte y feliz: nuestra mayor alegría."),
    dict(t="wide", cap=1, fotos=["N065@50,40"], icon="heart", eyebrow="En familia",
         titulo="Toda la <em>familia</em>", texto="Tantas personas felices de conocerte."),

    # --- Capítulo II · Bautizo (6) -----------------------------------------
    dict(t="chapter", cap=2, fotos=["B012@50,30"], roman="II", eyebrow="Capítulo dos", titulo="<em>Bautizo</em>",
         texto="Vestida de blanco, rodeada de luz y de quienes más te quieren."),
    dict(t="split2", cap=2, fotos=["B009@50,35", "B011@50,25", "B003@50,30"], icon="dove", eyebrow="Un día bendecido",
         titulo="Llena de <em>luz</em>", texto="Un día para dar gracias por el regalo de tenerte."),
    dict(t="wide", cap=2, fotos=["B013@50,30"], icon="dove", eyebrow="La ceremonia",
         titulo="La <em>bendición</em>", texto="Agua, fe y promesas hechas con el corazón."),
    dict(t="trio", cap=2, icon="heart", titulo="Rodeada de <em>amor</em>",
         fotos=["B015@50,30", "B008@50,30", "B002@50,30"], caps=["Con papá y mamá", "Abrazos", "En brazos de papá"]),
    dict(t="wide", cap=2, fotos=["B020@50,40"], icon="dove", eyebrow="Padrinos y familia",
         titulo="Testigos de <em>tu fe</em>", texto="Quienes prometieron acompañarte siempre."),
    dict(t="duo", cap=2, fotos=["B004@50,30", "B010@50,30"], icon="flower", eyebrow="Después de la fiesta",
         titulo="Pequeña <em>artista</em>", texto="Y al terminar el día, a jugar y a colorear."),

    # --- Capítulo III · Primer año (16) ------------------------------------
    dict(t="chapter", cap=3, fotos=["U007@50,30"], roman="III", eyebrow="Capítulo tres", titulo="Primer <em>año</em>",
         texto="Doce meses de descubrimientos, risas y primeras veces."),
    dict(t="year", cap=3, numero="12", eyebrow="meses · Capítulo III", titulo="Mi primer <em>año</em>",
         fotos=["U027@50,30", "U023@50,30", "U025@50,30", "U017@50,30"]),
    dict(t="trio", cap=3, icon="moon", titulo="Mi rincón <em>favorito</em>",
         fotos=["U006", "U014@50,30", "U016@50,30"], caps=["Lista para jugar", "Toda de rosa", "Hora de descubrir"]),
    dict(t="mosaic", cap=3, fotos=["U001@50,40", "U123@50,30", "U041@50,30", "U060", "U022@50,25"], icon="star",
         titulo="Mi primera <em>Navidad</em>", texto="Luces, regalos y la magia de estar juntos."),
    dict(t="wide", cap=3, fotos=["U024@50,40"], icon="steps", eyebrow="Primeras aventuras",
         titulo="El mundo es <em>enorme</em>", texto="Y lo quiero conocer todo, de la mano de papá."),
    dict(t="duo", cap=3, fotos=["U005@50,40", "U010@50,40"], icon="flower", eyebrow="Al aire libre",
         titulo="Paseos de <em>domingo</em>", texto="Sol, pasto y la mejor compañía."),
    dict(t="grid6", cap=3, fotos=["U031@50,30", "U035@50,30", "U040@50,30", "U042@50,30", "U047@50,30", "U053@50,30"],
         icon="star", titulo="Comidas y <em>juegos</em>", texto="Cada cucharada, una aventura; cada juguete, un tesoro."),
    dict(t="feature", cap=3, fotos=["U054@50,35"], icon="heart", eyebrow="Mamá y yo",
         titulo="Igualitas a <em>mamá</em>", texto="Mismas gafas, misma sonrisa."),
    dict(t="quad", cap=3, icon="heart", titulo="Mis personas <em>favoritas</em>",
         fotos=["U036@50,30", "U009@50,40", "U034@50,40", "U065@50,40"]),
    dict(t="wide", cap=3, fotos=["U076@50,35"], icon="star", eyebrow="Logros en familia",
         titulo="Celebrando <em>juntos</em>", texto="Los triunfos de casa también son tuyos."),
    dict(t="mosaic", cap=3, fotos=["U070@50,40", "U072@50,30", "U074@50,40", "U075@50,40", "U093@50,40"], icon="heart",
         titulo="Abuelos y <em>familia</em>", texto="Raíces que te sostienen y te llenan de mimos."),
    dict(t="trio", cap=3, icon="camera", titulo="Con <em>estilo</em>",
         fotos=["U055@50,30", "U052@50,40", "U063@50,40"], caps=["Gafas de estrella", "Caperucita", "Sesión de fotos"]),
    dict(t="grid6", cap=3, fotos=["U045@50,60", "U038@50,30", "U096@50,40", "U100@50,40", "U048@50,40", "U095@50,30"],
         icon="steps", titulo="Mis primeros <em>pasos</em>", texto="Primero gateando, luego de pie, y después… ¡a correr!"),
    dict(t="feature", cap=3, lado="r", fotos=["U107@50,35"], icon="cake", eyebrow="Mi primer cumpleaños",
         titulo="¡Un <em>añito</em>!", texto="Velas, globos y una fiesta llena de amor."),
    dict(t="mosaic", cap=3, fotos=["U112@50,40", "U110@50,40", "U099@50,40", "U104@50,40", "U111@50,40"], icon="cake",
         titulo="La gran <em>fiesta</em>", texto="Todos reunidos para celebrar tu primer año."),
    dict(t="wide", cap=3, fotos=["U113@50,40"], icon="cake", eyebrow="Uno y contando",
         titulo="Gracias por <em>venir</em>", texto="Cada abrazo hizo ese día inolvidable."),

    # --- Capítulo IV · Segundo año (14) ------------------------------------
    dict(t="chapter", cap=4, fotos=["D018@50,30"], roman="IV", eyebrow="Capítulo cuatro", titulo="Segundo <em>año</em>",
         texto="Rizos, carcajadas y una personalidad que no cabe en la casa."),
    dict(t="year", cap=4, numero="24", eyebrow="meses · Capítulo IV", titulo="Mi segundo <em>año</em>",
         fotos=["D030@50,30", "D009@50,30", "D013@50,30", "D022@50,30"]),
    dict(t="trio", cap=4, icon="camera", titulo="Con estilo <em>propio</em>",
         fotos=["D028@50,40", "D034@50,40", "D036@50,40"], caps=["Toda de rosa", "Con mi amiga Minnie", "Lista para salir"]),
    dict(t="full", cap=4, fotos=["D088@50,50"], eyebrow="Primera vez en el mar",
         titulo="Sol, arena <em>y mar</em>"),
    dict(t="grid6", cap=4, fotos=["D084@50,40", "D086@50,40", "D091@50,40", "D093@50,40", "D094@50,30", "D095@50,40"],
         icon="star", titulo="Días de <em>playa</em>", texto="Olas, castillos de arena y atardeceres naranjas."),
    dict(t="duo", cap=4, fotos=["D083@50,60", "D082@50,30"], icon="heart", eyebrow="Vacaciones",
         titulo="Atardeceres en <em>familia</em>", texto="Los tres, frente al mar."),
    dict(t="mosaic", cap=4, fotos=["D056@50,50", "D057@50,40", "D058@50,40", "D059@50,50", "D060@50,40"], icon="camera",
         titulo="Calles de <em>colores</em>", texto="Paraguas, luces y una exploradora feliz."),
    dict(t="wide", cap=4, fotos=["D049@50,40"], icon="steps", eyebrow="De paseo",
         titulo="Navegando <em>juntos</em>", texto="Viento en la cara y risas en el agua."),
    dict(t="trio", cap=4, icon="star", titulo="Noche de <em>disfraces</em>",
         fotos=["D040@50,30", "D041@50,30", "D042@50,40"], caps=["Lista", "Martillo en mano", "¡Dulce o truco!"]),
    dict(t="quad", cap=4, icon="steps", titulo="Pequeña <em>exploradora</em>",
         fotos=["D063@50,40", "D070@50,40", "D071@50,50", "D077@50,40"]),
    dict(t="duo", cap=4, fotos=["D103@50,35", "D105@50,40"], icon="flower", eyebrow="Entre flores",
         titulo="Campo de <em>girasoles</em>", texto="Tú, la flor más bonita del campo."),
    dict(t="feature", cap=4, fotos=["D072@50,35"], icon="heart", eyebrow="Disfraces con papá",
         titulo="Equipo <em>perfecto</em>", texto="Papá e hija, siempre en la misma aventura."),
    dict(t="mosaic", cap=4, fotos=["D117@50,40", "D108@50,40", "D111@50,40", "D114@50,40", "D116@50,40"], icon="cake",
         titulo="¡Dos <em>añitos</em>!", texto="Globos rosados, Minnie y muchísimo amor."),
    dict(t="wide", cap=4, fotos=["D113@50,40"], icon="cake", eyebrow="Fiesta de cumpleaños",
         titulo="Celebrando en <em>familia</em>", texto="Gracias a todos por estar."),

    # --- Capítulo V · Tercer año (10) --------------------------------------
    dict(t="chapter", cap=5, fotos=["T007@50,30"], roman="V", eyebrow="Capítulo cinco", titulo="Tercer <em>año</em>",
         texto="Ya no es una bebé: es una niña curiosa, divertida y llena de ideas."),
    dict(t="year", cap=5, numero="36", eyebrow="meses · Capítulo V", titulo="Mi tercer <em>año</em>",
         fotos=["T028@50,30", "T011@50,30", "T006@50,30", "T026@50,30"]),
    dict(t="trio", cap=5, icon="camera", titulo="Pequeña <em>modelo</em>",
         fotos=["T012@50,40", "T014@50,40", "T015@50,40"], caps=["Vestida de fiesta", "Pose de revista", "¡Sombrero nuevo!"]),
    dict(t="grid6", cap=5, fotos=["T008@50,30", "T009@50,40", "T010@50,40", "T016@50,40", "T023@50,40", "T025@50,40"],
         icon="flower", titulo="Jugar y <em>descubrir</em>", texto="Flores, columpios y mil cosas por aprender."),
    dict(t="duo", cap=5, fotos=["T018@50,30", "T017@50,30"], icon="heart", eyebrow="Papá y yo",
         titulo="Mi persona <em>favorita</em>", texto="Juegos, abrazos y velitas compartidas."),
    dict(t="trio", cap=5, icon="star", titulo="Fiestas y <em>celebraciones</em>",
         fotos=["T037@50,60", "T038@50,40", "T041@50,40"], caps=["Navidad", "En familia", "Amigos de colores"]),
    dict(t="wide", cap=5, fotos=["T044@50,40"], icon="heart", eyebrow="Todos juntos",
         titulo="Nuestra gran <em>familia</em>", texto="Gracias por cuidarla, quererla y acompañarla."),
    dict(t="feature", cap=5, lado="r", fotos=["T027@50,30"], icon="star", eyebrow="Tres años",
         titulo="Mi pequeña <em>princesa</em>", texto="Cada día más grande, cada día más tú."),
    dict(t="quad", cap=5, icon="heart", titulo="Tres años de <em>risas</em>",
         fotos=["T032@50,30", "T033@50,40", "T035@50,40", "T046@50,40"]),
    dict(t="feature", cap=5, fotos=["T047@50,35"], icon="flower", eyebrow="Y ahora…",
         titulo="¡A bailar <em>la vida</em>!", texto="Lo mejor de tu historia apenas está comenzando."),

    # --- Cierre -------------------------------------------------------------
    dict(t="end", cap=0),
]

# ---------------------------------------------------------------------------
# Fotos: copia optimizada
# ---------------------------------------------------------------------------
def parse(ref):
    if "@" in ref:
        i, pos = ref.split("@"); x, y = pos.split(",")
        return i, f"{x}% {y}%"
    return ref, "50% 40%"

RECORTE = {"N001": (0.025, 0.0, 0.025, 0.05)}

def preparar_fotos():
    os.makedirs(os.path.join(AQUI, "fotos"), exist_ok=True)
    ids = {parse(r)[0]: p.get("t") for p in PAGINAS for r in p.get("fotos", [])}
    for i, tipo in ids.items():
        dst = os.path.join(AQUI, "fotos", f"{i}.jpg")
        if os.path.exists(dst):
            continue
        im = ImageOps.exif_transpose(Image.open(os.path.join(RAIZ, CAT[i]))).convert("RGB")
        if i in RECORTE:  # quita bordes blancos que trae la foto original (izq, arriba, der, abajo en %)
            l, t, r, b = RECORTE[i]; w, h = im.size
            im = im.crop((int(w*l), int(h*t), int(w*(1-r)), int(h*(1-b))))
        im.thumbnail((2000, 2000) if tipo in ("full", "cover") else (1500, 1500), Image.LANCZOS)
        im.save(dst, quality=84, optimize=True, progressive=True)
    return ids

# ---------------------------------------------------------------------------
# HTML de cada tipo de página
# ---------------------------------------------------------------------------
def img(ref, cls="ph", extra=""):
    i, pos = parse(ref)
    return f'<div class="{cls}"{extra}><img src="fotos/{i}.jpg" style="object-position:{pos}" alt=""></div>'

def icon(name, cls="ic"):
    return f'<svg class="{cls}"><use href="#i-{name}"/></svg>'

def foot(p, n, left=None):
    style = f' style="left:{left}px"' if left else ""
    lbl = NOMBRE if p["cap"] == 0 else f"{NOMBRE} · {CAP[p['cap']]}"
    return f'<div class="foot"{style}><span>{lbl}</span><span class="num">{n:02d}</span></div>'

def page(p, n):
    t = p["t"]; f = p.get("fotos", [])
    g = lambda k, d="": p.get(k, d)
    if t == "cover":
        return f'''<section class="slide s-cover">
  <div class="left">
    {icon("star", "ic lg reveal")}
    <div class="eyebrow gold reveal d1" style="margin-top:34px">Álbum familiar</div>
    <h1 class="title name reveal d2"><em>{NOMBRE}</em></h1>
    <div class="rule reveal d3"></div>
    <div class="sub reveal d3">Mis primeros tres años</div>
    <div class="chapters reveal d4">
      <div>{icon("moon")}Nacimiento</div><div>{icon("dove")}Bautizo</div><div>{icon("cake")}1 año</div>
      <div>{icon("steps")}2 años</div><div>{icon("flower")}3 años</div>
    </div>
  </div>
  {img(f[0], "ph main")}
  <div class="vline"></div>
</section>'''
    if t == "chapter":
        return f'''<section class="slide dark s-chapter c{p['cap']}">
  <div class="txt">
    <div class="roman gold-text reveal">{g("roman")}</div>
    <div class="eyebrow gold reveal d1">{g("eyebrow")}</div>
    <h2 class="title reveal d2">{g("titulo")}</h2>
    <div class="rule reveal d3"></div>
    <p class="body reveal d3">{g("texto")}</p>
  </div>
  {img(f[0], "ph framed br reveal d2")}
  {foot(p, n)}
</section>'''
    if t == "feature":
        lado = g("lado", "l")
        firma = f'<div class="quote reveal d4">{g("firma")}</div>' if g("firma") else ""
        return f'''<section class="slide s-feature {lado}">
  {img(f[0], "ph framed " + ("tl" if lado == "l" else "br") + " reveal")}
  <div class="txt">
    {icon(g("icon", "heart"), "ic lg reveal d1")}
    <div class="eyebrow reveal d1">{g("eyebrow")}</div>
    <h2 class="title reveal d2">{g("titulo")}</h2>
    <div class="rule reveal d3"></div>
    <p class="body reveal d3">{g("texto")}</p>
    {firma}
  </div>
  {foot(p, n)}
</section>'''
    if t == "wide":
        return f'''<section class="slide s-wide">
  <div class="txt">
    {icon(g("icon", "heart"), "ic lg reveal")}
    <div class="eyebrow reveal d1">{g("eyebrow")}</div>
    <h2 class="title reveal d2">{g("titulo")}</h2>
    <div class="rule reveal d3"></div>
    <p class="body reveal d3">{g("texto")}</p>
  </div>
  {img(f[0], "ph framed br reveal d1")}
  {foot(p, n)}
</section>'''
    if t == "full":
        return f'''<section class="slide s-full">
  {img(f[0], "ph bg")}
  <div class="shade"></div>
  <div class="txt">
    <div class="eyebrow gold reveal d1">{g("eyebrow")}</div>
    <h2 class="title reveal d2">{g("titulo")}</h2>
    <div class="rule reveal d3"></div>
  </div>
  {foot(p, n)}
</section>'''
    if t == "split2":
        return f'''<section class="slide s-split2">
  {img(f[0], "ph main reveal")}
  <div class="txt">
    <div class="row-ic reveal d1">{icon(g("icon", "dove"), "ic lg")}<span class="eyebrow gold">{g("eyebrow")}</span></div>
    <h2 class="title reveal d2">{g("titulo")}</h2>
    <div class="rule reveal d3"></div>
    <p class="body reveal d3">{g("texto")}</p>
  </div>
  {img(f[1], "ph small a reveal d3")}
  {img(f[2], "ph small b reveal d4")}
  {foot(p, n, 960)}
</section>'''
    if t == "trio":
        cells = "".join(f'<div class="cell reveal d{k+2}">{img(r)}<div class="caption">{c}</div></div>'
                        for k, (r, c) in enumerate(zip(f, g("caps", ["", "", ""]))))
        return f'''<section class="slide s-trip">
  <div class="head">{icon(g("icon", "heart"), "ic reveal")}<h2 class="title reveal d1">{g("titulo")}</h2><div class="rule short reveal d2"></div></div>
  <div class="row">{cells}</div>
  {foot(p, n)}
</section>'''
    if t == "quad":
        cells = "".join(f'<div class="cell reveal d{min(k+1,4)}">{img(r)}</div>' for k, r in enumerate(f))
        return f'''<section class="slide s-quad">
  <div class="head">{icon(g("icon", "heart"), "ic reveal")}<h2 class="title reveal d1">{g("titulo")}</h2><div class="rule short reveal d2"></div></div>
  <div class="row">{cells}</div>
  {foot(p, n)}
</section>'''
    if t == "duo":
        return f'''<section class="slide s-duo">
  <div class="txt">
    {icon(g("icon", "heart"), "ic lg reveal")}
    <div class="eyebrow reveal d1">{g("eyebrow")}</div>
    <h2 class="title reveal d2">{g("titulo")}</h2>
    <div class="rule reveal d3"></div>
    <p class="body reveal d3">{g("texto")}</p>
  </div>
  {img(f[0], "ph a framed tl reveal d1")}
  {img(f[1], "ph b reveal d2")}
  {foot(p, n)}
</section>'''
    if t in ("mosaic", "grid6"):
        cls = "s-mosaic" if t == "mosaic" else "s-grid6"
        cells = "".join(img(r, "ph" + (" big" if (t == "mosaic" and k == 0) else "") + f" reveal d{min(k+1,4)}")
                        for k, r in enumerate(f))
        return f'''<section class="slide {cls}">
  <div class="side">
    {icon(g("icon", "heart"), "ic lg reveal")}
    <h2 class="title reveal d1">{g("titulo")}</h2>
    <div class="rule reveal d2"></div>
    <p class="body reveal d3">{g("texto")}</p>
  </div>
  <div class="grid">{cells}</div>
  {foot(p, n)}
</section>'''
    if t == "year":
        return f'''<section class="slide s-year">
  <div class="txt">
    <div class="big-num gold-text reveal">{g("numero")}</div>
    <div class="eyebrow reveal d1">{g("eyebrow")}</div>
    <h2 class="title reveal d2">{g("titulo")}</h2>
    <div class="rule short reveal d3"></div>
  </div>
  {img(f[1], "ph l reveal d2")}
  {img(f[0], "ph center framed reveal d1")}
  {img(f[2], "ph r1 reveal d3")}
  {img(f[3], "ph r2 reveal d4")}
  {foot(p, n)}
</section>'''
    if t == "end":
        ics = "".join(icon(x) for x in ("moon", "dove", "cake", "steps", "flower"))
        return f'''<section class="slide s-end">
  <div>
    <div class="mono reveal"><span class="gold-text">{NOMBRE[0]}</span></div>
    <div class="eyebrow gold reveal d1">Con todo nuestro amor</div>
    <h2 class="title reveal d2">La historia <em>continúa…</em></h2>
    <div class="rule reveal d3" style="margin:0 auto"></div>
    <div class="icons reveal d4">{ics}</div>
  </div>
  {foot(p, n)}
</section>'''
    raise ValueError(t)

# ---------------------------------------------------------------------------
CSS = r"""
:root{--paper:#F7F4EF;--ink:#2B2A28;--charcoal:#262523;--gray:#8C8881;--line:#DCD5C9;--gold:#B08D57;--gold-light:#D6BC8A;
--gold-grad:linear-gradient(135deg,#D9BF8C 0%,#B08D57 45%,#8E6D3E 70%,#CFB27C 100%);
--serif:"Cormorant Garamond","Times New Roman",serif;--sans:"Montserrat","Segoe UI",sans-serif}
*{box-sizing:border-box;margin:0;padding:0}
html,body{height:100%;background:#151514;overflow:hidden}
body{display:flex;align-items:center;justify-content:center;font-family:var(--sans);color:var(--ink)}
body.auto{cursor:none}
#stage{width:1920px;height:1080px;position:relative;flex:none;transform-origin:center center;box-shadow:0 30px 80px rgba(0,0,0,.45)}
.slide{position:absolute;inset:0;background:var(--paper);opacity:0;visibility:hidden;transition:opacity 1s ease,visibility 1s;overflow:hidden}
.slide.active{opacity:1;visibility:visible}
.slide.active .reveal{animation:rise 1.2s cubic-bezier(.2,.7,.2,1) both}
.slide.active .d1{animation-delay:.15s}.slide.active .d2{animation-delay:.3s}.slide.active .d3{animation-delay:.45s}.slide.active .d4{animation-delay:.6s}
@keyframes rise{from{opacity:0;transform:translateY(18px)}to{opacity:1;transform:none}}
.eyebrow{font-weight:400;font-size:15px;letter-spacing:.42em;text-transform:uppercase;color:var(--gray)}
.eyebrow.gold{color:var(--gold)}
.title{font-family:var(--serif);font-weight:300;line-height:1;color:var(--ink)}
.title em{font-style:italic;font-weight:300}
.body{font-family:var(--serif);font-size:30px;line-height:1.45;color:#5d5953}
.caption{font-size:12px;letter-spacing:.32em;text-transform:uppercase;color:var(--gray);margin-top:22px;display:flex;align-items:center;gap:14px}
.caption::before{content:"";width:26px;height:1px;background:var(--gold)}
.rule{width:120px;height:1px;background:var(--gold-grad)}
.rule.short{width:60px}
.gold-text{background:var(--gold-grad);-webkit-background-clip:text;background-clip:text;color:transparent}
.ph{position:absolute}
.ph img{width:100%;height:100%;object-fit:cover;display:block}
.ph.framed::after{content:"";position:absolute;inset:-16px;border:1px solid var(--gold-light);pointer-events:none}
.ph.framed.tl::after{inset:-16px 16px 16px -16px}
.ph.framed.br::after{inset:16px -16px -16px 16px}
.ic{width:34px;height:34px;stroke:var(--gold);fill:none;stroke-width:1.1;stroke-linecap:round;stroke-linejoin:round;display:block}
.ic.lg{width:54px;height:54px;stroke-width:.9}
.foot{position:absolute;left:110px;right:110px;bottom:46px;display:flex;justify-content:space-between;align-items:center;font-size:12px;letter-spacing:.38em;text-transform:uppercase;color:var(--gray)}
.foot .num{font-family:var(--serif);font-size:22px;letter-spacing:.08em;color:var(--gold);text-transform:none}
.dark{background:var(--charcoal)}.dark .title{color:#F3EEE6}.dark .body{color:#a9a399}.dark .foot{color:#8f8a82}
.txt .eyebrow{margin-top:30px}.txt .title{margin:30px 0 38px}.txt .body{margin-top:38px}

/* portada */
.s-cover .left{position:absolute;left:0;top:0;width:840px;height:100%;padding:150px 0 0 150px}
.s-cover .title{font-size:210px;margin:40px 0 34px -8px;line-height:.95}
.s-cover .sub{font-family:var(--serif);font-style:italic;font-size:40px;color:#6a655e;margin-top:34px}
.s-cover .chapters{position:absolute;left:150px;bottom:150px;display:flex;gap:46px}
.s-cover .chapters div{display:flex;flex-direction:column;align-items:center;gap:14px;font-size:11px;letter-spacing:.28em;text-transform:uppercase;color:var(--gray)}
.s-cover .ph.main{left:840px;top:0;width:1080px;height:1080px}
.s-cover .vline{position:absolute;left:840px;top:0;bottom:0;width:6px;background:var(--gold-grad)}

/* capítulo */
.s-chapter .txt{position:absolute;left:150px;top:0;bottom:0;width:820px;display:flex;flex-direction:column;justify-content:center}
.s-chapter .roman{font-family:var(--serif);font-weight:300;font-size:260px;line-height:.85;margin-bottom:30px}
.s-chapter .title{font-size:140px}
.s-chapter .body{max-width:620px}
.s-chapter .ph{right:170px;top:150px;width:580px;height:780px}
.s-chapter .ph.framed::after{border-color:rgba(214,188,138,.55)}

/* foto destacada */
.s-feature .ph{top:130px;width:760px;height:820px}
.s-feature.l .ph{left:150px}.s-feature.r .ph{left:1010px}
.s-feature .txt{position:absolute;top:0;bottom:0;width:680px;display:flex;flex-direction:column;justify-content:center}
.s-feature.l .txt{left:1060px}.s-feature.r .txt{left:150px}
.s-feature .title{font-size:108px}
.s-feature .quote{font-family:var(--serif);font-style:italic;font-size:34px;color:var(--gold);margin-top:46px}

/* foto horizontal */
.s-wide .txt{position:absolute;left:150px;top:0;bottom:0;width:440px;display:flex;flex-direction:column;justify-content:center}
.s-wide .title{font-size:88px}
.s-wide .body{font-size:28px}
.s-wide .ph{left:660px;top:140px;width:1110px;height:770px}

/* pantalla completa */
.s-full .ph.bg{inset:0;width:100%;height:100%}
.s-full .shade{position:absolute;inset:0;background:linear-gradient(90deg,rgba(20,18,16,.62) 0%,rgba(20,18,16,.25) 45%,rgba(20,18,16,0) 70%)}
.s-full .txt{position:absolute;left:150px;bottom:170px}
.s-full .title{color:#fff;font-size:130px}
.s-full .eyebrow{color:var(--gold-light)}
.s-full .foot{color:rgba(255,255,255,.75)}.s-full .foot .num{color:var(--gold-light)}

/* bautizo: grande + 2 */
.s-split2 .ph.main{left:0;top:0;width:820px;height:1080px}
.s-split2 .txt{position:absolute;left:960px;top:140px;width:800px}
.s-split2 .row-ic{display:flex;align-items:center;gap:22px}
.s-split2 .row-ic .eyebrow{margin:0}
.s-split2 .title{font-size:120px;margin:30px 0}
.s-split2 .body{margin-top:30px;max-width:720px}
.s-split2 .small{top:580px;width:360px;height:380px}
.s-split2 .small.a{left:960px}.s-split2 .small.b{left:1380px}

/* trío y cuarteto */
.s-trip .head,.s-quad .head{position:absolute;left:0;right:0;top:100px;text-align:center;display:flex;flex-direction:column;align-items:center;gap:22px}
.s-trip .title,.s-quad .title{font-size:78px}
.s-trip .row{position:absolute;left:150px;right:150px;top:320px;display:grid;grid-template-columns:repeat(3,1fr);gap:70px}
.s-trip .cell .ph,.s-quad .cell .ph{position:relative;width:100%;height:570px}
.s-quad .row{position:absolute;left:150px;right:150px;top:320px;display:grid;grid-template-columns:repeat(4,1fr);gap:36px}
.s-quad .cell:nth-child(even){margin-top:50px}
.s-quad .cell .ph{height:560px}

/* dúo */
.s-duo .txt{position:absolute;left:150px;top:0;bottom:0;width:470px;display:flex;flex-direction:column;justify-content:center}
.s-duo .title{font-size:88px}
.s-duo .body{font-size:28px}
.s-duo .ph.a{left:720px;top:130px;width:500px;height:740px}
.s-duo .ph.b{left:1270px;top:210px;width:500px;height:740px}

/* mosaico y cuadrícula */
.s-mosaic .side,.s-grid6 .side{position:absolute;left:150px;top:0;bottom:0;width:390px;display:flex;flex-direction:column;justify-content:center}
.s-mosaic .title,.s-grid6 .title{font-size:84px;margin:30px 0 36px}
.s-mosaic .body,.s-grid6 .body{font-size:27px;margin-top:34px}
.grid{position:absolute;left:620px;top:110px;width:1150px;height:820px;display:grid;gap:22px}
.grid .ph{position:relative;width:100%;height:100%;min-width:0;min-height:0;overflow:hidden}
.s-mosaic .grid{grid-template-columns:minmax(0,1.25fr) minmax(0,1fr) minmax(0,1fr);grid-template-rows:repeat(2,minmax(0,1fr))}
.s-mosaic .grid .big{grid-row:1/3}
.s-grid6 .grid{grid-template-columns:repeat(3,minmax(0,1fr));grid-template-rows:repeat(2,minmax(0,1fr))}

/* año */
.s-year .txt{position:absolute;left:150px;top:100px;width:440px}
.s-year .big-num{font-family:var(--serif);font-size:150px;font-weight:300;line-height:1}
.s-year .eyebrow{margin-top:10px}
.s-year .title{font-size:80px;margin:24px 0 30px}
.s-year .center{left:660px;top:110px;width:600px;height:820px}
.s-year .l{left:150px;top:560px;width:410px;height:370px}
.s-year .r1{left:1360px;top:110px;width:410px;height:390px}
.s-year .r2{left:1360px;top:540px;width:410px;height:390px}

/* cierre */
.s-end{display:flex;align-items:center;justify-content:center;text-align:center}
.s-end .mono{width:190px;height:190px;border:1px solid var(--gold);border-radius:50%;display:flex;align-items:center;justify-content:center;margin:0 auto 60px;position:relative}
.s-end .mono::after{content:"";position:absolute;inset:10px;border:1px solid var(--gold-light);border-radius:50%;opacity:.6}
.s-end .mono span{font-family:var(--serif);font-style:italic;font-size:110px;font-weight:300}
.s-end .title{font-size:96px;margin:30px 0 34px}
.s-end .icons{display:flex;gap:40px;justify-content:center;margin-top:60px}

/* barra de progreso del modo automático */
#bar{position:absolute;left:0;bottom:0;height:3px;width:0;background:var(--gold-grad);z-index:5;opacity:0}
body.auto #bar{opacity:.9}
/* controles */
.nav{position:fixed;bottom:18px;left:50%;transform:translateX(-50%);display:flex;align-items:center;gap:16px;opacity:0;transition:opacity .6s;z-index:9;font:400 12px var(--sans);letter-spacing:.2em;color:#cdbfa6}
body.ui .nav{opacity:.75}.nav:hover{opacity:1}
.nav button{background:rgba(20,20,20,.55);border:1px solid #6d6457;color:#d6bc8a;min-width:40px;height:40px;border-radius:20px;cursor:pointer;font-size:15px;padding:0 14px}
.nav button:hover{border-color:#d6bc8a}
.nav .count{color:#d6bc8a;min-width:70px;text-align:center}
"""

SVG = """<svg width="0" height="0" style="position:absolute"><defs>
<symbol id="i-star" viewBox="0 0 48 48"><path d="M24 5l5.6 11.9 13 1.6-9.6 9 2.5 12.9L24 34l-11.5 6.4L15 27.5l-9.6-9 13-1.6z"/></symbol>
<symbol id="i-heart" viewBox="0 0 48 48"><path d="M24 41S6 30.4 6 17.6C6 11.7 10.4 8 15.3 8c3.8 0 6.9 2.2 8.7 5.4C25.8 10.2 28.9 8 32.7 8 37.6 8 42 11.7 42 17.6 42 30.4 24 41 24 41z"/></symbol>
<symbol id="i-dove" viewBox="0 0 48 48"><path d="M6 28c6 0 10-3 13-8 2-3.5 5-6 9-6 3 0 5 1.6 6 3.6l6-1.6-4 5c0 9-7 15-16 15-6 0-10-2-14-8z"/><path d="M19 20c-1-5-4-8-9-10 0 6 2 10 6 13"/><circle cx="31" cy="17.5" r=".6"/></symbol>
<symbol id="i-cake" viewBox="0 0 48 48"><path d="M8 40h32M10 40V27h28v13"/><path d="M10 32c3 2.5 6 2.5 9.3 0s6.4-2.5 9.4 0 6.3 2.5 9.3 0"/><path d="M24 27v-7"/><path d="M24 20c-1.8 0-2.8-1.5-2.2-3.2L24 12l2.2 4.8c.6 1.7-.4 3.2-2.2 3.2z"/></symbol>
<symbol id="i-moon" viewBox="0 0 48 48"><path d="M33 34a14 14 0 01-12-25 15 15 0 1017 19 14 14 0 01-5 6z"/><path d="M36 9v6M33 12h6"/></symbol>
<symbol id="i-flower" viewBox="0 0 48 48"><circle cx="24" cy="20" r="4"/><path d="M24 16c-3-6 3-10 3-10s4 5 0 10M28 20c6-3 10 3 10 3s-5 4-10 0M24 24c3 6-3 10-3 10s-4-5 0-10M20 20c-6 3-10-3-10-3s5-4 10 0"/><path d="M24 34v9"/></symbol>
<symbol id="i-steps" viewBox="0 0 48 48"><path d="M15 8c3 0 5 4 5 9s-2 8-5 8-5-3-5-8 2-9 5-9z"/><path d="M11 29h8M33 19c3 0 5 4 5 9s-2 8-5 8-5-3-5-8 2-9 5-9z"/><path d="M29 40h8"/></symbol>
<symbol id="i-camera" viewBox="0 0 48 48"><rect x="6" y="14" width="36" height="24" rx="2"/><path d="M17 14l3-5h8l3 5"/><circle cx="24" cy="26" r="7"/></symbol>
</defs></svg>"""

JS = r"""
const SEG = 9;  // segundos por página en modo automático
const stage = document.getElementById('stage'), bar = document.getElementById('bar');
const slides = [...document.querySelectorAll('.slide')], count = document.getElementById('count');
let i = 0, timer = null;

/* ---------- Música ----------
   Si existe musica.mp3 junto al álbum, se usa esa canción.
   Si no, se genera una melodía original tipo cajita musical con Web Audio. */
const Music = (() => {
  const file = new Audio('musica.mp3'); file.loop = true; file.preload = 'auto';
  let hasFile = null;                       // null = todavía no se sabe
  file.addEventListener('canplaythrough', () => hasFile = true, { once: true });
  file.addEventListener('error', () => hasFile = false, { once: true });
  let ctx, master, dry, conv, sched, nextT = 0, step = 0, playing = false;
  const BPM = 66, E = 60 / BPM / 2;         // duración de una corchea
  // Fa – Rem – Sib – Do (notas MIDI)
  const CH = [[53, 57, 60], [50, 53, 57], [46, 50, 53], [48, 52, 55]];
  const ARP = [0, 1, 2, 1, 2, 1, 0, 1];
  // melodía original: 8 compases x 4 negras (0 = silencio)
  const MEL = [72,0,69,0, 74,72,69,0, 70,0,74,72, 72,0,0,0,
               77,0,76,74, 72,0,69,72, 74,0,70,69, 67,0,72,0];
  const hz = m => 440 * Math.pow(2, (m - 69) / 12);
  function init(){
    ctx = new (window.AudioContext || window.webkitAudioContext)();
    master = ctx.createGain(); master.gain.value = 0; master.connect(ctx.destination);
    conv = ctx.createConvolver();
    const len = ctx.sampleRate * 3.2, ir = ctx.createBuffer(2, len, ctx.sampleRate);
    for (let c = 0; c < 2; c++){ const d = ir.getChannelData(c); for (let k = 0; k < len; k++) d[k] = (Math.random()*2-1) * Math.pow(1 - k/len, 3); }
    conv.buffer = ir;
    dry = ctx.createGain(); dry.gain.value = .75; dry.connect(master);
    const wet = ctx.createGain(); wet.gain.value = .45; conv.connect(wet); wet.connect(master);
  }
  function voice(t, m, vel, dec, type){
    const o = ctx.createOscillator(), g = ctx.createGain();
    o.type = type || 'sine'; o.frequency.value = hz(m);
    g.gain.setValueAtTime(0, t); g.gain.linearRampToValueAtTime(vel, t + .008);
    g.gain.exponentialRampToValueAtTime(.0001, t + dec);
    o.connect(g); g.connect(dry); g.connect(conv);
    o.start(t); o.stop(t + dec + .05);
  }
  function bell(t, m, vel){ voice(t, m, vel, 2.6); voice(t, m + 12, vel * .18, .9); voice(t, m + 19, vel * .05, .5); }
  function tick(){
    while (nextT < ctx.currentTime + .25){
      const bar = Math.floor(step / 8) % 8, e = step % 8, ch = CH[bar % 4];
      if (e === 0) voice(nextT, ch[0] - 12, .16, 4.2, 'triangle');
      bell(nextT, ch[ARP[e]] + 12, .045);
      if (e % 2 === 0){ const n = MEL[bar * 4 + e / 2]; if (n) bell(nextT, n, .11); }
      nextT += E; step++;
    }
  }
  function startSynth(){
    if (!ctx) init();
    ctx.resume(); nextT = ctx.currentTime + .1; step = 0;
    master.gain.cancelScheduledValues(ctx.currentTime);
    master.gain.setValueAtTime(master.gain.value, ctx.currentTime);
    master.gain.linearRampToValueAtTime(.6, ctx.currentTime + 2.5);
    clearInterval(sched); sched = setInterval(tick, 50); tick();
  }
  function stopSynth(){
    if (!ctx) return;
    master.gain.cancelScheduledValues(ctx.currentTime);
    master.gain.setValueAtTime(master.gain.value, ctx.currentTime);
    master.gain.linearRampToValueAtTime(0, ctx.currentTime + 1.2);
    setTimeout(() => { if (!playing){ clearInterval(sched); ctx.suspend(); } }, 1300);
  }
  function play(){
    if (playing) return; playing = true; ui();
    if (hasFile !== false){
      file.play().then(() => { hasFile = true; }).catch(() => { hasFile = false; if (playing) startSynth(); });
    } else startSynth();
  }
  function stop(){ if (!playing) return; playing = false; ui(); if (hasFile) file.pause(); else stopSynth(); }
  function ui(){ document.getElementById('snd').textContent = playing ? '♪  Música: sí' : '♪  Música: no'; }
  return { play, stop, toggle(){ playing ? stop() : play(); }, get on(){ return playing; },
           get engine(){ return hasFile ? 'archivo' : (ctx ? ctx.state : 'ninguno'); } };
})();

function fit(){ const s = Math.min(innerWidth/1920, innerHeight/1080); stage.style.transform = `scale(${s})`; }
function go(n){
  i = Math.max(0, Math.min(slides.length-1, n));
  slides.forEach((s,k) => s.classList.toggle('active', k===i));
  count.textContent = String(i+1).padStart(2,'0') + ' / ' + slides.length;
  history.replaceState(null, '', '#' + (i+1));
  if (timer) restartBar();
}
function restartBar(){ bar.style.transition='none'; bar.style.width='0'; bar.offsetWidth; bar.style.transition=`width ${SEG}s linear`; bar.style.width='100%'; }
function auto(on){
  clearInterval(timer); timer = null; document.body.classList.toggle('auto', on);
  document.getElementById('play').textContent = on ? '❚❚  Pausa' : '▶  Automático';
  if (on){ timer = setInterval(() => { if (i < slides.length-1) go(i+1); else { auto(false); Music.stop(); } }, SEG*1000); restartBar(); Music.play(); }
  else { bar.style.transition='none'; bar.style.width='0'; }
}
function fullscreen(){ if (!document.fullscreenElement && document.documentElement.requestFullscreen) document.documentElement.requestFullscreen().catch(()=>{}); }
function startShow(withAuto){
  document.body.classList.add('started');
  fullscreen(); Music.play(); go(0);
  if (withAuto) auto(true);
}
document.getElementById('start-auto').onclick = () => startShow(true);
document.getElementById('start-manual').onclick = () => startShow(false);
document.getElementById('prev').onclick = () => go(i-1);
document.getElementById('next').onclick = () => go(i+1);
document.getElementById('play').onclick = () => auto(!timer);
document.getElementById('snd').onclick = () => Music.toggle();
document.getElementById('full').onclick = () => document.fullscreenElement ? document.exitFullscreen() : fullscreen();
addEventListener('keydown', e => {
  if (!document.body.classList.contains('started')){ if (e.key === 'Enter' || e.key === ' '){ e.preventDefault(); startShow(true); } return; }
  if (['ArrowRight','PageDown',' '].includes(e.key)) { e.preventDefault(); go(i+1); }
  else if (['ArrowLeft','PageUp'].includes(e.key)) go(i-1);
  else if (e.key==='Home') go(0); else if (e.key==='End') go(slides.length-1);
  else if (e.key==='a' || e.key==='A') auto(!timer);
  else if (e.key==='m' || e.key==='M') Music.toggle();
  else if (e.key==='f' || e.key==='F') document.getElementById('full').click();
});
let t; addEventListener('mousemove', () => { document.body.classList.add('ui'); clearTimeout(t); t = setTimeout(() => document.body.classList.remove('ui'), 2200); });
addEventListener('resize', fit);
const h = parseInt(location.hash.slice(1));
if (h > 1) document.body.classList.add('started');   // enlace directo a una página interior: sin pantalla de inicio
fit(); go((h || 1) - 1);
"""


# ---------------------------------------------------------------------------
# PORTADA (pantalla de inicio) — composición por capas
#   Capa 1  .capa-degradado   degradado CSS (también es el respaldo si no carga el fondo)
#   Capa 2  .capa-fondo       images/portada/fondo-desktop.webp | fondo-mobile.webp
#   Capa 3  .capa-ornamentos  ramas doradas SVG en las esquinas + destellos + remate
#   Capa 4  .capa-marco       marco perimetral fino
#   Capa 5  .capa-contenido   monograma, títulos y botones (HTML)
# Los recursos los genera portada_recursos.py. Los ids start-auto / start-manual
# no cambian: la música, la navegación y las fotos siguen igual.
# ---------------------------------------------------------------------------
RP = "images/portada/"

DESTELLOS = [  # (left %, top %, tamaño px, duración s, retraso s)
    (19, 31, 16, 8, 0), (76, 27, 14, 9.5, 1.4), (27, 64, 12, 10, 3), (71, 70, 15, 8.5, 2.2),
    (37, 18, 10, 11, 4), (63, 84, 10, 9, 5)]


def intro_html():
    esquinas = "".join(f'<img class="orn {c}" src="{RP}ornamento-{n}.svg" alt="">'
                       for c, n in (("sup-izq", "superior-izquierdo"), ("sup-der", "superior-derecho"),
                                    ("inf-izq", "inferior-izquierdo"), ("inf-der", "inferior-derecho")))
    brillos = "".join(f'<img class="brillo" src="{RP}destello.svg" alt="" '
                      f'style="left:{x}%;top:{y}%;width:{s}px;--dur:{d}s;--del:{dl}s">'
                      for x, y, s, d, dl in DESTELLOS)
    return f"""<div id="intro">
  <div class="capa capa-degradado" aria-hidden="true"></div>
  <div class="capa capa-fondo" aria-hidden="true"></div>
  <div class="capa capa-ornamentos" aria-hidden="true">{esquinas}{brillos}
    <img class="remate" src="{RP}remate-inferior.svg" alt="">
  </div>
  <div class="capa capa-marco" aria-hidden="true"></div>
  <div class="capa-contenido">
    <div class="box">
      <div class="i-mono">
        <svg class="i-ring" viewBox="0 0 160 160" aria-hidden="true">
          <defs><linearGradient id="g-anillo" x1="0" y1="0" x2="1" y2="1">
            <stop offset="0" stop-color="#F7E9C6"/><stop offset=".35" stop-color="#D6B779"/>
            <stop offset=".7" stop-color="#B8924E"/><stop offset="1" stop-color="#EBD7A6"/></linearGradient></defs>
          <circle class="r1" cx="80" cy="80" r="72"/><circle class="r2" cx="80" cy="80" r="66"/>
        </svg>
        <span>{NOMBRE[0]}</span>
        <img class="i-ring-spark" src="{RP}destello.svg" alt="">
        <img class="i-laurel izq" src="{RP}laurel-izquierdo.svg" alt="">
        <img class="i-laurel der" src="{RP}laurel-derecho.svg" alt="">
      </div>
      <div class="i-eyebrow"><i></i><span>Álbum familiar</span><i></i></div>
      <h1>{NOMBRE}</h1>
      <div class="i-sep" aria-hidden="true"><i></i><img src="{RP}corazon.svg" alt=""><i></i></div>
      <p>Mis primeros tres años</p>
      <div class="btns">
        <button id="start-auto" class="i-btn primary"><svg viewBox="0 0 12 14" aria-hidden="true"><path d="M1 1l10 6-10 6z"/></svg>Ver con música</button>
        <button id="start-manual" class="i-btn ghost">Pasar las páginas yo</button>
      </div>
      <div class="keys">← → páginas · A automático · M música · F pantalla completa</div>
    </div>
  </div>
</div>"""


INTRO_CSS = r"""
/* ===== Portada por capas ===== */
#intro{--deep:#A85F7D;--champ:#D6B779;--ivory:#FFF5EF;
  --marco:clamp(10px,calc(1.4vmin + 4px),28px);          /* separación del marco al borde */
  --orn:min(17vw,30vh,340px);                             /* tamaño de cada ornamento de esquina */
  position:fixed;inset:0;z-index:20;overflow:hidden auto;transition:opacity 1.1s ease,visibility 1.1s}
body.started #intro{opacity:0;visibility:hidden}

/* capas fijas detrás del contenido */
.capa{position:fixed;inset:0;pointer-events:none}
.capa-degradado{z-index:0;background:
  linear-gradient(160deg,rgba(168,95,125,0) 35%,rgba(118,72,112,.42) 100%),
  radial-gradient(ellipse at 50% 42%,#D49BB2 0%,#C7839F 35%,#B46F8C 70%,#A85F7D 100%)}
.capa-fondo{z-index:1;background:url("images/portada/fondo-desktop.webp") center/cover no-repeat}
.capa-ornamentos{z-index:2}
.capa-marco{z-index:3;inset:var(--marco);border:1px solid rgba(214,183,121,.6)}
.capa-marco::after{content:"";position:absolute;inset:6px;border:1px solid rgba(214,183,121,.25)}

/* ornamentos de esquina: tamaño fijo cuadrado (nunca se deforman) anclado al marco */
.orn{position:absolute;width:var(--orn);height:var(--orn);
  --pos:max(2px,calc(var(--marco) - var(--orn) * .09));
  filter:drop-shadow(0 1px 1px rgba(90,40,60,.15));animation:i-fade 2.2s ease .3s both}
.orn.sup-izq{left:var(--pos);top:var(--pos)}
.orn.sup-der{right:var(--pos);top:var(--pos)}
.orn.inf-izq{left:var(--pos);bottom:var(--pos);animation-delay:.6s}
.orn.inf-der{right:var(--pos);bottom:var(--pos);animation-delay:.6s}
.brillo{position:absolute;height:auto;opacity:0;animation:i-twinkle var(--dur) ease-in-out var(--del) infinite}
.remate{position:absolute;left:50%;bottom:calc(var(--marco) + 10px);transform:translateX(-50%);
  width:clamp(140px,15vw,250px);height:auto;animation:i-fade 2s ease 1.4s both}

/* capa de contenido */
.capa-contenido{position:relative;z-index:4;min-height:100%;display:flex;text-align:center}
#intro .box{margin:auto;width:100%;max-width:1100px;
  padding:max(calc(var(--marco) + 40px),9vh) 24px max(calc(var(--marco) + 64px),11vh)}

/* monograma */
.i-mono{--m:clamp(84px,min(11vw,16vh),156px);position:relative;width:var(--m);height:var(--m);
  margin:0 auto calc(var(--m) * .3);display:flex;align-items:center;justify-content:center;
  animation:i-mono 1.6s cubic-bezier(.2,.7,.2,1) both}
.i-ring{position:absolute;inset:0;width:100%;height:100%;overflow:visible}
.i-ring .r1{fill:rgba(168,95,125,.25);stroke:url(#g-anillo);stroke-width:2.6;stroke-dasharray:453;stroke-dashoffset:453;
  animation:i-draw 2.2s ease .3s forwards;filter:drop-shadow(0 0 6px rgba(246,224,180,.55))}
.i-ring .r2{fill:none;stroke:rgba(214,183,121,.55);stroke-width:.8}
.i-mono span{position:relative;font-family:var(--serif);font-style:italic;font-weight:500;font-size:calc(var(--m) * .56);
  line-height:1;color:var(--ivory);text-shadow:0 2px 10px rgba(110,40,70,.35);margin-top:-4%}
.i-ring-spark{position:absolute;right:4%;top:0;width:24%;height:auto;animation:i-twinkle 6s ease-in-out 1.8s infinite}
.i-laurel{position:absolute;bottom:-10%;width:66%;height:auto;animation:i-fade 1.8s ease .9s both}
.i-laurel.izq{left:-38%;transform:rotate(-14deg)}
.i-laurel.der{right:-38%;transform:rotate(14deg)}

/* textos */
.i-eyebrow{display:flex;align-items:center;justify-content:center;gap:clamp(12px,2vw,26px);
  font:500 clamp(13px,1.45vw,22px) var(--sans);letter-spacing:.42em;text-transform:uppercase;color:#F7E6D6;
  animation:i-rise 1.4s ease .45s both}
.i-eyebrow span{padding-left:.42em}
.i-eyebrow i,.i-sep i{display:block;height:1px;width:clamp(36px,11vw,170px);background:linear-gradient(90deg,rgba(227,200,143,0),#E3C88F)}
.i-eyebrow i:last-child,.i-sep i:last-child{background:linear-gradient(90deg,#E3C88F,rgba(227,200,143,0))}
#intro h1{font-family:var(--serif);font-style:italic;font-weight:500;line-height:1.02;letter-spacing:.01em;
  font-size:clamp(56px,min(12vw,19vh),184px);margin:clamp(4px,1.4vh,16px) 0 clamp(2px,1vh,10px);color:var(--ivory);
  text-shadow:0 6px 24px rgba(110,40,70,.35),0 0 1px rgba(214,183,121,.6);animation:i-name 1.8s cubic-bezier(.2,.7,.2,1) .6s both}
.i-sep{display:flex;align-items:center;justify-content:center;gap:14px;animation:i-rise 1.4s ease .95s both}
.i-sep i{width:clamp(44px,14vw,250px)}
.i-sep img{width:clamp(24px,2.6vw,40px);height:auto}
#intro p{font-family:var(--serif);font-style:italic;font-weight:500;font-size:clamp(22px,min(3.4vw,5.2vh),52px);
  color:var(--ivory);margin-top:clamp(4px,1.2vh,14px);text-shadow:0 2px 12px rgba(110,40,70,.3);animation:i-rise 1.4s ease 1.05s both}

/* botones (mismos ids y eventos; solo cambia el aspecto) */
#intro .btns{display:flex;gap:clamp(14px,2vw,28px);justify-content:center;flex-wrap:wrap;margin-top:clamp(22px,5vh,58px);
  animation:i-rise 1.4s ease 1.25s both}
.i-btn{display:inline-flex;align-items:center;justify-content:center;gap:16px;cursor:pointer;border-radius:999px;
  font:500 clamp(12px,1.25vw,18px) var(--sans);letter-spacing:.24em;text-transform:uppercase;
  padding:clamp(14px,2.2vh,22px) clamp(26px,3.4vw,50px);border:1px solid var(--champ);
  transition:transform .35s cubic-bezier(.2,.7,.2,1),box-shadow .35s ease,filter .35s ease,background-color .35s ease}
.i-btn svg{width:.95em;height:1.1em;fill:currentColor;flex:none}
.i-btn.primary{background:var(--ivory);color:var(--deep);box-shadow:0 8px 22px rgba(96,36,62,.28),inset 0 0 0 3px rgba(255,255,255,.55)}
.i-btn.ghost{background:transparent;color:var(--ivory)}
.i-btn:hover,.i-btn:focus-visible{transform:translateY(-3px);filter:brightness(1.05)}
.i-btn.primary:hover,.i-btn.primary:focus-visible{box-shadow:0 14px 30px rgba(96,36,62,.34),inset 0 0 0 3px rgba(255,255,255,.7)}
.i-btn.ghost:hover,.i-btn.ghost:focus-visible{background:rgba(255,245,239,.1);box-shadow:0 12px 26px rgba(96,36,62,.22)}
.i-btn:focus-visible{outline:2px solid var(--ivory);outline-offset:4px}
.i-btn:active{transform:translateY(-1px)}
#intro .keys{margin-top:clamp(16px,3.4vh,40px);font:500 clamp(10px,1.05vw,15px) var(--sans);letter-spacing:.24em;
  text-transform:uppercase;color:rgba(255,245,239,.85);animation:i-rise 1.4s ease 1.45s both}

/* ---------- composición por dispositivo ---------- */
/* Portátil y monitores 4:3 (horizontal, ≤1366): ornamentos proporcionalmente menores */
@media (orientation:landscape) and (max-width:1366px){
  #intro{--orn:min(16vw,28vh,300px)}
}
/* Tablet y teléfono en vertical: fondo vertical, ornamentos en las cuatro esquinas
   y contenido con margen superior/inferior para no cruzarse con las ramas */
@media (orientation:portrait){
  #intro{--orn:min(30vw,20vh,250px)}
  .capa-fondo{background-image:url("images/portada/fondo-mobile.webp")}
  #intro .box{padding:calc(var(--marco) + var(--orn) * .62) 20px calc(var(--marco) + var(--orn) * .62)}
  .remate{width:min(30vw,220px)}
}
/* Tablet vertical: contenido más grande para aprovechar el alto */
@media (orientation:portrait) and (min-width:601px){
  .i-mono{--m:clamp(110px,15vw,170px)}
  .i-eyebrow{font-size:clamp(15px,2.2vw,22px)}
  #intro h1{font-size:clamp(96px,15vw,170px)}
  #intro p{font-size:clamp(28px,4.4vw,46px)}
  .i-btn{font-size:clamp(13px,1.8vw,17px)}
  #intro .keys{font-size:clamp(11px,1.5vw,14px)}
}
/* Teléfono vertical */
@media (orientation:portrait) and (max-width:600px){
  .i-eyebrow{letter-spacing:.3em;font-size:12px}
  .i-eyebrow i{width:26px}
  #intro h1{font-size:clamp(54px,17vw,84px)}
  #intro p{font-size:clamp(20px,6vw,26px)}
  #intro .btns{flex-direction:column;align-items:center;gap:14px}
  .i-btn{width:min(100%,300px);letter-spacing:.18em;font-size:13px;padding:16px 20px}
  #intro .keys{display:none}
}
/* Teléfono horizontal y pantallas bajas: composición horizontal compacta */
@media (orientation:landscape) and (max-height:500px){
  #intro{--orn:min(15vw,30vh,140px)}
  #intro .box{padding:calc(var(--marco) + 18px) calc(var(--orn) * .55) calc(var(--marco) + 26px)}
  .i-mono{--m:62px;margin-bottom:20px}
  .i-eyebrow{font-size:11px}
  #intro h1{font-size:52px;margin:2px 0}
  #intro p{font-size:19px;margin-top:2px}
  #intro .btns{margin-top:14px;flex-wrap:nowrap}
  .i-btn{padding:11px 20px;font-size:11px;letter-spacing:.18em}
  #intro .keys,.remate{display:none}
}

/* animaciones suaves */
@keyframes i-fade{from{opacity:0}to{opacity:1}}
@keyframes i-rise{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:none}}
@keyframes i-mono{from{opacity:0;transform:scale(.9)}to{opacity:1;transform:none}}
@keyframes i-name{from{opacity:0;transform:translateY(18px);filter:blur(8px)}to{opacity:1;transform:none;filter:blur(0)}}
@keyframes i-draw{to{stroke-dashoffset:0}}
@keyframes i-twinkle{0%,100%{opacity:0;transform:translateY(0) scale(.6)}45%{opacity:.85;transform:translateY(-6px) scale(1)}60%{opacity:.6}}
@media (prefers-reduced-motion:reduce){
  #intro,#intro *{animation:none!important;transition:none!important}
  .i-ring .r1{stroke-dashoffset:0}
  .brillo{opacity:.5}
}
"""


def construir():
    preparar_fotos()
    cuerpo = "\n".join(page(p, n) for n, p in enumerate(PAGINAS, 1))
    doc = f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{NOMBRE} · Mis primeros tres años</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300;1,400;1,500&family=Montserrat:wght@300;400;500&display=swap" rel="stylesheet">
<style>{CSS}{TEMAS[TEMA]}{INTRO_CSS}</style></head>
<body>
{SVG}
<div id="stage">
{cuerpo}
<div id="bar"></div>
</div>
{intro_html()}
<div class="nav"><button id="prev">‹</button><span class="count" id="count"></span><button id="next">›</button>
<button id="play">▶  Automático</button><button id="snd">♪  Música: no</button><button id="full">⛶</button></div>
<script>{JS}</script>
</body></html>"""
    out = os.path.join(AQUI, SALIDA)
    open(out, "w", encoding="utf-8").write(doc)
    print(len(PAGINAS), "páginas, tema", TEMA, "->", out)
    if SALIDA != "index.html":
        return  # una muestra: no se toca la versión de un solo archivo
    # versión de un solo archivo (fotos incrustadas) para llevar en una USB
    import re, base64
    solo = re.sub(r'src="(fotos/[^"]+\.jpg)"', lambda m: 'src="data:image/jpeg;base64,' +
                  base64.b64encode(open(os.path.join(AQUI, m.group(1)), "rb").read()).decode() + '"', doc)
    # recursos de la portada (SVG y WEBP), tanto en src="..." como en url("...")
    tipos = {".svg": "image/svg+xml", ".webp": "image/webp"}
    def incrustar(m):
        ruta = m.group(2); ext = os.path.splitext(ruta)[1]
        datos = base64.b64encode(open(os.path.join(AQUI, ruta), "rb").read()).decode()
        return f'{m.group(1)}data:{tipos[ext]};base64,{datos}{m.group(3)}'
    solo = re.sub(r'(src="|url\(")(images/portada/[^"]+\.(?:svg|webp))(")', incrustar, solo)
    open(os.path.join(AQUI, f"{NOMBRE} - Album (un solo archivo).html"), "w", encoding="utf-8").write(solo)

# ---------------------------------------------------------------------------
# TEMAS de color.  "clasico" = dorado y gris.  "rosa" = rosado, lila y oro rosa,
# con letra más grande para que se lea bien desde lejos.
# Uso:  python generar.py                                    (tema rosa, actualiza index.html)
#       python generar.py --tema clasico --salida muestra.html  (solo una muestra)
# ---------------------------------------------------------------------------
TEMAS = {"clasico": "", "rosa": r"""
:root{--paper:#FBF6F5;--ink:#3D3340;--charcoal:#3A2B44;--gray:#8B7F8E;--line:#E7D9DE;
--gold:#C08AA2;--gold-light:#DCC2DA;
--gold-grad:linear-gradient(135deg,#EDC9C0 0%,#CC97A8 40%,#9E84C2 78%,#D9BCDD 100%)}
.slide{background:linear-gradient(135deg,#FDF8F7 0%,#FAF1F3 55%,#F5F0F9 100%)}
.dark{background:radial-gradient(ellipse at 30% 45%,#4D3A5C 0%,#33263E 72%)}
.dark .title{color:#FDF4F7}.dark .body{color:#D6C8DC}.dark .foot{color:#B9A8C2}
.title{color:#3D3340}
.eyebrow{font-size:19px;font-weight:500;letter-spacing:.3em;color:#9884BA}
.eyebrow.gold{color:#C9879F}
.body{font-size:38px;line-height:1.38;font-weight:500;color:#5C5062}
.caption{font-size:17px;font-weight:500;letter-spacing:.2em;color:#8E7A98;margin-top:20px}
.caption::before{background:#D9A0B4}
.foot{font-size:15px;letter-spacing:.3em;color:#9C8FA0}
.foot .num{font-size:30px}
.ic{stroke:#B387BB}
.ph.framed::after{border-color:#DDC3DD}
.s-chapter .ph.framed::after{border-color:rgba(236,196,220,.6)}
.s-cover .title{font-size:220px}
.s-cover .sub{font-size:50px;color:#8C6F92}
.s-cover .chapters div{font-size:15px;font-weight:500;letter-spacing:.16em;color:#8E7A98}
.s-chapter .title{font-size:150px}
.s-chapter .body{max-width:700px}
.s-feature .title{font-size:116px}
.s-feature .quote{font-size:40px;color:#C9879F}
.s-wide .txt{width:470px}.s-wide .ph{left:680px;width:1090px}
.s-wide .title{font-size:96px}.s-wide .body{font-size:36px}
.s-trip .title,.s-quad .title{font-size:92px}
.s-trip .row,.s-quad .row{top:340px}
.s-trip .cell .ph{height:540px}.s-quad .cell .ph{height:520px}
.s-duo .txt{width:500px}.s-duo .title{font-size:96px}.s-duo .body{font-size:36px}
.s-mosaic .side,.s-grid6 .side{width:440px}
.s-mosaic .title,.s-grid6 .title{font-size:90px}
.s-mosaic .body,.s-grid6 .body{font-size:34px}
.grid{left:650px;width:1120px}
.s-split2 .title{font-size:128px}
.s-year .title{font-size:88px}
.s-year .eyebrow{font-size:17px}
.s-end .title{font-size:110px}
.s-end .mono{border-color:#C08AA2}
#bar{height:4px}
.nav button{border-color:#8E7A98;color:#F0C3D3}
.nav .count{color:#F0C3D3}

/* Capítulos intercalados: I, III y V en morado; II y IV en rosado */
.s-chapter.c2,.s-chapter.c4{background:radial-gradient(ellipse at 30% 45%,#D691A9 0%,#B26886 55%,#94506E 100%)}
.s-chapter.c2 .roman,.s-chapter.c4 .roman{background:linear-gradient(135deg,#FFF3F6 0%,#F9D3DF 50%,#EDD3F2 100%);-webkit-background-clip:text;background-clip:text;color:transparent}
.s-chapter.c2 .eyebrow.gold,.s-chapter.c4 .eyebrow.gold{color:#FFE6EE}
.s-chapter.c2 .title,.s-chapter.c4 .title{color:#FFFFFF}
.s-chapter.c2 .body,.s-chapter.c4 .body{color:#FDEBF1}
.s-chapter.c2 .rule,.s-chapter.c4 .rule{background:linear-gradient(90deg,#FFF3F6,#F3C6D6)}
.s-chapter.c2 .ph.framed::after,.s-chapter.c4 .ph.framed::after{border-color:rgba(255,236,242,.75)}
.s-chapter.c2 .foot,.s-chapter.c4 .foot{color:rgba(255,240,245,.85)}
.s-chapter.c2 .foot .num,.s-chapter.c4 .foot .num{color:#FFFFFF}

"""}

import sys
_A = sys.argv[1:]
TEMA = _A[_A.index("--tema") + 1] if "--tema" in _A else "rosa"   # aprobado el 2026-11-27
SALIDA = _A[_A.index("--salida") + 1] if "--salida" in _A else "index.html"

if __name__ == "__main__":
    construir()
