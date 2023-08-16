import os

from PIL import Image

from pi_heif import register_heif_opener

register_heif_opener()

OPEN_PATH = " "
SAVE_PATH = " "

image_count = 0

for item in os.listdir(OPEN_PATH):
    item_path = os.path.join(OPEN_PATH, item)
    if os.path.isfile(item_path):
        try:
            im = Image.open(item_path)
            image_count += 1
            im.save(SAVE_PATH + f"{image_count}" + ".jpeg", "JPEG")
        except IOError:
            pass

print(f"{image_count} images processed to {SAVE_PATH}")