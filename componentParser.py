class ComponentParser(object):
    # SE3Component is class that based on str, found on soup(= HTML TAG)
    # parser progress counter
    counter = 0

    def __init__(self, component, titleType="##", subTitleType="###", skipSticker=True, isDevMode=True):
        # user setting
        self.component = str(component)
        self.title = titleType
        self.subtitle = subTitleType
        self.skipSticker = skipSticker

        #  for development function
        self.isDevMode = isDevMode

        # possible parsing components
        self.parsingFunctionList = [self.img_group, self.link, self.text, self.code, self.img, self.sticker, self.hr,
                                    self.textarea, self.video, self.script, self.anniversary, self.unreliable_text]

    # ============================================================================================

    # 개발편의용 프린트 함수
    def printDevMessage(self, message):
        if self.isDevMode:
            print("[DEV MODE] " + message, end='\n')

    # 파서 작동
    def parsing(self, component):
        self.printDevMessage(f"== parsing execution, current order is {ComponentParser.counter} ==")

        # temporary text variable
        txt = ''

        for parsingFunc in self.parsingFunctionList:
            # parsed text data
            data = parsingFunc(component)
            if data is not None:
                print('get item', data)
                txt += data
                break

        if txt == '':
            print('unkown tag: ' + str(component))

        self.printDevMessage("== postSetup is clear == ")

        return txt

    # ============================================================================================

    # parsing function for text
    def text(self, content):
        txt = ''
        if 'se-title-text' in str(content):
            for sub_content in content.select('.se-title-text'):
                txt += self.wrapping_text(self.title, sub_content.text, self.endline)
            return txt
        elif 'se-section-sectionTitle' in str(content):
            # for sub_content in content.select('.se-section-sectionTitle'):
            for i, sub_content in enumerate(content.select('.se-section-sectionTitle')):
                # print(str(i) + ' ' + sub_content.text.strip())
                if sub_content.text.strip() == '':
                    continue
                if 'se-l-default' in str(content):  # sectiontitle 1
                    txt += self.wrapping_text(self.subtitle1, sub_content.text)
                elif 'se-2-default' in str(content):  # sectiontitle 2
                    txt += self.wrapping_text(self.subtitle2, sub_content.text)
                elif 'se-3-default' in str(content):  # sectiontitle 3
                    txt += self.wrapping_text(self.subtitle3, sub_content.text)
                else:
                    txt += sub_content.text

                txt += self.endline
            return txt
        elif 'se-module-text' in str(content):
            for sub_content in content.select('.se-module-text'):
                for p_tag in sub_content.select('p'):
                    txt += p_tag.text
                    txt += self.endline
                if txt == '':
                    txt += sub_content.text
                    txt += self.endline
            return txt
        return None
