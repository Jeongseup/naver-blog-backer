from naverblogbacker.utils import isEmptyDirectory
from naverblogbacker.blog import BlogCrawler
from pick import pick


serviceTitle = ' Please choose an option: '
serviceOptions = ['backlink', 'backup', 'both']

def main(myId, myPath, myOption):

    if myOption is 'backlink':
        try:
            myBlog = BlogCrawler(targetId=myId, skipSticker=True, isDevMode=True)
            myBlog.backlinking(dirPath=myPath)
            print(f' [MESSAGE] Complete! created your backlinks')

        except Exception as e:
            print(e)
            exit(-1)

    elif myOption is 'backup':
        try:
            if not isEmptyDirectory(dirPath=myPath):
                pass

            myBlog = BlogCrawler(targetId=myId, skipSticker=True, isDevMode=True)
            # myBlog.crawling(dirPath=myPath)
            print(f'[MESSAGE] Complete! your blog posts, the number of error posts is {BlogCrawler.errorPost}')

        except Exception as e:
            print(e)
            exit(-1)

    else:
        try:
            if not isEmptyDirectory(dirPath=myPath):
                pass

            myBlog = BlogCrawler(targetId=myId, skipSticker=True, isDevMode=True)
            # myBlog.crawling(dirPath=myPath)
            print(f'[MESSAGE] Complete! your blog posts, the number of error posts is {BlogCrawler.errorPost}')

        except Exception as e:
            print(e)
            exit(-1)


if __name__ == '__main__':
    myOption, _ = pick(serviceOptions, serviceTitle, indicator='>')

    print(f'\n [MESSAGE] You selected this {myOption} service! \n''')

    myId = input(" Please, Enter your naver id : ")
    print(f'\n [MESSAGE] Your naver ID is {myId} \n')

    myPath = input(" Please, Enter empty folder path for saving yours : ")
    print(f'\n [MESSAGE] Your computer save path is {myPath} \n')

    checkTitle = f''' 
    ==== Check your options ====

    Current selected service is "{myOption}",
    Current entered id is "{myId}",
    Current computer save path is "{myPath}" '''

    checkOptions = ['go', 'stop']

    check, _ = pick(checkOptions, checkTitle, indicator='>')

    if check is 'go':
        main(myId, myPath, myOption)
