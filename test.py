
# Global Variables for Thread
naverId = "testId"
curPost = 1
postsNum = 0
crawlingProgressBar = None

class BlogCrawler:
	def __init__(self, _naverId, threadNum=4, isDevMode=False):
		global naverId
		print(naverId, "test")
		naverId = _naverId
		print(naverId)

		self.postUrlList = []
		self.isDevMode = isDevMode
		self.threadNum = threadNum

	def getPostList(self):
		pass

if __name__ == '__main__':
	print('main', naverId)
	c1 = BlogCrawler("thswjdtmq4")