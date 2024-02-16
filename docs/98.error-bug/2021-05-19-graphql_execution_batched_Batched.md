---
layout: post
title: "[spring error] java.lang.NoClassDefFoundError: graphql/execution/batched/Batched"
sidebar_label: "[spring error] java.lang.NoClassDefFoundError: graphql/execution/batched/Batched"
tag:
  - error
parent: error & bug
permalink: /docs/error-bug/spring/graphql_execution_batched_Batched
sitemap:
  lastmod: 2021-05-19
---

graphql을 spring에서 사용하려고 하던 중 에러가 났다.  
뭐가 잘못됐는지 시간을 한참 썼는데 원인은 허무하다.  
뭐 이런 일들이 항상 그렇지..

## 에러 메세지

```log
Caused by: java.lang.NoClassDefFoundError: graphql/execution/batched/Batched
	at com.coxautodev.graphql.tools.MethodFieldResolver$Companion.isBatched(MethodFieldResolver.kt:24) ~[graphql-java-tools-5.2.4.jar:na]
	at com.coxautodev.graphql.tools.MethodFieldResolver.scanForMatches(MethodFieldResolver.kt:103) ~[graphql-java-tools-5.2.4.jar:na]
	at com.coxautodev.graphql.tools.SchemaClassScanner.scanResolverInfoForPotentialMatches(SchemaClassScanner.kt:230) ~[graphql-java-tools-5.2.4.jar:na]
	at com.coxautodev.graphql.tools.SchemaClassScanner.handleRootType(SchemaClassScanner.kt:122) ~[graphql-java-tools-5.2.4.jar:na]
	at com.coxautodev.graphql.tools.SchemaClassScanner.scanForClasses(SchemaClassScanner.kt:80) ~[graphql-java-tools-5.2.4.jar:na]
	at com.coxautodev.graphql.tools.SchemaParserBuilder.scan(SchemaParserBuilder.kt:151) ~[graphql-java-tools-5.2.4.jar:na]
	at com.coxautodev.graphql.tools.SchemaParserBuilder.build(SchemaParserBuilder.kt:157) ~[graphql-java-tools-5.2.4.jar:na]
	at com.oembedler.moon.graphql.boot.GraphQLJavaToolsAutoConfiguration.schemaParser(GraphQLJavaToolsAutoConfiguration.java:57) ~[graphql-spring-boot-autoconfigure-5.0.2.jar:na]
	at com.oembedler.moon.graphql.boot.GraphQLJavaToolsAutoConfiguration$$EnhancerBySpringCGLIB$$e208bf0b.CGLIB$schemaParser$2(<generated>) ~[graphql-spring-boot-autoconfigure-5.0.2.jar:na]
	at com.oembedler.moon.graphql.boot.GraphQLJavaToolsAutoConfiguration$$EnhancerBySpringCGLIB$$e208bf0b$$FastClassBySpringCGLIB$$fdb89603.invoke(<generated>) ~[graphql-spring-boot-autoconfigure-5.0.2.jar:na]
	at org.springframework.cglib.proxy.MethodProxy.invokeSuper(MethodProxy.java:244) ~[spring-core-5.3.20.jar:5.3.20]
	at org.springframework.context.annotation.ConfigurationClassEnhancer$BeanMethodInterceptor.intercept(ConfigurationClassEnhancer.java:331) ~[spring-context-5.3.20.jar:5.3.20]
	at com.oembedler.moon.graphql.boot.GraphQLJavaToolsAutoConfiguration$$EnhancerBySpringCGLIB$$e208bf0b.schemaParser(<generated>) ~[graphql-spring-boot-autoconfigure-5.0.2.jar:na]
	at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method) ~[na:na]
	at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62) ~[na:na]
	at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43) ~[na:na]
	at java.base/java.lang.reflect.Method.invoke(Method.java:566) ~[na:na]
	at org.springframework.beans.factory.support.SimpleInstantiationStrategy.instantiate(SimpleInstantiationStrategy.java:154) ~[spring-beans-5.3.20.jar:5.3.20]
	... 124 common frames omitted
Caused by: java.lang.ClassNotFoundException: graphql.execution.batched.Batched
	at java.base/jdk.internal.loader.BuiltinClassLoader.loadClass(BuiltinClassLoader.java:582) ~[na:na]
	at java.base/jdk.internal.loader.ClassLoaders$AppClassLoader.loadClass(ClassLoaders.java:178) ~[na:na]
	at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:521) ~[na:na]
	... 142 common frames omitted
```

## 코드

문제의 pom.xml은 이렇다.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
	<parent>
        ...
		<version>2.7.0</version>
	</parent>
    ...
	<dependencies>
        ...
		<dependency>
			<groupId>com.graphql-java</groupId>
			<artifactId>graphql-spring-boot-starter</artifactId>
			<version>5.0.2</version>
		</dependency>
		<dependency>
			<groupId>com.graphql-java</groupId>
			<artifactId>graphql-java-tools</artifactId>
			<version>5.2.4</version>
		</dependency>
	</dependencies>
```

## 해결

위 pom.xml에서 문제는 springboot version 이었다.  
com.graphql-java의 현재 최신 버전인 각각 5.0.2와 5.2.4가 springboot 2.7.0과 호환이 되지 않는 것이 문제였고,  
springboot version을 2.6.7로 낮추면서 문제는 해결됐다.


### reference

참고한 graphql 코드
- https://www.baeldung.com/spring-graphql

해결 방법 stackoverflow
- https://stackoverflow.com/questions/71039670/spring-boot-graphqlqueryresolver-wont-run-runs-on-test-project
