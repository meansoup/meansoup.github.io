---
layout: post
title: java serialize 사용할 때 주의사항
parent: Java Tips
grand_parent: Java
permalink: /docs/java/tip/java-serialize
---

java에서 serialize를 잘 사용하지 않는 편이다.  
그럼에도 사용해야 하는 경우가 있는데, 이번이 그랬다.

## serialize 단점

1. java에서 serialize를 한다면 java 외의 다른 언어에서 deserialize할 수 없다.
    - 언어에 제약이 생기게 된다. batch나 다른 작업에도 java 밖에.
2. java serialize는 serialized된 data의 크기가 크다.
    - package / class 정보가 포함되기 때문에 다른 serialize 알고리즘 보다 무겁다.
3. 실수하기 쉽다.
    - 오늘 다루려고하는 부분인데 실수하기 쉽다.
    - serialize 하는 class에 손을 대는 경우 이미 만들어놓은 serialize 데이터가 deserialize가 불가능할 수 있다.


## 그럼에도 사용하는 경우

serialize의 장점은 **별도의 라이브러리가 필요없는 것** 하나 밖에 없다.
아주 형편없는 것. :weary:  

그럼에도 사용하는 경우는 **기존 모듈에서 사용하는 경우** 하나 뿐인 것 같다.

새로 합류한 팀에서 java serialize를 사용하고 있었고, 덕분에 serialize에 대해 다시 생각해볼 기회가 되었다.  
그 전에 serialize가 필요하면 성능(압축률과 시간, cpu 점유)을 비교해서 알고리즘을 선택했었는데, 그 중 java serialize는 없었다.  
특정 성능이 아주 중요하고, java serialize가 그걸 만족한다면 사용할 수도 있을 것 같으나 일반적으로 사용하진 않는다.


## serialize의 주의사항

오늘 정리하려고 했던 내용.  
serialize는 단점이 많지만 일단 사용한다면 별 수 없다.  
**실수하기 쉽다**는 부분을 커버하기 위해.

1. [serialVersionUID를 고정한다.](#serialVersionUID를-고정한다)
2. [package 이동에 주의한다.](#package-이동에-주의한다)
3. [테스트를 작성한다.](#테스트를-작성한다)

### serialVersionUID를 고정한다

property 추가 혹은 제거 등의 이유로 java class가 변하게 되면 `serialVersionUID`가 변하게 된다.  
**`serialVersionUID`는 serialize/deserialize에 사용되기 때문에 이 값이 바뀌지 않도록 고정**하는 것이 java serialize를 사용할 때 필수이다.

```java
// 임의의 값으로 고정
private static final long serialVersionUID = 1234567L;
```

### package 이동에 주의한다

내가 이번에 당했던 이슈는 이거다.  
legacy 프로젝트를 hexagonal과 ddd에 맞춰 리팩토링을 진행하면서 package를 옮겼더니 장애가 발생했다.

다행히 [InputStream에서 `readClassDescriptor()`를 조작](https://stackoverflow.com/questions/2358886/how-can-i-deserialize-the-object-if-it-was-moved-to-another-package-or-renamed)함으로써 문제를 해결할 수 있었다.  
이게 되게 재미있는 부분이었는데 stream을 쓰지 않다보니 package 이동이 문제가 된다는걸 모르고 있었던 것.  
실수가 발생하기 참 좋은 구조인 것 같다.

### 테스트를 작성한다

그래서 이런 문제들을 해결하려면 테스트가 필요하다.  
내가 리팩토링하면서 작성했던 테스트들은 변경된 구조에서의 serialize & deserialize.

그런데 java serialize를 사용한다면 **현재 알고리즘으로 serialized string을 만들어 놓고 이걸 수정된 로직에서 deserialize 하는 것을 테스트**할 수 있어야 한다.  
그니까 테스트는 이럴거다.

```java
@Test
void deserializeTest() {
   String serialized = "abcde.............."; // 현재 개발과 별개로 이전에 serialize 해놓은 데이터
   Object deserializedObject = Serializer.deSerialize(serialized);
}
```

이렇게 테스트를 작성하면 혹여 serialVersionUID가 바뀌었든, package가 바뀌었든 모두 커버할 수 있는 테스트를 갖게된다.


## 오늘의 결론

:x: java serialize 사용하지 마라.


### reference

- serialVersionUID 관련
  - https://www.baeldung.com/java-serial-version-uid
- package 이동 관련
  - https://stackoverflow.com/questions/2358886/how-can-i-deserialize-the-object-if-it-was-moved-to-another-package-or-renamed