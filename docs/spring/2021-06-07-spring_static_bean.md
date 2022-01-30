---
layout: post
title: "static method class와 spring bean"
tag:
  - spring
parent: spring
permalink: /docs/spring/static-method-vs-bean
---

며칠 전 리팩토링을 위해 코드를 보던 중 이상한 걸 발견했다.  

`~validator`라고 명시된 두 개의 클래스가 같은 패키지에 있었는데,  
하나는 static method로 구성된 class였고 다른 하나는 bean으로 사용되고 있었다.  

어떤게 옳을까라는 판단은 금방내릴 수 있었다.  
**정확하게 어떤 근거**로 이런 판단을 내린걸까? 에 대해선 선뜻 대답이 되지 않았다.  

대부분의 개발자들이 감각적으로 내리는 이런 결정들은 옳은 것 같다.  

> 실제로 DDD를 공부하면서 배운 개발 방법들을 우리 팀에선 이미 해오고 있던 방식이 있던 것처럼 경험이 쌓인 개발자일수록 더더욱 그렇다.

---

구글링해보니, 생각보다 이런 토론이 많이 있었다.  
내가 내린 결론은 이렇다.  

1. static은 종속성이 없을 때, 객체 생성이 필요 없을 때 사용해야 한다.
2. 조금이라도 의존성이 외부에 있거나, 내부에서 외부에 접근하는 경우(property)엔 static을 사용하면 안된다.
3. 어떤 이유로든 input에 따른 output이 동일하지 않은 경우 static을 사용하면 안된다.

이렇게 static을 사용할 수 있는 경우를 확인하고 사용할 수 있다.  
위와 같이 static을 사용할 수 있을 때는 최대한 static을 사용하는 것이 좋을 듯 하다.

---

사실, 너무 당연한 이야기들이다.  
평소에 잠시 잊었을 뿐이지.  

명확한 기준에도 토론의 주제가 되는 것들이 있었다.  

1. dependency가 생길 수 있으니 bean으로 해야한다.  
이 경우는 static method를 사용하다가 dependency가 생겨서 bean을 사용해야할 경우, 변경이 너무 번거롭다는 주장.  
나는 **나중에 변경 될 것이라고 하는 미래의 변화를 예측하려고 하는건 잘못** 이라는 의견에 동의한다.  

2. 변경 될만한 로직을 정적 메소드로 구현하는게 맞나?  
이것도 위와 동일

3. bean이면 mock으로 쉽게 할 수 있는 테스트들이 static은 어렵다.  
나도 이런 경우를 겪어봤다. 실제로 테스트를 위해 bean으로 바꾸고 싶다는 생각도 했다.  
base64Utils 를 사용하는 함수에 대한 테스트를 작성할 때, 인코딩/디코딩 된 값들을 준비해놔야 테스트가 가능한 경우가 있었다.  
하지만 이런 테스트는 실제로 필요한 것 아닐까 싶다.  

---

실제로 `bean`과 `static method`의 목적을 보면 더 명확하게 사용할 수 있지 싶다.  

**bean**: 의존성 역전을 위해 사용
**static method**: 종속성이 없을 때, 객체 생성이 필요 없을 때 사용


## reference

[http://kwon37xi.egloos.com/4844149](http://kwon37xi.egloos.com/4844149)
[https://softwareengineering.stackexchange.com/questions/360525/dependency-injection-vs-static-methods](https://softwareengineering.stackexchange.com/questions/360525/dependency-injection-vs-static-methods)
[https://www.baeldung.com/spring-bean](https://www.baeldung.com/spring-bean)
[https://stackoverflow.com/questions/2671496/when-to-use-static-methods](https://stackoverflow.com/questions/2671496/when-to-use-static-methods)