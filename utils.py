from datetime import datetime, timedelta
from urllib import request, parse
from html import unescape
import re, os, errno, json


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


# util for folder check
def checkBackupDir(dirName):
	try:
		# 정해진 위치에 폴더가 존재하지 않은 경우
		if not (os.path.isdir(dirName)):
			os.makedirs(os.path.join(dirName))

	# 폴더 생성 실패
	except OSError as e:
		if e.errno != errno.EEXIST:
			print(dirName + '폴더를 생성하지 못하였습니다.')
			raise
		return False
	return True


def removeSpecialChar(dirName):
	windowsDir = re.compile('[\?:|<|>|\||\*|\"\/]')  # Special Chars that cannot use in Windows' Directory Name
	fixedDirName = windowsDir.sub('', dirName)
	return fixedDirName


# util for saving images
def saveImage(url, path):
	try:
		link = parse.quote(url, safe=':/?-=')
		request.urlretrieve(link, path)
	except Exception as e:
		print(e)
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
	except Exception as e:
		print(e)
		return ''

# util for saving video
def saveVideo(url, path):
	try:
		request.urlretrieve(url, path)
	except Exception as e:
		print(e)
		return False
	return True
