---
layout: post
title: "[kotlin error] cannot be invoked as a function. The function 'invoke()' is not found"
sidebar_label: "[kotlin error] cannot be invoked as a function. The function 'invoke()' is not found"
tag:
  - error
parent: error & bug
permalink: /docs/error-bug/kotlin/cannot-be-invoked-as-a-function
sitemap:
  lastmod: 2021-05-01
---

## 에러 메세지

`cannot be invoked as a function. The function 'invoke()' is not found`

## 코드

```kotlin
class ListNode(var `val`: Int) {
    var next: ListNode? = null
}

    val base = ListNode(0)
    base.next(ListNode(1))
    var next = base.next()
```

이런 코드에서 문제가 났다.  
역시 책으로 공부하는거랑 써보는거랑 다르다..

property의 경우엔 저렇게 쓰는게 아니었다.

## 해결

```kotlin
    val base = ListNode(0)
    base.next = ListNode(1)
    var next = base.next()
```