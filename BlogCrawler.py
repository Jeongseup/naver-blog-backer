from progressbar import ProgressBar
from threading import Thread
import time

from utils import getPostTitleList, getTotalCount, parsingPostTitle

# Global Variables for Thread
targetId = ""
curPost = 1
postsNum = 0
crawlingProgressBar = None


class BlogCrawler:
	def __init__(self, _targetId, threadNum=4, isDevMode=False):
		# 개발 편의
		self.isDevMode = isDevMode

		# use global variable
		global targetId
		targetId = _targetId

		# init
		self.postList = []
		self.isDevMode = isDevMode
		self.threadNum = threadNum
		self.totalCount = None

		# init check
		if self.isForeignId():
			print("[INIT ERROR] 입력하신 ID로 검색된 포스트가 없습니다. 프로그램을 종료합니다.")

	# ============================================================================================

	# 개발편의용 프린트 함수
	def printDevMessage(self, message):
		if self.isDevMode:
			print("[DEV MODE] " + message, end='\n')

	# ============================================================================================

	def getPostList(self):
		self.printDevMessage("getPostList execution")

		totalCount = getTotalCount(targetId)
		# 전체 페이지 개수를 가져오는 currentPage수로 나눈 나머지 +1 만큼하면 모든 페이지 아이템을 가져올 수 있다.
		pages = (int(totalCount) % 30) + 1

		try:
			result = list()
			for i in range(1, pages):
				print(f'Getting post number list in page {i} in {pages}')
				tempPostList = getPostTitleList(targetId)

				# 내가 쓴 글이 아닌 공유 글 제외
				tempPostList = list(filter(lambda p: p['searchYn'] == 'true', tempPostList))

				for post in tempPostList:
					# 필요한 데이터만을 추출하고 appending
					result.append(parsingPostTitle(post))

			self.printDevMessage("clear")
			return result
		except Exception as e:
			print(e)
			return None

	# ============================================================================================

	def run(self):
		global naverId, postsNum, curPost, crawlingProgressBar
		initTime = time.time()

		print("[ Getting post address list in {0:0.2f}s ]".format((time.time() - initTime)))
		print("[ Total posts : {}posts. Backup begins... ]".format(postsNum))

		crawlingProgressBar = ProgressBar(max_value=postsNum, redirect_stdout=True)
		crawlingProgressBar.update(curPost)

		divListSize = postsNum // self.threadNum
		threads = self.makeCrawlingThreads(self.postList)

		self.startThreads(threads)

		print("[ {0} Posts backup complete in {1:0.2f}s ]".format(postsNum, time.time() - initTime))

	def startThreads(self, threads):
		for thread in threads:
			thread.start()

		for thread in threads:
			thread.join()

	def makeCrawlingThreads(self, postIdList):
		global postsNum
		threads = list()
		divListSize = postsNum // self.threadNum
		lastIndex = self.threadNum - 1

		for index in range(self.threadNum):
			if index == lastIndex:
				partialList = postIdList[index * divListSize:]
			else:
				partialList = postIdList[index * divListSize: (index + 1) * divListSize]
			threads.append(NaverBlogPostCrawlThread(partialList))
		return threads

# class BackerThread(Thread):
# 	def __init__(self, postList, isDevMode=False):
# 		Thread.__init__(self)
# 		self.postList = postList
# 		self.isDevMode = isDevMode
#
# 	def run(self):
# 		global curPost, postsNum, naverId, crawlingProgressBar
# 		for postUrl in self.postList:
# 			if self.isDevMode:
# 				print("{}/{}".format(curPost, postsNum))
# 			curPost += 1
# 			crawlingProgressBar.update(curPost)
# 			urlPrefix = "https://blog.naver.com/" + naverId + "/"
# 			postingCrawler = NaverBlogPostCrawler(urlPrefix + postUrl, self.isDevMode)
# 			postingCrawler.run()
#
#
