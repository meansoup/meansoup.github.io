---
layout: post
title: intellij 의미 없는 시간 줄이기 test file 편
sidebar_label: intellij 의미 없는 시간 줄이기 test file 편
parent: Intellij
grand_parent: 개발도구
permalink: /docs/dev-tools/intellij/test-file-template
sitemap:
  lastmod: 2022-06-12
---

intellij는 개발 시간을 단축할 수 있는 여러 기능들을 제공한다.  
한 번 설정해두면 짜잘짜잘한 시간들을 아낄 수 있는 방법 중 하나는 test file 생성을 template화 하는 것이다.

이게 뭔지는 중요하지 않다.  
써보면 안다.

### 설정 확인하기

1. (ctrl + alt + s) 로 settings 진입
2. Editor > File and Code Templates
3. JUnit5 Test Class 확인

여기서는 어떤 test를 쓰느냐에 따라 다르다.  
JUnit5를 기준으로 설명한다.


### 이해하기

```java
import org.junit.jupiter.api.Assertions.*;

#parse("File Header.java")
class ${NAME} {
  ${BODY}
}
```

우선 설정을 보면 위와 같이 되어있는 것을 확인할 수 있다.  

이건 `import org.junit.jupiter.api.Assertions.*;`를 자동으로 import하고, class 골격을 만든다는 뜻이다.

기본적으로 source code에서 **Ctrl + Shift + T**를 누르면 template으로 생성된 test class file을 확인할 수 있다.

오늘 목표는 자주 사용되는 import 들을 미리 추가하는 것.


### 설정하기

위 template을 아래와 같이 바꾼다.  
나 같은 경우는 junit5의 기본 Test 등과 mock 설정을 위한 import를 추가했다.

```java
import org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.extension.ExtendWith;

import org.assertj.core.api.Assertions.assertThat;
import org.mockito.Mockito.*;
import org.mockito.Mock;
import org.mockito.InjectMocks;
import org.mockito.junit.jupiter.MockitoExtension;

#parse("File Header.java")
class ${NAME} {
  ${BODY}
}
```


### 이득

intelij에서는 간단하게 import를 할 수 있지만 테스트 클래스를 자주 생성하는 경우 은근히 도움이 된다.  
- 그리고 일단 귀찮지 않다.  

+ intelij에서는 **Optimize Import**를 하면 사용하지 않는 import는 모두 제거해주니까 추가해두는 것이 아무 문제가 되지 않는다.  
+ Junit5를 설정하면 Java, Kotlin 모두 적용된다.
