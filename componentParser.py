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

    # parsing function for text
    def text(self):
        component = self.component

        self.printDevMessage("== text execution ==")

        txt = ''
        if 'se-section-sectionTitle' in str(component):
            print('start\n')
            print(component.text)
            print('end\n')

            for i, sub_content in enumerate(component.select('.se-section-sectionTitle')):
                # print(sub_content)
                print(sub_content.text)
                if sub_content.text.strip() == '':
                    continue

                if 'se-l-default' in str(component):  # sectiontitle 1
                    txt += self.wrappingText(self.subtitle, sub_content.text)
                else:
                    txt += sub_content.text

                txt += self.endLine
            return txt

        elif 'se-module-text' in str(component):
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



if __name__ == '__main__':
    print("test bed")

    testPostUrl = "https://blog.naver.com/thswjdtmq4/222626338613"
    c1 = BlogPost(testPostUrl, False)
    c1.postSetup()

    components = c1.postInframeSoup.select('.se-sectionTitle')
    tempComponent = components[0]

    c1 = ComponentParser(tempComponent)
    print(c1.text())