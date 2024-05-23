---
layout: post
title: 파이썬에서 다른 폴더 import 쉽게 하기
sidebar_label: import rootdir
nav_order: 2
parent: python
grand_parent: language
lang: ko
permalink: /docs/algorithm/language/python/python-import-rootdir
sitemap:
  lastmod: 2024-05-17
---

{: .note-title .mb-6 }
> rootdir
>
> [find rootdir](/ko/docs/algorithm/language/python/python-rootdir){: .btn }
> [add rootdir path for import](/ko/docs/algorithm/language/python/python-import-rootdir){: .btn .btn-purple }

파이썬에서 다른 폴더에 있는 코드를 import 하는 것은 굉장히 불편한 일이다.
python에서 import를 하기 위해선 적절한 path를 찾아서 `sys.path.append(...)`를 통해 추가 해줘야 한다.  

**rootdir** library를 통해 root directory를 직관적이고, 빠르고, 쉽게 추가할 수 있다.

### Usage

1. `pip install rootdir`로 rootdir를 설치한다.
2. `__root__.py`를 root path에 추가한다.
3. `import rootdir`로 rootdir를 import 한다.
4. `rootdir.root_dependency(__file__)`로 rootdir를 추가한다.

### example

만약 directory 구조의 python 프로젝트여서 다른 directory의 code를 import할 필요가 있다면 아래 코드를 복사하여 path를 추가하고, root directory 기반으로 import를 할 수 있다.

```python
import rootdir
rootdir.root_dependency(__file__)
```

**rootdir**를 통해서 위와 같은 코드로 dependency를 path에 추가하는 것은 directory 구조와 관계 없이 어느 파일에서든 동일하게 import할 수 있다.

### sample

아래와 같은 <u>sample project</u>[^1]를 참고하면, rootdir를 더 잘 이해하고 효율적으로 활용할 수 있다.

```
.
└── example/
├── a/
│   └── a_1.py
├── b/
│   ├── b_1/
│   │   ├── b_1_1/
│   │   │   └── b_1_1_1.py
│   │   └── b_1_2.py
│   └── b_2.py
├── main.py
└── __root__.py
```

**__root__.py**를 추가했다면 어느곳에서든 **rootdir**를 통해 root directory를 추가하여 import를 쉽게할 수 있다.  
예를 들면 **b_1_1_1.py**에서는 아래와 같이 rootdir의 directory를 추가할 수 있다.

```python
import rootdir
rootdir.root_dependency(__file__)

from a.a_1 import print_a_1

if __name__ == "__main__":
    print(rootdir.root_dir(__file__))
    print_a_1()
```

b_1_1_1.py 뿐만 아니라 b_1_2.py, b_2.py 등 어떤 프로젝트에서도 위 코드를 통해 동일하게 rootdir를 추가하고 동일하게 import 문을 활용할 수 있다.  
번거로운 `sys.path` 추가 작업을 하지 않아도 되며 path 계산도 하지 않아도 된다.

---

[^1]: rootdir에 명시된 [sample project](https://github.com/meansoup/rootdir/tree/main/sample)에서 실제 sample project와 동작을 확인할 수 있다.
