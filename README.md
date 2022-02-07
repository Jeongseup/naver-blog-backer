naver-blog-backer
=======

**naver-blog-backer**는 네이버 블로그를 백업(크롤링)과 백링크 두 API를 제공하는 패키지입니다.

백업(crawling) API는 개인 네이버 블로그의 글을 아카이빙 목적으로 기존 포스트를 마크다운언어 파일로 저장합니다.

백링크 API는 기존 네이버 블로그 사용자들의 애로사항인 구글 검색 엔진에 포스트가 인덱싱 되지 않는 문제를 해결하기 위한 포스트 백링크 텍스트 파일로 저장합니다.

※ 해당 패키지는 아래의 두 패키지를 참고하여 만들어졌습니다.
1. https://github.com/Lenir/Naver-Blog-Backup
2. https://github.com/chandong83/download-naver-blog

Installation
------------

    $ pip install naver-blog-backer

Usage
---------

**naverblogbacker**는 crawling과 backlinking 2가지 서비스를 제공합니다.

1. **crawling use case**


```python
    from naverblogbacker.utils import isEmptyDirectory
    from naverblogbacker.blog import BlogCrawler
    import os

    myId = 'YOUR NAVER ID' 
    myPath = 'SAVE DIRECTROY PATH'
    mySkipSticker = 'TRUE OR FALSE'

    if isEmptyDirectory(dirPath=myPath):

        myBlog = BlogCrawler(targetId=myId, skipSticker=mySkipSticker, isDevMode=False)
        myBlog.crawling(dirPath=myPath)

        # 정상적으로 실행 시 백업 후 에러 포스트 개수가 출력
        print(f'[MESSAGE] Complete! your blog posts, the number of error posts is {BlogCrawler.errorPost}')
        # 위의 메세지를 잘 보기 위해 프로그램 종료 전 정지
        os.system("pause")
```
SAVE DIRECTORY PATH는 반드시 빈 폴더여야 합니다. 그렇지 않으면, 에러가 발생하고 프로그램이 종료됩니다.

**output**
<img src="https://jeongseup.github.io/assets/naver-blog-backer/image/output_backup.png" width=70%></img>


2. **backlink use case**

```python
    from naverblogbacker.blog import BlogCrawler
    import os

    myId = 'YOUR NAVER ID' 
    myPath = 'SAVE DIRECTROY PATH'

    myBlog = BlogCrawler(targetId=myId, skipSticker=mySkipSticker, isDevMode=False)
    myBlog.backlinking(dirPath=myPath)

    # 정상적으로 실행 시 백업 후 에러 포스트 개수가 출력
    print(f' [MESSAGE] Complete! created your backlinks')
    # 위의 메세지를 잘 보기 위해 프로그램 종료 전 정지
    os.system("pause")
```
백링크 생성 api는 반드시 빈 폴더일 필요가 없습니다.

**output**

<img src="https://jeongseup.github.io/assets/naver-blog-backer/image/output_backlink.png" width=70%></img>

Options
-------

* ``targetId``: 백업 및 백링크를 위한 사용할 네이버 블로그 아이디입니다.
* ``dirPath``: 백업 혹은 백링크 결과물을 저장할 경로입니다.
* ``skipSticker`` : (optional) 블로그 포스트 내 스티커 이미지를 저장할지 말지에 대한 옵션입니다. 기본값은 True이며, True를 스티커 이미지를 스킵해 저장하지 않는 것을 뜻합니다.
* ``isDevMode``: (optional) **naver-blog-backer** 모듈 내 처리들에 대한 상세 히스토리를 볼 수 있는 개발자 모드 옵션입니다. 기본값은 False이며, 만약 True로 전환 시 [DEV MODE] 메세지가 출력됩니다.


Examples
---------
1. **using pthon script** (*the code is tests folder in this repository*)
```python
import os
from naverblogbacker.utils import isEmptyDirectory
from naverblogbacker.blog import BlogCrawler
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
    myId = 'YOUR NAVER ID'
    myPath = 'SAVE DIRECTORY'
    myOption =  'CHOOSE OPTIONS IN [backlink, backup]'

    main(myId, myPath, myOption)
```

2. **using program** (*the program, naverblogbacker.exe, is root path in this repository*)


#### Version Information
##### ver 0.0.1 ~ 0.0.6
Beta release. (crawling & backlicking complete) 

##### Later
it will be making GUI version for common users
___
Memo
-----
해당 라이브러리 및 프로그램 개발과 관련된 메모를 위한 공간입니다.

