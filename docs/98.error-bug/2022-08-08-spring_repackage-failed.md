---
layout: post
title: "[spring error] repackage failed: Unable to find main class"
parent: error & bug
permalink: /docs/error-bug/spring/repackage-failed-Unable-to-find-main-class
sitemap:
  lastmod: 2022-08-08
---

intellij에서 maven package 시 발생한 에러.  

## 환경

windows,  
intellij 2022,  
kotlin spring,  
multi-module project


## 에러 메세지

mvn으로 package를 하려고 하다가 발생했다.  
나는 multi-module로 core 모듈과, was 모듈을 가지고 있는데, project 상위 pom으로 build를 시도했다가 에러를 받았다.  

project packaging 중 core 모듈 packaing에서 에러가 발생한 것.  

```
Failed to execute goal org.springframework.boot:spring-boot-maven-plugin:2.7.0:repackage (repackage) on project whatisthebetter-core: Execution repackage of goal org.springframework.boot:spring-boot-maven-plugin:2.7.0:repackage failed: Unable to find main class

```


## 해결

**spring-boot-maven-plugin**에 대해 알 필요가 있다.  
spring-boot-maven-plugin은 springboot에서 executable jar & war를 packaging 하는 것을 지원한다.  

따라서 multi-module에서 core나 library 같은 module은 해당 dependency를 빼주면 된다.
core/library module에서 아래 plugin 제거.  

```xml
			<plugin>
				<groupId>org.springframework.boot</groupId>
				<artifactId>spring-boot-maven-plugin</artifactId>
			</plugin>
```

### reference

- https://docs.spring.io/spring-boot/docs/current/maven-plugin/reference/htmlsingle/
- https://stackoverflow.com/questions/42937577/unable-to-find-main-class-with-maven-on-spring-boot-project-in-eclipse