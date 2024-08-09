---
layout: post
title: "easyRandom - Java에서 테스트 객체 만들기"
sidebar_label: EasyRandom
parent: Java 라이브러리
grand_parent: Java
permalink: /docs/java/library/easyrandom
sitemap:
  lastmod: 2022-01-14
---

테스트 객체를 관리하는 패턴 중 [ObjectMother 패턴](/docs/pattern/object-mother)이 있다.  
java에서는 이 패턴을 구현하기 위한 방식으로 **EasyRandom**을 사용하면 효율적이다.

ObjectMother와 EasyRandom을 우리 팀 서비스 코드에 적용해 보았는데 적용 후 테스트 작성에 대한 효율이 눈에 띄기 좋아졌다.  
지금은 팀 내에서 ObjectMother 패턴이 자연스럽게 사용된다.  

## 장점

**ObjectMother 패턴**을 설명하는 페이지에도 적혀 있지만 이 간단한 패턴으로 얻은 명확한 장점들이 있다.

1. 이곳저곳 산개되었던 객체 생성 로직을 하나로 묶을 수 있었다.  
  - test Class/Method마다 객체를 만들던 로직이 있었는데, **ItemMother**와 같이 mother 패턴을 적용하면서 이런 로직이 사라졌다.
  - **Item**의 테스트 객체를 만들기 전에 **ItemMother**가 있는지를 보고 없으면 만들고 있으면 사용하는 방식.
2. 위와 같은 이유로 테스트 객체 생성에 드는 시간과 비용이 줄어들었고, 이는 테스트를 짜는 시간에 영향을 미쳤다.
2. 위와 같은 장점으로 완성도 높은 테스트 객체 생성 로직을 갖게 되었다.
  - 원래는 귀찮아서 대충 생성하던 것도 같은 생성 코드를 사용하기 때문에 점진적으로 완성도가 올라간다.
3. 객체 생성 로직이 숨겨지면서 가독성이 올라갔다.

우리 코드가 어떻게 되었고, 어떻게 바뀌었는지를 예를 들어서 설명해보겠다.  
예를 들면서 EasyRandom의 사용 방법도 설명한다.


## java에서 테스트 객체 만들기

우리가 테스트에서 만들었던 item 생성 코드들을 보자.

### 코드 sample 1

```java
    ItemDTO ItemDTO = new ItemDTO();
    ItemDTO.setCreatetime(0L);
    ItemDTO.setItemId("testItemId");
    ItemDTO.setOwner("testOwner");
```

- 테스트에서 이런 코드 반복이 많다. 언제까지 이런 코드를 **반복**할 것인가?
- 테스트의 value들이 random data가 아니다. 테스트가 특정 케이스만 커버할 수 있을지도 모른다. 모든 테스트가 random data로 이뤄져야 하는 건 아니지만 필요한 상황에 모르고 놓치는 경우보다 귀찮아서 안하는 경우일 때가 많다.

### 코드 sample 2

오래된 프로젝트의 테스트 코드에서 심심찮게 보이는 반복 호출을 위한 테스트 함수.

```java
public static ItemDTO createItemDTO() {
    ItemDTO dto = new ItemDTO();
    dto.setItemId("testItemId");
    dto.setCreatetime(0L);
    dto.setOwner("testOwner");

    return dto;
}
```

- 이전 코드보다 조금 낫다고 할 수 있지만 이런 코드틑 프로젝트 테스트의 곳곳에 있다.
- 누가 만들었는지, 있는지 없는지 조차 알지 못한다. 심한 경우는 test class 마다 존재한다.
- 여전히 **random value**는 아니다.

### 코드 sample 3

```java
private static ItemDTO initTestValue() {
    ItemDTO itemDTO = new ItemDTO();
    itemDTO.setCtime(RandomUtils.nextLong(100L, System.currentTimeMillis()));
    itemDTO.setItemId(RandomStringUtils.randomAlphanumeric(10));
    itemDTO.setOwner(RandomStringUtils.randomAlphanumeric(10));

    return itemDTO;
}
```

