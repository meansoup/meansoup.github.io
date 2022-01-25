---
layout: post
title: "[Kotlin] kotlin 장단점 (vs java)"
tag:
  - kotlin
---

kotlin을 공부하면서 확인한 장단점을 정리해보았다.  
kotlin은 java의 많은 것들을 녹여내면서, 최대한 편리하고 간결하게 사용할 수 있다는 특징이 있다.

## 장점

### 1. java와의 호환

java와 유사하여 java 개발자가 쉽게 kotlin을 사용할 수 있다.  
즉 러닝커브가 낮다는 것.

또한 컴파일하여 java와 완벽히 호환이 가능하다.  
java와 kotlin 코드를 하나의 프로젝트에서 같이 사용할 수도 있다.  

![kotlin-compile](/images/post/kotlin_in_action/1_1.jpg)

### 2. 안전한 코드

kotlin에서 가장 대표적인 특징 중 하나는 nullable type의 지원이다.  
kotlin은 nullable type과 not nullable type을 구분한다.  

not nullable type은 compile 시점에서 NPE를 발생시키기 때문에 runtime에 의도치 않은 NPE가 날 확률이 줄어든다.

```kotlin
var nullable: String? = null
var notNullable: String = null
```

type을 그냥쓰면 not nullable type이고,  
type에 `?`를 붙여서 nullable type을 사용할 수 있다.  

not nullable type에 위처럼 null을 넣으면 `Kotlin: Null can not be a value of a non-null type`과 같은 compile error가 발생한다.


실제로 kotlin 코드를 적용해서 NPE가 감소한 통계가 있다.
1. android app에서 kotlin 코드를 사용하는 경우 [app crash가 20% 줄어듦](https://developer.android.com/kotlin/first#why).
2. google home 팀은 kotlin 사용후 [NPE가 30% 감소](https://developer.android.com/stories/apps/google-home#results).

### 3. 간결하고 명확한 코드

kotlin은 java에서 불편하고 가독성이 떨어지는 코드들을 많이 개선했다.  
그 중 가장 대표적인 것이 nullable type operator와 type cast operator이다.  

#### 보일러 플레이팅

kotlin의 class는 type에 따라  class를 제공하여 보일러 플레이팅 코드가 굉장히 줄어든다.  

kotlin은 class 생성 시 `Getter/Setter`와 `AllArgsConstructor`를 기본으로 제공한다.  

`data class`를 사용하면 `@lombok.Data` 처럼 `equals()`, `hashCode()`, `toString()`을 제공한다. 

```kotlin
class Car(val model: String, var number: String)
```

위 코드에서 `Car`은 아래와 같은 기능이 제공된다.  
- AllArgsConstructor
- `model`에 대한 getter
- `number`에 대한 getter/setter


kotlin 코드 적용 이후 코드가 줄어든 통계가 있다.  
1. kotlinlang에서는 [rough하게 40%](https://kotlinlang.org/docs/faq.html#what-advantages-does-kotlin-give-me-over-the-java-programming-language) 정도의 라인 수가 줄어드는 것을 확인.
2. google home 팀은 [코드 size 33%](https://developer.android.com/kotlin/first) 줄어듦

#### safe call operator

`?.`으로 간단하고 명료하게 null 검사와 함수 호출을 가능하게 한다.

<details>
  <summary>kotlin class 코드</summary>
  <div markdown="1">

```kotlin
class Address(val country: String?)
class Company(val address: Address?)
class Person(val company: Company?) {
    fun getCountry(): String? {
        return company?.address?.country;
    }
}
```

  </div>
</details>

```kotlin
fun getCountry(): String? {
    return company?.address?.country
}
```
위 kotlin 코드는 아래 java 코드와 같다.

```java
void getCountry() {
    if (company == null) {
        return null;
    }
    
    if (company.getAddress() == null) {
        return null;
    }
    
    return company.getAddress().getCountry();
}
```

#### elvis operator

`?.`와 유사한데, default value를 명시해준다.

```kotlin
fun getCountry(): String {
    return company?.address?.country?:"kr"
}
```
위 kotlin 코드는 아래 java 코드와 같다.

```java
void getCountry() {
    if (company == null) {
        return "kr";
    }
    
    if (company.getAddress() == null) {
        return "kr";
    }
    
    if (company.getAddress().getCountry() == null) {
       return "kr";
    }

    return company.getAddress().getCountry();
}
```

#### smart cast

kotlin은 type cast에 `is`와 `as`를 제공한다.  
이 중에 `is`는 `instanceof`와 유사한데, compiler가 `smart cast`를 해줘서 더 편리하다.  

<details>
  <summary>kotlin class 코드</summary>
  <div markdown="1">

```kotlin
interface Expr
class Num(val value: Int): Expr
class Sum(val left: Expr, val right: Expr): Expr
```

  </div>
</details>

```kotlin
fun eval(e: Expr): Int {
    if (e is Num) {
        return e.value
    }
    if (e is Sum) {
        return eval(e.left) + eval(e.right)
    }
}
```

java 코드로 작성할 경우 `instanceof` 이후에 명시적으로 type cast를 해주어야 하는 코드를 kotlin에서는 `is`를 통해 위와 같이 처리할 수 있다.


### 4. 확장 함수

확장 함수는 클래스 밖에 선언된 함수를 말한다.  
기존의 api들을 재작성하지 않고 기능을 사용할 수 있어서, kotlin에서 **java의 클래스들을 그대로 사용하면서 기능을 추가**하기 위한 목적으로도 사용된다.  
확장 함수에서는 private, protected로 선언되지 않은 변수나 함수를 모두 자연스럽게 (내것 마냥) 호출할 수 있다.  

```kotlin
fun String?.isNullOrBlank(): Boolean = this == null || this.isBlank()
```

예를 들면, 위처럼 기본 타입에 대해서도 확장 함수를 작성할 수 있다.  
실제로 위와 유사한 코드가 이미 있다.

확장 함수로 kotlin은 [OO와 FP 모두 사용할 수 있다](https://kotlinlang.org/docs/faq.html#is-kotlin-an-object-oriented-language-or-a-functional-one).

### 5. 구글 공식 언어

무료 오픈소스 언어이자, 구글 공식 언어로의 채택.


## 단점

### 빌드 시간 & 크기

clean build의 경우 java보다 시간이 더 오래걸린다.  
kotlin은 [증분 컴파일(incremental build)](https://blog.jetbrains.com/ko/kotlin/2020/10/the-dark-secrets-of-fast-compilation-for-kotlin/)을 제공해서 partial build가 가능한 경우 java보다 더 빠르다.  
- java는 컴파일 회피만을 제공

**컴파일 회피**: 모듈 단위의 dirty 체크  
**증분 컴파일**: 파일 단위의 dirty 체크


kotlin runtime이 package에 들어가야 해서 배포 시 파일 사이즈가 더 커진다.

### 자바가 아니다

java와 유사하지만 자바가 아니다.  
분명히 세세한 사용들에 공부와 검색이 필요할 것이다.  

**java 6**을 베이스로 코틀린이 만들어졌다.  
**java 6**이후의 버전들과 다른 개념들이 존재한다.

### 학습 리소스의 제한

아무래도 java 보다는 자료들이 부족하다.  
검색하는데 더 많은 시간이 필요할 것이다.