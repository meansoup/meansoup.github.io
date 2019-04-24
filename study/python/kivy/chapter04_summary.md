
# chapter 4

# 예제

1. Screen과 ScreenManager의 사용
2. color가 하위에까지 영향을 미치는 것
3. color를 동적으로 setting
4. stencilView
5. scatter
6. recording gestures
7. use gestures
8. behavior

# 개념

## ScreenManager

ScreenManager는 여러 device에서 screen을 적절하게 조절할 수 있게 해준다.  
multiple screen을 갖도록 해주며 screen간 switch를 쉽게 해준다.
  * ScreenManager는 항상 `Screen` widget을 가져아하고, 다른 Widget을 가질 수 없음
    * ColorPicker를 `Screen` 하위에 놓음(ex/01 - comicscreenmanager.kv)
    * `Screen`으로 사용되는 곳에도 명시가 필요함
      * `ComicCreator`는 `ComicCreatorScreenManager`의 `Screen`으로 사용되고 있으며, 따라서 `ComicCreator@Screen`을 통해 Screen임을 명시함(ex/01 - comiccreator.kv)
    * `name` property를 `Screen`에 명시하여 screen을 변경할 수 있도록 함.
      * `root.current = 'comicscreen'`을 통해 comicscreen으로 switch 함. `root`는 여기서 ScreenManager 이고, `current`는 active screen 임
    * `Screen`은 `manager` attribute를 갖고, 이를 통해 접근할 수 있음
      * `current = 'colorscreen'`으로 colorscreen으로 switch 함.(ex/01 - generaloptions.py)  
      `comiccreator.kv`에서 각 항목들에 대해 id, root를 부여하는 이유
    * ComicScreenManager가 Screen들을 통제하게 되었기 때문에 최상위가 ComicScreenManager로 바뀌어야 하고, comiccreator.py에서 이렇게 변경된 것을 확인할 수 있음 (ex/01 - comiccreator.py)

