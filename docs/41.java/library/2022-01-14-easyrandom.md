---
layout: post
title: "easyRandom - Java에서 테스트 객체 만들기"
parent: Java 라이브러리
grand_parent: Java
permalink: /docs/java/library/easyrandom
sitemap:
  lastmod: 2022-01-14
---

Java에서 테스트 객체를 만드는걸 고민하다가 [ObjectMother 패턴](/docs/pattern/object-mother)에 대해서 공부하게 되었다.  
그러고 찾은게 바로 **EasyRandom**.
- mother 패턴을 모른다면 한 번은 공부하고 가면 좋겠다.

ObjectMother와 EasyRandom을 팀 내에 소개했는데 이를 적용하고 테스트 작성에 대한 효율이 눈에 띄기 좋아졌다.  
- 지금 우리 팀원들은 테스트 작성할 때 무조건 이 방식을 사용하는 정도.

장점이 몇 가지 있는데,  
1. 이곳저곳 산개되었던 객체 생성 로직을 하나로 묶을 수 있었다.  
  - test Class/Method마다 객체를 만들던 로직이 있었는데, `ItemMother`와 같이 mother 패턴을 적용하면서 이런 로직이 사라졌다.
  - `Item`의 테스트 객체를 만들기 전에 `ItemMother`가 있는지를 보고 없으면 만들고 있으면 사용하는 방식.
2. 위와 같은 이유로 테스트 객체 생성에 드는 시간과 비용이 줄어들었고, 이는 테스트를 짜는 시간에 영향을 미쳤다.
2. 위와 같은 장점으로 완성도 높은 테스트 객체 생성 로직을 갖게 되었다.
  - 원래는 귀찮아서 대충 생성하던 것도 같은 생성 코드를 사용하기 때문에 점진적으로 완성도가 올라간다.
3. 객체 생성 로직이 숨겨지면서 가독성이 올라갔다.

우리 코드가 어떻게 되었고, 어떻게 바뀌었는지를 예를 들어서 설명해보겠다.  
예를 들면서 EasyRandom의 사용 방법도 설명한다.


## java에서 테스트 객체 만들기

우리가 테스트에서 만들었던 item 생성 코드들을 보자.

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
private static ItemDTO initTestValue() {
    ItemDTO itemDTO = new ItemDTO();
    itemDTO.setCtime(RandomUtils.nextLong(100L, System.currentTimeMillis()));
    itemDTO.setItemId(RandomStringUtils.randomAlphanumeric(10));
    itemDTO.setOwner(RandomStringUtils.randomAlphanumeric(10));

    return itemDTO;
}
```

조금은 쓸만하다.
- 이 정도면 일종의 objectMother라고 할 수 있을 것 같다.
- 그치만 언제까지 random으로 **한땀 한땀** 넣어줄건지.

그리고 생성로직이 산개되어 있고 네이밍이 명확하지 않다는 문제는 여전하다.

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
    return item
  }
}
```

이렇게 되면 모두 동일한 생성 로직(`XXMother`)를 보게 되고 완성도 높고 재사용률 높은 테스트 코드가 완성된다.


## reference

Quick Guide to EasyRandom
- [https://www.baeldung.com/java-easy-random](https://www.baeldung.com/java-easy-random)

EasyRandom github
- [https://github.com/j-easy/easy-random](https://github.com/j-easy/easy-random)
