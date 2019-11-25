import librosa
import soundfile as sf
import os
import numpy as np

ASLQ_words = "C:\\Users\\craig\\Documents\\Listening_effort\\Audio_App\\ASLQ"
old = "C:\\Users\\craig\\Documents\\Listening_effort\\Audio_App\\ASLQ_22050"
x, s = librosa.load("C:\\Users\\craig\\Documents\\Listening_effort\\Audio_App\\Masking\\Noise_1.wav")

len_samps = len(x)

for filename in os.listdir(old):
    y , s = librosa.load(os.path.join(old, filename), sr=44100)

    dif = len_samps - len(y)

    y = np.insert(y, 0, [0]*int(dif/2))
    y = np.append(y, [0]*int(dif/2))

    sf.write(os.path.join(ASLQ_words, filename), y, 44100, subtype='PCM_24', format='WAV')
