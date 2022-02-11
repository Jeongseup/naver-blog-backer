
from naverblogbacker.blog import BlogCrawler

class Runner(BlogCrawler):
    def backlinking(self, dirPath):
        print(len(self.postList))


myBlog = Runner(targetId="thswjdtmq4", skipSticker=True, isDevMode=False)
myBlog.backlinking("C:")