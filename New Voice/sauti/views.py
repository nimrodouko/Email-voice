
import io
import json
import requests
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed
from google.cloud import speech
from google.oauth2 import service_account
from .models import Written






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

        written = Written(text=transcript)
        written.save()
        data = {'transcription': transcript, 'word_timings': results}
        return JsonResponse(data)
    else:
        return HttpResponseNotAllowed(['POST'])

def display_result(request):
    transcription = request.POST.get('transcription','')
    return render(request, 'display.html',{'transcription':transcription})

def send_email(request):
    if request.method == 'POST':
        to_email = request.POST.get('to_email')
        content = request.POST.get('transcription')
        mail = requests.post('https://open-email-delivery.onrender.com/send', json={
            "mailfrom": "oukonimrod@gmail.com",
            "mailto": to_email,
            "message": content,
        },timeout=60)
        return JsonResponse({
            'status_code': mail.status_code,
            'response': mail.json()
        })
    else:
        return JsonResponse({
            'status_code': 405,
            'response': 'Method Not Allowed'
        })
