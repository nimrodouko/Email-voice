from django.db import models

# Create your models here.
class Written(models.Model):
    transcript = models.TextField()
    audio_file = models.FileField(null=True)
    word_timings = models.TextField(null =True)

    
