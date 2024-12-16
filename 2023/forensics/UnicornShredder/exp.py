#!/usr/bin/env python3

import argparse
import io

from PIL import Image, ImageDraw  # pip install Pillow
import requests

BLOCK_X, BLOCK_Y = 30, 30

BASE_URL = "http://challs.crate.nu:41141"


def counter_to_rgb(c: int):
    return int(c / pow(255, 2)), int(c / 255), c % 255


def rgb_to_counter(r: int, g: int, b: int):
    return r * pow(255, 2) + g * 255 + b


def counter_to_xy(image: Image.Image, c: int):
    blocks_y = int(image.size[1] / BLOCK_Y)
    return int(c / blocks_y) * BLOCK_Y, (c % blocks_y) * BLOCK_X


def generate_pattern(width: int, height: int) -> Image.Image:
    img = Image.new("RGB", (width, height))

    draw = ImageDraw.Draw(img)

    counter = 0

    for x in range(0, img.size[0], BLOCK_X):
        for y in range(0, img.size[1], BLOCK_Y):
            r, g, b = counter_to_rgb(counter)
            draw.rectangle(xy=(x, y, x + BLOCK_X - 1, y + BLOCK_Y - 1), fill=(r, g, b))
            counter += 1

    return img


def shred(image: Image.Image) -> Image.Image:
    image_png = io.BytesIO()
    image.save(image_png, format="png")
    upload = requests.post(
        f"{BASE_URL}/upload.php", files={"file": image_png.getvalue()}, timeout=3
    )
    upload.raise_for_status()
    shredded = requests.get(f"{BASE_URL}/{upload.json()['output']}", timeout=3)
    shredded.raise_for_status()
    shredded_image = io.BytesIO(shredded.content)
    return Image.open(shredded_image)


def solve_pattern(image: Image.Image) -> dict[int, int]:
    counter = 0

    # Scrambled position to true position
    block_map = {}

    for x in range(0, image.size[0], BLOCK_X):
        for y in range(0, image.size[1], BLOCK_Y):
            r, g, b = image.getpixel((x + 2, y + 2))
            block_map[counter] = rgb_to_counter(r, g, b)
            counter += 1

    # True position to scrambled position
    block_map2 = {}

    for k, v in block_map.items():
        block_map2[v] = k

    return block_map2


def unscramble_image(image: Image.Image, block_map: dict[int, int]) -> Image.Image:
    counter = 0
    restored_image = image.copy()
    for x in range(0, image.size[0], BLOCK_X):
        for y in range(0, image.size[1], BLOCK_Y):
            true_x, true_y = counter_to_xy(image, block_map[counter])
            segment = image.crop((true_x, true_y, true_x + BLOCK_X, true_y + BLOCK_Y))
            restored_image.paste(segment, (x, y))
            counter += 1

    return restored_image


def main():
    parser = argparse.ArgumentParser(description="Solve script for Unicorn Shredder")
    parser.add_argument("flag", help="Path to shredded flag")

    args = parser.parse_args()

    flag = Image.open(args.flag)
    pattern = generate_pattern(*flag.size)

    for _ in range(30):
        scrambled_pattern = shred(pattern)
        block_map = solve_pattern(scrambled_pattern)
        restored_flag = unscramble_image(flag, block_map)
        restored_flag.show()


if __name__ == "__main__":
    main()
