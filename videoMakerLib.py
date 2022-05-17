from moviepy.editor import VideoFileClip, concatenate_videoclips
import moviepy.editor
import ffmpeg
import time
import os


# Clears all mp4s and .ts files
def delete_temp_mp4s(length):
    for i in range(length):
        os.remove(r'C:/Desk/Mp4Gen/workspace/mp4' + '/' + str(i+1) + '.mp4')
        os.remove(r'C:/Desk/Mp4Gen/workspace/mp4_temp' + '/' + str(i+1) + '.mp4')
        os.remove(r'C:/Desk/Mp4Gen/workspace/inter' + '/' + str(i+1) + '.ts')


# Deletes only .ts files
def delete_temp_ts(length):
    for i in range(length+1):
        os.remove(r'C:/Desk/Mp4Gen/workspace/inter' + '/' + str(i) + '.ts')


# turn frames into mp4
def frames_to_vid(ind):
    os.system('ffmpeg -r 30 -f image2 -s 1920x1080 -i workspace/frames_temp/%04d.png -vcodec libx264 -crf 25  -pix_fmt yuv420p workspace/mp4_temp/'+str(ind)+'.mp4')


# stitch wav to mp4
def mp4_plus_wav(ind):
    os.system('ffmpeg -i workspace/mp4_temp/'+str(ind)+'.mp4 -i workspace/audio/'+str(ind)+'.wav -c:v copy -shortest -map 0:v:0 -map 1:a:0 -c:a aac -b:a 192k workspace/mp4/'+str(ind)+'.mp4')


# Stitch all of these states into a temp mp4
def mp4_concatenation(clips, ind): # directory
    vids = ""
    n=1
    for i in clips:
        os.system('ffmpeg -i workspace/mp4/'+str(n)+'.mp4 -c copy -bsf:v h264_mp4toannexb -f mpegts workspace/inter/'+str(n)+'.ts')
        if n > 1:
            vids += "|"
        vids += "workspace/inter/"+str(n)+'.ts'
        n += 1
    #os.system('ffmpeg -i testing_space/sta.mp4 -c copy -bsf:v h264_mp4toannexb -f mpegts inter/0.ts')
    #vids += "|inter/0.ts"
    os.system('ffmpeg -i "concat:'+vids+'" -c copy -bsf:a aac_adtstoasc workspace/Done_mp4/'+str(ind)+'.mp4')


# stitch all mp4's togehter
def final_concatenation(clips,ind):
    num = 1
    videos = []
    for n in clips:
        temp_clip = VideoFileClip("workspace/Done_mp4/" + str(num) + ".mp4")
        if(num%2==0):
            temp_tran = VideoFileClip("workspace/testing_space/New.mp4")
        else:
            temp_tran = VideoFileClip("workspace/testing_space/sta2.mp4")
        videos.append(temp_clip)
        videos.append(temp_tran)
        num += 1
    final_clip = concatenate_videoclips(videos)
    final_clip.write_videofile("workspace/video/" + str(ind+1) + ".mp4")
    time.sleep(3)
    for i in range(len(clips)):
        os.remove(r'C:/Desk/Mp4Gen/workspace/Done_mp4' + '/' + str(i+1) + '.mp4') 