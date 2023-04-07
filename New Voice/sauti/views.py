from django.shortcuts import render
import io
import json
from django.http import JsonResponse, HttpResponseNotAllowed
from google.cloud import speech
from google.oauth2 import service_account
from django.views.decorators.csrf import csrf_exempt
from .models import Transcription




@csrf_exempt
def transcribe_audio(request):
    if request.method == 'POST':
        credentials = service_account.Credentials.from_service_account_file('friday.json')
        client = speech.SpeechClient(credentials=credentials)

        data = json.loads(request.body)
        audio_bytes = io.BytesIO(data['audio_data'].encode('utf-8'))

        audio = speech.RecognitionAudio(content=audio_bytes.read())

        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=16000,
            language_code='en-US',
            enable_automatic_punctuation=True,
            enable_word_time_offsets=True,
        )

        response = client.recognize(config=config, audio=audio)

        results = []
        for result in response.results:
            transcript = result.alternatives[0].transcript
            for word in result.alternatives[0].words:
                start_time = word.start_time.total_seconds()
                end_time = word.end_time.total_seconds()
                word_text = word.word
                results.append((start_time, end_time, word_text))

        transcription = Transcription(text=transcript)
        
        transcription.save()
        

        data = {'transcription': transcript, 'word_timings': results}
        return JsonResponse(data)
    else:
        return HttpResponseNotAllowed(['POST'])

def display_result(request):
    
    return render(request, 'display.html')