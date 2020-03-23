---
layout: post
title: Spring Structure
tag:
  - spring
---
## spring MVC 설계 구조
![model](/images/post/spring_model1.JPG)
Controller, Service, DAO, View 와 같이 각각의 기능별로 모듈화 시키는 방식으로 유지보수가 수월하다.  

![model2](/images/post/spring_model2.JPG)  
1. DispatcherServlet - 연결을 담당하며 클라이언트한테 요청을 받음.
2. HandlerMapping - Controller 중 알맞은 것을 찾아서 리턴.
3. HandlerAdapter - Controller의 Method 중 알맞은 것을 찾아서 호출해서 요청을 처리하고 결과를 Model(혹은 ModelAndView)로 리턴.
   - controller 뒤에는 service, DB도 있음.
4. ViewResolver - model에 적합한 view를 리턴.
5. View - 응답 생성 (front-end)

# 프로젝트 구조
![structure](/images/post/file_structure.JPG)  
java file - Controller, Service DAO 등을 포함하는 java 파일들이 위치.  
resource - java 파일 이외의 개발에 필요한 .xml 등의 자원 파일.  
webapp - 웹과 관련된 파일.  
spring - 스프링 컨테이너를 생성하기 위한 스프링 설정 파일.  
views - view로 사용될 JSP 파일.  
web.xml - 웹 설정 파일.  
pom.xml - spring에서 사용할 모듈을 명시하는 maven 설정 파일.  

## DispatcherServlet (a.k.a front controller)
1. DispatcherServlet을 servlet으로 등록.  
   - web.xml에 명시.
2. 위에서 명시한 file path에 spring 설정 파일(servlet-context.xml) 작성.  
   - spring 설정 파일(servlet-context.xml)도 여기서 등록함.  
3. spring container가 만들어지고, container에는 handlerMapping, HandlerAdapter, ViewResolver가 자동으로 생성 됨.  
   - controller에 집중하여 개발할 수 있음.  

`<annotation-driven />`:  
spring 설정 파일에 annotation 사용을 명시해야 `@Controller` 등의 annotation을 사용할 수 있음.

## `@Controller`
**class**에 `@Controller`를 명시하여 Controller를 만듦.  

## `@RequestMapping`
**method**에 `@RequestMapping`를 명시하여 사용자로부터 들어오는 요청에 매핑시키는 함수를 만듦.  
여기서 return하는 값에 맞춘 view가 호출된다.  

```java
@Controller
public class HomeController {
    @RequestMapping(value="/home") // localhost:8080/success
    public String home(Locale locale, Model model) {
        return "home"; // home.jsp
    }
}
```

value 속성이 단독적으로 쓰일 때는 생략이 가능하다.  
method 속성을 통해 POST/GET을 설정할 수 있다.(default - GET)  
```java
@RequestMapping("/home") // = @RequestMapping(value="home", method=RequestMethod.GET)
```

method끼리 공통된 Mapping path가 있으면 `@RequestMapping`을 controller에 사용하여 공통된 path를 명시할 수 있음.  
```java
@Controller
@RequestMapping("/home")
public class HomeController {
    @RequestMapping("/success") // localhost:8080/home/success
    ...
}
```

## service
`@Service`.  
class에 `@Service`를 명시하여 service를 만듦.  
사용할 때 `@Autowired`를 통해 자동으로 받음.
- `@Component`, `@Repository`도 같은 역할을 함.

## Dao
dao 객체도 `@Component`, `@Repository`로 생성할 수 있음.

## request 전송 정보 얻기
1. `HttpServletRequest`의 `getParameter()`를 통해
    ```xml
    ID: <input type="text" name="memId">
    ```
    ```java
    public String memLogin(Model model, HttpServletRequest request) {
        String memId = request.getParameter("memId");
    }
    ```
2. `@RequestParam` annotation을 통해
    ```java
    public String memLogin(Model model, @RequestParam(value="memId") String memId) { ... }
    ```
    - value 속성이 단독으로 쓰일때 생략 가능하다.  
    ```java
    @RequestParam("memId") // = @RequestParam(value="memId")
    ```
    - `required` 속성이 꼭 필요한지 여부 체크를 위해 사용될 수 있다.
    - `defaultValue` 속성이 전달되지 않을 경우의 default 값으로 사용될 수 있다.
    - 위 속성들은 보통 front-end에서 값을 검증 후 보내기 때문에 잘 사용되지 않음.
3. 커맨드 객체를 이용
    ```java
    // Member class
    public void setMemId(String memId) {
        this.memId = memId;
    }

    // controller
    pbulic String memJoin(Member member) { ... }
    ```
    setter/getter가 구현된 커맨드 객체에 대해 html의 값 name들이 커맨드 객체의 변수명과 일치한다면 자동으로 setter가 적용되기 때문.  
    view에서도 동일하게 커맨드 객체명.변수명을 통해 접근할 수 있음. 

`@ModelAttribute`.  
매개변수에 `@ModelAttribute("nickname")`를 통해 nickname라는 이름으로 view 단에서 해당 객체에 이전처럼 접근할 수 있음.  

method에 `@ModelAttribute("servertime")`과 같이 명시하면  
이 함수는 클래스에 어떤 함수가 호출되더라도 언제나 같이 호출되고  
이 이름으로 view 단에서 바로 결과값을 가져다가 쓸 수 있음.  

## 커맨드 객체 데이터 타입
해당 타입에 맞는 getter/setter를 만들어줘야 문제가 없음.  
- 기본타입/배열/List

## Model & modelAndView
controller에서 view에 데이터를 전달하기 위해 사용되는 객체로 Model과 ModelAndView가 있다.
Model은 view에 데이터만을 전달하기 위한 객체이고, ModelAndView 는 데이터와 view의 이름을 함께 전달하는 객체이다.