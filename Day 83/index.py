"""
Exercise : Write a program to pronounce list of names using win32 API. If you give a list as follows.

list = ["jaymin", "deep", "jeel"]

The program will pronounce :
    Shoutout to jaymin
    Shoutout to deep
    Shoutout to jeel
"""

# code 

import pyttsx3

def pronounce_names(name_list):
    engine = pyttsx3.init()

    for name in name_list:
        shoutout = f"Shoutout to {name}"
        print(shoutout)
        engine.say(shoutout)
        engine.runAndWait()

if __name__ == "__main__":
    name_list = ["jaymin", "deep", "jeel"]
    pronounce_names(name_list)