- code stype : cameCase
- 패키지 로직 (ver : 0.1)
    1. 일단.. blogPost라는 객체를 완성 후 url를 넣으면 bs4로 inframe 데이터를 가져온다.
    2. 전체 html data 중 se-component를 찾아서 실질적인 데이터만을 골라낸다.
    3. parser를 import하여 각 compoenent를 parser로 parsing 한다.


패키지 구성
### 패지키 구성
1. blog.py
2. parser.py
3. post.py
4. utils.py


에디터 버젼 4의 component 구성  
1. HEADER 와 CONTENT로 구성  
2. 모든 컨텐츠는 div.se-component로 구성    


HEADER ()  
- 카테고리명 :  se-component & se-documentTitle > se-component-content > ... > blog2_series    
- 제목 : se-component se-documentTitle > se-component-content > ... > se-title-text  
- etc..    

CONTENT  (div.se-main-container)  
- 텍스트 : se-component & se-text > se-component-content > se-section-text >    
    - 실제 텍스트 : ... > se-module-text > p.se-text-paragraph & span (span 태그에 실제 텍스트가 담김)    
    - 엔터 : ... > se-module-text > p.se-text-paragraph & span (nothing)    
    - 링크 : ... > se-module-text > p.se-text-paragraph & se-link  
    
- 소제목 : se-component & se-sectionTitle > se-component-content > ... > se-module-text > se-text-paragraph    

- 인용구 : se-component & se-quotation > se-component-content > ... > se-module-text > se-text-paragraph    

- 구분선 : se-component & se-horizontalLine > se-component-content > se-section-horizontalLine > se-module-horizontalLIne   
    - 구분선 : ... > hr.se-hr (스타일에 따라 변하지는 않음)  
    
- 일정 : se-component & se-schedule   
    - 일정 텍스트 : ... > se-component-content > se-section-schedule > se-module-schedule > ... > p.se-schedule-title   
    - 일정 데이트 : ... > script[data-module] > data.startAt, data.endAt  

- 코드 : se-component & se-code > se-component-content > se-section-code > se-section-code > se-module-code > se-code-source     

- 라이브러리(책, 영화) : se-component & se-material > se-component-content > se-section-material > a[data-linkdata]  

- 이미지 : se-component & se-image > se-component-content > se-section-image >  
    - 이미지 소스 : ... > se-module-image > a[data-link, src] or a > img[data-lazy-src]  
    - 이미지 텍스트 : ... > se-module-text & se-caption > p.se-text-paragraph > span  

- sns 이미지 : 이미지 컴포넌트와 동일  

- 스티커 : se-component & se-sticker > se-component-content > se-section-sticker >  
    - 이미지 소스 : ... > se-module-sticker > a > img.se-sticker-image[src]  
    - 이미지 텍스트 : ... > se-module-text & se-caption > p.se-text-paragraph > span  

- 비디오 :  se-component & se-video    
    - 비디오 컴포넌트 : ... > se-component-content > se-section-video    
    - 비디오 소스 : ... > script > data-module (vid, inkey) -> api 요청(https://apis.naver.com/rmcnmv/rmcnmv/vod/play/v2.0/VID?key=?) -> 파일 저장된 URL로 요청     

- 파일 : se-component & se-file > se-component-content > se-section-file > se-module-file >  a[data-link] -> api 요청(link)  

- 지도 :  se-component & se-placeMap > se-component-content > se-section-placeMap > se-module-text > a.se-map-info > se-map-title & se-map-address (생략하고 텍스트 데이터만 가져옴.)  

- 링크 : se-component & se-text > se-component-content > ... > se-module-oglink > se-text-paragraph > se-link    
    - a > se-oglink-thumbnail  
    - a > se-oglink-info  
    - se-oglink-title    
    - se-oglink-summary  
    - se-oglink url  
(ex: <a href="http://example.com" class="se-link" target="_blank"><strike><u><i><b>http://example.com</b></i></u></strike></a> )    

- 해시태그 : se-component & se-text > se-component-content > ... > se-module-text > se-text-paragraph > __se-hash-tag  



> https://wikidocs.net/21952
> https://hongku.tistory.com/338


<video id="dmp_Video" class="dmp_Video " playsinline="" webkit-playsinline="" x-webkit-airplay="allow" controlslist="nodownload" style="display: block; width: 100%; height: 100%; top: 0px; left: 0px;" src="blob:https://www.dailymotion.com/b38a4473-0553-46aa-ba9c-a7b6b6e3a190"></video>