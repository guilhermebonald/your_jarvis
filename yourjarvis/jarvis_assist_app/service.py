import requests
import os
from dotenv import load_dotenv
import speech_recognition as sr
from django.http import JsonResponse

dir_path = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(dir_path, "static", ".env")

load_dotenv(path)


# Get AI Response from API.
def get_chat(message):
    url = (
        f"https://api.betterapi.net/youchat?inputs={message}. Responda em portugues&key="
        + os.getenv("YOU_API_KEY")
    )

    response = requests.get(url)
    if response.status_code == 200:
        json = response.json()
        return json["generated_text"]
    else:
        return {"Falha na requisição": response.status_code}


# Get Audio and convert to Text.
def audio_to_text(file):
    r = sr.Recognizer()
    audio_file = file

    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)

    try:
        message = r.recognize_google(audio, language="pt-BR")
        return JsonResponse({"message": message})
    except sr.RequestError as e:
        return JsonResponse({"file error": e})
