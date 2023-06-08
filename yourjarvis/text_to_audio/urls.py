from django.urls import path
from . import views

# * Created for URL control
urlpatterns = [
    path("", views.text_to_audio, name="text_to_audio"),
]
