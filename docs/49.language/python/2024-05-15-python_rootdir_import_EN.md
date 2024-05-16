---
layout: post
title: The easiest way to import other directory in Python
sidebar_label: import rootdir
nav_order: 2
parent: python
grand_parent: language
lang: en
permalink: /docs/algorithm/language/python/python-import-rootdir
sitemap:
  lastmod: 2024-05-17
---

Importing code from different folders in Python can be very cumbersome.  
In order to import in Python, you need to find the appropriate path and add it using `sys.path.append(...)`.

With the **rootdir** library, you can add the root directory in an intuitive, fast, and easily.

Install rootdir with pip install rootdir.
Add __root__.py to the root path.
Import rootdir with import rootdir.


### Usage

1. Install rootdir with `pip install rootdir`
2. Add `__root__.py` to your root path
3. Import rootdir with `import rootdir`
4. Add the rootdir with `rootdir.root_dependency(__file__)`

### example

If you have a Python project with a directory structure and need to import code from different directories, you can copy the following code to add the path and perform imports based on the root directory.

```python
import rootdir
rootdir.root_dependency(__file__)
```

You can use the same import code regardless of the directory structure, the path of the specific file.  
With **rootdir**, you can add the directory by the above code.


### sample

Refer to the following <u>sample project</u>[^1] to better understand and efficiently use rootdir.

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

After adding **__root__.py**, you can easily add the root directory and perform imports from anywhere using **rootdir**.  
For example, **in b_1_1_1.py**, you can add the directory with rootdir as follows.

```python
import rootdir
rootdir.root_dependency(__file__)

from a.a_1 import print_a_1

if __name__ == "__main__":
    print(rootdir.root_dir(__file__))
    print_a_1()
```

Not only in b_1_1_1.py, but also in b_1_2.py, b_2.py, and any other file in project, you can add rootdir and perform imports in the same way using the above code.
You don't need to add sys.path or calculate path.


---

[^1]: You can check the actual [sample project](https://github.com/meansoup/rootdir/tree/main/sample) and its functionality in the sample project provided by rootdir.
