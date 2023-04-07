from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.display_result, name= 'display'),
    path('transcribe-audio/', views.transcribe_audio, name='transcribe_audio'),
]
