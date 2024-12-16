#!/usr/bin/env python3

import argparse
import io
import sys
from tkinter import Canvas, Label, Tk

import requests
from PIL import Image, ImageDraw, ImageTk  # pip install Pillow


class ShredderSolver:
    """
    GUI for displaying unshredded images.
    """

    def __init__(self, root, flag: Image.Image, block_size: tuple[int, int], url: str) -> None:
        self.block_x, self.block_y = block_size
        self.flag = flag
        self.url = url
        Label(text="Press enter to cycle through shred patterns, escape to quit").grid(row=0, column=0)
        self.canvas = Canvas(root, width=flag.size[0], height=flag.size[1])
        self.canvas.grid(row=1, column=0)
        self.pattern = self.generate_pattern(*flag.size)
        self.restored_flag = None
        self.new_pattern()

    def new_pattern(self, *_args):
        """
        Request a new shredded image from the server, reverse its shred pattern and apply it to the flag.
        """
        scrambled_pattern = self.shred(self.pattern)
        block_map = self.solve_pattern(scrambled_pattern)
        self.restored_flag = ImageTk.PhotoImage(self.unscramble_image(self.flag, block_map))
        self.canvas.create_image(0, 0, anchor="nw", image=self.restored_flag)

    def counter_to_rgb(self, c: int) -> tuple[int, int, int]:
        """
        Converts a sequential counter value (i.e. block number) to an RGB color value. Inverse of `rgb_to_counter`.

        @param c: Counter value

        @returns A tuple containing the red, green, and blue channel as 8-bit integers.
        """
        return int(c / pow(255, 2)), int(c / 255), c % 255

    def rgb_to_counter(self, r: int, g: int, b: int) -> int:
        """
        Converts an 8-bit RGB color value to a sequential value. Inverse of `counter_to_rgb`.

        @param r: Red value
        @param g: Green value
        @param b: Blue value

        @returns Counter value as an integer.
        """
        return r * pow(255, 2) + g * 255 + b

    def counter_to_xy(self, image: Image.Image, c: int) -> tuple[int, int]:
        """
        Converts a sequential counter value (i.e. block number) to the block's XY coordinates.

        @param image: Image used to produce counter value
        @param c: Counter value

        @returns A tuple with the X and Y coordinates.
        """
        blocks_y = int(image.size[1] / self.block_y)
        return int(c / blocks_y) * self.block_x, (c % blocks_y) * self.block_y

    def generate_pattern(self, width: int, height: int) -> Image.Image:
        """
        Creates an image with the given dimensions containing blocks with a known pattern (increasing RGB color values).
        Used to generate a known pattern that `solve_pattern` can use to reverse the shredding operation.

        @param width: Desired image width
        @param height: Desired image height

        @returns An image object.
        """
        img = Image.new("RGB", (width, height))

        draw = ImageDraw.Draw(img)

        counter = 0

        for x in range(0, img.size[0], self.block_x):
            for y in range(0, img.size[1], self.block_y):
                r, g, b = self.counter_to_rgb(counter)
                draw.rectangle(xy=(x, y, x + self.block_x - 1, y + self.block_y - 1), fill=(r, g, b))
                counter += 1

        return img

    def shred(self, image: Image.Image) -> Image.Image:
        """
        Upload an image to the challenge server, shred it and fetch the result.

        @param image: Image to shred

        @returns Shredded image.
        """
        image_png = io.BytesIO()
        image.save(image_png, format="png")
        upload = requests.post(
            f"{self.url}/upload.php",
            files={"file": image_png.getvalue()},
            data={"algo": "ultra-secure"},
            timeout=3,
        )
        upload.raise_for_status()
        shredded = requests.get(f"{self.url}/{upload.json()['output']}", timeout=3)
        shredded.raise_for_status()
        shredded_image = io.BytesIO(shredded.content)
        return Image.open(shredded_image)

    def solve_pattern(self, image: Image.Image) -> dict[int, int]:
        """
        Solves the shred operation by using a shredded version of an image created by `generate_pattern`.

        @param image: An image created by `generate_pattern`

        @returns A mapping from block numbers in the original, unshredded image to their new positions (block numbers) in the shredded image.
        """
        counter = 0

        # Scrambled position to true position
        block_map = {}

        for x in range(0, image.size[0], self.block_x):
            for y in range(0, image.size[1], self.block_y):
                r, g, b = image.getpixel((x, y))
                block_map[counter] = self.rgb_to_counter(r, g, b)
                counter += 1

        # True position to scrambled position
        block_map2 = {}

        for k, v in block_map.items():
            block_map2[v] = k

        return block_map2

    def unscramble_image(self, image: Image.Image, block_map: dict[int, int]) -> Image.Image:
        """
        Apply the given block mapping from `solve_pattern` to a shredded image to reverse the shredding operation.

        @param image: Shredded image
        @param block_map: Block map from `solve_pattern`

        @returns The unshredded image.
        """
        counter = 0
        restored_image = image.copy()
        for x in range(0, image.size[0], self.block_x):
            for y in range(0, image.size[1], self.block_y):
                true_x, true_y = self.counter_to_xy(image, block_map[counter])
                segment = image.crop((true_x, true_y, true_x + self.block_x, true_y + self.block_y))
                restored_image.paste(segment, (x, y))
                counter += 1

        return restored_image


def main():
    parser = argparse.ArgumentParser(
        description="Solve script for Unicorn Shredder 2.0",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("flag", help="Path to shredded flag")
    parser.add_argument("--block-x", "-x", type=int, default=1, help="Block size (width) for shredded images.")
    parser.add_argument("--block-y", "-y", type=int, default=600, help="Block size (height) for shredded images.")
    parser.add_argument("--url", default="http://challs.crate.nu:41141", help="URL to challenge server.")

    args = parser.parse_args()

    flag = Image.open(args.flag)

    tk = Tk()
    display = ShredderSolver(tk, flag=flag, block_size=(args.block_x, args.block_y), url=args.url)
    tk.bind("<Return>", display.new_pattern)
    tk.bind("<Escape>", lambda _event: sys.exit(0))
    tk.mainloop()


if __name__ == "__main__":
    main()
