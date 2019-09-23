---
layout: post
title: Test-Driven Development 03
tag:
  - TDD
---

## chapter 6

### 죄 지우기
이 전에([ch5](blog/2019/09/16/tdd_book_02/#chapter-5)) 저지른 죄(복붙!)를 청소해야 한다.  
가능한 방법은 `Franc`이 `dollar`를 상속하거나, 공통 부모를 갖도록 하는 방법이 있을 것이다.  
프랑이 달러를 상속해? 말도 안되보이고, 실제 구현해보면 얻을 이득이 없다는 것을 깨달을 것이다. 공통 분모를 갖는 방향으로 수정을 해 나간다.  
```java
class Money {
    protected int amount;
}

class Dollar extends Money {
}
```

### 죄 지우기2
[ch3](blog/2019/09/16/tdd_book_02/#chapter-3)에서 만든 `equals()`는 Dollar와 Franc에 모두 남아있을 것이다. 이 함수를 `Dollar` class에서 지우고, `Money` class에서 아래와 같이 수정한다.
```java
public boolean equals(Object object) {
    Money money = (Money) Object;
    return amount == money.amount;
}
```

그러면 뭐가 안됐나 보니까, Franc.equals()에 대한 테스트가 없었으므로 ch3에서 수정한 테스트 코드도 아래와 같이 수정해준다.  
```java
public void testEquality() {
    assertTrue(new Dollar(5).equals(new Dollar(5)));
    assertFalse(new Dollar(5).equals(new Dollar(6)));
    assertTrue(new Franc(5).equals(new Franc(5)));
    assertFalse(new Franc(5).equals(new Franc(6)));
}
```
왜 하는지 모르겠더라도 이런 테스트들을 작성한 후에 코드를 수정하도록 해야한다. 작성하고 보니, Dollar와 Franc가 거의 동일한 테스트를 중복해서 하고 있다. 이런 죄들을 `반드시 지워야만`{:.yelhglt} 한다. Franc도 `Dollar`class와 동일하게 `equals()`를 고칠 수 있고, 결국 `Money` class의 equals와 동일한 함수가 나와 코드를 제거할 수 있을 것이다.

근데 참 찝찝하다.. Franc와 Dollar의 비교는 어찌할 것인가.. 일단 뒤로 미루도록 한다.

### 여태까지
- 공통된 코드를 첫 번째 클래스(Dollar)에서 상위 클래스(Money)로 `단계적으로 옮겼다`{:.yelhglt}.
- 두 번째 클래스(Franc)도 Money의 하위 클래스로 만들었다.
- 불필요한 구현을 제거하기 전에 두 equals() 구현을 일치시켰다.

## chapter 7

### 미뤄둔 죄
앞서 미뤄둔 죄를 해결하기 위한 테스트를 작성한다.  
```java
public void testEquality() {
    assertTrue(new Dollar(5).equals(new Dollar(5)));
    assertFalse(new Dollar(5).equals(new Dollar(6)));
    assertTrue(new Franc(5).equals(new Franc(5)));
    assertFalse(new Franc(5).equals(new Dollar(6)));
}
```
당연히 테스트는 실패한다. 우선 빠르게 문제를 해결하면 아래와 같이 수정할 수 있다.
```java
public boolean equals(Object object) {
    Money money = (Money) object;
    return amount == money.amount && getClass().equals(money.getClass());
}
```

### 여태까지
- 결함을 끄집어내서 테스트로 만들었다.
- 완벽하지 않지만 봐줄만하게 테스트를 통과시켰다.
- 더 많은 동기가 있기 전에 더 많은 설계를 도입하지 않기로 했다.

그런데 참.. 한 챕터에 별로 하는게 없는 것 같다.

## chapter 8
Money class의 하위 클래스 Dollar, Franc가 하는 일이 별로 없으므로, 아예 제거하고 싶다. 이를 제거하기 위해서 단계적으로 진행해본다.  

### Factory Method
하위 클래스에 대한 직접적인 참조가 적어진다면 하위 클래스를 제거하기 위한 방향이라고 볼 수 있다. Money에 Dollar를 반환하는 Factory Method를 도입할 수 있다.  
```java
static Dollar dollar(int amount) {
    return new Dollar(amount);
}

public void testMultiplication() {
    Money five = Money.dollar(5);
    assertEquals(Money.dollar(10), five.times(2));
    assertEquals(Money.dollar(15), five.times(3));
}
```
1. five의 생성이 Money의 Factory Method를 참조한다.
2. Dollar에 대한 참조가 사라지길 바라므로, `Dollar five = ~`를 `Money five = ~`로 바꾼다.
3. 앗.. Money.times() 를 구현해야 된다.
4. assertEquals에서 사용하는 Dollar의 생성도 Factory Method를 참조한다.
5. 이제 `어떤 client code도 Dollar라는 이름의 하위 클래스가 있다는 사실을 알지 못한다`{:.yelhglt}.
6. `하위 클래스의 존재를 테스트에서 분리하여 어떤 모델 코드에도 영향을 주지 않고 상속 구조를 변경할 수 있게 되었다`{:.yelhglt}.

