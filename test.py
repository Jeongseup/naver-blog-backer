import urllib.request

url = "https://blogattach.naver.com/ae3bb20216252491b85e3b0936d1a5d17420dcd4/20220120_104_blogfile/thswjdtmq4_1642655879720_4luRA9_zip/chromedriver_win32.zip"
file_name = 'chrome.zip'

urllib.request.urlretrieve(url,file_name)
print("저장완료")

