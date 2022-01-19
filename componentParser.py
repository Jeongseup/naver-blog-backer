
class ComponentParser:
    # SE3Component is class that based on str, found on soup(= HTML TAG)
    def __init__(self, component, skipSticker = True, isDevMode= True):
        self.component = str(component)
        self.isDevMode = isDevMode
        self.skipSticker = skipSticker

        self.title = '#'
        self.subtitle1 = '##'
        self.subtitle2 = '###'
        self.subtitle3 = '####'

        # 파싱 리스트
        self.parsing_func_list = [self.img_group, self.link, self.text, self.code, self.img, self.sticker, self.hr,
                                  self.textarea, self.video, self.script, self.anniversary, self.unreliable_text]



    def __str__(self):
        return self.component

    def __del__(self):
        Parser.var -= 1

kim = Parser("kim")
lee = Parser("lee")

print(kim.component)
print(kim.var)