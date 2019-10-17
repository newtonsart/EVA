import goslate

def To_English(message):
    gs = goslate.Goslate()

    return gs.translate(message, "en")

def To_Spanish(message):
    gs = goslate.Goslate()
    
    return gs.translate(message, "es")
