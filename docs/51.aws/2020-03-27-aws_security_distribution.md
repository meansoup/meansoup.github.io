---
layout: post
title: 보안, 배포
sidebar_label: 보안, 배포
tag:
  - AWS
parent: aws
permalink: /docs/aws/security-deploy
sitemap:
  lastmod: 2020-03-27
---

##  애플리케이션 보안
통신에 대한 암호화는 Http protocol을 통해 할 수 있다.  
암호화에 필요한 키(SSL에서는 인증서)를 가지고 암호화/복호화를 진행한다.  

AWS Certificates Manager를 통해서 인증서를 쉽게 배포하고 관리할 수 있다.  

###  AWS Secrets Manager
Secrets Manager를 통해 수명 주기 전체에서 DB 자격 증명, API키 및 기타 암호를 교체 관리 검색한다.    
코드 상에 userid와 pw를 적는 것이 아니라, secrets Manager에 값을 적어두고 Secrets Manager에서 그 값을 가져와서 사용하도록 하는 방식이다.  
따라서 암호를 보호하고 유출을 막을 수 있다.

###  STS (Security Token Service)
어플리케이션에서 임시 키를 생성하는데 사용되는 서비스.  
IAM을 인증할때는 액세스키/보안키를 사용하지 않고 Security Token Service를 통한 임시 액세스키/보안키를 사용하는 것이 좋다.  
임시 키 발급을 요청한 사용자의 IAM 정책을 사용해서 권한을 제어한다.  
키를 만들면서 Role을 만들고 Role에 권한을 부여하여 해당 Role로 임시 키를 발급받을 수 있다.(Assume role) 이를 통해 사용자의 권한 전체를 부여하는게 아니라 일부 서비스만 권한을 줄 수 있다.  

STS 자격 증명 브로커를 사용할 수 있다.  
1. 사용자가 자격 증명 브로커에 엑서스를 요청
2. 자격 증명 브로커가 별도의 자격 증명 스토어를 통해 확인(예를 들면 회사 사람인지를 확인)
3. 자격 증명 브로커가 STS에 키를 요청
4. 받은 키로 AWS에 접근

###  Cognito
Amazon Cognito를 통해 다양한 기기에서 사용자 데이터 저장 및 동기화를 허용할 수 있다.  
외부 공급자(Google, Amazon, Facebook)로 인증 후 액세스할 수 있다. (이후 Congnito가 STS에 키를 요청)  
자체 인증 시스템을 연동해서 사용할 수도 있다.  

##  애플리케이션 배포
최근 데브옵스 문화로 많은 부분이 자동화되고 개발자가 배포도 같이하고 있다.  

###  IaC (Infrastructure as Code)
복잡한 환경에서의 배포를 해결하는 목적 중 하나이다.  
말 그대로 코드로 인프라를 갖추는 것이다.  
반복 가능하고 자동화된 방식으로 생성될 수 있도록 환경을 정의하고, 코드로 프로덕션 환경을 생성하는 것이다.

AWS에서는 이러한 배포 서비스로 CodeStar를 서비스하고 있다.

###  블루-그린 배포 패턴
기존환경(블루)로 라우팅하다가 신규코드(그린)으로 트래픽을 옮기고 이슈가 되면 다시 블루로 롤백하는 배포 방식이다.  
그린이 안정적이게 되면 블루가 된다.  
문제가 생기면 바로 롤백할 수 있으니 안전한 배포 방식이다.  

**Route53** - Amazon Route53으로 블루 그린 배포패턴을 위한 가중치 기반 트래픽 이동을 쉽게할 수 있다.  
**ELB 활용** - ELB에 블루 인스턴스만 있다가 그린 인스턴스를 추가하고, 블루 인스턴스를 중지 시키는 것.(삭제 아님)  

###  Elastic Beanstalk
AWS Elastic Beanstalk는 EC2, Auto Scaling, ELB 등의 AWS 서비스에 대한 래퍼를 제공하여 배포를 편하게 할 수 있다.