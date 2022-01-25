import unittest



'''
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
				continue

			data += ComponentParser(rawComponent, skipSticker=True).parsing

			if i == len(rawComponents) - 1:
				txt = '해시태그 : '
				for hashTag in ComponentParser.hashTagList:
					txt += hashTag

				data += ' ' + txt

		fp.write(data)

	ComponentParser.hashTagList = []
	ComponentParser.counter = 0
'''


class MyTestCase(unittest.TestCase):
	def test_something(self):
		self.assertEqual(True, False)


if __name__ == '__main__':
	unittest.main()
