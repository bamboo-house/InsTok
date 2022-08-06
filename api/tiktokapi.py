from TikTokApi import TikTokApi
import json

def tikapi (hash_tag):
    tag = api.hashtag(name=hash_tag)
    deta = []
    for video in tag.videos():
        id_info = video.id
        search_info= api.video(id=id_info).info()
        url = search_info["video"]["playAddr"]
        thumbnail= search_info["video"]["cover"]
        video_info  = {"id": id_info,"url":url,"thumbnail":thumbnail}
        deta.append(video_info)
    with open("./test.json","w",encoding='utf_8') as f:
        json.dump(deta,f,indent=4,ensure_ascii=False)
    
if __name__ =="__main__":
    api = TikTokApi()
    hash_tag = input("検索:")
    #hash_tag = "本田翼"
    tikapi(hash_tag)
