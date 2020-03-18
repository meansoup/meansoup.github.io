---
layout: post
title: Spring Dependency Injection
tag:
  - spring
---

## 의존 객체 주입
resource에서 xml로 bean을 생성 후 접근할 수 있다.  
1. xml 생성후 java 코드에서 xml을 불러와서 사용.  
```java
GenericXmlApplicationContext ctx = new GenericXmlApplicationContext("classpath:xmlname")
```
2. xml을 분리할 경우 매개변수로 xml 파일명을 모두 넣어 사용.
```java
GenericXmlApplicationContext ctx = new GenericXmlApplicationContext({"classpath:xmlname", "classpath:xmlname2"})
```
- 하나의 xml에서 다른 xml을 import하기도 한다.

bean은 동일한 타입에 대해 하나만 생성되고 `getBean()`으로 호출하더라도 동일 객체를 반환하는 singleton이다.  
prototype으로 쓰기 위해서는 bean에 `scope="prototype"`을 명시해줘야 한다.

## 다양한 의존 객체 주입
1. 생성자를 이용
    ```xml
    <bean id="studentDao" class="ems.member.dao.StudentDao"></bean>
    <bean id="registerService" class="ems.member.service.StudentRegisterService">
        <constructor-arg ref="studentDao"></constructor-arg>
    </bean>
    ```
    ```java
    public StudentRegisterService(StudentDao studentDao){
        this.studentDao = studentDao
    }
    ```
2. setter를 이용
    ```xml
    <bean id="dataBaseConnectionInfoDev" class="ems.member.DatabaseConnectionInfo">
        <property name="jdbcUrl" value="jdbc:oracle:thin:@localhost:1521:xe" />
        <property name="userId" value="scott" />
        <property name="userPw" value="tiger" />
    </bean>
    ```
    ```java
    public void setJdbcUrl(String jdbcUrl)
        this.jdbcUrl = jdbcUrl
    }
    public void setUserId(String userId)
        this.userId = userId
    }
    public void setUserPw(String userPw)
        this.userPw = userPw
    }
    ```
3. List type
    ```xml
    <property name="developers">
    <list>
        <value>Cheney.</value>
        <value>Eloy.</value>
        <value>Jasper.</value>
        <value>Dillon.</value>
        <value>Kian.</value>
    </list>
    </property>
    ```
    ```java
    public void setDevelopers(List<String> developers) {
        this.developers = developers
    }
    ```
4. map type
    ```xml
    <property name="administrators">
    <map>
        <entry>
            <key>
                <value>Cheney</value>
            </key>
                <value>cheney@springPjt.org</value>
        </entry>
        <entry>
            <key>
                <value>Jasper</value>
            </key>
                <value>jasper@springPjt.org</value>
        </entry>
    </map>
    </property>
    ```
    ```java
    public void setAdministrators(Map<String, String> administrator) {
        this.administrator = administrator;
    }
    ```

## 의존 객체 자동 주입
스프링 설정파일에서 `constructor-org` 또는 `property` 태그로 의존 대상을 명시하지 않아도 알아서 주입해주는 기능이다.  
`@Autowired`,`@Resource`, `@Inject` annotation을 사용하여 주입하려는 객체의 타입이 일치하는 객체를 자동으로 주입한다.  

`@Autowired`, `@Inject`:  
객체의 타입을 container에서 찾아서 해당하는 것을 넣어줌.
생성자에 사용하는 경우는 그냥 사용할 수 있음.  
변수나 함수에 사용하는 경우는 반드시 default constructor를 명시해줘야 함.  
- 해당 클래스의 변수/함수를 접근하려는데 클래스가 없기 때문에 접근이 안되기 때문.

`@Resource`:  
객체의 이름을 container에서 찾아서 해당하는 것을 넣어줌.  
생성자에는 사용할 수 없고 변수/함수에만 사용할 수 있음.  
- 동일하게 default constructor가 필요. 객체가 있어야 주입을 할 수 있기 때문.  

## 의존 객체 선택
동일한 데이터 타입의 다수의 Bean 객체가 있을 때 대상이 되는 객체를 선택하는 방법.  
위와 같은 상황에서 `@Autowired`를 통해 자동 주입을 할 경우 자동 주입 대상 객체를 판단하지 못해 Exception이 발생함.  

해결책:  
1. 어떤 객체를 쓸 것인지를 명시해준다.  
    ```xml
    <bean id="testObj1" class="com.mean.TestObj">
        <qualifier value="usedObj" />
    </bean>
    <bean id="testObj2" class="com.mean.TestObj" />
    ```
    ```java
    @Autowired
    @Qualifier("usedObj")
    private TestObj testObj;
    ```
2. `Autowired`,`Qualifier` 대신 `Inject`,`Named`를 사용한다.  
    ```xml
    <bean id="testObj1" class="com.mean.TestObj" />
    <bean id="testObj2" class="com.mean.TestObj" />
    ```
    ```java
    @Inject
    @Named(value="testObj1")
    private TestObj testObj;
    ```
3. java의 변수명과 bean id 명을 맞춰준다.  
    ```xml
    <bean id="testObj" class="com.mean.TestObj" />
    <bean id="testObj2" class="com.mean.TestObj" />
    ```
    ```java
    @Autowired
    private TestObj testObj;
    ```

## 의존 객체 자동 주입 체크
`Autowired`를 명시했는데 해당하는 객체가 container에 있지 않을 경우 exception이 발생하는 것을 막는 방법.  
근데 이렇게 코딩하는 경우는 있으면 안될 것이다.  
```java
@Autowired(required = false)
pricvate TestObj testObj;
```
