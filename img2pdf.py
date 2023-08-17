''' 
simple script converting images to pdf using pillow
DOCS: https://pillow.readthedocs.io/en/stable/index.html
'''
import os

from PIL import Image

# remember to use / instead of \
OPEN_PATH = " "
SAVE_PATH = " "

OUTPUT_FILENAME = ".pdf" # remember to include ".pdf" to filename

image_list = []
image_count = 0

for image in os.listdir(OPEN_PATH):
    image_path = os.path.join(OPEN_PATH, image)
    if os.path.isfile(image_path):
        try:
            im = Image.open(image_path)
            image_count += 1
            im = im.rotate(-90, expand=True)
            im = im.convert("RGB")
            image_list.append(im)
        except IOError:
            pass

im = image_list[0]
im.save(SAVE_PATH + OUTPUT_FILENAME, save_all=True, append_images=image_list[1::])

print(f"{image_count} images processed into PDF {SAVE_PATH}{OUTPUT_FILENAME}")