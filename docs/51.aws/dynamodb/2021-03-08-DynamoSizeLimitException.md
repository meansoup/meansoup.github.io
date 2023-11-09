---
layout: post
title: "DynamoSizeLimitException 이슈 정리"
parent: DynamoDB
nav_order: 1000
grand_parent: aws
permalink: /docs/aws/DynamoSizeLimitException
---

오늘은 생각지도 못한 DynamoSizeLimitException에 대해 기록한다.  
DynamoDB는 AWS에서 제공하는 NoSql DB이다.

먼저 `DynamoSizeLimitException`가 뭔지에 대해 알아볼 필요가 있다.

## DynamoSizeLimitException

Dynamo에서는 item에 대한 size 제한을 둔다.  
이 size를 넘는 item을 save 요청을 했을 때 Dynamo에서는 **DynamoSizeLimitException**를 반환한다.  

여기에 대해서는 [AWS 공식문서](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html#limits-items)를 참고하면 좋다.  
> The maximum item size in DynamoDB is 400 KB, which includes both attribute name binary length (UTF-8 length) and attribute value lengths (again binary length)  
> 그니까 총합 400KB를 넘으면 안된다 이거다

## 예상치 못한 문제 발생

이유를 설명하자면 복잡하지만 있으면 GC에 좋고, 없으면 번거로운 작업이 필요한 일이 있었다.  
자주 사용하는 dynamo table에 저장을 하기로 했고,  
size limit을 피하기 위해 400KB를 넘으면 저장하지 않도록 하는 로직을 구현했다.

그런데 exception이 발생해 alert가 왔다.
item을 확인해보니 고작 210KB 정도??

Document를 읽어도 원인을 알 수 없었고, 한참을 구글링 했다.

## LSI에서의 size limit

DynamoDB에서는 **Local Secondary Indexes(LSI)**를 제공하는데, LSI가 있으면 size limit 계산이 달라진다.

LSI는 item을 replica로 사용해서 size를 배로 먹는다는 것.  
따라서 LSI가 n개면 n + 1배의 size를 먹는다고 볼 수 있고, item size limit은 그만큼 줄어드는 것이다.  
우리는 LSI를 하나 사용하고 있었고, 210KB 짜리가 들어와서 LSI 덕에 400KB가 넘어 이슈가 발생한 것.

이런 내용들이 공식 document에 없다는건 좀 아쉽고,  
쉽게 발생하지 않는 이슈여서 자료도 잘 없는 것 같다.


[aws tech 팀에 contact한 사람의 답변](https://stackoverflow.com/questions/33768971/how-to-calculate-dynamodb-item-size-getting-validationerror-400kb-boto)을 통해 알 수 있었다.