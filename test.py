from naverblogbacker.utils import isEmptyDirectory
from naverblogbacker.crawler import BlogCrawler

myPath = 'C:\Jeongseup\python_test'
myId = 'thswjdtmq4'

def main():
    global myPath, myId

    # 빈 폴더 경로가 아니면 종료한다.
    # if not isEmptyDirectory(dirPath=myPath):
    #     exit(-1)

    myBlog = BlogCrawler(targetId=myId, isDevMode=True)
    # BlogCrawler page2까지만 해둠
    myBlog.run(dirPath=myPath)

if __name__ == '__main__':
    main()

