from django.db import models

# Create your models here.
class Transcription(models.Model):
    subject = models.TextField(max_length=100) 
    transcription = models.TextField(max_length=1000)

