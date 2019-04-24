---
layout: normal
title: chapter 1
---

* kivy
Android, iOS, Linux, windows, Mac OS 전부 동작  
핵심 부분을 Cython으로 구현하고 대부분의 그래픽 동작을 directly GPU와 연결하여 속도가 빠름  

* FooApp class 는 자동으로 foo.kv와 연결됨 (FooApp class를 갖는 파일 명은 상관 없음)

예제
----------
```
03 - 이렇게 widget을 personalize 할 수 있음. py에 해당 위젯 클래스 생성
04 - 이렇게 widget을 상속하여 사용할 수 있음. MyButton@Button
05 - layout 들 특성 확인 가능
06 - <Layout>같은 base class로 변경사항을 전체 적용가능
07 - pagelayout
08 - kv 파일들을 Builder.load_file 로 사용하는 등 kv 활용
```

개념
----------
```
widget		kivy GUI component. the minimal graphical units.
property	widget의 속성 중 하나 (ex/ text)
self		자기 자신
root		계층 최상위
id		.kv에서 다른 위젯에서 접근할 수 있도록 하는 값
property
		x, right, center_x
		y, top, center_y
		width, height를 각 self, root에 대해 쓸 수 있음
	
		size_hint - 0~1 의 비율 크기
			size_hint_x, size_hint_y
		pos_hint - 0~1 의 비율 위치	
```

layout
----------
```
1. FloatLayout
	size_hint, pos_hint로 창에 대한 비율로구성
2. RelativeLayout
	FloatLayout과 동일한데, layout에 대한 비율로 구성
3. GridLayout
	행과 열로 layout 구성
4. BoxLayout
	세로나 가로로 쌓는 구성
5. StackLayout
	BoxLayout과 동일한데, 계속 방향으로 쌓는 구성
6. ScatterLayout
	RelativeLayout과 유사한데, rotating, scaling, translating과 같은 멀티터치 사용
7. PageLayout
	멀티페이지 이펙트를 주고, 흔히 다른 layout들을 내부에 widget으로 사용
	swipe_threshold - 어느 비율만큼 당겨야 페이지가 넘어가는지
```
