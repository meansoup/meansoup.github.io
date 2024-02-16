---
layout: post
title: "kotlin in action 정리 #6"
sidebar_label: "kotlin in action 정리 #6"
parent: "kotlin in action 정리하기"
grand_parent: Kotlin
permalink: /docs/kotlin/kotlin-in-action/6
sitemap:
  lastmod: 2021-03-19
---

## chapter 6. The Kotlin Type System

**kotlin**에서는 java와 다르게 주의깊게 알아야 하는 부분은 두 가지다.
1. **Nullable Type**
2. **Read-Only Collection**


## Nullable Type

Java에서는 null이 굉장히 거슬리는 문제가 됐다.  
열심히 고려해도 `NPE(Null Pointer Exception)`는 너무 자주나고,  
null을 체크하는 코드들은 로직을 어지럽힌다.  

`Optional`과 같은 기능들이 추가됐지만 코드가 이뻐지는 것 같지는 않다.  
Kotlin에서는 이런 것들을 편하게 하기 위한 Type과 장치들을 제공한다.

### Type?

Nullable Type과 Non-Nullable Type은 간단하다.  
예제로 보면 쉽다.  

```kotlin
val nullable: String? = null // Type에 ?을 붙이면 nullable
val nonNullable: String = x // compile 시점에 error 발생
```

Type이 정해져있어, compile 시점에 error를 발생시키기 때문에 runtime에 의도하지 않은 NPE가 날 일이 없다.

### Safe Call Operator ?.

Kotlin에서 굉장한 장점이 바로 `?.` operator 이다.  
아주 간단하고 명료하게, 읽기 쉽게 null 검사와 함수 호출을 가능하게 한다.  

```kotlin
val allCaps: String? = s?.toUpperCase() // s가 null -> return null
                                        // !null -> return s.toUpperCase()

val country = company?.address?.country // company나 address가 null이면 return null
```

위와 같이 여러 상위 object들의 null check를 할 때 특히 유용하다.
- 위 예제를 Java에서 모두 null check 한다고 생각하면...

### Elvis Operator ?:

null 대신 사용할 default value를 지정한다.  
`?.`와 유사한데, default value를 명시해준다.  

```kotlin
val t: String = s?: "" // s가 null -> return ""

company?.address?: throw IllegalArgumentException("No Address")
```

두 번째 예제와 같이 elvis operator의 우항으로 `throw`를 넣을 수 있다. 
- Kotlin은 `return`이나 `throw` 같은 연산도 식(expression)이기 때문에 elvis operator의 우항으로 넣을 수 있음.

### Safe Casts: as?

명시적 type case `as`를 안전하게 할 수 있는 방법이 있다. ([2장 참고](https://meansoup.github.io/2021/01/07/kotlin_in_action_ch2/#is))  

```kotlin
val person = o as? Person ?: return false // type casting이 안될 경우 아예 함수 자체를 return false
```

### Not-null assertion !!

nullable type을 절대 null이 아닐거라고 단정 짓기 위해 `!!`을 사용한다.  
`!!` 사용한 값이 runtime에 실제 null이 올 경우 NPE가 발생한다.  

null 검사를 이미 했고 다시 하고싶지 않은 경우 사용할 수 있지만,  
nullable 체크를 하지 않아도 되지만 굉장히 위험하고 추천되지 않는 방식이다.  

```kotlin
fun ignoreNulls(s: String?) {
    val sNotNull: String = s!!
}
```

### let

let은 null이 아닐 경우 값을 변수에 넣어 작업을 진행하게 한다.  

```kotlin
if (email != null) sendEmailTo(email)

email?.let {email -> sendEmailTo(email)}
```
예를 들면 위 코드를 아래와 같이 바꿀 수 있다.

### lateinit

일반적으로 kotlin은 constuctor에서 모든 properties를 초기화해야 한다.  
Junit의 `@Before` 같은 경우 메소드 안에서 초기화를 하는데, 이런 경우에 Kotlin은
1. nullable type을 쓰고 `!!`를 쓰거나
2. non-nullable로 초기화를 해두거나

그치만 이런 방식은 좋지 않고 kotlin은 `lateinit`을 제공한다.

```kotlin
class MyTest {
    private lateinit var myService: Myservice // 아직 초기화 안함

    @Before fun setUp() {
        myService = MyService() // 초기화 한다
    }
}
```

`lateinit` property는 항상 var이어야 한다.  
lateinit property가 초기화되기 이전에 사용되면 lateinit 관련 exception이 발생한다.
- 이 exception이 NPE보다 문제의 원인을 확인하기 훨씬 편리하다.

### extensions on nullable types

nullable type에 대한 확장 함수는 safe call `?.` 없이 호출할 수 있다.  

```kotlin
s.isNullOrBlank() // s가 null이어도 true를 반환
```

java는 this가 호출된 객체를 가리키므로 항상 null이 아니다.  
반면 kotlin에서는 nullable type의 확장 함수에서는 this가 null이 될 수 있다.  

```kotlin
fun String?.isNullOrBlank(): Boolean = this == null || this.isBlank()
```

### type parameter

type parameter는 기본적으로 nullable하다.  
```kotlin
fun <T> printHashCode(t: T) { ... } // t가 nullable
fun <T: Any> printHashCode(t: T) { ... } // t가 not-nullable 
```

T의 type은 `Any?`로 추론되기 때문에 nullable하고 not-nullable로 바꾸려면 Any를 명시한다.  

### platform type

**platform type**은 nullable인지 아닌지 알 수 없는 타입을 말한다.  
이 type은 nullable로 처리해도 되고, not-nullable로 처리해도 된다.
- 모두 nullable로 하도록 해도 되겠지만 그러면 불필요한 null 체크가 필요할 수 있어 platform type을 만듦  

그런데 이 type을 kotlin에서 사용할 수 있도록 허락하지 않는다.  
Java와 코드가 혼용될 때, Java의 type들이 kotlin에서 platform type으로 표현된다.  
이럴 경우 java 처럼 runtime에 대한 handling은 개발자의 몫이다.

platform type의 표기는 `String!`과 같다.
- 사용할 수는 없고 error msg에서 확인할 수 있음.
