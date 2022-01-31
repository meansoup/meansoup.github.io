---
layout: post
title: ORMs
tag:
  - database
parent: db 개념
grand_parent: database
permalink: /docs/db/concept/orms
---

## ORM(Object Relational Mapping) 이란?

SQL Database를 사용하게 되면 아래와 같이 SQL query를 사용할 일들이 많아진다.  
```SQL
SELECT * FROM users WHERE email = 'meansoup@test.com';
```

**ORM**은 이런 복잡하고 번거로운 query들을 **Object-Oriented** 개념을 사용해서 data를 query/manipulate하는 기술을 말한다.
즉, SQL이 아니라 **우리가 사용하는 언어로 database를 사용하는 기술**이다.

예를 들면 Java의 ORMs의 표준 스펙인 **JPA**가 있다.  
- 난 ORMs를 정확히 몰랐는데, JPA를 생각하면 명확해진다.


## flow

![orm](/images/post/backend/orm.png)

ORM은 query를 작성해주는 소프트웨어라고 했다.  
위와 같이 코드로 작성된 object들이 ORM을 통해 database에 query로 변환된다.

## 예시

예를 들면 위의 query가 아래 java 코드처럼 접근이 가능하다.  
물론 간단한 setup이 필요하다.

```java
User findByEmail(String email);
```


## ORM 장점

### 원래 사용하던 언어를 사용할 수 있다.

- SQL은 powerful 하지만 훌륭하게 활용하지 못하는 경우가 많다.
- 그치만 원래 사용하던 언어들(Java ..)은 SQL보다 더 훌륭하게 활용할 수 있다.
- 함수를 호출하는 것 만큼 쉽다. (원래 db는 사용자 친화적이진 않으니까)
- 그래서 결국 가독섣이 굉장히 올라간다.

### 시간을 절약할 수 있다.

- ORM에서 제공하는 많은 feature들(transaction, connection pooling, streams)을 **out of the box**로 사용할 수 있다.
- 많은 기본적인 query들이 직접 query를 작성하는 것보다 효율적으로 동작한다.
- **DRY**로 데이터를 한 곳에서만 작성해서 유지 관리와 재사용이 쉽다.  
- 번거로운 SQL을 직접 작성하지 않아도 된다.

### 유연하다.

- database를 추상화할 수 있어 종속성이 줄어들고 database의 변경이 비교적 편하다.
- 코드를 작성하는 방식과 자연스럽게 연결된다.


## ORM 단점

- SQL을 훌륭하게 잘 쓴다면 더 좋은 성능의 query를 짤 수 있는 경우가 있다.
- ORM에서 수행할 수 없는 query도 존재한다.
- ORM을 배우기 위한 overhead가 있다.
- initial confiugration을 위한 작업들이 필요하다.
- ORM이 많은 것을 해주기 때문에 무슨 작업들이 ORM과 DB에서 벌어지는지에 대한 이해도가 떨어질 수 있다.


## 정리

**JPA**를 자주 사용하는 나한테 **ORM**의 개념은 굉장히 친숙하고 당연하기도 한 것 같다.  
**ORM**을 쓰면서도 일부 지원하지 않는 기능을 위한 **native query**를 작성하여 사용하고 있는데, 이런 방식이 가장 적절하지 않나 싶다.  

결국 ORM은 굉장히 유용하고 꼭 쓰여야 한다고 본다.
위에서 말한 단점처럼 DB query에 대한 이해도가 많이 줄어드는건 문제이긴 하다.



## 참고링크

[https://stackoverflow.com/questions/1279613/what-is-an-orm-how-does-it-work-and-how-should-i-use-one](https://stackoverflow.com/questions/1279613/what-is-an-orm-how-does-it-work-and-how-should-i-use-one)  
[https://blog.bitsrc.io/what-is-an-orm-and-why-you-should-use-it-b2b6f75f5e2a](https://blog.bitsrc.io/what-is-an-orm-and-why-you-should-use-it-b2b6f75f5e2a)  


각 언어별 유명한 ORM 소프트웨어 리스트.
- [https://en.wikipedia.org/wiki/List_of_object%E2%80%93relational_mapping_software#Java](https://en.wikipedia.org/wiki/List_of_object%E2%80%93relational_mapping_software#Java)
