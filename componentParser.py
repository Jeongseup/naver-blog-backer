from blogPost import BlogPost


class ComponentParser(object):
	# SE3Component is class that based on str, found on soup(= HTML TAG)
	# parser progress counter
	counter = 0

	def __init__(self, component, titleType="##", subTitleType="###", skipSticker=True, isDevMode=True):
		# user setting
		self.component = component
		self.title = titleType
		self.subtitle = subTitleType
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
	def wrappingText(self, header, txt, tail=''):
		return header + ' ' + txt.strip() + '' + tail

	# 파서 작동
	def parsing(self):
		self.printDevMessage(f"== parsing execution, current order is {ComponentParser.counter} ==")

		# temporary text variable
		txt = ''

		componentSting = str(self.component)

		# 텍스트 컴포넌트 체크
		if "se-component se-text" in componentSting:
			print('parsing text')
			print(self.component)
		# parsingTextComponent(self.component)

		# 소제목 컴포넌트 체크
		elif "se-component se-sectionTitle" in componentSting:
			print('parsing sectionTitle')

		# 인용구 컴포넌트 체크
		elif "se-component se-quotation" in componentSting:
			print('parsing quotation')

		# 구분선 컴포넌트 체크
		elif "se-component se-horizontalLine" in componentSting:
			print('parsing horizontalLine')

		# 일정 컴포넌트 체크
		elif "se-component se-schedule" in componentSting:
			print('parsing schedule')

		# 코드 컴포넌트 체크
		elif "se-component se-code" in componentSting:
			print('parsing code')

		# 라이브러리 컴포넌트 체크
		elif "se-component se-material" in componentSting:
			print('parsing material')

		# 이미지 컴포넌트 체크
		elif "se-component se-image" in componentSting:
			print('parsing image')

		# 스티커 컴포넌트 체크
		elif "se-component se-sticker" in componentSting:
			print('parsing sticker')
		# if (self.skipSticker):
		# 	print('test')

		# 비디오 컴포넌트 체크
		elif "se-component se-video" in componentSting:
			print('parsing video')

		# 파일 컴포넌트 체크
		elif "se-component se-file" in componentSting:
			print('parsing file')

		# 지도 컴포넌트 체크
		elif "se-component se-placesMap" in componentSting:
			print('parsing map')

		# 아웃고잉링크 컴포넌트 체크
		elif "se-component se-oglink" in componentSting:
			print('parsing oglink')

		# 수식 컴포넌트 체크
		elif "se-component se-formula" in componentSting:
			pass

		# 테이블 컴포넌트 체크
		elif "se-component se-table" in componentSting:
			pass

		else:
			print('find unknown tag\n' + str(self.component))

		self.printDevMessage("== postSetup is clear == ")

		return txt


# ============================================================================================

# parsing function for text
def text(self):
	component = self.component

	self.printDevMessage("== text execution ==")

	txt = ''
	if 'se-module-text' in str(component):
		for sub_content in component.select('.se-module-text'):
			for p_tag in sub_content.select('p'):
				txt += p_tag.text
				txt += self.endline
			if txt == '':
				txt += sub_content.text
				txt += self.endline
		return txt

	self.printDevMessage("== text is clear == ")

	return None


# parsing function for code

if __name__ == '__main__':
	print("== test bed start ==")

	testPostUrl = "https://blog.naver.com/thswjdtmq4/222626338613"
	c1 = BlogPost(testPostUrl, False)
	c1.postSetup()
	rawComponents = c1.postInframeSoup.select('div.se-component')

	for i, rawComponent in enumerate(rawComponents):
		if i == 0:
			# 처음에는 무조건 헤더부분의 다큐먼트 타이틀이 나온다.
			pass
		else:
			data = ComponentParser(rawComponent).parsing()
			print(data)

