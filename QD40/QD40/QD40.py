
import ffmpeg
import matplotlib.pyplot as plt
import numpy as np




def readfile(filename,height,width):

    # pipe the file into stdout using ffmpeg
    process = (ffmpeg
                .input(filename)
                .output('pipe:', format='rawvideo', pix_fmt='rgb24')
                .run_async(pipe_stdout = True)
              )

    # read from stdout into a numpy matrix, then add it to vframes
    vframes = list()
    while True:

        #read and check for EoF
        in_bytes = process.stdout.read(height*width*3)
        if not in_bytes:
            break

        #read in a frame
        vframe = np.frombuffer(in_bytes,np.uint8)
        vframe = vframe.reshape([height,width,3])
        
        # add the frame to the list
        vframes.append(vframe)
    
    print('OUT')

    return vframes

def test_vframes(vframes):

    for vframe in vframes:
        plt.imsave('frame.png',vframe)
        break

vframes = readfile('SimpsonsShot14.mov',720,960)
test_vframes(vframes)
print('COMPLETE')