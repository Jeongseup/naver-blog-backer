from blogPost import BlogPost


class ComponentParser(object):
	# SE3Component is class that based on str, found on soup(= HTML TAG)
	# parser progress counter
	counter = 0
	hashTagList = []

	def __init__(self, component, titleType="##", subTitleType="###", skipSticker=True, isDevMode=True):
		# user setting
		self.component = component
		self.title = titleType
		self.subTitle = subTitleType
		self.endLine = '\n\n'
		self.skipSticker = skipSticker

		#  for development function
		self.isDevMode = isDevMode

	# ============================================================================================

	# 개발편의용 프린트 함수
	def printDevMessage(self, message):
		if self.isDevMode:
			print("[DEV MODE] " + message, end='\n')

	# text wrapping for markdown style
	def wrappingText(self, txt, isTitle=False):
		if (isTitle):
			return self.title + ' ' + txt.strip() + '' + self.endLine
		else:
			return self.subTitle + ' ' + txt.strip() + '' + ''

	# ============================================================================================

	# 파서 작동
	@property
	def parsing(self):
		# self.printDevMessage(f"== parsing execution, current order is {ComponentParser.counter} ==")
		self.printDevMessage(f"== parsing execution ==")

		componentSting = str(self.component)

		# 텍스트 컴포넌트 체크
		if "se-component se-text" in componentSting:
			return self.parsingText()

		# 소제목 컴포넌트 체크
		elif "se-component se-sectionTitle" in componentSting:
			return self.parsingSectionTitle()

		# 인용구 컴포넌트 체크
		elif "se-component se-quotation" in componentSting:
			return self.parsingQuotation()

		# 구분선 컴포넌트 체크
		elif "se-component se-horizontalLine" in componentSting:
			return self.parsingHorizontalLine()

		# 일정 컴포넌트 체크
		elif "se-component se-schedule" in componentSting:
			return ''

		# 코드 컴포넌트 체크
		elif "se-component se-code" in componentSting:
			return self.parsingCode()

		# 라이브러리 컴포넌트 체크
		elif "se-component se-material" in componentSting:
			return ''

		# 이미지 컴포넌트 체크
		elif "se-component se-image" in componentSting:
			return ''

		# 스티커 컴포넌트 체크
		elif "se-component se-sticker" in componentSting:
			return ''


		# 비디오 컴포넌트 체크
		elif "se-component se-video" in componentSting:
			return ''


		# 파일 컴포넌트 체크
		elif "se-component se-file" in componentSting:
			return ''

		# 지도 컴포넌트 체크
		elif "se-component se-placesMap" in componentSting:
			return ''

		# 아웃고잉링크 컴포넌트 체크
		elif "se-component se-oglink" in componentSting:
			return self.parsingOglink()

		# 수식 컴포넌트 체크
		elif "se-component se-formula" in componentSting:
			print('지원하지 않는 컴포넌트입니다.')
			return ''

		# 테이블 컴포넌트 체크
		elif "se-component se-table" in componentSting:
			print('지원하지 않는 컴포넌트입니다.')
			return ''

		else:
			print('find unknown tag\n' + str(self.component))

	# ============================================================================================

	# parsing function for main title
	def parsingTitle(self):
		self.printDevMessage("== parsingTitle execution ==")

		txt = ''
		for content in self.component.select('.se-title-text'):
			txt += self.wrappingText(content.text, isTitle=True)

		self.printDevMessage("clear")
		return txt

	# parsing function for section title
	def parsingSectionTitle(self):
		self.printDevMessage("== parsingSectionTitle execution ==")

		txt = ''
		for content in self.component.select('.se-module-text'):
			for pTag in content.select('p'):
				txt += pTag.text
				txt += self.endLine

		self.printDevMessage("clear")
		return txt

	# parsing function for text & hashtag
	def parsingText(self):
		self.printDevMessage("== parsingText execution ==")

		txt = ''
		for content in self.component.select('.se-module-text'):
			for pTag in content.select('p'):

				if '#' in pTag.text:
					ComponentParser.hashTagList.append(pTag.text)
					continue

				txt += pTag.text
				txt += self.endLine

		self.printDevMessage("clear")
		return txt

	# parsing function for text
	def parsingHorizontalLine(self):
		self.printDevMessage("== parsingHorizontalLine execution ==")

		txt = ''
		for content in self.component.select('.se-hr'):
			txt += '---'
			txt += self.endLine

		self.printDevMessage("clear")
		return txt

	# parsing function for oglink
	def parsingOglink(self):
		self.printDevMessage("== parsingHorizontalLine execution ==")

		txt = ''

		oglinkTitleTag = self.component.select('.se-oglink-title')
		oglinkSummaryTag = self.component.select('.se-oglink-summary')
		oglink = self.component.select('.se-oglink-info')[0]['href']


		if len(oglinkTitleTag) == 0:
			oglinkTitle = "No Title"
		else:
			oglinkTitle = oglinkTitleTag[0].text

		if  len(oglinkSummaryTag) == 0:
			oglinkSummary = ''
		else:
			oglinkSummary = oglinkSummaryTag[0].text


		txt += f'[{oglinkTitle}]({oglink})' + ' : '
		txt += oglinkSummary
		txt += self.endLine

		self.printDevMessage("clear")
		return txt

	# parsing function for code
	def parsingCode(self):
		self.printDevMessage("== parsingCode execution ==")

		txt = ''
		for content in self.component.select('.se-code-source'):
			# 앞, 뒤 엔터 제거
			codeSnippet = content.text[1: -1]
			txt += f'```\n{codeSnippet}\n```'
			txt += self.endLine

		self.printDevMessage("clear")
		return txt

	# parsing function for quotation
	def parsingQuotation(self):
		self.printDevMessage("== parsingQuotation execution ==")

		txt = ''

		quotationSiteTag = self.component.select('.se-cite')

		if  len(quotationSiteTag) == 0:
			quotationSite = "No Site"
		else:
			quotationSite = quotationSiteTag[0].text

		for pTag in self.component.select('.se-quote'):
			txt += f'> {pTag.text}'
			txt += self.endLine

		txt += f'출처 : {quotationSite}'
		txt += self.endLine

		self.printDevMessage("clear")
		return txt

	# parsing function for image
	def parsingImage(self):
		self.printDevMessage("== parsingImage execution ==")

		txt = ''

		imageCaptionTag = self.component.select('.se-caption')
		if len(imageCaptionTag) == 0:
			imageCaption = ''
		else:
			imageCaption = imageCaptionTag[0].text

		for imageTag in self.component.select('img'):

			imageUrl = imageTag['data-lazy-src']

			txt += '![' + './img/' + str(self.counter) + '.png' + ']('
			txt += './img/' + str(self.counter) + '.png' + ')'
			txt += '\n'


			# if not utils.saveImage(url, self.folder_path + '/img/' + str(self.counter) + '.png'):
			# 	print('\t' + str(content) + ' 를 저장합니다.')
			# else:
			# 	self.counter += 1

		txt += self.endline
		return txt

# ============================================================================================


if __name__ == '__main__':

	testPostUrl = "https://blog.naver.com/thswjdtmq4/222626338613"
	c1 = BlogPost(testPostUrl, False)
	c1.postSetup()
	rawComponents = c1.postInframeSoup.select('div.se-component')

	with open('hashtag.md', "w", encoding='utf-8') as fp:

		data = ''

		for i, rawComponent in enumerate(rawComponents):

			if i == 0:
				# 처음에는 무조건 헤더부분의 다큐먼트 타이틀이 나온다.
				headComponent = rawComponent
				data += ComponentParser(headComponent, isDevMode=False).parsingTitle()
				continue

			data += ComponentParser(rawComponent).parsing

			if i == len(rawComponents) - 1:
				txt = '해시태그 : '
				for hashTag in ComponentParser.hashTagList:
					txt += hashTag

				data += ' ' + txt

		fp.write(data)

	ComponentParser.hashTagList = []
	print(ComponentParser.hashTagList)

# print('텍스트 파싱 결과 ', data)
