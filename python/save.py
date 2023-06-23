import pyttsx3

# text=f.read().replace("\n", " ")
# engine = pyttsx3.init()
# engine.say(text)
# engine.setProperty('rate', 120)
# engine.setProperty('volume', 0.01)
# engine.runAndWait()

def say(ans):
    '''
    Aseel Bdoor
    '''
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        engine.setProperty('voice', voice.id)
    engine.say(ans)
    engine.runAndWait()