---
layout: post
title: copy in Python
tag:
  - python
parent: python
grand_parent: language
permalink: /docs/algorithm/language/python/python-copy
sitemap:
  lastmod: 2022-03-06
---

파이썬에서는 세 종류의 복사가 있다고 볼 수 있다.  
- 생?복사, 얕은복사, 깊은복사  
경우에 따라 의도치 않게 참조하거나, 참조가 무시될 수 있으니 알고 구별하여 사용해야 한다.

## 생 복사
생 복사는 할당 연산을 통해 복사되는 것을 말한다.  
할당 시 주소까지 가져가기 때문에 아예 동일한 변수가 된다고 보면 된다.  
한 쪽에서 수정시 다른 곳에서도 수정된다.  
```python
a = [1, 2]
b = a # b는 a의 주소를 받음.

same = a is b # 동일 객체
same = id(a) == id(b) # 동일 주소

b[0] = 0 # b를 수정시 a도 수정
a[0] = 0 # a를 수정시 b도 수정
```

## 얕은 복사
shallow copy라고 한다.  
얕은 복사는 새로운 객체를 만들고, 원본 객체를 가리키는 참조를 새로운 복합 객체에 삽입한다.  
즉, 내부 객체는 참조 객체이다.  
```python
a = [1, [2, 3]]
b = a.copy()

same = a is b # False
same_val = a == b # True

# b의 immutable object의 값이 변경되지 않음.
a[0] = 0 # 새로운 객체를 만들었기 때문에 b의 immutable object의 값이 변경되지 않음.
a[1][0] = -1 # b의 mutable object의 값은 변경됨. 참조하고 있기 때문
```

얕은 복사의 방식([stackoverflow](https://stackoverflow.com/questions/2612802/how-to-clone-or-copy-a-list) 참고)은 여러가지가 있음.  
```python
b = a.copy()

b = a[:]    # 가독성 문제로 권장하지 않기도 함.

b = list(a)

import copy
b = copy.copy(a)    # a의 type을 알아내야 해서 살짝 더 느림.
```

## 깊은 복사
deep copy라고 한다.  
깊은 복사는 새로운 객체를 만들고, 재귀적으로 원본 객체의 사본을 새로 만든 복합 객체에 삽입한다.  
즉, 완전히 다른 객체를 만드는 것으로 객체 사이에 참조가 없다.  
따라서 어떤 수정도 서로 간에 영향을 미치지 않는다.  
```python
import copy
a = [1, [2, 3]]
b = copy.deepcopy(a)
```

깊은 복사 방식엔 문제([python docs](https://docs.python.org/ko/3/library/copy.html) 참고)가 있음.
- 재귀 객체가 순한 루프를 만들 수 있음.
  - memo dictionary를 두어 이미 복사된 것을 저장하여 해결.
- 깊은 복사는 모든 것을 복사하기 때문에, 복사본 간에 공유해야할 것도 복사할 수 있음.
  - user-defined class가 복사 연산이나 복사된 구성요소 집합을 override 하도록 함.

## 함수 내 반환 시
reference parameter로 전달된 함수에서, parameter 값을 변경시켜서 올려주고 싶다면 아래와 같이 해야한다.  
```python
def change_param(param: List[int]):
    new = [1, 2, 3] # calculated value
    for i in range(new):
        param[i] = new[i]
```
위와 같은 방식을 사용하는 이유는  
위에서 배운 생복사, 얕은 복사, 깊은 복사 모두 함수 내부에서 선언된 list의 주소값을 사용하기 때문이다.  
우리는 함수 밖에서 온 param의 주소 값을 그대로 가지고 수정해야 하는데 모든 copy는 새로운 list를 할당하여 실제 param을 변경하지 못한다.  

위 코드는 아래와 같은 문제가 있다.
1. index out of range를 피하기 위해 param에 사용하고자 하는 idx가 존재하는지 체크해야 함.
2. 다 차원 list가 될 경우 더 많은 반복문과 위의 문제가 중첩됨.

이런 경우는 빈번히 사용될텐데  
reference list의 주소를 그대로 두면서 copy를 진행하는 방법이 존재하나 찾아보았으나 없는 것으로 보인다.  
아래와 같은 방법이 최선일 것으로 생각된다.
```python
def change_param(param: List[int]):
    new = [1, 2, 3]
    param.clear()
    param.extend(new)
```
이렇게 하면 기존의 list의 주소를 두고 값을 변경할 수 있다.
