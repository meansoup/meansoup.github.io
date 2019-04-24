
# chapter 3

# 예제

1. id와 attribute 사용과 차이 구분 (.kv)
2. touch event 사용과 comicwidgets의(py/kv) StickMan/DraggableWidgets의 관계
3. localizing coordinates
4. drawing_space로의 접근과 python을 import하는 상황
5. bind/unbind, widget 생성을 drawingSpace가 아니라 widget에 하기 위해 to_local을 사용하는 것
6. bind on .kv
7. kivy properties
8. kivy properties advanced, root 주의

# 개념

* **id**
  * .kv 내에서만 접근 가능함
  * 보통 맨 앞에 _를 붙이지만, 구분하기 위함이지 필수는 아님
* **attribute**
  * 어떤 widget에 attribute를 생성하고, id를 여기 넣어주면 그 attribute로 접근
  * commiccreator.kv의 ToolBox에서 drawing_space attribute는 _drawing_space(id)를 가지고 있으며, python에서 drawing_space로 여기에 접근 가능(ex/01)
  * root도 동일 방식 (ex/01)
* **root**: base widget in the rule hierarchy
* **self**: current widget
* **app**: the instance of the application

## Touch event

touch event는 mouse, finger touch, magic pen touch으로 나뉘며, 아래 event는 mouse, finger touch에서 사용 가능하다.
  
