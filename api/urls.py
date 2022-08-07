from django.urls import path
from api.views import tiktok_api, instagram_api

urlpatterns = [
  path("tiktok_api/", tiktok_api),
  path("instagram_api/", instagram_api)
]