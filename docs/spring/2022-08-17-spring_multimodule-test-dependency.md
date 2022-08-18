---
layout: post
title: "spring multimodule에서 library module의 test class 사용하기"
parent: Spring
permalink: /docs/spring/multimodule-test-dependency
---

springboot multimodule을 사용하면서, test class가 dependency에 추가되지 않는 것을 확인했다.  
처음에는 그냥 그러려니 하고 조금 번거롭게 테스트 코드를 다시 작성했는데,  
테스트를 점점 추가하다보니 mother 패턴을 적용했던 코드들을 재사용하는 것이 맞다고 생각됐다.  


## 현상

src 코드는 잘 추가되어 사용하지만, test 코드들은 추가되지 않는 상황.  

현재 maven pom
```xml
		<dependency>
			<groupId>com.meansoup</groupId>
			<artifactId>whatisthebetter-core</artifactId>
			<version>0.0.1-SNAPSHOT</version>
			<scope>compile</scope>
		</dependency>
```


## 해결

현재 dependency는 그대로 두고 test dependency를 추가하면 사용할 수 있다.  
이렇게 되면 scope이 test여서 compile할 때 빨려들어가지도 않을거라 좋은 방향이다.

수정된 maven pom
```xml
		<dependency>
			<groupId>com.meansoup</groupId>
			<artifactId>whatisthebetter-core</artifactId>
			<version>0.0.1-SNAPSHOT</version>
			<scope>compile</scope>
		</dependency>
		<dependency>
			<groupId>com.meansoup</groupId>
			<artifactId>whatisthebetter-core</artifactId>
			<version>0.0.1-SNAPSHOT</version>
			<type>test-jar</type>
			<scope>test</scope>
		</dependency>
```


## dependency의 type

dependency의 artifact's packaging type을 명시하는 것이다.  
default는 jar.  
jar, pom, war, test-jar 등이 있고, test-jar를 통해 test package를 명시하였다.


## attach test-jar

위처럼하면 test를 돌리는데는 문제 없으나, mvn package / deploy 시에 test-jar가 core에서 생성되지 않아 에러가 발생한다.  
아래와 같이 plugin을 추가해서 해결한다.  

```xml
  <build>
    <plugins>
     <plugin>
       <groupId>org.apache.maven.plugins</groupId>
       <artifactId>maven-jar-plugin</artifactId>
       <version>3.0.2</version>
       <executions>
         <execution>
           <goals>
             <goal>test-jar</goal>
           </goals>
         </execution>
       </executions>
     </plugin>
    </plugins>
  </build>
```


## reference

- https://stackoverflow.com/questions/174560/sharing-test-code-in-maven

maven type
- https://zditect.com/blog/54005418.html
- https://www.quora.com/What-is-the-purpose-to-use-type-in-a-maven-dependency

test jar build
- https://maven.apache.org/guides/mini/guide-attached-tests.html