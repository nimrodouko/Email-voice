import speech_recognition as sr

# Initialize the recognizer
r = sr.Recognizer()

# Use the default microphone as the audio source
with sr.Microphone() as source:
    print("Speak now...")
    # Listen for audio and capture it
    audio = r.listen(source)

# Use Google Speech Recognition to transcribe the audio
try:
    text = r.recognize_google(audio)
    print("You said: {}".format(text))
except sr.UnknownValueError:
    print("Sorry, could not understand what you said.")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
