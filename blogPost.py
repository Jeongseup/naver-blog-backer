import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import re

class blogPost:
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
    

    def postSetup(self):
        try:
            self.printDevMessage("postSetup execution")

            self.postInframeUrl = self.getPostInframeUrl()
            self.postInframeSoup = self.getPostInframeSoup()
            self.postEditorVersion = self.getPostEditorVersion()

            self.postDate = self.getPostDate()
            print('here')

            # self.postLogNum = self.getPostLogNum()

        except Exception as e:
            print(e)

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
            for link  in links:
                publishDate = link.get_text()

            if self.isRelativePostDate(publishDate):
                publishDate = self.getRelativePostDate(publishDate)
            else:
                publishDateRegExpr = "20[0-9][0-9]\. [0-9]+\. [0-9]+\. [0-9]+:[0-9]+"
                publishDate = re.search(publishDateRegExpr, publishDate).group()

            self.printDevMessage(f'return is : {publishDate}')
            return publishDate

    # util for getPostDate
    def isRelativePostDate(self, postDate):
        if "전" in postDate:
            return True
        else:
            return False
    # util for getPostDate
    def getRelativePostDate(self, relativeDate):
        # eg. "방금 전", "3분전", "10시간 전"...
        curTime = datetime.now()
        if relativeDate == "방금 전":
            pass
        elif "분 전" in relativeDate:
            elapsedMin = re.search("[0-9]+", relativeDate).group()
            elapsedMin = int(elapsedMin)
            curTime = curTime - timedelta(minutes=elapsedMin)
        elif "시간 전" in relativeDate:
            elapsedHour = re.search("[0-9]+", relativeDate).group()
            elapsedHour = int(elapsedHour)
            curTime = curTime - timedelta(hours=elapsedHour)
        curTime = str(curTime)
        timeRegex = re.compile("[0-9]+-[0-9]+-[0-9]+ [0-9]+:[0-9]+")
        curTime = timeRegex.search(curTime).group()
        return curTime



# ├ def getPostDate(self): set self.postDate ( + isRelativePostDat, getRelativePostDate)
# ├ def isRelativePostDate(self): 만약에
# ├ def getPostEditiorVerison(self): set self.postEditorVerison
# ├ def postSetup(self): set self.postEditorVerison
# └ def run(self) : postSetup 후 파일생성 및 백업 시작 후 close까지


testPostURL = "https://blog.naver.com/thswjdtmq4/222625521000"
c1 = blogPost(testPostURL, True)
c1.postSetup()
