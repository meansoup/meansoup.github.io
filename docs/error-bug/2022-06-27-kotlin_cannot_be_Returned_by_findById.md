---
layout: post
title: "[spring error] kotlin cannot be returned by findById(), findById() should return Optional"
parent: error & bug
permalink: /docs/error-bug/spring/kotlin_cannot_be_Returned_by_findById
---

kotlin에서 jpa findById 사용하기.  

kotlin spring에서 java에서 사용하던 것처럼 jpa를 사용하려고 하면 만나는 에러에 대한 해결이다.  

## 에러 메세지

```
org.mockito.exceptions.misusing.WrongTypeOfReturnValue: 
MysqlUser cannot be returned by findById()
findById() should return Optional
***
If you're unsure why you're getting above error read on.
Due to the nature of the syntax above problem might occur because:
1. This exception *might* occur in wrongly written multi-threaded tests.
   Please refer to Mockito FAQ on limitations of concurrency testing.
2. A spy is stubbed using when(spy.foo()).then() syntax. It is safer to stub spies - 
   - with doReturn|Throw() family of methods. More in javadocs for Mockito.spy() method.
```

## 해결

해결 방법은 두 가지다.

1. mockK 적용
2. test와 code가 조금 이상하게 적용

나는 mockK를 적용하고 싶지 않아서 기존 mockito로 하는 방법을 설명한다.


### 원래 코드

```Kotlin

// main code
	val found = mysqlUserJpaRepository.findByIdOrNull(uid.toString())


// test code
	doReturn(mysqlUser).`when`(mysqlUserJpaRepository).findByIdOrNull(safeEq(uuid.toString()))
```

원래 코드는 이렇다.  
Optional이 나오면 안되서 findByIdOrNull을 사용하는데, 에러는 `findById`에 대한 에러를 받는 것.

### 해결 코드

```Kotlin

// main code
	val found = mysqlUserJpaRepository.findByIdOrNull(uid.toString())


// test code
	doReturn(Optional.of(mysqlUser)).`when`(mysqlUserJpaRepository).findById(safeEq(uuid.toString()))
```

해결 코드는 main code는 findByIdOrNull을 적용하고, test code에는 findById로 테스트한다.


## 원인

**findByIdOrNull**은 kotlin에서 정의한 extension code이다.  
mockito는 static method에 대한 mocking(kotlin의 extension code)를 지원할 계획이 없으며,  
따라서 findByIdOrNull의 실제 코드인 findById가 mockito에서 잡히는 상황.  

테스트에서는 findById를 사용해줘야 한다.  
혹은 mockK를 사용하면 해결할 수 있다.

## reference

https://stackoverflow.com/questions/59562177/mockito-findbyidornull-issue	
https://github.com/mockito/mockito/issues/1481  