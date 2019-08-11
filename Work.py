import os
#dirc = input('Enter video:   ')
dirc = 'Dream'
items = os.listdir('C:\\Users\\Sam\\Box Sync\\V\\Out\\'+str(dirc))
images = []
for names in items:
    if names.endswith('.PNG') and not names in images:
        images.append(names)

print(images)