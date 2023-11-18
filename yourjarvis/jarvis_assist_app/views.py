from django.http import JsonResponse, FileResponse
from .modules.text_processing import Text_To_Audio_Manage
from .modules.audio_processing import audio_to_text
from .forms import UploadFileForm
from django.views.decorators.csrf import csrf_exempt
import os
from dotenv import load_dotenv
from httpx import Client
from .modules.ai.request import DoRequest as req
from .modules.ai.ai import PoeAiGen

dir_path = os.path.dirname(os.path.abspath(__file__))
static_path = os.path.join(dir_path, "static", ".env")

temp_path = os.path.join(dir_path, "temp")

load_dotenv(static_path)
poeKey = os.getenv("POE-KEY")


@csrf_exempt
def jarvis_assist(request):
    if request.method == "POST":
        # FormFile instance // request.POST and request.FILES is required.
        form = UploadFileForm(request.POST, request.FILES)

        # Form Validate
        if form.is_valid():
            # Cleaning old .mp3 files
            for trash in os.listdir(temp_path):
                if ".mp3" in trash:
                    os.remove(temp_path + f"\\{trash}")

            # Get File from Form after validation pass.
            audio_file = form.cleaned_data["file"]

            # Convert user audio to text
            text_response = audio_to_text(audio_file)

            # Send message for AI and get response
            poeAi = PoeAiGen(request=req, client=Client, key_cookie=poeKey)
            poeAi.send_msg(bot="chinchilla", message=text_response)
            ai_response = poeAi.get_last_msg()

            # Converting text to audio and generate file.
            tta = Text_To_Audio_Manage()
            tta.text_to_audio(ai_response)
            file_name = tta.get_file_name()

            return FileResponse(open(file_name, "rb"))

        else:
            return JsonResponse(form.errors)

    return JsonResponse({"error": "invalid request, POST expected!"})
