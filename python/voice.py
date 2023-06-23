import speech_recognition as sr

def main():
    '''
    Aseel Bdoor
    '''
    r = sr.Recognizer()
 
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        # print("Please say something")
        audio = r.listen(source)
        # print("Recognizing Now .... ")

        # recognize speech using google
        try:
            text=r.recognize_google(audio)
            return text
 
        except Exception as e:
            return "I dont here you very well"


if __name__=="__main__":
    main()