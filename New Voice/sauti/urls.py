from django.urls import path
from . import views

urlpatterns = [
    path('send',views.display_result, name= 'display'),
    path('',views.recorder, name= 'voice'),
    path('transcribe_audio/', views.transcribe_audio, name='transcribe_audio'),
    path('send-email/', views.send_email, name='mail'),
]
