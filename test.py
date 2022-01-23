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


dataModule = '{"type":"v2_video", "id" :"SE-ab6c46f1-0005-4e67-8bc9-157fa1b56029", "data" : { "videoType" : "player", "vid" : "3A9F771DE6BF870FA8FD61CB817EEFA6FF66", "inkey" : "V12969c243f6c0ff5f7e3021dc9e8493b2099dd964be05e58c6e1c941b1cb09d2c3ab021dc9e8493b2099", "thumbnail": "https://phinf.pstatic.net/image.nmv/blog_2022_01_20_1149/a6ea48f9-794c-11ec-bd70-505dac8c38f5_01.jpg", "originalWidth": "1920", "originalHeight": "1040", "width": "693", "height": "375", "contentMode": "fit", "format": "normal", "mediaMeta": {"@ctype":"mediaMeta","title":"영상제목 test","tags":["testtag"],"description":"정보 test"}, "useServiceData": "false"}}'
jsonData = json.loads(unescape(dataModule).replace('\\"', ""))['data']

print(jsonData)
vdieoId = jsonData['vid']
vdieoInkey = jsonData['inkey']
videoOriginalWidth = jsonData['originalWidth']

# thumbnail Image 저장.. ?
# originalWidth
vdieoMetadata = jsonData['mediaMeta']
print(vdieoMetadata)

jsonUrl = 'https://apis.naver.com/rmcnmv/rmcnmv/vod/play/v2.0/' + vdieoId + '?key=' + vdieoInkey

import urllib.request, json
with urllib.request.urlopen(jsonUrl) as url:
	videoList = json.loads(url.read().decode())['videos']['list']

	for video in videoList:
		print(video['encodingOption']['width'])

		if str(video['encodingOption']['width']) == str(videoOriginalWidth):
			print(video['source'])
			break
