---
layout: post
title: Token Passing Operator in C++
tag:
  - c++
parent: c++
grand_parent: language
permalink: /docs/algorithm/language/cpp/token-passing-operator
sitemap:
  lastmod: 2019-09-23
---

일하면서 신가하게 본 cpp 코드에 대해서 정리해보려고 한다.  
오늘 처음 본 것은 아닌데, **Token pasting operator**라는 이전엔 듣도 보도 못한 operator가 있더라.  

### token passing operator란
[MS docs](https://docs.microsoft.com/ko-kr/cpp/preprocessor/preprocessor-operators?view=vs-2019)에 정의된 내용을 보면,
전처리 연산자로 @define과 함께 사용되는 operator이다[^1]. 토큰을 다른데 붙여서 사용한다는건데, 예제를 보지 않으면 선뜻 이해하기 어려운 개념이다.  
실제 처음 코드를 봤을 땐, 이런 문법이 있나 싶더라..  

### 기본 예제
```cpp
#include <stdio.h> 
#define token(base, postfix) base##postfix 

int main(void) { 
	int testval = 5000;
	printf("%d", token(test, val));

	return 0; 
}
```
가장 기본적인 예제는 위와 같다. base에 postfix를 붙여주는 방식으로 token passing operator가 사용된다.  
이런 코드는 응용해서 사용하면 이해하기 불편할 수 있지만 새로운 사용성을 제시한다.

### 응용 예제
```cpp
#define TO_VALID(name) { \
    name##_valid = true; \
}

#define PUT_IF_VALID(name, value) { \
    if(name##_valid) { \
        name = value; \
    } \
}

int test;
int game;
bool test_valid = false;
bool game_valid = false;

TO_VALID(test);
PUT_IF_VALID(test, 5000);
PUT_IF_VALID(game, 5000);
```
위와 같이 define을 함수화시켜서 서로 다른 여러 개의 name에 대해 접근할 수 있다.

### 주의 사항
1. `define`의 option처럼 사용되는 것으로, 일반문에서 사용할 수 없다.
2. 기본적으로 사용되는 변수들은 이미 정의되어 있어야 한다.
3. 아래와 같은 코드도 사용가능하지만, 추천하지 않는다.
```cpp
#define VAL_NAME(base, postfix) base##postfix
int token(test, val) = 3;
printf("%d", testval);
```

-----
[^1]: 여기에 나온 `#`, `#@` operator들은 개념이 정말 쉬운데, 내 리눅스 pc에서는 빌드되지 않더라..(왜지?) 사실 그닥 사용성이 애매한 operator들일 것 같아(실제로 의미있게 쓰이는데가 있는지도 잘 모르겠다) 이번 포스팅에 정리하지 않는다.
