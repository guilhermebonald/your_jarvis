import speech_recognition as sr
import json


# * Get Audio and convert to Text.
def audio_to_text(file):
    r = sr.Recognizer()

    with sr.AudioFile(file) as source:
        audio = r.record(source)

    try:
        message = r.recognize_whisper(audio, language="portuguese")
        return message
    except sr.RequestError as e:
        return json.dumps({"file error": e})
