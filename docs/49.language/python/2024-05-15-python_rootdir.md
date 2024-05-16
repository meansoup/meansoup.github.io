---
layout: post
title: 파이썬에서 root directory를 library로 쉽게 찾는 방법
sidebar_label: find rootdir
nav_order: 1
parent: python
grand_parent: language
lang: ko
permalink: /docs/algorithm/language/python/python-rootdir
sitemap:
  lastmod: 2024-05-16
---

{: .note-title .mb-6 }
> rootdir
>
> [find rootdir](/ko/docs/algorithm/language/python/python-rootdir){: .btn .btn-purple }
> [add rootdir path for import](/ko/docs/algorithm/language/python/python-import-rootdir){: .btn }

파이썬에서 root directory를 찾기란 쉽지 않다.  
**rootdir** library를 통해 root directory를 직관적이고, 빠르고, 쉽게 찾을 수 있다.

### Usage

1. `pip install rootdir`로 rootdir를 설치한다.
2. `__root__.py`를 root path에 추가한다.
3. `import rootdir`로 rootdir를 import 한다.
4. `rootdir.root_dir(__file__)`로 rootdir을 확인한다.

### example

만약 root directory가 필요하다면 아래와 같은 코드로 쉽게 확인할 수 있다.  
아래 코드를 복사하여 동작을 확인할 수 있다. 

```python
import rootdir

if __name__ == "__main__":
    print(rootdir.root_dir(__file__))
```

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

**__root__.py**를 추가했다면 어느곳에서든 **rootdir**를 통해 root directory를 찾을 수 있다.  
예를 들면 **b_1_1_1.py**에서는 아래와 같이 rootdir를 찾을 수 있다.

```python
import rootdir

if __name__ == "__main__":
    print(rootdir.root_dir(__file__))
```

b_1_1_1.py 뿐만 아니라 b_1_2.py, b_2.py 등 어떤 프로젝트에서도 위 코드를 통해 동일하게 rootdir를 찾을 수 있다.

---

[^1]: rootdir에 명시된 [sample project](https://github.com/meansoup/rootdir/tree/main/sample)에서 실제 sample project와 동작을 확인할 수 있다.
