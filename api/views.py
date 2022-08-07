from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from api.api_module import instagramapi
from api.api_module import tiktokapi

# import requests
# import pprint
import json

# from TikTokApi import TikTokApi
# import json


@api_view(["GET"])
def tiktok_api(request):
  data = tiktokapi.get_tiktok("淡路島")
  print(data)
  # j2p_data = json.loads(data)
  return Response(data, status=status.HTTP_201_CREATED)

@api_view(["GET"])
def instagram_api(request):
  # query = request.request.GET.get('query')
  data = instagramapi.get_instagram("本田翼")
  j2p_data = json.loads(data)
  return Response(j2p_data, status=status.HTTP_201_CREATED)
