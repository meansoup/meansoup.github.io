---
layout: post
title: Spring Settings
tag:
  - spring
parent: spring
permalink: /docs/spring/initializr
---

## Spring boot 세팅

[spring initializr](https://start.spring.io/)에서 spring boot 세팅

1. **Project:** Gradle Project
   - maven이 많이쓰이지만 성능은 Gradle이 좋음
2. **Language:** Java
3. **Spring Boot:** stable version
4. **Project Metadata:**
   - Group, Artifact, Name 에 적절히 기입
5. **Package name**: Jar
6. **Java**: 초기 프로젝트라면 최신 버전으로
7. **Dependencies**:
   - Lombok, Spring Web 추가
   - dependencies는 이후에 추가해도 됨

## Intellij Lombok 세팅

File > Settings > Plugins > `lombok` 설치  
File > Settings > Build ... > Compiler > `Build project automatically` 체크
File > Settings > Build ... > Compiler > Annotation Processors > `Enable annotation processing` 체크