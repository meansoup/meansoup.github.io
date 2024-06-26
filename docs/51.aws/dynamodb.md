---
layout: post
title: DynamoDB
sidebar_label: DynamoDB
nav_order: 1
parent: aws
has_children: true
permalink: /docs/aws/dynamo
sitemap:
  lastmod: 2024-05-03
---

**DynamoDB**는 완전 관리형 NoSQL DB 서비스으로 NoSQL의 특징을 갖는다.  
리전 기반 서비스로 AZ에 문제가 생기더라도 다른쪽에서 정상적으로 동작한다.  
완전 관리형 서비스로 사용자가 관리할 것이 거의 없다.  
- EC2에 os/db 설치 이후 db 서버로 쓸 수도 있지만 이런 서비스를 이용하면 초기세팅/소프트웨어 패치/운영 등을 신경쓰지 않아도 되서 더 편리함.  

데이터 볼륨이 증가하고 애플리케이션 성능 요구가 증가하면 DynamoDB는 자동 분할로 처리량을 충족하고 규모에 관계없이 낮은 지연 시간(보통 10밀리초 미만)을 유지한다.  
IAM의 계정 권한 관리로 세분화된 접근 제어가 가능하다.  
문서의 저장, 쿼리 및 업데이트를 지원하여 Json 문서를 테이블에 바로 저장할 수 있고 관련한 작업을 효율적으로 진행할 수 있다.

## database option
AWS에는 DynamoDB 외에도 다양한 DB 서비스를 지원하고 있다.  

**RDS**:  
Aurora, PostgreSQL, MySQL, MariaDB, Oracle 등 다양한 관계형 데이터베이스 서비스를 제공한다.  
RDB를 간편하게 설정하고 크기 조정이 가능하다.  
DB 관리를 AWS에서 해줘서 서비스에 집중할 수 있다.  
- ex) 소프트웨어 패치, 데이터베이스 백업

**Aurora**:  
MySQL, PostgreSQL 호환 RDB로 MySQL보다 최대 5배 빠르며 1/10 수준 비용으로 서비스를 제공함.  
MySQL, PostgreSQL 보다 더 높은 처리량을 가지며 쉽게 확장/축소할 수 있음.
Aurora Serverless 서비스도 있음.