#
#
# testList  = [{'id': '81C79F49179A28767D372780974B2E7A6B6B', 'useP2P': False, 'duration': 36.103, 'size': 814951, 'type': 'avc1', 'encodingOption': {'id': '360P_01', 'name': '360p', 'profile': 'BASE', 'width': 640, 'height': 348, 'isEncodingComplete': 'true', 'completeProgress': '100'}, 'bitrate': {'video': 179.0, 'audio': 0.0}, 'p2pMetaUrl': '', 'p2pUrl': '', 'source': 'https://b01-kr-naver-vod.pstatic.net/blog/a/read/v2/VOD_ALPHA/blog_2022_01_20_953/b0296203-794c-11ec-87b4-48df37269fd0.mp4?_lsu_sa_=6de501f8c1b360263bdcf5bc6c75dfb01ea536187f023ff63d97f3cc57243e854e2b8a086715c007802c3392a3370bab6fd3222fb3efd65d62a795f293df46a9f501bac697df397414b4e53005b7d7c4&in_out_flag=1', 'sourceFrom': 'GN'}, {'id': '3A9F771DE6BF870FA8FD61CB817EEFA6FF66', 'useP2P': False, 'duration': 36.103, 'size': 1195294, 'type': 'avc1', 'isDefault': True, 'encodingOption': {'id': '480P_01', 'name': '480p', 'profile': 'BASE', 'width': 854, 'height': 464, 'isEncodingComplete': 'true', 'completeProgress': '100'}, 'bitrate': {'video': 262.0, 'audio': 0.0}, 'p2pMetaUrl': '', 'p2pUrl': '', 'source': 'https://b01-kr-naver-vod.pstatic.net/blog/a/read/v2/VOD_ALPHA/blog_2022_01_20_614/b028026e-794c-11ec-87b4-48df37269fd0.mp4?_lsu_sa_=6445d5f841506e06ecdde55a6f5513b52e1738b83a05ff843477e1c1473831b587230a3d6da51903105f33c22a310b7f8a4c0a7ba355182a27918803d63b9dd9a012f7a8cbc84497c82d5af0c75f3614&in_out_flag=1', 'sourceFrom': 'GN'}, {'id': '15F18AA57DB5431557E0B345EA0F58B9B699', 'useP2P': False, 'duration': 36.103, 'size': 2049058, 'type': 'avc1', 'encodingOption': {'id': '720P_01', 'name': '720p', 'profile': 'MAIN', 'width': 1280, 'height': 694, 'isEncodingComplete': 'true', 'completeProgress': '100'}, 'bitrate': {'video': 451.0, 'audio': 0.0}, 'p2pMetaUrl': '', 'p2pUrl': '', 'source': 'https://b01-kr-naver-vod.pstatic.net/blog/a/read/v2/VOD_ALPHA/blog_2022_01_20_1380/b028508f-794c-11ec-87b4-48df37269fd0.mp4?_lsu_sa_=6c95a0fc810e6076a7d2c5726d855bbb4e8d35482007bff0343785c5a74631458a274a716da5500080eb3fe215321b5dc749ebf5236dc5a145c3acfa79fa70c91f2ebd9410805c9986d88d5bc605434d&in_out_flag=1', 'sourceFrom': 'GN'}, {'id': '970FF64502C4700AA795708E9389CC236CE0', 'useP2P': False, 'duration': 36.103, 'size': 548453, 'type': 'avc1', 'encodingOption': {'id': '270P_01', 'name': '270p', 'profile': 'BASE', 'width': 480, 'height': 260, 'isEncodingComplete': 'true', 'completeProgress': '100'}, 'bitrate': {'video': 120.0, 'audio': 0.0}, 'p2pMetaUrl': '', 'p2pUrl': '', 'source': 'https://b01-kr-naver-vod.pstatic.net/blog/a/read/v2/VOD_ALPHA/blog_2022_01_20_896/b0289eb0-794c-11ec-87b4-48df37269fd0.mp4?_lsu_sa_=671519fc61c56ca6d1dd95a069a549b37e353f387c0f4f2f3c8799cc077a3de58526fa346a85670ed0f93f12a5374b69b945e95f4c619938c41c86aba5cc8c73192cbaccdfe943e3ca63dd9e6a039ccd&in_out_flag=1', 'sourceFrom': 'GN'}, {'id': '99119F00F219891B5797DED0B06BBC892E14', 'useP2P': False, 'duration': 36.103, 'size': 3876367, 'type': 'avc1', 'encodingOption': {'id': '1080P_01', 'name': '1080p', 'profile': 'HIGH', 'width': 1920, 'height': 1040, 'isEncodingComplete': 'true', 'completeProgress': '100'}, 'bitrate': {'video': 856.0, 'audio': 0.0}, 'p2pMetaUrl': '', 'p2pUrl': '', 'source': 'https://b01-kr-naver-vod.pstatic.net/blog/a/read/v2/VOD_ALPHA/blog_2022_01_20_13/b028c5c1-794c-11ec-87b4-48df37269fd0.mp4?_lsu_sa_=6ee598fe31f36b96b9db15b46c552ab4be383138c6042f0036d71bcf071e3ae597252a6b62456007d07933b2483c6b8dfecd3e94abe649f41d623405278479ea7e4e78bd77e1a468f941b35e5ed901d6&in_out_flag=1', 'sourceFrom': 'GN'}, {'id': 'C11EB8D3CCCC2E8A720DBB9EAD3D6B3A7A4A', 'useP2P': False, 'duration': 36.103, 'size': 299641, 'type': 'avc1', 'encodingOption': {'id': '144P_01', 'name': '144p', 'profile': 'BASE', 'width': 256, 'height': 140, 'isEncodingComplete': 'true', 'completeProgress': '100'}, 'bitrate': {'video': 65.0, 'audio': 0.0}, 'p2pMetaUrl': '', 'p2pUrl': '', 'source': 'https://b01-kr-naver-vod.pstatic.net/blog/a/read/v2/VOD_ALPHA/blog_2022_01_20_608/b02913e2-794c-11ec-87b4-48df37269fd0.mp4?_lsu_sa_=62b5c3fc011c6b86d4d2d5d76d65bcb25e1a3978c6032fc43bb761c177b83725b1227a8e69e5620750b93ee2583a0b9dd0533ec4b2156990a6b12cd7929d5427f4297d82d5da46930b5474fcd78d1298&in_out_flag=1', 'sourceFrom': 'GN'}]
#
# for item in testList:
# 	print(item)

# print(json.loads(jsonUrl))
# https://b01-kr-naver-vod.pstatic.net/blog/a/read/v2/VOD_ALPHA/blog_2022_01_20_13/b028c5c1-794c-11ec-87b4-48df37269fd0.mp4?_lsu_sa_=6a5565f431e06de6d2de156d6185efb58ec637e8c0003f913d37e9cde7683aa5f923eaea69f5270880a232d2e43b4b1b8acc3a5dabb6db69021502fa55a98357cfd88f75b4fe27b6b6bdc3233c98a074&in_out_flag=1

# 3A9F771DE6BF870FA8FD61CB817EEFA6FF66
# V12969c243f6c0ff5f7e3021dc9e8493b2099dd964be05e58c6e1c941b1cb09d2c3ab021dc9e8493b2099