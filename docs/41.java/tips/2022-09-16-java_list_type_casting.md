---
layout: post
title: list type casting 하기
sidebar_label: list type casting 하기
parent: Java Tips
grand_parent: Java
permalink: /docs/java/tip/list-type-casting
sitemap:
  lastmod: 2022-09-16
---

이번에 작업하면서 list를 casting 할 일이 있었다.  
대충 표현하면 이런 코드.

```java
class A { /* ... */ }
class B extends A { /* ... */ }

List<A> items;
List<B> needs;
```

나는 B의 list가 필요한데 가져온 list는 A인 상황.

## stream

가장 먼저 생각난건 stream으로 변환하기.
```java
List<B> = items.stream().map(i -> (B) i).collect(Collectors.toList());
```

근데 이거 loop를 한 번 돌게 되는게 억울하다.  
그래서 찾아보았다.  


## generic type casting

결론부터 말하자면 이렇게 해결할 수 있다.

```java
List<B> = (List<A>) (List<?>) items;
```

이유는 A가 B의 parent 이지만 List<A>는 List<B>의 parent가 아니기 때문에 type casting이 되지 않는다.  
그치만 **List<A>, List<B> 모두 List<?>의 child 이기 때문에 type casting이 가능하다.**

![list casting](/images/post/java/tips/generics-listParent.gif)



### reference

- https://stackoverflow.com/questions/933447/how-do-you-cast-a-list-of-supertypes-to-a-list-of-subtypes  
- https://docs.oracle.com/javase/tutorial/java/generics/subtyping.html