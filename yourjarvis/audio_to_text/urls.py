from django.urls import path
from . import views

# * Audio_To_Text URL.
urlpatterns = [
    path("", views.audio_to_text, name="audio_to_text"),
]
