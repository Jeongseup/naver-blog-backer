from urllib import request

url = 'https://blogattach.naver.com/f461e85c4e7f7ecbe2046e536b85ff8f2f748b02/20220120_88_blogfile/thswjdtmq4_1642613221301_Uts8Ix_psd/mobile.psd'

print(url.split('/')[-1])

'''
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
'''