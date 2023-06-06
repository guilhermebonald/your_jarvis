from django.urls import path
from . import views

# * Created for URL control
urlpatterns = [
    path("", views.index, name="index"),
]
