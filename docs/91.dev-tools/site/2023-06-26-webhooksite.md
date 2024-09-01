---
layout: post
title: Request 확인을 위해 임의로 Request를 받아주는 Website
sidebar_label: webhook site
parent: website
lang: ko
permalink: /docs/tools/website/webhook-site
grand_parent: Tools
sitemap:
  lastmod: 2024-09-01
---

요청한 request를 임의로 받아주는 server url을 발행해주는 사이트가 있다.  
이 url로 request를 보내면, request가 잘 왔는지, 어떻게 왔는지를 분석해준다.  


인프라가 갖춰지지 않은 상태로 처음 개발을 시작할 때는 문제를 확인하는게 더 어렵다.

클라이언트에 문제가 있는지  
서버에 문제가 있는지  
서버가 잘 떠 있는지  
gateway 등록 문제가 있지는 않은지    
infra의 권한 문제가 있지는 않은지  

**서버가 동작하지 않는다.** 는 이유로 확인을 시작해야할 때 초기에는 확인해야할 것들이 너무 많다.  

서버 개발자 입장에선 acceptance test나 scenario test를 위해 작성하는 test client 들이 server(local 혹은 dev)에 잘 들어오지 않는 경우도 있다.  

나는 이번에 multi-part request의 call을 잘 만들었는지 확인하고 싶은데, 이걸 확인하기 위해 찾다가 이 사이트를 발견하게 되었다.

## 사용법

- [https://webhook.site/](https://webhook.site/)에 접속한다.
- 해당 페이지에서 임의로 발급되는 webhook site url을 확인한다.
  - 예를 들면 `https://webhook.site/554e2d76-a7ee-46c3-8f9f-ce6819fbcedf`
- 해당 host로 작성한 test를 날린다.
- 분석되는 call을 페이지에서 확인한다.
