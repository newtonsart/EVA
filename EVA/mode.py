import say, json

change_commands = {"en":"change","es":"cambiar"}
exit_commands = {"en":"exit", "es":"salir"}
search_commands = {"en":"search", "es":"buscar"}

def change_language(language):
    if language == "Spanish":
            lang = "es"
            say.Spanish("Idioma cambiado al Español")
    
    elif language == "inglés":
            lang = "en"
            say.English("Language changed to English")
    
    else:
        say.English("Language not found")
        lang = "???"
    
    with open("info.json", "r") as read_file:
        data = json.load(read_file)
    with open("info.json", "w") as write_file:
        data["language"] = lang
        write_file.write(json.dumps(data))


def get_func(speech, lang):
    speech_divided = speech.split()
    mode = speech_divided[0]

    try:

        if mode == change_commands[lang]:
            change_language(speech_divided[2])

        elif mode == exit_commands[lang]:
            with open("info.json", "r") as read_file:
                data = json.load(read_file)
                user = data["username"]
            if lang == "en":
                say.English(f"Goodbye, {user}")
            elif lang == "es":
                say.Spanish(f"Adios, {user}")
            exit()
        elif mode == search_commands[lang]:
            wikipedia.set_lang(lang)
            search = wikipedia.summary(speech_divided[1:]

            if lang == "en":
                say.English(f"This is what i found on wikipedia. {search}")

            elif lang == "es":
                say.Spanish(f"Esto es lo que he encontrado en la wikipedia, {search}")
        
        else: 
            print("Strange input: \n"+speech)
            if lang == "en":
                say.English("I haven't understood you")

            elif lang == "es":
                say.Spanish("No te he entendido bien")

    except IndexError: pass
    except UnboundLocalError: pass
