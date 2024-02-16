---
layout: post
title: "config.js"
sidebar_label: "config.js"
tag:
- vue
parent: vue
permalink: /docs/vue/config
grand_parent: Etc
sitemap:
  lastmod: 2021-03-30
---

vue로 github.io에 github page를 로딩하기 위해 build 했다.  

1. `vue create {project}` 로 project를 생성하고,
2. `npm run build` 로 build 한 뒤,
3. github에 push

하면 되야하는데 되지 않는다.

github에서는 `/docs`에 있는 정적 페이지들을 호출할 수 있도록 제공하고 있고 vue의 build 산출물이 docs로 쓰여지게 해야 한다. 
- default는 `/dist` 인데 이걸 바꿔주는 것을 config.js에서 할 수 있다.

```javascript
module.exports = {
    outputDir: './docs',
    publicPath: '/votes/'
}
```

이렇게 하면 `npm run build` 시 `/docs`로 산출물이 생성되고, publicPath는 `/votes`로 시작하게 된다.  

