# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import webbrowser
import speech_recognition as sr
speech=sr.Recognizer()

def voice_to_text():
    voice_input=""
    with sr.Microphone() as source:
        speech.adjust_for_ambient_noise(source)
        try:
            
            audio=speech.listen(source)
            voice_input=speech.recognize_google(audio)
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            pass
        except sr.WaitTimeoutError:
            pass
    return voice_input

while True:
    print('Python is listning ...')
    inp = voice_to_text() 
           
    print(f'You just said {inp}.')
    
    if inp == "stop listening":
        print('Goodbye Prashant!')
        break
    elif "browser" in inp:
        inp = inp.replace('browser ' ,'')
        webbrowser.open("https://google.com/search?q="+inp)
        continue

