class Test:
	def __init__(self, id):
		self.id = id
		self.count = None

		self.setup()
		print(Test)

	def setup(self):
		self.count = 10


if __name__ == '__main__':
	c1 = Test('jeongseup')
	print(c1.id, c1.count)