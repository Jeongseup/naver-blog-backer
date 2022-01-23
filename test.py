import urllib.request
#
# url = "https://blogattach.naver.com/ae3bb20216252491b85e3b0936d1a5d17420dcd4/20220120_104_blogfile/thswjdtmq4_1642655879720_4luRA9_zip/chromedriver_win32.zip"
# file_name = 'chrome.zip'
#
# urllib.request.urlretrieve(url,file_name)
# print("저장완료")
#

from html import unescape
import json

dataModule = '{"type":"v2_oembed", "id" :"SE-110b61fb-42b2-49b1-9bdc-3ae9662f60a8", "data" : { "html": &quot;&lt;iframe width&#x3D;\&quot;200\&quot; height&#x3D;\&quot;113\&quot; src&#x3D;\&quot;https://www.youtube.com/embed/d1NurScOaHI?feature&#x3D;oembed\&quot; frameborder&#x3D;\&quot;0\&quot; allow&#x3D;\&quot;accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\&quot; allowfullscreen&gt;&lt;/iframe&gt;&quot;, "originalWidth" : "200", "originalHeight" : "113", "contentMode" : "fit", "description": &quot;#노포맛집 #부천자유시장맛집 #부천맛집부천에서 닭곰탕이 정말 맛있는 믿거나말거나 상호명이 믿거나말거나 ㅎㅎㅎ저 오랜 단골이지만 오늘 상호명 처음 알았네요...그냥 닭곰탕 맛있어서 닭곰탕집... 이렇게 말했는데....사라진 줄 알았던.. 단골집의 부활!!! 꼭 한번은 가보세요. 숨은...&quot;, "inputUrl": "https://www.youtube.com/watch?v&#x3D;d1NurScOaHI", "thumbnailUrl" : "https://i.ytimg.com/vi/d1NurScOaHI/hqdefault.jpg", "thumbnailHeight" : "360", "thumbnailWidth" : "480", "title": &quot;부천 자유시장맛집 닭곰탕 굿! 오래된 노포집 분식점 믿거나말거나&quot;, "providerUrl": "https://www.youtube.com/", "align": "center", "type" : "video" }}'
unescapedData = unescape(dataModule)
# print(unescapedData.replace('\\"', ''))

json_data = json.loads(unescapedData.replace('\\"', ""))
# print(json_data)
# print(json_data['data']['inputUrl'])
# print(json_data['data']['title'])
# print(json_data['data']['thumbnailUrl'])
# print(json_data['data']['description'])
keys = json_data['data'].keys()


key1 = 'description'

if key1 in json_data['data'].keys():
	print("Key exists")
else:
	print("Key does not exist")

keys2 = [key for key in json_data['data']]
print(list(keys))
print(keys2)

