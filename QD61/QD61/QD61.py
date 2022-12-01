

import ffmpeg



def readfile(filename):

    height,width = 720,960
    sample_rate = 48000
    audio_perframe = 2000

    a_stream = (ffmpeg
                .input(filename, format='s16le')
                .output('pipe:')
                .run_async(pipe_stdout=True))

    
    v_stream = (ffmpeg
                .input(filename, format='rawvideo', pix_fmt='rgb24')
                .output('pipe:')
                .run_async(pipe_stdout=True))

    
    while True:

        a_bytes = a_stream.stdout.read(audio_perframe)
        v_bytes = v_stream.stdout.read(height*width*3)

        if not a_bytes and not v_bytes:
            break

    return a_bytes,v_bytes


def savefile(filename,audio,video):

    height,width = 720,960
    filetype = filename[-4]
    
    a_stream = (ffmpeg
                .input('pipe:',format='s16le')
                .output(filename)
                .run_async(pipe_stdin=True))

    a_stream.stdin.write(audio)

    v_stream = (ffmpeg
                .input('pipe:',format='rawvideo', pix_fmt='rgb24', s='{}x{}'.format(width,height))
                .output(filename)
                .run_async(pipe_stdin=True))

    v_stream.stdin.write(video)
    
    saving = ffmpeg.input('pipe:',format='s16le')
    saving.run_async(pipe_stdin=True)
    saving.stdin.write(audio)
    saving.input('pipe:',format='rawvideo', pix_fmt='rgb24', s='{}x{}'.format(width,height))
    saving.stdin.write(video)
    
    saving = (ffmpeg
              .concat(a_stream,v_stream)
              .output(a_stream,v_stream,filename, pix_fmt='yuv420p')
              .run())

    saving.communicate()
    

def main():
    filename = 'SimpsonsShot14.mov'
    audio,video = readfile(filename)
    savefile('TEST.mov',audio,video)

main()


