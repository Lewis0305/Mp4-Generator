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


################################ Paint ################################
        for dot in red_dots:
                for n in range(3):
                        for j in range(4):
                                image.putpixel((dot[0]+n-2,dot[1]+j-2), (26 ,26 ,27))



        image.save('C:\\Users\\Sam\\Box Sync\\V\\Out\\'+str(dirc)+'\\'+str(i+1)+'-0.png')
        name = 1
        for dot in red_dots:
                if [dot[0]-1, dot[1]-1] not in red_dots and \
                   [dot[0], dot[1]-1] not in red_dots and \
                   [dot[0]+1, dot[1]-1] not in red_dots:
                        temp = image
                        floor = 0
                        for bot in wht_bttms:
                                if dot[1] < bot:
                                        floor = bot
                                        break
                        
                        
                        
                        
                        y_paint = 0
                        print(floor)
                        for y in image_array:
                                x_paint = 0
                                for xy in image_array:
                                        if y_paint > floor+3:
                                                temp.putpixel((x_paint,y_paint), (26 ,26 ,27))
                                        if y_paint > dot[1] and x_paint > dot[0]:
                                                temp.putpixel((x_paint,y_paint), (26 ,26 ,27))
                                        x_paint += 1
                                y_paint += 1
                        temp.save('C:\\Users\\Sam\\Box Sync\\V\\Out\\'+str(dirc)+'\\'+str(i+1)+'-'+str(name)+'.png')
                        name += 1
        



        


        #image.save('C:\\Users\\Sam\\Box Sync\\V\\Out\\'+str(dirc)+'\\'+str(i)+'-1.png')



        i += 1