* **on_touch_down**: new touch start
* **on_touch_move**: the touch is moved
* **on_touch_up**: the touch ends
  * 각 touch event는 parameter(touch)로 여러 정보를 갖는 [MotionEvent](https://kivy.org/doc/stable/api-kivy.input.motionevent.html#kivy.input.motionevent.MotionEvent)를 받음
  * return value가 hierarchy 구조상 parent에게 touch event를 신경 써야 하는가/아닌가를 알려주는 역할(ex/02 - comicwidgets.py)
  * 유사하게 super.on_touch_~ 으로 chidren의 event를 신경쓸 수 있음

* **collide_point**는 모든 widget이 app(coordinate space)에서 발생하는 touch event(MotionEvent)를 받지만, 그 event가 특정 widget에서 발생하는지 확인하는 보편적인 방법(ex/02 - comicwidgets.py)

## dynamic create/deleate canvas

* `self.selected`에 Line instance를 넣어서 삭제할 수 있게 구현한 부분 확인 (ex/02)
* `with self.canvas`를 통해 canvas에 instructions를 넣을 수 있음
* `self.canvas.remove(self.selected)`를 통해 canvas에 self.selected를 지울 수 있음
* to_parent로 부모의 coordinate에 접근
  * DraggableWidget의 parent(drawing space)의 범위 조건 체크를 위해 사용(ex/02 - comicwidgets.py)
* left corner를 벗어나지 않게, `(touch.x - self.width/2, touch.y - self.height/2)`

## localizing coordinates

to_parent 같이, 현재 widget에서 구현하지만, 움직일 공간이 parent, 혹은 parent's parent와 같은 경우 coordinates의 범위를 지정해주는 것.  
RelativeLayout은 coordinate의 위치 값들이 다 다르니까.  
RelativeLayout이 아닌 layout들은 그 상위에 대해 절대적인 coordinate 값을 가지고 있음.

* **to_parent()**: transform relative coordinates inside RelativeLayout to the parent of RelativeLayout
* **to_local()**: transform the coordinates of parent of RelativeLayout to RelativeLayout
* **to_window()**: transform the coordinates of the current widget to absolute coordinate with respect to the window
* **to_widget()**: transform the absolute coordinates to coordinates within the parent of the current widget

* `self.parent.drawing_space`를 통해 ToolButton에서 parent(ToolBox)의 drawing_space attribute에 접근 (ex/04)
* `add_widget()`으로 layout에 widget을 더해줌 (ex/04 - toolbox.py)
* [`#:import toolbox toolbox`](https://kivy.org/doc/stable/guide/lang.html#special-syntaxes)으로 toolbox를 .kv에 import 함. (ex/04)
  * comiccreator.py에서 comiccreator.kv를 사용하고(kv에서 자동으로), commiccreator는 toolbox.kv를 사용하므로(내부적으로 사용하며, .py에서 Builder.load_file로 load), toolbox.py는 자동으로 호출되지 않아, import 필요.  
  즉, toolbox.py가 main이었다면 import를 안해도 .kv를 가져갔겠지만, toolbox가 main이 아니라 사용되는 상황에서, .py를 import 해줘야 했음.

## bind/unbind

binding의 2가지 방법
1. at .py, it works for every instance about this class  
    touch_down의 경우 overriding하여 사용하고, 나머지에 대해 bind 함.  
    we didn't want the `on_touch_move`, `on_touch_up` events active all the time.  
    move와 up은 touch_down이 발생한 이후에 발생할 수 있으므로, 이 이벤트들을 항상 active 상태에 두는 것이 아니라, touch_down시에 bind를 통해 관리하도록 하는 것. (ex/05 - toolbox.py)

    * [`#:import toolbox toolbox`](https://kivy.org/doc/stable/guide/lang.html#special-syntaxes)으로 toolbox를 .kv에 import 함. (ex/05)
        1. `ToolCircle(toolbox.kv)` mapping with `ToolCircle(toolbox.py)` by `Builder.load_file('toolbox.kv')`
        2. `ToolCircle(toolbox.py)` extends `ToolFigure(ToolButton)` in python
        3. `ToolButton(toolbox.py)` mapping with `ToolButton(toolbox.kv)`
        4. for use ToolCircle with full operation(py/kv) it needs to import py at kv
    * `widget.canvas.add`의 사용과 함께, widgetize, end_figure에서 그리는 방법 (ex/05)

2. at .kv, it works only for this instance  
    특정 instance에 대해 bind하기 때문에 collide_point를 사용할 필요가 없음.

    * **Button**: `on_press:`와 `on_release:` (ex/06 - generaloptions.kv)
    * **ToggleButton**: `on_state` - .py에서 'down', 'normal'로 구분

* `clear_widgets()`: 모든 widget을 지움 (ex/06 - generaloptions.py)
* `remove_widget(x.children[0])`: 가장 최근에 추가된 widget을 지움


## [Kivy property](https://kivy.org/doc/stable/api-kivy.properties.html)

property가 정의되면 Kivy는 내부적으로 property와 연관된 event를 생성하고, 이 event는 'on_**property_name**' method와 연결됨. (ex/06 - generaloptions.py)  
따라서, property에 값을 넣어주면 on_**property** 가 자동으로 실행 됨.
  *  comicwidgets.py의 `on_touch_move()`에서 generalOptions의 `translation =`를 통해 generalOptions.py의 `translation`에 값을 넣고 이 property는 `on_translation()`를 trigger함.
    * traslation의 사용과, on_translation이 child에 매개변수로 넘겨주는 값들 주의(ex/07)

* `center_x`도 property를 내부적으로 사용하는 것.
* .kv의 vertex instruction의 attribute도 내부적으로 property로 사용 됨.
* python property와 혼동해서는 안됨.  
* **attribute**: used to describe variables(references, objects, instances) that belongs to class
  * Kivy Property는 항상 attribute, attribute가 모두 Kivy Property는 아님
* kivy property는 static attribute로 선언되나, internally transformed to attribute instansces.
  * `counter`는 static하게 선언되나 attribute instances가 되고, `previous_counter`는 static attribute로 되어 all StatusBar가 share.. (ex/07 - statusbar.py)
    * class name이나 `__class__`로 바로 접근 가능 (ex/07 - statusbar.py)
  * `__init__` 안에서 선언되는 것들은 instance 임.
    * `self.selected` is not shared (ex/06 - comicwidgets.py)  

  Kivy property
    * **BoundedNumericProperty**: set the maximum and minimum values
    * **AliasProperty**: extend the properties, create our own properties
    * NumericProperty
    * StringProperty
    * ListProperty
    * DictProperty
    * ObjectProperty
    * StringProperty

* 바로바로 다른 widget의 값을 변화시키는 심층 활용 (ex/08)
  1. drawingspace.py에서 `status_bar.counter` 변경
  2. statusbar.py의 `counter`변경 및 `on_counter` 호출
  3. statusbar.kv의 `root.counter`의 변경 및 `on_counter`에 의한 `msg_label`변경
    * 외부 widget에서의 변경 확인
    * .kv에서 root는 해당 .kv 파일에서의 최상위 hierarchy를 가리키는 것으로 보임
      * `root.counter`가 comiccreator를 가리키지 않고 statusbar를 가리키며, `self.counter`는 Label을 가리키는 것으로 보임 