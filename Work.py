import os

#dirc = input('Enter video:   ')
dirc = 'test'
folder = 'C:\\Users\\Sam\\Box Sync\\V\\Out\\'+str(dirc)
items = os.listdir(folder)
images = []
for names in items:
        if names.endswith('.PNG') and not names in images:
                images.append(names)
images = images[1:]

from PIL import Image
import numpy as np

print(images)
i = 1
for title in images:


## Creates list of the bottom of text blocks in all images but title ##
        image = Image.open(folder+'\\'+str(title))
        image_array = np.asarray(image)
        prev_wht = 0
        y_pixel = 0
        wht_bttms = []
        red_dots = []
        for y in image_array:
                current_wht = 0
                x_pixel = 0
                for xy in y:
                        if np.array_equal(xy, [215, 218, 220, 255]):
                                current_wht = 1
                        if np.array_equal(xy, [255, 0, 0, 255]):
                                red_dots.append([x_pixel+1,y_pixel])
                        x_pixel += 1
                if current_wht == 0 and prev_wht == 1:
                        wht_bttms.append(y_pixel)
                y_pixel += 1
                prev_wht = current_wht



        for dot in red_dots:
                for n in range(3):
                        for j in range(4):
                                image.putpixel((dot[0]+n-2,dot[1]+j-2), (26 ,26 ,27))

        image.save('C:\\Users\\Sam\\Box Sync\\V\\Out\\'+str(dirc)+'\\'+str(i)+'.png')



        i += 1