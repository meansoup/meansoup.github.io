---
layout: post
title: "Object Mother"
parent: Test
permalink: /docs/pattern/object-mother
sitemap:
  lastmod: 2022-01-14
---

이번엔 **ObjectMother**라는 패턴에 대해서 정리한다.  
**ObjectMother**는 우리가 코드를 개발하면서 한 번쯤은 생각해봤고, 또 편의를 위해 조금씩은 작성해봤을 내용의 패턴이다.  
사실 패턴이란게 다 그렇지 않나 싶다.

간단히 표현하자면 test object를 만들어주는 class라고 할 수 있을 것이다.  
패턴을 잘 정의하는 **Martin Fowler**의 글을 참고해서 정리해본다.

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

장 단점은 오역의 여지가 없도록 **ThoughWorks** 논문의 내용을 그대로 발췌했다.

### 장점

1. Simplified and standardized test object creation
2. Ease of maintenance, because test object creation is entrusted to a specific class or group of classes.
3. test object clean-up.
4. the pattern recovers even greater amounts of time that would otherwise be spent writing and maintaining unit tests.
5. by removing a significant hurdle from the test-writing process, ObjectMother encourages developers to write more tests.

### 단점

1. added time spent building the pattern


### Java에서 objectMother 적용하기

ObjectMother를 공부하면서[Java에서 ObjectMother 패턴 적용](/docs/java/library/easyrandom)하기 위해 도움이 되는 라이브러리들을 찾아보았고,  
실제 우리 팀 코드에 적용을 해 보았다.  
굉장히 간단한데 실제 패턴을 적용해서 얻는 이점이 많았다.

## reference

martinfowler의 **ObjectMother**
- [https://martinfowler.com/bliki/ObjectMother.html](https://martinfowler.com/bliki/ObjectMother.html)  

Thoughtworks 논문 '**ObjectMother, Easing Test Object Creation in XP**'
- [http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.18.4710&rep=rep1&type=pdf](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.18.4710&rep=rep1&type=pdf)
