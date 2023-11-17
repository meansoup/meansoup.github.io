---
layout: post
title: "[spring error] JpaRepository NoSuchBeanDefinitionException"
parent: error & bug
permalink: /docs/error-bug/spring/NoSuchBeanDefinitionException_JpaRepository
sitemap:
  lastmod: 2022-06-25
---

spring에서 Jpa bean이 잘 생성되지 않은 경우

## 에러 메세지

```
Caused by: org.springframework.beans.factory.NoSuchBeanDefinitionException: No qualifying bean of type 'com.meansoup.whatisthebetter.application.port.out.like.mysql.MysqlLikeJpaRepository' available: expected at least 1 bean which qualifies as autowire candidate. Dependency annotations: {@org.springframework.beans.factory.annotation.Autowired(required=true)}
	at org.springframework.beans.factory.support.DefaultListableBeanFactory.raiseNoMatchingBeanFound(DefaultListableBeanFactory.java:1799)
	at org.springframework.beans.factory.support.DefaultListableBeanFactory.doResolveDependency(DefaultListableBeanFactory.java:1355)
	at org.springframework.beans.factory.support.DefaultListableBeanFactory.resolveDependency(DefaultListableBeanFactory.java:1309)
	at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.resolveDependency(AbstractAutowireCapableBeanFactory.java:489)
	at org.springframework.beans.factory.annotation.ParameterResolutionDelegate.resolveDependency(ParameterResolutionDelegate.java:136)
	at org.springframework.test.context.junit.jupiter.SpringExtension.resolveParameter(SpringExtension.java:270)
	at org.junit.jupiter.engine.execution.ExecutableInvoker.resolveParameter(ExecutableInvoker.java:216)
	... 54 more
```

## 해결

JpaConfiguration을 위한 class를 생성해준다.

```Kotlin
@Configuration
@EnableJpaAuditing
@EnableJpaRepositories("com.meansoup.whatisthebetter")
class JpaConfiguration {}
```


## 원인

spring에서 jpa repository를 enable 하기 위해서 필요하다.