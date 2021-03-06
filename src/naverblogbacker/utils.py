from datetime import datetime, timedelta
from urllib import request, parse
from html import unescape
from requests.utils import unquote
import re
import os
import errno
import json


# util for getPostDate
def isRelativePostDate(postDate):
	if "전" in postDate:
		return True
	else:
		return False


# util for getPostDate
def getRelativePostDate(relativeDate):
	# eg. "방금 전", "3분전", "10시간 전"...
	curTime = datetime.now()
	if relativeDate == "방금 전":
		pass
	elif "분 전" in relativeDate:
		elapsedMin = re.search("[0-9]+", relativeDate).group()
		elapsedMin = int(elapsedMin)
		curTime = curTime - timedelta(minutes=elapsedMin)
	elif "시간 전" in relativeDate:
		elapsedHour = re.search("[0-9]+", relativeDate).group()
		elapsedHour = int(elapsedHour)
		curTime = curTime - timedelta(hours=elapsedHour)
	curTime = str(curTime)
	timeRegex = re.compile("[0-9]+-[0-9]+-[0-9]+ [0-9]+:[0-9]+")
	curTime = timeRegex.search(curTime).group()
	return curTime


# util for folder empty check
def isEmptyDirectory(dirPath):
	if os.path.exists(dirPath) and os.path.isdir(dirPath):
		if not os.listdir(dirPath):
			print("[MESSAGE] Directory is empty, Start backup your blog :)")
			return True
		else:
			raise Exception("[ERROR] Given Directory don't exists")
			return False
	else:
		raise Exception("[ERROR] Given Directory don't exists")
		return False


# utils for create post folder
def createNewDirectory(dirPath):
	try:
		# 폴더가 존재하지 않으면
		if not (os.path.isdir(dirPath)):
			# 포스트 폴더
			os.makedirs(os.path.join(dirPath))

			# 포스트 소스 폴더
			assetPath = dirPath + "/" + "asset"
			os.makedirs(os.path.join(assetPath))
		else:
			pass
	except OSError as e:
		if e.errno != errno.EEXIST:
			raise Exception(f'[ERROR] {dirPath} 폴더를 생성하지 못 했습니다.')
		return False
	return True


# util for saving images
def saveImage(url, path):
	try:
		link = parse.quote(url, safe=':/?-=')
		request.urlretrieve(link, path)
	except Exception as e:
		return False
	return True


# util for script tag parse
def parsingScriptTag(stringData):
	unescapedString = unescape(stringData)
	return json.loads(unescapedString.replace('\\"', ""))


# utils for finding out video source
def getVideoSource(jsonData):
	try:
		videoId = jsonData['vid']
		videoInkey = jsonData['inkey']
		videoOriginalWidth = jsonData['originalWidth']

		jsonUrl = 'https://apis.naver.com/rmcnmv/rmcnmv/vod/play/v2.0/' + videoId + '?key=' + videoInkey

		with request.urlopen(jsonUrl) as url:
			videoList = json.loads(url.read().decode())['videos']['list']

			for video in videoList:
				if str(video['encodingOption']['width']) == str(videoOriginalWidth):
					return video['source']

			# 만약 videoOriginalWidth가 존재하지 않는다면 1080P로 처리한다.
			return videoList[2]['source']

	except Exception as e:
		print(f'[ERROR] {videoId}의 미디어 소스를 찾지 못하였습니다.')
		return ''


# util for saving video
def saveVideo(url, path):
	try:
		request.urlretrieve(url, path)
	except Exception as e:
		# print(e)
		return False
	return True


# util for get post title list
def getTotalCount(targetId):
	postTitleListUrl = f'https://blog.naver.com/PostTitleListAsync.naver?blogId={targetId}'
	try:
		res = request.urlopen(postTitleListUrl).read().decode()
		# json parsing
		jsonData = json.loads(unescape(res).replace('\\', ''))

		return int(jsonData['totalCount'])

	except Exception as e:
		return str(e)


# util for get post title list
def getPostTitleList(targetId, currentPage, categoryNo=0):
	postTitleListUrl = f'https://blog.naver.com/PostTitleListAsync.naver?blogId={targetId}&viewdate=&currentPage={currentPage}&categoryNo={categoryNo}&parentCategoryNo=0&countPerPage=30'

	try:
		res = request.urlopen(postTitleListUrl).read().decode()
		# json parsing
		jsonData = json.loads(unescape(res).replace('\\', ''))

		return jsonData['postList']

	except Exception as e:
		print(e)
		return None


# util for parsing post data
def parsingPostTitle(post):
	tempObj = dict()

	if isRelativePostDate(post['addDate']):
		tempObj['date'] = getRelativePostDate(post['addDate'])
	else:
		tempObj['date'] = post['addDate']

	tempObj['title'] = unquote(post['title'], encoding='utf-8').replace('+', ' ')
	tempObj['logNo'] = post['logNo']

	return tempObj
