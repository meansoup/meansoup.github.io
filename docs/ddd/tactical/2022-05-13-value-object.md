---
layout: post
title: 제대로 알자, VO
parent: 전술적 설계
grand_parent: Domain Driven Design
nav_order: 5
permalink: /docs/ddd/tactical/vo
---

DDD를 꽤나 공부했다고 생각했는데도 개발/설계를 해보면 DDD는 정말 어렵다.  
개발 사이트나 블로그, 책을 훑어보듯 보면 VO는 참 쉽다.  
value를 저장하고 바뀌면 안되는 녀석.

쉬워보이지만 설계할 때 보면 정말 명확하지 않다.  
개념을 명확하게 잡아야 설계에서 써먹을 수 있다는 생각이 이번에 들었다.  

*Vaughn Vernon의 Implement Domain Driven Design*의 **Value Object** 챕터를 작년에도 읽고 올해도 읽는데,  
DDD 설계와 논의를 진행하고 나서 읽으니까 더 와 닿는 것들이 많아 정리해본다.


## ValueObject(VO)

Value Object는 말 그대로 값을 갖는 객체를 말한다.  
값을 갖기 때문에 이 값 자체가 변할 수는 없다.

<div class="code-example" markdown="1" style="font-size: 0.8em">
예시
{: .label .label-yellow}  

계좌에 100원이라는 값이 있다고 치자.  
친구가 10원을 이체해줬으면 110원이 된다.  
이건 100원이라는 값 자체가 110원이 된게 아니다.  
내 계좌가 가지고 있는 값이 100원이라는 값에서 110원이라는 값으로 바뀐 것이다.

즉, 값 자체는 바뀌지 않는다.  
값이 대체되는 것 뿐이다.
</div>


## VO의 특징

**Value Object**의 특징은 가볍지 않다.  
어떤 글보다 이 책에서 명확하게 설명하고 있는데 이걸 잘 이해해야 개발에서 VO를 잘 녹여낼 수 있지 않을까 싶다.

아래의 특징들은 VO의 특징이기도 하고,  
이런 특징들이 없거나 필요하지 않은 모델은 VO가 아닐 수 있다.  


### domain의 어떤 대상을 측정하고 수량화하고 설명한다

모든 VO는 **model의 특성의 의미**를 가지고 있고 이를 측정, 수량화, 설명한다.  
이 말은 **domain model의 어떤 값이 측정, 수량화, 설명을 한다면** VO일 가능성이 크다는 것이다.

<div class="code-example" markdown="1" style="font-size: 0.8em">
예시
{: .label .label-yellow}  

**나이**를 예로 들어보자.  
나이는 실제하는 대상은 아니지만 대상이 살아온 햇수를 **측정하거나 수량화**한다.

**이름**을 예로 들어보자.  
이름도 실제하는 대상은 아니지만 대상을 어떻게 부를지를 **설명**해준다.
</div>


### immutable하다

**절대로 변하지 않는 것**. 가장 대표적인 VO의 특징이다.  
이 특성과 밀접하게 관련있는 중요한 특징들이 있다.  
- 그냥 변하지 않아야 돼 하는게 아니라, 관련된 특성들을 잘 알고 이해하는게 중요하다.

aggregate의 Id도 절대 변하면 안되니까 VO를 사용할 수도 있다.


### 관련 특성을 모은 필수 단위로 개념적 전체(Conceptual Whole)를 모델링한다

대상을 나타내기 위해 **개별적인 특성이 아닌 하나의 전체 값으로 모델링 되어야 한다**는 것을 **개념적 전체(Conceptual Whole)**라고 한다.  

<div class="code-example" markdown="1" style="font-size: 0.8em">
예시
{: .label .label-yellow}  

금액을 말할 때 **100**은 의미가 없고 **원**도 의미가 없다.  
**100원**이 합쳐져야 금액이라고 할 수 있다. 이게 바로 개념적 전체이다. 
</div>

이 개념이 중요한게 Value Object는 불변하는 값이야 라고 해서 하나의 VO에 때려박는건 개념적 전체를 무시한 DDD의 Value Object가 아닌 그저 Value에 불과한 것이다.  
각 VO가 유비쿼터스 언어에 따라 적절하게 이름 붙여진 응집도 높은 개념적 전체를 구성해야 한다.  

개념적 전체는 불변성과도 밀접하게 관련이 있다.  
위의 예시에서 금액(money) 객체에 **100**을 넣어두고 나중에 **원**을 붙이는 건 안된다.  
개념적 전체를 위해 constructor에서 한번에 완성된 VO가 나와야 한다.


### 측정이나 설명이 변경될 땐 완벽히 대체 가능하다

Entity가 VO를 가지고 있는데 올바른 상태의 VO가 아니라면 새로운 값으로 대체되어야 한다.  

<div class="code-example" markdown="1" style="font-size: 0.8em">
예시
{: .label .label-yellow}  

숫자를 예로 들어보자.  
`int total = 3;` 에서 total의 값이 변경되면 `total = 4;`를 한다.  
`3 = 4;`와 같이 3의 값을 바꾸는게 아니라 total에 새로운 value로 대체하는 것이다.  

이름을 예로 들어보자.  
`FullName fullName = new FullName("임", "꺽정");`에서 이름을 개명해서 임걱정으로 바꾼다고 하면 `FullName fullName = new FullName("임", "걱정");`과 같이 한다.  
~~`fullName.setFirstName("걱정");`~~과 같이 한다면 VO가 아닌 것이고 하면 안되는 짓이다.
</div>


