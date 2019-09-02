---
layout: normal
title: Kivy
---

## kivy - interactive applications and games in python second edition

* [practice code](https://www.packtpub.com/support)

1. [chapter01](../chapter01_summary)  
    GUI Basic - Building an Interface

2. [chapter02](../chapter02_summary)  
    Graphics - the Canvas

3. [chapter03](../chapter03_summary)  
    Widget Events - Binding Actions

4. [chapter04](../chapter04_summary)  
    Improving the User Experience

5. [chapter05](../chapter05_summary)  
    multi touch game

6. [chapter06](../chapter06_summary)  
    video player

## 그 외 study 리스트

[build](../build)과정 중 문제점  
[label size](#label-size)를 text 사이즈에 따라 설정하기  

**Widget Parameter**:  
kivy widget constructor parametor를 추가하는 방법. [property 명시](https://kivy.org/doc/stable/api-kivy.properties.html).

**font**:  
한글폰트등의 폰트 적용 방법. 폰트도 StringProperty 임. [`font_name`으로 적용](https://kivy.org/doc/stable/api-kivy.uix.label.html#catering-for-unicode-languages).
* [눈누](https://noonnu.cc/)에서 무료폰트를 확인할 수 있음.

**connect .kv with .py**:  
`self.ids.~`으로 접근하는 경우도 있으며,  
`layout_content=ObjectProperty(None)`와 같이 Property를 생성하면, 해당 .kv 클래스에서 동일 name으로 사용하는 방식. (BiblePage 참고)

**dynamic added scroll view**:  
scroll view에 들어갈 widget들이 많을 때, 그걸 동적으로 추가하고 넣어주는 [코드](https://gist.github.com/smglab/a5f4fcfb094f54c44ff0)

**[mark up](https://kivy.org/doc/stable/api-kivy.core.text.markup.html)**:  
`markup=True`와 함께, text에 부분적으로 color, font 등의 수정을 할 수 있음.

**action bar**:  
action bar를 `top: root.height`로 위치 설정을 하였을 때, 윈도우에서 제대로 설정 되었지만, 안드로이드에서는 위에 상태표시줄까지 위치로 잡아 그만큼 잘리는 현상이 발생하였음.  
해당 코드를 `pos_hint: {'top': 1}`로 해결할 수 있음.  



### label size

label의 text에 따라 size를 조절해주는 [코드](https://stackoverflow.com/questions/18670687/how-i-can-adjust-variable-height-text-property-kivy)  
```python
    l.bind(width=lambda s, w: s.setter('text_size')(s, (w, None)))
    l.bind(texture_size=l.setter('size'))
```
`width`에 따라 `s`(label)의 `text_size`를 setter로 `(w, None)`으로 설정. 즉, `text_size`를 `width`로 설정하는 것  

kv 파일에서 text에 따라 size를 조절해주도록 하는 [코드](https://stackoverflow.com/questions/43666381/wrapping-the-text-of-a-kivy-label)
```python
    text_size: self.width, None
    size_hint: 1, None
    height: self.texture_size[1]
```
와 같이, `text_size`를 `width`로 맞추고, `height`를 width로 정해진 texture_size의 값으로 설정.

**주의사항**:  
위와 같은 size 조절은 `bind`로 발생함.  
즉 width와 texture_size가 변경될 때 dynamic하게 코드를 변경하는 것.  
따라서 위와 같은 코드 바로 뒤에 `l.height`와 같은 코드를 사용해도 height를 구할 수 없음.  
  - 실제로 scrollview 구현 중 height에 따른 scroll 위치를 적용하는데 애를 먹음.
  - `l.bind(height=self.lavel_height_changed)`와 같이, height에 bind를 통해 원하는 값들을 처리할 수 있음.