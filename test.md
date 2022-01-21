## Today I Learned : 내 블로그 포스트(게시물)의 전체기간 조회수 순위(랭킹) 보는 방법

안녕하세요 :) 취준생 블로거 'seup'입니다. 이번 글은 각자 열심히 키우고 계신 개인 네이버 블로그에 대한 데이터(조회수 및 etc)를  각 포스팅의  조회수(readCount)를 기준으로 순위를 메겨보는 것에 대해 공유하고자 합니다.​​ 사실 이번 글 및 실험을 하기 전에 다른 것에 대해 먼저 알아보고 있었는데요. 

​

​

​

그 연유는 내 블로그를 구글 검색에 등록시키위해서 키자드 없이 블로그의 백링크를 만들기 위해서 였습니다.(이 방법은 이 글에 잘 나와있는데 실제로 2022년 1월 기준으로 내가 해보니 정말로 구글에 내 글이 제대로 검색되는 것을 확인하였습니다)

​

​

​

하여튼..  저 키자드 없이 블로그 포스팅을 좀 더 간편하게 하는 것도 지금 실험 중인데 이를 위해서는 우선 이번 실험이 첫 단계였다고 사려됩니다. 우선은 이번 포스팅에서는 개인 블로그 내 전체 포스트의 조회수 순위를 전체 기간을 기준으로 sorting 해보는 것을 말씀드리겠습니다.

---

※ 반말체로 작성하였습니다.  

또한, 기술적인 내용이 많으니 그냥 따라서 해보기만 하고 싶은 분들은 맨 아래 최종부분만 보시길 권유드립니다 :)

​

키자드 백링크를 스스로 만들기 위해서는 내 블로그에 기재된 모든 포스트들의 URL속 inframe URL를 찾아 이를 구글 블로거에 포스팅해야한다. 결국 내가 올린 모든 게시물들에 일일이 접근해서 각각 URL을 copy&paste해서 텍스트로 쭉 나열해서 이를 저장해야하는 것을 뜻하는데 너무 비효율적인 생각이 들었다. 

​

​

그리고 사실상 요즘 블로그를 시작하는 사람이 부쩍 늘어난 만큼 이를 자동화해서 적어도 깔끔하게 [제목, URL]이 하나의 txt파일로 저장하게 하는 프로그램을 짜는 것이 나를 위해서도 그리고 다른 사람들에게도 필요한 것이라 생각했다. (사실 이렇게 된다면 키자드에 돈을 후원하면서 까지 쓰고 있는 유저들 혹은 키자드가 불안하여 구글 검색에 노출하지 못한 유저들의 애로사항을 풀어줄 수 있다고 생각한다)

​

​

​

하튼 이를 위해서는 내 블로그 포스트들의 데이터를 좀 더 다뤄볼 필요가 있다고 생각하던 중 재미난 글을 발견했다. 아래의 글인데 블로그 내에 어떤 포스트(게시물)이 가장 조회수가 많은지 알아볼 수 있는 방법을 적어둔 글이었다.

​

https://m.blog.naver.com/hsm622/221540041793

