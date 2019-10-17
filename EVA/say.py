from gtts import gTTS
import os

def main(message, lang):
    tts = gTTS(message, lang)
    tts.save("say.mp3")
    os.system("mpg123 -q say.mp3")

def English(message):
    main(message, "en")

def Spanish(message):
    main(message, "es")