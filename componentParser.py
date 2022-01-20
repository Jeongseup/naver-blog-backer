from blogPost import BlogPost


class ComponentParser(object):
    # SE3Component is class that based on str, found on soup(= HTML TAG)
    # parser progress counter
    counter = 0

    def __init__(self, component, titleType="##", subTitleType="###", skipSticker=True, isDevMode=True):
        # user setting
        self.component = component
        self.title = titleType
        self.subtitle = subTitleType
        self.endLine = '\n\n'
        self.skipSticker = skipSticker

        #  for development function
        self.isDevMode = isDevMode

        # possible parsing components
        # self.parsingFunctionList = [self.img_group, self.link, self.text, self.code, self.img, self.sticker, self.hr,
        #                             self.textarea, self.video, self.script, self.anniversary, self.unreliable_text]

    # ============================================================================================

    # 개발편의용 프린트 함수
    def printDevMessage(self, message):
        if self.isDevMode:
            print("[DEV MODE] " + message, end='\n')

    # text wrapping for markdown style
    def wrappingText(self, header, txt, tail=''):
        return header + ' ' + txt.strip() + '' + tail

    # 파서 작동
    def parsing(self):
        self.printDevMessage(f"== parsing execution, current order is {ComponentParser.counter} ==")

        # temporary text variable
        txt = ''

        for parsingFunc in self.parsingFunctionList:
            # parsed text data
            data = parsingFunc(self.component)
            if data is not None:
                # print('get item', data)
                txt += data
                break

        # if txt == '':
        #     print('unkown tag: ' + str(self.component))

        self.printDevMessage("== postSetup is clear == ")

        return txt

    # ============================================================================================

    def isParagraphComponent(self):
        if "se-component se-paragraph" in str(self.component):
            return True
        else:
            return False

    # ============================================================================================

    # parsing function for text
    def text(self):
        component = self.component

        self.printDevMessage("== text execution ==")

        txt = ''
        if 'se-module-text' in str(component):
            for sub_content in component.select('.se-module-text'):
                for p_tag in sub_content.select('p'):
                    txt += p_tag.text
                    txt += self.endline
                if txt == '':
                    txt += sub_content.text
                    txt += self.endline
            return txt

        self.printDevMessage("== text is clear == ")

        return None

    # parsing function for code


import time

if __name__ == '__main__':
    print("== test bed start ==")

    testPostUrl = "https://blog.naver.com/thswjdtmq4/222626338613"
    c1 = BlogPost(testPostUrl, False)
    c1.postSetup()
    components = c1.postInframeSoup.select('div.se-component')

    iteration = 0
    totalTime = 0
    while iteration < 10:
        iteration += 1

        start = time.time()  # 시작 시간 저장
        #  작업
        textComponentCount = 0

        for component in components:
            if 'se-component se-text' in str(component):
                textComponentCount += 1

        print(f'{textComponentCount}개의 text component를 모두 찾았습니다.')

        duration = time.time() - start
        print(f'{iteration}번째 소요시간 : ', duration)
        totalTime += duration

    print(f'총 {len(components)}개의 컴포넌트를 찾는 소요시간은 평균 {totalTime / 10}초 입니다.')

    # c1 = ComponentParser(tempComponent)
    # print(c1.text())
