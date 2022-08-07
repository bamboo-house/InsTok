from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(["GET"])
def tiktok_api(resuest):
  data = [
    {
      "id": 1,
      "title": "タイトル１タイトル１",
      "body": "ボディ１ボディ１ボディ１ボディ１"
    },
    {
      "id": 2,
      "title": "タイトル２タイトル２タイトル２",
      "body": "ボディ２ボディ２ボディ２ボディ２"
    },
    {
      "id": 3,
      "title": "タイトル3タイトル3タイトル3",
      "body": "ボディ3ボディ3ボディ3ボディ3"
    }
  ]
  # target_keyword = request.keyword
  # tiktok_json = get_tiktok(target_keyword)
  # return Response(tiktok_json, status=status.HTTP_201_CREATED)
  return Response(data, status=status.HTTP_201_CREATED)

@api_view(["GET"])
def instagram_api(resuest):
  data = [
    {
      "id": 1,
      "title": "タイトル１タイトル１",
      "body": "ボディ１ボディ１ボディ１ボディ１"
    },
    {
      "id": 2,
      "title": "タイトル２タイトル２タイトル２",
      "body": "ボディ２ボディ２ボディ２ボディ２"
    }
  ]
  return Response(data, status=status.HTTP_201_CREATED)
