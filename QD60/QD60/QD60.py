
import ffmpeg
import numpy as np
import pyaudio



def readfile(filename):

    n_channels = 2
    height,width = 720,960

    # convert data from an arbitrary format to s16le audio data
    a_pipe = (ffmpeg
               .input(filename)
               .output('pipe:', format='s16le')
               .run_async(pipe_stdout=True)
              )

    # convert data from an arbitrary format to rgb24 video data
    v_pipe =  (ffmpeg
               .input(filename)
               .output('pipe:', format='rawvideo',pix_fmt='rgb24')
               .run_async(pipe_stdout=True)
              )

    # read audio and video data into lists to return
    aframes = list()
    vframes = list()
    while True:
        # read the audio data from stdout
        a_bytes = a_pipe.stdout.read()
        v_bytes = v_pipe.stdout.read(height*width*3)

        # upon running out of data, exit
        if not a_bytes and not v_bytes:
            break

        # convert audio bytes to a list of audio samples
        if a_bytes:
            a_frame = np.frombuffer(a_bytes,np.int16).reshape(-1,n_channels)
            aframes.append(a_frame)

        # convert video bytes to a list of video frames
        if v_bytes:
            vframe = np.frombuffer(v_bytes,np.uint8).reshape(height,width,3)
            vframes.append(vframe)

    return aframes,vframes


def playfile(aframes):

    # instantiate pyaudio
    p = pyaudio.PyAudio()

    # create the stream to play
    stream = p.open(format=pyaudio.paInt16,
                    channels = 2,
                    rate = 48000,
                    output = True)

    # play the audio
    for aframe in aframes:
        a_bytes = aframe.tobytes()
        stream.write(a_bytes)

    # close the audio stream
    stream.stop_stream()
    stream.close()

    # exit pyaudio
    p.terminate()


def main():
    aframes,vframes = readfile('SimpsonsShot14.mov')
    playfile(aframes)

main()