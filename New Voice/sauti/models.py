from django.db import models

# Create your models here.
class Written(models.Model):
    text = models.TextField(max_length=500)
    to_email = models.EmailField(null= True)

    
  

    
