---
layout: post
title: "single table 적용 후기"
parent: DynamoDB
grand_parent: aws
nav_order: 3
permalink: /docs/aws/dynamo/single-table-result
---

우리 팀은 dynamodb를 많이 쓰고 있다.  
RDB를 쓰다가 dynamodb로 넘어가서 시행착오가 좀 있었다. 

dynamodb를 처음 적용한 한 모듈은 RDB처럼 table을 나눠서 사용하고 있었다.  
성능 개선을 위한 story를 진행하면서 single table에 대한 얘기가 나왔고 migration을 진행했다.

사실 한지는 좀 됐는데 single table에 대해 다시 생각해볼 시간이 있어 정리해본다.

## single table

[single table 이란?](https://meansoup.github.io/docs/aws/dynamo/single-table)

## table design 변경

이후에 개발하는 모듈에선 single table을 완전히 적용하기도 했지만  
사실 이번 모듈의 migration은 single table까지는 아니다.  

table을 합치는 방식으로 10개의 table을 4개의 table로 합쳤다.  


## 비용 개선

provision WCU가 절반으로 줄었다.  
- 넉넉하게 세팅하던 값이 줄었기 때문이 아닌가 싶다.
- 그리고 scaling을 고려해서 여러 table로 나뉘어 있던 데이터들이 하나의 row에 합쳐지는 것들이 있어서 WCU 개선이 컸던 것으로 생각된다.

provision RCU가 50% 정도 늘었다.
- 이건 원인을 잘 모르겠다. 당시 call 수가 늘었는지.. 지금은 정확하게 기억나지는 않는다.
- 개념적으로는 줄어드는게 맞다만.


## 성능 개선

이 모듈은 요구사항에 맞게 data를 동기화 해주는게 주 목적이었다.  
db query가 줄어드니 성능은 크게 개선되었다.  
주요 api들의 성능이 40~80% 까지 개선되었다.


## 회고

지금 생각하면 table 수를 더 줄일 수 있었을텐데 싶기도 하고.  
이때는 single query load multiple type entity에 대한 생각이 잘 없었어서 그런 방향으로 성능 개선이 다시 가능할 것 같다.  
물론 바빠서 못함.

