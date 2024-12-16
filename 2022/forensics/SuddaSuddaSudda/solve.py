#!/usr/bin/env python3
import string

from PIL import Image, ImageDraw, ImageFont, ImageChops, ImageFilter
import numpy as np

FLAG_LENGTH = 19
FLAG_COORDS = (90, 280, 660, 322)

img = Image.open("card.png")
font = ImageFont.truetype("LiberationMono-Regular.ttf", size=50)
segment_image = img.crop(FLAG_COORDS)

guess = ["1"] * FLAG_LENGTH
old_guess = None

while guess != old_guess: # Exit if no change was made to the guess
    old_guess = guess.copy()

    for index, _ in enumerate(guess):
        guesses = {}

        for guess_char in string.digits + " ":
            new_guess = guess.copy()
            new_guess[index] = guess_char

            base_img = Image.open("card_blank.png")
            draw = ImageDraw.Draw(base_img)
            draw.text((FLAG_COORDS[0], FLAG_COORDS[1]), "".join(new_guess), font=font, fill="white")

            test_segment = base_img.crop(FLAG_COORDS)
            test_segment = test_segment.filter(ImageFilter.BoxBlur(radius=20))

            diff = ImageChops.difference(segment_image, test_segment)
            arr = np.asarray(diff)
            guesses[guess_char] = arr.sum()

        best_char, diff = sorted(guesses.items(), key=lambda x: x[1])[0][0:2]
        guess[index] = best_char
        print(f"{''.join(guess)}\t{diff=: >10}", end="\r")

        if diff == 0:
            break

print()
