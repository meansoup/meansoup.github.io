---
layout: post
title: "kotlin in action #6-2"
tag:
  - kotlin
parent: kotlin
grand_parent: language
permalink: /docs/algorithm/language/kotlin/kotlin-in-action-6-2
---

## chapter 6-2. The Kotlin Type System

## Primitive Types

java는 **primitive type**(int 등)과 **reference type**(string 등)을 갖는다.  
Collection에서는 reference type이 필요하고 이런 상황들에서 primitive type을 쓰는 방법이 **wrapper type**을 이용하는 것이다.  

kotlin에서는 wrapper type을 따로 구분하지 않고 사용한다.  
- 그치만 항상 객체로 표현하는 것은 비효율적이고, 실행 시점에 가장 효율적인 방식으로 표현한다.
- kotlin의 `Int` type은 대부분의 경우 `int`로 컴파일 되고, Collection 등에 사용될 땐 java의 `Integer`가 들어간다.  

java type에 맞는 kotlin type
- **Integer types** - Byte, Short, Int, Long
- **Floating-point number types** - Float, Double
- **The charater type** - Char
- **The boolean type** - Boolean

kotlin도 마찬가지로 **jvm에서 primitive type을 collection에서 받아주지 않으므로** null을 사용하는 `Int?`와 같은 경우 외에도 collection에서 사용될 땐 `Integer`로 변환된다.

### Number conversions

kotlin에서는 number type의 자동 변환을 해주지 않는다.  
Int를 Long에 넣으려면 명시적 변환을 해줘야한다는 말이다.  

## Root type Any, Any?

Java에서는 `Object`가 최상위 클래스이고,  
Kotlin에서는 `Any`가 그렇다.  
- Java에서 Object를 주면 Kotlin에서는 `Any!`가 되는거다.  

## Unit type

`Unit` type은 Java에서의 `void`와 같다.  
```kotlin
fun f(): { ... }
fun f(): Unit { ... } // 위와 같음
```

Java의 void와 다른 점은 Unit은 모든 기능을 갖는 일반적인 타입이고,  
type argument 쓸 수 있다.  
`Unit` type에 속한 값은 딱 하나 `Unit` 뿐이다.

generic에서 Unit을 반환할 때 유용하다. (void는 안되니까)
```kotlin
interface Processor<T> {
    fun process(): T
}
class NoResultProcessor: Processor<Unit> {
    override fun process() { /* return이 필요 없음 */ }
}
```

## Nothing type

성공적으로 return하는 경우가 없는 경우, 즉 fail 함수와 같이 return 값 자체가 의미 없는 함수.  
무한 loop를 도는 함수.  
함수가 정상적으로 끝나지 않는다는 사실을 명시하는 것이고, 코드 분석에 유용하단다.  

`Nothing`은 return type이나 return type으로 쓰일 type parameter로만 쓸 수 있다.  


## Collections

Collections에서도 nullable이 적용된다.  
```kotlin
List<Int?>  // Int가 nullable, List는 not-nullable
List<Int>?  // Int는 not-nullable, List는 nullable
List<Int?>? // Int도 List도 nullable
```

### Read-only & mutable

Kotlin에서는 collection에 대해 수정 가능한지 여부를 제공한다.  
즉, 수정 불가능한 collection을 제공한다는 것이다.  

> Java에서는 `final`로 생성하더라도 collection 자체를 바꿀 수 없을 뿐 내부 entity들을 추가/삭제하는 것은 가능했다.  
> 이런 것을 막기 위해선 `Collection.unmodifiableList()` 같은 함수로 생성하거나 따로 unmodifiable collection을 구현해야 했다.  

Kotlin에서는 `MutableCollection`과 `Collection`을 가지고 collection의 변경 가능 여부를 구별한다.  
이를 통해 어떤 코드에서 collection에 대해 수정을 하는지, 조회만 하는지를 확인할 수 있다.  

![collection structure](/images/post/kotlin_in_action/6_1.JPG)
- kotlin은 **java.util**의 collection 구조를 mutable collection에 그대로 적용함
- Java의 collection들(ArrayList 등)을 Kotlin interface를 상속한 것처럼 취급함
- Java와 kotlin의 코드를 혼용하면, java에서는 모두 수정이 가능

### collection 생성 함수

|collection type|read only|mutable|
|---|---|---|
|List|listOf|mutableListOf, arrayListOf|
|Set|setOf|mutableSetOf, hashSetOf, linkedSetOf, sortedSetOf|
|Map|mapOf|mutableMapOf, hashMapOf, linkedMapOf, sortedMapOf|

## Array

기본적으로 Array보다는 Collection을 사용해야 한다.  
Java의 API들이 Array를 사용하는 경우가 있어 써야할 수 있다.  
- 사실 java에서도 array를 잘 안쓰는 것 같은데..

`arrayOf`, `arrayOfNulls`로 생성할 수 있다.  
`toTypedArray`로 collection을 Array로 바꿀 수 있다.  
`IntArray`, `ByteArray`, `CharArray`, `BooleanArray` 등의 클래스들은 `int[]`, `byte[]` 등으로 컴파일 된다.
- 생성자가 size를 받고 default 값으로 초기화 된 배열을 만듦
