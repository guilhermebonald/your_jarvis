from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('audio_to_text/', include('audio_to_text.urls')),
    path('chat_ai/', include('chat_ai.urls')),
    path('text_to_audio/', include('text_to_audio.urls'))
]
