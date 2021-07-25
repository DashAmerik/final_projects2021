import speech_recognition as sr
r = sr.Recognizer()
sound = sr.AudioFile('sentance_1.wav')
with sound as source:
    audio = r.record(source)
text = r.recognize_bing(audio)
print(text)
