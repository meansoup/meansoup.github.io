---
layout: post
title: container
sidebar_label: container
tag:
  - AWS
parent: aws
permalink: /docs/aws/container
sitemap:
  lastmod: 2020-03-27
---

container란 배포를 쉽게할 수 있는 방법으로 사용한다.  
개발자가 운영팀의 도움 없이도 배포를 할 수 있다.  
개발을 하고 배포하는데 설치/setup 해야하는 작업들이 굉장히 많다. (os/application)

배포 방식의 변화:  
1. os/app 들을 차례대로 설치 - 너무 오래 걸림
2. os와 platform을 image화 하여 copy/paste로 하여 배포 - os 배포 시간과 부팅 시간이 걸림
3. os의 가상화를 이용해 os는 동일하게 사용하고 컨테이너화(app만 독립적으로 동작하도록 쪼개서 파티션화) 함 - app 실행 시간만 걸림

**런타임 엔진**, **코드**, **종속항목** 으로 구성된다.  
서버 > 호스트 OS > 도커 위에 각 컨테이너(Bins/Libs, app)가 올라간다.  

## 도커 컨테이너
도커 컨테이너는 애플리케이션을 실행하는데 필요한 모든 항목(코드, 실행시간, 시스템 도구, 라이브러리 ...)를 포함하고 있는 배포의 표준화된 단위이다.

간편하게 서비스 모델링을 할 수 있다.  
경량, 이식성, 일관성을 갖는다.  
모든 앱 모든 언어에서 사용할 수 있다.  
한 번만 작성하여 패키지화 해두면 어디서든 실행할 수 있다.  
앱을 [마이크로 서비스](https://meansoup.github.io/blog/2020/03/25/aws_terms/#%EB%A7%88%EC%9D%B4%ED%81%AC%EB%A1%9C-%EC%84%9C%EB%B9%84%EC%8A%A4)로 더욱 쉽게 분리할 수 있다.

## 개발 수명 주기
Dockerfile은 컨테이너에 포함되는 구성 요소를 포함하고 있는 파일로, 명령어들로 이루어져 있다.  
Dockerfile을 통해 컨테이너 이미지를 생성하고 이 이미지를 다운 받아서 사용하도록 한다.

## 도커 이미지
도커 이미지는 파일 모음으로 아래와 같은 구조(스택)로 도커 이미지가 구성된다.
> 커널(bootfs) > 기본 이미지(Debian) > 이미지(emacs 추가) > 이미지(Apache 추가) > 컨테이너(쓰기 가능)

지침은 Dockerfile에 저장된다.  
대부분 동일한 os를 기반하여야 한다.  
도커 이미지를 저장하기 위해 amazon ECR/Docker Hub/private repository를 사용할 수 있다.  

## Amazon 컨테이너 서비스
컨테이너가 많아졌을 때는 관리하기가 어려워질 수 있다.  
AWS에서 컨테이너 관련하여 서비스를 제공한다.

**관리** - ECS, EKS (배포/예약/조정 및 관리)  
**호스팅** - EC2, Fargate (Fargate는 EC2를 관리해줌)  
**이미지** - ECR (컨테이너 이미지용 리포지토리)  

**ECS** - 컨테이너의 배포 관리를 도와주는 완전 관리형 컨테이너 조정 서비스.  
**EKS** - k8s를 쉽게 실행할 수 있도록 하는 관리형 서비스.  
**Fargate** - 컨테이너를 실행하기 위해 조정할 필요가 없음. 컨테이너 이미지를 업로드하고 리소스 요구사항을 지정하면 컨테이너를 실행해 준다. ECS와 같이 사용되기도 함.  