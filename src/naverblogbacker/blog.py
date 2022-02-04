from tqdm import tqdm
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

			for i in tqdm(range(1, 2)):
				self.printDevMessage(f'Getting post number list in page {i} in {pages}')
				tempPostList = getPostTitleList(self.targetId, i)

				# 내가 쓴 글이 아닌 공유 글 제외
				tempPostList = list(filter(lambda p: p['searchYn'] == 'true', tempPostList))
				print(f'공유한 글을 제외한 {len(tempPostList)}개의 포스트가 준비되었습니다.')

				for post in tempPostList:
					# 필요한 데이터만을 추출하고 appending
					myPostList.append(parsingPostTitle(post))

			# post setup
			self.totalCount = totalCount
			self.myTotalCount = len(myPostList)
			self.postList = myPostList

			self.printDevMessage(f'[MESSAGE] Find out your {len(myPostList)} posts!')

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


	def backlinking(self):
		urlPrefix = f'https://blog.naver.com/PostView.naver?blogId={self.targetId}&logNo='

		if len(self.postList) == 0:
			raise(Exception(f'[ERROR] postList 함수가 정상적으로 실행되지 않았습니다.'))

		for post in tqdm(self.postList):
			# 먼저 빈 폴더에 현재 진행할 포스트 로그넘버로된 폴더생성
			tempBackLink = urlPrefix + "/" + post['logNo']

			filePath = dirPath + '/' + 'word.md'
			ComponentParser.assetPath = dirPath + '/asset'
			rawComponents = self.postInframeSoup.select('div.se-component')

			try:
				with open(filePath, mode='w', encoding='utf-8') as fp:
					# 작성될 텍스트 데이터 초기화
					data = ''
					for i, component in enumerate(rawComponents):
						if i == 0:
							# 처음에는 무조건 헤더부분의 다큐먼트 타이틀이 나온다.
							data += ComponentParser(component, isDevMode=self.isDevMode).parsingTitle()
							continue

						data += ComponentParser(component, skipSticker=self.isDevMode).parsing()

						# last loop에서는 해시태그까지 추가해준다.
						if i == (len(rawComponents) - 1):
							txt = '해시태그 : '
							for hashTag in ComponentParser.hashTagList:
								txt += hashTag

							data += ' ' + txt
					# 작성
					fp.write(data)

				if ComponentParser.errorCounter != 0:
					BlogPost.errorCount += 1

				# 포스트 백업 후 클래스 변수 초기화
				ComponentParser.hashTagList = []
				ComponentParser.counter = 0
				ComponentParser.errorCount = 0

				return True

			except Exception as e:
				print(e)
				return False

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

