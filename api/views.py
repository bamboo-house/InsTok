from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(["GET"])
def tiktok_api(resuest):
  data = [
    {
      "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
      "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit"
    },
    {
      "title": "qui est esse",
      "body": "est rerum tempore vitae\nsequi sint nihil reprehenvel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
    }
  ]
  return Response(data, status=status.HTTP_201_CREATED)
