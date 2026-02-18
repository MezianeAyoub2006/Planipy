from PIL import Image, ImageDraw, ImageFont
import sys
import os

CHARSET = ''.join(chr(i) for i in range(32, 127))

def generate_glyphs(font_path, font_size, output_path="glyphs.png"):
    font = ImageFont.truetype(font_path, font_size)

    sizes = [font.getbbox(c) for c in CHARSET]
    glyph_w = max(b[2] - b[0] for b in sizes)
    glyph_h = max(b[3] - b[1] for b in sizes)

    cols = 16
    rows = (len(CHARSET) + cols - 1) // cols

    img_w = cols * glyph_w
    img_h = rows * glyph_h

    img = Image.new("RGBA", (img_w, img_h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    for i, char in enumerate(CHARSET):
        col = i % cols
        row = i // cols
        x = col * glyph_w
        y = row * glyph_h
        bbox = font.getbbox(char)
        offset_x = -bbox[0]
        offset_y = -bbox[1]
        draw.text((x + offset_x, y + offset_y), char, fill=(255, 255, 255, 255), font=font)

    img.save(output_path)

    print(f"Spritesheet : {output_path}")
    print(f"Taille glyphe : {glyph_w}x{glyph_h}px")
    print(f"Grille : {cols}x{rows} ({len(CHARSET)} glyphes)")
    print(f"Image : {img_w}x{img_h}px")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(1)

    font_path = sys.argv[1]
    font_size = int(sys.argv[2])
    output = sys.argv[3] if len(sys.argv) > 3 else "glyphs.png"

    if not os.path.exists(font_path):
        print(f"Font introuvable : {font_path}")
        sys.exit(1)

    generate_glyphs(font_path, font_size, output)