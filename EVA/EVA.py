import speech2text, say, mode, json
import speech_recognition as sr

def run():

    with sr.Microphone() as source:
        global lang
        with open("info.json", "r") as read_file:
            data = json.load(read_file)
            lang = data["language"]
        if lang == "en":
            speech = speech2text.English(source)
        elif lang == "es":
            speech = speech2text.Spanish(source)
        else: 
            speech = speech2text.English(source)
            lang = "en"

        mode.get_func(speech, lang)

        speech = " "

