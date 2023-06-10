from django.urls import path
from . import views

# * Created for URL control
urlpatterns = [
    path("", views.jarvis_assist, name='jarvis_assist'),
]
