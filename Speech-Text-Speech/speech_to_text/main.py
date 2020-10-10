import speech_recognition as sr
import pyaudio
import os

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say Something to begin")
    audio = r.listen(source)
    voice_data = r.recognize_google(audio)
    print(voice_data)