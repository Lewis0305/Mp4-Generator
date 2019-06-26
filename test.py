import frameMakerLib as frame
import audioMakerLib as audio
import videoMakerLib as video
import ffmpeg
import os
from moviepy.editor import VideoFileClip, concatenate_videoclips
import moviepy.editor


def final_concatenation(clips,ind):
    num = 1
    videos = []
    for n in clips:
        temp_clip = VideoFileClip("workspace/Done_mp4/" + str(num) + ".mp4")
        if(num%2==0):
            temp_tran = VideoFileClip("workspace/blank_slate/New.mp4")
        else:
            temp_tran = VideoFileClip("workspace/blank_slate/sta2.mp4")
        videos.append(temp_clip)
        videos.append(temp_tran)
        num += 1
    final_clip = concatenate_videoclips(videos)
    final_clip.write_videofile("workspace/video/" + str(ind+1) + ".mp4")

done = frame.read_direct('workspace/Done_mp4','.mp4')
vids = frame.read_direct('workspace/video','.mp4')
final_concatenation(done,len(vids))
print("Done")