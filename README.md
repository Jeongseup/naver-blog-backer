# naver-blog-backer
naver blog backer (backlinker &amp; backup)

### memo

가정 :이전 단계에서 naver id를 입력하면 id에 맞춰 모든 post URL을 가져오는 로직이 구현되었다는 가정 그 이후에 url 하나씩 넘겨준다.

스타일 가이드 
> https://medium.com/@kkweon/%ED%8C%8C%EC%9D%B4%EC%8D%AC-doc-%EC%8A%A4%ED%83%80%EC%9D%BC-%EA%B0%80%EC%9D%B4%EB%93%9C%EC%97%90-%EB%8C%80%ED%95%9C-%EC%A0%95%EB%A6%AC-b6d27cd0a27c
> https://google.github.io/styleguide/pyguide.html

패키지 룰 : cameCase로 작성

패키지 로직 (ver : 0.1)
1. 일단.. blogPost라는 객체를 완성 후 url를 넣으면 bs4로 inframe 데이터를 가져온다.
2. 전체 html data 중 se-component를 찾아서 실질적인 데이터만을 골라낸다.
3. parser를 import하여 각 compoenent를 parser로 parsing 한다.


패키지 구성

#### class) blogPost : 블로그 인프레임 데이터를 저장하는 객체  
#### blogPost.py  
└ input args & init : blog url ( + path, fileName 고려중)  
├ self.url : 원래 블로그 URL  
├ self.inFrameUrl : inframe url   
├ self.postEditorVersion : blog post가 editor version이 4인지 확인, 일단 내 블로그 모든 글은 4로 되어있는거 같아서 이 버젼으로만 사용하게 만들 생각.  
├ self.postTitle : postTitle HTML 상단 제목  
├ self.postDate : 포스트 게시일  
├ self.imageCount : 이미지 개수  
├ self.inFrameSoup : inframe url을 bs4에 넣어 리턴 받은 html data  
├ self.saveDir : 저장할 공간  
├ self.saveFile : 저장할 때 파일명  
├ self.saveFile : 저장할 때 파일명  
├ self.isDevMode : 개발모드 시 print on  
└ self.imageCount : 이미지 개수  
... self.postLogNum도 필요할까?  

└ functions  
├ def isforeignURL(self) : url 제대로 넣었는지 확인  
├ def getInframeUrl(self): set self.inFrameUrl (if isForeignUrl is True)  
├ def getPostEditiorVerison(self): set self.postEditorVerison  
├ def getPostDate(self): set self.postDate ( + isRelativePostDat, getRelativePostDate)  
├ def isRelativePostDate(self): 만약에  
├ def getPostEditiorVerison(self): set self.postEditorVerison  
├ def postSetup(self): set self.postEditorVerison  
└ def run(self) : postSetup 후 파일생성 및 백업 시작 후 close까지  

#### module) parser : 블로그 데이터 내 컴포넌트마다 파싱하는 함수 모음  
#### componentParser.py  
└ input args : one component in blogPost  
├ self.url : 원래 블로그 URL  
├  
├  
└  


에디터 버젼 4의 component 구성  
1. HEADER 와 CONTENT로 구성  
2. 모든 컨텐츠는 div.se-component로 구성    


테스트 페이지
https://blog.naver.com/PostView.naver?blogId=thswjdtmq4&logNo=222626338613&redirect=Dlog&widgetTypeCall=true&directAccess=false

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



한 component 안에는 여러 개의 텍스트가 존재할 수 있다?  -> 이거 한 컴포넌트 돌릴 떄 for문으로 돌려야할 거 같은데.. ?  
임베드 영상은 어떻게 처리해야 할지.. ?  



> https://wikidocs.net/21952
> https://hongku.tistory.com/338