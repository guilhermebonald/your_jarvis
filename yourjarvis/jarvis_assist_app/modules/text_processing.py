import os
import pyttsx3
from tempfile import NamedTemporaryFile

dir_path = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(dir_path, "static", ".env")


# * Text to Audio
class Text_To_Audio_Manage:
    def text_to_audio(self, text):
        temp_path = os.path.join(dir_path, "temp")
        with NamedTemporaryFile(
            prefix="Y_Jarvis-", delete=True, mode="wb", dir=temp_path
        ) as file:
            # pyttsx3 convert text to audio
            engine = pyttsx3.init()
            self.temp_file_name = file.name
            engine.save_to_file(text, self.temp_file_name + ".mp3")
            engine.runAndWait()

    def get_file_name(self):
        file_name = self.temp_file_name + ".mp3"
        return file_name


# tta = Text_To_Audio_Manage()
# tta.text_to_audio("Olá, Boa noite!")
