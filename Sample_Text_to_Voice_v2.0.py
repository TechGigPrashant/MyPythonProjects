# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 23:05:12 2023

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 22:58:51 2023

@author: user
"""

import pyttsx3

engine = pyttsx3.init()

while True:
    inp=input("What what do you want to convert to Speech ? \n")
    if inp== "done":
        print(f"You just typed in {inp}; goodbye !")
        engine.say(f"You just typed in {inp}; goodbye !")
        engine.runAndWait()
        break
    else:
        print(f"You just typed in {inp}")
        engine.say(f"You just typed in {inp};")
        engine.runAndWait()
        continue
