from django.urls import path
from . import views

# * Created for URL control
urlpatterns = [
    path("", views.chat_ai, name='chat_ai'),
]
