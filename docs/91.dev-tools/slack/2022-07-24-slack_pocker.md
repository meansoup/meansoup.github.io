---
layout: post
title: slack에서 스마트하게 추정하기
sidebar_label: slack에서 스마트하게 추정하기
parent: 슬랙
grand_parent: Tools
permalink: /docs/dev-tools/slack/pocker-planner
sitemap:
  lastmod: 2022-07-24
---

원격 근무가 많아지면서 회의하는 방식에 대한 변화도 당연히 생기기 마련이다.  
우리는 agile하게 일을 진행하는데, sprint를 할 때는 story에 대한 추정을 한다.

추정 방식은 핸드폰의scrum pocker 앱을 통해 해왔었는데,  
원격 근무를 하게 되면 회의할 때 '하나 둘 셋' 하고 자기가 선택한 포커 숫자를 화면에 공개하고 있었다. 

최근 회사 보안 문제로 카메라를 켜지 못하는 상황이 되어 웃긴 상황이 벌어졌다.  
'하나 둘 셋' 하고 슬랙 쓰레드에 각자 추정하는 값을 입력하는 방식...

최첨단을 달리고자 하는 개발자들이 하기에 조금 아쉽지 않나 싶다.

더 스마트하게 추정을 할 수 없을까 싶어 찾다가 발견한 슬랙 앱.

## demo

![pocker](/images/post/dev-tools/slack/slack_pocker_planner.gif)

공식 사이트에서 제공하는 demo를 그대로 가져왔다.  
직접 사용해도 동일하게 편하게 사용할 수 있다.

## slack pocker planner

[https://deniz.co/slack-poker-planner/](https://deniz.co/slack-poker-planner/)

옛날 방식의 앱이긴 하나 굉장히 효율적이었다.  
팀 내에서도 좋은 반응을 받았다.

## 사용법

1. 위 사이트에서 add to slack
2. add 완료 (권한이 없다면 권한 요청)
3. install slack app
4. slack 채널에 **pocker planner** 추가
5. `/pp {title}`으로 사용



### reference

- https://deniz.co/slack-poker-planner