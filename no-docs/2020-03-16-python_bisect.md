<!-- ---
layout: post
title: bisect implementation
tag:
  - python
---

## bisect

프로그래밍에서 가장 흔히 쓰이는 binary search.  
python에서는 아래와 같이 사용된다.  
```python
import bisect
bisect.bisect([1,2,3,5], 4)
```

## python 코드

[cpython bisect 구현](https://github.com/python/cpython/blob/master/Lib/bisect.py) 참고.

코드를 구현해야할 경우도 있지만,  
bisect가 어떻게 구현되는지를 보면 binary search 알고리즘을 이해하기 쉽다.  

`bisect_left`와 `bisect_right`에서 어떤 코드 차이가 있는지를 확인하는 것도 도움이 된다. -->