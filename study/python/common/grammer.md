---
layout: normal
title: Grammer
---

### * (Asterisk)

`*` 는 parameter에서 쓰일 때, C에서처럼 주소값을 받아오는 것이 아니라,  
가변인자, 즉, 여러 개의 parameter를 받아올 수 있게 하는데 사용 됨.

`**` 는 parameter에서 쓰일 때,
keword 형태로 parameter를 넘겨줄 수 있도록 하는데 사용 됨.  
`key_name='key value'` 형태로 사용함.
* 일반적으로 kivy 등에서 `**kwargs`를 사용하는 것은, keyword arguments의 약자.

### with
`with` 는 file에 접근할 때 주로 사용되며, close를 하지 않아도 자동으로 cloase를 해주어 편리하게 사용 됨.

### switch - case
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

### reversed for
`for(int i = MAX; i >=0; --i)` 를 파이썬에서 사용하기 위한 [코드](https://stackoverflow.com/questions/4294082/decreasing-for-loops-in-python-impossible).  
`for i in reversed(range(10)):` or `for i in range(10, 0, -1):`

### [go for built-in function](https://docs.python.org/3/library/functions.html)
C로 짜여진 built-in code를 활용하는 것.  
빠른 성능.

### join
String을 연결하기 위해 join을 사용 하는 것.  
`+` 으로 String을 연결할 수 있지만, `+` 는 새로운 Stringㅇ르 생성한 후 복사하는 방식으로 굉장히 비효율적.  
자바의 `StringBuilder.append()`와 유사.

### use multiple assignment to swap variables
python에서는 `x, y = y, x`로 swap이 가능하며, 속도도 빠름. temp를 사용하면, 가독성과 속도 모두를 잃음.

### use local variable
가능한 local variable을 사용하는 것이 좋음. `global`에서 값을 가져오는게 시간이 걸림.  

### lazy importing
전반적으로 쓰이는 게 아니라면, importing을 필요한 부분에서 사용하도록 하면, 로딩을 줄일 수 있음.

### python list
python에서 list는 array로 구현되어 있음.  
즉, index로 접근 가능하다는 장점.
앞 부분에 insert를 하면 뒤의 값들의 처리를 위해 효율이 떨어진다는 단점.
앞 부분에 insert/remove를 자주한다면 `deque`를 사용하는 것이 좋음.  
`deque`는 double-linked list로 구현되어 있음.

### use dict and set to test membership
dictionary와 set은 hash table을 사용해 구현되어 element exist 여부를 확인하는데 굉장히 빠름.  
`O(1)`의 속도를 보이며, membership 체크에 dict나 set의 container를 사용히주면 효율적.  
```python
mylist = ['a', 'b', 'c'] #Slower, check membership with list:
'c' in mylist
myset = set(['a', 'b', 'c']) # Faster, check membership with set:
'c' in myset
```

### comprehensions
[list comprehension](https://docs.python.org/3/tutorial/datastructures.html?highlight=comprehension#list-comprehensions)  
반복문과 조건문을 통해 list를 생성하는 방식.  
간결하고 가독성 있으며,  
python interpreter에 최적화되어 보다 빠른 성능을 보임.  
comprehension은 list 외에도 dict, set 등에서도 사용 됨.  

## 추가 공부 필요
### use listcomprehension
### use xrange
### itertools
### bisect
### python decorator '@'

참고:  
[Python Performance Tips: Part 1](https://www.monitis.com/blog/python-performance-tips-part-1/)