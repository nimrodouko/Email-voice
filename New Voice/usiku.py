import pyaudio
import speech_recognition as sr

# Create a PyAudio object
p = pyaudio.PyAudio()

# Open the microphone
stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

# Record some audio
print("recording...")
audio_data = stream.read(44100)

# Close the microphone
stream.stop_stream()
stream.close()
p.terminate()

# Use SpeechRecognition to transcribe the audio
r = sr.Recognizer()
transcription = r.recognize_google(audio_data)

print(transcription)
