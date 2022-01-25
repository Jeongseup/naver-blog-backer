import requests, re, time
from threading import Thread
# from progressbar import ProgressBar
import os, shutil

# Global Variables for Thread
naverId = ""
curPost = 1
postsNum = 0
crawlingProgressBar = None


class BlogCrawler:
	def __init__(self, _naverId, threadNum=4, isDevMode=False):
		global naverId
		naverId = _naverId
		self.postUrlList = []
		self.isDevMode = isDevMode
		self.threadNum = threadNum

	def getPostList(self):
		pass

	def copyCSSfile(self):
		packagePath = os.path.dirname(NaverBlogPostCrawler.__file__)
		cssPath = str(packagePath) + "/blogstyle.css"
		shutil.copyfile(cssPath, "./blogstyle.css")

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

	def getEntirePostIdList(self, startPage):
		page = startPage
		postIdList = []
		pastIdList = []
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

	def isDuplicateList(self, postNumList1, postNumList2):
		if len(postNumList1) == len(postNumList2):
			for index in range(len(postNumList1)):
				if postNumList1[index] != postNumList2[index]:
					return False
			return True
		else:
			return False

	def getPostIdListViaPage(self, pageNum):
		getPostList = "https://blog.naver.com/" \
					  "PostList.nhn?from=postList&" \
					  "blogId={}&currentPage={}".format(naverId, pageNum)
		postListHtml = requests.get(getPostList).text
		postListSoup = BeautifulSoup(postListHtml, "html5lib")
		postNumTags = re.search("var tagParam .*\';", str(postListSoup)).group()
		postNumList = re.findall('[0-9]+', postNumTags)
		if postNumList == None:
			raise NonePostListException
		return postNumList


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
# class NonePostListException(Exception):
# 	pass
