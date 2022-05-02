---
layout: post
title: Spring Container
parent: Spring
permalink: /docs/spring/container
---

## DI(Dependency Injection)
의존성 주입.  
의존성을 넣는 것.  
대표적으로는 `setter`가 있음.  
[wiki](https://ko.wikipedia.org/wiki/%EC%9D%98%EC%A1%B4%EC%84%B1_%EC%A3%BC%EC%9E%85) 참고.  

결국 클래스와 객체 생성을 분리하여 유연성을 갖기 위한 방법.

## IoC(Inversion of Control)
제어의 역전.  
흐름 제어를 외부에서 가져가는 것.  
[wiki](https://ko.wikipedia.org/wiki/%EC%A0%9C%EC%96%B4_%EB%B0%98%EC%A0%84) 참고.  

다른 부분에 대해 배제하고 모듈에만 집중할 수 있다는 장점.  

## IoC Container
spring 에서는 의존성 제어로 DI의 역할도 가지고 있음.  
의존성 제어를 framework에서 하는 것을 말함.  

**container**에서 객체(Bean)를 생성/조립하고 - 메모리에 로드된 상태.  
java 코드에서 객체가 호출되어 사용하는 - `new`를 사용하지 않고 로드된 객체 사용.  

## Life Cycle

1. 스프링 컨테이너 생명 주기
```java
// container가 메모리에 생성됨.
GenericXmlApplicationContext ctx = new GenericXmlApplicationContext("classpath:applicationContext.xml");

// container 소멸
ctx.close();
```
2. 빈(Bean) 객체 생명 주기
container가 생성될 때 Bean이 생성되고, container 종료 시 객체가 소멸되기 때문에 continaer의 생명 주기와 같이 간다.  

3. InitializingBean, DisposableBean
Bean 생성/소멸 시점에 수행할 기능을 추가할 수 있음.  
```java
public class TestObj implements InitializingBean, DisposableBean {
    @Override
    public void afterPropertiesSet() throws Exception {
        System.out.println("do something when created");
    }
    @Override
    public void destroy() throws Exception {
        System.out.println("do something when destroyed");
    }
}
```

4. init-method, destroy-method
implements 사용과 동일하게 작동하고 어느게 더 좋다하는 것은 없음.  
```xml
<bean id="testObj" class="com.mean.TestObj"
init-method="initMethod" destroy-method="destroyMethod" />
```
```java
public class TestObj {
    public void initMethod() {
        System.out.println("do something when created");
    }
    public void destroy() {
        System.out.println("do something when destroyed");
    }
}
```

## 참고자료
[인프런 자바 스프링 프레임워크(renew ver.) - 신입 프로그래머를 위한 강좌](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-%ED%94%84%EB%A0%88%EC%9E%84%EC%9B%8C%ED%81%AC_renew/dashboard)의 DI / Life Cycle.