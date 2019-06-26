# Mp4-Generator

Audio only works with programs on my computer so the Simple branch removes it

Thinking about taking out tesseract OCR to fix frequent mistakes with one letter words
i.e. I was -> Iwas
This could also be fixed by image size issue I talk about later.

Sometimes there is a blip of noise at the end of a clip.
This could be frome the video clips being slightly shorter than the audio clip.

Annoying audio issue with transition clips.
This is most likely because of differing audio enconding codecs.
I am going to try and fix it by a new concatenation method ment for all types of files at the same time.
The documantation for this new method says it will re-encode files.

I need to add music over the whole video

Check out a 1080 formatting error I am getting in my new test images.
These images are way smaller than the old ones so this could cause it.
My math for formatting checks out as far as I can see. 
I think there is rounding somewhere that WAY more noticeable in smaller files.

Then I will need to polish the video as much as I can.

Then checkout Youtube API so it can post.
I will also need to make an account of course.

Also files and frames are being saved to directories so I can watch it work for debugging.
