---
layout: post
title: "SQL vs NoSQL"
sidebar_label: "SQL vs NoSQL"
parent: Database
permalink: /docs/db/why-use-nosql
sitemap:
  lastmod: 2022-06-15
---

AWS에서 진행하는 dynamodb immersion day 세션에 참여할 수 있는 기회가 생겼다.  
강사님께서 왜 nosql을 사용하게 되었고 쓰는지에 대한 배경을 설명해주신 것이 인상적어서 정리해본다.


## SQL with Normalization

**RDBS에서 가장 중요하게 생각하는 것은 정규화**이다.  
그렇다면 왜 정규화를 하는가? 이 것이 중요하다.

정규화를 하는 **목적은 당연히 데이터의 중복을 제거하는 것**이 가장 크다.
- 물론 이를 통한 데이터의 일관성을 유지하는 목적도 있다.

얼핏 보면 당연하지만 데이터의 중복을 제거하는 것이 왜 중요했는지는 시대적 배경을 보면 이해가 된다.  



### hard drive로 보는 Normalization

![5mb hard](/images/post/database/why-use-nosql/5mbharddrive1956.jpg)

1956년 IBM의 5MB hard drive를 한 달 대여하는 비용이 $3200 이었다.
- 2019년 가격으로 환산하면 약 $30000 이다.

당시에는 hard disk가 이와 같이 굉장히 비쌌기 때문에 **hard disk를 효율적으로 사용하는 것이 가장 중요한 일**이 되었다.  
따라서 당시에 개발되고 주로 사용되던 **RDBS에서는 데이터의 중복을 최소화하는 방향으로** 개발 되었다.  
사실, **정규화하는 operation은 CPU를 사용하는 것인데 CPU를 더 사용하는 비용을 지불하여 disk 비용을 줄이는 것**이라고 볼 수 있다.  

그치만 현재에 와서는 hard disk 값은 굉장히 싸졌다.


## 그래서 SQL vs NoSQL

그래서 CPU 비용이 되려 비싼 현재에서는 정규화로 과도한 disk 비용을 줄이는 것보다 CPU 비용을 줄이고 disk 비용을 늘리는 방향의 NoSQL이 틀리지 않다.


## 아마존의 dynamodb

NoSQL은 최근에 와서야 개발되기 시작한 기술이다.  
다른 NoSQL들도 비슷한 상황에서 개발되었는데 아마존에서는 어떻게 dynamodb를 개발하게 되었는지를 보면 이해가 된다.

1. 2004년 12월
   - 12월은 아마존 쇼핑에서 트래픽이 가장 큰 달이다.
   - DB scalability 이슈가 발생했다.
2. 2007년 10월
   - 현재의 dynamodb와는 다르지만 dynamo 논문이 발표되었다.
3. 2012년 1월
   - dynamodb genaral availability

SQL에서는 ACID 때문에 scale을 늘리는 것이 더 쉽지 않고,  
최근의 enterprise급 service들은 scale이 굉장히 크기 때문에 NoSQL이 발전하게 되었다.


## Scale up vs Scale out

![scale up vs scale out](/images/post/database/why-use-nosql/scaleup-scaleout.png)

위와 같이 sql은 ACID 지원등을 이유로 scale up(vertical-scaling)을 해야 하는게 기본이다.  
반면에 nosql들은 scale out(horizontal scaling)으로 관리할 수 있어 scale 관리가 쉽다.


## 결론

규모있는 서비스를 하는 경우는 scalable하게 사용 가능한지를 따져봐야하고 그런 면에서 NoSQL이 용이하다.  
- scaling이 쉽기 때문

그러나 global 대기업들에서 여전히 SQL을 많이 쓰고 있다. (보통 둘 다 쓴다)  
그럴 수 있는 이유는 SQL을 scalable하게 사용할 수 있도록 managing 하는 내부 service들을 이미 가지고 있기 때문이다.

nosql을 선택하는데는 여러 기준이 있겠지만 scaling을 고려한다면 enterprise 급인데 SQL을 scalable하게 관리하는 service가 없다면 nosql을 충분히 고려해볼만 하다.
- 우리 회사도 그렇다.

현재는 SQL이 NoSQL의 장점을, NoSQL이 SQL의 장점을 따라가고 있어 경계가 모호해지는 부분들도 있다.

### reference

- AWS immersion day session 강의
- https://proftomcrick.com/2011/12/26/in-1956-5mb-was-big-enough-for-anyone/
- https://softwareengineering.stackexchange.com/questions/194340/why-are-nosql-databases-more-scalable-than-sql
- https://www.iunera.com/kraken/uncategorized/what-is-a-nosql-database/