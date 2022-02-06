---
layout: post
title: Time Complexity in Python data-structure
tag:
  - python
parent: python
grand_parent: language
permalink: /docs/algorithm/language/python/time-complexity
---

당연하게도 자료구조에 따라 python operation들의 time complexity가 달라진다.  
같은 operation도 어떤 자료구조를 쓰느냐에 따라 성능이 달라질 수 있다.

고민이 될 때는 아래 링크를 참고해서 각 동작들의 cost를 확인해보는 것도 좋겠다.

## 기본 자료형 time complexity

아래 링크에서 정리된 표를 보면 좋다.

- [https://wiki.python.org/moin/TimeComplexity](https://wiki.python.org/moin/TimeComplexity)

---

## libary

### heapq

| Operation | Average Big O |
|-----------|---------------|
| push      | O(log n)      |
| pop       | O(log n)      |

- [https://stackoverflow.com/questions/38806202/whats-the-time-complexity-of-functions-in-heapq-library/38833175](https://stackoverflow.com/questions/38806202/whats-the-time-complexity-of-functions-in-heapq-library/38833175)

## reference

- [https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt](https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt)
- [https://stackoverflow.com/questions/38806202/whats-the-time-complexity-of-functions-in-heapq-library/38833175](https://stackoverflow.com/questions/38806202/whats-the-time-complexity-of-functions-in-heapq-library/38833175)