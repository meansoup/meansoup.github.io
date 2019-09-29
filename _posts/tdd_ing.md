## chapter 11
여태까지의 작업들로, 하위 클래스 Dollar, Franc에는 이제 생성자 밖에 남지 않았다. 생성자 때문에 하위 클래스가 있을 필요는 없으므로 하위클래스를 제거한다.

### 하위 클래스 제거
코드의 의미를 변경하지 않으면서, 하위 클래스에 대한 참조를 상위 클래스에 대한 참조로 변경할 수 있다. 먼저 factory method를 고치도록 한다.  
```java
// Money class, franc 에 대한 factory class도 동일하게 수정
static Money dollar(int amount) {
    return new Money(amount, "USD");
}
```

이렇게 되면, `Franc`는 지울 수 있는데, 다른 테스트에서 `new Dollar`를 사용하는 곳이 남아있다.
[testDifferentClassEquality()](blog/2019/09/25/tdd_book_03/#times-refactoring-2)에서 동치성 비교에 사용하고 있었다.  
[testEquality()](blog/2019/09/25/tdd_book_03/#Factory-Method)에서 충분히 테스트 되고 있는 것 같다. 사실상 Money class로 통합되었으므로 과한 테스트를 수정해 아래와 같이 중복을 지울 수 있겠다.  
```java
public void testEquaility() {
    assertTrue(Money.dollar(5).equals(Money.dollar(5)));
    assertFalse(Money.dollar(5).equals(Money.dollar(6)));
    assertFalse(Money.dollar(5).equals(Money.franc(5)));
}
```
삭제 및 정리의 근거:  
- testDifferentClassEquality() 는 클래스 대신 currency를 비교하도록 하는 코드로, 여러 클래스가 존재할 경우 의미가 있다. 클래스를 지우는 현재에 의미가 없는 테스트이다.
- `Dollar`와 `Franc`에 대한 별도의 테스트가 존재하지만, 클래스가 두 개 일때는 차이가 있을 수 있었지만, 통합된 로직상에서 별도의 테스트는 필요 없다.

### 여태까지
- 하위 클래스를 삭제했다.
- 기존 구조에 필요했지만, 변경된 구조에서 필요없는 테스트도 삭제했다.

## chapter 12
우리의 할일 목록엔 `$5 +10CHF = $10 (환율 2:1인 경우)`와 같은 덧셈이 있다.  
전체 더하기 기능을 어떻게 시작해야 할지 모르겠으니, `$5 + $5 = $10`과 같은 간단한 예부터 시작해보자.

### 간단한 덧셈
당연히 테스트부터 만든다.
```java
public void testSimpleAddition() {
    Money sum = Money.dollar(5).plus(Money.dollar(5));
    assertEquals(Money.dollar(10), sum);
}
```

plus에 대한 구현은, 이전에 배운 것처럼 우선은 사기(가짜 구현) 치듯 `Money.dollar(10)`을 return할 수도 있겠지만, 어떻게 해야할 지가 명확하므로 구현해버린다.  
```java
Money plus(Money addend) {
    return new Money(amount + addend.amount, currency);
}
```

### 환율 고려
환율을 고려한 덧셈의 방식에는 여러가지 방식이 있을 것이다. Money와 비슷하게 동작하지만, 두 Money의 합을 나타내는 객체를 만드는 것..  
저자는 여기서 두 가지 메타포를 생각했다.  
1. Money의 합을 지갑처럼 가지고 있어, 서로 다른 금액과 통화가 존재
2. 각 통화와 금액을 환율에 맞춰 수식으로 존재

두 번째 방법으로 진행한다. 이럴 경우 Money가 수식의 가장 작은 단위가 될 것이며, 연산의 결과로 Expression들이 생기고, 그 중 하나에 더한 값이 나올 것이다.

### 환율 고려 2
TDD 논리에 따라 테스트를 작성해 나간다. 테스트 작성이 제일 중요한 듯 하다.  

1. 환율을 적용함으로써 얻어지는 reduced를 사용한다.
  ```java
  public void testSimpleAddition() {
      ...
      assertEquals(Money.dollar(10), reduced);
  }
  ```
2. 환율이 적용되는 곳은 bank니까
  ```java
  public void testSimpleAddition() {
      ...
      Money reduced = bank.reduce(sum, "USD");
      assertEquals(Money.dollar(10), reduced);
  }
  ```
  - 왜 `Money`가 아닌 `Bank`가 `reduce()`를 맡아야 하는가?
    - Expression(여기선 Money들의 수식)는 여기서 핵심이고, 핵심이 되는 객체가 다른 부분에 대해서 될 수 있는 한 모르도록 해야, 유연하고, 테스트하기 쉽고, 재활용이나 이해하기 쉽다.
    - Expression과 관련된 오퍼레이션이 많을 것이고, 모든 오퍼레이션을 Expression에만 추가하면 무한히 커질 수 있기 때문이다.
    - 만약 Bank가 별 필요가 없다면, 기꺼이 Expression으로 구현을 옮길 수도 있다.
3. 당장은 bank가 할 건 없다. 객체 하나만 있으면 된다.
  ```java
  public void testSimpleAddition() {
      ...
      Bank bank = new Bank();
      Money reduced = bank.reduce(sum, "USD");
      assertEquals(Money.dollar(10), reduced);
  }
  ```
4. 두 Money의 합은 Expression이어야 한다.
  ```java
  public void testSimpleAddition() {
      ...
      Expression sum = five.plus(five);
      Bank bank = new Bank();
      Money reduced = bank.reduce(sum, "USD");
      assertEquals(Money.dollar(10), reduced);
  }
  ```
5. $5 만들기.
  ```java
  public void testSimpleAddition() {
      Money five = Money.dollar(5);
      Expression sum = five.plus(five);
      Bank bank = new Bank();
      Money reduced = bank.reduce(sum, "USD");
      assertEquals(Money.dollar(10), reduced);
  }
  ```

### 컴파일하기
와.. 이걸 컴파일 해야한다.

1. Expression이 필요하다. cllass보다 inteface가 가벼우니까 interface로 만든다.
  `interface Expression`
2. `Money.plus()`가 Expression을 구현해야 한다. Expression에는 아직 아무 구현도 없으니까..
  `Class Money implements Expression`
3. Bank class와 `reduce()` 함수가 필요하다.
   ```java
   class Bank
   Money reduce(Expression source, String to) {
       return null;
   }
   ```
4. 이제 컴파일이 되고, 테스트가 바로 실패한다.
5. 오.. 이제 가짜 구현을 할 수 있다.
6. 가짜!
   ```java
      Money reduce(Expression source, String to) {
       return Money.dollar(10);
   }
   ```
7. 테스트 통과! 리팩토링할 준비가 되었다.

### 여태까지
- 큰 테스트($5 + 10CHF)를 작은 테스트($5 + $5)로 줄여서 발전을 보일 수 있었다.
- 필요한 계산(Expression)에 대한 가능한 메타포들을 신중히 생각해보았다.
- 새 메타포를 기반으로 기존의 테스트를 재 작성했다.
- 테스트를 빠르게 컴파일했다.
- 테스트를 실행했다.
- 진짜 구현을 위한 리팩토링을 기다린다.

## chapter 13
모든 중복을 제거해야 테스트를 완료했다고 말할 수 있다. 코드 중복은 없더라도, 데이터 중복이 있을 경우에도 제거해주어야 한다.  
가짜구현 [`Money.dollar(10)`](#컴파일하기)은 테스트 코드에 있는 `five.plus(five)`와 데이터 중복이라고 볼 수 있다.  
우리는 Money들에 대한 연산을 `수식으로 존재`{:.yelhglt}하게 만들어 주기로 했으므로 덧셈의 결과가 Money가 아닌 수식으로 존재해야 한다.

### Sum
plus에 대한 연산의 결과는 [Money를 반환](#간단한-덧셈)하였지만, 이건 엄연히 말하면 수식으로 존재하는 것이 아니고, Sum과 같은 Expression으로 존재해야 한다[^1].
두 Money의 합은 Sum이어야 한다.  
```java
public void testPlusReturnsSum() {
    Money five = Money.dollar(5);
    Expression result = five.plus(five);
    Sum sum = (Sum) result;
    assertEquals(five, sum.augend);
    assertEquals(five, sum.addend);
}
```
우선 테스트를 작성했다. 이 테스트는 오래가지 못할 것이다. 연산의 외부 행위가 아닌 내부 구현에 너무 깊게 관여하기 때문이다. 그래도, 테스트를 통과하면 우선 한 걸음 나아간 것이다.  
실행해보면 에러가 계속 날거고, 통과하기 위해 아래와 같은 수정이 필요하다.  
```java
// Sum class 생성
class Sum {
    Money augend;
    Money addend;
}
// Money class
Expression plus(Money addend) {
    return new Sum(this, addend);
}
```
또, Sum의 생성자도 필요하고, Sum은 Expression이어야 한다.
```java
// Sum class
class Sum implements Expression
Sum(Money augend, addend) {
    this.augend = augend;
    this.addend = addend;
}
```

이제, `testSimpleAddition()`에서 `Bank.reduce()`는 Sum을 전달받는다. sum으로 받는 통화가 모두 같고, reduce로 얻을 통화도 같다면, 결과는 sum의 money들을 합친 값이어야 한다.  
```java
public void testReduceSum() {
    Expression sum = new Sum(Money.dollar(3), Money.dollar(4));
    Bank bank = new Bank();
    Money result = bank.reduce(sum, "USD");
    assertEquals(Money.dollar(7), result);
}
```
테스트에 대한 코드는,  
```java
//Bank class
Money reduce(Expression source, String to) {
    Sum sum = (Sum) source;
    int amount = sum.augend.amount + sum.addend.amount;
    return new Money(amount, to);
}
```
와 같이 구현될 수 있을텐데 이 코드는 두 가지 이유로 지저분하다[^2].  
1. 캐스팅(형변환), 이 코드는 모든 Expression에 대해 작동해야 한다.
2. 두 단계에 거친 reference.

아래와 같이 메서드를 Sum 내부로 옮길 수 있을 것이다.  
```java
//Bank class
Money reduce(Expression source, String to) {
    Sum sum = (Sum) source;
    return sum.reduce(to);
}
//Sum class
public Money reduce(String to) {
    int amount = augend.amount + addend.amount;
    return new Money(amount, to);
}
```

### reduce
위의 테스트는 통과했고, 위 코드에 더 할 것이 명확하지 않으니 새로운 할 일을 확인하여 테스트를 생성한다.  
`reduce(Money)`의 경우에 대한 테스트이다.  
```java
public void testReduceMoney() {
    Bank bank = new Bank();
    Money result = bank.reduce(Money.dollar(1), "USD");
    assertEquals(Money.dollar(1), result);
}
```

해결 코드:  
1. 지저분하다.
  ```java
  //Bank class
  Money reduce(Expression source, String to) {
      if (source instanceof Money) return (Money) source;
      Sum sum = (Sum) source;
      return sum.reduce(to);
  }
  ```
2. 한 걸음[^3].
  ```java
  //Bank class
  Money reduce(Expression source, String to) {
      if (source instanceof Money) return (Money) source.reduce(to);
      Sum sum = (Sum) source;
      return sum.reduce(to);
  }
  //Money class
  public Money reduce(String to) {
      return this;
  }
  ```
3. 깔끔하다.
  ```java
  //Expression
  Money reduce(String to);
  // Bank class
  Money reduce(Expression source, String to) {
      return source.reduce(to);
  }
  ```

### 여태까지
- 중복이 제거되기 전까지 테스트를 통과한 것으로 치지 않았다.
- 앞으로 필요할 것으로 예상되는 객체(Sum)의 `생성을 강요하기 위한 테스트`{:.yelhglt}를 작성했다.
- 빠른 솓도로 객체 구현을 시작했따.
- 한 곳에서 캐스팅을 이용해 구현했다가, `테스트 통과 후 적당한 자리로 코드를 옮겼다`{:.yelhglt}.

## chapter 14

### 환전
단순한 변환을 생각하면 2Franc이 있는데 이것을 Dollar로 바꾼다고 생각해보자. 자 테스트는 이미 만들었다.  
```java
public void testReduceMoneyDifferentCurrency()) {
    Bank bank = new bank();
    bank.addRate("CHF", "USD", 2);
    Money result = bank.reduce(Money.franc(2), "USD");
    assertEquals(Money.dollar(1), result);
}
```
테스트 통과를 위해 아래와 같은 코드를 작성할 수 있다.  
```java
//Money class
public Money reduce (string to) {
    int rate = (currency.equals("CHF") && to.equals("USD")) ? 2 : 1;
    return new (Money(amount / rate, to));
}
```
문제는, Money가 환율을 알아선 안된다는 것. Bank가 알아야할 부분이고, `각 객체가 해야할 역할에 정확하고 독립적이어야 한다`{:.yelhglt}.




131p

-----
[^1]: 그니까, sum 안에 두 값이 있다면, sum은 두 값의 합이라는 식을 나타내는 객체가 되는 것이니까. 현재의 plus는 수식이 완료된 값을 반환하므로 구현하기로 한 방향과 맞지 않다.  
[^2]: TDD지만 객체지향적 개념을 배워가는 것 같다. 이런 개념들이 기본적으로 필요하단 말이겠지.  
[^3]: 이렇게 느리고 맘에 안들게 한 걸음씩 밟아가야 하는 것인가..