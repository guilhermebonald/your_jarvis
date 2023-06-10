from django.http import HttpResponse
from django.http import JsonResponse
from .service import get_chat, audio_to_text
from .forms import UploadFile
from django.views.decorators.csrf import csrf_exempt
import speech_recognition as sr


@csrf_exempt
def jarvis_assist(request):
    if request.method == "POST":
        # Recognizer Instance
        r = sr.Recognizer()
        # FormFile instance // request.POST and request.FILES is required.
        form = UploadFile(request.POST, request.FILES)

        # Form Validate
        if form.is_valid():
            # Get File from Form after validation pass.
            audio_file = form.cleaned_data["file"]
            # Opening
            with sr.AudioFile(audio_file) as source:
                audio = r.record(source)

            try:
                message = r.recognize_google(audio, language="pt-BR")
                return JsonResponse({"message": message})
            except sr.RequestError as e:
                return JsonResponse({"file error": e})
        else:
            return JsonResponse(form.errors)

    return JsonResponse({"error": "Requisição Inválida"})


def chat_ai(request):
    get_message = get_chat("Olá Boa Noite!")
    return HttpResponse(get_message)
