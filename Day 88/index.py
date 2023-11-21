# shoutout to everybody exercise.
# solution of exercise.

import pyttsx3


def pronounce_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    text_to_pronounce = "shoutout to everybody"
    pronounce_text(text_to_pronounce)
