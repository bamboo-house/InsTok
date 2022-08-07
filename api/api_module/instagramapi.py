import requests
import pprint
import json

class InstagramHashtagSearch:
    # ハッシュタグのID取得用URL
    hashtag_id_api = "https://graph.facebook.com/ig_hashtag_search?user_id={user_id}&q={hashtag}&access_token={access_token}"

    # ハッシュタグの検索用URL
    hashtag_search_api = "https://graph.facebook.com/{hashtag_id}/top_media?user_id={user_id}&fields=id,media_type,media_url,permalink&access_token={access_token}"

    # コンストラクタ引数：インスタグラムのビジネスアカウントID、APIのトークン
    def __init__(self, user_id, access_token):
        self.user_id = user_id
        self.access_token = access_token

    # ハッシュタグの検索して、パーマリンクのリストを得る
    def get_permalink_list(self, hashtag):
        # return [d.get("permalink") for d in self.__seach_hashtag(hashtag) ]
        b =  [d for d in self.__seach_hashtag(hashtag) if d.get("media_url") is not None]

        datelist= []

        for i in range(len(b)-1):
            id = b[i]['id']
            permalink = b[i]['permalink']
            media_url = b[i]['media_url']
            dct = {"id":id, "url":permalink, "thumbnail":media_url}
            datelist.append(dct)
        return(datelist)



    # ハッシュタグの検索して、画像リンクのリストを得る（画像でないページはスキップする）
    # def get_media_url_list(self, hashtag):
    #     return [d.get("media_url") for d in self.__seach_hashtag(hashtag) if d.get("media_url") is not None]


    # ハッシュタグで検索して、jsonデータを取得する
    def __seach_hashtag(self, hashtag):
        # ハッシュタグIDの取得
        hashtag_id_url = self.hashtag_id_api.format(user_id=self.user_id, hashtag=hashtag, access_token=self.access_token)

        # 応答のjsonをパースして数値を取得
        hashtag_id = self.__request_url(hashtag_id_url)[0]["id"]

        # ハッシュタグの検索
        hashtag_search_url = self.hashtag_search_api.format(hashtag_id=hashtag_id, user_id=self.user_id, access_token=self.access_token)

        # 応答のjsonをパースして数値を取得
        result_list = self.__request_url(hashtag_search_url)
        # print(result_list)
        return result_list


    # WebAPIを叩く
    def __request_url(self, url):
        response = requests.get(url)
        return json.loads(response.text)["data"]

def get_instagram(q):
    obj = InstagramHashtagSearch("17841454148257811","EAAuPmMzVoBsBAOb5sP1TZAPaXVRVZBCXjGlD5VNcGnYmOROZAQdwtnerB5zNM5ei6SJVyZCe2tugFB7WQtcCMGGjhEb0c6vdccy0SpErSaZAPMZBeZBM0cajkcrAKscdSRqIEaJYTRhvKLOY4Q5ouf5kqm1fVetiFBhLp03qQ0dNM7TmviznUsnLQOFRFYj4kcdYESMc6EIhTjTZCVApproQNl99cIBqZCAq0b7zoP7CXSOrwpGuJ4tXUc0YvtsXYsOEZD")
    pprint.pprint(obj.get_permalink_list(str(q)))

    return json.dumps(obj.get_permalink_list(str(q)), ensure_ascii=False, indent=4)
