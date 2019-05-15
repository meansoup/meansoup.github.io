---
layout: normal
title: Kivy android build
---

## android build

[android build](https://kivy.org/doc/stable/guide/packaging-android.html)는 ubuntu에서만 가능함.  
[Buildozer](https://github.com/kivy/buildozer)를 통해 전체 build process를 간편하게 실행할 수 있음. 현재 kivy에서 추천하고 있는 방법.  

build 과정
1. buildozer init
2. edit buildozer.spec
    * log_level=2 로 바꿔줘야 문제가 없음
3. ...


### issue

* installing/updating sdk platform tools if necessary:  
log_level=2 로 하면 해결 됨

* Aidl not found, please install it.
...