---
layout: normal
title: chapter 5
---

## 예제

1. **atlas** - images.kv  
2. **sound** - boom.py
3. **animation** - ammo.py, invader.py  
  origin position을 tx, ty로 설정  
4. **automatic bind** - dock.py
5. **concatenation of animation** - fleet.py
6. **multi touch** - shooter.py
  
## 개념

## Atlas

여러 image를 처리하기 위한 방법으로, `sprite`로도 알려져 있음
application image들을 하나의 큰 image로 group화 하여 request를 줄이는 방식  
하나의 큰 atlas 이미지와 각 이미지에 대한 좌표들을 json file로 저장하는 작업을 내부적으로 해줌  

atlas 이미지를 생성하기 위해 [pillow library](http://python-pillow.github.io/)가 필요하며 아래와 같은 명령어로 실행함  
  * `python -m kivy.atlas invasion 100 *.png` (basename, size, img list)
  * `basename`.png, `basename`.atlas(json format) 이 생성됨

atlas 이미지를 사용하기 위해서
  * kv에서는 `source: atlas://src/path/imgfile`와 같이 사용

## SoundLoader

kivy에서 sound effect를 사용하기 위해서 SoundLoader를 사용함  
`SoundLoader.load('soundfile.wav')`와 같이 soundfile을 load하면 Sound class를 return하고 이를 `.play()`를 통해 재생시킬 수 있음

## [Animation](https://kivy.org/doc/stable/api-kivy.animation.html)

목적지까지 움직이는 것과 같은 간단한 animation을 설정하는데 사용  
default로 period를 1초로 갖음  

`on_start`, `on_progress`, `on_complete`의 3개의 event를 bind  
  * `on_progress`에서 progression은 진행 정도

animation instance의 parameter는 적용할 widget의 어떤 property도 될 수 있음
  *  main.py의 start_game을 보면 font_size를 Animation에 적용하는 것을 확인할 수 있음

[transition](https://kivy.org/doc/stable/api-kivy.animation.html#kivy.animation.AnimationTransition)으로 목적지까지의 transition의 모양을 설정할 수 있음  

`on_complete`를 통해 두 개의 animation을 연결할 수 있음.  

## Automatic bind

`pos: self.parent.pos`를 layout에 선언함으로써 parent가 움직일때, child도 움직이도록 할 수 있음  
  * 이렇게 parent가 바뀔 때, child가 따라서 pos가 바뀌게 할 수 있는데, 이 pos의 변화와 parent가 아닌 다른 event에 의한 pos의 변화가 겹쳐서 발생하면 문제가 생길 수 있음. 따라서 parent의 pos 변화를 받도록 하는 widget을 만들고, 실제 widget은 마음대로 움직이도록 함 (ex/ dock.py)

## scheduling

kivy Clock을 import하여 사용  
`schedule_interval` 을 통해 주기적으로 해당 함수를 실행(단위는 초)  
`schedule_once` 를 통해 한 번만 해당 함수를 실행  

마찬가지로 `unschedule`을 통해 schedule을 해제할 수 있음  

## multi-touch

모든 kivy widget과 component는 multi-touch를 지원함  
kivy는 각 touch에 대한 data들을 제공하여 이를 활용해 multi-touch를 구현할 수 있도록 함  

[collide_point](chapter03_summary.md/##Touch-event) 로, `touch.pos`가 어디에 있는지를 통해 touch를 구분하도록 함  

`on_touch_down`, `on_touch_move`, `on_touch_up`은 모두 같은 touch reference를 사용하기 때문에 이를 통해 touch를 구분할 수 있음.  
예제처럼 `touch.ud` (user data)를 활용하여 down을 어디서 했는지 구분하는 등으로 사용 가능함.

* shooter.py 에서 next shoot까지 delay를 주기 위해 `reload_gun`을 사용하는 것

## keyboard

`Window.request_keyboard` 를 통해 keyboard를 받는데, paremeter 중 하나로 keyboard가 closed될 때 수행될 함수를 넣어주며, 보통 unbind를 넣음.  
`bind(on_key_down=)` 를 통해, key를 누를 때 수행 될 함수를 구현하여 bind 해 줌.  
mobile device에서는 keyboard를 사용하지 않아야 할 수 있음.  

어떤 event에 `bind` 할 수 있는 method의 개수는 제한이 없음.