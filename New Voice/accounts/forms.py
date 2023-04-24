from .models import CustomUser
from django import forms
from django.contrib.auth.forms import UserCreationForm


class CustomCreation(UserCreationForm):
      class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields =UserCreationForm.Meta.fields +('email',)
        
        
        
        
        


