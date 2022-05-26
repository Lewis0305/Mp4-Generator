from PIL import Image
import frameMakerLib as frame
import audioMakerLib as audio
import videoMakerLib as video
import numpy as np
import time
import re

# string for name, int of clip
def make_vid_clip(image_name, clip):
    # [ start, listBlack, listWhite ]
    photo_read_data = [0, [[0]], []]
    image = Image.open(image_name)
    read = Image.open(image_name)
    A = np.asarray(image)
    frame.white_black_INFO(A, photo_read_data)  # Find writing
    frame.make_read(A, read, photo_read_data)  # Make blank writing for OCR
    text = frame.read_photo() # Read file
    points = frame.punc_mark(photo_read_data[2]) # Look for sentences
    frame.paint_frame(A, points, photo_read_data, image_name) # Make and save all frames
    words = re.split('[,.?!]', text) # Split text into sentences
    del words[-1]

    words = audio.page_text_clean(words) # Clean the sentences of newlines
    audio.make_audio(words)
    durations = audio.find_durations(words)
    direc = frame.read_direct('workspace/frames', '.png')
    index = 1
    for dire in direc:
        frames = durations[index-1]
        tempim = Image.open('workspace/frames/' + dire) # open image
        # re-format frames into 16:9 1080p
        frame.insert_image(frame.image_format_1080(tempim, A), tempim)
        tempim2 = Image.open('workspace/frames/' + dire)
        frame.make_temp(frames, tempim2)
        #for i in range(frames):
        #    tempim2.save('frames_temp/' + str(i+1) + '.png')
        video.frames_to_vid(index)
        frame.delete_temp_frames(frames)
        video.mp4_plus_wav(index)
        index += 1
    mp = frame.read_direct('workspace/mp4', '.mp4')
    video.mp4_concatenation(mp, clip)

    audio.delete_audio(len(words))
    frame.delete_state_frames(len(points))
    video.delete_temp_mp4s(len(points))
