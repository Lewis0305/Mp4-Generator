import moviepy.editor as mpe
import ffmpeg
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
    #os.system('ffmpeg -i blank_slate/sta.mp4 -c copy -bsf:v h264_mp4toannexb -f mpegts inter/0.ts')
    #vids += "|inter/0.ts"
    os.system('ffmpeg -i "concat:'+vids+'" -c copy -bsf:a aac_adtstoasc workspace/Done_mp4/'+str(ind)+'.mp4')


# stitch all mp4's togehter
# THIS IS NOW PROVEN TO BE WHERE THE AUDIO GLICH IS FROM
def final_concatenation(clips,ind):
    names = '' # Names of all input mp4
    clip = '' # Video and audio streams
    total = 0  # Total number of clips
    for n in clips:
        names += '-i workspace/Done_mp4/' + str(total + 1) + '.mp4 '
        names += '-i workspace/blank_slate/New.mp4 '
        clip += '[' + str(total) + ':v:0][' + str(total) + ':a:0]'
        clip += '[' + str(total+1) + ':v:0][' + str(total+1) + ':a:0]'
        total += 2
    os.system('ffmpeg ' + names + ' \
              -filter_complex "' + clip + 'concat=n=' + str(total) + ':v=1:a=1[outv][outa]" \
              -map "[outv]" -map "[outa]" workspace/video/' + str(ind+1) + '.mp4')

"""
def final_concatenation(clips,ind):
    vids = ""
    n=1
    #os.system('ffmpeg -i blank_slate/sta2.mp4 blank_slate/sta.mp4 -hide_banner')
    os.system('ffmpeg -i workspace/blank_slate/New.mp4 -c copy -bsf:v h264_mp4toannexb -f mpegts workspace/inter/0.ts')
    for i in clips:
        os.system('ffmpeg -i workspace/Done_mp4/'+str(n)+'.mp4 -c copy -bsf:v h264_mp4toannexb -f mpegts workspace/inter/'+str(n)+'.ts')
        if n > 1:
            #vids += "|"
            vids += "|workspace/inter/0.ts|"
        vids += "workspace/inter/"+str(n)+'.ts'
        n += 1
    print(vids)
    os.system('ffmpeg -i "concat:'+vids+'" -c copy -bsf:a aac_adtstoasc workspace/video/'+str(ind+1)+'.mp4')
    for i in range(len(clips)):
        os.remove(r'C:/Desk/Mp4Gen/workspace/Done_mp4' + '/' + str(i+1) + '.mp4')
"""