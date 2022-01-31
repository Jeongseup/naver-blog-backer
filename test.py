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


if __name__ == '__main__':
    myId = input("Please, Enter your naver id : ")
    print(f'[MESSAGE] YOUR ID IS {myId}')

    myPath = input("Please, Enter empty folder path for saving yours : ")
    print(f'[MESSAGE] SAVE PATH IS {myPath}')

    main(myId, myPath)
