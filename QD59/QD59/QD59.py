


import ffmpeg
import numpy as np


def read(filename):

    samplerate = 48000
    n_channels = 2

    process = (ffmpeg
           .input(filename)
           .output('pipe:', format='s16le')
           .run_async(pipe_stdout = True))

    while True:
        in_bytes = process.stdout.read(samplerate)
        if not in_bytes:
            break

        waveform = np.frombuffer(in_bytes, dtype=np.int16).reshape(-1,n_channels)
        #waveform = waveform.tobytes()

    print(waveform)

def main():
    read('SimpsonsShot14.mov')

main()