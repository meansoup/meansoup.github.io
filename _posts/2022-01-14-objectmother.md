---
layout: post
title: "Object Mother Pattern과 java"
tag:
  - Object Mother
  - Java
---

이번엔 `ObjectMother`라는 패턴에 대해서 정리한다.  
`ObjectMother`는 우리가 코드를 개발하면서 한 번쯤은 생각해봤고, 또 편의를 위해 조금씩은 작성해봤을 내용의 패턴이다.  
사실 패턴이란게 다 그렇지 않나 싶다.

간단히 표현하자면 test object를 만들어주는 class라고 할 수 있을 것이다.  
패턴을 잘 정의하는 **Martin Fowler**의 글을 참고해서 정리해본다.

## Object Mother 란?

테스트에 사용되는 여러 `example objects`를 생성하는데 도움을 주는 클래스이다.  

테스트를 작성할 때 많은 예제 데이터가 필요하고,  
이런 `data set`을 `test fixture`라고 부른다.

여러 테스트 클래스에서 유사한 `data`가 필요한 경우가 많다.  
테스트 시점에서 `standard fixtures`를 만들 수 있는 `factory object`를 만드는 것이 합리적이다.  
`Object Mother`는 이런 factory를 말한다.

이렇게 만들어진 object는 일부 test case에서는 적절하지 않을 수 있다.  
그렇지만 Folwer는 이런 경우에서 조차도 새로운 object 생성보다 `Object Mother`로 생성한 객체를 수정하는 방향이 더 이해하기 쉽다고 말한다.  

- 참고로 Object Mother라는 단어는 **Thoughtworks** 프로젝트에서 처음 쓰였다.


## Object Mother 장 단점

장 단점은 오역의 여지가 없도록 `ThoughWorks` 논문의 용을 그대로 발췌했다.

### 장점

1. Simplified and standardized test object creation
2. Ease of maintenance, because test object creation is entrusted to a specific class or group of classes.
3. test object clean-up.
4. the pattern recovers even greater amounts of time that would otherwise be spent writing and maintaining unit tests.
5. by removing a significant hurdle from the test-writing process, ObjectMother encourages developers to write more tests.

### 단점

1. added time spent building the pattern


## reference

martinfowler의 `ObjectMother`
- [https://martinfowler.com/bliki/ObjectMother.html](https://martinfowler.com/bliki/ObjectMother.html)  

Thoughtworks 논문 '`ObjectMother, Easing Test Object Creation in XP`'
- [http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.18.4710&rep=rep1&type=pdf](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.18.4710&rep=rep1&type=pdf)


---


## java에서 테스트 객체 만들기

이제 그럼 java에서 효율적으로 object mother를 사용해보자.

### 실제 코드 sample 1

```java
    ItemDTO ItemDTO = new ItemDTO();
    ItemDTO.setCtime(0L);
    ItemDTO.setItemId("testItemId");
    ItemDTO.setOwner("testOwner");
```

문제가 많다.
- 테스트에서 이런 코드 반복이 많다. 언제까지 이런 코드를 **반복**할 것인가?
- 모르고 놓치는 경우보다 귀찮아서 안 하는 경우들이 참 많은데 **random value**도 아니다.

### 실제 코드 sample 2

오래된 프로젝트의 테스트 코드에서 심심찮게 보이는 반복 호출을 위한 테스트 함수.

```java
public static ItemDTO createItemDTO(){
    long crrntTime = System.currentTimeMillis();
    Meta meta = MetaTest.create();

    ItemDTO dto = new ItemDTO();
    dto.setItemId(itemId);
    dto.setCtime(crrntTime);
    dto.setMtime(crrntTime);
    dto.setOwner(owner);
    dto.setLastmodifier(owner);

    dto.setMeta(meta.getMeta());
    dto.setStatus(Status.CREATED);

    return dto;
}
```

아직 문제가 많다.
- 이런 코드가 프로젝트 **곳곳**에 있다.
  - 누가 만들었는지, 있는지 기억도 못하기 때문에
  - 심한 경우는 test class 마다 존재하기도 한다
- 여전히 **random value**는 아니다.
  - 값을 받아오기엔 random으로 해야할 게 많고, randomUtil로 모두 넣기 귀찮았나보다.

### 실제 코드 sample 3

```java
private Usage initTestValue() {
    uid = RandomStringUtils.randomAlphanumeric(10);
    imageCount = RandomUtils.nextInt(100, 1000);
    videoCount = RandomUtils.nextInt(100, 1000);
    imageSize = RandomUtils.nextLong(100L, 1000L);
    videoSize = RandomUtils.nextLong(100L, 1000L);

    return new Usage(uid, imageCount, videoCount, imageSize, videoSize);
}
```

조금은 쓸만하다.
- 이 정도면 일종의 objectMother라고 할 수 있을 것 같다.
- 그치만 언제까지 random으로 **한땀 한땀** 넣어줄건지.


## EasyRandom

**ObjectMother**의 역할을 하는 프로젝트들이 찾아보니 몇 개 있었다.  
굉장히 유명하고 보편적으로 사용되는 프로젝트들은 아니지만 흥미로웠다.

Naver에서 관리하고 있는 `FixtureMonkey` 도 있었고,  
약간은 올드한 네이밍의 `PODAM`,  
조금 궤가 다르지만 param test에 random하게 값을 채워주는 `AutoParams` 들을 사용해봤다.

가장 쓰기 편하고 효율적인 프로젝트는 `EasyRandom`이었다.
- 이름 값 한다.
- star 수도 가장 많았다.

`EasyRandom`은 굉장히 강력한데, 내가 사용하며 확인된 사항은 다음과 같다.
1. **setter가 없어도 된다.**
2. **contructor가 없어도 된다**. (private contructor only인 경우)
3. 자동으로 **sub class들의 값도 random하게 채워준다.**
4. test object **list 생성이 간단하다.**

setter와 constructor가 없어도 된다는 점이 굉장히 좋았다.
- 가독성++

특정 entity의 경우 private consturctor만 갖고 factory에서 생성을 하는데, factory는 또 dto를 받는 번거로운 구조를 갖는 경우가 있었다.  
이런 경우 항상 테스트에서 dto 생성 후 entity를 만드는 test 이해도를 떨어뜨리는 작업을 했어야 했다.  
`EasyRandom`은 이런 단점들을 보완해준다.

### 사용법

1. add dependency

```xml
<dependency>
    <groupId>org.jeasy</groupId>
    <artifactId>easy-random-core</artifactId>
    <version>4.0.0</version>
</dependency>
```

2. use

```java
    EasyRandom generator = new EasyRandom();
    Person person = generator.nextObject(Person.class);
    List<Person> persons = generator.objects(Person.class, 5).collect(Collectors.toList());
```

굉장히 간단하다.  
List(필요하다면 다른 colletions)를 만들기도 쉽다.  
위에서 언급한 장점들까지 고려한다면 random value object 생성을 한 줄에!

3. use with param

```java
    EasyRandomParameters parameters = new EasyRandomParameters();
    parameters.stringLengthRange(3, 3);
    parameters.collectionSizeRange(5, 5);
    EasyRandom generator = new EasyRandom(parameters);
    Person person = generator.nextObject(Person.class);
```

특정 param이나 value에 조건을 더할 수도 있다.  
- 아주 간단하게.


## reference

Quick Guide to EasyRandom
- [https://www.baeldung.com/java-easy-random](https://www.baeldung.com/java-easy-random)

EasyRandom github
- [https://github.com/j-easy/easy-random](https://github.com/j-easy/easy-random)
