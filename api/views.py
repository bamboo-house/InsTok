from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from api.api_module import instagramapi
from api.api_module import tiktokapi
import json

@api_view(["GET"])
def tiktok_api(request, word):
  # data = tiktokapi.get_tiktok("淡路島")
  # print(data)
  # j2p_data = json.loads(data)
  print(word)
  data = [{
        "id": "6792000415627037953",
        "url": "https://v16-webapp.tiktok.com/e2f763d1a71267fcf3daa1995e091508/62f27aa2/video/n/v0102/41e94c91b3ee4c2e99a02726d2d21699/?a=1988&ch=0&cr=0&dr=0&lr=tiktok&cd=0%7C0%7C1%7C0&cv=1&br=7416&bt=3708&btag=80000&cs=0&ds=3&ft=eXd.6HVJMyq8ZA1Q_we2N1.eyl7Gb&mime_type=video_mp4&qs=0&rc=OTk7ZmlpZTRpaDY4Mzk4OEBpanU0d3AzdnEzczMzZTgzM0A1LWFhXmMwXzAxYy1hXzQwYSM0LWxmYmhxZC5fLS0xLzRzcw%3D%3D&l=202208090917390102230222102390E3D2",
        "thumbnail": "https://p16-sign-sg.tiktokcdn.com/obj/v0201/408989eaff9c4fd8891a0a21c76a32a6?x-expires=1660057200&x-signature=j9ck0Zil4%2FADR6oImnWxeFTTbjI%3D"
    },
    {
        "id": "7060015827667455234",
        "url": "https://v16-webapp.tiktok.com/087f85de6cd1c68a38759b112e6d828c/62f27aa0/video/tos/alisg/tos-alisg-pve-0037c001/ec309878d5a24af4b9905b8a070e596d/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0&cv=1&br=3524&bt=1762&btag=80000&cs=0&ds=3&ft=eXd.6HVJMyq8Z41Q_we2Npz3yl7Gb&mime_type=video_mp4&qs=0&rc=OGY7NDNoNGloNjw5M2VnN0BpajNlNDY6Zjc2OjMzODczNEAxL14vNGJhNjUxNi9hXl9eYSNuZWJlcjRnX3FgLS1kMS1zcw%3D%3D&l=202208090917390102230222102390E411",
        "thumbnail": "https://p16-sign-sg.tiktokcdn.com/obj/tos-alisg-p-0037/c55215c2a1004a7f83a405e88f0bd59d_1643788033?x-expires=1660057200&x-signature=Oe%2Bvf8pEXPdEKPTBiu65ZsfmuOk%3D"
    },
    {
        "id": "6986194883094646018",
        "url": "https://v16-webapp.tiktok.com/4457516f9363bb70b30c59b900f0cbf0/62f27acf/video/tos/alisg/tos-alisg-pve-0037/f8c2a3808d4542dfb90ca7e24e3328c0/?a=1988&ch=0&cr=0&dr=0&lr=tiktok&cd=0%7C0%7C1%7C0&cv=1&br=3162&bt=1581&btag=80000&cs=0&ds=3&ft=eXd.6HVJMyq8Z41Q_we2NO3oyl7Gb&mime_type=video_mp4&qs=0&rc=NDM8OTVmaWRkOmZpOjVoZEBpanV2dGQ6Zmh5NjMzODgzNEAxXjExMTUvNTYxX2JjMGIyYSMyXmdwcjRnMm1gLS1kLy1zcw%3D%3D&l=202208090917400102230222102390E43B",
        "thumbnail": "https://p16-sign-sg.tiktokcdn.com/obj/tos-alisg-p-0037/304c95b8b04941ce9b7578644c60b121?x-expires=1660057200&x-signature=zT7da%2B7R7nmdcYZTalV8oslz0AE%3D"
    }
  ]
  return Response(data, status=status.HTTP_201_CREATED)

@api_view(["GET"])
def instagram_api(request):
  # query = request.request.GET.get('query')
  data = instagramapi.get_instagram("本田翼")
  j2p_data = json.loads(data)
  return Response(j2p_data, status=status.HTTP_201_CREATED)