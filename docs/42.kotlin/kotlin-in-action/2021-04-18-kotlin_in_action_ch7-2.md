---
layout: post
title: "kotlin in action 정리 #7-2"
sidebar_label: "kotlin in action 정리 #7-2"
parent: "kotlin in action 정리하기"
grand_parent: Kotlin
permalink: /docs/kotlin/kotlin-in-action/7-2
sitemap:
  lastmod: 2021-04-18
---

## chapter 7-2. Operator overloading and other conventions

## Destructuring declarations

Destructuring declaration(구조 분해 선언)을 사용하는 방법을 보자.  
```kotlin
val p = Point(10, 20)
val (x, y) = p
```

이렇게 여러 변수의 초기화가 가능한 방식이다.
- python도 여러 변수의 초기화를 하지만 kotlin과는 다르다.

destructuring은 다음과 같은 convention을 사용한다.  
![destructuring](/images/post/kotlin_in_action/7_1.JPG)

- 초기화 할 좌변의 변수들을 괄호로 묶어야 한다.
- destructuring declaration은 초기화를 위해 `componentN` 함수를 호출한다. 여기서 `N`은 destructuring declaration의 변수 위치에 따라 붙는 번호다.
- `data` class는 생성자에 있는 property에 대해 자동으로 `componentN` 함수를 만들어준다.
- kotlin standard libary에서는 맨 앞의 다섯 property에 대해서만 `componentN`을 제공한다.  
- collection에 대해서도 `destructuring`이 가능하다.

data class가 아닌 경우의 구현
```kotlin
class Point(val x: Int, val y: Int) {
    operator fun component1() = x
    operator fun component2() = y
}
```

### Destructuring in loop

변수 선언이 들어갈 수 이쓴ㄴ 장소라면 어디든 구조 분해 선언을 사용할 수 있다.  
- `for` 안에서도 사용할 수 있다.

특히 map에서 유용하게 사용할 수 있다.
```kotlin
fun printEntries(map: Map<String, String>) {
    for ((key, value) in map) {
        println("$key -> $value")
    }
}
```

## delegated property

field에 단순 저장하는 것보다 더 복잡하게 작동하는 property를 쉽게 구현할 수 있다.  
- delegate를 활용해서 값을 field가 아니라 db table이나 browers session, map 등에도 저장할 수 있다.

```kotlin
// delegate의 일반적인 문법
class Foo {
    var p: Type by Delegate()
}

// compiler에서 해석해서 생기는 코드
class Foo {
    private val delegate = Delegate()
    var p: Type
    set(value: Type) = delegate.setValue(..., value)
    get() = delegate.getValue(...)
}
```

위에서 예시로 사용한 `Delegate` class 처럼 사용하려면 `getValue`와 `setValue` 함수를 가지고 있어야 된다.  

### lazy initialization

**lazy initialization**는 객체의 일부를 초기화하지 않고 남겨뒀다가 필요할 경우 초기화할 때 쓰는 패턴이다.  
아래는 email을 실제 사용할 때 한 번만 초기화하도록 구현한 class 이다.  
```kotlin
class Person(val name: String) {
    private var _emails: List<Email>? = null // 이런걸 backing property라고 함.
    val emails: List<Email>
    get() {
        if (_emails == null) {
            _emails = loadEmails(this)
        }
        return _emails!!
    }
}
```

`email`은 not nullable하기 때문에 `_email`을 사용해서 활용해야 한다.  
```kotlin
class Person(val name: String) {
    val emails by lazy { loadEmails(this) }
}
```

`lazy`는 `getValue` 함수가 있는 객체를 반환한다.  
`lazy`가 `by`와 함께 사용되면 delegate property를 만들 수 있다.  
`lazy` 함수는 기본적으로 thread safe 하다.  
- 필요에 따라 동기화에 사용할 락을 lazy 함수에 전달할 수 있다.
- multi thread에서 사용하지 않을 property를 위해 lazy 함수가 동기화하지 못하게 막을 수도 있다.

### implement delegate property

```kotlin
class ObservableProperty(var propValue: Int, val changeSupport: PropertyChangeSupport) {
    operator fun getValue(p: Person, prop: KProperty<*>): Int = propValue
    operator fun setValue(p: Person, prop: KProperty<*>, newValue: Int) { // KProp은 나중에 다룸. name을 가져올 수 있다는 것만 알자.
        val oldValue = propValue
        propValue = newValue
        changeSupport.firePropertyChange(prop.name, oldValue, newValue) // noti하기 위한 따로 구현된 함수라고만 생각하자
    }
}

class Person(val name: String, age: Int, salary: Int): PropertyChangeAware() {
    var age: Int by ObservableProperty(age, changeSupport)
    var salary: Int by ObservableProperty(salary, changeSupport)
}
```

`by` 오른쪽에 오는 객체를 delegate 객체라고 한다.  
진짜 객체의 property를 읽거나 쓸 때마다 delegate 객체의 getValue와 setValue를 호출한다.  

`getValue`와 `setValue`에도 `operator`가 붙는다.  

위 코드를 kotlin standard에 있는 `Delegates`를 이용해서 아래와 같이 바꿀 수 있다.  
```kotlin
class Person(val name: String, age: Int, salary: Int): PropertyChangeAware() {
    private val observer = {
        prop: KProperty<*>, oldValue: Int, newValue: Int ->
        changeSupport.firePropertyChange(prop.name, oldValue, newValue)
    }
    var age: Int by Delegates.observable(age, observer)
    var salary: Int by Delegates.observable(salary, observer)
}
```

`by`의 우항에는 꼭 새로운 instance가 생성되어야 하는 것은 아니다.  
`getValue`와 `setValue`를 포함하는 객체를 반환하는 함수 호출이나 다른 property, 다른 expression이 올 수 있다.

### delegate property rule

delegate가 어떻게 동작하는지 정리해본다.  
```kotlin
class C {
    var prop: Type By MyDelegate()
}
```

compiler는 `MyDelegate` class의 instance를 hidden property에 저장한다.  
- 이걸 `<delegate>`라고 부른다.  
compiler는 `KProperty` type의 object를 property를 표현하기 위해 사용한다.  
- 이걸 `<property>`라고 부른다.

```kotlin
class C {
    private val <delegate> = MyDelegate()
    var prop: Type
    get() = <delegate>.getValue(this, <property>)
    set(value: Type) = <delegate>.setValue(this, <property>, value)
}
```

![delegate](/images/post/kotlin_in_action/7_2.JPG)

이렇게 compiler가 property의 접근자에 대해 `get/setValue` 호출 코드를 생성해준다.  

### framework에서 delegate 활용

```kotlin
object Users : IdTable() { // db table
    val name = varchar("name", length = 50).index() // property = column
    val age = integer("age")
}

class User(id: EntityID) : Entity(id) { // 각 User instance는 table에 들어있는 구체적인 entity에 해당
    var name: String by Users.name
    var age: Int by Users.age
}
```

`Users`는 db 전체에 단 하나만 있는 table을 표현하므로 singleton으로 선언됨.  
위 같은 코드에서는 User에 접근할 때 entity에 정의된 db에서 값을 가져오므로 편리하다.  

F/W는 `Column` class 안에 `get/setValue`를 정의한다.  
`get/setValue`는 kotlin delegate conventions의 요구사항을 만족한다.  
```kotlin
operator fun <T> Column<T>.getValue(o: Entity, desc: KProperty<*>): T {
    // retrieve the value from the database
}
operator fun <T> Column<T>.setValue(o: Entity, desc: KProperty<*>, value: T) {
   // update the value in the database
}
```