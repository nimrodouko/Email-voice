import pyaudio
import speech_recognition as sr
from .models import Written
def  recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("speak now:")
        audio = r.listen(source, timeout = 5)
    
    try:
        text = r.recognize_google(audio)
        written =Written(text=text)
        written.save()
        return(text)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results:{e}")