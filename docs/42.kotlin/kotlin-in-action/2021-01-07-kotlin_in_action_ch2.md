---
layout: post
title: "kotlin in action 정리 #2"
parent: "kotlin in action 정리하기"
grand_parent: Kotlin
permalink: /docs/kotlin/kotlin-in-action/2
sitemap:
  lastmod: 2021-01-07
---

## chapter 2. Kotlin Basics

## kotlin function body

![function-body](/images/post/kotlin_in_action/2_1.jpg)

kotlin의 function 구조는 위와 같다.  

### expression

Kotlin은 반복문(for, while)을 제외하고는 expression으로 판단된다. (If, when 등)
`expression`은 value를 갖는다는 점에서 statement와 차이점을 보인다.
반면 java에서는 모든 control structure들이 statement이다. 

여기서 value를 갖는다는 것은 expression 자체(expression의 결과)가 value를 갖는 것을 말한다.  
```kotlin
// 예를 들면 아래 if expression은 value를 갖고 있다.
fun max(a: Int, b: Int): Int = if (a > b) a else b
```

### expression body

Block body와 expression body로 function의 body를 구분한다.  
Block body: `{}`으로 body가 쌓여진 일반적인 함수.  
Expression body: `{}` 없이 구현된 함수. 보통 one line function에서 사용하는 함수.  

### variable

변수에 타입을 명시하지 않아도 된다.  
명시할수도 있는데, 초기 값을 넣어주지 않으면 타입 추론이 안되므로 명시해주어야 한다.  

`val`(from value): immutable (final in java)  
`var`(from variable): mutable

기본적으로 val을 사용하고, 수정이 필요한 경우만 var를 사용하도록 한다.  
var이 change value를 허락해도, type은 fix되서 바뀔 수 없다.  

`$`로 local variable에 접근할 수 있고, 이건 $(expression) 으로도 사용이 가능하다.
```kotlin
println("Hello, $name!")
println("Hello, ${if (args.size > 0) args[0] else "someone"}!")
```

### class

kotlin은 public이 default라 public을 생략할 수 있다.  
property를 선언하면 기본적으로 내부적으로 getter/setter가 같이 선언된 것이라고 보면 된다.  
그냥 class의 property를 사용하면 java의 getter를 호출해준다.  

getter/setter 외의 custom accessors를 만들 수 있다.  
custom accessors와 function을 만드는것의 차이는  
- 성능 상으로는 차이가 없다
- 가독성에만 차이가 있다

### package

kotlin에도 package가 있고 java의 package 정책과 유사하다.  
import로 class와 method를 구분하지 않고 method도 import할 수 있다.  

여러 class를 하나의 file에 넣을 수 있다.  

### enum

enum이 java랑 좀 다르다.
```kotlin
// 예제가 이해하기 편할 듯 하다.
enum class Color(
    val r: Int, val g: Int, val b: Int
) {
    RED(255, 0, 0), ORANGE(255, 165, 0),
    YELLOW(255, 255, 0), GREEN(0, 255, 0), BLUE(0, 0, 255),
    INDIGO(75, 0, 130), VIOLET(238, 130, 238);

    fun rgb() = (r * 256 + g) * 256 + b
}
>>> println(Color.BLUE.rgb())
```

### when

when과 함께 쓰일 때 enum의 효과가 더 크다.  
when은 java의 switch와 비슷한데, 더 파워풀하다.  
- any objects나 들어올 수 있다. (set 등)

no arg when 을 사용할 때도 있다.
- 가독성은 좀 떨어질 수 있다.
- 성능상 이점을 얻기 위할 때 사용할 수 있다.
- no arg이기 때문에 extra objects를 생성하지 않는다는 장점이 있다.

### is

`is`는 java의 `instanceof`와 유사하다.  
instanceof 체크하고 type casting을 해야하는 java와 달리 is는 compiler가 `smart cast`를 해준다. (더 강력하고 편리하다)  
- smart cast를 위해서 property가 `val`이어야 하고, custom accessor를 가질 수 없다. 그렇지 않으면 property에 대한 access가 동일한 값을 주는지에 대해 보장할 수 없다.
- 명시적 type cast는 `as`를 이용한다.

### block value

`if`나 `when`의 branch에 block을 가질 수 있다.
block이 있으면, block의 가장 마지막 expression이 block의 result가 된다.
- if나 when은 kotlin에서 expression이고 반환 값을 갖는다는 점을 상기하자.

```kotlin
fun evalWithLogging(e: Expr): Int =
    when (e) {
        is Sum -> {
            val left = evalWithLogging(e.left)
            val right = evalWithLogging(e.right)
            println("sum: $left + $right")

            left + right // return value
        }
    }
```

### loop

java의 for loop과 완전히 매칭되는 for loop은 없다.
- while은 java랑 완전히 같음.

그래서 range, progression을 사용한다.  
range는 1..10 처럼 사용될 수 있고, 이런 range를 progression이라고 한다.  
- range는 char에도 된다. ('A'..'F', '0'..'9')

또, `downTo`, `step`, `until`을 제공하는데 직관적이다.  
```kotlin
for (i in 1..10)
for (i in 100 downTo 1 step 2)
for (i in 0 until size)
```

### exception

exception은 java와 유사하다.  
try, catch, finally도 java와 유사하다.  

java와 다른 점은 kotlin의 throw, try도 expression이다.  
- try는 if와 다르게 `{}` body를 항상 가져야 한다.  
```kotlin
val number = try {
        Integer.parseInt(reader.readLine())
    } catch (e: NumberFormatException) {
        return
    }
```

또 다른 점은 kotlin은 함수에 `throws`를 명시하지 않아도 된다.
- java와 다르게  `checked exception`과 `unchecked exception`을 구분하지 않는다는 것.
- 경험 상 `checked exception`에서 rethrow나 ignore exception 같은 처리들이 불필요하게 수행되는 경우가 많아 구분을 하지 않는 설계를 했다고 한다.