---
layout: post
title: Domain Service
parent: 전술적 설계
grand_parent: Domain Driven Design
nav_order: 7
permalink: /docs/ddd/tactical/domain-service
---

개념만 보면 domain은 domain 로직이 있는 곳이다.  
막상 개발/설계를 해보니 어디까지가 domain service이고 어디까지가 application service 인지의 분간하는게 쉽지가 않다.  

설계 할때는 이게 맞다 저게 맞다 토론을 하곤 하는데 항상 돌이켜보면 어딘가는 잘못 설계된 것 같다.  
아직 DDD에 대한 이해가 많이 부족한 것 같다.

최근에 *이거 되게 이상한데? 어디에 둬야하지?* 싶은 로직이 있었다.  
그걸 명확하게 하기 위해 domain service를 다시 보았다.


## 도메인 서비스 (domain service)

domain 내에서 service란 도메인 고유의 작업을 수행하는 stateless operation이다.  
당연히 domain service는 유비쿼터스 언어에 맞게 모델링 되어야 한다.

domain service는 필요에 따라 어떤 도메인 객체든 사용할 수 있다.  

말 그대로 도메인 로직을 가지고 있는 서비스인데,  
그렇다면 어떤 로직이 domain service에 들어가고 어떤 로직이 entity/vo에 들어가는지를 알아야 한다.



## 도메인 모델에서 서비스가 생성되는 경우

일반적으로 이런 상황에서 사용할 수 있다.
- Perform a significant business process 
- Transform a domain object from one composition to another 
- Calculate a Value requiring input from more than one domain object

아래와 같은 상황에서는 필수로 사용해야 한다.

### 1. Entity/VO에서 적절하지 않은 함수

도메인 내의 함수 중 Entity나 VO의 자연스러운 책임이 아닌 경우 독립된 인터페이스로서 서비스로 선언된 operation model을 선언한다.  
그러니까 Aggregate이나 VO에서 수행되어야 하는 **operation이 각 Aggregate/VO의 함수로 적절하지 않다고 느껴질 때**가 도메인 서비스를 사용할 때이다.  

대표적인 경우는 함수로 부적절하다고 느껴질 때 **static method를 생성하는** 경향이 있다.  
이런 경우를 Vaughn Vernon은 **냄새나는 코드**라고 표현했다. 도메인 서비스를 써야한다는 냄새!

<div class="code-example" markdown="1" style="font-size: 0.8em">
예시
{: .label .label-yellow}  

최근에 VO에 추가한 static method가 생각이 났다.  

```java
public class CountVo {
    // ...

    public static CountVo add(CountVo augend, CountVo addend) {
        return new CountVo(augend.imageCount + addend.imageCount, augend.videoCount + addend.videoCount);
    }
}
```

위와 같은 코드가 들어갔는데, CountVo에 대한 로직을 CountVo가 갖도록하기 위함이었다.  
나는 반대했던 코드인데 뭔가 이상했기 때문이다.  
이 책을 보면서 명확한 것은 이런 **이상한 느낌(책에서 말하는 냄새나는?)**이 도메인 서비스를 써야한다는 신호인 것 같다.
</div>


### 2. domain 로직이 밖으로 유출되는 경우

**domain 로직은 domain 영역 밖으로는 절대로 유출되서는 안된다**.  
즉, client로 유출되서는 안된다는 말이다. 심지어 client가 application service라고 할지라도.
- client의 책임은 모든 세부사항을 다루는 domain operation을 호출하는 역할 뿐이다.

여기서 절대로의 의미는 **아주 당연하다고 생각되는 작은 로직도 비즈니스 로직이면 application service에 존재해서는 안된다**는 말이다.  
- 예를 들면 위와 같이 값을 더하는 단순 덧셈 연산 로직일지라도.
- application은 이 domain 로직(덧셈 연산)을 요청할 책임이 있는 것.



## 도메인 서비스가 아닌 경우

