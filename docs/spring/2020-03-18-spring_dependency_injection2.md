---
layout: post
title: Spring Dependency Injection 2
tag:
  - spring
parent: spring
permalink: /docs/spring/dependency-injection2
---

## anotation을 이용한 설정
기존 xml을 이용한 스프링 설정 파일을 Java 파일로 제작하는 방법이다.  

`@Configuration`:  
해당 클래스가 spring 설정 파일로서 spring container를 생성할 수 있음을 명시한다.  

`@Bean`:  
해당 메소드로 Bean 객체를 생성하는 것을 명시한다.  

## anotation 적용
before:  
```xml
<bean id="studentDao" class="ems.member.dao.StudentDao" ></bean>
```
```java
GenericXmlApplicationContext ctx = 
        new GenericXmlApplicationContext("classpath:applicationContext.xml");
```

after:  
```java
// main class
AnnotationConfigApplicationContext ctx = 
		new AnnotationConfigApplicationContext(MemberConfig.class);

// Configuration class
@Configuration
public class MemberConfig {

	@Bean
    //     class      id
	public StudentDao studentDao() {
		return new StudentDao();
	}
```

## 다양한 타입의 의존 객체 주입 적용
다양한 타입에 대해 직관적으로 Bean을 생성할 수 있다.  
```java
@Bean
public DataBaseConnectionInfo dataBaseConnectionInfoDev() {
    DataBaseConnectionInfo infoDev = new DataBaseConnectionInfo();
		infoDev.setJdbcUrl("jdbc:oracle:thin:@localhost:1521:xe");
		infoDev.setUserId("scott");
		infoDev.setUserPw("tiger");
    
    return infoDev;
}

@Bean
public EMSInformationService informationService() {
    EMSInformationService info = new EMSInformationService();
    info.setInfo("Education Management System program was developed in 2015.");
    info.setCopyRight("COPYRIGHT(C) 2015 EMS CO., LTD. ALL RIGHT RESERVED. CONTACT MASTER FOR MORE INFORMATION.");
    info.setVer("The version is 1.0");
    info.setsYear(2015);
    info.setsMonth(1);
    info.setsDay(1);
    info.seteYear(2015);
    info.seteMonth(2);
    info.seteDay(28);
    
    ArrayList<String> developers = new ArrayList<String>();
    developers.add("Cheney.");
    developers.add("Eloy.");
    developers.add("Jasper.");
    developers.add("Dillon.");
    developers.add("Kian.");
    info.setDevelopers(developers);
    
    Map<String, String> administrators = new HashMap<String, String>();
    administrators.put("Cheney", "cheney@springPjt.org");
    administrators.put("Jasper", "jasper@springPjt.org");
    info.setAdministrators(administrators);
    
    Map<String, DataBaseConnectionInfo> dbInfos = new HashMap<String, DataBaseConnectionInfo>();
    dbInfos.put("dev", dataBaseConnectionInfoDev());
    dbInfos.put("real", dataBaseConnectionInfoReal());
    info.setDbInfos(dbInfos);
    
    return info;
}
```

## 설정 파일 분리
xml을 구분했던 것처럼 java 파일도 분리할 수 있다.  
1. 사용 클래스에서 모든 설정 class를 넣어 사용.
```java
AnnotationConfigApplicationContext ctx = 
		new AnnotationConfigApplicationContext(MemberConfig1.class, MemberConfig2.class, MemberConfig3.class);
```
2. 하나의 설정 파일에서 다른 것들을 import.
```java
@Configuration
@Import({MemberConfig2.class, MemberConfig3.class})
public class MemberConfig1 {
```
- MemberConfig2에서 Config1의 Bean을 사용한다면 이것도 `@Autowired`를 명시하여 사용할 수 있다. 파일이 분리되더라도 Container는 하나이기 때문이다.