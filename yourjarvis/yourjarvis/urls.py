from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('your_jarvis/', include('jarvis_assist_app.urls')),
]
