#!/usr/bin/env python3
import re

from PIL import Image, ImageDraw, ImageFont, ImageFilter # pip install Pillow

try:
    from secret import FLAG
except ImportError:
    FLAG = "cratectf{1111 1111 1111 1111}"
    print(f"Flag not available, using placeholder: {FLAG}")

FONT_FILE = "LiberationMono-Regular.ttf"
FLAG_POSITION = (90, 280)

# Load base image
img = Image.open("card_blank.png")
draw = ImageDraw.Draw(img)

# Load fonts
font = ImageFont.truetype(FONT_FILE, size=50)
small_font = ImageFont.truetype(FONT_FILE, size=14)

# Break flag into components, e.g.:
# flag_prefix = "ctfname{"
# flag = "1111 1111 1111 1111"
# flag_suffix = "}"
flag_prefix, flag, flag_suffix = re.search(r"(.*\{)(.+)(\})", FLAG).group(1, 2, 3)

# Print flag prefix and suffix onto base image
draw.text((5, FLAG_POSITION[1] + 18), flag_prefix, font=small_font, fill=("white"))
width, height = draw.textsize(flag, font=font)
draw.text((FLAG_POSITION[0] + width + 10, FLAG_POSITION[1] + 18), flag_suffix, font=small_font, fill="white")

# Print flag onto base image
draw.text(FLAG_POSITION, flag, font=font, fill="white")

# Blur the flag-containing part of the image
flag_coords = (FLAG_POSITION[0], FLAG_POSITION[1], FLAG_POSITION[0] + width, FLAG_POSITION[1] + height)
blur_part = img.crop(flag_coords)
blur_part = blur_part.filter(ImageFilter.BoxBlur(radius=20))
img.paste(blur_part, flag_coords)

print("Flag bounding box:", flag_coords)
print(f"Flag is {len(flag)} characters long.")

img.save("card.png")
