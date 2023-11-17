---
layout: post
title: "[kotlin error] ClassNotFoundException: kotlin.jvm.JvmInline"
parent: error & bug
permalink: /docs/error-bug/kotlin/ClassNotFoundException_kotlin_jvm_JvmInline
sitemap:
  lastmod: 2022-06-23
---

kotlin에서 **jackson-module-kotlin**를 사용할 때 에러.

## 에러 메세지

```
Caused by: java.lang.ClassNotFoundException: kotlin.jvm.JvmInline
	at java.base/jdk.internal.loader.BuiltinClassLoader.loadClass(BuiltinClassLoader.java:582)
	at java.base/jdk.internal.loader.ClassLoaders$AppClassLoader.loadClass(ClassLoaders.java:178)
	at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:521)
	... 80 more
```

## 코드

```xml
<!-- pom.xml -->
		<dependency>
			<groupId>com.fasterxml.jackson.module</groupId>
			<artifactId>jackson-module-kotlin</artifactId>
			<version>2.13.3</version>
		</dependency>
```

## 해결

```xml
<!-- pom.xml -->
		<dependency>
			<groupId>com.fasterxml.jackson.module</groupId>
			<artifactId>jackson-module-kotlin</artifactId>
			<version>2.12.7</version>
		</dependency>
```

## 원인

jackson-module-kotlin에서 2.13 version 부터 kotlin 1.5를 사용하기 시작했다.  
- 참고로 JvmInline이 kotlin 1.5에서 나왔음.

dependency version을 내리거나, kotlin verison을 올리면 된다.  


## reference

https://github.com/FasterXML/jackson-module-kotlin/issues/523
