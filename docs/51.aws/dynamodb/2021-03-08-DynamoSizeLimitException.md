---
layout: post
title: "예상치 못한 DynamoSizeLimitException 이슈 정리"
sidebar_label: "DynamoSizeLimitException"
parent: DynamoDB
nav_order: 1000
grand_parent: aws
permalink: /docs/aws/dynamo/DynamoSizeLimitException
sitemap:
  lastmod: 2021-03-08
---

최근 DynamoSizeLimitException 에러를 겪을 일이 있었다.  
생각지도 못하게 DynamoSizeLimitException를 겪게 되어 원인을 파악하였고, AWS 공식 document에 나오지 않는 내용을 기록한다.

## What is DynamoSizeLimitException

DynamoDB에서는 item에 대한 size 제한을 둔다.  
정해진 size를 넘는 item을 save 요청을 했을 때 Dynamo에서는 **DynamoSizeLimitException**를 반환한다.

[AWS dynamoDB Limits](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ServiceQuotas.html#limits-items)를 확인하면 아래와 같은 문구를 확인할 수 있다.

```
The maximum item size in DynamoDB is 400 KB, which includes both attribute name binary length (UTF-8 length) and attribute value lengths (again binary length)
```

결국 하나의 item이 400KB를 넘을 수 없다는 것.


## DynamoSizeLimitException occur under 400KB

그렇지만 400KB를 넘지 않는 케이스에서 DynamoSizeLimitException가 발생했다.  
Dynamo의 size limit에 대해 우리는 이미 알고 있었고, 400KB가 넘는 케이스는 별도로 처리하는 로직을 구현했다.

그럼에도 DynamoSizeLimitException가 발생했다.

item을 확인해보니 item의 크기는 고작 210KB 정도.  
Document 에서도 원인을 찾을 수 없었다.

## Why DynamoSizeLimitException occur?

원인은 Local Secondary Indexes(LSI)에서 찾을 수 있었다.  
DynamoDB에 **LSI가 있으면 size limit 계산이 달라진다.**

LSI는 item을 replica로 사용해서 size를 배로 사용한다.  
따라서 **LSI가 n개라면 최대 n + 1 배의 size를 사용할 수 있다**는 것이고, item size limit은 그만큼 줄어들게되는 것이다.  
우리는 LSI가 하나 있었고, 210KB의 item이 LSI로 인해 400KB 이상의 size를 가지며 이슈가 발생한 것이다.

LSI를 사용해서는 안되는 이유가 하나 더 늘었다.
