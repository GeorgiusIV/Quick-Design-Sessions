


import pyaudio
import ffmpeg



def loadAudio(filename):
    
    CHUNK = 1024

    process = (ffmpeg
               .input(filename)
               .output('pipe:',format='s16le',acodec='pcm_s16le')
               .run_async(pipe_stdout = True))

    aframes = list()
    while True:
        in_bytes = process.stdout.read(CHUNK)
        if not in_bytes:
            break

        aframes.append(in_bytes)

    return aframes



def convertAudio(infile):
    pass


def playAudio(aframes):

    p = pyaudio.PyAudio()

    stream = (p.open(format=pyaudio.paInt16,
                     channels=2,
                     rate=48000,
                     output = True))

    for frame in aframes:
        stream.write(frame)

    stream.stop_stream()
    stream.close()

    p.terminate()


def main():
    aframes = loadAudio('SimpsonsShot14.mov')
    playAudio(aframes)

if __name__ == "__main__":
    main()







