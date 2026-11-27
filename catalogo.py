# Crea un catálogo con IDs cortos para cada foto y hojas de contacto para elegirlas.
import os, glob, json, re, sys
from PIL import Image, ImageOps, ImageDraw, ImageFont, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
os.chdir(os.path.dirname(os.path.abspath(__file__)) + "/..")
caps = [("N", "1ero*"), ("B", "2do*"), ("U", "3ro*"), ("D", "4to*"), ("T", "5to*")]
def key(f):
    m = re.match(r"(\d+)", os.path.basename(f)); return (int(m.group(1)) if m else 999, os.path.basename(f))
cat = {}
for pre, pat in caps:
    d = glob.glob(pat)[0]
    files = [f for f in glob.glob(d + "/*") if f.lower().endswith((".jpg", ".jpeg"))]
    if pre == "N":
        files += glob.glob("presentacion/heic/*.jpg")
    for n, f in enumerate(sorted(files, key=key), 1):
        cat[f"{pre}{n:03d}"] = f.replace("\\", "/")
json.dump(cat, open("presentacion/catalogo.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
out = sys.argv[1]
font = ImageFont.truetype("arial.ttf", 22)
ids = list(cat)
per, cols, tw, th = 48, 8, 200, 220
for s in range(0, len(ids), per):
    chunk = ids[s:s+per]; rows = (len(chunk)+cols-1)//cols
    sheet = Image.new("RGB", (cols*tw, rows*(th+28)), "white"); d = ImageDraw.Draw(sheet)
    for i, k in enumerate(chunk):
        im = ImageOps.exif_transpose(Image.open(cat[k])).convert("RGB"); w, h = im.size
        im.thumbnail((tw-6, th-6)); x, y = (i%cols)*tw, (i//cols)*(th+28)
        sheet.paste(im, (x+3, y+3))
        d.text((x+4, y+th+2), f"{k} {'H' if w>h*1.05 else 'V' if h>w*1.05 else 'C'}", fill="black", font=font)
    sheet.save(f"{out}/cat{s//per+1:02d}.jpg", quality=72)
print(len(cat), "fotos")
