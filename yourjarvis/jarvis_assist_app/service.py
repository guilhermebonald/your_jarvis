import requests
import os
from dotenv import load_dotenv
import speech_recognition as sr
import json

dir_path = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(dir_path, "static", ".env")

load_dotenv(path)


# * Get AI Response from API.
def get_ai(message):
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


# * Get Audio and convert to Text.
def audio_to_text(file):
    r = sr.Recognizer()

    with sr.AudioFile(file) as source:
        audio = r.record(source)

    try:
        message = r.recognize_google(audio, language="pt-BR")
        return message
    except sr.RequestError as e:
        return json.dumps({"file error": e})
