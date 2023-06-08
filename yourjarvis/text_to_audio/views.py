from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def text_to_audio(request):
    return HttpResponse('Text To Audio')