from django.urls import path

from . import views

app_name = 'sensors'

urlpatterns = [
    path("", views.index, name="index"),
    path("logs/", views.logs, name="logs"),
]