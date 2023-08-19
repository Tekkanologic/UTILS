''' iterates through folder, renaming files by enumeration (Image x .png) '''

import os

PATH = " "

for i, file in enumerate(os.listdir(PATH)):
    new_name = "Image" + str(i) + ".png"
    os.rename(os.path.join(PATH, file), os.path.join(PATH, new_name))

print("Rename complete!")