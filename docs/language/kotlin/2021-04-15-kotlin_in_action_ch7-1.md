---
layout: post
title: "kotlin in action #7"
tag:
  - kotlin
parent: kotlin
grand_parent: language
permalink: /docs/algorithm/language/kotlin/kotlin-in-action-7-1
---

## chapter 7. Operator overloading and other conventions

## why convensions?

Java에서는 `Iterable`을 구현하면 `for` loop를 사용할 수 있고, `AutoCloseable`을 구현하면 `try-with-resources`를 사용할 수 있다.  
- Java는 이처럼 어떤 type인지가 중요함.

Kotlin에서도 Kotlin은 `plus` 라는 함수를 정의하면 `+` 연산자로 사용할 수 있는 등의 방식으로 유사한 특성을 제공한다.
- Kotlin 에서는 함수의 이름과 연관이 있다. 
- Kotlin이 이런 방식을 사용하는 건 기존의 Java class를 kotlin에 적용하기 위해서.
  - 새로운 class를 만들 수는 없지만 새로운 함수는 추가할 수 있으니까.

## Overloading arithmetic operators

BigInteger class나 Point class에서 `plus` 함수를 호출하는 대신 `+`로 사용하는 것이 이해하기에도 가독성 면에서도 좋다.  

예제를 보자.

```kotlin
data class Point(val x: Int, val y: Int) {
  operator fun plus(other: Point): Point {
    return Point(x + other.x, y + other.y)
  }
}
```
> val p1 = Point(10, 20)  
> val p2 = Point(30, 40)  
> println(p1 + p2)  
Point(x=40, y=60)

`plus` 함수 앞에는 `operator`가 꼭 붙어야 한다.
- 모든 operator를 정의할 때 필요함.
- 이게 없이 operator 함수 명들을 사용하면 `operator modifier is required`라는 에러가 발생.
- `a + b`는 내부적으로 `a.plus(b)`를 호출함.

### arithmetic operators

| expression | Function name |
|------------|---------------|
| a * b      | times         |
| a / b      | div           |
| a % b      | rem           |
| a + b      | plus          |
| a - b      | minus         |

operator overloading을 하더라도 연산자 우선순위가 적용된다.  
- `a + b * c`에서 `b * c`가 먼저 수행됨.

### different operand types

```kotlin
operator fun Point.times(scale: Double): Point {
return Point((x * scale).toInt(), (y * scale).toInt())
}
```
> val p = Point(10, 20)  
> println(p * 1.5)  
Point(x=15, y=30)

parameter의 type이 같지 않아도 된다.  
- 여기서도 역시나 `a * b`는 내부적으로 `a.times(b)`로 치환된다.
  - 중요한 것은 **교환 법칙**을 지원하지 않는다는 것.
    - 즉, `b * a`는 다른 식이고 위의 method에 적용될 수 없음.
    - 필요하다면 `operator fun Double.times(p: Point)` method를 정의해야 함

### different result type

```kotlin
operator fun Char.times(count: Int): String {
return toString().repeat(count)
}
```
> println('a' * 3)

aaa

유사하게 parameter들과 result의 type이 달라도 된다.  

### bit operator

kotlin은 standard number type에 대한 bit operator를 제공하지 않는다.  
bit 연산이 필요한 경우 아래 함수들을 사용한다.  

| java bit operator | kotlin method |
|:-----------------:|:-------------:|
|         <<        |      shl      |
|         >>        |      shr      |
|        >>>        |      ushr     |
|         &         |      and      |
|         \|        |       or      |
|         ^         |      xor      |
|         ~         |      inv      |

### assign operator

`+=`, `-=` 등의 함수들을 따로 정의할 수 있다.  
- `plusAssign`, `minusAssign`과 같은 함수

`+=` operator는 `plus`(a = a.plus(b)) 와 `plusAssign`(a.plusAssign(b)) 양쪽으로 컴파일될 수 있다.  
- 어떤 class가 이 두 함수를 모두 정의하고 둘 다 `+=`에 사용 가능한 경우 컴파일 에러가 발생. 
- class과 일관성있게 설계하는 것이 좋다.
  - `plus`와 `plusAssign`을 동시에 정의하는 것은 피하자.

