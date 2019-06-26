import frameMakerLib as frame
import audioMakerLib as audio
import videoMakerLib as video
import MakerLib as make

done = frame.read_direct('workspace/Done_mp4','.mp4')
vids = frame.read_direct('workspace/video','.mp4')
video.final_concatenation(done,len(vids))
print("Done")