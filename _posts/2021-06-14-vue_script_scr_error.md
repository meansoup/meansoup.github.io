---
layout: post
title: "[vue] Uncaught SyntaxError: Unexpected token '<' 에러"
tag:
- vue
- error
---

vue에서 `Uncaught SyntaxError: Unexpected token '<'`에러를 받을 때,  
srcipt의 src를 잘못 명시한 경우이다.

index.html의 header에 script를 넣고 싶은 경우에는,  
`public` path 밑에 `.js`, `css` 파일들을 두어야 한다.
- favicon.ico가 있는 그 위치