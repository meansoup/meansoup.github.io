---
layout: post
title: DDD의 기둥 Ubiquitous Language
sidebar_label: Ubiquitous Language
parent: 전략적 설계
grand_parent: Domain Driven Design
nav_order: 1
permalink: /docs/ddd/strategic/ubiquitous
sitemap:
  lastmod: 2023-12-28
---

*It’s one of the two primary pillars of DDD’s strengths.* - Vaughn Vernon

Vaughn Vernon의 말처럼 유비쿼터스 언어는 DDD의 가장 강력한 요소 중 하나이며 DDD에서 절대 빠질 수 없는 개념이다.  

## 유비쿼터스, Ubiquitous

유비쿼터스라는 단어는 **'어디에나 있다. 아주 흔하다'** 라는 말을 의미한다.  

## 유비쿼터스 언어

유비쿼터스 언어의 의미도 어디에서나 발견되는 언어라는 의미이다.  

그러나 유비쿼터스 언어는 팀 내에 공유된 언어로 **팀 내에서** 어디에서나 발견되는 언어라고 보는 것이 정확하다.  
DDD의 개념은 실제 도메인 모델을 코드에 녹이는 것이기 때문에 도메인의 용어(유비쿼터스 언어)들이 정의되는 것이 중요하기 때문이다.  

따라서 유비쿼터스 언어는 도메인 전문가와 개발자 모두 공유하는 언어이며, 뿐만 아니라 실제로 해당 프로젝트에 참여하는 모든 사람들이 공유하는 언어이다.  
팀 내에서 무슨 역할을 맡더라도 프로젝트에 참여하고 있다면 해당 프로젝트의 유비쿼터스 언어를 사용하게 된다.

## 유비쿼터스 언어의 필요성

도메인에 맞는 소프트웨어를 만들려면 도메인을 설명할 수 있는 방법이 필요하다.  
모델과 모델들의 관계, 이벤트, 비즈니스, 모델의 변화를 설명할 수 있는 방법들이 필요하다.  
이런 설명을 함께 일관되게 사용하기 위해 필요한 것이 유비쿼터스 언어이다.

유비쿼터스 언어를 사용해 비즈니스 개념이나 프로세스를 쉽게 설명할 수 있다면 올바른 방향으로 언어를 결정해나가고 있다고 볼 수 있다.  
반대로 설명에 어려움을 느낀다면 무언가 놓치고 있을 가능성이 높다.


## 유비쿼터스 언어의 특징

유비쿼터스 언어는 팀에 의해 쓰이는 명사, 형용사, 동사, 등의 풍부한 표현을 포함한다.  
팀이 사용하는 모든 문서, 소프트웨어, 테스트는 이 언어를 담고 있으며 이 언어에 맞춰진다.

### 1. 의사소통

팀 내에서 사용하는 용어와 비즈니스 용어를 일치시키고 소프트웨어 모델에 반영한다.  
개발자, 비즈니스 전문가를 포함한 모든 팀원들이 동일한 언어로 의사소통할 수 있다.

### 2. 비즈니스 이해

개발자들이 비즈니스 전문가와 의사소통하며 비즈니스를 이해하는 속도가 향상된다.  
비즈니스 도메인을 더 깊이 이해할 수 있다.

### 3. 도메인 복잡성 해결

유비쿼터스 언어로 생성한 도메인 모델을 통한 추상화로 복잡한 도메인을 더 이해하기 쉽게 만든다.  
역할이 비즈니스 로직에 맞게 명확하게 분리됨을 통해 복잡성이 줄고 이해관계자 간의 이해도를 맞출 수 있다.


## 유비쿼터스 언어를 어떻게 만들까

1. 물리적이고 개념적인 도메인 그림을 그리고 이름과 행동을 붙여보기
2. 간단한 정의로 구성된 용어집 만들기
    - 맘에 들지 않더라도 용어집 쓰기. 용어집을 씀으로써 추가적인 용어와 구문을 언어로 끄집어낼 수 있다.
3. 일부 팀원이 작성했다면 만들어진 구문을 리뷰하고 동의하지 못하는 경우가 많으므로 변경이 발생하더라도 대응할 수 있게 준비하기

