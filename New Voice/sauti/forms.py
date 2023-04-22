from django import forms
from .models import Written

class WrittenForm(forms.ModelForm):
    class Meta:
        model =Written
        fields =['to_email']

