import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write
import speech_recognition as sr

fr = 44100 #frequency
seconds = 10
print("the recording has started")
data = sd.rec(int(seconds * fr), samplerate = fr, channels = 2)
sd.wait()
y = (np.iinfo(np.int32).max * (data/np.abs(data).max())).astype(np.int32)

print("finished recording")
write("out.wav",fr,y)


r = sr.Recognizer()
sound = sr.AudioFile('out.wav')
with sound as source:
    audio = r.record(source)
text = r.recognize_google(audio)
print(text)
