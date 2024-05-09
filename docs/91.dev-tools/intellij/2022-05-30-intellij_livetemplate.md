---
layout: post
title: intellij 의미 없는 시간 줄이기 live template 편
sidebar_label: Intellij live template
parent: Intellij
grand_parent: Tools
permalink: /docs/dev-tools/intellij/live-template
sitemap:
  lastmod: 2022-05-30
---

intellij는 개발 시간을 단축할 수 있는 여러 기능들을 제공한다.  
그 중 내가 가장 많이 사용하는 것 중 하나가 **live template**이다.  

이게 뭔지는 중요하지 않다.  
써보면 안다.

### live template 확인하기

1. (ctrl + alt + s) 로 settings 진입
2. Editor > Live Templates
3. 각 언어 확인

여기서 각 언어를 들어가면 intellij에서 기본적으로 제공하는 live template 들을 확인할 수 있다.  
몇 개를 써보면 금방 감이 온다. 개발 시간을 단축시킬 수 있는 유용한 template 들이 많아서 template 리스트를 확인하는 것도 의미가 있다.  

<div class="code-example" markdown="1" style="font-size: 0.8em">
예시
{: .label .label-yellow}  

![live template basic](/images/post/dev-tools/intellij/live-template/live-template-basic.gif)

`sout`을 입력하고 enter 혹은 tab을 누르면 java에서는 `System.out.println();`이 완성된다.
</div>

이렇게 **자주 쓰이는 template들을 약어로 등록하는 것을 live template이라고 한다**.


### live template 설정하기

나는 TDD 개발에서 자주 사용하는 given-when-then template을 사용한다.  
이게 단순한데 매번 테스트 생성이 번거로워 live template으로 등록하는데 이걸 예로 들어보자.  

1. (ctrl + alt + s) 로 settings 진입
2. Editor > Live Templates
3. 언어 선택 -> kotlin
4. add

아래와 같이 **tm**, **tc**에 대해 추가하기

```kotlin
// Abbreviation: tm
// Description: make test method

@Test
fun $testname$() {
    // given
     
    // when
     
    // then
}
```

```kotlin
// Abbreviation: tc
// Description: make test class

@Nested
class $classname$ {
 
}
```

![tc tm 추가](/images/post/dev-tools/intellij/live-template/tc_tm.JPG)



### 동작 확인

간단하지만 정말 많은 시간을 줄일 수 있는 template.

![tc tm 확인](/images/post/dev-tools/intellij/live-template/tc_tm.gif)
