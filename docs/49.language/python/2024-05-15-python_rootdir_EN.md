---
layout: post
title: The easiest way to find root directory in Python
sidebar_label: find rootdir
nav_order: 1
parent: python
grand_parent: language
lang: en
permalink: /docs/algorithm/language/python/python-rootdir
sitemap:
  lastmod: 2024-05-16
---

{: .note-title .mb-6 }
> rootdir
>
> [find rootdir](/docs/algorithm/language/python/python-rootdir){: .btn .btn-purple }
> [add rootdir path for import](/docs/algorithm/language/python/python-import-rootdir){: .btn }


Finding the root directory in Python can be challenging.  
With the **rootdir**, you can find the root directory intuitively, quickly, and easily.

### Usage

1. Install rootdir with `pip install rootdir`
2. Add `__root__.py` to your root path.
3. Import rootdir with `import rootdir`
4. Check the root directory with `rootdir.root_dir(__file__)`

### example

If you need to find the root directory, you can easily do so with the following code.  
Copy and run the code below to verify its functionality.

```python
import rootdir

if __name__ == "__main__":
    print(rootdir.root_dir(__file__))
```

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

Once you add **__root__.py**, you can find the root directory from anywhere using **rootdir**.  
For example, in **b_1_1_1.py**, you can find the rootdir as shown below.

```python
import rootdir

if __name__ == "__main__":
    print(rootdir.root_dir(__file__))
```

You can find the root directory using above code not only in b_1_1_1.py but also in b_1_2.py, b_2.py, or any other file in the project.

---

[^1]: You can check the actual [sample project](https://github.com/meansoup/rootdir/tree/main/sample) and its functionality in the sample project provided by rootdir.
