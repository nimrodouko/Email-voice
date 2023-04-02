import speech_recognition as sr
import tkinter as tk

class SpeechRecognizerGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.resizable(False, False)
        self.root.title("Speech Recognizer")

        
        self.mic_button = tk.Button(text="🎤", font=("Arial", 60), command=self.start_listening)
        self.mic_button.pack()

        
        self.text_box = tk.Text(width=50, height=10, font=("Arial", 12))
        self.text_box.pack()

        self.r = sr.Recognizer()

    def start_listening(self):
        with sr.Microphone() as source:
            self.r.adjust_for_ambient_noise(source)
            self.text_box.delete("1.0", tk.END)
            self.text_box.insert(tk.END, "Listening...")

            audio = self.r.listen(source)

            try:
                recognized_text = self.r.recognize_google(audio)
                self.text_box.delete("1.0", tk.END)
                self.text_box.insert(tk.END, recognized_text)
            except Exception as e:
                self.text_box.delete("1.0", tk.END)
                self.text_box.insert(tk.END, f"Reapet: {str(e)}")

if __name__ == "__main__":
    app = SpeechRecognizerGUI()
    app.root.mainloop()
