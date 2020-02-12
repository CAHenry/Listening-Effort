from moviepy.editor import *
import os
import soundfile as sf

path = "C:\\Users\\craig\\Documents\\Videos\\BKB\\"
audio_path = "C:\\Users\\craig\\Documents\\Listening-Effort\\Max\\BKB\\"

for video in os.listdir(path):
    audio = AudioFileClip(path+video)
    audio_array = audio.to_soundarray(fps=44100)
    video = os.path.splitext(video)[0]
    sf.write(os.path.join(audio_path, video + ".wav"), audio_array[:, 0], 44100, subtype='PCM_24', format='WAV')
