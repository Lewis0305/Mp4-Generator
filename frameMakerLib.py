from PIL import Image
import numpy as np
import pytesseract as tes
import pyautogui as gu
import argparse
import cv2 as cv
import os


# Reads the contents of the directory specified as string
# directory equals None will read current
def read_direct(directory, *args): # Args are also strings ie. '.png'
    items = os.listdir(directory)
    newlist = []
    if len(args) == 0:
        return items
    for arg in args:
        for names in items:
            if names.endswith(arg) and not names in newlist:
                newlist.append(names)
    return newlist
    # Returns array of file names with . endswitch


# Looks at an image and says where the text is
def white_black_INFO(A,data):
    i,black,whiteline = 0,1,0
    for a in A:
        j = 0
        black2 = black
        black = 1
        if whiteline > 0:
            whiteline += 1
        for n in a:
            if np.array_equal(n, [215, 218, 220, 255]): # That is the RGBT value for the background color
                black = 0
                if whiteline== 0:
                    whiteline = 1
                elif whiteline == 5:
                    whiteline = -1
                    data[0] = j
            j += 1
        if black == 1 and black2 == 0:
            data[1].append([i])
            data[2][-1].append(i)
        if black == 0 and black2 == 1:
            data[1][-1].append(i)
            data[2].append([i])
        i += 1
    data[1][-1].append(i)


# Edits the image based on text location so it has less errors in OCR
def make_read(A, read, data):
    i=0
    for yaxe in A:
        j=0
        if (i<data[2][0][0] or i>data[2][-1][1]):

            for xaxe in yaxe:
                read.putpixel((j,i), (26, 26, 27))
                j+=1
        else:
            j=0
            for xaxe in yaxe:
                read.putpixel((j,i), (26, 26, 27))
                if j > data[0]-25:
                    break
                j+=1
        i+=1     
    read.save('Read.png')


# Read the photo and return the text
# I get a lot of red lines under my cv. here but it is right and works
def read_photo():
    imager = cv.imread("Read.png")
    gray = cv.cvtColor(imager, cv.COLOR_BGR2GRAY)
    filename = "{}.png".format(os.getpid())
    cv.imwrite(filename, gray)
    text = tes.image_to_string(Image.open(filename))
    os.remove(filename)
    return text


# Break the text into sentences and find locations
def punc_mark(white_list):
    co_points = []
    imager = cv.imread("Read.png")
    y,x,_ = imager.shape
    boxes = tes.image_to_boxes(imager) # also include any config options you use
    letters = []
    breaks = [',','.','?','!']
    for b in boxes.splitlines():
        b = b.split(' ')
        letters.append(b)
    for letter in letters:
        if letter[0] in breaks:
            co_points.append([(int(letter[1])+5), y-(int(letter[2])+13)])
    return organize_point(co_points, white_list)



def organize_point(co_points, white_list):
    organ_point = []
    for point in co_points:
        level = 0
        for white in white_list:
            if point[1] >= white[0] and point[1] <= white[1]:
                organ_point.append([point[0], level])
                break
            level+=1
    return organ_point


# Make each frame state
def paint_frame(A, points, data, image_name):
    index_name = 1
    for point in points:
        if point == points[-1]:
            break
        i=0
        temp_image = Image.open(image_name)
        for yaxe in A:
            j=0
            if i > data[2][point[1]][0]-2 and i < data[2][point[1]][1]:
                for xaxe in yaxe:
                    if j > point[0]:
                        temp_image.putpixel((j,i), (26, 26, 27))
                    j+=1
            elif i >= data[2][point[1]][1]:
                for xaxe in yaxe:
                    if j > data[0]-10:
                        temp_image.putpixel((j,i), (26, 26, 27))
                    j+=1
            i+=1
        temp_image.save('workspace/frames/' + 'testImage' + zeros(index_name) + str(index_name) + '.png')
        index_name += 1
    main_image = Image.open(image_name)
    main_image.save('workspace/frames/'  + 'testImage' + zeros(index_name) + str(index_name) + '.png')


# Return the number of zeros that it needs
def zeros(index_name):
    if len(str(index_name)) == 1:
        return '000'
    elif len(str(index_name)) == 2:
        return '00'
    elif len(str(index_name)) == 3:
        return '0'
    elif len(str(index_name)) == 4:
        return ''


# Delete frames of image state
def delete_state_frames(length):
    for i in range(length):
        os.remove(r'C:/Desk/Mp4Gen/workspace/frames' + '/' + 'testImage' + zeros(length) + str(i+1) + '.png')


# Delete temp frames
def delete_temp_frames(length):
    for i in range(length):
        os.remove(r'C:/Desk/Mp4Gen/workspace/frames_temp' + '/' + zeros(i+1) + str(i+1) + '.png')

    
# Make temp png frame
def make_temp(length, tempim2):
    for i in range(length):
        tempim2.save('workspace/frames_temp/' + zeros(i+1) + str(i+1) + '.png')


# Format image to 1080p ready
def image_format_1080(image, npArr):
    y,x,_ = npArr.shape
    y_test = round((x/16)*9)
    if( y_test > y):
        x_temp = x+(1920-x)
        y_temp = round(y+  (((1920-x)/16)*9)  )
        end = image.resize((x_temp, y_temp))
        #end.save('end.png')
    elif( y_test < y):
        y_temp = y+(1080-y)
        x_temp = round(x+  (((1080-y)/16)*9)  )
        end = image.resize((x_temp, y_temp))
        #end.save('end.png')
    else:
        x_temp = 1920
        y_temp = 1080
        end = image.resize((x+ (1920-x), y+ (1080-y)))
        #end.save('end.png')
    return end


# Insert formatted image into the 1080p image correctly
def insert_image(end,image):
    x_temp,y_temp = end.size
    ten80 = Image.open('workspace/blank_slate/1080grey.jpg')
    tempim = ten80.copy()
    if(y_temp==1080):
        tempim.paste(end, (int((1920-x_temp)/2),0))
    elif(x_temp==1920):
        tempim.paste(end, (0,int((1080-y_temp)/2)))
    tempim.save(image.filename)