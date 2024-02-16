---
layout: post
title: "[spring error] log4j2, Class path contains multiple SLF4J bindings"
sidebar_label: "[spring error] log4j2, Class path contains multiple SLF4J bindings"
parent: error & bug
permalink: /docs/error-bug/spring/Class-path-contains-multiple-SLF4J-bindings
sitemap:
  lastmod: 2022-08-10
---

intellij에서 log를 설정한 뒤 test 실행 혹은 application run 중에 경고 같은 에러 발생.  

## 환경

windows,  
intellij 2022,  
kotlin spring,  
log4j2


## pom.xml

내 pom 파일 일부.  
gradle로 해도 같은 에러가 났다면 동일하게 해결할 수 있을 것 같다.  

```xml
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter</artifactId>
		</dependency>
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-web</artifactId>
			<exclusions>
				<exclusion>
					<groupId>org.springframework.boot</groupId>
					<artifactId>spring-boot-starter-logging</artifactId>
				</exclusion>
			</exclusions>
		</dependency>

		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-log4j2</artifactId>
			<version>2.7.2</version>
		</dependency>
```


## 에러 메세지

mvn으로 package를 하려고 하다가 발생했다.  
나는 multi-module로 core 모듈과, was 모듈을 가지고 있는데, project 상위 pom으로 build를 시도했다가 에러를 받았다.  

project packaging 중 core 모듈 packaing에서 에러가 발생한 것.  

```
SLF4J: Class path contains multiple SLF4J bindings.
SLF4J: Found binding in [jar:file:/C:/Users/soup/.m2/repository/ch/qos/logback/logback-classic/1.2.11/logback-classic-1.2.11.jar!/org/slf4j/impl/StaticLoggerBinder.class]
SLF4J: Found binding in [jar:file:/C:/Users/soup/.m2/repository/org/apache/logging/log4j/log4j-slf4j-impl/2.17.2/log4j-slf4j-impl-2.17.2.jar!/org/slf4j/impl/StaticLoggerBinder.class]
SLF4J: See http://www.slf4j.org/codes.html#multiple_bindings for an explanation.
SLF4J: Actual binding is of type [ch.qos.logback.classic.util.ContextSelectorStaticBinder]
```


## 해결

에러 메세지 그대로, slf4j에 binding된 dependency가 하나가 아니어서 발생한 에러다.  
해결을 위해서는 추가된 slf4j가 의도된 dependency만 추가되도록, 그렇지 않은건 제거해줄 필요가 있다.

maven dependency를 확인해보자.  

내 maven dependency  

![Class path contains multiple SLF4J bindings](/images/post/issue/spring/Class-path-contains-multiple-SLF4J-bindings.png)

보다시피 내가 추가한 **org.springframework.boot:spring-boot-starter-log4j2:2.7.2** 외에도,  
**org.springframework.boot:spring-boot-starter:2.7.0** 이 가지고 있는 logging이 있다.  
여기서 에러가 발생한 것.  

spring-boot-starter-web에서는 exclude를 해줬는데, spring-boot-starter에서는 누락한 것을 추가해준다.  


```xml
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter</artifactId>
			<exclusions>
				<exclusion>
					<groupId>org.springframework.boot</groupId>
					<artifactId>spring-boot-starter-logging</artifactId>
				</exclusion>
			</exclusions>
		</dependency>
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-web</artifactId>
			<exclusions>
				<exclusion>
					<groupId>org.springframework.boot</groupId>
					<artifactId>spring-boot-starter-logging</artifactId>
				</exclusion>
			</exclusions>
		</dependency>

		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-log4j2</artifactId>
			<version>2.7.2</version>
		</dependency>
```

### reference

- https://www.baeldung.com/slf4j-classpath-multiple-bindings