---
layout: post
title: "dynamo 내부구조 이해하기"
parent: DynamoDB
grand_parent: aws
nav_order: 1
permalink: /docs/aws/dynamo/structure
math: mathjax3
---

dynamo를 사용하기 위해서 꼭 알고있어야 하는 값들이 있다.  
WCU, RCU, partition의 max size.  
**AWS immersion day session 강의**를 들으면서 원래는 외우고 있었던 것들을 이해할 수 있는 시간이 되었다.

[왜 nosql?](/docs/33.database/2022-06-15-why-use-nosql.md)의 내용도 도움이 된다.


## partitioning

mysql에서는 sharding을 하지만 비슷한 목적으로 dynamodb는 partitioning을 한다.  
즉 data를 partition 단위로 나눈다는 것이다.  

이 partition 하나는 10GB를 저장할 수 있고, WCU는 1KB, RCU는 3KB까지 수용할 수 있다.  
따라서 저장공간이 10GB가 넘거나 WCU/RCU가 넘치는 경우 partition을 다시 나누도록 한다.


## partitioning 주의사항

그렇기 때문에 partition을 어떻게 나누느냐의 기준이되는 partition key가 굉장히 중요하다.  

10GB가 되지 않는 경우 하나의 partition은 여러 개의 partition key를 가질 수 있다.  
여러 개의 partition key를 가진 data set(partition)이 커질 경우 partition key를 기반으로 두 개의 partition으로 분리되는 방식이다.

그렇지만 **하나의 partition key의 데이터가 여러 partition에 저장될 수는 없다.**  
따라서 하나의 partition key로 저장 가능한 data는 10GB가 maximum이라는 것이다.

key 설계를 잘못하게되면 heavy user에 대한 data에서 data 에러가 날 수 있다.  
한 사람의 데이터라도 잘 분산해서 저장될 필요가 있다는 것.


## dynamodb 내부구조

dynamo의 내부 architecture에 대해서 배우면 partition에 대한 제약들을 더 잘 이해할 수 있다.  

![dynamo architecture](/images/post/aws/dynamodb/dynamo-architecture.JPG)

위 그림처럼   
1. dynamodb로 request가 들어오면 requestRouter 중에 한 곳으로 할당된다. 
2. requestRouter에서 storageNode로 routing을 한다.

여기서 중요한 점은 storage node는 3개의 node로 이루어져 있다는 것인데, leaderNode와 2개의 followerNode이다.

- db write가 발생하면 leaderNode가 업데이트되고 leaderNode가 followerNode에 data를 복제한다.
- 3개 중 2개의 node가 업데이트가 되면 node에서 ack를 보낸다.


## 내부구조 보고 제약사항 이해하기

위 개념을 이해하면 제약들을 이해하기 쉽다.

하나의 node는 1KB의 CU만을 갖는다.
- read는 3개의 node에서 이뤄질 수 있으므로 RCU는 $$ 1KB * 3 = 3KB$$.
- write는 leaderNode에서만 이뤄지므로 WCU는 1KB.

각 node는 10GB의 저장공간을 가지므로 하나의 partition의 max size는 10GB.

eventually consistancy에서 read를 할 경우
- read 요청이 $$ 1/3 $$ 확률로 각 node로 가게 된다.
- 위에서 말했듯 3개 중 2개의 node가 업데이트 되면 ack를 보내기 때문에 나머지 하나는 업데이트 되지 않았을 수 있다.
-  $$ 1/3 $$ 확률 & 1/3의 노드가 아직 업데이트 되기 이전에, read 요청이 들어온 경우 old data를 가져갈 수 있다.
-  물론 대부분의 case는 그 전에 업데이트 되는 편이다.

strong consistance는 read를 할 경우 항상 leader node로 간다.


### reference

- AWS immersion day session 강의