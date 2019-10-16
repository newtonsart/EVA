import speech_recognition as sr
import goslate
from gtts import gTTS
import os

def say(message, lang):
    tts = gTTS(message, lang)
    tts.save("say.mp3")
    os.system("mpg123 -q say.mp3")

def change_language(language):
    if language == "Spanish":
            lang = "es"
            say("Idioma cambiado al Español", lang)
    
    elif language == "inglés":
            lang = "en"
            say("Language changed to English", lang)
    
    else:say("Language not found", lang)
    
    return lang

def translate(message):
    gs = goslate.Goslate()

    return gs.translate(message, lang)


def get_speech(source):
    r.adjust_for_ambient_noise(source)
        
    print("I'm listening.")
    
    audio = r.listen(source)
    
    print("Recognizing")
    
    try:
        speech = r.recognize_google(audio, language = lang)
    except sr.UnknownValueError:pass
    try:
        return speech
    except UnboundLocalError:
        return "???"

    


def run():

    with mic as source:
        global lang

        speech = get_speech(source)
        speech_divided = speech.split()

        mode = speech_divided[0]

        try:

            if mode == change_commands[lang]:
                lang=change_language(speech_divided[2])

        except IndexError: pass
        except UnboundLocalError: pass

        try:

            if mode == exit_commands[lang]:
                if lang == "en":
                    say("Goodbye Arthur",lang)

                elif lang == "es":
                    say("Adios Arturo",lang)
                exit()
        except IndexError: pass
        except UnboundLocalError: pass

        try:

            if mode == "???":
                if lang == "en":
                    say("I haven't understood you",lang)

                elif lang == "es":
                    say("No te he entendido bien",lang)
        except IndexError: pass
        except UnboundLocalError: pass

        speech = " "

if __name__ == "__main__":

    r = sr.Recognizer()
    mic = sr.Microphone()
    lang = "en"
    change_commands = {"en":"change","es":"cambiar"}
    exit_commands = {"en":"exit", "es":"salir"}

    while True:
        run()