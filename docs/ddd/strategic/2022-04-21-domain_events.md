---
layout: post
title: 도메인 이벤트 (Domain Events)
parent: 전략적 설계
grand_parent: Domain Driven Design
nav_order: 5
permalink: /docs/ddd/strategic/domain_events
---

*일단 **domain events**를 사용하는 법을 알고나면 이에 중독되서 어떻게 **domain events** 없이 살아왔는지 의아해질 것이다. - Vaughn Vernon*


### event란?

우선 event가 뭔지 알아보자.  
event에는 이런 특성들이 있다.

1. event란 과거에 발생한 것을 말한다.
  - 그렇기 때문에 항상 과거형으로 쓰인다.
  - 요청과 혼동하기 쉽기 때문에 과거형을 지키는 것이 좋다.
2. event는 변경할 수 없다.
  - 이미 발생했기 때문에 바꿀 수 없다.
3. event는 한 번만 발생할 수 있다.
  - 다시 발생하더라도 이건 다른 event이다.


## domain event란?

말 그대로 domain에서 발생한 event.  
domain의 변화를 다른 곳에 알리기 위해 event로 만드는 것이다.  

domain event도 domain model의 일부이다.  
domain event는 aggregate에 의해 생성된다.  

아래와 같은 장점 때문에 사용된다.

### 장점

domain의 변경에 대한 side effect를 명시적으로 구현할 수 있다.
- 유비쿼터스 언어에 기반한 도메인 규칙을 도메인 이벤트로 명시적으로 표현할 수 있는 것.


### domain event 맞나?

event와 domain event를 헷갈리기 쉽다.  
아래와 같은 조건들로 domain event 인지 파악하는데 참고할 수 있다.

#### 맞는 근거

1. stakeholders와 business가 관심이 있나? 
2. 우리 system에서 결정된 event 인가?

#### 틀린 근거

1. 기술적인 이슈인가? 
2. bounded context 밖에서 일어났나? 
3. system에 대한 요청인가?
  - 이건 command 이지 event가 아니기 때문


---


### domain event 뽑기

1. ... 할 때
2. 이런 일이 일어나면 ...
3. ... 하면

과 같은 경우 domain event modeling을 해야할 가능성이 크다.

### modeling 하기

event를 전달하는 목적이 크기 때문에 event는 보통 immutable이고 모델링이 간단하다.

앞서 말했듯 과거에 발생했다는 것을 이름에 반영하는게 중요하다.

발생한 시점(date)이 들어가는 편이고,  
그 외의 event의 의미를 나타내기 위한 속성들이 무엇이 필요한지 생각해봐야 한다.


### 이벤트 발행

domain model이 event messaging infra에 노출(coupling)되어선 안된다.

### publisher

publisher는 domain이 modeling 되지 않는다.  
즉, DomainEventPublisher는 모든 domain event를 받아서 처리해줄 수 있지, 특정 domain model과 연결되지 않는다는 것이다.

### subscriber

domain event의 handling은 application이 해야할 일이다.  
domain은 domain logic에만 집중하기 때문이다.  
event handler나 side-effect action들은 domain이 신경쓰지 않는다.  

### diagram

![sequence](/images/post/ddd/strategic/events_sequence.JPG)

위 sequence에서 **aggregate**가 `publish()` 하지만,  
**DomainEventPublisher**가 `publish()`를 받아서 **DomainEventSubscriber**에게 전달한다.  

![class](/images/post/ddd/strategic/events_class.JPG)

publisher는 여러 subscriber에게 event를 전달할 수 있다.  
event를 어떻게 처리하는지는 subscriber(application service)의 몫이다.  

그림에 나오진 않지만 마찬가지로 publisher도 aggregate 들의 event를 받을 수 있다.  
그래서 domain이 들어가서는 안된다.


---


### event 생성과 전달을 분리하기

transaction을 commit 하기 직전에 event를 handler에 전달하는 방식이 바로 event를 전달하는 것보다 좋다.

1. event 바로 전달되면 side-effect이 클 수 있고, domain model을 test하기 어렵다.
2. event 발생과 handler로 보내는 작업을 분리할 수 있다.
3. 발생과 전달을 분리하면 model 캡슐화에 도움이 된다.
4. event 전달에 유연성을 준다.


### reference

- https://lostechies.com/jimmybogard/2014/05/13/a-better-domain-events-pattern/
- https://docs.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/domain-events-design-implementation
- https://serialized.io/ddd/domain-event/
- Implement Domain Driven Design (chapter8 Domain Events), Vaughn Vernon
