---
layout: post
title: "Object Mother, 테스트에 가장 중요한 패턴"
sidebar_label: "Object Mother"
parent: Test
permalink: /docs/pattern/object-mother
sitemap:
  lastmod: 2024-03-13
---

이번엔 **ObjectMother**라는 패턴에 대해서 정리한다.  
**ObjectMother**는 우리가 코드를 개발하면서 한 번쯤은 생각해봤고, 또 편의를 위해 조금씩은 작성해봤을 내용의 패턴이다.  
사실 패턴이란게 다 그렇지 않나 싶다.

간단히 표현하자면 test object를 만들어주는 class라고 할 수 있을 것이다.  
패턴을 잘 정의하는 [Martin Fowler의 글](https://martinfowler.com/bliki/ObjectMother.html)을 참고해서 정리해본다.

## Object Mother 란?

테스트에 사용되는 여러 **example objects**를 생성하는데 도움을 주는 클래스이다.  

테스트를 작성할 때 많은 예제 데이터가 필요하고,  
이런 **data set**을 **test fixture**라고 부른다.

여러 테스트 클래스에서 유사한 **data**가 필요한 경우가 많다.  
테스트 시점에서 **standard fixtures**를 만들 수 있는 **factory object**를 만드는 것이 합리적이다.  
**Object Mother**는 이런 factory를 말한다.

이렇게 만들어진 object는 일부 test case에서는 적절하지 않을 수 있다.  
그렇지만 Folwer는 이런 경우에서 조차도 새로운 object 생성보다 **Object Mother**로 생성한 객체를 수정하는 방향이 더 이해하기 쉽다고 말한다.  

- 참고로 Object Mother라는 단어는 **Thoughtworks** 프로젝트에서 처음 쓰였다.


## Object Mother 장 단점

장 단점은 오역의 여지가 없도록 <u>ThoughWorks 논문</u>[^1]의 내용을 그대로 발췌했다.

### 장점

1. Simplified and standardized test object creation
2. Ease of maintenance, because test object creation is entrusted to a specific class or group of classes.
3. test object clean-up.
4. the pattern recovers even greater amounts of time that would otherwise be spent writing and maintaining unit tests.
5. by removing a significant hurdle from the test-writing process, ObjectMother encourages developers to write more tests.

### 단점

1. added time spent building the pattern

### 주의 사항

ObjectMother 패턴의 힘은 강력하다.  
프로젝트에 도입한 뒤 팀원들은 자발적으로 ObjectMother에 테스트 객체를 추가하기 시작했다.  

그러나 ObjectMother를 온전히 이해하지 못하고 작성하는 Mother 패턴들은 ObjectMother의 본질을 흐리게 한다.  
ObjectMother는 **standard fixtures**를 만드는 것이다.  
개념을 온전히 이해하지 못하고 사용하는 경우엔 standard fixture를 만드는 것이 아니라 모든 fixture를 Object Mother에 추가하는 경우가 많다.  
**standard fixture가 아니라 아무 fixture나 추가된 ObjectMother는 사용되지 않는 것보다는 낫지만 Mother 패턴의 가독성과 신뢰성, 확장성을 많이 떨어뜨린다.**


### Java에서 objectMother 적용하기

ObjectMother를 공부하면서 [Java에서 ObjectMother 패턴 적용](/docs/java/library/easyrandom)하기 위해 도움이 되는 라이브러리들을 찾아보았고, 실제 우리 팀 코드에 적용을 해 보았다.  
굉장히 간단한데 실제 패턴을 적용해서 얻는 이점이 많았다. java에서 적용하며 얻은 이점들은 위 페이지에 정리한다.  

-----
[^1]: Thoughtworks 논문 [ObjectMother, Easing Test Object Creation in XP](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.18.4710&rep=rep1&type=pdf) 참고
