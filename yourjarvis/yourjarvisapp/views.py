from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    text = 'Olá'
    return render(request, 'home.html', {'variavel': text})