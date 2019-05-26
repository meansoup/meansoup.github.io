---
layout: normal
title: Grammer
---

## * (Asterisk)

`*` 는 parameter에서 쓰일 때, C에서처럼 주소값을 받아오는 것이 아니라,  
가변인자, 즉, 여러 개의 parameter를 받아올 수 있게 하는데 사용 됨.

`**` 는 parameter에서 쓰일 때,
keword 형태로 parameter를 넘겨줄 수 있도록 하는데 사용 됨.  
`key_name='key value'` 형태로 사용함.
* 일반적으로 kivy 등에서 `**kwargs`를 사용하는 것은, keyword arguments의 약자.

## with
`with` 는 file에 접근할 때 주로 사용되며, close를 하지 않아도 자동으로 cloase를 해주어 편리하게 사용 됨.

## switch - case
파이썬에선 switch 문을 지원하지 않음.  
길고 보기 싫은 if - else의 반복을 없애기 위한 [코드](https://stackoverflow.com/questions/60208/replacements-for-switch-statement-in-python).  
```python
def f(x):
    return {
        'a': 1,
        'b': 2
    }.get(x, 9)    # 9 is default if x not found
```

**주의 사항**:  
if 문처럼 해당하는 부분만 실행되는 것이 아니라, 전체코드가 실행 되고, 해당 값을 반환 함.
예를 들어, 
```python 
def f(x):
    return {
        1: test_list.append(1),
        2: test_list,
    }.get(len(test_list), [0, 0])
```
위와 같은 코드에서 length가 2여도, append(1)이 수행되어 원하는 값을 얻을 수 없으며, 코드에 따라 에러가 발생하기도 함.

## reversed for
`for(int i = MAX; i >=0; --i)` 를 파이썬에서 사용하기 위한 [코드](https://stackoverflow.com/questions/4294082/decreasing-for-loops-in-python-impossible).  
`for i in reversed(range(10)):` or `for i in range(10, 0, -1):`