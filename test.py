import json
from urllib import request

from naverblogbacker.utils import isEmptyDirectory
from naverblogbacker.blog import BlogCrawler

def main(myId, myPath):
    try:
        # 저장 경로가 빈 폴더가 아닌 경우 에러 발생
        if not isEmptyDirectory(dirPath=myPath):
            pass

        myBlog = BlogCrawler(targetId=myId, skipSticker=True, isDevMode=True)
        myBlog.crawling(dirPath=myPath)

        print(f'[MESSAGE] Complete! your blog posts, the number of error posts is {BlogCrawler.errorPost}')

    except Exception as e:
        print(e)
        exit(-1)

def test():
    jsonUrl = 'https://apis.naver.com/rmcnmv/rmcnmv/vod/play/v2.0/B01A6FD3C12A8F466D405508428F425CE66C?key=V12710773d50b5f308c4bfc00f15df45674a3e1015640fbced4f7b1c50fd43ea324b1fc00f15df45674a3'

    with request.urlopen(jsonUrl) as url:
        videoList = json.loads(url.read().decode())['videos']['list']

        videoOriginalWidth = 1920

        for video in videoList:
            if str(video['encodingOption']['width']) == str(videoOriginalWidth):
                return print("here")

        return print("there")

if __name__ == '__main__':
    # myId = input("Please, Enter your naver id : ")
    # print(f'[MESSAGE] YOUR ID IS {myId}')

    # myPath = input("Please, Enter empty folder path for saving yours : ")
    # print(f'[MESSAGE] SAVE PATH IS {myPath}')

    # main(myId, myPath)
    test()