[어떤 포스트가 가장 조회수가 많은지 알고싶어서..](https://m.blog.naver.com/hsm622/221540041793) : 말 그대로 정말 뜬금없는 호기심이 생겼다. 네이버 블로그에 포스팅한 내 글중 조회수가 가장 많은게 몇건...

​

왜? 굳이 복잡하게 저렇게 코딩까지하면서 해야하냐? 란 생각이 드는 사람들을 위해 말해주자면 각자 블로그에 로그인한 상태로 '관리 >내  블로그 통계 > 조회수 순위' 를 들어가보면 알겠지만, 사실상 네이버 블로그에서는 따로 모든 기간 내에 어떤 포스트가 가장 조회수가 많았는지는 알려주지 않는다. (다만 일간, 주간, 월간을 지원한다)

​

​

​

그래서 우선 이것부터 한번 해보고 싶어서 위에 적어둔 그 글을 따라 읽고, 더불어 같이 비비모 스터디를 진행 중인 wan9s님이 짜준 코드 (네이버 블로그 크롤러)를 바탕으로 좀 더 나은 코드를 작성해보기로 했다.

​

​

우선 기본적으로 Node.js 환경에서 개인 블로그 데이터를 받아오는 경우 로그인 상태가 아니어서 인지 readCount 즉, 조회수는 불러와지지 않는 것을 발견했다.따로 데이터 요청 시 header에 몇몇 데이터(ex: 쿠키)를 넣어보면 정상적으로 readCount(조회수)가 불러와질까? 생각했지만 그렇지 않았다. 그래서 결국 로그인한 브라우저 내 콘솔을 활용하여 데이터를 추출하기로 결정했다.

​

​

내 포스트 데이터를 요청하기 위해 이해해야 할 것은 내 블로그 내에서 전체보기 탭이 어떻게 작동하는 지를 이해하는 것이다. 그 방법은 바로 전체보기 탭 내에 어떤 다음페이지를 클릭하거나 다음 버튼을 누를 때 즉시 데이터를 요청하고 받아아와서 이를 다시 자바스크립트를 통해 그리는 것이었다. (글로서는 어려우니 아래의 영상을 보는 것이 도움이 될 것 같다)

​

​

따라서 결국 각자 로그인한 블로그에서 전체보기 탭에 조회수가 보이는 이유는 저런 방식으로 네이버 API를 통해 데이터를 받아와서 그려지기 때문에 우리가 확인할 수 있던 것을 의미한다.

​

​

잠깐 어떤 데이터들이 불러와지는 지를 확인해보면 아래와 같이 기본적인 포스트(게시물)의 제목와 조회수 그리고 게시물의 고유번호, 검색허용과 비허용 등의 여러 데이터들이 포함되어 있음을 확인할 수 있다.

​

이후 보다 자세한 사항은 이미 위에 기재한 원문을 보는 것으로 하고 이제 본론으로 넘어가 내 블로그의 게시물들의 조회수 랭킹을 확인해볼까 한다.(전체 코드는 맨 아래에 기재한다)

​

내가 진행하는 방법은 4단계로 구성된다.

​

1. 내 블로그에 기재된 전체 포스트 개수를 알아온다.

2. 그 포스트 개수를 기준으로 30개씩 잘라서 for loop를 돌면서 모든 데이터를 요청한다.

3. 각 데이터는 전처리하여 저장한다.

4. 최종 결과물을 조회수를 기준으로 sorting하여 출력한다.

​

​

1. 블로그 내 기재된 전체 포스트 개수를 알아오는 방법

```
function getBlogInfo(targetId) {
    let result = []
    let totalCount

    const xmlHttp = new XMLHttpRequest()
    const originURL = `https://blog.naver.com/PostTitleListAsync.naver?blogId=${targetId}`

    xmlHttp.open('GET', originURL, false)
    xmlHttp.send(null)

    totalCount = JSON.parse(
        xmlHttp.responseText.replace(/['<> \\]/g, '')
    ).totalCount
    
    return totalCount
}
```

2. 그 포스트 개수를 기준으로 30개씩 잘라서 for loop를 돌면서 모든 데이터를 요청(30개씩 자르는 이유는 데이터 요청시 한번에 요청할 수 있는 개수가 30개가 상한이기 때문이다, 전체보기 탭에서 30개씩 보기가 최대인 것을 확인해보면 된다)

```
function getBlogInfo(targetId) {
    let result = []
    let totalCount

    const xmlHttp = new XMLHttpRequest()
    const originURL = `https://blog.naver.com/PostTitleListAsync.naver?blogId=${targetId}`

    xmlHttp.open('GET', originURL, false)
    xmlHttp.send(null)

    totalCount = JSON.parse(
        xmlHttp.responseText.replace(/['<> \\]/g, '')
    ).totalCount

    // 전체 페이지 개수를 가져오는 currentPage 수로 나눈 나머지 + 1 만큼하면 모든 페이지를 가져온다.
    const range = Number(totalCount) % 30

    for (let i = 1; i < range + 1; i++) {
        var tempURL = `https://blog.naver.com/PostTitleListAsync.naver?blogId=${targetId}&viewdate=&currentPage=${i}&categoryNo=0&parentCategoryNo=0&countPerPage=30`

        // 포스트 가져오기
        xmlHttp.open('GET', tempURL, false)
        xmlHttp.send(null)

        let pages = xmlHttp.responseText
        let data = parseing(pages, targetId)

        result.push(...data)
        console.log(`Add ${data.length} items in result`)
    }

    return result
}
```

3. 각 데이터는 전처리하여 저장한다.(wan9s님의 코드를 참고하였다, 또한 전처리시에 검색비허용은 필터링함으로써 기존의 좋은 글들을 적으신 원문의 글들의 품질을 떨어뜨리는 행위를 방지하고자 하였다)​

```
function parseing(pages, targetId) {
    let data = pages.replace(/['<> \\]/g, '')
    let posts = JSON.parse(data).postList

    // 검색비허용 제외
    posts = posts.filter((item) => item.searchYn === 'true')

    // 필요한 데이터 추출
    return posts.map((item) => {
        var tempObj = {}
        // 날짜
        tempObj.date = item.addDate

        //  제목
        tempObj.title = decodeURI(item.title)
            .replace(/\+/g, ' ')
            .replace(/%23/g, '#')
            .replace(/%26/g, '&')
            .replace(/%2C/g, ',')
            .replace(/%2F/g, '/')
            .replace(/%3A/g, ':')
            .replace(/%3F/g, '?')
            .replace(/%3D/g, '=')
            .replace(/&#39%3B/g, "'")
            .replace(/&quot%3B/g, '"')
            .replace(/&%2339%3B/g, "'")

        // 조회수
        tempObj.readCount = Number(item.readCount.replace(",", ""))

        // URL
        tempObj.url = `https://blog.naver.com/${targetId}/${item.logNo}`
        return tempObj;
    })
}
```

4. 최종 결과물을 조회수를 기준으로 sorting하여 출력한다.

```
  return result.sort((a, b) => b.readCount - a.readCount)
```

---

최종 코드 및 방법 소개

이렇게 하면 최종적으로 아래의 코드가 작성된다. 여기서부터는 일반 블로거 분들도 따라할 수 있도록 쉽게 설명할까 한다. 먼저 아래의 코드를 쭉 복사하고 F12를 켜서 개발자 도구를 연다.

```
function getBlogInfo(targetId) {
    let result = []
    let totalCount

    const xmlHttp = new XMLHttpRequest()
    const originURL = `https://blog.naver.com/PostTitleListAsync.naver?blogId=${targetId}`

    xmlHttp.open('GET', originURL, false)
    xmlHttp.send(null)

    totalCount = JSON.parse(
        xmlHttp.responseText.replace(/['<> \\]/g, '')
    ).totalCount

    // 전체 페이지 개수를 가져오는 currentPage 수로 나눈 나머지 + 1 만큼하면 모든 페이지를 가져온다.
    const range = Number(totalCount) % 30

    for (let i = 1; i < range + 1; i++) {
        var tempURL = `https://blog.naver.com/PostTitleListAsync.naver?blogId=${targetId}&viewdate=&currentPage=${i}&categoryNo=0&parentCategoryNo=0&countPerPage=30`

        // 포스트 가져오기
        xmlHttp.open('GET', tempURL, false)
        xmlHttp.send(null)

        let pages = xmlHttp.responseText
        let data = parseing(pages, targetId)

        result.push(...data)
        console.log(`Add ${data.length} items in result`)
    }

    return result.sort((a, b) => b.readCount - a.readCount)
}

function parseing(pages, targetId) {
    let data = pages.replace(/['<> \\]/g, '')
    let posts = JSON.parse(data).postList

    // 검색비허용 제외
    posts = posts.filter((item) => item.searchYn === 'true')

    // 필요한 데이터 추출
    return posts.map((item) => {
        var tempObj = {}
        // 날짜
        tempObj.date = item.addDate

        //  제목
        tempObj.title = decodeURI(item.title)
            .replace(/\+/g, ' ')
            .replace(/%23/g, '#')
            .replace(/%26/g, '&')
            .replace(/%2C/g, ',')
            .replace(/%2F/g, '/')
            .replace(/%3A/g, ':')
            .replace(/%3F/g, '?')
            .replace(/%3D/g, '=')
            .replace(/&#39%3B/g, "'")
            .replace(/&quot%3B/g, '"')
            .replace(/&%2339%3B/g, "'")

        // 조회수
        tempObj.readCount = Number(item.readCount.replace(",", ""))

        // URL
        tempObj.url = `https://blog.naver.com/${targetId}/${item.logNo}`
        return tempObj;
    })
}


var result = getBlogInfo("YOUR BLOG ID")
console.table(result.slice(0, 10))

```

그럼 이제 아래처럼 어떤 창이 뜰텐데 나처럼 아래 뜨지 않는 이유는 오른쪽에 톱니바퀴 옆에 (...) 표시 눌러 Dock side를 바꾸면 원하는 형태로 볼 수 있다. 그리고 이후에 개발자 도구에 위치한 Console 탭을 눌러 위에 복사한 코드를 붙여넣기 한다.

그럼 이제 이렇게 될텐데 여기서 YOUR BLOG ID라고 적혀있는 부분은 각자 자기 블로그 아이디로 바꾼 뒤 enter를 누른다. 그리고 만약 순위를 10개 아닌 그 이상을 조회하고 싶다면 그 다음 줄에 있는  slice(0, 10)에서 10 대신 더 큰 값을 적으면 된다. (또한 현재 페이지에 내가 로그인한 상태여야 한다)

​

이렇게 하면 최종적으로 아래와 같이 테이블 형태로 내 블로그 포스트(게시물) 순위 상위 10개 데이터가 이렇게 출력이 된다. 우선적으로 날짜, 제목, 조회수, 주소만을 갖고 출력되도록 해두었다. 

​

이제 그 다음으로는 키자드없이 백링크를 쉽게 하기 위해 위와 같은 방식으로 내 URL를 추출해와서 쉽게 복사 붙여넣기로 각자 블로그를 백링크하는 방법을 연재할까 한다.

​

​

#블로그조회수확인 #네이버블로그 #조회수 #조회수순위 #조회수랭킹 #네이버블로그크롤링 #네이버블로그API #TIL 

