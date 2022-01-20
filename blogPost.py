import requests
from bs4 import BeautifulSoup
import sys
import utils


class BlogPost:
    def __init__(self, url, isDevMode=False):
        # 개발 편의
        self.isDevMode = isDevMode
        # init
        self.url = url
        self.postInframeUrl = ''
        self.postEditorVersion = None
        self.postLogNum = None
        self.postDate = None
        self.postInframeSoup = None

        self.imageCount = 0
        self.saveDir = ''
        self.saveFile = None

        # init check
        if self.isForeignUrl():
            print("[INIT ERROR] URL이 잘못되었습니다. 프로그램을 종료합니다.")

    # ============================================================================================

    # 개발편의용 프린트 함수
    def printDevMessage(self, message):
        if self.isDevMode:
            print("[DEV MODE] " + message, end='\n')

    # 유저가 입력한 URL 이 올바른지 체크하는 함수
    def isForeignUrl(self):
        self.printDevMessage("isForeignUrl execution")

        if 'blog.naver.com' in self.url:
            return False
        else:
            return True

    # ============================================================================================

    def postSetup(self):
        try:
            self.printDevMessage("== postSetup execution == ")

            self.postInframeUrl = self.getPostInframeUrl()
            self.postInframeSoup = self.getPostInframeSoup()
            self.postEditorVersion = self.getPostEditorVersion()
            self.postDate = self.getPostDate()

            self.printDevMessage("== postSetup is clear == ")

        # 여기서는 폴더 생성 체크까지만, 다 되었다면 run 함수로 넘긴다.

        except Exception as e:
            print(e)
            sys.exit(-1)

    def getPostInframeUrl(self):
        self.printDevMessage("== getPostInframeUrl 실행 ==")

        originHtml = requests.get(self.url).text
        originSoup = BeautifulSoup(originHtml, features="html.parser")

        for link in originSoup.select('iframe#mainFrame'):
            postInframeUrl = "http://blog.naver.com" + link.get('src')

        self.printDevMessage(f'return is : {postInframeUrl}')
        return postInframeUrl

    def getPostInframeSoup(self):
        self.printDevMessage("== getPostInframeSoup execution ==")

        if not (self.postInframeUrl == ''):
            inframeHtml = requests.get(self.postInframeUrl).text
            inframeSoup = BeautifulSoup(inframeHtml, features="html.parser")

            self.printDevMessage(f'return is : {len(inframeSoup)} links')
            return inframeSoup
        else:
            raise Exception("[ERROR] getPostInframeSoup가 정상적으로 실행되지 않았습니다.")

    def getPostEditorVersion(self):
        self.printDevMessage("== getPostEditorVersion execution ==")

        for link in self.postInframeSoup.select('div#post_1'):
            postEditiorVersion = link.get('data-post-editor-version')

        if postEditiorVersion == None:
            raise Exception("[ERROR] 지원하지 않는 에디터 버젼입니다.")

        self.printDevMessage(f'return is : {postEditiorVersion}')
        return postEditiorVersion

    def getPostDate(self):
        self.printDevMessage("== getPostDate execution ==")

        links = self.postInframeSoup.select('span.se_publishDate')
        if len(links) == 0:
            raise Exception("[ERROR] 포스트 게시일을 찾지 못했습니다.")

        else:
            for link in links:
                publishDate = link.get_text()

            if utils.isRelativePostDate(publishDate):
                publishDate = utils.getRelativePostDate(publishDate)

            # publishDateRegExpr = "20[0-9][0-9]\. [0-9]+\. [0-9]+\. [0-9]+:[0-9]+"
            # publishDate = re.search(publishDateRegExpr, publishDate).group()

            self.printDevMessage(f'return is : {publishDate}')
            return publishDate

    # ============================================================================================

    def run(self):
        self.printDevMessage("== run execution ==")

        self.postSetup()

        try:
            # "fp" stands for "file pointer"
            # with open(dir + '/' + file_name, "w", encoding='utf-8') as fp:
            with open('./post/test.txt', mode='w', encoding='utf-8') as fp:
                txt = 'write test'

                # if 'se_component' in str(self.postInframeSoup):
                #     for sub_content in soup.select('div.se_component'):
                #         txt += parser.parsing(sub_content)
                # else:
                #     for sub_content in soup.select('div.se-component'):
                #         txt += parser.parsing(sub_content)

                fp.write(txt)
            return
        except Exception as e:
            print(e)
            return False


if __name__ == '__main__':
    testPostUrl1 = "https://blog.naver.com/thswjdtmq4/222619927525"
    testPostUrl2 = "https://blog.naver.com/thswjdtmq4/222625521000"
    c1 = BlogPost(testPostUrl2, False)
    c1.postSetup()

    components = c1.postInframeSoup.select('div.se-component')
    print(components[0])
    # for component in c1.postInframeSoup.select('div.se-component'):
    #     # 컨텐츠 하나 가져오고
    #  컨텐츠 가져올 때 어차피 첫 컨텐츠는 무조건 title이니까 바로 title로 처리 se-title-text로 접근

    #     print("===================")
    #     print(component)
    #     print("===================")
    # #
    #     break
    # 파싱하고
    # 파일에 쓰고
