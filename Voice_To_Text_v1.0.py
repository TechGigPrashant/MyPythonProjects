# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import speech_recognition as sr

speech=sr.Recognizer()

print('Python is listning ...')

with sr.Microphone() as source:
    speech.adjust_for_ambient_noise(source)
    audio=speech.listen(source)
    inp=speech.recognize_google(audio)

print(f'You just said {inp}.')

