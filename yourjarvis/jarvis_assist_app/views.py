from django.http import JsonResponse, FileResponse
from .service import get_ai, audio_to_text, Text_To_Audio_Manage
from .forms import UploadFileForm
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def jarvis_assist(request):
    if request.method == "POST":
        # FormFile instance // request.POST and request.FILES is required.
        form = UploadFileForm(request.POST, request.FILES)
        text_to_audio_manage = Text_To_Audio_Manage()

        # Form Validate
        if form.is_valid():
            # Get File from Form after validation pass.
            audio_file = form.cleaned_data["file"]

            # Context
            get_text = audio_to_text(audio_file)
            ai_response = get_ai(get_text)

            # Text To Audio Manage
            text_to_audio_manage.text_to_audio(get_text)
            file_name = text_to_audio_manage.get_file_name()

            return FileResponse(open(file_name, "rb"))

        else:
            return JsonResponse(form.errors)

    return JsonResponse({"error": "invalid request, POST expected!"})
