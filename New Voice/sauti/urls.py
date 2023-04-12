from django.urls import path
from . import views

urlpatterns = [
    path('',views.display_result, name= 'display'),
    path('transcribe-audio/', views.transcribe_audio, name='transcribe_audio'),
    path('send-email/', views.send_email, name='mail'),
]
