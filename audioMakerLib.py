import pyautogui as gu
import contextlib
import time
import wave
import os


# Checks to make sure the audio program is open
def check_ball():
    while True:
        find2 = gu.locateOnScreen('workspace/blank_slate/Ball_head.PNG')
        find = gu.locateOnScreen('workspace/blank_slate/Arrow.PNG')
        if find !=None and find2 != None:
            break
    # Opens window
    gu.click(find2[0],find2[1])
    gu.click(find2[0],find2[1])
    # Select voice
    gu.click(find[0]+7,find[1]+7)
    time.sleep(.3)
    gu.click(find[0],find[1]+117)
    # Prepare to type
    gu.click(find2[0]+30,find2[1]+800)


# Takes in array of strings and cleans each one
def page_text_clean(words):
    if len(words[0]) == 1:
        words = text_clean(words)
    else:
        for i in range(len(words)):
            words[i] = text_clean(words[i])
    return words


# The cleaning of the strings
def text_clean(text):
    text = repr(text)
    # text = text[1:-1] // streamlined in next line
    # not sure if that syntax works
    return text[1:-1].replace(r"\n"," ")


# Generates .wav files from text
def text_to_audio(text, index):
    # Deletes all old text
    gu.hotkey('ctrl', 'A')
    gu.typewrite(['backspace'])
    # New message
    gu.typewrite(text)
    time.sleep(.3)
    # Saves .wav file
    gu.hotkey('Ctrl', 'w')
    gu.typewrite(r'C:\Desk\Mp4Gen\workspace\audio' + '\\' + index + '.wav')
    gu.typewrite(['enter'])
    time.sleep(2)


# Finds number of video frames from all audio files audio frames
def find_durations(text):
    times = []
    for i in range(len(text)):
        times.append(get_duration('workspace/audio/' + str(i+1) + '.wav'))
    return times


# Finds number of video frames from audio file frames
def get_duration(file_name):
    with contextlib.closing(wave.open(file_name,'r')) as f:
        # These say there is an error on both of the f. but I am 
        # using it right and they are working (red lines)
        duration = f.getnframes() / float(f.getframerate())
        return round(duration * 30)+5


# Loops over all the text to make audio for
def make_audio(text):
    for i in range(len(text)):
        text_to_audio(text[i], str(i+1))


# Deletes all audio files
def delete_audio(length):
    for i in range(length):
        os.remove(r'C:\Desk\Mp4Gen\workspace\audio' + '\\' + str(i+1) + '.wav')