"""Pone el logo de Escuadrón Geek en la esquina inferior derecha de una imagen.

Uso: python3 _marca/logo_stamp.py imagen.jpg blanco|negro
  blanco -> para fondos oscuros, negro -> para fondos claros.
Deja libre la zona inferior derecha (unos 330x130 px en una imagen de 1600x900).
"""
import os
import sys
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))


def stamp(path, variant, height=88, margin=(110, 60)):
    im = Image.open(path).convert("RGB")
    W, H = im.size
    lg = Image.open(os.path.join(HERE, f"logo-{variant}.png"))
    w = int(lg.width * height / lg.height)
    lg = lg.resize((w, height), Image.LANCZOS)
    im.paste(lg, (W - margin[0] - w, H - margin[1] - height), lg)
    im.save(path, quality=84, optimize=True, progressive=True)


if __name__ == "__main__":
    stamp(sys.argv[1], sys.argv[2])
