import librosa
import soundfile as sf
import os
import numpy as np

bkb_words = "C:\\Users\\craig\\Documents\\Listening-Effort\\Max\\BKB"
old = "C:\\Users\\craig\\Documents\\Listening-Effort\\Max\\BKB_Old"
max_len = 0
for filename in os.listdir(old):
    y, s = librosa.load(os.path.join(old, filename), sr=44100)
    if y.shape[0] > max_len:
        max_len = y.shape[0]

for filename in os.listdir(old):
    y, s = librosa.load(os.path.join(old, filename), sr=44100)
    padding_len = max_len - y.shape[0]
    padding = np.zeros(padding_len, dtype="float32")
    print(filename)
    y = np.concatenate((y, padding))
    sf.write(os.path.join(bkb_words, filename), y, 44100, subtype='PCM_24', format='WAV')