
import io
import json
import requests

from django.shortcuts import render,redirect
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse
from .import speech_to_text
from .models import Written


def display_result(request):
    
    
    return render(request, 'display.html')

def index(request):
    if request.method =='POST':
       
      

        text = speech_to_text.recognize_speech()
        return render(request,'display.html',{"text":text})
    else:
        return render(request, "voice.html")


def send_email(request):
    if request.method == 'POST':
        to_email = request.POST.get('to_email')
        content = request.POST.get('transcription')

        written = Written(to_email=to_email,text=content)
        written.save()
        mail = requests.post('https://open-email-delivery.onrender.com/send', json={
            "mailfrom": "oukonimrod@gmail.com",
            "mailto": to_email,
            "message": content,
        })
        return redirect('inbox')
    else:
        return JsonResponse({
            'status_code': 405,
            'response': 'Method Not Allowed'
        })

def showinbox(request):
    
        

    context ={
        'object_list':Written.objects.all(),
        
        
    }
    return render(request, 'inbox.html',context)
