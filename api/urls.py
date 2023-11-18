from django.urls import path
from .views import tick

urlpatterns = [
    path("tick/", tick),
]
