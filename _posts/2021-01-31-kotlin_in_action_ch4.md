---
layout: post
title: "[Kotlin in action #4] Classes, Objects and Interface"
tag:
  - kotlin
---

## chapter 4.

### interface

interface가 abstract method와 non-abstract method를 모두 가질 수 있다.  
- java 8과 비슷. abstrat & default method  
그치만 어떤 state도 가질 수 없다.  

```kotlin
interface Clickable {
    fun click()
    fun showOff() = print("I'm clickable!") // default 명시자가 필요 없음
}

class Button: Clickable {
    override fun click() = println("I was clicked")
}
```
- kotlin에서는 `override` 사용이 강제된다.(역할은 java의 `@Override`와 동일.

java와 유사하게 interface의 implements는 여러 개가 가능하고, class extends는 하나만 가능하다.

동일한 non-abstract method를 갖는 interface 여러 개를 implements 하는 class는 override가 강제로 필요하다.
- 특정 interface를 super 하는 방법은 `super<Clickable>.showOff()`


### modifier

open, final, abstact

java에서는 final을 명시하지 않으면 class 상속이 가능하다.  
이런 경우 의도치 않은, 잘 명시되지 않은 class에 대한 상속을 하게 될 수 있다.  
상속 이후 parent class가 변경되어 child class가 의도한 동작을 하지 않는 **fragile base class** 문제가 발생할 수 있다.
- 이런 문제가 있었고, <Effective Java> 등에서 상속을 의도하지 않는 경우 모두 final로 쓰라는 제안을 한다.
- kotlin은 default를 `final`로 쓰고 상속을 허용하려면 `open`을 명시해야 한다.
- class open 뿐 아니라 open class의 상속받을 method에도 open을 명시해야 한다.
- `override`를 명시한 경우 기본적으로 open 이다.

abstract class는 open이 없어도 된다. java와 유사하다.
```kotlin
abstract class Animated {
    abstract fun animate() // override 꼭 필요
    open fun stopAnimating() {} // override 가능
    fun animateTwice() {} // override 불가
}
```


### visibility modifier

|Modifier|Class member|Top-level declaration|
|---|---|---|
|public (default)|Visible everywhere|Visible everywhere|
|internal|Visible in a module|Visible in a module|
|protected|Visible in subclasses|(can not used)|
|private|Visible in a class|Visible in a file|

- kotlin은 기본적으로 public 이다.
- package private이 kotlin에는 없다.
  - kotlin에게 package는 namespace 관리용 정도.
- `internal`이 kotlin엔 존재하는데, 모듈(maven, gradle 등의 프로젝트 모듈) 내에서만 쓰일 수 있게 해서 **encapsulation**을 지원한다.
  - module은 java의 package와는 다르다. module은 여러 package가 있을 수 있음.
- java에서는 같은 package 안에서 protected 멤버에 접근할 수 있지만, kotlin에서는 그렇지 않다.


### inner & nested class

|Class A declared within another class B|In Java|In Kotlin|
|---|---|---|
|Nested class (doesn't store a reference to an outer class)|static class A|class A|
|Inner class(stores a reference to an outer class|class A|inner class A|

- kotlin은 default가 nested class.
- kotlin inner class에서 outer class에 접근하려면 `this@{OuterClassName}`을 써야 함.


### sealed class

`sealed`를 붙이면 클래스 상속을 제한한다.
- 제한하는데, 클래스 외부의 상속을 막는 것.

```kotlin
sealed class Expr {
    class Num(val value: Int) : Expr()
    class Sum(val left: Expr, val right: Expr) : Expr()
}
```

- 이렇게 내부에 상속만 가능
- `when(classVar)`처럼 쓸 때, else가 하위 class에 대한 예외 처리로 default로 들어가야 한다.
  - `sealed`를 명시하면 클래스 상속이 제한되니 else가 필요 없다.
  - 이런 방식은 class가 추가되었을 때에 대한 예외를 까먹지 않을 수 있다는 장점이 있음.


### primary constructor

```kotlin
class User constructor(_nickname: String) {
    val nickname: String

    init { nickname = _nickname }
}

class User(_nickname: String) {
    val nickname = _nickname
}

class User(val nickname: String)
```

위 방식 모두 primary constructor를 만드는 방식이다.  
class name과 괄호로 싸여진 코드를 primary constructor라고 한다.  

class 정의 시 constructor를 별도로 생성하지 않으면 컴파일러가 default costructor(class())를 만들어준다.

primary constructor에 private을 붙여서 외부에서 instance 생성을 막을수도 있다.
- `class Secretive private constructor() {}`


### secondary constructor

```kotlin
open class View {
    constructor(ctx: Context) { /* code */ }
    constructor(ctx: Context, attr: AttributeSet) { /* code */ }
}
```

- 위처럼 View에 `()`가 없으니 primary는 선언하지 않았다고 볼 수 있다.

secondary constructor는 `constructor`로 시작한다.  
필요에 따라 여러 개를 생성해도 된다.  


### properties declared in interfaces

```kotlin
interface User {
    val nickname: String
}

class PrivateUser(override val nickname: String) : User
class SubscribingUser(val email: String) : User {
    override val nickname: String
    get() = email.substringBefore('@')
}
class FacebookUser(val accountId: Int) : User {
    override val nickname = getFacebookName(accountId)
}
```

property의 override를 위처럼 할 수 있다.

```kotlin
interface User {
    val email: String
    val nickname: String
    get() = email.substringBefore('@')
}
```

점점 예제 없이 설명이 안된다...
property의 getter/setter를 구현할 수도 있으나, field가 없으니 field를 참조할 수 없다.  
위와 같은 경우 email은 abstract 하니까 구현이 필요하고, nickname은 안해도 된다.


### backing field 

[baeldung의 backing fields](https://www.baeldung.com/kotlin/backing-fields)를 참고하면 좋다.  
- Kotlin will use a Java field to store the property values.
- These Java fields are known as backing fields in the Kotlin world.


### backing field in getter/setter

```kotlin
var statusCode: Int = 100
    set(value) {
        if (value in 100..599) statusCode = value
    }

var statusCode: Int = 100
    set(value) {
        if (value in 100..599) field = value
    }
```
위 예제에서 `statusCode`에 할당하면, 계속 statusCode의 setter를 불러서 endless recursion을 만듦.  
따라서 kotlin에서는 `field`라는 애를 사용.


### setter visibility

```kotlin
class LengthCounter {
    var counter: Int = 0
        private set
}
```
이렇게 하면 class 밖에서 counter를 set할 수 없음.


### data class

```kotlin
kdata class Client(val name:String, val postalCode: Int)
```

`toString()`, `equals()`, `hashCode()` 를 자동으로 구현해주는 class.  
- kotlin은 `==`에 `equals()`를 사용한다. 주솟값을 비교하려면 `===`를 쓰면 된다.

data class의 property들은 **immutable**하게 `val`을 쓰는 것을 권장.
- hashMap 등에 넣고 값이 변경되어 문제가 발생할 수도 있고,
- multi thread에서 변경될 경우를 고려하지 않아도 되고,
- data class가 제공하는 `copy()`를 써서 데이터 수정보다 유사하게 데이터를 복사하면 된다.


### by

상속이 불가능한 class인데 상속이 필요하면 `Decorator` 패턴으로 상속을 흉내낸다.  
이러면 구현해야할 양이 많은데, kotlin은 `by`를 제공해서 구현 양을 줄인다.


### object for singleton

```kotlin
object Payroll {
    // ...
}

Payroll.allEmployees.add(Person())
```
object는 consturctor가 필요없이 위처럼 그냥 쓰인다.


### companion object

companion object는 바깥 class의 private도 호출할 수 있어서 factory pattern 등을 구현하기 좋다.  
companion에 정의된 property나 method는 companion이 정의된 class 이름으로 접근할 수 있다.
- 그러면 왜 굳이 class 안에 안넣고 companion을 쓰느냐..?
- companion + extension으로 사용하는 예제가 있음
- companion object에 naming을 붙여서 사용할수도 있음
- companion에서 interface를 구현할 수도 있음


### anonymous inner class

java에서 흔히 쓰이는 event listener와 같은 코드를 kotlin에서 object를 활용해 anonymous object로 사용할 수 있다.
- anonymous object는 외부의 변수를 접근할 수 있음.