### 다른 값과 등가성을 사용해 비교할 수 있다

VO에는 entity처럼 id가 없다.  
두 객체의 모든 **property가 같다면 같은 객체로 간주한다**.


### collaborator에게 side effect free한 행동을 제공한다

VO의 함수는 불변성을 침해하면 안되기 때문에 side-effect free한 함수만 제공해야 한다.  
side-effect free method라는 것은 **함수를 수행할 때 어떤 수정도 발생하지 않는 함수**를 말한다.  

1. 내 값(함수를 가진 VO)을 바꿔야 한다면 **대체를 적용**한다.
  - VO의 함수 내부에서 값을 계산한 새로운 VO를 반환할 수 있다. 그치만 수정은 절대 일어나선 안된다.
2. 중요한건 **남의 값(parameter로 들어오는 객체의 property)도 바꿔서는 안된다**.
  - 간과하기 쉬운 부분인데 VO가 Entity를 받아서 entity의 값을 수정한다면 이건 side-effect를 한참 만드는 설계이다.
  - VO가 Entity를 받아선 안되고 연산이 필요하다면 Entity에서 필요한 Value를 만들어서 받아야 한다.
    - 설령 entity가 수정되지 않는다고 하더라도 **코드를 읽는 사람은 entity의 값을 바꾸는지 바꾸지 않는지를 알 수 없기 때문**이고 이를 테스트하기도 어려워진다.
    - 모델의 명확성을 약화시키는 설계이기도 하다.
  - 그니까 사실은 가능한 **VO의 parameter로 mutable한 객체가 들어오면 안된다**.
  

### primitive는 VO가 아니다

Value Object라고 생각하고 primitive나 wrapper type을 VO 대신 사용해선 안된다.  
primitive는 Domain으로 modeling된 naming을 가지고 있지도 않고 side-effect이 없는 함수를 정의할 수도 없다.  
**이는 domain 모델을 속이는 것이다**.


## VO의 이점

VO의 특징들을 이해하고 나면 이점들은 명확하다.  

1. 생성이 쉽다.
2. 테스트가 쉽다.
3. 사용이 쉽다.
4. 최적화가 쉽다.
5. 유지관리가 쉽다.

이건 VO 대신 Entity를 사용해서 생성, 테스트, 사용, 최적화, 유지관리를 해보면 쉽게 느낄 수 있다.  


## VO 저장하기

VO도 영속성 저장소에 저장할 수 있다.  
알다시피 대부분은 부모 entity에 담겨서 저장된다.  

그러나 놀랍지만 vo가 반드시 repository의 entity로 저장되어야 할 때가 있다.
나는 이 부분이 굉장히 헷갈렸는데, **Repository의 Entity와 Domain의 Entity를 헷갈려선 안된다**.  
VO가 저장이 필요한 경우 repository의 entity로 저장된다고 하더라도 domain에서는 VO인 상태를 유지해야 한다.  

DB model은 부차적인 것이고 domain model을 위해 DB model을 설계해야 한다.  
- VO가 repository에서 entity로 저장된다고 domain도 entity로 모델링하는 것은 db의 구조를 따라가는 것이다.

persistance repository에서는 결국 Id를 가져야 하는데 VO는 Id가 없어야하는 부분이 거슬릴 수 있다.  
- 그래도 VO는 VO.
- protected Id를 갖는 abstract class를 VO가 extends 하는 방식 등으로 id를 VO class에서 숨길 수 있다.


## VO 구현하기

1. setter가 있을 수 있지만 private으로 constructor에서만 호출되어야 한다.
   - 잘못된 값이 세팅될 때 assertion을 여기서 진행할 수 있는데 이걸 guard라고 한다.
   - 난 무조건 없어야 된다고 생각했는데 **guard와 같은 명확한 구분을 위해 private setter**는 좋은 것 같다.
2. 아래서 말할 copy constructor
3. getValue() 보다는 value() 같은 유창하게(fluent) 읽을 수 있는 표현을 사용한다
   - String을 보면 charAt(), compareTo(), contaions() 등 get이 들어가는 경우는 거의 없다.


## VO 테스트하기

VO의 테스트는 domain 전문가 입장에서 **의미가 있어야 한다**.  
VO의 함수는 모든 경우에서 불변성이 보장되어야 한다.  
따라서 모든 VO 함수 테스트 전 후에 vo의 값이 변하지 않았는지를 테스트하는게 좋다.
  - 이건 새롭게 배운건데 되게 중요한 것 같다.

<div class="code-example" markdown="1" style="font-size: 0.8em">
예시
{: .label .label-yellow}  

```java
TestVo testVo = new TestVo(...);
TestVo copyTestVo = new TestVo(testVo);

assertEquals(testVo, copyTestVo);

testVo.anyMethod(..);

assertEquals(testVo, copyTestVo);
```

testVo의 `anyMethod()`를 테스트하는 코드에서 anyMethod에 대한 테스트는 기본적으로 하면서 VO가 바뀌지는 않았는지를 테스트한다.

</div>

예시와 같은 이유로 위에서 언급했듯 copy constructor를 구현한다.



### reference

- Implement Domain Driven Design (chapter6 Domain Events), Vaughn Vernon
