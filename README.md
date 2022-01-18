# naver-blog-backer
naver blog backer (backlinker &amp; backup)

### memo

가정 :이전 단계에서 naver id를 입력하면 id에 맞춰 모든 post URL을 가져오는 로직이 구현되었다는 가정 그 이후에 url 하나씩 넘겨준다.

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
