---
layout: post
title: "DynamoDB Streams는 뭐고 언제 사용하는게 좋을까?"
sidebar_label: "Streams"
parent: DynamoDB
grand_parent: aws
nav_order: 4
lang: ko
permalink: /docs/aws/dynamo/streams
sitemap:
  lastmod: 2024-06-24
---

서비스가 성숙기에 접어들게 되면, 회사에선 서비스 비용을 줄이기 시작한다.  
우리는 성숙기에 접어든지 한참 된 서비스이기 때문에 매년 비용에 대한 압박을 받게 된다.

'이런 상황에서 DynamoDB의 Streams가 아무리 좋다고 한들, 쓸 수 있을까?' 라는 생각이 항상 들었다.  
그런데 아주 적합한 케이스를 찾았다.

우선 DynamoDB Streams가 뭔지 알아보자.


## DynamoDB Streams

DynamoDB의 변경 사항을 캡처해서 전달하는 DynamoDB의 서비스이다.  

Streams은 다음과 같은 특징을 갖고 있다.
- DynamoDB의 변경 사항 정보를 시간순으로 가지고 있는다.
- Streams Record 통해 어떤 데이터가 변경되었는지 확인할 수 있다.
- Streams Record는 24시간 동안 데이터를 저장한다.
- AWS의 다른 서비스와 쉽게 결합하여 사용할 수 있다.
- 활성화/비활성화가 쉬우며 DynamoDB 테이블에 영향을 미치지 않는다.
- 전달할 정보를 지정할 수 있다.
  - KEYS_ONLY, NEW_IMAGE, OLD_IMAGE, NEW_AND_OLD_IMAGE 

모든 변경 사항을 Streams로 받을 수 있기 때문에 Streams의 활용 방안은 다양하다.  
**데이터 분석이나, 비동기 작업, 데이터 복제, 백업, 이벤트 전달 등의 목적으로도 사용할 수 있다.**  

그러나 앞서 말했듯 **문제는 비용**이다.  
모든 변경 사항이 Streams로 전달된다는 것은, **모든 변경 사항에 대해 추가 비용이 발생한다**는 것이다.  


## 언제 사용하는게 좋을까?

비용에 대한 압박이 없다면 앞서 언급한 데이터 분석, 비동기 작업, 데이터 복제 등의 모든 케이스에서 Streams를 편리하게 사용할 수 있다.  
그러나 사용량이 증가함에 따라 가파르게 증가하는 클라우드 비용을 고려했을 때, 단순히 현재 비용이 적다는 이유만으로 Streams를 많이 사용하는 것은 적절하지 않을 수 있다.  

이번에 새로운 시스템을 설계하면서 Streams가 아주 적절한 케이스를 발견했다.   
우리는 확장성을 고려하여 user table을 DynamoDB로 설계를 하였고 user에 대한 통계를 고려하고 있었다.  
통계를 쉽게 뽑기 위해선 다양한 query가 가능한 DB가 필요했다.

user DB와 같은 경우 데이터는 무한정 증가할 수 없다. (전세계 인구가 user가 된다고 하더라도 70억에 불과하다.)  
동시에 user DB의 경우 데이터 변화가 잦지 않다.  
따라서 쌓이는 데이터는 많을 수 있으나, 서비스를 지속하면서 발생하는 Streams 자체는 많지 않은 케이스이다.  


인스타그램으로 예시를 들어보자.  
인스타그램은 약 15억 사용자를 보유하고 있으며 하루에 약 1억 건의 포스팅이 생긴다고 한다.  

포스팅에 대한 데이터를 DynamoDB에 저장하고 Streams를 사용한다면 매일 적어도 1억 건 이상의 Streams Record가 발생하게 될 것이며 이는 비용상 이슈가 될 수 있다. 

그러나 15억 사용자를 고려하면 **사용자 데이터는 대부분 가입 시나리오에서 업데이트 되며, 그 이후로 변경사항이 잦지 않다**.  
인스타그램을 서비스하는 수 년 동안 15억 건의 Streams Record가 발생한다고 한다면, 이는 아주 저렴한 비용임을 확인할 수 있다.


## 비용에 대한 계산

일반적으로 많이 사용하는 Streams와 Lambda를 통해 비용을 산정해본다.  
비용은 현재 문서를 작성하는 24년 6월 24일 기준으로 <u>aws 비용문서</u>[^1] 기준으로 정리한다.  
한국(서울), 미국(오레곤), 유럽(아일랜드)의 비용이 동일했다.

### Streams

- ~~매달 첫 DynamoDB Streams 읽기 요청 유닛 250만 건은 무료~~
- ~~이후 DynamoDB Streams 읽기 요청 유닛 10만 건당 0.0217 USD~~
- DynamoDB Streams에서 데이터 읽기 작업에 대한 요금을 청구하나 **<u>lambda에서 호출하는 경우 무료</u>**[^2]

Streams의 경우 Lambda와 함께 사용할 경우 읽기 요청에 대한 비용이 발생하지 않는다.  

### Lambda

lambda는 계산이 좀 복잡하다.  
CPU 초당 요금과, 건당 요금, 메모리 요금을 별도로 과금한다.  

CPU (x86) 요금
- 처음 60억GB-초/월  GB-초당 0.0000166667 USD 
- 다음 90억GB-초/월  GB-초당 0.000015 USD
- 다음 150억GB-초/월 GB-초당 0.0000133334 USD

호출 건당 요금
- 요청 1백만 건당 0.20 USD

메모리(MB) 1밀리초당 요금
- 128     0.0000000021 USD
- 512     0.0000000083 USD
- 1,024   0.0000000167 USD
- 1,536   0.0000000250 USD
- 2,048   0.0000000333 USD


### 비용 예시 및 계산

인스타그램의 user db를 DynamoDB Streams와 Lambda를 사용하여 통계 DB로 연동하는 설계에 대한 비용을 계산해본다.
- AWS RDS가 필요하겠지만 이 비용은 여기에 포함하지 않는다.

- 시나리오: **15억 건의 유저 데이터가 DynamoDB Streams를 통해 Lambda로 요청된다.**
- 가정
  - 128MB의 가장 저렴한 메모리를 사용하며, lambda를 1초간 사용한다고 가정한다.

- 총 비용: $28,450
  - Streams: $0
  - CPU 초당 요금: $25,000 (0.0000166667 * 1,500,000,000)
  - CPU 건당 요금: $300 (0.20 * 1,500)
  - 메모리 요금: $3,150 (0.0000000021 * 1,500,000,000 * 1,000)

물론 실제 서비스에서는 유저 변경에 따른 Streams Record 발행이 더 발생할 수 있다. 
그러나 서비스를 수 년간 운영하며 Streams 도입 비용 총 $28,000를 지불한다면 서비스 규모 대비 매우 작은 비용이라고 예상된다.


결과적으로 우리 팀에서는 현재 user DB의 통계 작업을 위해 Streams 도입 중이다.


---

[^1]: [Streams 비용문서](https://aws.amazon.com/ko/dynamodb/pricing/provisioned/)와 [Lambda 비용문서](https://aws.amazon.com/ko/lambda/pricing/)를 참고한다.
[^2]: [Streams 사용량](https://docs.aws.amazon.com/ko_kr/amazondynamodb/latest/developerguide/CostOptimization_StreamsUsage.html) 문서에서 Lambda와 함께 용할 때의 비용을 확인할 수 있다.  