유비쿼터스 언어를 만드는 것은 도메인 모델을 만드는 것과도 관련이 있다.  
도메인 모델을 만들 때 프로젝트를 위해 가장 좋은 언어를 완성하기 위해 합의와 타협을 거치며 토론하고 논쟁한다. 때로는 흥정할 수도 있다.  
기존 문서의 참고, 비즈니스 지식의 공유, 기술 표준, 어학 사전들을 참조하는 과정도 지난다.  
**가장 좋은 개념과 용어와 의미가 무엇인지**에만 초점을 맞춘다.


## 유비쿼터스 언어 주의사항

보편적으로 사용되고 흔히 보이는 유비쿼터스 언어라는 의미가 **엔터프라이즈 전체나 전사적인, 혹은 세계적이거나 보편적인 도메인 언어라는 의미는 아니다**.  

컨텍스트는 생각보다 작고, 컨텍스트 당 하나의 유비쿼터스 언어가 있다.  
유비쿼터스 언어는 바운디드 컨텍스트를 격리시키고 그 안에서 프로젝트를 진행하는 팀 내에서만 유비쿼터스하다.  

그러므로 전체 엔터프라이즈나 다른 팀 같이 넓은 범위에서 유비쿼터스 언어를 적용하려고 하면 성공할 수 없고 적절하지 않다.  

**격리된 컨텍스트 상에서 합의된 유비쿼터스 언어가 아닌 모든 개념을 거부하라.** 라고 표현하는데, 이는 모든 도메인 용어들을 합의한 유비쿼터스 언어로 만들자는 말과 동시에 다른 컨텍스트의 유비쿼터스 언어가 합의 없이 침범할 수 없음을 의미한다.


## 유비쿼터스 언어의 변화

언어는 시간이 지남에 따라 크고 작은 변화를 겪으면서 확장되고 변화한다.  
언어처럼 유비쿼터스 언어도 성장하고 변화한다.  

그렇기 때문에 처음 유비쿼터스 언어를 만드는데 영감을 주었던 결과물들은 시간이 지나면서 쓸모 없어질 가능성이 매우 크다.  
그렇기 때문에 결국 유비쿼터스 언어가 가장 지속적으로 유지되고 보장되는 것은 팀원간의 이야기와 코드상의 모델이다.  
**팀원간의 이야기와 코드가 유비쿼터스 언어의 영속적인 발현**이기 때문에 이야기 속의 유비쿼터스 언어에 맞춰 결과물들(그림, 용어집 등의 문서)를 업데이트하기 어렵다면 버릴 수 있어야 한다.  
모든 문서를 최신으로 동기화하는 것이 현실적으로 어렵기 때문에 이편이 실용적이며 죄책감을 느낄 필요가 없다.  


## 코드레벨에서의 유비쿼터스 언어

| Possible Viewpoints                                                                            | Result Code                                                                                               |
|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| "Who cares? Just code it up." <br>Um, not even close.                             | `patient.setShotType(ShotTypes.TYPE_FLU);` <br>`patient.setDose (dose);` <br>`patient.setNurse(nurse);`   |
| "We give flu shots to patients."  <br>Better, but misses some important concepts. | `patient.giveFlushot();`                                                                                  |
| "Nurses administer flu vaccines to patients in standard doses." <br> This seems like what we’d like to run with at this time, at least until we learn more.             | `Vaccine vaccine = vaccines.standardAdultFluDose();` <br> `nurse.administerFluVaccine(patient, vaccine);` |

유비쿼터스 언어를 코드레벨에서 적용하는 생각들에 많이 미흡했던 것 같다.  
나는 보통 유비쿼터스 언어를 뽑아서 도메인 모델을 만드는데 의의를 많이 뒀었는데, 이번에 다시 *Vaughn Vernon*의 책을 읽으면서 느낀건 위처럼 코드레벨에서 유비쿼터스 언어를 더 고민할 필요가 있다는 것.  


### reference

- Implement Domain Driven Design, Vaughn Vernon
- https://vaadin.com/blog/ddd-part-1-strategic-domain-driven-design
