from django.http import JsonResponse
from .service import get_ai, audio_to_text, text_to_audio
from .forms import UploadFileForm
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def jarvis_assist(request):
    if request.method == "POST":
        # FormFile instance // request.POST and request.FILES is required.
        form = UploadFileForm(request.POST, request.FILES)

        # Form Validate
        if form.is_valid():
            # Get File from Form after validation pass.
            audio_file = form.cleaned_data["file"]

            # Context
            get_text = audio_to_text(audio_file)
            ai_response = get_ai(get_text)

            return JsonResponse(ai_response)

            # response
            # return JsonResponse({
            #     "Question": get_text,
            #     "Response": ai_response
            #                      })

        else:
            return JsonResponse(form.errors)

    return JsonResponse({"error": "invalid request, POST expected!"})
