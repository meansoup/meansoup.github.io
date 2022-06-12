---
layout: post
title: intellij 의미 없는 시간 줄이기 live template 편
parent: intellij 설정하기
grand_parent: 개발툴
permalink: /docs/dev-tools/intellij/live-template
---

intellij는 개발 시간을 단축할 수 있는 여러 기능들을 제공한다.  
그 중에 가장 많이 사용하는 것 중 하나가 **live template**이다.  

이게 뭔지는 중요하지 않다.  
써보면 안다.

### 설정 확인하기

1. (ctrl + alt + s) 로 settings 진입
2. Editor > Live Templates
3. 각 언어 확인

여기서 각 언어를 들어가면 intellij에서 기본적으로 제공하는 live template 들을 확인할 수 있다.  
몇 개를 써보면 금방 감이 온다.  

<div class="code-example" markdown="1" style="font-size: 0.8em">
예시
{: .label .label-yellow}  

예를 들면 `sout` 이라고 입력하고 enter 혹은 tab을 치면 (설정에 따라 다름)  

kotlin에서는 `println()`이,  
java에서는 `System.out.println();`이 완성되는 것을 확인할 수 있다.
</div>

이렇게 **자주 쓰이는 template들을 약어로 등록하는 것을 live template이라고 한다**.  
기본적으로 제공하는 것 중 `iter` 등을 사용하기도 한다.



### 설정하기

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
