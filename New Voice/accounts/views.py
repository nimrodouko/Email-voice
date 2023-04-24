from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .forms import CustomCreation


class SignupView(generic.CreateView):
    template_name='signup.html'
    form_class = CustomCreation
    success_url =reverse_lazy('voice')


# Create your views here.
