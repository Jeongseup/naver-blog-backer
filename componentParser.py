from blogPost import BlogPost


class ComponentParser(object):
	# SE3Component is class that based on str, found on soup(= HTML TAG)
	# parser progress counter
	counter = 0

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
			pass

		# 구분선 컴포넌트 체크
		elif "se-component se-horizontalLine" in componentSting:
			return self.parsingHorizontalLine()

		# 일정 컴포넌트 체크
		elif "se-component se-schedule" in componentSting:
			pass

		# 코드 컴포넌트 체크
		elif "se-component se-code" in componentSting:
			pass

		# 라이브러리 컴포넌트 체크
		elif "se-component se-material" in componentSting:
			pass

		# 이미지 컴포넌트 체크
		elif "se-component se-image" in componentSting:
			pass

		# 스티커 컴포넌트 체크
		elif "se-component se-sticker" in componentSting:
			pass

		# 비디오 컴포넌트 체크
		elif "se-component se-video" in componentSting:
			pass

		# 파일 컴포넌트 체크
		elif "se-component se-file" in componentSting:
			pass

		# 지도 컴포넌트 체크
		elif "se-component se-placesMap" in componentSting:
			pass

		# 아웃고잉링크 컴포넌트 체크
		elif "se-component se-oglink" in componentSting:
			return self.parsingOglink()

		# 수식 컴포넌트 체크
		elif "se-component se-formula" in componentSting:
			pass

		# 테이블 컴포넌트 체크
		elif "se-component se-table" in componentSting:
			pass

		else:
			print('find unknown tag\n' + str(self.component))

		self.printDevMessage("== postSetup is clear == ")
		return ''

	# ============================================================================================

	# parsing function for main title
	def parsingTitle(self):
		self.printDevMessage("== parsingTitle execution ==")

		txt = ''
		for content in self.component.select('.se-title-text'):
			txt += self.wrappingText(content.text, isTitle=True)

		self.printDevMessage("== title is clear == ")
		return txt

	# parsing function for section title
	def parsingSectionTitle(self):
		self.printDevMessage("== parsingSectionTitle execution ==")

		txt = ''
		for content in self.component.select('.se-module-text'):
			for pTag in content.select('p'):
				txt += pTag.text
				txt += self.endLine

		self.printDevMessage("== text is clear == ")
		return txt

	# parsing function for text
	def parsingText(self):
		self.printDevMessage("== parsingText execution ==")

		txt = ''
		for content in self.component.select('.se-module-text'):
			for pTag in content.select('p'):
				txt += pTag.text
				txt += self.endLine

		self.printDevMessage("== text is clear == ")
		return txt

	# parsing function for text
	def parsingHorizontalLine(self):
		self.printDevMessage("== parsingHorizontalLine execution ==")

		txt = ''
		for content in self.component.select('.se-hr'):
			txt += '---'
			txt += self.endLine

		self.printDevMessage("== horizontal line is clear == ")
		return txt


	def parsingOglink(self):
		self.printDevMessage("== parsingHorizontalLine execution ==")

		txt = ''

		oglinkTitle = self.component.select('.se-oglink-title')[0].text
		oglinkSummary = self.component.select('.se-oglink-summary')[0].text
		oglink = self.component.select('.se-oglink-info')[0]['href']

		if oglinkTitle is '':
			oglinkTitle = "No Title"

		txt += f'[{oglinkTitle}]({oglink})' + ' : '
		txt += oglinkSummary
		txt += self.endLine

		self.printDevMessage("== oglink is clear == ")
		return txt


# ============================================================================================

import os

# parsing function for code

if __name__ == '__main__':

	testPostUrl = "https://blog.naver.com/thswjdtmq4/222626338613"
	c1 = BlogPost(testPostUrl, False)
	c1.postSetup()
	rawComponents = c1.postInframeSoup.select('div.se-component')

	with open('test.md', "w", encoding='utf-8') as fp:

		data = ''

		for i, rawComponent in enumerate(rawComponents):
			if i == 0:
				# 처음에는 무조건 헤더부분의 다큐먼트 타이틀이 나온다.
				headComponent = rawComponent
				data += ComponentParser(headComponent, isDevMode=False).parsingTitle()
			else:
				data += ComponentParser(rawComponent).parsing()

		fp.write(data)

# print('텍스트 파싱 결과 ', data)
