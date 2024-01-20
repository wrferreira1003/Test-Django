from django.urls import path
from .API.api import api

urlpatterns = [
    path('', api.urls)
]
