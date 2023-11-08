---
layout: post
title: jekyll gh page 폰트 설정하기
permalink: /docs/blog/font
parent: blog
grand_parent: Etc
---

## TL;DR

jekyll theme 마다 font custom이 다를 수 있다.  
검색은 참고만 하되 기본적으로는 theme guide 페이지와 github 코드를 보자.

## font 적용 안되는 경우

github blog를 다시 관리하기 시작하면서 참 맘에 안드는 부분이 글씨체다.  
tistory나 국내 서비스 블로그들은 알아서 이쁜 폰트들을 제공하지만 github은 아니니까.  
**기본 폰트 킹받는다**.

페이지에 폰트를 적용하기 위해 부단한 노력을 했다.  
역시나 구글에 검색을 많이 했는데 내 검색어는 다음과 같다.  
- jekyll font
- jekyll 폰트
- jekyll 한글 폰트
- jekyll github font
- ...

결론을 말하자면 여기서 나온 해결책들이 나한텐 하나도 적용되지 않았다.  
아마 이런 사람들이 많지 않을까?

## font 적용 안되는 이유

jekyll은 테마마다 포맷들이 참 다르다.  
이전에 내가 사용하던 유명한 테마인 lanyon이랑 현재 사용하는 just-the-docs 테마랑은 페이지를 꾸며주는 포맷부터 다르니까.  

그러니까,  
**css를 custom으로 적용하는 방식도 다른 경우가 제법 된다**는 것이다.  
그래서 위의 방식들이 나한텐 통하지 않았다.

## 해결책

나 같은 경우는 해답을 테마 가이드 페이지에서 찾았다.  
- [jekyll custom theme guide page](https://pmarsceill.github.io/just-the-docs/docs/customization/)
- 아니면 github directory 구조에서도 힌트를 얻는다 ([theme gitub code](https://github.com/pmarsceill/just-the-docs/tree/master/_sass))

몇 번이고 봤던 페이지인데도 대충봐서 놓쳤던 것을.. 한참 시간을 버리고서야 다시 보게 되었다.  
가이드를 따라서 해결한 나의 [코드](https://github.com/meansoup/meansoup.github.io/blob/master/_sass/custom/custom.scss)는 아래와 같다.

```scss
// path: /_sass/custom/custom.scss

@font-face {
    font-family: 'GowunDodum-Regular';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2108@1.1/GowunDodum-Regular.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}

p, a, h1, h2, h3, h4, h5, h6 {
    font-family: "GowunDodum-Regular";
}
```

## font list 참고

[https://noonnu.cc/font_page](https://noonnu.cc/font_page)