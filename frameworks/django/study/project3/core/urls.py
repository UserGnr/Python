from django.urls import path
from django import IndexView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]
