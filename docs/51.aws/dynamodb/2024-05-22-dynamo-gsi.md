---
layout: post
title: "DynamoDB Secondary Index: 주의 사항 및 비용 이슈"
sidebar_label: "Secondary Index"
parent: DynamoDB
grand_parent: aws
nav_order: 1
lang: ko
permalink: /docs/aws/dynamo/si
sitemap:
  lastmod: 2024-05-22
---

DynamoDB의 효율적인 query를 위해서 Secondary Index의 활용이 필요하다.  

DynamoDB에서는 Secondary Index를 사용하여 기본키 외에 대체키를 통해 테이블에서 데이터를 쿼리할 수 있다.  
Secondary Index는 아래 내용들을 포함한다.
- 대체키 속성, 기본키 속성, 기본 테이블에 포함된 다른 속성의 선택적 하위 세트(프로젝션된 속성)

DynamoDB는 자동으로 테이블의 기본키를 기반으로 인덱스를 생성하고 테이블이 변경될 때마다 자동으로 모든 인덱스를 업데이트한다.

DynamoDB는 GSI, LSI 두 종류의 Secondary Index를 지원한다.  
LSI는 현재 AWS에서도 사용을 지양하고 있기 때문에 GSI 위주로 개념과 사용하면서 겪었던 주의사항들, LSI를 사용하지 않는 이유를 정리한다.


## GSI (Global Secondary Index)
**GSI**는 이 인덱스에 대한 쿼리가 모든 파티션을 아우르며, 특정 파티션에 국한되지 않고 테이블 전체를 대상으로 쿼리를 수행할 수 있다는 점 때문에 Global 이라는 표현을 사용한다.

- 파티션 키와 필요하다면 정렬 키를 가질 수 있으며 이는 원래 테이블의 파티션 키와 정렬 키와는 다른 값이다.
- 키 값이 고유할 필요는 없다.
- 테이블이 생성될 때 생성되거나 기존 테이블에 추가할 수 있다.
- 테이블 생성 이후 삭제될 수 있다.
- 최종 일관성만 지원한다.
- 읽기 및 쓰기 작업에 대한 처리량(RCU, WCU)을 별도로 설정한다.
- 쿼리는 인덱스에 프로젝션된 속성만 반환한다.
- GSI는 최대 20개까지 생성할 수 있다.

### GSI의 파티션

GSI에서는 **키 값이 고유할 필요는 없다.** 는 이유로, 동일한 key에 여러 데이터를 쌓을 수 있으며 이를 통해 GSI는 메인 테이블에서 할 수 없는 데이터 구조를 가져갈 수 있다.

예를 들면, main table에 **name, age, country, passportNo**이 있다고 하자.  
고유한 값을 위해 primary key를 passportNo로 설정할 수 있을 것이다.

그런데 국가별로 query가 필요한 Usecase가 있다면, country를 GSI의 기본키로 선택할 수 있다.  
이렇게 되면 country라는 동일한 key에 대해 고유하지 않은 여러 데이터를 쌓고 가져올 수 있는 구조를 만들 수 있다.

이런 구조가 안전할까?  
GSI는 내부에서 key를 가지고 샤딩하면서 partition을 나눠주기 때문에 안전하다.  
동일한 key로 이론상으로는 제한 없이 데이터를 넣을 수 있는 것이다.    
사실 이건 main table도 동일하나, main table에서는 동일한 primary key에 대해 여러 데이터를 가질 수 없다.


### GSI의 CU (Capacity Unit)

GSI는 main table과 CU가 분리되어 있다.  
GSI에서 읽을 때, 쓸 때 CU를 각각 소모한다는 것인데, main table 동작과도 연관이 있다.

GSI의 RCU의 경우 throttling이 나더라도 main table에 영향을 주지 않는다.  
GSI의 WCU의 경우 throttling이 나는 경우 main table의 write도 실패하게 된다.  
DynamoDB는 내부적으로 <u>main table과 변경되는 데이터와 관련된 GSI를 모두 write</u>[^1] 하기 때문에 GSI에 write가 실패하는 경우 main table도 실패하게 된다.

정리하자면 DynamoDB의 write는 GSI의 write로 이어진다.  
DynamoDB의 update는 경우에 따라 GSI의 delete & write로 이어질 수 있다.

위의 예시를 다시 보면, country가 KR에서 US로 바뀌는 경우 GSI의 KR 키에 프로젝션된 데이터가 delete 되고, US 키에 프로젝션된 데이터가 write 된다.  
이 케이스에선 DynamoDB write 하나에 2개의 CU가 소모된다.

DynamoDB의 요금에서 상당수를 차지하는 것이 CU이기 때문에 write 한번에 3개의 CU(main table write 1번 + GSI write 2번)을 사용하는 데이터 구조는 비용 측면에서 좋은 방향은 아니다.  
DynamoDB table에 여러 개의 GSI가 적용될 수 있기 때문에, DynamoDB의 GSI를 설계할 때 비용 측면도 같이 고려될 필요가 있다.


## LSI (Local Secondary Index)

**LSI**는 인덱스가 특정 파티션 키를 가진 항목과 같은 테이블 파티션에 위치해 있기 때문에 Local 이라고 표현한다.    
즉, 같은 파티션 키 값을 가진 애들에 대한 쿼리로 지정된 파티션 키 값의 데이터만 쿼리할 수 있다.

- Local Secondary Index의 파티션 키는 테이블의 파티션 키와 같다.
- 테이블이 생성될 때만 생성될 수 있다.
- 테이블 생성 이후 삭제될 수 없다.
- 최종 일관성과 강력한 일관성을 지원한다.
- 별도로 프로비저닝된 처리량이 없이 테이블의 읽기 및 쓰기 용량을 사용한다.
- 쿼리는 인덱스에 프로젝션되지 않은 속성을 반환할 수 있다.
- 테이블에서 특정 파티션 키를 갖는 모든 항목과 이에 상응하는 Local Secondary Index 항목이 같은 파티션에 저장된다. 이런 항목 모음의 총 크기는 10GB를 초과할 수 없다.
- LSI는 최대 5개까지 생성할 수 있다.


LSI는 명확한 단점들이 있고, GSI 대비 장점이 뚜렷하지 않아 현재는 권장되지 않는다.
1. LSI의 경우 추가/삭제할 수 없다.
2. main table의 자원을 같이 사용한다.
3. partition key 별 10GB의 크기 제한이 존재한다.

대신 GSI를 사용하는 것이 좋다.

---

[^1]: [main table과 GSI table의 상관관계](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GSI.html#GSI.ThroughputConsiderations)와 [GSI CU 부족 시 main table의 영향도](https://repost.aws/knowledge-center/dynamodb-gsi-throttling-table)를 참고할 수 있다. 