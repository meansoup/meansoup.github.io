---
layout: post
title: Time Complexity in Python data-structure
tag:
  - python
---

자료구조에 따라 python operation들의 time complexity가 달라진다.  
같은 operation도 어떤 자료구조를 쓰느냐에 따라 성능이 달라질 수 있다.
- [python wiki](https://wiki.python.org/moin/TimeComplexity) 참고.

## x in s
여러가지 다른 부분이 있지만, list와 set의 `x in s`를 비교해본다.  
list는 기본적으로 sequence type이다.  
따라서 index를 통해 접근 가능하고 index를 활용한 opration들도 많다.  
하지만 그렇기 때문에 `in` 검사에 O(n)을 요구한다. 다 확인해봐야하기 때문이다.  

반면,  
set([python Docs](https://docs.python.org/3.8/library/stdtypes.html#set-types-set-frozenset) 참고)은 **unordered collection of distinct hashable object**이다.  
따라서 동일한 값을 갖지 못하고 index를 통한 접근도 되지 않는다.  
그치만 hashable이라는 특성 덕분에 `x in s`는 O(1)의 성능을 갖는다. (hash가 꼬이지 않는 average case의 경우)  

반복적으로 `x in s`를 사용할 경우 set을 사용하면 속도를 개선할 수 있다.  
- list를 set으로 바꾸는 건 O(n). `s = set(l)`  

## 추가 참고
- [https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt](https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt)