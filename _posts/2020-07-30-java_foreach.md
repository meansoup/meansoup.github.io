---
layout: post
title: java foreach
tag:
  - java
  - performance
---

요새 `stream`을 쓰다보면 참 편리하기도하고 코드가 짧아져 가독성도 좋아지니 기분이 좋다.  
그런데 `stream.foreach()`란 녀석은 사실 `for ( : )`문과 비교하여 코드야 한 두줄 줄일 수 있더라도 가독성을 헤친다는 느낌이 되려 들더라.  

*performance에서는 차이가 없을까?* 하여 조금 찾아보았다.

## 결론

결국 `for ( : )`이 성능적으로 더 좋다는 것이다.  
그니까 `stream.foreach()`는 stream을 효율적으로 사용하고 이것과 연계되어 사용할때 사용하는 것이 좋겠다.  

## 내용

1. 성능 떨어진다.
  - 오버헤드 발생으로 성능이 더 떨어진다.
2. 가독성 떨어진다.
  - 나만 그런게 아니구나.. 대부분 나쁘진 않더라도 좋지는 않다더라.
3. 디버깅 어렵다.
  - 내부적으로 JVM과 library가 할 일이 많아져서 error stack이 지저분하다.
4. 제한적인 요소가 있다.
  - `final`이 아닌 변수를 사용할 수 없다.
  - 예외처리에 불편함이 있다.
  - `return`, `continue`, `break`와 같은 flow control을 할 수 없다.
  - parallel 하게 실행될 수 있다.

## 참고자료

- [stackoverflow foreach() vs for loop](https://stackoverflow.com/questions/16635398/java-8-iterable-foreach-vs-foreach-loop)  
- [homeefficio님의 "for-loop를 Stream.forEach()로 바꾸지 말아야 할 3가지 이유" 번역문](https://homoefficio.github.io/2016/06/26/for-loop-%EB%A5%BC-Stream-forEach-%EB%A1%9C-%EB%B0%94%EA%BE%B8%EC%A7%80-%EB%A7%90%EC%95%84%EC%95%BC-%ED%95%A0-3%EA%B0%80%EC%A7%80-%EC%9D%B4%EC%9C%A0/)  