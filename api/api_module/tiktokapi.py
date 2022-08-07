from TikTokApi import TikTokApi
import json

def tik(hash_tag):
    api = TikTokApi()
    data = []
    tag = api.hashtag(name=hash_tag)
    for video in tag.videos():
        id_info = video.id
        search_info= api.video(id=id_info).info()
        url = search_info["video"]["playAddr"]
        thumbnail= search_info["video"]["cover"]
        video_info  = {"id": id_info,"url":url,"thumbnail":thumbnail}
        data.append(video_info)
        if len(data) == 15:
            break
    Json_data = json.dumps(data,indent=4,ensure_ascii=False)
    return Json_data
def get_tiktok(get_keyword):
    data = tik(get_keyword)
    return json.loads(data)

if __name__ =="__main__":
    data = get_tiktok("車")
    print(data)
