from django.urls import path
from api.views import tiktok_api

urlpatterns = [
  path("tiktok/", tiktok_api, name="tiktok")
]