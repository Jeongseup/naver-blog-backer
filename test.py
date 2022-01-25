

from utils import getPostTitleList

if __name__ == '__main__':

	targetId = "thswjdtmq4"
	data = getPostTitleList(targetId)

	totalCount = data['totalCount']

	print(totalCount)

	# 전체 페이지 개수를 가져오는 currentPage수로 나눈 나머지 +1 만큼하면 모든 페이지 아이템을 가져올 수 있다.
	pages = (int(totalCount) % 30) + 1

	for i in range(1, pages):
		tempUrl = f'https://blog.naver.com/PostTitleListAsync.naver?blogId=${targetId}&viewdate=&currentPage=${i}&categoryNo=0&parentCategoryNo=0&countPerPage=30'

		getPostTitleList(targetId)
		print(i)

		break

