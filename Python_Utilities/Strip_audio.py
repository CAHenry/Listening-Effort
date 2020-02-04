from moviepy.editor import *
import os
import soundfile as sf

path = "D:\\Documents\\Docs\\Imperial\\Assets\\Videos\\bkb\\"
audio_path = "D:\\Documents\\Docs\\Imperial\\Assets\\BKB_Sentences\\"

for video in os.listdir(path):
    audio = AudioFileClip(path+video)
    audio_array = audio.to_soundarray(fps=44100)
    sf.write(os.path.join(audio_path, video), audio_array, 44100, subtype='PCM_24', format='WAV')
