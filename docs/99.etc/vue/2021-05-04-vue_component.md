---
layout: post
title: "vue 3.0 global component"
sidebar_label: "vue 3.0 global component"
tag:
- vue
parent: vue
permalink: /docs/vue/component
grand_parent: Etc
sitemap:
  lastmod: 2021-05-04
---

vue.js 3.x에서 global component를 사용하기.  

guide에 나온 내용은 vue.js 2.x 내용이어서 3.x에서는 조금 다른 부분이 있었다.  

java의 객체를 만들어서 클래스들에서 사용하는 것처럼, vue에서도 `.vue` 파일을 생성하고 다른 곳에서 활용하고 싶었다.  

vue에서는 이런걸 **component**라고 하고 등록하고 사용하고 있었다.

component에는 두 가지 종류가 있는데, **local**과 **global**이 있다.  

**local component**:  
쓸 때마다 각 vue에서 등록해서 사용하는 지역변수 같은 느낌

**global component**:  
한 번 등록하고 각 vue에서 사용하는 전역변수 같은 느낌

몰라서 그렇지 한 번만 예제를 확인하면 적용하기는 쉽다.

## 예제

### 객체처럼 사용할 `Child.vue`

```javascript
<template>
  <div>
    ...
  </div>
</template>
 
<script>
export default {
  name: 'Child'
}
</script>
 
<style>
    ...
</style>
```

### local component로 사용하는 vue 구현

local component를 사용할 vue 파일에서 component를 import하고 사용한다.

```javascript
<template>
  <div>
    <Child />
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

<style>
    ...
</style>
```

### global component로 사용하는 app 구현

global component를 사용할 프로젝트의 main.js 파일에서 component를 import한다.
그러면 위 local component에서 사용하는 것처럼 각 vue에서 component를 쓸 수 있다.  

```javascript
import { createApp } from 'vue'
import App from './App.vue'
import child from './components/Child'

const app = createApp(App)
app.component('Child', child)
app.mount('#app')
```

사용하는 쪽 vue에선 script에서 import 없이 바로 template에서 사용할 수 있다.

```javascript
    <Child />
```

## 참고

[vue guide](https://kr.vuejs.org/v2/guide/components.html#%EC%A7%80%EC%97%AD-%EB%93%B1%EB%A1%9D)
- 현재는 3.x guide는 없음