import colorama
from colorama import Fore, Style, Back
import speech_recognition as sr

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(Fore.LIGHTBLUE_EX + "Speak:" + Style.RESET_ALL, end="")
        audio = r.listen(source)

    try:
        print(Fore.LIGHTBLUE_EX + "User: " + Style.RESET_ALL, end="")
        text = r.recognize_google(audio)
        print(text)
        return text.lower()
    except sr.UnknownValueError:
        print(Fore.LIGHTBLUE_EX + "User: " + Style.RESET_ALL + "Sorry, I didn't understand that.")
        return ""
    except sr.RequestError as e:
        print(Fore.LIGHTBLUE_EX + "User: " + Style.RESET_ALL + "Sorry, there was an issue with speech recognition. {0}".format(e))
        return ""




if __name__=="__main__":
    a=listen()
    print(a)