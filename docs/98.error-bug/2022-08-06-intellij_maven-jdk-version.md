---
layout: post
title: "[intellij error] Maven 3.3.1+ requires JDK 1.7+"
parent: error & bug
permalink: /docs/error-bug/intellij/maven-jdk-version
sitemap:
  lastmod: 2022-08-06
---

intellij에서 maven build 혹은 package 시 발생한 에러.  

## 환경

windows,  
intellij 2020 and 2022,  
kotlin spring,  
multi-module project


## 에러 메세지

왼쪽 하단에 팝업 노티로 아래와 같은 메세지가 출력.

```
Error running 'whatisthebetter-was [package]': Maven 3.3.1+ requires JDK 1.7+. Please set appropriate JDK
```


## 해결

1. Settings(Ctrl + Alt + S) 진입
2. Build, Execution, Deployment > Build Tools > maven > importing 진입
3. JDK for importer를 내가 가지고 있는 java 버전으로 설정
   - 나 같은 경우는 openjdk 11.
   - 윈도우 default 인지 모르겠으나, 초기 설정은 **Use Project JDK**으로 되어있었음.

이래도 해결되지 않았다면,

1. Build, Execution, Deployment > Build Tools > maven > Runner 진입
2. 위와 동일하게 내가 가지고 있는 java 버전으로 설정

