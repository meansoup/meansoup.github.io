---
layout: post
title: AWS 비용 효율화
sidebar_label: AWS 비용 효율화
parent: aws
permalink: /docs/aws/cost-efficiency
sitemap:
  lastmod: 2022-09-27
---

연말이 다가오면 회사에선 항상 비용을 줄이라고 한다.  
매년 비용을 어떻게 줄였는지 간략하게 정리해본다.


## 비용들

AWS에서 service 별로 어떻게 비용이 증가하는지 확인할 수 있다.  
tag를 달아서 운영하는 모듈별로 어떤 비율로 사용하는지.

비용은 크게 네 가지로 나눌 수 있다.

1. storage
2. database
3. instance
4. network


## Storage 비용

storage 비용은 request 비용과 storage 비용으로 나뉜다.  

### request 비용 줄이기

크기가 작은 경우 dynamoDb에 밀어 넣을 수 있다.  
그렇게 되면 성능도 확보할 수 있고 request 비용도 줄일 수 있다.

그치만 크기가 큰 경우나 사용성에 따라 되려 dynamo 저장 비용이 커질 수 있다.  
dynamo는 request 비용이 싸고 S3는 storage 비용이 싸다.  

### storage 비용 줄이기

storage layering을 통해 s3 오래된 데이터를 cold storage로 이동시킨다.  
S3 Glacier가 분 단위 이상의 검색 시간이 걸려서 사용하지 못했으나 새롭게 나온  **S3 Glacier Instant Retrieval** 같은 타입에서는 밀리초 단위의 검색 시간 소요하기 때문에 비용을 줄이면서 충분히 사용할 수 있다.

물론 우리 팀에선 아직 안써봤고 신뢰성이 조금 떨어질 수 있다고 판단했다.  
(dynamo에서 consistency가 늘어졌던 적도 있고..)


## database 비용

database 비용도 비슷한데 RCU/WCU와 storage 비용으로 나뉜다.

### dynamo storage 비용 줄이기

유사하게 storage layering으로 오래된 data를 s3로 이동시킨다.  
호출비용과 저장비용을 잘 계산해서 진행해야 한다. 무작정 s3는 되려 비쌀 수 있다.  

잘 사용하지 않는 데이터를 bulk로 s3에 backup하면 비용을 많이 줄일 수 있다.  
다만 서비스 로직 변경이 크다.

### CU 줄이기

CU는 provision을 줄이는 방향으로도 갈 수 있다.  
우리 팀에선 single table로 migration 해서 CU를 크게 줄였다.


## storage & database 공통 비용 줄이기

storage나 database 모두 data를 저장하는 곳이다.  
data가 service됨에 따라 data가 쌓이기만 한다면 비용은 계속 증가할 수 밖에 없다.  

따라서 data에 대한 핸들링이 필요하다.

### garbage collection 하기

지워야 했던, 지울 수 있는 데이터를 삭제한다.  

삭제가 필요했던 탈퇴한 사용자에 대한 데이터 삭제가 되지 않았다거나.  
관련된 data가 삭제되었으나 남아있는 찌꺼기가 있다거나.  
성능 상의 이슈로 미뤄진 data 삭제 등이 남아있을 수 있다.

### data life cycle 확인하고 조절하기

data life cycle이 사실 비용에서 가장 중요하다.  
data가 10년이 지나도 쌓이기만 한다면 비용은 증가할 수 밖에.  
1Y 보관기간의 데이터를 6M으로 줄일 수 있다면 storage 비용을 반으로 줄일 수 있다.  

data life cycle을 확인하고 그 정도의 life cycle이 필요한지 확인한다.  
삭제를 하는 경우를 명확하게 정의하고 ttl 설정 혹은 delay batch로 삭제한다.  

사진/동영상의 경우 thumbnail의 lifecycle도 고려가 필요하다.


## instance 비용

서비스 특성에 따라 instance가 CPU / memory / I/O 중 어디에 bound 되는지 확인할 필요가 있다.  
어느 정도의 instance type과 크기가 필요한지 테스트 해서 적절한 type을 사용한다.


## network 비용

binary가 비효율적으로 흐르지 않는지 확인한다.  
client와 통신에 compression(Gzip 등)이 적용되었는지 확인한다. 


---


실제로 서비스가 오픈되었다면 심각한 상황이 아니고서야 비용을 크게 줄일만한 부분이 잘 없다.  
우리가 제공하는 서비스 같은 경우는 data가 많이 쌓여서 CPU 비용은 비율이 낮을 정도이다.  

결국 data life cycle을 확인하고 data 비용을 줄여나가는 방향.  
서비스 초기에 life cycle을 잘 잡아두면 도움이 많이 된다.  

내가 생각하기에 어느정도 GC가 진행됐다면 지금 우리팀 같은 상황에선 비용이 새고 있는 곳은 없는 것 같다.  
(작년/재작년에는 새고있는 돈들을 많이 잡았지만)  
결국 이정도 상황에선 **storage layering**을 어떻게 잘 해나가느냐가 비용을 줄일 수 있는 키가 되지 않을까 싶다.
