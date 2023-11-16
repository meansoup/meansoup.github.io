---
layout: post
title: Spring Connection Pool 확인하기
nav_order: 1
parent: Spring JPA
grand_parent: Spring
permalink: /docs/spring/jpa/find-connection-pool
sitemap:
  lastmod: 2022-05-11
---

spring 에서는 몇 가지 connection pool을 제공한다.  
DB를 사용할 때는 connection pool 설정은 필수인데 어떤 pool을 쓰느냐에 따라 property가 달라지기 때문에 어떤 connection pool을 쓰는지 확인하는 방법을 찾아봤다.

## default connection pool

Spring Boot에서는 아래와 같은 우선순위로 connection pool을 사용한다.

1. HikariCP
2. Tomcat pooling
3. DBCP2
4. Oracle UCP

**HikariCP**가 performance & concurrency가 가장 우수해서 default로 사용된다.  
**HikariCP**를 사용할 수 없는 경우 **Tomcat pooling**을 사용하고 차례대로 각 CP를 사용한다.

`spring-boot-starter-jdbc` 혹은 `spring-boot-starter-data-jpa`을 사용하면 자동으로 HikariCP를 사용한다고 보면된다.


## connection pool 직접 확인하기

connection pool을 default로 **Hikari**를 쓰겠지만 서비스를 운영하는 입장에서 확인하지 않고 설정하기엔 찝찝했다.  
Spring에서 어떤 connection pool을 쓰는지 확인하는 방법을 알고 싶기도 했다.

### 1. test에서 확인하기

```java
@SpringBootTest
class AnyThingTest {

    @Autowired
    DataSource dataSource;

    @Test
    void checkCP() {
        System.out.println("DATASOURCE = " + dataSource);
    }
}
```
> *printed:  **DATASOURCE = HikariDataSource (HikariPool-1)***

### 2. service에서 확인하기

test는 환경이 다를까 못 미더워서 추가로 확인해보기

```java

@Component
class AnyThing {

    @Autowired
    DataSource dataSource;

    @PostConstruct
    void init() {
        System.out.println("DATASOURCE = " + dataSource);
    }
}

```
> *printed:  **DATASOURCE = HikariDataSource (HikariPool-1)***


### reference

spring boot의 default connection pool 우선순위
- https://docs.spring.io/spring-boot/docs/current/reference/htmlsingle/#data.sql.datasource.connection-pool

connection pool 확인하기
- https://mkyong.com/spring-boot/spring-boot-how-to-know-which-connection-pool-is-used/