from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def audio_to_text(request):
    return HttpResponse('Audio To Text')