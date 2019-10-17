import speech_recognition as sr

r = sr.Recognizer()

def main(source, lang):
    r.adjust_for_ambient_noise(source)
    
    print("Listening")

    audio = r.listen(source)

    print("Recognizing")

    try:
        speech = r.recognize_google(audio, language = lang)
    except sr.UnknownValueError:pass
    try:
        return speech
    except UnboundLocalError:
        return "???"

def English(source):
    return main(source,"en")

def Spanish(source):
    return main(source,"es")