---
layout: post
title: "[spring error] log4j2.yml, yaml property not work"
parent: error & bug
permalink: /docs/error-bug/spring/yaml-property-not-work
sitemap:
  lastmod: 2022-08-10
---

spring에서 log4j2.yml, log4j2.yaml를 설정했는데 되지 않는 상황.  
아무 에러도 뜨지 않고 console이 그냥 멈춘 상태였다.  

## 환경

windows,  
intellij 2022,  
kotlin spring,  
log4j2.yaml


## 현상

console이 멈췄다.  
run했다는 메세지만 남고 에러도 없고 시작도 안했다.  

혹시나 싶어서 동일한 log4j2를 xml로 작성해보면 제대로 동작하는 것도 확인 가능했다.
- 테스트를 위한다면 인터넷에 샘플로 제공된 아무 xml이나 넣고 run해서 console 출력을 확인.


## 해결

아주 기본적인 실수를 셋업할 땐 참 많이도 한다.  
회사에선 xml만 쓰는데 log4j2의 경우 yml이 가독성이나 라인 수가 더 효율적일 것 같아서 시도했다가 시간을 많이도 버렸따.
yaml를 읽어주는 dependency가 빠졌던 것.

```xml
	<dependency>
		<groupId>com.fasterxml.jackson.dataformat</groupId>
		<artifactId>jackson-dataformat-yaml</artifactId>
		<version>2.5.0</version>
	</dependency>
```

### reference

- https://stackoverflow.com/questions/28101903/what-is-a-sample-default-config-file-in-yaml-for-log4j2