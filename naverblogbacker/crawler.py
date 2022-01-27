from tqdm import tqdm
import time
from naverblogbacker.utils import getPostTitleList, getTotalCount, parsingPostTitle, createNewDirectory
from naverblogbacker.post import BlogPost

class BlogCrawler:
	def __init__(self, targetId, dirPath, isDevMode=False):
		# init check
		if isinstance(getTotalCount(targetId), str):
			print("[INIT ERROR] 입력하신 ID로 검색된 포스트가 없습니다. 프로그램을 종료합니다.")
			return -1

		# 개발 편의
		self.isDevMode = isDevMode

		# init variables
		self.targetId = targetId
		self.dirPath = dirPath
		self.postList = []
		self.totalCount = None
		self.myTotalCount = None

		# setup
		self.getPostList()

	# ============================================================================================

	# 개발편의용 프린트 함수
	def printDevMessage(self, message):
		if self.isDevMode:
			print("[DEV MODE] " + message, end='\n')

	# ============================================================================================

	# setup
	def getPostList(self):
		self.printDevMessage("getPostList execution")

		totalCount = getTotalCount(self.targetId)
		# 전체 페이지 개수를 가져오는 currentPage수로 나눈 나머지 +1 만큼하면 모든 페이지 아이템을 가져올 수 있다.
		pages = (totalCount // 30) + 1

		try:
			myPostList = list()

			for i in tqdm(range(1, pages + 1)):
				# print(f'Getting post number list in page {i} in {pages}')
				tempPostList = getPostTitleList(self.targetId, i)

				# 내가 쓴 글이 아닌 공유 글 제외
				tempPostList = list(filter(lambda p: p['searchYn'] == 'true', tempPostList))
				# print(f'{len(tempPostList)}개의 포스트 리스트를 준비하였습니다.')
				for post in tempPostList:
					# 필요한 데이터만을 추출하고 appending
					myPostList.append(parsingPostTitle(post))

			# post setup
			self.totalCount = totalCount
			self.myTotalCount = len(myPostList)
			self.postList = myPostList

			self.printDevMessage("clear")

		except Exception as e:
			print(e)

	# ============================================================================================

	def run(self):
		global myPath
		initTime = time.time()
		print("[ Getting post address list in {0:0.2f}s ]".format((time.time() - initTime)))
		print("[ Total posts : {}posts. Backup begins... ]".format(self.myTotalCount))


		urlPrefix = f'https://blog.naver.com/{self.targetId}/'
		for post in tqdm(self.postList):
			# 먼저 빈 폴더에 현재 진행할 포스트 로그넘버로된 폴더생성
			tempPostDir = myPath + "/" + post['logNo']

			if createNewDirectory(tempPostDir):

			# 포스트 크롤링 시작
			tempPostUrl = urlPrefix + post['logNo']
			tempPost = BlogPost(tempPostUrl, isDevMode=False)
			tempPost.run()

		print("[ {0} Posts backup complete in {1:0.2f}s ]".format(self.myTotalCount, time.time() - initTime))