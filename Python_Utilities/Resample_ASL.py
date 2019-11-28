import librosa
import soundfile as sf
import os

ASLQ_words = "C:\\Users\\craig\\Documents\\Listening-Effort\\Max"
old = "C:\\Users\\craig\\Documents\\Listening-Effort\\Max\\ASLQ_Matt"
for filename in os.listdir(old):
    y, s = librosa.load(os.path.join(old, filename), sr=44100)
    # librosa.output.write_wav(os.path.join(ASLQ_words, filename), y, 44100)
    sf.write(os.path.join(old, filename), y, 44100, subtype='PCM_24', format='WAV')
