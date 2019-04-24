
# chapter 2

# 예제

1. canvas 그리는 방법에 대한 예제(Triangle ~ Mesh)
2. line을 원, 삼각형, 사각형 등으로 그리는 예제
3. 이미지와 색상
4. canvas.after
5. 이동, 회전
6. comicWidget.kv: PushMatrix, PopMatrix  
	toolbax.kv: Push/PopMatrix with canvas.after, self.x/y  
	drawingspace.kv: default Push/PopMatrix with canvas.before  

# 개념

* **coordinate space**  
	coordinate space는 제한되지 않으며, bottom-left corner of the screeon을 origin으로 함
* **canvas**  
	widget에 vector shape를 그릴 수 있음  
	canvas에 그리는게 아니라, canvas는 coordinate space에 그리는 명령들의 집합  
	모든 widget은 각각 Canvas를 포함.  
	모든 widget은 동일한 coordiante space를 공유  
	coordiante space는 windows나 screen size에 제한되지 않음  
    canvas는 canvas.before, canvas, canvas.after의 세 객체를 가짐.  
	canvas.after는 가장 마지막에 호출되어 다른 widget들 위에 생성됨.(ex/04)

* **vertax instruction**  
	inherit from the VertexInstruction. 어떤걸 그릴 건지에 대한 것.
	VertexInstruction을 상속하기 때문에 pos, size가 Widget거랑 다름. fixed value를 써야함
* **context instruction**  
	inhefit from the CntextInstruction. 어디에, 어떻게 그릴지에 대한 것. (Color, Rotate, Translate, Scale)

## [vertax instruction](https://kivy.org/doc/stable/api-kivy.graphics.vertex_instructions.html)
기본적인 모양들을 그리기 위한 명령어.

**instruction** | **description**
----------------|----------------
Rectangle |
Ellipse	| 부채꼴 같은 것. 0도가 12시</br> angle_start, angle_end 로 부채꼴을 그릴 수 있음</br> segments 는 몇 개의 선으로 원을 그리는지에 대한 것. 무제한의 선으로 원을 그려야 정확한 원이겠지만, default=180, segments : 3으로 하면 삼각형(ex/01)
Triangle | x,y points 3개 -> 삼각형
Quad | points 4개 -> 사각형
Line | points 2개 -> 선 (2개씩 여러 개로 여러 선 그릴 수 있음)
Point | points 1개 -> 점 (여러 개로 여러 점 찍을 수 있음 ex/01)
Bezier | 곡선. points를 attractors로 사용. (math formalism.. 수학적)</br> dash_length 는 점선의 길이, dash_offset 은 점선 사이의 거리
Mesh | 삼각형의 조합으로 이루어지며, 굉장히 수학적


## context instruction
colors, rotating, translating, scaling the coordinate space.  
coordinate space에 위와 같은 변화들을 주기 위해 사용하는 명령어.

**instruction** | **description**
----------------|----------------
`source: 'kivy.png'` | 이미지를 넣을 수 있음
`Color: rgba:` | color 설정 가능. 이미지가 있다고 해도, 이미지가 해당 컬러를 갖게 됨(ex/03)
`Rotate: angle:` | 회전 </br>  `Rotate: axis:` - 어떤 축으로 할지 축을 지정(ex/05)
`Translate: x: or y:` | 이동. 회전 상태라면, x, y의 방향이 반대가 됨
`Scale: xyz:` | 각 축에 대한 size를 비율로 지정. 0.5배를 했다면, 원상복구를 위해선 2배를 해줘야 함

* **PushMatrix**: PushMatrix, which will save the current coordinate space context
* **PopMatrix**: PopMatrix, which return the context to its original state. 즉, 이 사이에 context instruction을 쓰면 다른애들 영향 x.
	* canvas에서 적용, canvas.after에서 해제하는 방식으로도 사용함(ex/06)

* Color, Rotate, Translate, Scale은 모두 설정하면 그 다음부터 coordinate space에 영향을 계속 미침.
* 모든 적용을 회피하기 위해선 RelativeLayout 하위에서 적용하면 됨. RelativeLayout은 내부적으로 widget의 position 등을 결정하기 때문
* RelativeLayout은 내부에 PushMatrix, PopMatrix를 가지고 있음.
* widget 속의 각 widget들은 각각 canvas.before, canvas, canvas.after를 가짐
* canvas.before에는 별도의 Push/PopMatrix가 있어 여기서 구현하면 canvas 전에 cotext를 원상 복구.