- 이 정도면 일종의 objectMother라고 할 수 있을 것 같다.
- 그렇지만 언제까지 random data를 **한땀 한땀** 넣어줄건지.
- 생성로직이 산개되어 있고 네이밍이 명확하지 않다는 문제는 여전하다. 즉 다른 사람이 동일한 코드를 다시 만들 것이다.

### Object Mother

ObjectMother는 테스트 객체의 생성에 대한 패턴을 제공하며 이는 눈에 띄는 확연한 약속으로 테스트 데이터 생성 로직의 산개를 막는다.  
테스트 코드 중복과 관리에 대한 문제를 [ObjectMother 패턴](/docs/pattern/object-mother)으로 풀어낼 수 있다.  

## EasyRandom

**ObjectMother**를 효율적으로 사용하기 위한 테스트 데이터를 생성하는 프로젝트들이 찾아보았다.

Naver에서 관리하고 있는 **FixtureMonkey** 도 있었고,  
약간은 올드한 네이밍의 **PODAM**,  
조금 궤가 다르지만 param test에 random하게 값을 채워주는 **AutoParams** 들을 사용해봤다.

가장 쓰기 편하고 효율적인 프로젝트는 **EasyRandom**이었다.  
EasyRandom은 github star 수도 가장 많았고, 이름 값 하는 프로젝트다.  


EasyRandom은 굉장히 강력한데 다음과 같은 특징들이 있다.  
1. **setter가 없어도 된다.**
2. **contructor가 없어도 된다**. (private contructor only인 경우)
3. 자동으로 **sub class들의 값도 random하게 채워준다.**
4. test object **list 생성이 간단하다.**

setter와 constructor가 없어도 된다는 점이 굉장히 좋았다.
- 가독성++

특정 entity의 경우 private consturctor만 갖고 factory에서 생성을 하는데, factory는 또 dto를 받는 번거로운 구조를 갖는 경우가 있었다.  
이런 경우 항상 테스트에서 dto 생성 후 entity를 만드는 test 이해도를 떨어뜨리는 작업을 했어야 했다.  
**EasyRandom**은 이런 단점들을 보완해준다.

## 사용법

우선 dependency를 추가한다.  

```xml
<dependency>
    <groupId>org.jeasy</groupId>
    <artifactId>easy-random-core</artifactId>
    <version>4.0.0</version>
</dependency>
```

### 기본 사용

```java
    EasyRandom generator = new EasyRandom();
    Person person = generator.nextObject(Person.class);
    List<Person> persons = generator.objects(Person.class, 5).collect(Collectors.toList());
```

간단하게 사용할 수 있고 List나 다른 Collection을 만들기도 쉽다.  

### parameter와 함께 사용

```java
    EasyRandomParameters parameters = new EasyRandomParameters();
    parameters.stringLengthRange(3, 3);
    parameters.collectionSizeRange(5, 5);
    EasyRandom generator = new EasyRandom(parameters);
    Person person = generator.nextObject(Person.class);
```

아주 간단하게 특정 param이나 value에 조건을 더할 수도 있다.

### 적용된 코드 예시

```java
public class ItemDTOMother {
  private static ItemDTO generate() {
    EasyRandom easyRandom = new EasyRandom();
    return easyRandom.nextObject(ItemDTO.class);
  }

  private static ItemDTO generateDeleted() {
    ItemDTO item = generate();
    item.setStatus("DELETED");
    return item;
  }
}
```

이렇게 되면 모두 동일한 생성 로직(`XXMother`)를 보게 되고 완성도 높고 재사용률 높은 테스트 코드가 완성된다.


## reference

- Quick Guide to EasyRandom, [https://www.baeldung.com/java-easy-random](https://www.baeldung.com/java-easy-random)
- EasyRandom github, [https://github.com/j-easy/easy-random](https://github.com/j-easy/easy-random)
