import say, json, wikipedia

change_commands = {"en":"change","es":"cambiar"}
exit_commands = {"en":"exit", "es":"salir"}
search_commands = {"en":"search", "es":"buscar"}
silence_commands = {"en":"silence", "es":"silencio"}
say_commands = {"en":"say", "es":"di"}

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
                say.English("Goodbye, "+user)

            elif lang == "es":
                say.Spanish("Adios, "+user)
            exit()
        elif mode == search_commands[lang]:
            wikipedia.set_lang(lang)
            try:
                search = wikipedia.summary(speech_divided[1::], sentences=2)
            
                if lang == "en":
                    say.English("This is what i found on wikipedia about {}. {}".format(speech_divided[1::], search))
                elif lang == "es":
                    say.Spanish("Esto es lo que he encontrado en la wikipedia sobre {}. {}".format(speech_divided[1::],search))
            except wikipedia.exceptions.DisambiguationError:
                if lang == "en":
                    say.English("Be more precise")
                elif lang == "es":
                    say.Spanish("Sé más preciso")
            
        elif mode == silence_commands[lang]:
            with open("info.json", "r") as read_file:
                data = json.load(read_file)
                silence = data["silence"]
            
            if silence == "False":
                with open("info.json", "w") as write_file:
                    data["silence"] = "True"
                    write_file.write(json.dumps(data))

            if silence == "True":
                with open("info.json", "w") as write_file:
                    data["silence"] = "False"
                    write_file.write(json.dumps(data))

        elif mode == say_commands[lang]:
            if lang == "en":
                say.English(" ".join(speech_divided[1::]))
            elif lang == "es":
                say.Spanish(" ".join(speech_divided[1::]))

        else: 
            with open("info.json", "r") as read_file:
                data = json.load(read_file)
                silence = data["silence"]
            if silence == "False":
                print("Strange input: \n"+speech)
                if lang == "en":
                    say.English("I haven't understood you")

                elif lang == "es":
                    say.Spanish("No te he entendido bien")

    except IndexError: pass
    except UnboundLocalError: pass
