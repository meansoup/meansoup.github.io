---
layout: post
title: "vue 3.0 component props 전달하기"
sidebar_label: "vue 3.0 component props 전달하기"
tag:
- vue
parent: vue
permalink: /docs/vue/passing-props
grand_parent: Etc
sitemap:
  lastmod: 2021-05-05
---

[component 적용](/docs/vue/component)을 한 뒤에 component의 props를 전달하는 방법이다.  

component에는 `data`가 있고 `prop`이 있는데, `prop`은 component를 생성하는 쪽에서 각기 다른 값을 넣어줄 수 있는 것이다. 
- 내가 이해하기엔 java에서 생성자에 넣어주는 값 정도?

component를 사용할 수 있게 적용하고 난 뒤 할 작업은 prop을 통해 각 component들을 구성하고 view를 꾸며주는 일이다.
이 또한 예제를 보면 간단한데, 문제를 찾는데 시간이 걸렸다.

## 예제
예제 코드는 [component 적용](/docs/vue/component)의 내용을 참고하자.  
component 구성이 완료되었다고 생각하고 코드를 일부만 작성하겠다.  

### 객체처럼 사용할 `Child.vue`

```javascript
<template>
  <div>
    <p>{{ msg }}</p> // prop 사용
    <img v-bind:src="require(`@/assets/${image}`)" alt="test image"> // prop 사용 - image, require가 필수이다.
  </div>
</template>
 
<script>
export default {
  name: 'Child',
  props: {
      msg: String,
      image: String
  }
}
</script>
```

### component를 사용하는 vue

component에서는 prop들을 넣어준다

```javascript
<template>
  <div>
    <Child msg="child test msg" image="1.png"/> // 여기서 1.png는 src/assets/1.png 에 있다.
  </div>
</template>

<script>
import child from './Child' // 상대주소로 기입

export default {
  name: 'HelloWorld',
  components: {
    'Child': child  // 앞의 naming이 사용할 name, 뒤에는 import한 name
  },

}
</script>
```

## 참고

[vue guide, props 전달하기](https://kr.vuejs.org/v2/guide/components-props.html#%EC%A0%95%EC%A0%81-amp-%EB%8F%99%EC%A0%81-prop-%EC%A0%84%EB%8B%AC%ED%95%98%EA%B8%B0)  
[stackoverflow, image 보이기](https://stackoverflow.com/questions/56624817/passing-and-binding-img-src-from-props-in-vue-js)
