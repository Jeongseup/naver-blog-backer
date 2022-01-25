import requests, re, time
from threading import Thread
# from progressbar import ProgressBar
import os

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
		global naverId
		naverId = _targetId

		# init
		self.postUrlList = []
		self.isDevMode = isDevMode
		self.threadNum = threadNum

		# init check
		if self.isForeignId():
			print("[INIT ERROR] 입력하신 ID로 검색된 포스트가 없습니다. 프로그램을 종료합니다.")

	# ============================================================================================

	def getTotalPosts(self):
		return len(self.postUrlList)

	# ============================================================================================

	def run(self):
		global naverId, postsNum, curPost, crawlingProgressBar
		initTime = time.time()
		startPage = 1
		urlPrefix = "https://blog.naver.com/" + naverId + "/"
		postIdList = self.getEntirePostIdList(startPage)
		postsNum = len(postIdList)
		print("[ Getting post address list in {0:0.2f}s ]".format((time.time() - initTime)))
		print("[ Total posts : {}posts. Backup begins... ]".format(postsNum))
		self.copyCSSfile()
		crawlingProgressBar = ProgressBar(max_value=postsNum, redirect_stdout=True)
		crawlingProgressBar.update(curPost)

		divListSize = postsNum // self.threadNum
		threads = self.makeCrawlingThreads(postIdList)

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

	def getEntirePostIdList(self, category=0):

		while True:
			try:
				partialList = self.getPostIdListViaPage(page)
				if page == 1 or page % 20 == 0:
					print("Getting post number list in page {}...".format(page))
				if partialList == [] or self.isDuplicateList(pastIdList, partialList):
					return postIdList
				postIdList.extend(partialList)
				pastIdList = partialList
				page += 1
			except NonePostListException:
				return postIdList



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
