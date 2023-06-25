---
layout: post
title: client call 확인을 위한 webhook site
parent: 사이트
permalink: /docs/dev-tools/site/webhook-site
grand_parent: 개발툴
---

굉장히 좋은 사이트를 알아왔다.  
처음 개발을 할 때, 클라이언트에 문제가 있는지 서버에 문제가 있는지.  
서버가 잘 떠 있는지 GW 나 권한 문제가 있지는 않은지 애매하게 확인할 부분들이 있다.  

서버 개발자 입장에선 acceptance test나 scenario test를 위해 작성하는 test client 들이 server(local 혹은 dev)에 잘 들어오지 않는 경우도 있다.  
특히 multi-part의 경우 call을 잘 만들었나 싶은데 이걸 확인하기 아주 좋은 사이트.

## 사용법

- `https://webhook.site/`에 접속한다.
- 해당 페이지에서 임의로 발급되는 webhook site url을 확인한다.
  - 예를 들면 `https://webhook.site/554e2d76-a7ee-46c3-8f9f-ce6819fbcedf`
- 해당 host로 작성한 test를 날린다.
- 분석되는 call을 페이지에서 확인한다.

## reference

- [https://webhook.site/](https://webhook.site/) 