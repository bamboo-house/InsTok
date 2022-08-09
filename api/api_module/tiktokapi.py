from TikTokApi import TikTokApi
import json
import sys
import threading

def get_tiktok(hash_tag):
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
        if (len(data) > 10):
            break
    api.shutdown()
    Json_data = json.dumps(data,indent=4,ensure_ascii=False)
    return Json_data
# from TikTokApi import TikTokApi

# verifyfp = "7C7895aec232c70a2649cd4db07ac203a2b593743d30ddfc14dbf316f6eb5c5f50"
# api = TikTokApi.get_instance(custom_verifyFp=verifyfp)

# # 特定のハッシュタグを持つ動画を10個取得
# results = 10
# hashtag = 'apple'
# tiktoks = api.by_hashtag(count=results, hashtag=hashtag)

# # 各動画の情報をループ処理で取得
# for tiktok in tiktoks:
#     print([tiktok])

# # 動画のダウンロード
# video_bytes = api.get_video_by_tiktok(tiktoks[0])
# video_title = tiktoks[0]["id"]

# # urlを指定して動画をダウンロードする場合は以下を使用
# # video_bytes = api.get_video_by_url('https://www.tiktok.com/@clearlyhemo/video/7032985960992361730?is_copy_url=1&is_from_webapp=v1&q=Messi&t=1638852369929')

# # 動画の保存
# with open(f"{video_title}.mp4", "wb") as o:
#     o.write(video_bytes)
