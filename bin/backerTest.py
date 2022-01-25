#!/usr/bin/env python

from NaverBlogCrawler import NaverBlogCrawler as nblog
import sys

usage = "naverblogbackup \"your_naver_ID\""

if __name__ == "__main__":
    argNum = len(sys.argv)
    if argNum == 2:
        naverId = str(sys.argv[1])
        crawler = nblog.NaverBlogCrawler(naverId)
        crawler.run()
    else:
        print(usage)
