# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import speech_recognition as sr
speech=sr.Recognizer()

while True:
    print('Python is listning ...')
    inp=""
    with sr.Microphone() as source:
        speech.adjust_for_ambient_noise(source)
        try:
            
            audio=speech.listen(source)
            inp=speech.recognize_google(audio)
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            pass
        except sr.WaitTimeoutError:
            pass
        
    print(f'You just said {inp}.')
    if inp == "stop listening":
        print('Goodbye Prashant!')
        break

