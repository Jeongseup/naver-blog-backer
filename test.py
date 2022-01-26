from utils import getPostTitleList, getTotalCount
import json
from requests.utils import unquote


def parsingPostTitle(post):
	tempObj = dict()

	tempObj['date'] = post['addDate']
	tempObj['title'] = unquote(post['title'], encoding='utf-8').replace('+', ' ')
	tempObj['logNo'] = post['logNo']

	return tempObj


if __name__ == '__main__':
	# targetId = "thswjdtmq4"
	# data = getTotalCount(targetId)
	# totalCount = data['totalCount']

	# 전체 페이지 개수를 가져오는 currentPage수로 나눈 나머지 +1 만큼하면 모든 페이지 아이템을 가져올 수 있다.
	# pages = (int(totalCount) % 30) + 1
	with open('test.json', mode='r') as fp:
		jsonData = json.load(fp)

		postList = jsonData['postList']

		filtered = filter(lambda post: post['searchYn'] == 'true', postList)
		postList = list(filtered)

		new_data = [parsingPostTitle(post) for post in postList]
		print(new_data)

# for i in range(1, pages):
# 	tempUrl = f'https://blog.naver.com/PostTitleListAsync.naver?blogId=${targetId}&viewdate=&currentPage=${i}&categoryNo=0&parentCategoryNo=0&countPerPage=30'
#
# 	getPostTitleList(targetId)
# 	print(i)
#
# 	break
