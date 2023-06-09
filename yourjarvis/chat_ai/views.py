from django.shortcuts import render
from django.http import HttpResponse
from .service import get_chat


# Create your views here.
def chat_ai(request):
    get_message = get_chat('Olá Boa Noite!')
    return HttpResponse(get_message)
