---
layout: normal
title: chapter 6
---

## 예제

1. video widget
2. AsyncImage

## 개념

## video widget

kivy 에서는 video widget을 제공함.  

**property**:  

* allow_stretch - True이면, screen size에 맞게 video가 커질 수 있음.
* color - play 중이지 않을 때 덮어쓰는 색상.
* source - 재생할 비디오 위치.
  * `#:set A B`를 통해 kv에서 주소를 define하여 사용할 수 있음.  

일반적으로 [Factory](chapter04_summary.md/##Factory)를 통해 재정의하여 사용하는데, property를 활용하여 재정의 함.

* `on_state`에서 state가 변경될 때 호출되며 (state는 play, pause, stop을 가짐)
* `on_eos`는 end of stream 일때 호출되며
* `_on_load`는 video가 memory로 load될 때, ready to play일 때 실행 됨.

## AsyncImage

AsyncImage는 Image와 달리 image가 loading 되는 동안 program을 사용할 수 있도록 함.  
큰 이미지를 받을 때 사용될 수 있음.

-----

이외에 sidebar, ScrollView와 같은 kivy widget들의 활용.