## Color

  * 동적 coloring  
    `canvas.add`와 `with ---.canvas:`를 통해 color를 추가할 수 있음.(ex/03 - toolbox.py)  
      * ToolStickman의 경우 `canvas.before.add`를 사용하였는데, 이는 `Color` instruction이 `Stickman` Canvas에 추가한 다른 instructions보다 먼저 적용되게 하기 위함이다.  
      다른 ToolFigure에서 `before`를 사용하지 않는 것은 해당 canva의 order에 대한 권한을 가지고 있기 때문이다.
      * 소스상 color_picker.color를 가져다 사용하며, `*`를 통해 `colorpicker.color`의 list를 unpack 해줌.
        * 예를들면 (1, 0, 1) 을 unpack하여 1, 0, 1로 만듦
      * Color를 import해야 함
       
  * **ColorPicker**
    * 색상을 고르는 widget, 자리를 많이 차지하는 편. 예제상 보이는 colorpicker와는 상관 없는 API를 말하는 것으로 보임.
  * **[transision](https://kivy.org/doc/stable/api-kivy.uix.screenmanager.html#changing-transitions)**
    * screen을 switch 할 때 어떤 animation이 보이는가에 대한 것.

  * `load_file`은 .kv를 include하는 것이며, 이와 유사하게 `load_string`으로 .kv를 python file에서 사용할 수 있음(ex/02)

## stencilView

  특정 영역에만 이벤트를 처리하기 위해서 `collide_points`와 같은 방법을 사용했었는데, 이건 group mode나 resize 같은 상황에서 완벽하지 않다.  
  따라서 StencilView를 쓰는데, `StencilView`는 drawing area를 해당 view의 공간까지로 제한하며, 밖에 그려진 것들은 숨겨진다.
   * `drawingspace`를 제한하기 위해 `StencilView`를 상속하도록 함. `DrawingSpace(stencilView)` (ex/04 - drawingspace.py)  

  `StencilView`는 `RelativeLayout`이 아니므로, `StencilView` class는 relative coordinates를 사용할 수 없다.  
  즉, 여기서 사용한다면 상위의 RelativeLayout을 사용하게 되는 것이며, 일반적으로 drawing은 `relative coordinates`를 사용하는 것이 좋으므로 `RelativeLayout`안에 `DrawingSpace`을 사용하도록 한다.
   * 원래 `DrawingSpace(RelativeLayout)`으로 RelativeLayout을 상속하고 있었으므로, 위의 수정을 반영하면서 RelativeLayout으로 DrawingSpace를 감싸도록 함. (ex/04 - comiccreator.kv)
     * RelativeLayout에서 width, height의 설정과, DrawingSpace에서 default로 `size_hint: 1, 1`을 통해 동일한 area를 갖고 있음을 확인.

  원래 touch event에 대한 정의는, 어디서든 할 수 있는 것으로 보임(ch3에서 다루는)
   * `on_touch_down`을 보면, toolbox.py의 `ToolButton`에 정의되어 있지만, collide_point로 가리키고 있는 범위는 drawingspace이기 때문이다.  
   혼동되었던 개념인데, 관련한 touch event를 해당 클래스 함수에서 전 범위에 관해 정의하고 있다고 생각하면 될 것 같다.

  `StencilView`에서는 특성상 코드가 이전과 변경됨.  
   * `on_touch_down`에서 collide_point을 drawingspace에서 했었으나, drawingspace는 StencilView로 ReleativeLayout이 아니므로, .parent.collide_point를 사용하여 위치를 확정한다.  (ex/04 - toolbox.py)  
     `update_figure`에서 더이상 collide_point를 고려하지 않는데, StemcilView가 이런 역할들을 하기 때문.  
     `update_figure`, `end_figure`에서 to_widget을 사용하지 않는데, 이미 RelativeLayout인 parent로부터 coordiantes를 받았기 때문. (어렵다.. diff 로 확인)

## scatter

  scale, rotate와 같은 기능들을 가지고 있는 class. 두 손가락으로 scale과 rotate를 할 수 있도록 구현되어 있고, mobile에서도 사용가능함.
   * `scatter`도 `RelativeLayout`처럼 relative coordinates를 사용 함.
  
  scatter 적용  
  1. DraggableWidget이 Scatter를 상속하도록 함. (ex/05 - comicwidgets.py)
  2. scatter가 event를 받을 수 있도록 `on_touch_down`에 `super.on_touch_down`를 추가 함.
  3. scatter가 `pos` property에 대한 `on_pos` method를 지원하므로 `on_touch_move` 대신 사용.
  4. scatter는 `rotation`과 `scale` property를 또한 지원하며, `on_rotation`, `on_scale` 사용.
     * DraggableWidget의 rotation, scale이 group mode에서 동작할 수 있도록 GeneralOptions class에 해당 property를 추가 및 구현.  
       * 여기서, 특정 DraggableWidget의 rotation, scale의 변화를 property로 간단히 GeneralOptions로 넘겨주고, GeneralOptions에서는 가지고 있는 child들의 property들을 바꿈으로 전체 적용을 하는 점에서, property의 장점을 확인.  
       toolbox.py에서 `return DraggableWidget`를 하는 부분을 새삼 확인.
  
## gesture

  kivy 에서는 gesture를 저장할 수 있는데, gesture를 string으로 저장함.  
  `on_touch_down`, `on_touch_move`, `on_touch_up` 마다 point를 저장하여 string으로 변환하는 방식이다.
   1. `gesture = Gesture()`로 Gesture를 생성하고 (ex/06)
   2. `gesture.add_stroke(self.points)`로 points를 넣고
      * `self.points += [touch.pos]`로 points가 기록되어 있음
   3. `gesture.normalize()`로 default number로 바꾸고
   4. `GestureDatabase.gesture_to_str(gesture)`로 string으로 출력하여 확인하도록 함.

  kivy 에서 저장한 gesture를 활용하는 방식.  
   1. `str_to_gesture`로 저장해둔 string gesture를 gesture로 바꿈  (ex/07 - drawingspace.py)
   2. `GestureDataBase.add_gesture`로 gesture를 database에 추가
   3. `on_touch_down`, `on_touch_move`, `on_touch_up`에 대한 함수 구현.  
      각 함수에서 `[touch.pos]`를 저장하고, `on_touch_up`에서 `GestureDatabase.find`를 통해 database에서 저장된 gesture가 있는지 찾도록 함.
      * 여기서는 `down`, `move`, `up`으로 해당 함수들을 구현하고 있으며, `activate`, `deactivate` 함수들로 `bind`, `unbind`를 통해 해당 함수들을 매핑하여 사용하고 있음.
   4. 찾은 값과, database에 넣은 gesture가 일치하는지 확인하여 사용.
      * 여기서는 `discriminate`를 통해 해당 그림들을 그리도록 하였음.

   * `self.gdb = GestureDatabase()`로 database 생성
   * line을 `rotate(90)` 등을 통해 여러 방향에서의 직선을 인식할 수 있도록 함
   * `find(gesture, minscore=0.50)` 에서 minscore는 정확도. 여기선 틀릴 확률이 높으므로 0.5를 사용
   * `find()` 의 return 값은 **score of the recognition**과 **recognized gesture**의 pair
     * 여기서는 `recognized[1]`를 사용해서 어떤 gesture인지 확인하고 있음
   * drawingspace.py 에서 children property를 쓰는 것
   * `disabled` property는 자동으로 children 들도 deactivate로 만듦. 이벤트가 children한테 전달되지 않음
     * 여기선 gesture activate 시, tool_box.disabled로, tool_box의 모든 것들이 deactivate로 선택되지 않음. (ex/07 - drawingspace.py)

## behavior

  특정 widget의 classic behavior를 다른 behavior에 사용할 수 있음.  
  예를 들어, ButtonBehavior(on_press, onRelease를 사용하기 위한)를 Label이나 Image widget에 사용할 수 있음.  
  behavior는 widget의 appearance를 바꾸는 것이 아니라, functionallity만 넣어줌  
  **multiple inheritance**를 통해 사용할 수 있지만, touch가 중복되거나, 동일 property를 갖는 경우에 대해 조심해서 사용해야 함.  
  현재는,
   * ButtonBehavior
   * ToggleButtonBehavior
   * DragBehavior
  
  의 Behavior만 사용할 수 있음.
  
  * StatusBar에서 `ButtonBehavior`를 multiple inheritance로 상속하고, `on_press`를 구현
  * `Popup`을 kivy에서 제공하고, 사용할 수 있음 (ex/08 - statusbar.py)

## style

