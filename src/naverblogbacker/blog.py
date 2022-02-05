from tqdm import trange, tqdm
from .post import BlogPost
from .utils import getPostTitleList, getTotalCount, parsingPostTitle, createNewDirectory

class BlogCrawler(object):
	errorPost = 0

	def __init__(self, targetId, skipSticker=True, isDevMode=False):
		# init check
		if isinstance(getTotalCount(targetId), str):
			print("[INIT ERROR] 입력하신 ID로 검색된 포스트가 없습니다. 프로그램을 종료합니다.")
			exit(-1)

		# 개발 편의
		self.isDevMode = isDevMode

		# init variables
		self.targetId = targetId
		self.postList = []
		self.totalCount = None
		self.myTotalCount = None
		self.skipSticker = skipSticker

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

			for i in trange(1, pages + 1):
				# self.printDevMessage(f'Getting post number list in page {i} in {pages}')
				tempPostList = getPostTitleList(self.targetId, i)

				# 내가 쓴 글이 아닌 공유 글 제외
				tempPostList = list(filter(lambda p: p['searchYn'] == 'true', tempPostList))
				# print(f'공유한 글을 제외한 {len(tempPostList)}개의 포스트가 준비되었습니다.')

				for post in tempPostList:
					# 필요한 데이터만을 추출하고 appending
					myPostList.append(parsingPostTitle(post))

			# post setup
			self.totalCount = totalCount
			self.myTotalCount = len(myPostList)
			self.postList = myPostList

			self.printDevMessage(f' [MESSAGE] Find out your {len(myPostList)} posts!\n')

		except Exception as e:
			print(e)

	# ============================================================================================

	def crawling(self, dirPath):
		urlPrefix = f'https://blog.naver.com/{self.targetId}/'

		if len(self.postList) == 0:
			raise(Exception(f'[ERROR] postList 함수가 정상적으로 실행되지 않았습니다.'))

		for post in tqdm(self.postList):
			# 먼저 빈 폴더에 현재 진행할 포스트 로그넘버로된 폴더생성
			tempPostDir = dirPath + "/" + post['logNo']

			if not createNewDirectory(tempPostDir):
				raise Exception(f"[ERROR] : {post['logNo']}포스트 폴더가 정상적으로 생성되지 않았습니다.")

			# 포스트 크롤링 시작
			tempPostUrl = urlPrefix + post['logNo']
			tempPost = BlogPost(tempPostUrl, isDevMode=self.isDevMode)
			tempPost.run(dirPath=tempPostDir)

			if BlogPost.errorCount != 0:
				BlogCrawler.errorPost += 1

			# 포스트 백업 후 클래스 변수 초기화
			BlogPost.errorCount = 0


	def backlinking(self, dirPath):
		urlPrefix = f'https://blog.naver.com/PostView.naver?blogId={self.targetId}&logNo='
		filePath = dirPath + '/' + 'backlink.txt'

		if len(self.postList) == 0:
			raise(Exception(f'[ERROR] postList 함수가 정상적으로 실행되지 않았습니다.'))

		try:
			with open(filePath, mode='w', encoding='utf-8') as fp:
				data = ''

				pbar = tqdm(self.postList)
				for post in pbar:
					txt = ''

					txt += post['title']
					txt += '\n'

					txt += urlPrefix + post['logNo']
					txt += '\n\n'

					data += txt
					pbar.set_description(" Processing")

				fp.write(data)

			return True
		except Exception as e:
			print(e)
			return False
