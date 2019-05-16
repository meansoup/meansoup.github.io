---
layout: normal
title: Kivy android build
---

## android build

[android build](https://kivy.org/doc/stable/guide/packaging-android.html)는 ubuntu에서만 가능함.  
[Buildozer](https://github.com/kivy/buildozer)를 통해 전체 build process를 간편하게 실행할 수 있음. 현재 kivy에서 추천하고 있는 방법.  

build 과정
1. sudo pip install buildozer
2. buildozer init
3. edit buildozer.spec
4. ...


### issue

* installing/updating sdk platform tools if necessary:  
    `buildozer.spec`에서 log_level=2 로 하면 해결 됨

* Aidl not found, please install it[:](https://github.com/kivy/buildozer/issues/824)  
    license 관련 문제가 나올 때, `y` 를 입력