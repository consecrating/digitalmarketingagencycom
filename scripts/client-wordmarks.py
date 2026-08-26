#!/usr/bin/env python3
"""
Render clean WHITE wordmark logos for the real clients, matching the
existing marquee style (monochrome light wordmarks on transparent bg).
"""
import os
from PIL import Image, ImageDraw, ImageFont

WORKSPACE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(WORKSPACE, "assets/img/brands")
os.makedirs(OUT, exist_ok=True)

FONT_BOLD = "/usr/share/fonts/google-noto/NotoSans-ExtraBold.ttf"
FONT_COND = "/usr/share/fonts/google-noto/NotoSans-SemiCondensedExtraBold.ttf"

# Real clients -> (filename, display text). White wordmarks, uppercase for uniformity.
CLIENTS = [
    ("1.png", "Mercedes-Benz"),
    ("2.png", "Hindustan Petroleum"),
    ("3.png", "Casino Pride"),
    ("4.png", "Kidzee"),
    ("5.png", "BJP"),
    ("6.png", "St Anthony School"),
    ("7.png", "Edify School"),
    ("8.png", "Mount Litera Zee"),
]

# Canvas sized like the original brand logos; text vertically centered, white, transparent bg
W, H = 520, 130
COLOR = (255, 255, 255, 255)  # solid white; marquee CSS applies faded opacity


def render(fn, text):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    # Pick font size that fits width
    size = 62
    font_path = FONT_BOLD if len(text) <= 12 else FONT_COND
    while size > 20:
        font = ImageFont.truetype(font_path, size)
        bbox = d.textbbox((0, 0), text, font=font)
        tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
        if tw <= W - 40:
            break
        size -= 2
    font = ImageFont.truetype(font_path, size)
    bbox = d.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    x = (W - tw) / 2 - bbox[0]
    y = (H - th) / 2 - bbox[1]
    d.text((x, y), text, font=font, fill=COLOR)
    img.save(os.path.join(OUT, fn))
    print(f"  ✓ {fn}  '{text}'  (size {size})")


if __name__ == "__main__":
    print("Rendering white client wordmarks...")
    for fn, text in CLIENTS:
        render(fn, text)
    print("Done.")
