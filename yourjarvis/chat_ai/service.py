import requests
import os
from dotenv import load_dotenv

dir_path = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(dir_path, 'static', '.env')

load_dotenv(path)

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