무엇보다 중요한 것은 domain service가 과하면 안된다는 것이다.  
적절한 상황에만 service로 domain 로직을 모델링 해야지, 지나치게 되면 domain 로직이 Entity와 VO에 흩어지지 못하고 service에만 몰리게 된다.  
- 이건 제대로 모델링 된 domain이라고 할 수 없다.

service라는 단어가 뭔가 거창해보일 수 있다.  
domain service에서 service라는 단어가 들어있다고해서 대단위이거나 원격 기능이 있는 무거운 트랜잭션 오퍼레이션이라는 의미가 아니다.

**아닌 경우**:  
트랜잭션이나 보안은 애플리케이션 서비스내에서 다뤄질 애플리케이션의 문제이지 도메인 서비스에서 다뤄선 안 된다.  
애플리케이션 서비스는 당연히 아니다.  
복잡한 비즈니스 시스템과 상호교류 하도록 해주는 단위의 큰 컴포넌트.



## 도메인 서비스 분리

서비스에 분리된 인터페이스가 있어야 하는지 판단해야 한다.
- 인터페이스 구현체는 domain 영역 밖에 있을 수 있다.

분리된 인터페이스는 반드시 필요한 것은 아니다. 단일 클래스를 사용해도 된다.
- 여기에 대해선 논란이 많다.

java 프로젝트에서 interface를 접두사로 하고 **-impl**을 접미사로 하는 방식이 꽤 보편적이다.
그리고 심지어 같은 package에 위치하기도 한다.
이런 네이밍이라면 인터페이스 분리가 필요가 없다거나 네이밍을 신중하게 생각해야한다는 의미일 수 있다.
**-impl**, **Default-**는 좋지 않다.

여러 특정한 구현을 제공하고 그 구현에 맞게 분리하게 된다면 그에 맞게 이름을 붙여야 한다.
- repository -> mysqlRepository

혹은 의존성 분리를 위해 인터페이스를 나눌 수 있다.



---

## 예제 코드로 이해하기


책에 있는 코드가 domain service를 더 명확하게 이해하게 도와주는 것 같다.

client code

```java
UserDescriptor userDescriptor =
        DomainRegistry
                .authenticationService()
                .authenticate(aTenantId, aUsername, aPassword);
```

service code

```java
package com.saasovation.identityaccess.infrastructure.services;

public class DefaultEncryptionAuthenticationService implements AuthenticationService {
    @Override
    public UserDescriptor authenticate(TenantId aTenantId, String aUsername, String aPassword) {
        if (aTenantId == null) {
            throw new IllegalArgumentException("TenantId must not be null.");
        }
        if (aUsername == null) {
            throw new IllegalArgumentException("Username must not be null.");
        }
        if (aPassword == null) {
            throw new IllegalArgumentException("Password must not be null.");
        }
        UserDescriptor userDescriptor = null;

        Tenant tenant =
                DomainRegistry
                        .tenantRepository()
                        .tenantOfId(aTenantId);
        if (tenant != null && tenant.isActive()) {
            String encryptedPassword =
                    DomainRegistry
                            .encryptionService()
                            .encryptedValue(aPassword);
            User user =
                    DomainRegistry
                            .userRepository()
                            .userFromAuthenticCredentials(
                                    aTenantId,
                                    aUsername,
                                    encryptedPassword);
            if (user != null && user.isEnabled()) {
                userDescriptor = user.userDescriptor();
            }
        }
        return userDescriptor;
    }
}
```

코드에서 배운 점:  
- service가 없다면 client가 tenant, user, encrypt domain을 호출해서 어떻게 인증할지를 알아야 한다.
  - 이건 너무 과하다.
  - 세부 사항은 모두 domain으로 넣어야 한다. 이를 위해 domain service를 사용한다.
- domain service가 필요에 따라 구현체는 다른 package(domain 밖)에 존재할 수 있다.
- 생각한 것보다 많은 부분이 domain service일 수 있다.


### reference

- Implement Domain Driven Design (chapter7 Domain Events), Vaughn Vernon
