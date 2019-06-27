import frameMakerLib as frame
import audioMakerLib as audio
import videoMakerLib as video
import MakerLib as make

lis = frame.read_direct('workspace/png','.PNG')
audio.check_ball()
for i in range(len(lis)):
    make.make_vid_clip('workspace/png/'+lis[i],i+1)

done = frame.read_direct('workspace/Done_mp4','.mp4')
vids = frame.read_direct('workspace/video','.mp4')
video.final_concatenation(done,len(vids))
#video.delete_temp_ts(len(done))
print("Done")