**Redshift**:  
완전 관리형 데이터 웨어하우스. ([나무위키 웨어하우스](https://namu.wiki/w/%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%9B%A8%EC%96%B4%ED%95%98%EC%9A%B0%EC%8A%A4) 참고. 의사 결정을 위한 데이터 사용)  
기존 솔루션 비용의 1/10 미만으로 페타바이트 규모로 확장할 수 있음.  
다양한 개방형 형식(csv, json, ...) 지원.  

**Neptune**:  
완전관리형 그래프 데이터베이스.  

**ElastiCache**:  
memCache나 Redis를 관리하는 관리형 상태로 지원하는 서비스.  
in memory data store, cache를 쉽게 배포/운영할 수 있음.  
당연히 메모리를 사용하니까 DB보다 빠른 검색을 지원하고, 성능 향상을 볼 수 있다.  
Redis나 memcache를 활용하는 것으로 얘네의 장점을 보다 쉽게 적용할 수 있다.

## DynamoDB 구성
DynamoDB는 테이블, 항목, 속성으로 구성되고 각 항목들은 키 값을 갖는다.
- 각각 엑셀의 시트, 행, 열로 생각할 수 있다.  

스키마가 고정되어 있지 않기 때문에 항목에 속성의 추가가 자유롭다.  

DynamoDB는 테이블의 항목을 파티션 키에 따라 여러 항목으로 나누고 파티션은 스토리지로 백업되고 리전 내의 복수의 AZ에 자동으로 복제된다.  
- 파티션 단위로 다른 위치에 저장될 수 있다는 것.  

데이터에 접근할 때는 파티션 키를 통해 접근하기 때문에 파티션 키는 고유한 값이어야 한다.  
정렬 키는 선택적으로 사용되며 동일한 파티션 키를 사용하고 싶다면 정렬 키를 사용하여 `파티션 키 + 정렬 키`의 값이 고유하도록 구성할 수 있다.  
- ex) 파티션 키는 sessionId, 정렬 키는 Time으로 동일한 세션에 대해 같은 파티션을 사용하도록 하고 시간에 따라 값을 저장할 수 있다.  

## 일관성
DynamoDB는 일관성 수준을 지원한다.  
여기서 일관성은 찰나의 시간에 쓰여진 데이터를 받아오는지에 대한 여부이다.  
**최종적 일관성** - 읽기 작업이 쓰기 작업 이후에 수행되는 경우 약간 오래된 데이터를 반환할 수 있음.  
**강력한 일관성** - 가장 최신 데이터를 반환.  
**트랜잭션** - ACID를 요구. 읽고 쓰기가 끝나는 것이 하나의 트랜잭션임을 보장하는 것. (계좌이체)  

## 처리량
한 번에 들어온 요청에 대해 어느 정도까지 처리할 수 있는지 capacity를 설정할 수 있다.  
처리량은 파티션 간에 균등하게 나뉜다. (파티션당 처리량 = capacity / 파티션 수)  
**RCU** - 최대 4KB 규모의 객체에 강력한 일관된 읽기를 수행할 수 있는 건수.  
**WCU** - 1KB 쓰기를 수행할 수 있는 초당 건수.

## 글로벌 테이블
하나 이상의 DynamoDB 테이블의 모음으로 단일 AWS 계정이 소유한 복제 테이블이다.  
글로벌 테이블에서는 리전당 하나의 복제 테이블만 사용되고 동일한 테이블 이름과 기본 키 스키마를 갖는다.
글로벌 테이블을 사용하면 복제 솔루션을 구축할 필요 없이 완전 관리형 솔루션을 제공한다.

DynamoDB에서 해당 리전에 동일한 테이블을 생성하기 위해 모든 작업을 수행하고 진행 중인 데이터 변경을 모두에게 전파한다.  
이런 복제에 스트림이 사용된다.  
쓰기 일관성에서 동시 업데이트가 발생하는 경우에는 가장 마지막에 설정된 값으로 기록한다.  
읽기 일관성에서 최종적 일관성을 지원한다.  

## 백업 및 복원
백업, 복원, 특정 시점으로의 복구를 쉽게 할 수 있도록 지원한다.

## API
**제어 작업**: DynamoDB 테이블을 생성하고 관리.  
**데이터 작업**: 테이블 데이터에 CRUD 작업을 수행.

## 객체 지속성 모델
DynamoDB에 클라이언트 측 객체를 유지할 수 있다.  
- 테이블에 대한 객체 매핑(클래스 인스턴스)를 지원한다.
객체 지속성 프로그래밍 인터페이스로 이를 지원하는데 이를 통해 CRUD 작업과 쿼리를 실행할 수 있다.  

## Function
테이블에서 PutItem, GetItem, UpdateItem, DeleteItem으로 항목과 관련한 작업을 수행할 수 있고,  
Query, Scan 으로 값을 가져올 수 있다.
- Query, Scan 작업의 경우 1MB의 데이터라는 기본 페이지 매김 제한으로 반환되는 데이터 양이 제한된다.
- Query, Scan 작업의 경우 Limit 파라미터를 통해 반환되는 최대 항목 수를 지정할 수 있다.

Batch로 데이터를 검색하거나 쓸 때 단일 요청으로 더 높은 처리와 효율적인 시간을 얻어낼 수 있다.  
실패시 실패한 테이블과 항목을 재시도한다.  
**BatchGetItem** - 여러 테이블에서 최대 100개의 항목으로 이루어진 데이터를 최대 16MB까지 읽음.  
**BatchWriteItem** - 여러 테이블에서 최대 25번의 put 또는 delete 요청을 통해 최대 16MB까지 씀.  

[DynamoDB javaSDK method Docs](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/dynamodbv2/document/DynamoDB.html), [DynamoDB API reference](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Operations_Amazon_DynamoDB.html) 참고.

## 그외 참고 사항
예약어 자리 표시자 - 표현식에서 속성 이름을 위한 자리 표시자. ([AWS Docs](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.ExpressionAttributeNames.html) 참고)  

리터럴 값 자리 표시자 - 표현식에서 속성 값을 위한 자리 표시자. ([AWS Docs](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.ExpressionAttributeValues.html) 참고)  
조건부 쓰기 수행 - ConditionExpression을 만족하면 쓰기를 수행. ([AWS Docs](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.SpecifyingConditions.html) 참고)  
처리량 예외 처리 - 처리량이 초과하면 `provisionedThroughputExceededException`으로 알림을 전송하도록 CloudWatch 경보 설정. ([AWS Docs](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/metrics-dimensions.html) 참고)  

## 효율성 확보
데이터를 고려하여 파티션 키가 분산될 수 있도록 구현한다.  
- 파티션 키에 따라 파티션이 나뉘며 경우에 따라 어떤 파티션엔 데이터가 적고 어떤 파티션엔 극도로 많아 작업 처리가 느려질 수 있다. 균일하게 파티션을 분배하여 처리를 분산시키는 것이 처리량을 극대화.

핫 데이터(자주 사용)와 콜드 데이터(자주 사용하지 않음)을 분리한다.  
- 자주 사용되는 데이터는 처리량이 더 높은 테이블에 별도로 저장한다거나 오래된 데이터를 다른 스토리지로 이동하는 등의 방식. 

다수의 속성을 갖는 테이블 대신 일대다 테이블을 사용한다.
- 최소한의 정보가 필요한 경우에도 쓸데없이 대량의 데이터를 가져오게 되는 문제를 해결.
- 항목 크기가 DynamoDB의 최대 항목 크기를 초과하는 문제를 막을 수 있음.

자주 액세스하는 속성을 별도 테이블에 저장한다.  
- 큰 항목에 자주 액세스 하지만 큰 속성을 다 사용하지 않는다면 자주 사용되는 별도의 테이블을 분리하여 처리량을 개선.

로컬 보조 인덱스를 가능한 작게 유지한다.
- 로컬 보조 인덱스는 스토리지와 테이블의 처리량을 사용하기 때문에 자주 쿼리하는 속성에 대해서만 생성하도록 함.
- 전체 테이블을 포함하지 않는 스파스 인덱스를 사용하여 효율성을 높임.

메모리 가속인 DAX(DynamoDB Accelerator)를 추가한다. (app - (DAX) - DynamoDB 구조)  
- 캐싱서비스로 밀리초 단위의 응답속도를 마이크로초 단위까지 줄일 수 있음.
- DynamoDB와 호환되어 변경사항이 크지 않음.
- read가 많은 경우 처리량을 줄여 비용을 절감시킴.