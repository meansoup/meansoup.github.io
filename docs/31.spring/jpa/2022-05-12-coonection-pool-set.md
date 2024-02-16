---
layout: post
title: Spring JPA connection pool 조정하기
sidebar_label: Spring JPA connection pool 조정하기
nav_order: 1
parent: Spring JPA
grand_parent: Spring
permalink: /docs/spring/jpa/set-connection-pool
sitemap:
  lastmod: 2022-05-12
---

DB를 사용한다면 connection pool을 설정하는 것은 필수이다.  
분명 작년에도 했던 작업인데 이번에 Mysql connection pool을 조정하면서 기억이 나지 않아서 기록한다.


## connection pool 확인

setting 전에 [어떤 connection pool을 사용하고 있는지 확인](/docs/spring/jpa/find-connection-pool)해야 한다.
- default는 **Hikari**

## 현재 db의 connection 확인

database 접속 후 아래 명령어로 connection을 확인할 수 있다.
```sql
show status like "%connect%";
```

## JPA property setting

[Spring Common Property](https://docs.spring.io/spring-boot/docs/current/reference/html/application-properties.html#appendix.application-properties.data)를 참고한다.  

`spring.datasource`로 검색하면 datasource property를 찾을 수 있다.  
여기서 어떤 connection pool을 사용하느냐에 따라 세팅해야 하는 property가 다르다.

일반적으로는 hikari이고 max pool size와 minimum idle을 세팅해준다.  
```property
spring.datasource.hikari.maximum-pool-size=10 # 최대 pool size
spring.datasource.hikari.minimum-idle=10 # 최소 pool size
```
- hikari에서는 minimum과 maximum을 같게 커넥션 수를 고정하여 최적의 성능을 뽑을 수 있다.


## connection pool 주의사항

당연하게도 JPA의 property 세팅은 instance 단위이고 maximum 10이고 instance가 20 대이면 200개의 connection이 생길 수 있다.  
이를 고려하여 DB(Mysql 등)의 Max Connection을 넉넉하게 유지해야 한다.  


### reference

spring common property
- https://docs.spring.io/spring-boot/docs/current/reference/html/application-properties.html