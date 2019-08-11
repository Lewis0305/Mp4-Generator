import os

#dirc = input('Enter video:   ')
dirc = 'Dream'
folder = 'C:\\Users\\Sam\\Box Sync\\V\\Out\\'+str(dirc)
items = os.listdir(folder)
images = []
for names in items:
    if names.endswith('.PNG') and not names in images:
        images.append(names)
images = images[1:]

from PIL import Image
import numpy as np

i = 1
for title in images:
    image = Image.open(folder+'\\'+str(title))
    image_array = np.asarray(image)
    prev_wht = 0
    for y in image_array:
        current_wht = 0
        for xy in y:
            if np.array_equal(xy, [215, 218, 220, 255]):
                current_wht = 1
                break



    i += 1