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
            dct = {"id":id, "permalink":permalink, "media_url":media_url}
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

# if __name__ == '__main__':
#     obj = InstagramHashtagSearch("17841454148257811","EAARn5vWZBORsBAB3MQHh9nGIroGZBZBKxS2ZCyNyiBoKetysVqnBmXzYnukNgLHkBOvkCNik8yXNjheU9mo9lckUC2Fsm9BUgOAkZAchXslN67dfYfxoUqFxtv7oiYDyqcwQGANcoYpCnwMtwkX3WLBtvMbOZC9BZBsZCZCAZBuBKPvJWoo7kZAgTf15GCKyIH9v0gZD")
#     result1=obj.get_permalink_list("マキアート")
#     result = obj.get_media_url_list("マキアート")

#     print(result1)

def result(q):
    obj = InstagramHashtagSearch("17841454148257811","EAARn5vWZBORsBAGTaZCH0e0tb0nzWQTmDZAB1LSBmSZC9TtucGhqKLHbZBJ2EZA69u5z7rrRiiIaq0ZASdD02cm2s0uBOAGi1ansHc0kp5K3GG06n3fYcaZCqPE3dnzlAZCKfEXopuzFX0MkZBZCd7BfzgaDdX4OqlpQPfZBKwfcTyTbZACM6ODk5QEWW")
    # permalink_url=obj.get_permalink_list(str(q))
    # madia_url = obj.get_media_url_list(str(q))
    # pprint.pprint(obj.get_permalink_list(str(q)))

    with open('../instagram_data.json', mode='wt', encoding='utf-8') as file:
        json.dump(obj.get_permalink_list(str(q)), file, ensure_ascii=False, indent=4)


    # res=obj.__seach_hashtag(str(q))
    # print(res)

    # hosiijson=obj.__request_url(obj.hashtag_search_url)
    # print(hosiijson)



    # pprint.pprint(permalink_url)
    # pprint.pprint(madia_url)
    # print(len(permalink_url))
    # print(len(madia_url))




result("カフェ")
