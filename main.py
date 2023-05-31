import speech_recognition as sr
import os
from dotenv import load_dotenv
import requests
import pyttsx3

load_dotenv()


# ? >> Audio to Text
def audio_to_text():
    palavra_chave = "computador"
    r = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            print("\n... \n")
            audio = r.listen(source)

        try:
            message = r.recognize_google(audio, language="pt-BR")

            if palavra_chave.lower() in message:
                print("\nPalavra-Chave detectada... Ouvindo!\n")
                message = r.recognize_google(audio, language="pt-BR")
                split_message = message.split()
                message = " ".join(split_message[1:])
                return message
            else:
                print("\nPalavra-Chave não detectada.!\n")
        except sr.UnknownValueError:
            print("\nVoz não detectada.\n")
        except sr.RequestError as e:
            print("Erro na solicitação:", str(e))


# ? >> CHAT
def chat_ai(chat):
    url = (
        f"https://api.betterapi.net/youchat?inputs={chat}. Responda em portugues&key="
        + os.getenv("YOU_API_KEY")
    )
    response = requests.get(url)
    if response.status_code == 200:
        json = response.json()
        return json["generated_text"]
    else:
        print(f"Falha na requisição: {response.status_code}")


# ? Text to Audio
def text_to_audio(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def main():
    message = audio_to_text()
    print("\nPergunta: " + message)
    text = chat_ai(message)
    print("\nResposta: " + text)
    text_to_audio(text)


while True:
    main()
