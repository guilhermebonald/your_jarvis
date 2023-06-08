import speech_recognition as sr
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import UploadFile


# Create your views here.
@csrf_exempt
def audio_to_text(request):
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
