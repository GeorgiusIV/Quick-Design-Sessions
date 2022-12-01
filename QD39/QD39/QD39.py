
import ffmpeg
import numpy as np
import cv2 as cv

process = (ffmpeg
           .input('SimpsonsShot14.mov')
           .output('pipe:',format='rawvideo', pix_fmt='rgb24')
           .run_async(pipe_stdout=True, pipe_stderr=True))

height, width = 720,960
#print(process.communicate())
vframes = list()
while True:
    RGB_matrix = np.frombuffer(process.stdout.read(height*width*3), np.uint8)
    RGB_matrix.reshape([height,width,3])
    vframes.append(RGB_matrix)
    if RGB_matrix.all()==0:
        break
    


print(RGB_matrix)

cv.imshow('name',vframes[0])
cv.waitKey(0)