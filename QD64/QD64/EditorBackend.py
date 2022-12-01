
import numpy as np
import cv2
import ffmpeg

def loadFile(filename):
    '''
    reads 'filename' from the current directory in as audio and video buffers
    then converts each into two numpy arrays and returns them

    attributes:
        height -- int
        width -- int
        samplerate -- int
        perframe -- int

        aframes -- list
        vframes -- list
        astream -- ffmpeg stream
        vstream -- ffmpeg stream
        abytes -- bytes
        vbytes -- bytes
        aframe -- numpy array
        vframe -- numpy array
    '''

    height,width = 720,960
    samplerate = 48000
    perframe = samplerate//24
    nbytes = 2
    nchannels = 2

    # create byte streams for the audio and video from filename
    astream = (ffmpeg
              .input(filename)
              .output('pipe:', format='s16le')
              .run_async(pipe_stdout=True))

    vstream = (ffmpeg
              .input(filename)
              .output('pipe:', format='rawvideo', pix_fmt='rgb24')
              .run_async(pipe_stdout=True))

    # initialise aframes and vframes
    aframes = list()
    vframes = list()

    while True:
        # read the right number of bytes from astream and vstream
        abytes = astream.stdout.read(perframe*nbytes*nchannels)
        vbytes = vstream.stdout.read(height*width*3)

        # if there are no bytes left, exit
        if not abytes and not vbytes:
            break

        # if there are bytes, read them into a numpy array
        if abytes:
            aframe = np.frombuffer(abytes,np.int16).reshape([-1,nchannels])
        if vbytes:
            vframe = np.frombuffer(vbytes,np.uint8).reshape([height,width,3])

        # append the matrices to aframes and vframes
        aframes.append(aframe)
        vframes.append(vframe)

    return aframes, vframes

def saveFile(filename,fmt,height,width):
    '''
    reads two numpy arrays, one for audio and one for video
    then compiles both into a single file called 'filename' with format fmt

    '''
    pass


def getEmptyFrame(height,width):

    return np.zeros([height,width,3])


class Audio():
    def __init__(self):
        pass

    def setaframes(self,aframes):
        self.aframes = aframes
        self.nchannels = 2
        self.framewidth = len(aframes[0])
        self.nframes = len(aframes)
        self.LChannel = np.concatenate([aframe[0] for aframe in self.aframes])
        self.RChannel = np.concatenate([aframe[1] for aframe in self.aframes])
        self.nsamples = self.nframes*self.framewidth



class Video():
    def __init__(self):
        pass

    def setvframes(self,vframes):
        self.vframes = vframes






