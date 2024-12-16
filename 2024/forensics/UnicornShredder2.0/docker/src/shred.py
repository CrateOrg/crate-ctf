import sys
import json
import os
import random
import string
from datetime import datetime
from PIL import Image

result = {
}

def resize_image(img):
    width, height = img.size
    new_width = (width // 30) * 30
    new_height = (height // 30) * 30
    return img.resize((new_width, new_height))

def shred_image(img, algo):
    width, height = img.size
    if algo == "scissor-friendly":
        img = resize_image(img)
        width, height = img.size # changed after resize
        rect_width = 30
        rect_height = 30
    elif algo == "ultra-secure":
        rect_width = 1
        rect_height = height
    rects = []

    # Divide the image into rectangles
    for i in range(0, width, rect_width):
        for j in range(0, height, rect_height):
            rect = img.crop((i, j, i + rect_width, j + rect_height))
            rects.append(rect)

    # Randomize the rects, defense grade randomization
    random.seed(random.randint(93784539, 93784549))
    random.shuffle(rects)

    # Create a new blank image
    shredded_img = Image.new("RGB", (width, height))

    # Paste the randomized rects into the new image
    idx = 0
    for i in range(0, width, rect_width):
        for j in range(0, height, rect_height):
            shredded_img.paste(rects[idx], (i, j))
            idx += 1

    return shredded_img

def main():
    if len(sys.argv) != 3:
        result["error"] = "shredder stuck, contact devs"
        print(json.dumps(result, indent=4))
        sys.exit(2)

    algo = sys.argv[1]
    input_file = sys.argv[2]

    try:
        img = Image.open(input_file)
        fmt = img.format
        if not fmt.lower() in ["gif", "jpg", "jpeg", "png"]:
            raise Exception()
    except Exception as e:
        result["error"] = "file not shreddable"
        print(json.dumps(result, indent=4))
        sys.exit(1)
    try:
        shredded_img = shred_image(img, algo)
        random.seed(datetime.now().timestamp())
        randomname = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(32))
        outfilename = f"/var/www/html/shreds/{randomname}.{fmt.lower()}"
        shredded_img.save(outfilename, format=fmt)
        result["output"] = "shreds/" + outfilename.split("/")[-1]
        print(json.dumps(result, indent=4))
    except Exception as e:
        result["error"] = "unexpected error, contact devs"
        print(json.dumps(result, indent=4))
        sys.exit(1)

if __name__ == "__main__":
    main()
