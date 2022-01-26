class Test:
	def __init__(self, id):
		self.id = id
		self.count = None

		self.setup()
		print(Test)

	def setup(self):
		self.count = 10


if __name__ == '__main__':
	# c1 = Test('jeongseup')
	# print(c1.id, c1.count)

	postList = [i for i in range(1, 324)]

	print(len(postList))
	print(postList)

	divListSize = 323 // 4
	print(divListSize)

	# thread 수에 맞게 slicing 하려고 했던 것.. ? -> 나중에 좀 손보자
	for index in range(4):
		if index == 3:
			# 3/4 시점부터?
			partialList = postList[index * divListSize:]
		else:
			partialList = postList[index * divListSize: (index + 1) * divListSize]
		print(partialList)


		threads.append(NaverBlogPostCrawlThread(partialList))