import os
from naverblogbacker.utils import saveImage, parsingScriptTag, saveVideo, getVideoSource


class ComponentParser(object):
	# SE3Component is class that based on str, found on soup(= HTML TAG)
	# parser progress counter
	counter = 0
	errorCounter = 0
	hashTagList = []
	assetPath = ''

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
			# return ''
			return self.parsingText()

		# 소제목 컴포넌트 체크
		elif "se-component se-sectionTitle" in componentSting:
			# return ''
			return self.parsingSectionTitle()

		# 인용구 컴포넌트 체크
		elif "se-component se-quotation" in componentSting:
			# return ''
			return self.parsingQuotation()

		# 구분선 컴포넌트 체크
		elif "se-component se-horizontalLine" in componentSting:
			# return ''
			return self.parsingHorizontalLine()

		# 일정 컴포넌트 체크
		elif "se-component se-schedule" in componentSting:
			print('지원하지 않는 컴포넌트입니다.')
			return ''

		# 코드 컴포넌트 체크
		elif "se-component se-code" in componentSting:
			# return ''
			return self.parsingCode()

		# 라이브러리 컴포넌트 체크
		elif "se-component se-material" in componentSting:
			# return ''
			return self.parsingMaterial()

		# 이미지 컴포넌트 체크
		elif "se-component se-image" in componentSting:
			# return ''
			return self.parsingImage()

		# 이미지 스트립 컴포넌트 체크
		elif "se-component se-imageStrip" in componentSting:
			# return ''
			return self.parsingImageStrip()

		# 스티커 컴포넌트 체크
		elif "se-component se-sticker" in componentSting:
			if not self.skipSticker:
				return self.parsingSticker()
			else:
				return ''

		# 비디오 컴포넌트 체크
		elif "se-component se-video" in componentSting:
			# return ''
			return self.parsingVideo()

		# 파일 컴포넌트 체크
		elif "se-component se-file" in componentSting:
			# return ''
			return self.parsingFile()

		# 지도 컴포넌트 체크
		elif "se-component se-placesMap" in componentSting:
			# return ''
			return self.parsingPlacesMaps()

		# 아웃고잉링크 컴포넌트 체크
		elif "se-component se-oglink" in componentSting:
			# return ''
			return self.parsingOglink()

		# 임베드 컴포넌트 체크
		elif "se-component se-oembed" in componentSting:
			# return ''
			return self.parsingOembed()

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
			return ''

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

		oglinkTitle = "No Title"
		oglinkSummary = ''

		oglinkTitleTag = self.component.select('.se-oglink-title')
		oglinkSummaryTag = self.component.select('.se-oglink-summary')
		oglink = self.component.select('.se-oglink-info')[0]['href']

		if len(oglinkTitleTag) != 0:
			oglinkTitle = oglinkTitleTag[0].text

		if len(oglinkSummaryTag) != 0:
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
		quotationSite = "No Site"

		quotationSiteTag = self.component.select('.se-cite')

		if len(quotationSiteTag) != 0:
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
		imageCaption = ''

		imageCaptionTag = self.component.select('.se-caption')
		if len(imageCaptionTag) != 0:
			imageCaption = imageCaptionTag[0].text

		for imageTag in self.component.select('img'):

			imageUrl = imageTag['data-lazy-src']

			# 나중에 이미지 확장자 셀렉터하는 것 추가할 것
			txt += f'![{ComponentParser.counter}](./asset/{ComponentParser.counter}.png)'
			txt += self.endLine
			txt += imageCaption

			if saveImage(imageUrl, f'{ComponentParser.assetPath}/{ComponentParser.counter}.png'):
				ComponentParser.counter += 1
			else:
				ComponentParser.errorCounter += 1
				print(f'[ERROR] {ComponentParser.counter}번째 이미지가 정상적으로 저장되지 않았습니다.')

		self.printDevMessage('clear')
		return txt

	# parsing function for image
	def parsingImageStrip(self):
		self.printDevMessage("== parsingImageStrip execution ==")

		txt = ''

		imageCaptionTag = self.component.select('.se-caption')

		for i, imageTag in enumerate(self.component.select('img')):

			imageUrl = imageTag['data-lazy-src']

			# 나중에 이미지 확장자 셀렉터하는 것 추가할 것
			txt += f'![{ComponentParser.counter}](./asset/{ComponentParser.counter}.png)'
			txt += self.endLine

			if len(imageCaptionTag) != 0:
				txt += imageCaptionTag[i]

			if saveImage(imageUrl, f'{ComponentParser.assetPath}/{ComponentParser.counter}.png'):
				ComponentParser.counter += 1
			else:
				ComponentParser.errorCounter += 1
				print(f'[ERROR] {ComponentParser.counter}번째 이미지가 정상적으로 저장되지 않았습니다.')

		self.printDevMessage('clear')
		return txt

	# parsing function for sticker
	def parsingSticker(self):
		self.printDevMessage("== parsingSticker execution ==")

		txt = ''

		for imageTag in self.component.select('img'):
			imageUrl = imageTag['src']

			# 나중에 이미지 확장자 셀렉터하는 것 추가할 것
			txt += f'![{ComponentParser.counter}](./asset/{ComponentParser.counter}.png)'
			txt += self.endLine

			if saveImage(imageUrl, f'{ComponentParser.assetPath}/{ComponentParser.counter}.png'):
				ComponentParser.counter += 1
			else:
				ComponentParser.errorCounter += 1
				print(f'[ERROR] {ComponentParser.counter}번째 이미지가 정상적으로 저장되지 않았습니다.')

		self.printDevMessage('clear')
		return txt

	def parsingOembed(self):
		self.printDevMessage("== parsingOembed execution ==")

		txt = ''

		videoThumbnail = ''
		videoTitle = ''
		videoDescripton = ''
		videoUrl = ''

		for content in self.component.select('script'):
			jsonData = parsingScriptTag(content['data-module'])['data']

			videoUrlKey = 'inputUrl'
			titleKey = 'title'
			thumbnailKey = 'thumbnailUrl'
			descriptionKey = 'description'

			if videoUrlKey in jsonData.keys():
				videoUrl = jsonData[videoUrlKey]

			if titleKey in jsonData.keys():
				videoTitle = jsonData[titleKey]

			if thumbnailKey in jsonData.keys():
				videoThumbnail = jsonData[thumbnailKey]

			if descriptionKey in jsonData.keys():
				videoDescripton = jsonData[descriptionKey]

			txt += f'[![{videoTitle}]({videoThumbnail})]({videoUrl})'
			txt += self.endLine

			txt += '설명 : ' + videoDescripton
			txt += self.endLine

			self.printDevMessage("clear")
			return txt

	def parsingVideo(self):
		self.printDevMessage("== parsingVideo execution ==")

		txt = ''
		for content in self.component.select('script'):
			jsonData = parsingScriptTag(content['data-module'])['data']
			videoUrl = getVideoSource(jsonData)

			videoThumbnail = jsonData['thumbnail']
			videoTitle = jsonData['mediaMeta']['title']
			videoTags = jsonData['mediaMeta']['tags']
			videoDescription = jsonData['mediaMeta']['description']

			# 나중에 확장자 셀렉터하는 것 추가할 것
			txt += f'[![{ComponentParser.counter}]({videoThumbnail})](./asset/{ComponentParser.counter}.mp4)'
			txt += self.endLine

			txt += f'제목 : {videoTitle}, 설명 : {videoDescription}'
			txt += self.endLine

			txt += '해시태그 : '
			for hashTag in videoTags:
				txt += '#' + hashTag + ' '
			txt += self.endLine

			if saveVideo(videoUrl, f'{ComponentParser.assetPath}/{ComponentParser.counter}.mp4'):
				ComponentParser.counter += 1
			else:
				ComponentParser.errorCounter += 1
				print(f'[ERROR] {ComponentParser.counter}번째 이미지가 정상적으로 저장되지 않았습니다.')

		self.printDevMessage('clear')
		return txt

	def parsingPlacesMaps(self):
		self.printDevMessage("== parsingPlacesMaps execution ==")

		txt = ''
		for content in self.component.select('a.se-map-info'):
			jsonData = parsingScriptTag(content['data-linkdata'])

			txt += f'장소명 : {jsonData["name"]}'
			txt += self.endLine
			txt += f'주소 : {jsonData["address"]}'
			txt += self.endLine

		self.printDevMessage("clear")
		return txt

	def parsingMaterial(self):
		self.printDevMessage("== parsingMaterial execution ==")

		txt = ''
		for content in self.component.select('a.se-module-material'):
			jsonData = parsingScriptTag(content['data-linkdata'])

			txt += f'{jsonData["title"]}({jsonData["type"]}), 링크 : {jsonData["link"]}'
			txt += self.endLine

		self.printDevMessage("clear")
		return txt

	def parsingFile(self):
		self.printDevMessage("== parsingFile execution ==")

		txt = ''
		for content in self.component.select('a.se-file-save-button'):
			jsonData = parsingScriptTag(content['data-linkdata'])

			fileUrl = jsonData["link"]
			fileName = fileUrl.split('/')[-1]

			txt += f'![{fileName}](./asset/{fileUrl["link"]})'
			txt += self.endLine

		if saveVideo(fileUrl, f'{ComponentParser.assetPath}/{fileName}'):
			pass
		else:
			ComponentParser.errorCounter += 1
			print(f'[ERROR] "{fileName}" 파일이 정상적으로 저장되지 않았습니다.')

		self.printDevMessage("clear")
		return txt
