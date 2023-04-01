from django.shortcuts import render
import speech_recognition as sr
import websocket

def home(request):
    return render(request,'home.html')

def on_message(ws,message):
    pass

def on_error(ws,error):
    pass

def on_close(ws):
    pass

def on_open(ws):

    def main():
        r = sr.Recognizer()
        with sr.Microphone()as source:
            r.adjust_for_ambient_noise(source)
            print("please say something..")

            audio = r.listen(source)

            try:
                message=r.recognize_google(audio)
                ws.send(message)
            except Exception as e:
                print("Error :" + str(e))
        
        ws.close()
    
    websocket.enableTrace(True)
    ws.run_forever()


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://localhost:8000/ws/", on_message=on_message, on_error=on_error, on_close=on_close)
    ws.on_open =on_open
    ws.run_forever()
    main()




    