`plus`의 경우 새로운 값을 반환하는 것이고,  
`plusAssign`의 경우 현재 값을 변경하는 것이다.  
- `Point`처럼 변경 불가능한 class라면 `plus`만 있는 것이 맞다.
- `builder`같이 변경 가능한 class를 설계한다면 `plusAssign`만 있는 것이 맞다.

kotlin collection은 `+`와 `+=`를 모두 제공한다.  
> val list = arrayListOf(1, 2)  
> list += 3  
> val newList = list + listOf(4, 5)  
> println(list)  
[1, 2, 3]  
> println(newList)  
[1, 2, 3, 4, 5]

### unary operator

| expression | function name |
|:----------:|:-------------:|
|     +a     |   unaryPlus   |
|     -a     |   unaryMinus  |
|     !a     |      not      |
|  ++a, a++  |      inc      |
|  --a, a--  |      dec      |

동일하게 unary operator에서도 overloading을 할 수 있다.  

## comparison operators

### equals

class에 대해 배울 때 kotlin은 [`==`로 `equals`를 호출한다](https://meansoup.github.io/2021/01/31/kotlin_in_action_ch4/#data-class)는 것을 배웠다.  
`!=`도 동일하게 equals를 호출한다.  

`kotlin`은 `==`에 대해서 null check를 하기 때문에 nullable 값에도 적용할 수 있다.
- java처럼 귀찮은 null 체크를 직접하거나 `equals` 내부에서 구현하지 않아도 됨.
- `a == b`가 `a?.equals(b) ?: (b == null)`로 컴파일 되기 때문.

```kotlin
class Point(val x: Int, val y: Int) {
  override fun equals(obj: Any?): Boolean {
    if (obj === this) return true
    if (obj !is Point) return false
    return obj.x == x && obj.y == y
  }
}
```

Point의 equals를 구현하면 위와 같다.  

equals는 `Any`에 정의된 `equals`를 `override` 하는 것이다.  
`Any`에는 `equals`를 `operator`를 붙이지만 여기서는 정의된 함수를 override하는 것이라서 `operator`를 붙이지 않아도 상위 class(Any)의 operator 지정이 적용된다.

### compareTo

Java에서는 `Comparable` interface를 구현해서 sort 등의 작업을 한다.  
- `e1.compareTo(e2)` 와 같이 명시  
Kotlin에서도 똑같은 `Comparable` interface를 지원하고, `compareTo` 함수를 호출하는 **convention**을 제공한다.
- `<`, `>`, `<=`, `>=`이 compareTo로 컴파일 됨.
- `a >= b`는 `a.compareTo(b) >= 0`
- `a < b`는  `a.compareTo(b) < 0`

```kotlin
class Person(val firstName: String, val lastName: String): Comparable<Person> {
  override fun compareTo(other: Person): Int {
    return compareValuesBy(this, other, Person::lastName, Person::firstName)
  }
}
```
> val p1 = Person("Alice", "Smith")  
> val p2 = Person("Bob", "Johnson")  
> println(p1 < p2)  

`equals`와 마찬가지로, `compareTo`가 `Comparable`에 정의되어 있으므로 `override`를 한다.  
`Comparable`을 구현하지 않고 `operator`를 붙일 수도 있다.  
`compareValuesBy`는 param으로 받은 함수의 결과를 0이 아닌 값이 나올 때까지 비교한다. 0이 아닌 값이 나오면 값을 반환하고, 끝까지 나오지 않으면 0을 반환한다.  

## conventions for collection & ranges

### index as get, set

`get`, `set`을 구현하면 index로 접근이 가능하다.  
- `print(x[a])`는 `print(x.get(a))`
- `print(x[a, b])`는 `print(x.get(a, b))`
- `x[a] = b`는 `x.set(a, b)`
- `x[a, b] = c`는 `x.set(a, b, c)`

`Map` `MutableMap`에는 `get`, `set`이 이미 있다.

```kotlin
operator fun Point.get(index: Int): Int {
  return when(index) {
    0 -> x
    1 -> y
    else -> throw IndexOutOfBoundsException("Invalid coordinate $index")
  }
}
```
> val p = Point(10, 20)  
> println(p[1])  
> 20  

`get`의 param으로 `Int`가 아닌 type도 사용할 수 있다.  
필요하다면 다른 type에 대해 overloading한 **get 함수를 여러 개 정의**할 수 있다.

```kotlin
data class MutablePoint(var x: Int, var y: Int)

operator fun MutablePoint.set(index: Int, value: Int) {
  when(index) {
    0 -> x = value
    1 -> y = vaule
    else -> throw IndexOutOfBoundsException("Invalid coordinate $index")
  }
}
```
> val p = MutablePoint(10, 20)  
> p[1] = 42  
> println(p)  
MutablePoint(x=10, y=42)  

### in

`contains`를 구현하면 `in`으로 접근이 가능하다.  
- `a in c`는 `c.contains(a)`

```kotlin
data class Rectangle(val upperLeft: Point, val lowerRight: Point)
  operator fun Rectangle.contains(p: Point): Boolean {
    return p.x in upperLeft.x until lowerRight.x && p.y in upperLeft.y until lowerRight.y
}
```
> val rect = Rectangle(Point(10, 20), Point(50, 50))
> println(Point(20, 30) in rect)  

true
> println(Point(5, 5) in rect)  

false

`10..20`은 10 <= x <= 20 의 범위를 확인하고,  
`10 until 20`은 10 <= x < 20 의 범위를 확인한다.  

### rangeTo

`rangeTo`를 구현하면 범위를 만들 때 사용하는 `..`로 접근이 가능하다.
- `a..b`는 `a.rangeTo(b)`
- `Comparable` interface를 구현하면 `rangeTo`를 정의할 필요가 없음.
  - kotlin standard library가 모든 `Comparable`에 적용가능한 `rangeTo`를 함수를 가지고 있음.
  - `operator fun <T: Comparable<T>> T.rangeTo(that: T) ClosedRange<T>`
  - `kotlin.ranges.ComparableRange` class를 보면 `rangeTo` 정의를 확인할 수 있음.
- `ClosedRange`는 범위를 가지고 있고 `contains`를 정의해서  `a in b..c`가 가능한 것.
  - `a in b..c` = `a in closedRange의 구현(b=start, c=end)` = `closedRange의 구현(b=start, c=end).contains(a)`

`rangeTo`는 다른 연산자보다 우선순위가 낮으나 괄호를 써주는게 이해하기 좋다.
- `0..n + 1`는 `0..(n + 1)`과 같음
- `0..n.forEach{}`는 우선순위 문제로 compile할 수 없음.
  - `(0..n).forEach{ print(it) }`

### iterator, for loop

for loop에서 사용하는 `for (x in list) { ... }`도 `in`을 사용하지만 `contains`와는 다르다.  
`list.iterator()`를 호출해서 java와 마찬가지로 hasNext와 next 호출을 반복하는 식으로 변환된다.  

Kotlin에서는 이 또한 convention으로 iterator 함수를 정의할 수 있다.  
- `String`의 상위 class `CharSequence`는 `iterator` 확장 함수를 정의한다.
- `operator fun CharSequence.iterator(): CharIterator`
- 따라서 `for (c in "abc") {}` 이 가능하다.

```kotlin
operator fun ClosedRange<LocalDate>.iterator(): Iterator<LocalDate> = object : Iterator<LocalDate> {
  var current = start
  override fun hasNext() = current <= endInclusive // compareTo 사용
  override fun next() = current.apply{ current = plusDays(1) }
}
```

> val newYear = LocalDate.ofYearDay(2017, 1)  
> val daysOff = newYear.minusDays(1)..newYear  
> for (dayOff in daysOff) { println(dayOff) }  

2016-12-31  
2017-01-01