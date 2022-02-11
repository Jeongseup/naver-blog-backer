import os
from naverblogbacker.utils import isEmptyDirectory
from naverblogbacker.blog import BlogCrawler
from naverblogbacker.auth import sendToken
from pick import pick


def main(myId, myPath, myOption):

    if myOption is 'backlink':
        try:
            myBlog = BlogCrawler(targetId=myId, skipSticker=True, isDevMode=False)
            myBlog.backlinking(dirPath=myPath)
            print(f' [MESSAGE] Complete! created your backlinks')
            os.system("pause")

        except Exception as e:
            print(e)
            os.system("pause")

    elif myOption is 'backup':
        try:
            if not isEmptyDirectory(dirPath=myPath):
                pass

            myBlog = BlogCrawler(targetId=myId, skipSticker=True, isDevMode=False)
            myBlog.crawling(dirPath=myPath)
            print(f'[MESSAGE] Complete! your blog posts, the number of error posts is {BlogCrawler.errorPost}')
            os.system("pause")

        except Exception as e:
            print(e)
            os.system("pause")

    else:
        print(f' [MESSAGE] Sorry, It`s currently not supported')
        os.system("pause")

if __name__ == '__main__':

    serviceTitle = ' Please choose an option: '
    serviceOptions = ['backlink', 'backup', 'both']

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
    Current computer save path is "{myPath}" 
    '''

    checkOptions = ['go', 'stop']

    check, _ = pick(checkOptions, checkTitle, indicator='>')

    if check is 'go':
        print(f'\n [MESSAGE] Please wait a second while sending a mail with temporary token \n')

        SENDER = "MANAGER SECRET"
        PASSWORD = "MANAGER SECRET"

        authToken = sendToken(f'{myId}@naver.com', SENDER, PASSWORD)

        print(f'\n [MESSAGE] Check your naver email. And then Verify the token \n')
        inputToken = input("token is : ")

        if str(authToken) == str(inputToken):
            main(myId, myPath, myOption)
            os.system("pause")
        else:
            print(f'\n [MESSAGE] Sorry, your input token is not correct, Exit the programe. Bye :) \n')
            os.system("pause")
    else:
        print(f'\n [MESSAGE] Exit the programe. Bye :) \n')
        os.system("pause")